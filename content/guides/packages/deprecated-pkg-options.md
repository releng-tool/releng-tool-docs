# Deprecated package options

The following outlines deprecated configuration options for packages. It
is not recommended to use these options.

(pkg-opt-dependencies)=
### `LIBFOO_DEPENDENCIES`

:::{warning}
The option is deprecated and packages should use
[`LIBFOO_NEEDS`](pkg-opt-needs) instead.
:::

List of package dependencies a given project has. If a project depends on
another package, the package name should be listed in this option. This ensures
releng-tool will process packages in the proper order. The following shows an
example package `libfoo` being dependent on `liba` and `libb` being
processed first:

```python
LIBFOO_DEPENDENCIES = [
    'liba',
    'libb',
]
```
