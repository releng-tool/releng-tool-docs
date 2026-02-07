## `LIBFOO_INSTALL_OPTS`

:::{versionchanged} 2.2 Support added for path-like values.
:::

Provides a means to pass command line options into the installation process.
This option can be defined as a dictionary of string pairs or a list with
strings -- either way defined will generate argument values to include in
the installation event. This field is optional.

```python
LIBFOO_INSTALL_OPTS = {
    # include the "install" target to the command
    'install': '',
    # adds "--option value" to the command
    '--option': 'value',
}

# (or)

LIBFOO_INSTALL_OPTS = [
    # include the "install" target to the command
    'install',
    # adds "--some-option" to the command
    '--some-option',
]
```

Defining custom install options will prevent the default `install` target from
being added. Users looking to utilize the `install` target for the install
stage with custom arguments should explicitly include the `install` target in
their options.
