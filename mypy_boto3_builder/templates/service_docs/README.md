# Type annotaitons for boto3 {{ package.service_name.class_name }} module

Auto-generated documentation for [{{ package.service_name.class_name }}]({{ package.service_name.doc_link}})
type annotations stubs module [{{ package.service_name.module_name }}]({{ package.service_name.pypi_link }}).

```bash
pip install {{ package.service_name.pypi_name }}
```

## {{ package.client.name }}

Type annotations for  `boto3.client("{{ package.service_name.boto3_name }}")` as [{{ package.client.name }}](./client.md)

Can be used directly:

```python
from {{ package.service_name.module_name }}.client import {{ package.client.name }}
```

{% if package.client.exceptions_class.attributes %}
{{ package.client.name }} [exceptions](./client.md#exceptions)
{% endif %}

{% if package.client.methods %}
### Methods
{% for method_name in package.client.method_names -%}
- [{{ method_name }}](./client.md#{{ get_anchor_link(method_name) }}){{ '\n' -}}
{% endfor %}
{% endif %}

{% if package.client.exceptions_class.attributes %}
### Exceptions
{% for attribute in package.client.exceptions_class.attributes -%}
- [{{ attribute.name }}](./client.md#{{ get_anchor_link(attribute.name) }}){{ '\n' -}}
{% endfor %}
{% endif %}

{% if package.service_resource %}
## {{ package.service_resource.name }}

Type annotations for `boto3.resource("{{ package.service_name.boto3_name }}")`.

Can be used directly:

```python
from {{ package.service_name.module_name }}.service_resource import {{ package.service_resource.name }}
```

{% if package.service_resource.methods %}
### Methods
{% for method_name in package.service_resource.method_names -%}
- {{ package.service_resource.name }}.{{ method_name }}{{ '\n' -}}
{% endfor %}
{% endif %}

{% if package.service_resource.sub_resources %}

### Resources

Type annotations for additional resources from `boto3.resource("{{ package.service_name.boto3_name }}").*`.

Can be used directly:

```python
from {{ package.service_name.module_name }}.service_resource import {{ package.service_resource.sub_resources[0].name }}, ...
```

{% for sub_resource in package.service_resource.sub_resources -%}
- {{ sub_resource.name }}{{ '\n' -}}
{% endfor %}
{% endif %}

{% if package.service_resource.collections %}
### Collections

Type annotations for collections from `boto3.resource("{{ package.service_name.boto3_name }}").*`.

Can be used directly:

```python
from {{ package.service_name.module_name }}.service_resource import {{ package.service_resource.collections[0].name }}, ...
```

{% for collection in package.service_resource.collections -%}
- {{ collection.name }}{{ '\n' -}}
{% endfor %}
{% endif %}

{% endif %}

{% if package.paginators %}
## Paginators

Type annotations for paginators from `boto3.client("{{ package.service_name.boto3_name }}").get_paginator("...")`.

Can be used directly:

```python
from {{ package.service_name.module_name }}.paginators import {{ package.paginators[0].name }}, ...
```

{% for paginator in package.paginators -%}
- {{ paginator.name }}{{ '\n' -}}
{% endfor %}
{% endif %}

{% if package.waiters %}
## Waiters

Type annotations for waiters from `boto3.client("{{ package.service_name.boto3_name }}").get_waiter("...")`.

Can be used directly:

```python
from {{ package.service_name.module_name }}.waiters import {{ package.waiters[0].name }}, ...
```

{% for waiter in package.waiters -%}
- {{ waiter.name }}{{ '\n' -}}
{% endfor %}
{% endif %}

{% if package.literals %}
## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from {{ package.service_name.module_name }}.literals import {{ package.literals[0].name }}, ...
```

{% for literal in package.literals -%}
- [{{ literal.name }}](./literals.md#{{ get_anchor_link(literal.name) }}){{ '\n' -}}
{% endfor %}
{% endif %}

{% if package.typed_dicts %}
## Structures


Type annotations for [typed dictionaries](./structures.md) used in methods and schema.

Can be used directly:

```python
from {{ package.service_name.module_name }}.type_defs import {{ package.typed_dicts[0].name }}, ...
```

{% for typed_dict in package.typed_dicts -%}
- [{{ typed_dict.name }}](./structures.md#{{ get_anchor_link(typed_dict.name) }}){{ '\n' -}}
{% endfor %}
{% endif %}