# CMake package

:::{versionchanged} 2.6
releng-tool now populates `CMAKE_FIND_ROOT_PATH`.
:::

A CMake package provides support for processing a [CMake][cmake] supported
module.

```python
LIBFOO_TYPE = 'cmake'
```

During the configuration stage of a CMake package, `cmake` will be invoked to
generate build files for the module. For the build stage, `cmake --build` will
invoke the generated build files. Similar approach for the installation stage
where the build option is invoked again but with the `install` target invoked:
`cmake --build --target install`. Each stage can be configured to manipulate
environment variables and options used by the CMake executable.

The default configuration built for projects is `RelWithDebInfo`. A developer
can override this option by explicitly adjusting the configuration option
`LIBFOO_CMAKE_BUILD_TYPE` to, for example, `Debug`:

```python
LIBFOO_CMAKE_BUILD_TYPE = 'Debug'
```

Packages can be configured with a toolchain using with the define
[`CMAKE_TOOLCHAIN_FILE`][cmake-toolchain-file] (via
[`LIBFOO_CONF_DEFS`](pkg-opt-cmake-conf-defs)) or using the command line option
[`--toolchain`][cmake-opt-toolchain] (via
[`LIBFOO_CONF_OPTS`](pkg-opt-cmake-conf-opts)). releng-tool will provide
required staging/target paths through the
[`CMAKE_FIND_ROOT_PATH`][cmake-find-root-path] configuration. Ensure the
toolchain configuration accepts `CMAKE_FIND_ROOT_PATH` hints. For example,
using either:

```
list(APPEND CMAKE_FIND_ROOT_PATH "INTERNAL_SDK_PATH")
```

Or:

```
if(NOT DEFINED CMAKE_FIND_ROOT_PATH)
    set(CMAKE_FIND_ROOT_PATH "INTERNAL_SDK_PATH")
endif()
```

The following shows the default arguments used in stages and outlines
configuration options that are available for an CMake package to set.
See also the [CMake package examples](/examples/examples-cmake). All stages
are invoked with a [`PKG_BUILD_DIR`](env-pkg-build-dir) working directory.

````{tab} Configuration
```{eval-rst}
.. only:: latex

    Configuration stage
    -------------------
```

The configuration stage invokes `cmake` with the arguments:

```none
cmake -C <RELENG-TOOL-CONFIG-CACHE> <PROJECT_DIR>
```

With the configuration cache that populates the options:

```none
CMAKE_<LANG>_STANDARD_INCLUDE_DIRECTORIES=<INCLUDE_PATHS>
CMAKE_BUILD_TYPE=<BUILD_TYPE>
CMAKE_FIND_ROOT_PATH=<SYSROOT_PATHS>
CMAKE_FIND_ROOT_PATH_MODE_PROGRAM=NEVER
CMAKE_INCLUDE_PATH=<INCLUDE_PATHS>
CMAKE_INSTALL_LIBDIR="lib"
CMAKE_INSTALL_PREFIX=<PREFIX>
CMAKE_LIBRARY_PATH=<LIBRARY_PATHS>
CMAKE_MODULE_PATH=<MODULE_PATHS>
CMAKE_SKIP_INSTALL_ALL_DEPENDENCY=ON
```

The project directory is configured to [`PKG_BUILD_DIR`](env-pkg-build-dir).

The build type is configured by
[`LIBFOO_CMAKE_BUILD_TYPE`](pkg-opt-cmake-build-type).

Paths may vary based on how the package's
[`LIBFOO_INSTALL_TYPE`](pkg-opt-install-type) is configured. System root paths
provided will only include the staging directory if `staging` is configured.
Both the staging and target directories are provided is the `target` is
configured. Likewise with the host directory if `host` is configured.

The same concepts apply for defined include (`<sysroot>[/<prefix>]/include`),
library (`<sysroot>[/<prefix>]/lib`) and module paths
(`<sysroot>[/<prefix>]/share/cmake/Modules`).

Packages may override default defines using the
[`LIBFOO_CONF_DEFS`](pkg-opt-cmake-conf-defs) option.

A package may opt-out of configuring `CMAKE_<LANG>_STANDARD_INCLUDE_DIRECTORIES`
variables using the
[`releng.cmake.disable_direct_includes`](quirk-releng.cmake.disable_direct_includes)
quirk.
````

````{tab} Build
```{eval-rst}
.. only:: latex

    Build stage
    -----------
```

The build stage invokes `cmake` with the arguments:

```none
cmake --build <BUILD_OUTPUT_DIR> --config <BUILD_TYPE>
```

With the following environment variables set:

```none
CMAKE_BUILD_PARALLEL_LEVEL=<NJOBS>
```

The `--build` directory is configured to
[`PKG_BUILD_OUTPUT_DIR`](env-pkg-build-output-dir).

The `--config` type is configured to the value defined for
[`LIBFOO_CMAKE_BUILD_TYPE`](pkg-opt-cmake-build-type). Although, this option
may not be applicable/used in all build environments.

The environment variable `CMAKE_BUILD_PARALLEL_LEVEL` is populated by either
the [`--jobs` argument](arg-jobs) or [`LIBFOO_FIXED_JOBS`](pkg-opt-fixed-jobs).
Although, if the configuration results in a single job, the environment
variable will not be set.
````

````{tab} Install
```{eval-rst}
.. only:: latex

    Install stage
    -------------
```

The install stage invokes `cmake` with the arguments:

```none
cmake \
    --build <BUILD_OUTPUT_DIR> \
    --config <BUILD_TYPE> \
    --target install
```

With the following environment variables set:

```none
CMAKE_INSTALL_ALWAYS=1
DESTDIR=<TARGET_DIR>
```

The `--build` directory is configured to
[`PKG_BUILD_OUTPUT_DIR`](env-pkg-build-output-dir).

The `--config` type is configured to the value defined for
[`LIBFOO_CMAKE_BUILD_TYPE`](pkg-opt-cmake-build-type). Although, this option
may not be applicable/used in all build environments.

The `DESTDIR` path will be set to the target sysroot the package should
install into (see also [`LIBFOO_INSTALL_TYPE`](pkg-opt-install-type)).
`cmake` may be invoked multiple times for each target it needs to install into.

The installation stage can be skipped by configuring
[`LIBFOO_CMAKE_NOINSTALL`](pkg-opt-cmake-noinstall).
````

(pkg-opt-cmake-build-defs)=
:::{include} _pkg-build-defs.md
:::
:::{include} _pkg-build-defs-example-dentry.md
:::

(pkg-opt-cmake-build-env)=
:::{include} _pkg-build-env.md
:::

(pkg-opt-cmake-build-opts)=
:::{include} _pkg-build-opts.md
:::

(pkg-opt-cmake-build-type)=
## `LIBFOO_CMAKE_BUILD_TYPE`

:::{versionadded} 0.17
:::

Specifies the [build type][cmake-build-type] used for the CMake package.
A package may use a common build type (`Debug`, `Release`, `RelWithDebInfo`
or `MinSizeRel`), or may have a custom build type defined. A developer
needing to use a specific build type can configure this option with the
name of the configuration. By default, the `RelWithDebInfo` build type is
used for all CMake packages.

```python
LIBFOO_CMAKE_BUILD_TYPE = 'Debug'
```

(pkg-opt-cmake-noinstall)=
## `LIBFOO_CMAKE_NOINSTALL`

:::{versionadded} 0.10
:::

Specifies whether the CMake package should skip an attempt to invoke the
install command. Ideally, projects will have an [install][cmake-install]
rule configured to define how a project will install files into a target (or
staging) environment. Not all CMake projects may have this rule defined, which
can cause the installation stage for a package to fail. A developer can
specify this no-install flag to skip a CMake-driven install request and
manage installation actions through other means (such as post-processing).
By default, the installation stage is invoked with a value of `False`.

```python
LIBFOO_CMAKE_NOINSTALL = True
```

(pkg-opt-cmake-conf-defs)=
:::{include} _pkg-conf-defs.md
:::
:::{include} _pkg-conf-defs-example-dentry.md
:::

(pkg-opt-cmake-conf-env)=
:::{include} _pkg-conf-env.md
:::

(pkg-opt-cmake-conf-opts)=
:::{include} _pkg-conf-opts.md
:::

(pkg-opt-cmake-env)=
:::{include} _pkg-env.md
:::

(pkg-opt-cmake-install-defs)=
:::{include} _pkg-install-defs.md
:::
:::{include} _pkg-install-defs-example-dentry.md
:::

(pkg-opt-cmake-install-env)=
:::{include} _pkg-install-env.md
:::

(pkg-opt-cmake-install-opts)=
:::{include} _pkg-install-opts.md
:::


[cmake-build-type]: https://cmake.org/cmake/help/latest/variable/CMAKE_BUILD_TYPE.html
[cmake-find-root-path]: https://cmake.org/cmake/help/latest/variable/CMAKE_FIND_ROOT_PATH.html
[cmake-install]: https://cmake.org/cmake/help/latest/command/install.html
[cmake-opt-toolchain]: https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-toolchain
[cmake-toolchain-file]: https://cmake.org/cmake/help/latest/variable/CMAKE_TOOLCHAIN_FILE.html
[cmake]: https://cmake.org/
