# Autotools package

An autotools package provides support for processing a
[GNU Build System][gnu-build-sys] supported module.

```python
LIBFOO_TYPE = 'autotools'
```

When an autotools package performs a configuration stage, the package may
invoke `autoreconf` (if configured to do so) and then invoke `configure`.
When the build stage is reached, `make` will be invoked followed by
`make install` during the installation stage.

The following sections outline configuration options are available for an
autotools package.

## `LIBFOO_AUTOTOOLS_AUTORECONF`

Specifies whether the package needs to perform an autotools
re-configuration. This is to assist in the rebuilding of GNU Build System
files which may be broken or a patch has introduced new build script
changes that need to be applied. This field is optional. By default,
`autoreconf` is not invoked.

```python
LIBFOO_AUTOTOOLS_AUTORECONF = True
```

:::{include} _pkg-build-defs.md
:::
:::{include} _pkg-build-defs-example-default.md
:::

:::{include} _pkg-build-env.md
:::

:::{include} _pkg-build-opts.md
:::

:::{include} _pkg-conf-defs.md
:::
:::{include} _pkg-conf-defs-example-default.md
:::

:::{include} _pkg-conf-env.md
:::

:::{include} _pkg-conf-opts.md
:::

:::{include} _pkg-env.md
:::

:::{include} _pkg-install-defs.md
:::
:::{include} _pkg-install-defs-example-default.md
:::

:::{include} _pkg-install-env.md
:::

:::{include} _pkg-install-opts.md
:::


[gnu-build-sys]: https://www.gnu.org/software/automake/manual/html_node/index.html
