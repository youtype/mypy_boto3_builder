# Literals for boto3 {{ package.service_name.class_name }} module

[Back to {{ package.service_name.class_name }} type annotations](./README.md)

Auto-generated documentation for [{{ package.service_name.class_name }}]({{ package.service_name.doc_link}})
type annotations stubs module [{{ package.service_name.module_name }}]({{ package.service_name.pypi_link }}).

- [Literals for boto3 {{ package.service_name.class_name }} module](#literals-for-boto3-{{ get_anchor_link(package.service_name.class_name) }}-module)
{% for literal in package.literals -%}
{{ '  ' -}}- [{{ literal.name }}](#{{ get_anchor_link(literal.name) }}){{ '\n' -}}
{% endfor %}

{% for literal in package.literals -%}
## {{ literal.name }}

```python
from {{ package.service_name.module_name }}.literals import {{ literal.name }}
```

Values:

{% for child in literal.children -%}
- `{{ child }}`{{ '\n' -}}
{% endfor -%}
{{ '\n' -}}
{% endfor %}