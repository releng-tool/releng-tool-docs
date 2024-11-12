# Script package (default)

A script-based package is the most basic package type available. By default,
packages are considered to be script packages unless explicitly configured
to be another package type ([`LIBFOO_TYPE`](pkg-opt-type)). If a developer
wishes to explicitly configure a project as script-based, the following
configuration can be used:

```python
LIBFOO_TYPE = 'script'
```

A script package has the ability to define three Python stage scripts:

- `<package>-configure.rt` - script to invoke during the configuration stage
- `<package>-build.rt` - script to invoke during the build stage
- `<package>-install.rt` - script to invoke during the installation stage

For example, a `libfoo` package would have the following files for a
script-based package:

```
└── my-releng-tool-project/
    ├── package/
    │   └── libfoo/
    │       ├── libfoo.rt
    │       ├── libfoo-build.rt
    │       ├── libfoo-configure.rt
    │       └── libfoo-install.rt
    ...
```

An example build script (`libfoo-build.rt`) can be as follows:

```python
releng_execute(['make'])
```

When a package performs a configuration, build or installation stage; the
respective script (mentioned above) will be invoked. Package scripts are
optional. If a script is not provided for a stage, the stage will be
skipped.

See also [script helpers](/guides/script-helpers) for helper functions and
variables available for use, as well as [bootstrapping](bootstrapping) or
[post-processing](post-processing) for more stage script support.
