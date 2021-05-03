# Type annotations for boto3 {{ package.service_name.class_name }} module

> [Index](../README.md) > {{ package.service_name.class_name }}

Auto-generated documentation for [{{ package.service_name.class_name }}]({{ package.service_name.boto3_doc_link }})
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

Type annotations for  `boto3.resource("{{ package.service_name.boto3_name }}")` as [{{ package.service_resource.name }}](./service_resource.md)

Can be used directly:

```python
from {{ package.service_name.module_name }}.service_resource import {{ package.service_resource.name }}
```

{% if package.service_resource.collections %}
### Collections

Type annotations for collections from `boto3.resource("{{ package.service_name.boto3_name }}").*`.

Can be used directly:

```python
from {{ package.service_name.module_name }}.service_resource import {{ package.service_resource.collections[0].name }}, ...
```

{% for collection in package.service_resource.collections -%}
- [{{ collection.name }}](./service_resource.md#{{ get_anchor_link(package.service_resource.name) }}.{{ get_anchor_link(collection.attribute_name) }}){{ '\n' -}}
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
- [{{ sub_resource.name }}](./service_resource.md#{{ get_anchor_link(sub_resource.name) }}){{ '\n' -}}
{% endfor %}
{% endif %}
{% endif %}

{% if package.paginators %}
## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("{{ package.service_name.boto3_name }}").get_paginator("...")`.

Can be used directly:

```python
from {{ package.service_name.module_name }}.paginators import {{ package.paginators[0].name }}, ...
```

{% for paginator in package.paginators -%}
- [{{ paginator.name }}](./paginators.md#{{ get_anchor_link(paginator.name) }}){{ '\n' -}}
{% endfor %}
{% endif %}

{% if package.waiters %}
## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("{{ package.service_name.boto3_name }}").get_waiter("...")`.

Can be used directly:

```python
from {{ package.service_name.module_name }}.waiters import {{ package.waiters[0].name }}, ...
```

{% for waiter in package.waiters -%}
- [{{ waiter.name }}](./waiters.md#{{ get_anchor_link(waiter.name) }}){{ '\n' -}}
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
## Typed dictionaries


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from {{ package.service_name.module_name }}.type_defs import {{ package.typed_dicts[0].name }}, ...
```

{% for typed_dict in package.typed_dicts -%}
- [{{ typed_dict.name }}](./type_defs.md#{{ get_anchor_link(typed_dict.name) }}){{ '\n' -}}
{% endfor %}
{% endif %}