"""
Interactive chat buddy to help user to select services and generate type annotations.

Copyright 2024 Vlad Emelianov
"""

import logging
import sys
from collections.abc import Callable, Sequence
from pathlib import Path

import questionary
from colorama import Fore, Style, just_fix_windows_console
from prompt_toolkit.shortcuts.prompt import CompleteStyle
from prompt_toolkit.validation import ValidationError

from mypy_boto3_builder.cli_parser import CLINamespace
from mypy_boto3_builder.constants import PROG_NAME
from mypy_boto3_builder.enums.output_type import OutputType
from mypy_boto3_builder.enums.product import Product
from mypy_boto3_builder.enums.product_library import ProductLibrary
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils.boto3_utils import get_available_service_names
from mypy_boto3_builder.utils.path import print_path

MAX_SERVICE_PRINTED = 20
MAX_SERVICE_SELECTABLE = 20
DEFAULT_OUTPUT_PATH = Path("./vendored")
REPORT_URL = "https://github.com/youtype/mypy_boto3_builder/issues"
QMARK = "Input:  "
BUILDER_PREFIX = "Builder:"
YOU_PREFIX = "You:    "
PAIR = 2


class ServiceActions:
    """
    Available service actions.
    """

    build = "continue"
    add = "add another service"
    add_all = "add all available services"
    remove = "remove selected service"
    remove_all = "remove all selected services"


class PackageManagerChoices:
    """
    Available package managers.
    """

    pip = "pip"
    poetry = "poetry"
    pipenv = "pipenv"
    uv = "uv"
    unknown = "... I dont' know :("


def _tag(message: str | float, color: str = Fore.CYAN) -> str:
    return f"{color}{Style.BRIGHT}{message}{Style.RESET_ALL}"


def _linebreak() -> None:
    sys.stdout.write("\n")


def _join_and(items: Sequence[str]) -> str:
    if not items:
        return ""
    if len(items) == 1:
        return f"only {items[0]}"
    if len(items) == PAIR:
        return f"{items[0]} and {items[1]}"
    return f"{', '.join(items[:-1])}, and {items[-1]}"


class ChatBuddy:
    """
    Interactive chat buddy to help user to select services and generate type annotations.
    """

    def __init__(self) -> None:
        self.available_service_names: tuple[ServiceName, ...] = ()
        self.selected_service_names: list[ServiceName] = []
        self.initial_service_names: list[ServiceName] = []
        self.product_library = ProductLibrary.boto3
        self.library_name: str = ""
        self.product: Product = Product.types_boto3_custom
        self.output_path: Path = DEFAULT_OUTPUT_PATH
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
        self.package_manager = PackageManagerChoices.pip

    def _get_selected_service_names(self) -> list[ServiceName]:
        return [i for i in self.available_service_names if i.is_essential()]

    @staticmethod
    def _say(message: str) -> None:
        sys.stdout.write(f"{_tag(BUILDER_PREFIX, Fore.MAGENTA)} {message}\n\n")

    def _respond(self, message: str) -> None:
        sys.stdout.write(f"{_tag(YOU_PREFIX, Fore.GREEN)} {message}\n\n")

    def _select_service_name(
        self, message: str, service_names: list[ServiceName]
    ) -> ServiceName | None:
        choices = {f"{i.class_name} ({i.boto3_name})": i for i in service_names}
        lower_choices = {k.lower(): v for k, v in choices.items()}
        lower_choices.update({i.class_name.lower(): i for i in service_names})
        lower_choices.update({i.boto3_name.lower(): i for i in service_names})
        selected_choice: str
        if len(choices) > MAX_SERVICE_SELECTABLE:

            def _validate(choice: str) -> bool:
                if choice and choice.lower() not in lower_choices:
                    raise ValidationError(len(choice), f"{choice} service does not exist")
                return True

            self._say("Start typing service name so I can find it in the list.")
            selected_choice = questionary.autocomplete(
                message=message,
                qmark=QMARK,
                choices=list(choices),
                complete_style=CompleteStyle.COLUMN,
                validate=_validate,
            ).unsafe_ask()
            _linebreak()
        else:
            self._say("Which one?")
            selected_choice = questionary.select(
                message=message,
                qmark=QMARK,
                choices=["nothing, go back", *choices],
            ).unsafe_ask()
            _linebreak()
        if not selected_choice:
            return None
        key = selected_choice.lower()
        return lower_choices.get(key)

    def _is_all_selected(self) -> bool:
        return len(self.selected_service_names) == len(self.available_service_names)

    def _get_services_message(self) -> str:
        selected = self.selected_service_names
        if self._is_all_selected():
            return (
                f"Do you want type annotations for {_tag('ALL')} available services?"
                f" It will take {_tag('10-20 minutes')}!"
            )
        if not selected:
            return f"Okay, what service do you want to {_tag('add')}?"

        if len(selected) == 1:
            return (
                f"Should we build type annotations only for {_tag(selected[0].class_name)} service?"
            )

        if len(selected) > MAX_SERVICE_PRINTED:
            selected_strs = [
                *(_tag(i.class_name) for i in selected[: MAX_SERVICE_PRINTED - 1]),
                f"{_tag(len(selected) - MAX_SERVICE_PRINTED + 1)} other",
            ]
        else:
            selected_strs = [_tag(i.class_name) for i in selected]
        selected_str = _join_and(selected_strs)
        return f"Do you use {selected_str} services?"

    def _select_library(self) -> ProductLibrary | None:
        library_choices = {
            "boto3": ProductLibrary.boto3,
            "aiobotocore": ProductLibrary.aiobotocore,
            "aioboto3": ProductLibrary.aioboto3,
            "boto3 (legacy boto3-stubs)": ProductLibrary.boto3_legacy,
            "none of them": None,
        }
        selected = questionary.select(
            "My project uses",
            qmark=QMARK,
            choices=list(library_choices),
            default=ProductLibrary.boto3.value,
        ).unsafe_ask()
        _linebreak()
        return library_choices[selected]

    def _select_product(self) -> Product:
        product_map = {
            ProductLibrary.boto3: Product.types_boto3_custom,
            ProductLibrary.boto3_legacy: Product.boto3_custom,
            ProductLibrary.aiobotocore: Product.aiobotocore_custom,
            ProductLibrary.aioboto3: Product.aioboto3_custom,
        }
        return product_map[self.product_library]

    def _select_services(self) -> list[ServiceName]:
        result = self.selected_service_names
        while True:
            self._say(self._get_services_message())
            response_choices = list(
                filter(
                    None,
                    [
                        ServiceActions.build if result else None,
                        ServiceActions.add if not self._is_all_selected() else None,
                        ServiceActions.add_all if not self._is_all_selected() else None,
                        ServiceActions.remove if result else None,
                        ServiceActions.remove_all if result else None,
                    ],
                )
            )
            response = questionary.select(
                "Let's",
                qmark=QMARK,
                choices=response_choices,
                default=response_choices[0],
            ).unsafe_ask()
            _linebreak()
            match response:
                case ServiceActions.build:
                    return result
                case ServiceActions.add:
                    result_set = set(result)
                    choice_service_names = [
                        i for i in self.available_service_names if i not in result_set
                    ]
                    message = "I use" if not result else "I also use"
                    service_name = self._select_service_name(message, choice_service_names)
                    if service_name is None:
                        continue
                    result.append(service_name)
                    continue
                case ServiceActions.add_all:
                    result.clear()
                    result.extend(self.available_service_names)
                    continue
                case ServiceActions.remove:
                    service_name = self._select_service_name("I do not use", result)
                    if service_name is None:
                        continue
                    result.remove(service_name)
                    continue
                case ServiceActions.remove_all:
                    result.clear()
                    continue
                case _:
                    return result

    def _get_service_names_args(self) -> list[str]:
        if self._is_all_selected():
            return ["all"]
        return [i.name for i in self.selected_service_names]

    def _get_install_cmd(self, whl_path: Path) -> str:
        if self.package_manager == PackageManagerChoices.uv:
            return f"uv add --dev {whl_path}"
        if self.package_manager == PackageManagerChoices.pip:
            return f"pip install {whl_path}"
        if self.package_manager == PackageManagerChoices.poetry:
            return f"poetry add -G dev {whl_path}"
        if self.package_manager == PackageManagerChoices.pipenv:
            return f"pipenv install --dev {whl_path}"

        return f"pip install {whl_path}"

    def _find_last_whl(self) -> Path | None:
        prefix = self.product_library.get_package_prefix()
        packages = list(self.output_path.glob(f"{prefix}*.whl"))
        if not packages:
            return None

        packages.sort(key=lambda x: x.name)
        return packages[-1]

    def _say_commands(self) -> None:
        cmd = " ".join(self.args.to_cmd())
        lines = [
            f"# generate {self.library_name} services",
            cmd,
        ]
        found_whl = self._find_last_whl()
        if found_whl:
            lines.extend(
                (
                    "",
                    f"# install with {self.package_manager}",
                    self._get_install_cmd(found_whl),
                )
            )
        lines_indent = (f"  {line}" if line else "" for line in lines)
        self._say(f"\n\n{'\n'.join(lines_indent)}\n")

    def _select_package_manager(self) -> str:
        result = questionary.select(
            "My package manager is",
            qmark=QMARK,
            choices=[
                PackageManagerChoices.uv,
                PackageManagerChoices.pip,
                PackageManagerChoices.poetry,
                PackageManagerChoices.pipenv,
                PackageManagerChoices.unknown,
            ],
            default=PackageManagerChoices.uv,
        ).unsafe_ask()
        _linebreak()
        if result == PackageManagerChoices.unknown:
            self._say("Then let's use pip to install the package.")
            return PackageManagerChoices.pip

        return result

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
        return response

    def _get_response_services(self) -> str:
        if self._is_all_selected():
            return "Let's include all the services. Just in case. I might need them later."

        if self.selected_service_names == self.initial_service_names:
            return "Looks good. I use the most popular services."

        services_str = _join_and([i.class_name for i in self.selected_service_names])
        return f"Yes, I use {services_str} services."

    def run(self, run_builder: Callable[[CLINamespace], None]) -> None:  # noqa: PLR0915
        """
        Run chat buddy.
        """
        just_fix_windows_console()
        self._say(f"Hello from {_tag(PROG_NAME)}!")
        self._say(
            f"It looks like you plan to add {_tag('boto3')}, {_tag('aioboto3')},"
            f" or {_tag('aiobotocore')} type annotations to your project."
        )
        self._say(
            f"You launched me with no {_tag('OUTPUT_PATH')} command-line argument,"
            f" so I decided to help you a bit."
        )
        self._say(f"Remember, if anything goes wrong, report to {_tag(REPORT_URL)}")
        self._say(f"First of all, what {_tag('AWS SDK library')} do you use?")
        product_library = self._select_library()
        if not product_library:
            self._respond("No, I do not use any of these libraries.")
            self._say("No worries, you can always run me again if you start using them.")
            self._finish()
            return

        self.product_library = product_library
        self.library_name = self.product_library.get_library_name()
        self._respond(
            f"I use {_tag(self.library_name)} in this project."
            f" Now, how to build {_tag('type annotations')} for it?"
        )

        self.product = self._select_product()

        self._say(
            f"Just a sec! I am fetching all available services for {_tag(self.library_name)}..."
        )
        self.available_service_names = tuple(get_available_service_names())
        self.initial_service_names = self._get_selected_service_names()
        self.selected_service_names = list(self.initial_service_names)
        self._say("Thanks for waiting!")
        self._say(
            f"There are {_tag(len(self.available_service_names))} supported services"
            f" for {_tag(self.library_name)}."
            " However, most projects use only"
            f" {_tag(len(self.selected_service_names))} of them."
            " Let me know if you use any other services."
        )
        self.selected_service_names = self._select_services()
        self._respond(self._get_response_services())

        if len(self.selected_service_names) == 1:
            services_str = f"{_tag(self.selected_service_names[0].class_name)} service support"
        else:
            services_str = f"{_tag(len(self.selected_service_names))} services support"

        self._say(
            f"Great! Now I am ready to generate type annotations for {_tag(self.library_name)}"
            f" with {services_str}."
        )
        self._say(
            f"Almost forgot... Where should I put a generated {_tag(self.product.value)} package?"
        )
        self._say(
            f"I prefer to use {_tag(print_path(self.output_path))} directory,"
            " but it is up to you."
        )
        self.output_path = self._select_output_path()
        self._respond(
            f"Save the package in {_tag(print_path(self.output_path))}."
            f" I might even add it to {_tag('git')}!"
        )

        self.args = self._get_cli_namespace()

        self._say(f"Got it! I can start building {_tag(self.product.value)} now if you want.")
        if not self._do_start_building():
            self._respond("No, I just want to check how to do it.")
            self._say(f"No worries, you can always build {_tag(self.product.value)} later!")
            self._say_commands()
            self._finish()
            return

        self._respond("Go for it!")
        run_builder(self.args)
        _linebreak()

        found_whl = self._find_last_whl()
        if not found_whl:
            self._say(
                "All done! But I could not find a built wheel. Something went wrong."
                f" Please report: {_tag(REPORT_URL)}"
            )
            self._say_commands()
            self._finish()
            return

        self._say(f"I have built {_tag(print_path(found_whl))}, and it is ready to install.")

        self._say(
            f"Let me know what {_tag('package manager')} you use."
            f" I can recommend {_tag('uv')}, because it is extremely fast."
            " But you can choose any other."
        )
        self.package_manager = self._select_package_manager()
        self._respond(
            f"Sure, I use {_tag(self.package_manager)}. How to install the generated package?"
        )

        self._say(
            f"Use these commands to {_tag('update')}"
            f" and {_tag('install')} {_tag(self.product.value)}"
            f" when you bump {_tag(self.library_name)} version:"
        )
        self._say_commands()
        self._finish()

    def _finish(self) -> None:
        self._say("Bye-bye! Have a nice day!")
