(quirk-releng.xmake.disable_deps_init)=
# Quirk `releng.xmake.disable_deps_init`

releng-tool will default generate Xmake dependency folders for configured
modes. This involves detecting available targets of a package, along with
knowing the mode, to generate these folders. This is performed since in
some environment (e.g. OS X), it has been observed that dependencies may
fail to install when Xmake believes the parent folder of a dependency exists
but does not.

Not all environments require pre-building these folders. If a developer
experiences issues when pre-building dependency folders, this feature can be
disabled using the quirk `releng.xmake.disable_deps_init`:

```
releng-tool --quirk releng.xmake.disable_deps_init
```

## See also

- [](quirks)
