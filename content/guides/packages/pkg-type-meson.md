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
can override this option by explicitly adjusting the configuration option
`LIBFOO_MESON_BUILD_TYPE` to, for example, `debug`:

```python
LIBFOO_MESON_BUILD_TYPE = 'debug'
```

The following shows the default arguments used in stages and outlines
configuration options that are available for a Meson package to set.
See also the [Meson package examples](/examples/examples-meson). All stages
are invoked with a [`PKG_BUILD_DIR`](env-pkg-build-dir) working directory.

````{tab} Configuration
```{eval-rst}
.. only:: latex

    Configuration stage
    -------------------
```

The configuration stage invokes `meson` with the arguments:

```none
meson setup \
    --buildtype debugoptimized \
    -Dcmake_prefix_path=<SYSROOT_PATHS> \
    -Dlibdir=lib \
    -Dpkg_config_path=<SYSROOT_PKGCFG_PATHS> \
    -Dprefix=<PREFIX> \
    -Dwrap_mode=nodownload \
    <BUILD_OUTPUT_DIR>
```

The build type is configured by
[`LIBFOO_MESON_BUILD_TYPE`](pkg-opt-meson-build-type).

The build output directory is configured to
[`PKG_BUILD_OUTPUT_DIR`](env-pkg-build-output-dir).

Paths may vary based on how the package's
[`LIBFOO_INSTALL_TYPE`](pkg-opt-install-type) is configured. System root paths
provided will only include the staging directory if `staging` is configured.
Both the staging and target directories are provided is the `target` is
configured. Likewise with the host directory if `host` is configured.
pkg-config paths are defined to `<sysroot>/lib/pkgconfig`.

If [`LIBFOO_PREFIX`](pkg-opt-prefix) resolves to an empty prefix, the
`-Dprefix` define is not provided.

In the event that a package is reconfigured (e.g.
[`<pkg>-reconfigure`](action-pkg-reconfigure)), the `--reconfigure` argument
will also be included.
````

````{tab} Build
```{eval-rst}
.. only:: latex

    Build stage
    -----------
```

The build stage invokes `meson` with the arguments:

```none
meson compile -C <BUILD_OUTPUT_DIR> --jobs <NJOBS>
```

The `-C` directory is configured to
[`PKG_BUILD_OUTPUT_DIR`](env-pkg-build-output-dir).

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

The install stage invokes `meson` with the arguments:

```none
meson install -C <BUILD_OUTPUT_DIR> --destdir <TARGET_DIR> --no-rebuild
```

With the following environment variables set:

```none
DESTDIR=<TARGET_DIR>
```

The `-C` directory is configured to
[`PKG_BUILD_OUTPUT_DIR`](env-pkg-build-output-dir).

The `--destdir` argument and `DESTDIR` environment path will be set to the
target sysroot the package should install into (see also
[`LIBFOO_INSTALL_TYPE`](pkg-opt-install-type)). `meson install` may be invoked
multiple times for each target it needs to install into.

The installation stage can be skipped by configuring
[`LIBFOO_MESON_NOINSTALL`](pkg-opt-meson-noinstall).
````

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

(pkg-opt-meson-build-type)=
## `LIBFOO_MESON_BUILD_TYPE`

:::{versionadded} 2.7
:::

Specifies the [build type][meson-build-type] used for the Meson package.
A package may use a Meson-supported build type (`plain`, `debug`,
`debugoptimized`, `release` or `minsize`). A developer needing to use a
specific build type can configure this option with the name of the
configuration. By default, the `debugoptimized` build type is used for all
Meson packages.

```python
LIBFOO_MESON_BUILD_TYPE = 'debugoptimized'
```

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


[meson-build-type]: https://mesonbuild.com/Builtin-options.html#details-for-buildtype
[meson-install]: https://mesonbuild.com/Commands.html#install
[meson]: https://mesonbuild.com/
