## `LIBFOO_INSTALL_OPTS`

:::{versionchanged} 2.2 Support added for path-like values.
:::

Provides a means to pass command line options into the installation process.
This option can be defined as a dictionary of string pairs or a list with
strings -- either way defined will generate argument values to include in
the installation event. This field is optional.

```python
LIBFOO_INSTALL_OPTS = {
    # adds "--option value" to the command
    '--option': 'value',
}

# (or)

LIBFOO_INSTALL_OPTS = [
    # adds "--some-option" to the command
    '--some-option',
]
```
