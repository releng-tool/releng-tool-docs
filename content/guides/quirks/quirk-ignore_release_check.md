(quirk-releng.ignore_release_check)=
# Quirk `releng.ignore_release_check`

```{warning}
Using this option is never recommended since it overrides the purpose of
release checks. The quick is solely available to help special corner cases
for developers.
```

:::{versionadded} 3.1
:::

Users may invoke releng-tool in a [release mode](/guides/release-checks). If
a user is experiencing an odd corner case or a development scenario where they
wish to permit a build to continue even if a release check has been triggered,
they may do so by configuring the `releng.ignore_release_check` quirk.
For example, using the command line:

```
releng-tool --quirk releng.ignore_release_check
```

Or adding in the project configuration:

```
quirks = [
    ...
    'releng.ignore_release_check',
]
```

## See also

- [](quirks)
