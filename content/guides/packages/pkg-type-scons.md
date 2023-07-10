# SCons package

A SCons package provides support to easily invoke [SCons][scons] commands
at various stages of a package.

```python
LIBFOO_TYPE = 'scons'
```

SCons-based projects by default will invoke the default target during the
build stage, and invoke the `install` alias for the installation stage.
Developers can configure a specific target to invoke during the build stage
by specifying a `LIBFOO_BUILD_OPTS` configuration. For example, if a
package uses the target `release` for standard release builds, the
following can be used:

```python
LIBFOO_BUILD_OPTS = [
    'release',
]
```

For the installation stage, the `install` alias is typically invoked.
However, developers can override what target to invoke by adding it into the
install options:

```python
LIBFOO_INSTALL_OPTS = [
    'install-minimal',
]
```

For packages which do not have an installation alias to run, developers can
use the [](pkg-scons-noinstall) option to skip the installation stage for
a package.

Default configurations for a SCons package will not run a configuration stage.
However, if a user wants to run a specific target during this stage, the
target can be added into the configuration options. For example, if the
SCons definition has a target `prework` that should be invoked
during the configuration stage, the following can be used:

```python
LIBFOO_CONF_OPTS = [
    'prework',
]
```

Alternatively, if no configuration options are specified, a
`<package>-configure` [script](pkg-type-script) can be invoked if available.

The following sections outline configuration options are available for a SCons
package.

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

(pkg-scons-noinstall)=
## `LIBFOO_SCONS_NOINSTALL`

Specifies whether a SCons package should skip an attempt to invoke the
install alias. Ideally, projects will have an [install alias][scons-alias]
defined to specify how a project will install files into a target (or staging)
environment. Not all SCons projects may have this target defined, which
can cause the installation stage for a package to fail. A developer can
specify this no-install flag to skip a SCons install target request and
manage installation actions through other means (such as post-processing).
By default, the installation stage is invoked with a value of `False`.

```python
LIBFOO_SCONS_NOINSTALL = True
```

[scons-alias]: https://scons.org/doc/production/HTML/scons-man.html#f-Alias
[scons]: https://scons.org/
