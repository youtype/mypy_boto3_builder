# TypeDocGrammar

[Mypy_boto3_builder Index](../../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) /
[Parsers](../index.md#parsers) /
[Docstring Parser](./index.md#docstring-parser) /
TypeDocGrammar

> Auto-generated documentation for [mypy_boto3_builder.parsers.docstring_parser.type_doc_grammar](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_doc_grammar.py) module.

## TypeDocGrammar

[Show source in type_doc_grammar.py:19](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_doc_grammar.py#L19)

Grammar to parse boto3 docs syntax.

EOL ::= ["\r"] "\n"
SOL ::= LINE_START
line ::= [^EOL]+ EOL
word ::= alphanums + "_"
indented_block ::= INDENT (line_indented | any_line)
line_indented ::= any_line indented_block
type_definition ::= ":type" [^:]+ ":" [^EOL]+
rtype_definition ::= ":rtype:" [^EOL]+
returns_definition ::= (":returns:" | ":return:") [^EOL]+
param_definition ::= ":param" [^:]+ ":" [^EOL]+ EOL [indented_block]
response_structure ::= "**Response Structure**" line [indented_block]
typed_dict_key_line ::= "-" "**" word "**" "*(" word ")" "--*" [^EOL]+ + EOL
type_line ::= "-" "*(" word ")" "--*" [^EOL]+ + EOL
any_line ::= typed_dict_key_line | type_line | line

#### Signature

```python
class TypeDocGrammar:
    ...
```

### TypeDocGrammar.disable_packrat

[Show source in type_doc_grammar.py:136](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_doc_grammar.py#L136)

Disable packrat boost.

#### Signature

```python
@staticmethod
def disable_packrat() -> None:
    ...
```

### TypeDocGrammar.enable_packrat

[Show source in type_doc_grammar.py:129](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_doc_grammar.py#L129)

Enable packrat boost.

#### Signature

```python
@staticmethod
def enable_packrat() -> None:
    ...
```

### TypeDocGrammar.fail_action

[Show source in type_doc_grammar.py:109](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_doc_grammar.py#L109)

Check for input end.

#### Signature

```python
@classmethod
def fail_action(
    cls,
    _input_string: str,
    _chr_index: int,
    _source: ParserElement,
    error: BaseException,
) -> None:
    ...
```

### TypeDocGrammar.reset

[Show source in type_doc_grammar.py:119](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_doc_grammar.py#L119)

Reset call stack and packrat.

#### Signature

```python
@classmethod
def reset(cls) -> None:
    ...
```



