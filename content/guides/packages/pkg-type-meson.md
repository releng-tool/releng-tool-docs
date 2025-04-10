# Meson package

:::{versionadded} 0.16
:::

A Meson package provides support for processing a [Meson][meson] supported
module.

```python
LIBFOO_TYPE = 'meson'
```

During the configuration stage of a Meson package, `meson setup` will be
invoked to generate build files for the module. For the build stage,
`meson compile` will invoke the generated build files. For the installation
stage (if enabled), `meson install` will be used. Each stage can be
configured to manipulate environment variables and options used by Meson.

The default configuration built for projects is `debugoptimized`. A developer
can override this option by explicitly adjusting the define option
`buildtype` to, for example, `debug`:

```python
LIBFOO_CONF_DEFS = {
    'buildtype': 'debug',
}
```

The following sections outline configuration options are available for a Meson
package.

(pkg-opt-meson-build-defs)=
:::{include} _pkg-build-defs.md
:::
:::{include} _pkg-build-defs-example-dentry.md
:::

(pkg-opt-meson-build-env)=
:::{include} _pkg-build-env.md
:::

(pkg-opt-meson-build-opts)=
:::{include} _pkg-build-opts.md
:::

(pkg-opt-meson-noinstall)=
## `LIBFOO_MESON_NOINSTALL`

Specifies whether the Meson package should skip an attempt to invoke the
install command. Ideally, projects will have an [install][meson-install]
options configured to define how a project will install files into a target
(or staging) environment. Not all Meson projects have installation options
configured, or there can be cases where installation stage for a package to
fail due to issues with some host environments. A developer can specify this
no-install flag to skip a Meson-driven install request and manage installation
actions through other means (such as post-processing). By default, the
installation stage is invoked with a value of `False`.

```python
LIBFOO_MESON_NOINSTALL = True
```

(pkg-opt-meson-conf-defs)=
:::{include} _pkg-conf-defs.md
:::
:::{include} _pkg-conf-defs-example-dentry.md
:::

(pkg-opt-meson-conf-env)=
:::{include} _pkg-conf-env.md
:::

(pkg-opt-meson-conf-opts)=
:::{include} _pkg-conf-opts.md
:::

(pkg-opt-meson-env)=
:::{include} _pkg-env.md
:::

(pkg-opt-meson-install-defs)=
:::{include} _pkg-install-defs.md
:::
:::{include} _pkg-install-defs-example-dentry.md
:::

(pkg-opt-meson-install-env)=
:::{include} _pkg-install-env.md
:::

(pkg-opt-meson-install-opts)=
:::{include} _pkg-install-opts.md
:::


[meson-install]: https://mesonbuild.com/Commands.html#install
[meson]: https://mesonbuild.com/
