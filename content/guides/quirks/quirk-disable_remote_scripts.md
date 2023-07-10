# Quirk `releng.disable_remote_scripts`

releng-tool package sources have the ability to define configuration,
build and installation stage scripts from a remote source. If a user is
having issues with a project's remote scripts for a package, the
`releng.disable_remote_scripts` quirk can be used to skip any invoke of
these scripts:
  
```
releng-tool --quirk releng.disable_remote_scripts
```

## See also

- [](quirks)
