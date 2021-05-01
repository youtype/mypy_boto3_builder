# {{ package.client.name }} for boto3 {{ package.service_name.class_name }} module

[Back to {{ package.service_name.class_name }} type annotations](./README.md)

Auto-generated documentation for [{{ package.service_name.class_name }}]({{ package.service_name.doc_link}})
type annotations stubs module [{{ package.service_name.module_name }}]({{ package.service_name.pypi_link }}).

- [{{ package.client.name }} for boto3 {{ package.service_name.class_name }} module](#{{ get_anchor_link(package.client.name) }}-for-boto3-{{ get_anchor_link(package.service_name.class_name) }}-module)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
{% for method_name in package.client.method_names -%}
{{ '    ' -}}- [{{ method_name }}](#{{ get_anchor_link(method_name) }}){{ '\n' -}}
{% endfor %}

Type annotations for `boto3.client("{{ package.service_name.boto3_name }}")`

Can be used directly:

```python
from {{ package.service_name.module_name }}.client import {{ package.client.name }}
```

## Exceptions

{% if package.client.exceptions_class.attributes %}
`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from {{ package.service_name.module_name }}.client import {{ package.client.exceptions_class.name }}

def handle_error(exc: {{ package.client.exceptions_class.name }}.{{ package.client.exceptions_class.attributes[0].name }}) -> None:
    ...
```
{% else %}
{{ package.client.name }} has no exceptions.
{% endif %}

Exceptions:

{% for attribute in package.client.exceptions_class.attributes -%}
- `{{ package.client.exceptions_class.name }}.{{ attribute.name }}`{{ '\n' -}}
{% endfor %}

## Methods

{% for method in package.client.methods %}
### {{ method.name }}

Type annotations for `boto3.client("{{ package.service_name.boto3_name }}").{{ method.name }}`.

{{ method.docstring }}

```python
{% include "common/method.py.jinja2" with context -%}
```
{% else %}
{{ package.client.name }} has no public methods.
{% endfor %}
