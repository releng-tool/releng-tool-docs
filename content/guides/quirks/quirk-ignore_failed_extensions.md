(quirk-releng.ignore_failed_extensions)=
# Quirk `releng.ignore_failed_extensions`

:::{versionadded} 2.7
:::

For projects that configure extensions, if an extension fails to load (either
missing or a bad extension definition), the releng-tool process will stop with
an error.

If a user wants to ignore the failed loading of extension for a given run,
they may do so by configuring the `releng.ignore_failed_extensions` quirk.

```
releng-tool --quirk releng.ignore_failed_extensions
```

## See also

- [](quirks)
