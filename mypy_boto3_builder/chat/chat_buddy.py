"""
Interactive chat buddy to help user to select services and generate type annotations.

Copyright 2024 Vlad Emelianov
"""

import logging
import sys
from collections.abc import Callable, Sequence
from enum import Enum
from pathlib import Path
from typing import Final

import questionary
from prompt_toolkit.shortcuts.prompt import CompleteStyle
from prompt_toolkit.validation import ValidationError

from mypy_boto3_builder.chat.chat import Chat, Choice
from mypy_boto3_builder.chat.text_style import TextStyle
from mypy_boto3_builder.chat.type_defs import Message
from mypy_boto3_builder.cli_parser import CLINamespace
from mypy_boto3_builder.constants import PROG_NAME
from mypy_boto3_builder.enums.output_type import OutputType
from mypy_boto3_builder.enums.product import Product
from mypy_boto3_builder.enums.product_library import ProductLibrary
from mypy_boto3_builder.package_data import (
    Boto3StubsCustomPackageData,
    TypesAioBoto3CustomPackageData,
    TypesAioBotocoreCustomPackageData,
    TypesBoto3CustomPackageData,
)
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils.boto3_utils import get_available_service_names
from mypy_boto3_builder.utils.path import print_path
from mypy_boto3_builder.utils.version_getters import get_botocore_version

MAX_SERVICE_PRINTED = 20
MAX_SERVICE_SELECTABLE = 20
MAX_SERVICE_PYCHARM = 20
DEFAULT_OUTPUT_PATH = Path("./vendored")
REPORT_URL = "https://github.com/youtype/mypy_boto3_builder/issues"
QMARK = "Input:"
BUILDER_PREFIX = "NotAI:"
YOU_PREFIX = "You:  "
PAIR = 2
PROJECT_PATH = Path.cwd()


class ServiceActions:
    """
    Available service actions.
    """

    build = "continue"
    add = "add another service"
    add_all = "add all available services"
    recommended = "add only recommended services"
    remove = "remove selected service"
    remove_all = "remove all selected services"


class PackageManager(Enum):
    """
    Available package managers.
    """

    pip = "pip"
    uv = "uv"
    poetry = "poetry"
    pipenv = "pipenv"


# def _tag(message: str | float, color: str = Fore.CYAN, style: str = Style.BRIGHT) -> str:
#     return f"{color}{style}{message}{Style.RESET_ALL}{Fore.RESET}"


def _tag(message: str | float) -> tuple[TextStyle, str]:
    return (TextStyle.tag, str(message))


# def _gray(message: str | float, color: str = Fore.WHITE) -> str:
#     return _tag(message, color, Style.DIM)


def _linebreak() -> None:
    sys.stdout.write("\n")


def _stringify(service_name: ServiceName) -> str:
    return f"{service_name.class_name} ({service_name.boto3_name})"


# def _typewrite(message: str) -> None:
#     words = message.split(" ")
#     for index, word in enumerate(words):
#         if index == len(words) - 1:
#             sys.stdout.write(word)
#             sys.stdout.flush()
#             break

#         sys.stdout.write(f"{word} ")
#         time.sleep(0.02)
#         sys.stdout.flush()


def _join_and(items: Sequence[tuple[TextStyle, str]], name: str = "") -> Message:
    name_suffix = f" {name}{"" if len(items) == 1 else "s"}" if name else ""
    if not items:
        return ("no ", name_suffix)
    if len(items) == 1:
        return ("only ", items[0], name_suffix)
    if len(items) == PAIR:
        return (items[0], " and ", items[1], name_suffix)

    result: Message = []
    for item in items[:-1]:
        result.extend((item, ", "))

    result.extend(("and ", items[-1], name_suffix))
    return result


class ChatBuddy:
    """
    Interactive chat buddy to help user to select services and generate type annotations.
    """

    PRODUCT_MAP: Final = {
        ProductLibrary.boto3: Product.types_boto3_custom,
        ProductLibrary.boto3_legacy: Product.boto3_custom,
        ProductLibrary.aiobotocore: Product.aiobotocore_custom,
        ProductLibrary.aioboto3: Product.aioboto3_custom,
    }

    def __init__(self, run_builder: Callable[[CLINamespace], None]) -> None:
        self.available_service_names: tuple[ServiceName, ...] = ()
        self.available_lookup_map: dict[str, ServiceName] = {}
        self.selected_service_names: list[ServiceName] = []
        self.recommended_service_names: list[ServiceName] = []
        self.product_library = ProductLibrary.boto3
        self.library_name: str = ""
        self.product: Product = Product.types_boto3_custom
        self.output_path: Path = DEFAULT_OUTPUT_PATH
        self.project_path = PROJECT_PATH
        self.args = CLINamespace(
            log_level=logging.ERROR,
            output_path=self.output_path,
            service_names=[],
            build_version="",
            output_types=[OutputType.wheel],
            products=[],
            disable_smart_version=False,
            download_static_stubs=True,
        )
        self.package_manager: PackageManager = PackageManager.pip
        self.run_builder = run_builder
        self.chat = Chat()

    def _get_selected_service_names(self) -> list[ServiceName]:
        return [i for i in self.available_service_names if i.is_essential()]

    def _say(self, *messages: Message | str) -> None:
        for message in messages:
            self.chat.say(message)

    def _respond(self, *messages: Message | str) -> None:
        for message in messages:
            self.chat.respond(message)

    @staticmethod
    def _get_service_lookup_map(service_names: Sequence[ServiceName]) -> dict[str, ServiceName]:
        result = {_stringify(i).lower(): i for i in service_names}
        result.update({i.class_name.lower(): i for i in service_names})
        result.update({i.boto3_name.lower(): i for i in service_names})
        return result

    def _select_service_name(
        self,
        message: str,
        service_names: list[ServiceName],
        go_back_message: str,
    ) -> ServiceName | None:
        choices = {f"{i.class_name} ({i.boto3_name})": i for i in service_names}
        lookup_choices = self._get_service_lookup_map(service_names)
        selected_choice: str
        if len(choices) > MAX_SERVICE_SELECTABLE:

            def _validate(choice: str) -> bool:
                if not choice:
                    return True
                if choice.lower() in lookup_choices:
                    return True

                available_service_name = self.available_lookup_map.get(choice.lower())
                if not available_service_name:
                    raise ValidationError(len(choice), f"{choice} service does not exist")

                if available_service_name in self.selected_service_names:
                    raise ValidationError(
                        len(choice),
                        f"{_stringify(available_service_name)} service is already selected",
                    )

                raise ValidationError(
                    len(choice),
                    f"{_stringify(available_service_name)} service is already removed",
                )

            self._say(
                (
                    "Start typing ",
                    _tag("service name"),
                    " so I can find it in the list. Leave the input ",
                    _tag("empty"),
                    " and press ",
                    _tag("Enter"),
                    " to continue.",
                )
            )
            selected_choice = questionary.autocomplete(
                message=message,
                qmark=QMARK,
                choices=list(choices),
                complete_style=CompleteStyle.COLUMN,
                validate=_validate,
            ).unsafe_ask()
            _linebreak()
        else:
            selected_choice = questionary.select(
                message=message,
                qmark=QMARK,
                default=go_back_message,
                choices=[go_back_message, *choices],
            ).unsafe_ask()
            _linebreak()
        if not selected_choice:
            return None
        key = selected_choice.lower()
        return lookup_choices.get(key)

    def _add_service_names(self) -> None:
        selected_set = set(self.selected_service_names)
        message = "I use"
        while True:
            choice_service_names = [
                i for i in self.available_service_names if i not in selected_set
            ]
            selected_service_name = self._select_service_name(
                message=message,
                service_names=choice_service_names,
                go_back_message="all of the above. Continue.",
            )
            if not selected_service_name:
                break

            self.selected_service_names.append(selected_service_name)
            selected_set.add(selected_service_name)
            self._say(*self._get_services_messages())

    def _remove_service_names(self) -> None:
        service_choices = [
            Choice(
                f"{i.class_name} ({i.boto3_name})",
                i.class_name,
                (
                    f"{i.class_name} ({i.boto3_name})",
                    i.name.lower(),
                    i.class_name.lower(),
                    f"{i.class_name} ({i.boto3_name})".lower(),
                ),
            )
            for i in self.selected_service_names
        ]
        service_choice_map = {
            f"{i.class_name} ({i.boto3_name})": i for i in self.selected_service_names
        }
        selected = self._select_multiple(
            message="I do not use",
            choices=service_choices,
            finish=Choice("Anything else (go back)", "anything else"),
            finish_selected=Choice("Anything else (go back)", ""),
            erase_when_done=False,
        )
        selected_services = [service_choice_map[i] for i in selected]
        for selected_service_name in selected_services:
            self.selected_service_names.remove(selected_service_name)

    def _is_all_selected(self) -> bool:
        return len(self.selected_service_names) == len(self.available_service_names)

    def _get_selected_services_message(self) -> Message:
        selected = self.selected_service_names
        if not selected:
            return (_tag("no"), " services")
        if self._is_all_selected():
            return (_tag("all"), " ", _tag(len(selected)), " available services")
        if len(selected) > MAX_SERVICE_PRINTED:
            selected_strs = [
                *(_tag(i.class_name) for i in selected[: MAX_SERVICE_PRINTED - 1]),
                _tag(f"{len(selected) - MAX_SERVICE_PRINTED + 1} other"),
            ]
        else:
            selected_strs = [_tag(i.class_name) for i in selected]
        return _join_and(selected_strs, "service")

    def _get_services_messages(self) -> list[Message]:
        selected = self.selected_service_names
        result: list[Message] = []
        if len(self.selected_service_names) > MAX_SERVICE_PYCHARM:
            result.append(
                (
                    "If you use ",
                    _tag("PyCharm"),
                    " select less than ",
                    _tag(MAX_SERVICE_PYCHARM),
                    " services. Otherwise, you may have peroformance issues.",
                )
            )
        if self._is_all_selected():
            result.extend(
                (
                    ("Do you really need type checking for ", _tag("ALL"), " available services?"),
                    (
                        "Building all takes ",
                        _tag("10-20 minutes"),
                        ", and package size is around ",
                        _tag("12 megabytes"),
                        "!",
                    ),
                )
            )
            return result
        if not selected:
            result.append(("Okay, what service do you want to ", _tag("add"), "?"))
            return result

        if len(selected) == 1:
            result.append(
                ("Should I add type checking only for ", _tag(selected[0].class_name), " service?")
            )
            return result

        result.append(("Do you use ", *self._get_selected_services_message(), "?"))
        return result

    def _select(
        self,
        message: str,
        choices: Sequence[Choice | str],
        *,
        default: str | None = None,
        message_end: str = ".",
        erase_when_done: bool = True,
    ) -> str:
        return self.chat.select(
            message=message,
            choices=choices,
            default=default,
            message_end=message_end,
            erase_when_done=erase_when_done,
        )

    def _select_multiple(
        self,
        message: str,
        choices: Sequence[Choice | str],
        *,
        default: str | None = None,
        message_end: str = ".",
        finish: Choice | str = "",
        finish_selected: Choice | str | None = None,
        erase_when_done: bool = True,
    ) -> list[str]:
        return self.chat.select_multiple(
            message=message,
            choices=choices,
            default=default,
            finish=finish,
            finish_selected=finish_selected,
            message_end=message_end,
            erase_when_done=erase_when_done,
        )

    def _select_library(self) -> ProductLibrary | None:
        library_choices = {
            ProductLibrary.boto3.get_chat_choice(): ProductLibrary.boto3,
            ProductLibrary.aiobotocore.get_chat_choice(): ProductLibrary.aiobotocore,
            ProductLibrary.aioboto3.get_chat_choice(): ProductLibrary.aioboto3,
            ProductLibrary.boto3_legacy.get_chat_choice(): ProductLibrary.boto3_legacy,
            "none of them": None,
        }
        selected = self._select(
            "This project uses",
            choices=list(library_choices),
            default=ProductLibrary.boto3.value,
        )
        return library_choices[selected]

    def _select_product(self) -> Product:
        return self.PRODUCT_MAP[self.product_library]

    def _select_services(self) -> list[ServiceName]:
        result = self.selected_service_names
        while True:
            self._say(*self._get_services_messages())
            response_choices = list(
                filter(
                    None,
                    [
                        ServiceActions.build if result else None,
                        ServiceActions.add if not self._is_all_selected() else None,
                        ServiceActions.recommended
                        if self.selected_service_names != self.recommended_service_names
                        else None,
                        ServiceActions.remove if result else None,
                        ServiceActions.add_all if not self._is_all_selected() else None,
                        ServiceActions.remove_all if result else None,
                    ],
                )
            )
            response = self._select(
                message="I want to",
                choices=response_choices,
                erase_when_done=False,
            )
            match response:
                case ServiceActions.build:
                    return result
                case ServiceActions.add:
                    self._add_service_names()
                    continue
                case ServiceActions.add_all:
                    result.clear()
                    result.extend(self.available_service_names)
                    continue
                case ServiceActions.remove:
                    self._remove_service_names()
                    continue
                case ServiceActions.remove_all:
                    result.clear()
                    continue
                case ServiceActions.recommended:
                    result.clear()
                    result.extend(self.recommended_service_names)
                    continue
                case _:
                    return result

    def _get_service_names_args(self) -> list[str]:
        if self._is_all_selected():
            return ["all"]
        return [i.name for i in self.selected_service_names]

    def _get_install_cmd(self, whl_path: Path) -> str:
        match self.package_manager:
            case PackageManager.uv:
                return f"uv add --dev {whl_path}"
            case PackageManager.pip:
                return f"pip install {whl_path}"
            case PackageManager.poetry:
                return f"poetry add -G dev {whl_path}"
            case PackageManager.pipenv:
                return f"pipenv install --dev {whl_path}"

    def _find_last_whl(self) -> Path | None:
        prefix = self.product_library.get_package_prefix()
        packages = list(self.output_path.glob(f"{prefix}*.whl"))
        if not packages:
            return None

        packages.sort(key=lambda x: x.name)
        return packages[-1]

    def _say_commands(self) -> None:
        cmd = " ".join(("uvx", *self.args.to_cmd()))
        lines = [
            (
                TextStyle.dim,
                f"# generate {self.library_name} services",
            ),
            cmd,
        ]
        found_whl = self._find_last_whl()
        if found_whl:
            lines.extend(
                (
                    "",
                    (TextStyle.dim, f"# install with {self.package_manager.value}"),
                    self._get_install_cmd(found_whl),
                )
            )
        lines_indent = (f"  {line}" if line else "" for line in lines)
        self._say(f"\n\n{'\n'.join(lines_indent)}\n")

    def _select_package_manager(self) -> PackageManager:
        choices_map = {i.value: i for i in PackageManager}
        result = questionary.select(
            "My package manager is",
            qmark=QMARK,
            choices=[
                *choices_map,
                "... I dont' know :(",
            ],
        ).unsafe_ask()
        _linebreak()
        if result not in choices_map:
            self._say(("I see... Let's use ", _tag("pip"), " then."))
            return PackageManager.pip

        return choices_map[result]

    def _select_output_path(self) -> Path:
        def _validate(path: Path | None) -> bool:
            if not path:
                raise ValidationError(0, "Path should not be empty")
            return True

        response = questionary.path(
            message="Save package in",
            qmark=QMARK,
            default=DEFAULT_OUTPUT_PATH.as_posix(),
            complete_style=CompleteStyle.READLINE_LIKE,
            validate=_validate,
        ).unsafe_ask()
        _linebreak()
        return Path(response)

    def _get_cli_namespace(self) -> CLINamespace:
        return CLINamespace(
            log_level=logging.INFO,
            output_path=self.output_path,
            service_names=self._get_service_names_args(),
            build_version="",
            output_types=[OutputType.wheel],
            products=[self.product],
            disable_smart_version=False,
            download_static_stubs=True,
        )

    def _do_start_building(self) -> bool:
        response = questionary.confirm(
            message=f"Start building {self.product.value}?",
            qmark=QMARK,
        ).unsafe_ask()
        _linebreak()
        return bool(response)

    def _get_response_services(self) -> Message:
        if self._is_all_selected():
            return (
                "Let's include ",
                _tag("all"),
                " the services. Just in case. I might need them later.",
            )

        if self.selected_service_names == self.recommended_service_names:
            return ("I use only ", _tag("recommended"), " services.")

        return ("Yes, I use ", _tag("selected"), " services.")

    def run(self) -> None:
        """
        Run chat buddy.
        """
        self._say(
            ("Hello from ", _tag(PROG_NAME), "!"),
            (
                "It looks like you plan to add ",
                _tag("type checking"),
                " and ",
                _tag("auto-complete"),
                " for ",
                _tag("boto3"),
                ", ",
                _tag("aioboto3"),
                ", or ",
                _tag("aiobotocore"),
                " to your project in ",
                _tag(print_path(self.project_path)),
                " directory.",
            ),
            (
                "You launched me with no ",
                _tag("OUTPUT_PATH"),
                " command-line argument, so I decided to help you a bit.",
            ),
            (
                "By the way, my author did not add any tests for my code.",
                " So, if anything goes wrong, report to ",
                _tag(REPORT_URL),
            ),
            (
                "First of all, what ",
                _tag("AWS SDK library"),
                " do you use in this project?",
            ),
        )
        product_library = self._select_library()
        if not product_library:
            self._respond("No, I do not use any of these libraries.")
            self._say("No worries, you can always run me again if you start using them.")
            self._finish()
            return

        self.product_library = product_library
        self.library_name = self.product_library.get_library_name()
        self._respond(
            (
                "I use ",
                _tag(self.library_name),
                " in this project.",
                " Now, how can I add ",
                _tag("type checking"),
                " and ",
                _tag("code completion"),
                " for it?",
            )
        )

        self.product = self._select_product()

        botocore_str = f"botocore {get_botocore_version()}"
        self._say(
            (
                "Oh, it is easy. Just a sec, I am fetching all available services for ",
                _tag(self.library_name),
                " from ",
                _tag(botocore_str),
                " shapes...",
            )
        )
        self.available_service_names = tuple(get_available_service_names())
        self.available_lookup_map = self._get_service_lookup_map(self.available_service_names)
        self.recommended_service_names = self._get_selected_service_names()
        self.selected_service_names = list(self.recommended_service_names)
        self._say(
            ("Thanks for waiting!",),
            (
                "There are ",
                _tag(len(self.available_service_names)),
                " supported services for ",
                _tag(self.library_name),
                ".",
            ),
            (
                "However, most projects use only ",
                _tag(len(self.selected_service_names)),
                " so I ",
                _tag("recommend"),
                " adding only them.",
            ),
        )
        self.selected_service_names = self._select_services()
        self._respond(self._get_response_services())

        if len(self.selected_service_names) == 1:
            services_str = (_tag(self.selected_service_names[0].class_name), " service support")
        else:
            services_str = (_tag(len(self.selected_service_names)), " services support")

        self._say(
            (
                "Great! Let's generate type annotations for ",
                _tag(self.library_name),
                " with ",
                *services_str,
                ".",
            )
        )
        package_name = f"{self.product_library.get_package_prefix()}_*.whl"

        self.args = self._get_cli_namespace()

        self._say(("I can start building ", _tag(package_name), " now if you want."))
        if not self._do_start_building():
            self._respond("No, I just want to check how to do it.")
            self._say(("No worries, you can always build ", _tag(self.product.value), " later!"))
            self._say_commands()
            self._finish()
            return

        self._respond("Go for it!")

        self._say(
            ("Almost forgot... Where should I put a generated ", _tag(package_name), " package?"),
            (
                "I prefer to use ",
                _tag(print_path(self.output_path)),
                " directory, but it is up to you.",
            ),
        )
        self.output_path = self._select_output_path()
        self._respond(
            (
                "Save the package in ",
                _tag(print_path(self.output_path)),
                ". I might even add it to ",
                _tag("git"),
                "!",
            )
        )
        self._say(("Good idea! Building to ", _tag(print_path(self.output_path)), " directory..."))
        self._run_builder()

    def _get_documentation_url(self) -> str:
        match self.product:
            case Product.types_boto3_custom:
                return TypesBoto3CustomPackageData.local_doc_link
            case Product.boto3_custom:
                return Boto3StubsCustomPackageData.local_doc_link
            case Product.aiobotocore_custom:
                return TypesAioBotocoreCustomPackageData.local_doc_link
            case Product.aioboto3_custom:
                return TypesAioBoto3CustomPackageData.local_doc_link
            case _:
                return TypesBoto3CustomPackageData.local_doc_link

    def _run_builder(self) -> None:
        self.run_builder(self.args)
        _linebreak()

        found_whl = self._find_last_whl()
        if not found_whl:
            self._say(
                (
                    "All done! But I could not find a built wheel. Something went wrong.",
                    " Please report: ",
                    _tag(REPORT_URL),
                )
            )
            self._say_commands()
            self._finish()
            return

        self._say(
            (
                "I have built ",
                _tag(print_path(found_whl)),
                ", and it is ready to install.",
            ),
            (
                "Let me know which ",
                _tag("package manager"),
                " you use. I can recommend ",
                _tag("uv"),
                ", because it is extremely fast.",
            ),
        )
        self.package_manager = self._select_package_manager()
        self._respond(
            (
                "Sure, I use ",
                _tag(self.package_manager.value),
                ". How to install the generated package?",
            )
        )

        self._say(
            (
                "Use these commands to ",
                _tag("update"),
                " and ",
                _tag("install"),
                " ",
                _tag(self.product.value),
                " when you bump ",
                _tag(self.library_name),
                " version:",
            )
        )
        self._say_commands()
        self._finish()

    def _finish(self) -> None:
        self._say(
            (
                "Check ",
                _tag(self._get_documentation_url()),
                " documentation. It describes all type annotations for ",
                _tag(self.library_name),
                ".",
            ),
            "Bye-bye! Have a nice day!",
        )
