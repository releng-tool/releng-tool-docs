# Cargo package

:::{versionadded} 1.3
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


[cargo]: https://doc.rust-lang.org/cargo/
