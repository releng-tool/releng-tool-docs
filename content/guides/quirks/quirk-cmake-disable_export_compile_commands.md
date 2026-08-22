(quirk-releng.cmake.disable_export_compile_commands)=
{class="quirk-header"}
# Quirk `releng.cmake.disable_export_compile_commands`

For CMake-based projects, releng-tool will populate
[`CMAKE_EXPORT_COMPILE_COMMANDS`][cmake-export-cc] to an enabled state. This is
to help developers by default have a compilation database available for
inspection and use by supplementary tooling.

If enabling this feature causes issues for a package, it can be disabled by
configuring the `CMAKE_EXPORT_COMPILE_COMMANDS` option to use an unset value:

```python
LIBFOO_CONF_DEFS = {
    'CMAKE_EXPORT_COMPILE_COMMANDS': None,
}
```

However, if multiple packages have issues, developers may utilizes this quirk
to disable this feature. The feature can be disabled using the
`releng.cmake.disable_export_compile_commands` quirk using the command line:

```
releng-tool --quirk releng.cmake.disable_export_compile_commands
```

Or adding in the project configuration:

```python
releng_config(
    ...
    quirks=[
        ...
        'releng.cmake.disable_export_compile_commands',
    ],
)
```

## See also

- [`CMAKE_EXPORT_COMPILE_COMMANDS`][cmake-export-cc]
- [](quirks)


[cmake-export-cc]: https://cmake.org/cmake/help/latest/variable/CMAKE_EXPORT_COMPILE_COMMANDS.html
