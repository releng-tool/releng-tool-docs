# Alternative extensions

A default configuration file is typically a file named `releng` at the root
of a project. Consider the following example of a project with a `libfoo`
package with various stage scripts:

```
└── my-project/
    ├── package/
    │   └── libfoo/
    │       └── libfoo
    │       └── libfoo-build
    │       └── libfoo-install
    └── releng
```

If a developer prefers to define extensions for various configurations and
scripts, files detected with a `.releng` or `.py` extensions can be used
instead. For example, the above example is equivalent to the structure:

```
└── my-project/
    ├── package/
    │   └── libfoo/
    │       └── libfoo.releng
    │       └── libfoo-build.releng
    │       └── libfoo-install.releng
    └── releng.releng
```

Or the structure:

```
└── my-project/
    ├── package/
    │   └── libfoo/
    │       └── libfoo.py
    │       └── libfoo-build.py
    │       └── libfoo-install.py
    └── releng.py
```

For a specific file to be loaded, releng-tool uses the following priority:

1. File without an extension
2. File with a `.releng` extension
3. File with a `.py` extension

Only the first detected file will be loaded. For example, if a project has
multiple releng-tool configuration files with different extensions:

```
└── my-project/
    ├── package/
    │   └── libfoo/
    │       └── ...
    ├── releng
    ├── releng.releng
    └── releng.py
```

Only the `releng` configuration script will be used.
