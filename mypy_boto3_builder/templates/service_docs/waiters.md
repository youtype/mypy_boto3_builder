# Waiters for boto3 {{ package.service_name.class_name }} module

[Back to {{ package.service_name.class_name }} type annotations](./index.md)

Auto-generated documentation for [{{ package.service_name.class_name }}]({{ package.service_name.doc_link}})
type annotations stubs module [{{ package.service_name.module_name }}]({{ package.service_name.pypi_link }}).

{% for waiter in package.waiters -%}
## {{ waiter.name }}

Type annotations for `boto3.client("{{ package.service_name.boto3_name }}").get_waiter("{{ waiter.waiter_name }}")`.

Can be used directly:

```python
from {{ package.service_name.module_name }}.waiters import {{ waiter.name }}

def get_{{ waiter.waiter_name }}_waiter() -> {{ waiter.name }}:
    return boto3.client("{{ package.service_name.boto3_name }}").get_waiter("{{ waiter.waiter_name }}")
```

{{ waiter.docstring }}

```python
{% with class=waiter, render_docstrings=False -%}
{% include "common/class.py.jinja2" with context -%}{{ '\n' -}}
{% endwith -%}
```
{% else %}
{{ package.client.name }} has no waiters.
{% endfor %}
