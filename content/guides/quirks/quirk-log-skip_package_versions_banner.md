(quirk-releng.log.skip_package_versions_banner)=
{class="quirk-header"}
# Quirk `releng.log.skip_package_versions_banner`

:::{versionadded} 4.2
:::

At the start of a releng-tool run, configured package versions will be
printed to the output stream. This is to help users actively inspect configured
revisions at the start of a possible long run. For users not wanting to display
this information in their logs, the `releng.log.skip_package_versions_banner`
quirk can be used. For example, using the command line:

```
releng-tool --quirk releng.log.skip_package_versions_banner
```

Or adding in the project configuration:

```python
releng_config(
    ...
    quirks=[
        ...
        'releng.log.skip_package_versions_banner',
    ],
)
```

## See also

- [](quirks)
