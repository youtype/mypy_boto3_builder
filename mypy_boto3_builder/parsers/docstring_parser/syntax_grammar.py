"""
Pyparsing grammar for request and response syntax.
"""
from pyparsing.core import (
    Combine,
    Forward,
    Group,
    Literal,
    Opt,
    ParserElement,
    SkipTo,
    Word,
    alphanums,
    alphas,
)
from pyparsing.helpers import delimitedList


class SyntaxGrammar:
    """
    Grammar to parse boto3 request/response syntax.

    ellipsis = "..."
    name_value ::= alphanums + "_-."
    string_value ::= alphas{0,2} "'"  [^']+  "'"
    plain_value ::= string_value | name_value
    literal_item ::= list_value | dict_value | set_value | plain_value
    literal_value ::= literal_item ("|" literal_item)+
    any_value ::= literal_value | list_value | dict_value | set_value | union_value | func_call | plain_value
    empty_list_value ::= "[" [ellipsis] [","] "]"
    non_empty_list_value ::= "[" any_value ("," any_value)* [","] "]"
    list_value ::= empty_list_value | non_empty_list_value
    set_value ::= "{" any_value ("," any_value)* [","] "}"
    func_call ::= name_value "(" any_value ("," any_value)* [","] ")"
    empty_dict_value ::= "{" [ellipsis] [","] "}"
    non_empty_dict_value ::= "{" string_value ":" any_value ("," string_value ":" any_value)* [","] "}"
    dict_value ::= empty_dict_value | non_empty_dict_value
    union_item ::= literal_value | list_value | dict_value | set_value | plain_value
    union_value ::= union_item ("or" union_item)+
    argument ::= alphanums "=" any_value
    definition ::= [^']+ "(" argument ("," argument)* [","] ")"
    request_syntax ::= "**Request Syntax**" "::" definition
    response_syntax ::= "**Response Syntax**" "::" (list_value | dict_value)
    """

    ellipsis = Literal("...")
    name_value = Word(alphanums + "_-.")
    string_value = Combine(Opt(Word(alphas, max=2)) + Literal("'") + SkipTo("'") + Literal("'"))
    plain_value = (string_value | name_value).setResultsName("value")
    literal_item = Forward()
    literal_value = (
        Group(literal_item).setResultsName("literal_first_item")
        + Literal("|")
        + delimitedList(Group(literal_item), delim="|").setResultsName("literal_rest_items")
    )
    any_value = Forward()
    empty_list_value = Group(Literal("[") + Opt(ellipsis) + Opt(",") + Literal("]")).setResultsName(
        "empty_list"
    )
    non_empty_list_value = (
        Literal("[")
        + Group(delimitedList(Group(any_value))).setResultsName("list_items")
        + Opt(",")
        + Literal("]")
    )
    list_value = empty_list_value | non_empty_list_value
    set_value = (
        "{" + Group(delimitedList(Group(any_value))).setResultsName("set_items") + Opt(",") + "}"
    )
    func_call = Group(
        name_value.setResultsName("name")
        + Literal("(")
        + Opt(delimitedList(Group(any_value))).setResultsName("args")
        + Opt(",")
        + Literal(")")
    ).setResultsName("func_call")
    empty_dict_value = Group(Literal("{") + Opt(ellipsis) + Opt(",") + Literal("}")).setResultsName(
        "empty_dict"
    )
    non_empty_dict_value = (
        Literal("{")
        + Opt(
            delimitedList(
                Group(
                    string_value.setResultsName("key")
                    + Literal(":").suppress()
                    + Combine(any_value).setResultsName("value")
                )
            ).setResultsName("dict_items")
        )
        + Opt(",")
        + Literal("}")
    )
    dict_value = empty_dict_value | non_empty_dict_value
    literal_item <<= list_value | dict_value | set_value | plain_value
    union_item = literal_value | list_value | dict_value | set_value | plain_value
    union_value = (
        Group(union_item).setResultsName("union_first_item")
        + Literal("or").suppress()
        + delimitedList(
            Group(union_item),
            delim="or",
        ).setResultsName("union_rest_items")
    )
    any_value <<= (
        literal_value | list_value | dict_value | set_value | union_value | func_call | plain_value
    )
    argument = (
        Word(alphanums).setResultsName("name")
        + Literal("=")
        + Group(any_value).setResultsName("value")
    )
    definition = (
        SkipTo("(")
        + Literal("(")
        + Opt(delimitedList(Group(argument))).setResultsName("arguments")
        + Opt(",")
        + Literal(")")
    )
    request_syntax = "**Request Syntax**" + Literal("::") + definition
    response_syntax = (
        "**Response Syntax**"
        + Literal("::")
        + Group(list_value | dict_value).setResultsName("value")
    )

    @classmethod
    def reset(cls) -> None:
        """
        Reset packrat boost.
        """
        cls.disable_packrat()

    @staticmethod
    def enable_packrat() -> None:
        """
        Enable packrat boost.
        """
        ParserElement.enablePackrat(cache_size_limit=128)

    @staticmethod
    def disable_packrat() -> None:
        """
        Disable packrat boost.
        """
        ParserElement.enablePackrat(cache_size_limit=0)
