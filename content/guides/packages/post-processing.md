# Package post-processing

Every package, no matter which package [`LIBFOO_TYPE`](pkg-opt-type) is
defined, can create a post-processing script to invoke after a package
has completed an installation stage. The existence of a `<package>-post`
inside a package directory will trigger the post-processing stage for
the package. An example post-processing script for a package `libfoo`
would be named `libfoo-post`:

```
└── my-releng-tool-project/
    ├── package/
    │   └── libfoo/
    │       └── libfoo
    │       └── libfoo-post           <----
    ...
```

With the contents of `libfoo-post` being set to:

```python
 print('perform post-processing work')
```

May generate an output such as follows:

```shell-session
$ releng-tool libfoo
patching libfoo...
configuring libfoo...
building libfoo...
installing libfoo...
perform post-processing work
```

Post-processing scripts for a package are optional. If no post-processing
script is provided for a package, no post-processing stage will be performed
for the package.

See [script helpers](/guides/script-helpers) for helper functions and
variables available for use. Developers may also be interested in using a
[bootstrapping script](bootstrapping).