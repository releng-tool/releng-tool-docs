## `LIBFOO_CONF_OPTS`

:::{versionchanged} 2.2 Support added for path-like values.
:::

Provides a means to pass command line options into the configuration process.
This option can be defined as a dictionary of string pairs or a list with
strings -- either way defined will generate argument values to include in the
configuration event. This field is optional.

```python
LIBFOO_CONF_OPTS = {
    # adds "--option value" to the command
    '--option': 'value',
}

# (or)

LIBFOO_CONF_OPTS = [
    # adds "--some-option" to the command
    '--some-option',
]
```
