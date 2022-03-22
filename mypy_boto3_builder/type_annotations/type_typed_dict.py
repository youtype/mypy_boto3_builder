"""
Wrapper for `typing/typing_extensions.TypedDict` type annotations.
"""
from collections.abc import Iterable, Iterator

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.import_helpers.internal_import_record import InternalImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript


class TypedDictAttribute:
    """
    TypedDict attribute wrapper.

    Arguments:
        name -- Attribute name.
        type_annotation -- Attribute type annotation.
        required -- Whether the attribute has to be set.
    """

    def __init__(self, name: str, type_annotation: FakeAnnotation, required: bool) -> None:
        self.name = name
        self.required = required
        self.type_annotation = type_annotation

    def get_type_annotation(self) -> FakeAnnotation:
        """
        Get wrapped for non-required type annotation or raw type annotation.
        """
        if self.is_required():
            return self.type_annotation

        return TypeSubscript(Type.NotRequired, [self.type_annotation])

    def render(self, parent_name: str = "") -> str:
        """
        Render attribute to use in class-based TypedDict definition.

        Returns:
            A string with argument definition.
        """
        return f'"{self.name}": {self.get_type_annotation().render(parent_name)}'

    def get_types(self) -> set[FakeAnnotation]:
        """
        Get type_annotaion types with `NotRequired` if needed.
        """
        return self.get_type_annotation().get_types()

    def is_required(self) -> bool:
        """
        Whether argument is required.
        """
        return self.required


class TypeTypedDict(FakeAnnotation):
    """
    Wrapper for `typing/typing_extensions.TypedDict` type annotations.

    Arguments:
        name -- Type name.
        children -- Typed dict attributes.
        docstring -- Docstring for render.
        stringify -- Convert type annotation to string to avoid circular deps.
        replace_with_dict -- Render Dict[str, Any] instead to avoid circular dependencies.
    """

    def __init__(
        self,
        name: str,
        children: Iterable[TypedDictAttribute] = (),
        docstring: str = "",
        stringify: bool = False,
        replace_with_dict: Iterable[str] = tuple(),
    ) -> None:
        self.name = name
        self.children = list(children)
        self.docstring = docstring
        self.stringify = stringify
        self.replace_with_dict = set(replace_with_dict)

    def get_sort_key(self) -> str:
        """
        Sort Typed Dicts by name.
        """
        return self.name

    def __hash__(self) -> int:
        children = "".join(i.name for i in self.children)
        hash_str = f"{self.name} {children}"
        return hash(hash_str)

    def get_attribute(self, name: str) -> TypedDictAttribute:
        """
        Find attribute by `name`.

        Arguments:
            name -- Attribute name.

        Returns:
            Found attribute.
        """
        for child in self.children:
            if child.name == name:
                return child

        raise ValueError(f"No child with name {name}")

    def render(self, parent_name: str = "") -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        if parent_name in self.replace_with_dict:
            return Type.DictStrAny.render()

        if self.stringify:
            return f'"{self.name}"'

        if parent_name and parent_name == self.name:
            return f'"{self.name}"'

        return self.name

    @staticmethod
    def get_typing_import_record() -> ImportRecord:
        """
        Get import record required for using TypedDict.

        Fallback to typing_extensions for py38-.
        """
        return ImportRecord(
            ImportString("typing"),
            "TypedDict",
            min_version=(3, 9),
            fallback=ImportRecord(ImportString("typing_extensions"), "TypedDict"),
        )

    def get_import_record(self) -> ImportRecord:
        """
        Get import record required for using type annotation.
        """
        return InternalImportRecord(ServiceModuleName.type_defs, name=self.name)

    def add_attribute(self, name: str, type_annotation: FakeAnnotation, required: bool) -> None:
        """
        Add new attribute to a dictionary.

        Arguments:
            name -- Argument name.
            type_annotation -- Argument type annotation.
            required -- Whether argument has to be set.
        """
        self.children.append(TypedDictAttribute(name, type_annotation, required))

    def is_dict(self) -> bool:
        """
        Always True as it is a TypedDict.
        """
        return True

    def is_typed_dict(self) -> bool:
        """
        Always True as it is a TypedDict.
        """
        return True

    def has_optional(self) -> bool:
        """
        Whether TypedDict has optional keys.
        """
        for child in self.children:
            if not child.is_required():
                return True
        return False

    def has_required(self) -> bool:
        """
        Whether TypedDict has required keys.
        """
        for child in self.children:
            if child.is_required():
                return True
        return False

    def has_both(self) -> bool:
        """
        Whether TypedDict has both optional and required keys.
        """
        return self.has_required() and self.has_optional()

    def get_required(self) -> list[TypedDictAttribute]:
        """
        Get a list of required attributes.
        """
        result: list[TypedDictAttribute] = []
        for child in self.children:
            if child.is_required():
                result.append(child)
        return result

    def get_optional(self) -> list[TypedDictAttribute]:
        """
        Get a list of optional attributes.
        """
        result: list[TypedDictAttribute] = []
        for child in self.children:
            if not child.is_required():
                result.append(child)
        return result

    def copy(self) -> "TypeTypedDict":
        """
        Create a copy of type annotation wrapper.
        """
        return TypeTypedDict(
            self.name,
            list(self.children),
            docstring=self.docstring,
            stringify=self.stringify,
            replace_with_dict=self.replace_with_dict,
        )

    def is_same(self, other: "TypeTypedDict") -> bool:
        """
        Check whether typed dict attributes are the same as `other`.
        """
        children = [i.render() for i in self.children]
        other_children = [i.render() for i in other.children]
        return other_children == children

    def get_children_types(self) -> set[FakeAnnotation]:
        """
        Extract required type annotatyions from attributes.
        """
        result: set[FakeAnnotation] = set()
        for child in self.children:
            result.update(child.get_types())
        return result

    def get_children_typed_dicts(self) -> set["TypeTypedDict"]:
        """
        Extract required TypeTypedDict list from attributes.
        """
        result: set[TypeTypedDict] = set()
        children_types = self.get_children_types()
        for type_annotation in children_types:
            if not isinstance(type_annotation, TypeTypedDict):
                continue
            result.add(type_annotation)

        return result

    def get_children_literals(
        self, processed: Iterable["TypeTypedDict"] = tuple()
    ) -> set[TypeLiteral]:
        """
        Extract required TypeLiteral list from attributes.
        """
        result: set[TypeLiteral] = set()
        if self in processed:
            return result
        children_types = self.get_children_types()
        for type_annotation in children_types:
            if isinstance(type_annotation, TypeLiteral):
                result.add(type_annotation)
            if isinstance(type_annotation, TypeTypedDict):
                result.update(type_annotation.get_children_literals((self, *processed)))
        return result

    def replace_self_references(self) -> None:
        """
        Replace self refenrences with `Dict[str, Any]` to avoid circular dependencies.
        """
        for child in self.get_children_typed_dicts():
            if child is self:
                child.replace_with_dict.add(self.name)
                continue
            for sub_child in child.get_children_typed_dicts():
                if sub_child.replace_with_dict:
                    continue
                if sub_child is self:
                    sub_child.replace_with_dict.add(child.name)
                    continue

    @property
    def requires_safe_render(self) -> bool:
        """
        Whether TypedDict has reserved words and has to be rendered safely.
        """
        return True
        # return any(is_reserved(child.name) for child in self.children)

    def iterate_children(self) -> Iterator[TypedDictAttribute]:
        """
        Iterate over children from required to optional.
        """
        for child in self.get_required():
            yield child
        for child in self.get_optional():
            yield child
