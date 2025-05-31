(quirk-releng.disable_devmode_ignore_cache)=
# Quirk `releng.disable_devmode_ignore_cache`

:::{versionadded} 2.4
:::

Packages may be configured with
[`LIBFOO_DEVMODE_IGNORE_CACHE`](pkg-opt-devmode-ignore-cache) to always attempt
a new fetch of sources for a development-configured revision. However, if a
remote is not available during a rebuild event, the process will fail since
the package cannot be re-fetched from the configured site. To help a builder
hint that using the cache is fine for an invoke, this quirk can be provided to
avoid any re-fetch attempt.

```
releng-tool --quirk releng.disable_devmode_ignore_cache
```

## See also

- [](quirks)
