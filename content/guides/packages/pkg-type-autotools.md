# Autotools package

An Autotools package provides support for processing a
[GNU Build System][gnu-build-sys] supported module.

```python
LIBFOO_TYPE = 'autotools'
```

When an Autotools package performs a configuration stage, the package may
invoke `autoreconf` (if configured to do so) and then invoke `configure`.
When the build stage is reached, `make` will be invoked followed by
`make install` during the installation stage.

The following sections outline configuration options are available for an
Autotools package.

(pkg-opt-autotools-autoreconf)=
## `LIBFOO_AUTOTOOLS_AUTORECONF`

Specifies whether the package needs to perform an Autotools
re-configuration. This is to assist in the rebuilding of GNU Build System
files which may be broken or a patch has introduced new build script
changes that need to be applied. This field is optional. By default,
`autoreconf` is not invoked.

```python
LIBFOO_AUTOTOOLS_AUTORECONF = True
```

(pkg-opt-autotools-build-defs)=
:::{include} _pkg-build-defs.md
:::
:::{include} _pkg-build-defs-example-default.md
:::

(pkg-opt-autotools-build-env)=
:::{include} _pkg-build-env.md
:::

(pkg-opt-autotools-build-opts)=
:::{include} _pkg-build-opts.md
:::

(pkg-opt-autotools-conf-defs)=
:::{include} _pkg-conf-defs.md
:::
:::{include} _pkg-conf-defs-example-default.md
:::

(pkg-opt-autotools-conf-env)=
:::{include} _pkg-conf-env.md
:::

(pkg-opt-autotools-conf-opts)=
:::{include} _pkg-conf-opts.md
:::

(pkg-opt-autotools-env)=
:::{include} _pkg-env.md
:::

(pkg-opt-autotools-install-defs)=
:::{include} _pkg-install-defs.md
:::
:::{include} _pkg-install-defs-example-default.md
:::

(pkg-opt-autotools-install-env)=
:::{include} _pkg-install-env.md
:::

(pkg-opt-autotools-install-opts)=
:::{include} _pkg-install-opts.md
:::


[gnu-build-sys]: https://www.gnu.org/software/automake/manual/html_node/index.html
