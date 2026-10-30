# Deprecated package options

The following outlines deprecated configuration options for packages. It
is not recommended to use these options.

(pkg-opt-dependencies)=
### `LIBFOO_DEPENDENCIES`

:::{deprecated} 1.3
Packages should use [`LIBFOO_NEEDS`](pkg-opt-needs) instead.
:::

List of package dependencies a given project has. If a project depends on
another package, the package name should be listed in this option. This ensures
releng-tool will process packages in the proper order. The following shows an
example package `libfoo` being dependent on `liba` and `libb` being
processed first:

```python
LIBFOO_DEPENDENCIES = [
    'liba',
    'libb',
]
```

(pkg-opt-remote-config)=
## `LIBFOO_REMOTE_CONFIG`

:::{versionadded} 1.3
:::
:::{deprecated} 2.9
This feature is planned to be removed in the future v4.4 release.
:::

Flag value to indicate that a package should attempt to load any package
configurations which may be defined in the package's source. If the package
includes a `.releng-tool` file at the root of their sources, supported
configuration options that have not been populated will be registered into
the package before invoking a package's configuration stage.

```python
LIBFOO_REMOTE_CONFIG = True
```

See also
[`releng.disable_remote_configs` quirk](quirk-releng.disable_remote_configs).

(pkg-opt-remote-scripts)=
## `LIBFOO_REMOTE_SCRIPTS`

:::{versionadded} 1.3
:::
:::{deprecated} 2.9
This feature is planned to be removed in the future v4.4 release.
:::

Flag value to indicate that a package should attempt to load any package
scripts which may be defined in the package's source. Typically, a
script-based package will load configuration, build, etc. scripts from its
package definition folder. If a script-based package is missing a stage script
to invoke and finds an associated script in the package's source, the detected
script will be invoked. For example, if `libfoo.rt` package may attempt to load
a `libfoo-configure.rt` script for a configuration stage. In the event that the
script cannot be found and remote scripting is permitted for a package, the
script (if exists) `releng-configure.rt` will be loaded from the root of the
package's contents.

```python
LIBFOO_REMOTE_CONFIG = True
```

See also
[`releng.disable_remote_scripts` quirk](quirk-releng.disable_remote_scripts).
