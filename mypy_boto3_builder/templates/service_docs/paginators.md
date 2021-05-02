# Paginators for boto3 {{ package.service_name.class_name }} module

> [Index](../index.md) > [{{ package.service_name.class_name }}](./index.md) > Paginators

Auto-generated documentation for [{{ package.service_name.class_name }}]({{ package.service_name.doc_link}})
type annotations stubs module [{{ package.service_name.module_name }}]({{ package.service_name.pypi_link }}).

{% for paginator in package.paginators -%}
## {{ paginator.name }}

Type annotations for `boto3.client("{{ package.service_name.boto3_name }}").get_paginator("{{ paginator.operation_name }}")`.

Can be used directly:

```python
from {{ package.service_name.module_name }}.paginators import {{ paginator.name }}

def get_{{ paginator.operation_name }}_paginator() -> {{ paginator.name }}:
    return boto3.client("{{ package.service_name.boto3_name }}").get_paginator("{{ paginator.operation_name }}")
```

{{ paginator.docstring }}

```python
{% with class=paginator, render_docstrings=False -%}
{% include "common/class.py.jinja2" with context -%}{{ '\n' -}}
{% endwith -%}
```
{% else %}
{{ package.client.name }} has no paginators.
{% endfor %}
