# Structures for boto3 {{ package.service_name.class_name }} module

[Back to {{ package.service_name.class_name }} type annotations](./README.md)

Auto-generated documentation for [{{ package.service_name.class_name }}]({{ package.service_name.doc_link}})
type annotations stubs module [{{ package.service_name.module_name }}]({{ package.service_name.pypi_link }}).

- [Structures for boto3 {{ package.service_name.class_name }} module](#structures-for-boto3-{{ get_anchor_link(package.service_name.class_name) }}-module)
{% for typed_dict in package.typed_dicts -%}
{{ '  ' -}}- [{{ typed_dict.name }}](#{{ get_anchor_link(typed_dict.name) }}){{ '\n' -}}
{% endfor %}

{% for typed_dict in package.typed_dicts -%}
## {{ typed_dict.name }}

```python
from {{ package.service_name.module_name }}.type_defs import {{ typed_dict.name }}
```

{% if typed_dict.get_required() %}
Required fields:
{% for field in typed_dict.get_required() -%}
- `{{ field.name }}`: `{{ field.type_annotation.render() }}`{{ '\n' -}}
{% endfor -%}
{% endif %}

{% if typed_dict.get_optional() %}
Optional fields:
{% for field in typed_dict.get_optional() -%}
- `{{ field.name }}`: `{{ field.type_annotation.render() }}`{{ '\n' -}}
{% endfor -%}
{% endif %}

{% endfor %}