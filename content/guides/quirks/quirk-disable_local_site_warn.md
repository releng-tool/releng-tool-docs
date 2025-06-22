(quirk-releng.disable_local_site_warn)=
# Quirk `releng.disable_local_site_warn`

:::{versionadded} 1.4
:::
:::{deprecated} 2.5
This quirk is no longer applicable. releng-tool will no longer generate
a warning when using a local package.
:::

Users can create packages using a [local site](site-local) for initial
development and testing scenarios. However, using local sites is not
recommended for long-term use; hence a warning is generated when
releng-tool runs. While the warning aims to promote a user to move the
package into their own site of some sort (e.g. Git), a user may be good
enough with using a specific package as a local one. For such cases,
using this quirk can prevent any warnings generated when a local site is
used.

```
releng-tool --quirk releng.disable_local_site_warn
```

## See also

- [](quirks)
