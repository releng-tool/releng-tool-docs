# Cargo package

:::{versionadded} 1.3
:::
:::{versionchanged} 1.4 Added support for dependency patching.
:::

A Cargo package provides support for processing a [Cargo][cargo] supported
module.

```python
LIBFOO_TYPE = 'cargo'
```

During the configuration stage of a Cargo package, `cargo` will be invoked to
generate build files for the module. After fetching and extracting a package,
`cargo vendor` will be invoked to download any defined dependencies defined
in `Cargo.toml`. After all dependencies are acquired, a build stage will
be triggered using `cargo build`, followed by an installation stage using
`cargo install`. Each stage can be configured to manipulate environment
variables and options used by the Cargo executable.

Cargo packages are handled a bit differently compared to other package
types. In order to support having Cargo application packages work with
library dependencies managed in a releng-tool project, all Cargo packages
in play will need to be extracted ahead of time before any individual
Cargo package can be built.

For any Cargo package that defines a dependency to another Cargo package
that is defined inside a releng-tool project, dependencies will be
automatically [patched][cargo-patch] to use the local package definition.

The following sections outline configuration options are available for a
Cargo package.

(pkg-opt-cargo-build-defs)=
:::{include} _pkg-build-defs.md
:::
:::{include} _pkg-build-defs-example-dentry.md
:::

(pkg-opt-cargo-build-env)=
:::{include} _pkg-build-env.md
:::

(pkg-opt-cargo-build-opts)=
:::{include} _pkg-build-opts.md
:::

(pkg-opt-cargo-name)=
## `LIBFOO_CARGO_NAME`

:::{versionadded} 1.4
:::

Provides an explicit name to use for a Cargo package. By default, the used
Cargo name is assumed to be the same as the package name used in releng-tool.
If the names do not match, it is recommended to explicitly set the package
name as it will be used to patch package dependencies together.

```python
LIBFOO_CARGO_NAME = 'example-name'
```

(pkg-opt-cargo-noinstall)=
## `LIBFOO_CARGO_NOINSTALL`

:::{versionadded} 1.4
:::

Specifies whether the Cargo package should skip an attempt to invoke the
install command. This option can be helpful when defining a Cargo package
that is used as a library (instead of a full application).
By default, the installation stage is invoked with a value of `False`.

```python
LIBFOO_CARGO_NOINSTALL = True
```

(pkg-opt-cargo-env)=
:::{include} _pkg-env.md
:::

(pkg-opt-cargo-install-defs)=
:::{include} _pkg-install-defs.md
:::
:::{include} _pkg-install-defs-example-default.md
:::

(pkg-opt-cargo-install-env)=
:::{include} _pkg-install-env.md
:::

(pkg-opt-cargo-install-opts)=
:::{include} _pkg-install-opts.md
:::


[cargo-patch]: https://doc.rust-lang.org/cargo/reference/config.html#patch
[cargo]: https://doc.rust-lang.org/cargo/
