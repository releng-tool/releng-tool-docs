# Offline builds

A user can prepare for an offline build by using the `fetch` action:

```shell
releng-tool fetch
```

Package content will be downloaded into the respective `dl/` or `cache/`
folders into the output directory. Future builds for the project should no
longer need external access until these folders are removed.

:::{note}
There are a few exceptions where offline builds may not function as expected.

1. If running in a development mode and a package definition defines a
   [`LIBFOO_DEVMODE_IGNORE_CACHE`](pkg-opt-devmode-ignore-cache) configuration,
   updated sources will be re-fetched each time.
2. If a developer defines a package definition or a post-build script which
   performs fetch-like calls (e.g. if custom files are downloaded when running
   a `libfoo-build` script), releng-tool will not stop the script from
   performing this request. Offline builds are only possible if developers
   define their projects in a way where fetching-like operations only occur
   during a fetch-stage.
:::
