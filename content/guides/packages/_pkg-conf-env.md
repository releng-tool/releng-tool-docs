## `LIBFOO_CONF_ENV`

:::{versionchanged} 2.2 Support added for path-like values.
:::

Provides a means to pass environment variables into the configuration process.
This option is defined as a dictionary with key-value pairs where the key is
the environment name and the value is the environment variable's value. This
field is optional.

```python
LIBFOO_CONF_ENV = {
    'OPTION': 'VALUE',
}
```
