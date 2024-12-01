"""
Interactive chat buddy to help user to select services and generate type annotations.

Copyright 2024 Vlad Emelianov
"""

import logging
import sys
from collections.abc import Callable
from pathlib import Path

import questionary
from colorama import Fore, Style, just_fix_windows_console
from prompt_toolkit.validation import ValidationError

from mypy_boto3_builder.cli_parser import CLINamespace
from mypy_boto3_builder.constants import PROG_NAME
from mypy_boto3_builder.enums.output_type import OutputType
from mypy_boto3_builder.enums.product import Product
from mypy_boto3_builder.enums.product_library import ProductLibrary
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils.boto3_utils import get_available_service_names
from mypy_boto3_builder.utils.path import print_path

MAX_SERVICE_PRINTED = 10
MAX_SERVICE_SELECTABLE = 10
DEFAULT_OUTPUT_PATH = Path("./vendored")
REPORT_URL = "https://github.com/youtype/mypy_boto3_builder/issues"


class ServiceActions:
    """
    Available service actions.
    """

    build = "Let's build!"
    add = "Select another service"
    add_all = "Select all available services"
    remove = "Remove selected service"
    remove_all = "Remove all selected services"


class PackageManagerChoices:
    """
    Available package managers.
    """

    pip = "pip"
    poetry = "poetry"
    pipenv = "pipenv"
    uv = "uv"
    unknown = "I dont' know :("


def _tag(message: str | float) -> str:
    return f"{Fore.CYAN}{Style.BRIGHT}{message}{Style.RESET_ALL}"


def _quote(message: str, name: str = "Builder") -> str:
    return f"{Fore.MAGENTA}{Style.BRIGHT}{name}:{Style.RESET_ALL}{Fore.RESET} {message}"


class ChatBuddy:
    """
    Interactive chat buddy to help user to select services and generate type annotations.
    """

    def __init__(self) -> None:
        self.available_service_names: tuple[ServiceName, ...] = ()
        self.selected_service_names: list[ServiceName] = []
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
        sys.stdout.write(f"{_quote(message)}\n")

    def _select_service_name(
        self, title_suffix: str, service_names: list[ServiceName]
    ) -> ServiceName | None:
        choices = {i.class_name: i for i in service_names}
        lower_choices = {k.lower(): v for k, v in choices.items()}
        selected_choice: str
        if len(choices) > MAX_SERVICE_SELECTABLE:

            def _validate(choice: str) -> bool:
                if choice and choice.lower() not in lower_choices:
                    raise ValidationError(len(choice), f"{choice} service does not exist")
                return True

            selected_choice = questionary.autocomplete(
                f"Enter service name {title_suffix}",
                choices=list(choices),
                validate=_validate,
            ).unsafe_ask()
        else:
            selected_choice = questionary.select(
                f"Select service {title_suffix}",
                choices=["<< Go back", *choices],
            ).unsafe_ask()
        if not selected_choice:
            return None
        key = selected_choice.lower()
        return lower_choices.get(key)

    def _is_all_selected(self) -> bool:
        return len(self.selected_service_names) == len(self.available_service_names)

    def _get_services_message(self) -> str:
        selected = self.selected_service_names
        if self._is_all_selected():
            selected_str = f"{_tag('ALL')} are selected"
        elif not selected:
            selected_str = f"{_tag('NONE')} selected"
        else:
            selected_str = ", ".join(
                _tag(service_name.class_name)
                if index < MAX_SERVICE_PRINTED
                else f"and {_tag(len(selected) - MAX_SERVICE_PRINTED)} other"
                for (index, service_name) in enumerate(selected[: MAX_SERVICE_PRINTED + 1])
            )
            selected_str = f"{selected_str} {'are' if len(selected) > 1 else 'is'} selected"
        return (
            f"From {_tag(len(self.available_service_names))} available"
            f" {_tag(self.product_library.value)} services {selected_str}."
        )

    def _select_library(self) -> ProductLibrary:
        library_choices = {
            "boto3": ProductLibrary.boto3,
            "aiobotocore": ProductLibrary.aiobotocore,
            "aioboto3": ProductLibrary.aioboto3,
            "boto3 (legacy boto3-stubs)": ProductLibrary.boto3_legacy,
        }
        selected = questionary.select(
            "",
            choices=list(library_choices),
            default=ProductLibrary.boto3.value,
        ).unsafe_ask()
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
                message="What do you want to do?",
                choices=response_choices,
                default=response_choices[0],
            ).unsafe_ask()
            match response:
                case ServiceActions.build:
                    return result
                case ServiceActions.add:
                    result_set = set(result)
                    choice_service_names = [
                        i for i in self.available_service_names if i not in result_set
                    ]
                    service_name = self._select_service_name("to add", choice_service_names)
                    if service_name is None:
                        continue
                    result.append(service_name)
                    continue
                case ServiceActions.add_all:
                    result.clear()
                    result.extend(self.available_service_names)
                    continue
                case ServiceActions.remove:
                    service_name = self._select_service_name("to remove", result)
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
            "",
            choices=[
                PackageManagerChoices.uv,
                PackageManagerChoices.pip,
                PackageManagerChoices.poetry,
                PackageManagerChoices.pipenv,
                PackageManagerChoices.unknown,
            ],
            default=PackageManagerChoices.uv,
        ).unsafe_ask()
        if result == PackageManagerChoices.unknown:
            return PackageManagerChoices.pip

        return result

    def _select_output_path(self) -> Path:
        def _validate(path: Path | None) -> bool:
            if not path:
                raise ValidationError(0, "Path should not be empty")
            return True

        return Path(
            questionary.path(
                "Path to output directory",
                default=DEFAULT_OUTPUT_PATH.as_posix(),
                validate=_validate,
            ).unsafe_ask()
        )

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
        return questionary.confirm(f"Start building {self.product.value}?").unsafe_ask()

    def run(self, run_builder: Callable[[CLINamespace], None]) -> None:
        """
        Run chat buddy.
        """
        just_fix_windows_console()
        self._say(f"Hello and welcome to {_tag(PROG_NAME)}!")
        self._say(
            f"It looks like you want to add {_tag('type annotations')} to your project,"
            " but you launched me with no command-line arguments. So I decided to help you a bit!"
        )
        self._say(f"Remember, if anything goes wrong, report to {_tag(REPORT_URL)}")
        self._say(f"First of all, what {_tag('AWS SDK library')} do you use?")
        self.product_library = self._select_library()

        self.product = self._select_product()

        self.library_name = self.product_library.get_library_name()
        self._say(
            "Good choice! Hold on, I am fetching all available services for"
            f" {_tag(self.library_name)}..."
        )
        self.available_service_names = tuple(get_available_service_names())
        self.selected_service_names = self._get_selected_service_names()
        self._say(
            f"Found {_tag(len(self.available_service_names))} services"
            f" for {_tag(self.library_name)}. However, most projects use only"
            f" {_tag(len(self.selected_service_names))} of them."
            " Let me know if you use any other services or want to remove some."
        )
        self.selected_service_names = self._select_services()

        self._say(
            f"Great! Now I am ready to generate type annotations for {_tag(self.library_name)}"
            f" with {_tag(len(self.selected_service_names))} included services."
        )
        self._say(
            "One more thing."
            f" Where should I put a generated {_tag(self.product.value)} package?"
            f" I prefer to use {_tag(print_path(self.output_path))} directory,"
            " but you can change it."
        )
        self.output_path = self._select_output_path()

        self.args = self._get_cli_namespace()

        self._say(f"Got it! I can start building {_tag(self.product.value)} now if you want.")
        if not self._do_start_building():
            self._say(f"No worries, you can always build {_tag(self.product.value)} later!")
            self._say_commands()
            self._finish()
            return

        run_builder(self.args)

        found_whl = self._find_last_whl()
        if not found_whl:
            self._say(
                "All done! But I could not find a built wheel. Something went wrong."
                f" Please report: {_tag(REPORT_URL)}"
            )
            self._say_commands()
            self._finish()
            return

        self._say(f"All done! I have built {_tag(print_path(found_whl))}. Let's install it!")

        self._say(
            f"Let me know what {_tag('package manager')} you use."
            f" I can recommend {_tag('uv')}, because it is the best."
            " But you can choose any other."
        )
        self.package_manager = self._select_package_manager()

        self._say(
            f"All done! Use this commands to {_tag('update')}"
            f" and {_tag('install')} {_tag(self.product.value)}"
            f" when you bump {_tag(self.library_name)} version:"
        )
        self._say_commands()
        self._finish()

    def _finish(self) -> None:
        self._say("Bye-bye! Have a nice day!")
