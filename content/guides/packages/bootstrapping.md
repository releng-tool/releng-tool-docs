# Package bootstrapping

Every package, no matter which package [`LIBFOO_TYPE`](pkg-opt-type) is
defined, can create a bootstrapping script to invoke before a package
starts a configuration stage. The existence of a `<package>-bootstrap.rt`
inside a package directory will trigger the bootstrapping stage for the
package. An example bootstrapping script for a package `libfoo` would be
named `libfoo-bootstrap.rt`:

```
└── my-releng-tool-project/
    ├── package/
    │   └── libfoo/
    │       ├── libfoo.rt
    │       └── libfoo-bootstrap.rt   <----
    ...
```

With the contents of `libfoo-bootstrap.rt` being set to:

```python
 print('perform bootstrapping work')
```

May generate an output such as follows:

```shell-session
$ releng-tool libfoo
patching libfoo...
perform bootstrapping work
configuring libfoo...
building libfoo...
installing libfoo...
```

Bootstrapping scripts for a package are optional. If no bootstrapping
script is provided for a package, no bootstrapping stage will be performed
for the package.

See [script helpers](/guides/script-helpers) for helper functions and
variables available for use. Developers may also be interested in using a
[post-processing script](post-processing).
