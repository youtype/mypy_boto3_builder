# Waiters for boto3 {{ package.service_name.class_name }} module

> [Index](../README.md) > [{{ package.service_name.class_name }}](./README.md) > Waiters

Auto-generated documentation for [{{ package.service_name.class_name }}]({{ package.service_name.boto3_doc_link }})
type annotations stubs module [{{ package.service_name.module_name }}]({{ package.service_name.pypi_link }}).

{% for waiter in package.waiters -%}
## {{ waiter.name }}

Type annotations for `boto3.client("{{ package.service_name.boto3_name }}").get_waiter("{{ waiter.waiter_name }}")`.

Can be used directly:

```python
from {{ package.service_name.module_name }}.waiter import {{ waiter.name }}

def get_{{ waiter.waiter_name }}_waiter() -> {{ waiter.name }}:
    return boto3.client("{{ package.service_name.boto3_name }}").get_waiter("{{ waiter.waiter_name }}")
```

[Open boto3 documentation]({{ waiter.boto3_doc_link }})

```python
{% with class=waiter, render_docstrings=False -%}
{% include "common/class.py.jinja2" with context -%}{{ '\n' -}}
{% endwith -%}
```
{% else %}
{{ package.client.name }} has no waiters.
{% endfor %}
