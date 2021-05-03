# Literals for boto3 {{ package.service_name.class_name }} module

> [Index](../README.md) > [{{ package.service_name.class_name }}](./README.md) > Literals

Auto-generated documentation for [{{ package.service_name.class_name }}]({{ package.service_name.boto3_doc_link }})
type annotations stubs module [{{ package.service_name.module_name }}]({{ package.service_name.pypi_link }}).

{% for literal in package.literals -%}
## {{ literal.name }}

```python
from {{ package.service_name.module_name }}.literals import {{ literal.name }}
```

Values:

{% for child in literal.children|sort -%}
- `{{ child }}`{{ '\n' -}}
{% endfor -%}
{{ '\n' -}}
{% endfor %}