# System-specific package options

The following outlines systems-specific configuration options available for
packages.

(pkg-opt-vsdevcmd)=
## `LIBFOO_VSDEVCMD`

:::{note}
The option is ignored in non-Windows environments.
:::

:::{versionadded} 1.3
:::

Allows a package to automatically load Visual Studio Developer Command
Prompt (`VsDevCmd.bat`) variables into the releng-tool process. This will
allow a package to invoke commands as if releng-tool was started from
within a Visual Studio Developer Command Prompt.

```python
LIBFOO_VSDEVCMD = True
```

A package looking to use an explicit version of Visual Studio can specify a
version string that is compatible with [Visual Studio Locator's][vswhere]
(vswhere) `-version` argument.

```python
LIBFOO_VSDEVCMD = '[17.0,18.0)'
```

See also [`vsdevcmd`](conf-vsdevcmd) and
[`LIBFOO_VSDEVCMD_PRODUCTS`](pkg-opt-vsdevcmd-products).

(pkg-opt-vsdevcmd-products)=
## `LIBFOO_VSDEVCMD_PRODUCTS`

:::{note}
The option is ignored in non-Windows environments.
:::

:::{versionadded} 2.4
:::

Allows a package to configure which products to search for when releng-tool
invokes [Visual Studio Locator][vswhere] to find which Visual Studio tooling
to use. By default, releng-tool operates as if `vswhere` is invoked with the
`-products *` argument. Providing a string in this option replaces the
asterisk value with the configured value.

```python
LIBFOO_VSDEVCMD_PRODUCTS = 'Microsoft.VisualStudio.Product.BuildTools'
```

See also [`vsdevcmd_products`](conf-vsdevcmd-products) and
[`LIBFOO_VSDEVCMD`](pkg-opt-vsdevcmd).


[vswhere]: https://github.com/microsoft/vswhere
