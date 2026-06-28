# Release Mode

:::{versionadded} 3.1
:::

Users can invoke releng-tool in a "release mode". It can be used to sanity
check a run is using a runtime configuration appropriate for a release. This
mode can be enabled using the [`--release` argument](arg-release). For example:

```
releng-tool --release
```

What a release means for developers may vary, but there are some options
releng-tool can determine that should not be applied for a typical release.
A series of checks are performed. In the event that a check detects a runtime
configuration state that should not be used for a release, releng-tool will
stop.

Checks performed include:

- Verify no actions are being used (e.g. running only `libfoo-build`).
- Verify not running in a [development mode](development-mode).
- Verify not running in a [local-sources mode](local-sources-mode).
- Verify [`LIBFOO_FORCE_REVISION`](pkg-opt-force-revision) is not used.

When running in a release mode, releng-tool will also set the
[`RELENG_RELEASE`](env-releng-release) variable. Developers can utilize this
in their own projects for additional checks. For example:

```python
if RELENG_RELEASE:
    if <some-condition>:
        releng_exit('failed a release pre-check')
```
