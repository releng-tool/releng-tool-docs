# Quirks

releng-tool also provides a series of configuration quirks to change the
default running state of a releng-tool run. This can be used to help manage
rare host environment scenarios where releng-tool may be experiencing issues.

## Command line quirks

Quirks for a run can be enabled through the command line. releng-tool accepts
`--quirk <quirk-id>` argument, for example:

```
releng-tool --quirk releng.some_quirk_id
```

If multiple quirks are desired, the quirk argument can be provided multiple
times:

```
releng-tool --quirk releng.quirk1 --quirk releng.quirk2
```

Configuration quirks do not persist and need to be utilized each run of
releng-tool.

## Configuration-driven quirks

Quirks can also be enabled through configuration override scripts. This can
be used in certain build scenarios where defining a script override is
easier than specifying multiple command line options.

For example, if an override script
[`releng-overrides`](/guides/configuration-overrides) is created, the following
can be used to enable one or more quirks for a releng-tool run:

```python
quirks = [
    'releng.quirk1',
    'releng.quirk2',
    ...
]
```

## Available quirks

The following is a list of all available quirks supported by releng-tool:

:::{toctree}
:maxdepth: 1

releng.bzr.certifi <quirk-bzr-certifi>
releng.cmake.disable_direct_includes <quirk-cmake-disable_direct_includes>
releng.cmake.disable_parallel_option <quirk-cmake-disable_parallel_option>
releng.disable_prerequisites_check <quirk-disable_prerequisites_check>
releng.disable_remote_configs <quirk-disable_remote_configs>
releng.disable_remote_scripts <quirk-disable_remote_scripts>
releng.disable_spdx_check <quirk-disable_spdx_check>
releng.git.no_depth <quirk-git-no_depth>
releng.git.no_quick_fetch <quirk-git-no_quick_fetch>
releng.stats.no_pdf <quirk-stats-no_pdf>
:::
