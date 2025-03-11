(quirk-releng.disable_verbose_patch)=
# Quirk `releng.disable_verbose_patch`

:::{versionadded} 2.2
:::

When utilizing [patching](/guides/patching) capabilities in releng-tool,
all patches are by default applied with a `--verbose` argument. If this
is not preferred by a project, this quirk can be set to omit the argument.

```
releng-tool --quirk releng.disable_verbose_patch
```

## See also

- [Patching](/guides/patching)
- [](quirks)
