# Make package

A make package provides support to easily invoke [GNU Make][gnu-make]
commands at various stages of a package.

```python
LIBFOO_TYPE = 'make'
```

Make-based projects by default will invoke the default target during the build
stage, and invoke the `install` target for the installation stage. Developers
can configure a specific target to invoke during the build stage by specifying
a `LIBFOO_BUILD_OPTS` configuration. For example, if a package uses the
target `release` for standard release builds, the following can be used:

```python
LIBFOO_BUILD_OPTS = [
    'release',
]
```

For the installation stage, the `install` target is typically invoked.
However, developers can override what target to invoke by adding it into the
install options:

```python
LIBFOO_INSTALL_OPTS = [
    'install-minimal',
]
```

For packages which do not have an installation target to run, developers can
use the [](pkg-opt-make-noinstall) option to skip the installation stage for
a package.

Default configurations for a make package will not run a configuration stage.
However, if a user wants to run a specific target during this stage, the
target can be added into the configuration options. For example, if the
Makefile configuration has a target `prework` that should be invoked
during the configuration stage, the following can be used:

```python
LIBFOO_CONF_OPTS = [
    'prework',
]
```

Alternatively, if no configuration options are specified, a
`<package>-configure`  [script](pkg-type-script) can be invoked if available.

The following sections outline configuration options are available for a make
package.

(pkg-opt-make-build-defs)=
:::{include} _pkg-build-defs.md
:::
:::{include} _pkg-build-defs-example-default.md
:::

(pkg-opt-make-build-env)=
:::{include} _pkg-build-env.md
:::

(pkg-opt-make-build-opts)=
:::{include} _pkg-build-opts.md
:::

(pkg-opt-make-conf-defs)=
:::{include} _pkg-conf-defs.md
:::
:::{include} _pkg-conf-defs-example-default.md
:::

(pkg-opt-make-conf-env)=
:::{include} _pkg-conf-env.md
:::

(pkg-opt-make-conf-opts)=
:::{include} _pkg-conf-opts.md
:::

(pkg-opt-make-env)=
:::{include} _pkg-env.md
:::

(pkg-opt-make-install-defs)=
:::{include} _pkg-install-defs.md
:::
:::{include} _pkg-install-defs-example-default.md
:::

(pkg-opt-make-install-env)=
:::{include} _pkg-install-env.md
:::

(pkg-opt-make-install-opts)=
:::{include} _pkg-install-opts.md
:::

(pkg-opt-make-noinstall)=
## `LIBFOO_MAKE_NOINSTALL`

Specifies whether a make package should skip an attempt to invoke the
install target. Ideally, projects will have an `install` target configured
to define how a project will install files into a target (or staging)
environment. Not all make projects may have this target defined, which
can cause the installation stage for a package to fail. A developer can
specify this no-install flag to skip a make install target request and
manage installation actions through other means (such as post-processing).
By default, the installation stage is invoked with a value of `False`.

```python
LIBFOO_MAKE_NOINSTALL = True
```


[gnu-make]: https://www.gnu.org/software/make/manual/html_node/index.html
