# SyntaxGrammar

[mypy-boto3-builder Index](../../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) /
[Parsers](../index.md#parsers) /
[Docstring Parser](./index.md#docstring-parser) /
SyntaxGrammar

> Auto-generated documentation for [mypy_boto3_builder.parsers.docstring_parser.syntax_grammar](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/syntax_grammar.py) module.

- [SyntaxGrammar](#syntaxgrammar)
  - [SyntaxGrammar](#syntaxgrammar-1)
    - [SyntaxGrammar.disable_packrat](#syntaxgrammardisable_packrat)
    - [SyntaxGrammar.enable_packrat](#syntaxgrammarenable_packrat)
    - [SyntaxGrammar.reset](#syntaxgrammarreset)

## SyntaxGrammar

[Show source in syntax_grammar.py:19](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/syntax_grammar.py#L19)

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

#### Signature

```python
class SyntaxGrammar:
    ...
```

### SyntaxGrammar.disable_packrat

[Show source in syntax_grammar.py:141](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/syntax_grammar.py#L141)

Disable packrat boost.

#### Signature

```python
@staticmethod
def disable_packrat() -> None:
    ...
```

### SyntaxGrammar.enable_packrat

[Show source in syntax_grammar.py:134](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/syntax_grammar.py#L134)

Enable packrat boost.

#### Signature

```python
@staticmethod
def enable_packrat() -> None:
    ...
```

### SyntaxGrammar.reset

[Show source in syntax_grammar.py:127](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/syntax_grammar.py#L127)

Reset packrat boost.

#### Signature

```python
@classmethod
def reset(cls) -> None:
    ...
```


