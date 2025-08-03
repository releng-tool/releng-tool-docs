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
`--config` to, for example, `Debug`:

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

The following sections outline configuration options are available for a CMake
package.

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
