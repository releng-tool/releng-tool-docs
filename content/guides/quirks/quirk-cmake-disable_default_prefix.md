(quirk-releng.cmake.disable_default_prefix)=
# Quirk `releng.cmake.disable_default_prefix`

For CMake-based projects, releng-tool will populate
[`CMAKE_PREFIX_PATH`][cmake-prefix-path] to paths applicable for a package.
This is to help packages find dependencies using find operations using
["Config" mode][cmake-cfg-mode].

While the use of this configuration should work for most scenarios, it may
be problematic for project's using CMake toolchain definitions with
cross-compiling considerations. For example, a toolchain configuration may setup
[`CMAKE_FIND_ROOT_PATH_MODE_PROGRAM`][cmake-find-root-path-mode-program] to not
be `NEVER`. In turn, if a package is aimed to be cross-compiled and find
operations are performed for executables, the CMake project may find staging
executables that cannot run on the host system.

One workaround for a package is to override/unset the `CMAKE_PREFIX_PATH`
option to use a default/unset value:

```
LIBFOO_CONF_DEFS = {
    'CMAKE_PREFIX_PATH': None,
}
```

However, if multiple packages are a concern for a project, developers may
utilizes this quirk to disable this feature. The feature can be disabled using
the `releng.cmake.disable_default_prefix` quirk using the command line:

```
releng-tool --quirk releng.cmake.disable_default_prefix
```

Or adding in the project configuration:

```python
releng_config(
    ...
    quirks=[
        ...
        'releng.cmake.disable_default_prefix',
    ],
)
```

Note, once disabled, individual packages may need to explicitly configure
paths for various dependencies that a project relies on "Config" mode
resolutions.

## See also

- [`CMAKE_PREFIX_PATH`][cmake-prefix-path]
- [](quirks)


[cmake-cfg-mode]: https://cmake.org/cmake/help/latest/command/find_package.html#config-mode-search-procedure
[cmake-find-root-path-mode-program]: https://cmake.org/cmake/help/latest/variable/CMAKE_FIND_ROOT_PATH_MODE_PROGRAM.html
[cmake-prefix-path]: https://cmake.org/cmake/help/latest/variable/CMAKE_PREFIX_PATH.html
