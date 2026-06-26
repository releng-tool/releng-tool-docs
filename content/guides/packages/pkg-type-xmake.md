# Xmake package

:::{versionadded} 3.1
:::

An Xmake package provides support for processing an [Xmake][xmake] supported
module.

```python
LIBFOO_TYPE = 'xmake'
```

During the configuration stage of an Xmake package, `xmake config` will be
invoked to generate build files for the module. For the build stage,
`xmake build` will invoke the generated build files. For the installation
stage (if enabled), `xmake install` will be used. Each stage can be
configured to manipulate environment variables and options used by Xmake.

The default configuration applies no explicit mode. A developer can set this
option to a supported mode of the project by explicitly adjusting the
configuration option `LIBFOO_XMAKE_BUILD_TYPE` to, for example, `debug`:

```python
LIBFOO_XMAKE_BUILD_TYPE = 'debug'
```

The following shows the default arguments used in stages and outlines
configuration options that are available for an Xmake package to set.
See also the [Xmake package examples](/examples/examples-xmake). All stages
are invoked with a [`PKG_BUILD_DIR`](env-pkg-build-dir) working directory.

````{tab} Configuration
```{eval-rst}
.. only:: latex

    Configuration stage
    -------------------
```

The configuration stage invokes `xmake` with the arguments:

```none
xmake config \
    --includedirs=<SYSROOT_INCLUDE_PATHS> \
    --linkdirs=<SYSROOT_LIBRARY_PATHS> \
    --mode=<MODE> \
    -o <BUILD_OUTPUT_DIR>
```

With the following environment variables set:

```none
XMAKE_CONFIGDIR=<BUILD_OUTPUT_DIR>
XMAKE_GLOBALDIR=<BUILD_BASE_DIR>/.releng-tool-xmake-global
```

The mode/build type can configured by
[`LIBFOO_XMAKE_BUILD_TYPE`](pkg-opt-xmake-build-type). If no mode is
configured, the `--mode` argument will not be used.

The build output directory is configured to
[`PKG_BUILD_OUTPUT_DIR`](env-pkg-build-output-dir).

Paths may vary based on how the package's
[`LIBFOO_INSTALL_TYPE`](pkg-opt-install-type) is configured. For example,
system include/library paths provided will only include the staging directory 
if `staging` is configured. Likewise, both the staging and target directories
are provided when using `staging_and_target`.
````

````{tab} Build
```{eval-rst}
.. only:: latex

    Build stage
    -----------
```

The build stage invokes `xmake` with the arguments:

```none
xmake build --jobs <NJOBS>
```

With the following environment variables set:

```none
XMAKE_CONFIGDIR=<BUILD_OUTPUT_DIR>
XMAKE_GLOBALDIR=<BUILD_BASE_DIR>/.releng-tool-xmake-global
```

The number of jobs is populated by either the [`--jobs` argument](arg-jobs),
[`LIBFOO_FIXED_JOBS`](pkg-opt-fixed-jobs) or
[`LIBFOO_MAX_JOBS`](pkg-opt-max-jobs). Although, if the configuration results
in a single job, the argument will not be used.
````

````{tab} Install
```{eval-rst}
.. only:: latex

    Install stage
    -------------
```

The install stage invokes `xmake` with the arguments:

```none
xmake install --installdir <TARGET_DIR>
```

With the following environment variables set:

```none
XMAKE_CONFIGDIR=<BUILD_OUTPUT_DIR>
XMAKE_GLOBALDIR=<BUILD_BASE_DIR>/.releng-tool-xmake-global
```

The `--installdir` argument will be set to the target sysroot the package
should install into (see also [`LIBFOO_INSTALL_TYPE`](pkg-opt-install-type)).
`xmake install` may be invoked multiple times for each target it needs to
install into.

The installation stage can be skipped by configuring
[`LIBFOO_XMAKE_NOINSTALL`](pkg-opt-xmake-noinstall).
````

(pkg-opt-xmake-build-defs)=
:::{include} _pkg-build-defs.md
:::
:::{include} _pkg-build-defs-example-default.md
:::

(pkg-opt-xmake-build-env)=
:::{include} _pkg-build-env.md
:::

(pkg-opt-xmake-build-opts)=
:::{include} _pkg-build-opts.md
:::

(pkg-opt-xmake-conf-defs)=
:::{include} _pkg-conf-defs.md
:::
:::{include} _pkg-conf-defs-example-default.md
:::

(pkg-opt-xmake-conf-env)=
:::{include} _pkg-conf-env.md
:::

(pkg-opt-xmake-conf-opts)=
:::{include} _pkg-conf-opts.md
:::

(pkg-opt-xmake-env)=
:::{include} _pkg-env.md
:::

(pkg-opt-xmake-install-defs)=
:::{include} _pkg-install-defs.md
:::
:::{include} _pkg-install-defs-example-default.md
:::

(pkg-opt-xmake-install-env)=
:::{include} _pkg-install-env.md
:::

(pkg-opt-xmake-install-opts)=
:::{include} _pkg-install-opts.md
:::

(pkg-opt-xmake-build-type)=
## `LIBFOO_XMAKE_BUILD_TYPE`

Specifies the [mode][xmake-mode] to use for the Xmake package. Modes
for an individual package may vary as a project file (`xmake.lua`) defines
modes it supports (although commonly named modes include `debug`, `release`,
`releasedbg` and `minsizerel`). A developer needing to use a specific mode
can configure this option with the name of the mode. By default, no explicit
mode is used for all Xmake packages.

```python
LIBFOO_XMAKE_BUILD_TYPE = 'releasedbg'
```

See also [`default_xmake_build_type`](conf-default-xmake-build-type).

(pkg-opt-xmake-noinstall)=
## `LIBFOO_XMAKE_NOINSTALL`

Specifies whether the Xmake package should skip an attempt to invoke the
install command. Ideally, projects will have an [install][xmake-install]
options configured to define how a project will install files into a target
(or staging) environment. Not all Xmake projects have installation options
configured, or there can be cases where installation stage for a package to
fail due to issues with some host environments. A developer can specify this
no-install flag to skip an Xmake-driven install request and manage installation
actions through other means (such as post-processing). By default, the
installation stage is invoked with a value of `False`.

```python
LIBFOO_XMAKE_NOINSTALL = True
```


[xmake-install]: https://xmake.io/guide/basic-commands/install-and-uninstall.html
[xmake-mode]: https://xmake.io/posts/quickstart-8-switch-build-mode.html
[xmake]: https://xmake.io/
