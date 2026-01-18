# SCons package

:::{versionadded} 0.13
:::

A SCons package provides support to easily invoke [SCons][scons] commands
at various stages of a package.

```python
LIBFOO_TYPE = 'scons'
```

SCons-based projects by default will invoke the default target during the
build stage, and invoke the `install` alias for the installation stage.

The following shows the default arguments used in stages and outlines
configuration options that are available for a SCons package to set.
See also the [SCons package examples](/examples/examples-scons). All stages
are invoked with a [`PKG_BUILD_DIR`](env-pkg-build-dir) working directory.

````{tab} Configuration
```{eval-rst}
.. only:: latex

    Configuration stage
    -------------------
```

Default configurations for SCons packages will not run a configuration stage.
However, if a user wants to run a specific target during this stage, a
target can be added into the configuration options. For example, if the
package has a target `prework` that should be invoked during the
configuration stage, the following can be used:

```python
LIBFOO_CONF_OPTS = [
    'prework',
]
```

Which will invoke `scons` with the arguments:

```none
scons -Q prework
```

Alternatively, if no configuration options are specified, a
`<package>-configure` [script](pkg-type-script) can be invoked if available.
````

````{tab} Build
```{eval-rst}
.. only:: latex

    Build stage
    -----------
```

The build stage invokes `scons` with the arguments:

```none
scons -Q --jobs=<NJOBS>
```

This will trigger the default target for the SCons configuration.
Developers can configure a specific target to invoke during the build stage by
specifying a [`LIBFOO_BUILD_OPTS`](pkg-opt-scons-build-opts) configuration. For
example, if a package uses the target `release` for standard release builds,
the following can be used:

```python
LIBFOO_BUILD_OPTS = [
    'release',
]
```

The number of jobs is populated by either the [`--jobs` argument](arg-jobs) or
[`LIBFOO_FIXED_JOBS`](pkg-opt-fixed-jobs). Although, if the configuration
results in a single job, the argument will not be used.
````

````{tab} Install
```{eval-rst}
.. only:: latex

    Install stage
    -------------
```

The install stage invokes `scons` with an `install` target:

```none
scons -Q install
```

With the following variables set:

```none
DESTDIR=<TARGET_DIR>
PREFIX=<PREFIX>
```

The `DESTDIR` path will be set to the target sysroot the package should
install into (see also [`LIBFOO_INSTALL_TYPE`](pkg-opt-install-type)).
`scons install` may be invoked multiple times for each target it needs to
install into.

The prefix argument is configured to [`LIBFOO_PREFIX`](pkg-opt-prefix).

If a package defines install options, the `install` target is not provided
by default. Developers can override what target to invoke by adding it into
the install options:

```python
LIBFOO_INSTALL_OPTS = [
    'install-minimal',
]
```

The installation stage can be skipped by configuring
[`LIBFOO_SCONS_NOINSTALL`](pkg-opt-scons-noinstall).
````

(pkg-opt-scons-build-defs)=
:::{include} _pkg-build-defs.md
:::
:::{include} _pkg-build-defs-example-default.md
:::

(pkg-opt-scons-build-env)=
:::{include} _pkg-build-env.md
:::

(pkg-opt-scons-build-opts)=
:::{include} _pkg-build-opts.md
:::

(pkg-opt-scons-conf-defs)=
:::{include} _pkg-conf-defs.md
:::
:::{include} _pkg-conf-defs-example-default.md
:::

(pkg-opt-scons-conf-env)=
:::{include} _pkg-conf-env.md
:::

(pkg-opt-scons-conf-opts)=
:::{include} _pkg-conf-opts.md
:::

(pkg-opt-scons-env)=
:::{include} _pkg-env.md
:::

(pkg-opt-scons-install-defs)=
:::{include} _pkg-install-defs.md
:::
:::{include} _pkg-install-defs-example-default.md
:::

(pkg-opt-scons-install-env)=
:::{include} _pkg-install-env.md
:::

(pkg-opt-scons-install-opts)=
:::{include} _pkg-install-opts.md
:::

(pkg-opt-scons-noinstall)=
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
