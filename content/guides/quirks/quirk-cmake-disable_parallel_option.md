# Quirk `releng.cmake.disable_parallel_option`

```{warning}
This quirk is no longer applicable as of v1.0. CMake parallelization is
now driven internally using the `CMAKE_BUILD_PARALLEL_LEVEL` environment
variable.
```

When releng-tool invokes a build stage for a CMake project, the `--parallel`
argument is used to trigger multiple jobs for a build. If running on a host
system running a version/variant of CMake which do not explicitly provide the
parallelization option, the build may fail. Users to enable the
`releng.cmake.disable_parallel_option` quirk to prevent this option from being
used:

```
releng-tool --quirk releng.cmake.disable_parallel_option
```

## See also

- [](quirks)
