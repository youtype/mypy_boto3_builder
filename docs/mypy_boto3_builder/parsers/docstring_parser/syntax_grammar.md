# SyntaxGrammar

> Auto-generated documentation for [mypy_boto3_builder.parsers.docstring_parser.syntax_grammar](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/docstring_parser/syntax_grammar.py) module.

Pyparsing grammar for request and response syntax.

- [mypy-boto3-builder](../../../README.md#mypy_boto3_builder) / [Modules](../../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) / [Parsers](../index.md#parsers) / [Docstring Parser](index.md#docstring-parser) / SyntaxGrammar
    - [SyntaxGrammar](#syntaxgrammar)
        - [SyntaxGrammar.disable_packrat](#syntaxgrammardisable_packrat)
        - [SyntaxGrammar.enable_packrat](#syntaxgrammarenable_packrat)
        - [SyntaxGrammar.reset](#syntaxgrammarreset)

## SyntaxGrammar

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/docstring_parser/syntax_grammar.py#L19)

```python
class SyntaxGrammar():
```

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

### SyntaxGrammar.disable_packrat

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/docstring_parser/syntax_grammar.py#L146)

```python
@staticmethod
def disable_packrat() -> None:
```

Disable packrat boost.

### SyntaxGrammar.enable_packrat

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/docstring_parser/syntax_grammar.py#L139)

```python
@staticmethod
def enable_packrat() -> None:
```

Enable packrat boost.

### SyntaxGrammar.reset

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/docstring_parser/syntax_grammar.py#L132)

```python
@classmethod
def reset() -> None:
```

Reset packrat boost.
