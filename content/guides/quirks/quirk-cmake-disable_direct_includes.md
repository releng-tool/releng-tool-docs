# Quirk `releng.cmake.disable_direct_includes`

For CMake-based projects, releng-tool will populate a series of include
directories (internally or from a project's configuration definition) to
configure a CMake project with. These include paths will be populated into
the [`CMAKE_INCLUDE_PATH`][cmake-include-path] option when generating native
build scripts.

In addition to `CMAKE_INCLUDE_PATH`, releng-tool will also populate multiple
language type's
[`CMAKE_<LANG>_STANDARD_INCLUDE_DIRECTORIES`][cmake-std-includes] as well.
This registers convenient include paths for languages (e.g. C/C++), avoiding
the need for project definitions to explicitly configure common include paths
in host, staging or target areas.

However, if this causes issues for a build environment (such as when building
a CMake project with a toolchain file which has issues with standard include
overrides), the option can be disabled using the
`releng.cmake.disable_direct_includes` quirk:


```
releng-tool --quirk releng.cmake.disable_direct_includes
```

## See also

- [`CMAKE_<LANG>_STANDARD_INCLUDE_DIRECTORIES`][cmake-std-includes]
- [`CMAKE_INCLUDE_PATH`][cmake-include-path]
- [](quirks)


[cmake-std-includes]: https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_STANDARD_INCLUDE_DIRECTORIES.html
[cmake-include-path]: https://cmake.org/cmake/help/latest/variable/CMAKE_INCLUDE_PATH.html
