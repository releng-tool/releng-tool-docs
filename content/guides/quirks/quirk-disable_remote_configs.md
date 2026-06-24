(quirk-releng.disable_remote_configs)=
# Quirk `releng.disable_remote_configs`

releng-tool package sources have the ability to inject late-stage
configuration options from a remote source. If a user is having issues
with a project's remote options for a package, the
`releng.disable_remote_configs` quirk can be used to skip any application
of late-stage configuration options using the command line:
  
```
releng-tool --quirk releng.disable_remote_configs
```

Or adding in the project configuration:

```
quirks = [
    ...
    'releng.disable_remote_configs',
]
```

## See also

- [](quirks)
