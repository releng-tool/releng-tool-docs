# Alternative extensions

:::{deprecated} 2.0
The `.releng` extension is no longer recommended and will be removed in
a future release.
:::
:::{deprecated} 2.2
Extensionless configurations/scripts are no longer recommended and may
be removed in a future release.
:::
:::{versionchanged} 2.2
Extension priority orders have changed (<2.2: *(none)*, `.rt`, `.releng`,
`.py`; >=2.2: `.rt`, `.py`, *(none)*, `.releng`).
:::

A default configuration file is typically a file named `releng-tool.rt`
at the root of a project. Consider the following example of a project
with a `libfoo` package with various stage scripts:

```
└── my-project/
    ├── package/
    │   └── libfoo/
    │       └── libfoo.rt
    │       └── libfoo-build.rt
    │       └── libfoo-install.rt
    └── releng-tool.rt
```

Developers who do not prefer the `.rt` extension may use the `.py` extension.
For example, the above example is equivalent to the structure:

```
└── my-project/
    ├── package/
    │   └── libfoo/
    │       └── libfoo.py
    │       └── libfoo-build.py
    │       └── libfoo-install.py
    └── releng-tool.py
```

For a specific file to be loaded, releng-tool uses the following priority:

1. File with a `.rt` extension
1. File with a `.py` extension
1. File without an extension (*deprecated*)
1. File with a `.releng` extension (*deprecated*)

Only the first detected file will be loaded. For example, if a project has
multiple releng-tool configuration files with different extensions:

```
└── my-project/
    ├── package/
    │   └── libfoo/
    │       └── ...
    ├── releng-tool.rt
    └── releng-tool.py
```

Only the `releng-tool.rt` configuration script will be used.
