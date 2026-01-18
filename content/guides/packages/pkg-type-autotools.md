# Autotools package

An Autotools package provides support for processing a
[GNU Build System][gnu-build-sys] supported module.

```python
LIBFOO_TYPE = 'autotools'
```

The following shows the default arguments used in stages and outlines
configuration options that are available for an Autotools package to set.
See also the [Autotools package examples](/examples/examples-autotools).
All stages are invoked with a [`PKG_BUILD_DIR`](env-pkg-build-dir)
working directory.

````{tab} Configuration
```{eval-rst}
.. only:: latex

    Configuration stage
    -------------------
```

The configuration stage will invoke `./configure` with the arguments:

```none
./configure --exec-prefix <PREFIX> --prefix <PREFIX>
```

The prefix arguments are configured to [`LIBFOO_PREFIX`](pkg-opt-prefix).

If [`LIBFOO_AUTOTOOLS_AUTORECONF`](pkg-opt-autotools-autoreconf) is configured,
`autoreconf` will be invoked before `./configure` is started:

```none
autoreconf
```
````

````{tab} Build
```{eval-rst}
.. only:: latex

    Build stage
    -----------
```

The build stage invokes `make` with the arguments:

```none
make --jobs <NJOBS>
```

The number of jobs is populated by either the [`--jobs` argument](arg-jobs) or
[`LIBFOO_FIXED_JOBS`](pkg-opt-fixed-jobs). Although, if the configuration
results in a single job, the argument will not be used.
````

````{tab} Install
```{eval-rst}
.. only:: latex

    Install stage
    -------------
```

The install stage invokes `make` with an `install` target:

```none
make install
```

With the following environment variables set:

```none
DESTDIR=<TARGET_DIR>
```

The `DESTDIR` path will be set to the target sysroot the package should
install into (see also [`LIBFOO_INSTALL_TYPE`](pkg-opt-install-type)).
`make install` may be invoked multiple times for each target it needs to
install into.

If a package defines install options, the `install` target is not provided
by default.
````

(pkg-opt-autotools-autoreconf)=
## `LIBFOO_AUTOTOOLS_AUTORECONF`

Specifies whether the package needs to perform an Autotools
re-configuration. This is to assist in the rebuilding of GNU Build System
files which may be broken or a patch has introduced new build script
changes that need to be applied. This field is optional. By default,
`autoreconf` is not invoked.

```python
LIBFOO_AUTOTOOLS_AUTORECONF = True
```

(pkg-opt-autotools-build-defs)=
:::{include} _pkg-build-defs.md
:::
:::{include} _pkg-build-defs-example-default.md
:::

(pkg-opt-autotools-build-env)=
:::{include} _pkg-build-env.md
:::

(pkg-opt-autotools-build-opts)=
:::{include} _pkg-build-opts.md
:::

(pkg-opt-autotools-conf-defs)=
:::{include} _pkg-conf-defs.md
:::
:::{include} _pkg-conf-defs-example-default.md
:::

(pkg-opt-autotools-conf-env)=
:::{include} _pkg-conf-env.md
:::

(pkg-opt-autotools-conf-opts)=
:::{include} _pkg-conf-opts.md
:::

(pkg-opt-autotools-env)=
:::{include} _pkg-env.md
:::

(pkg-opt-autotools-install-defs)=
:::{include} _pkg-install-defs.md
:::
:::{include} _pkg-install-defs-example-default.md
:::

(pkg-opt-autotools-install-env)=
:::{include} _pkg-install-env.md
:::

(pkg-opt-autotools-install-opts)=
:::{include} _pkg-install-opts.md
:::

Defining custom install options will prevent the default `install` target from
being added. Users looking to utilize the `install` target for the install
stage with custom arguments should explicitly include the `install` in their
options.


[gnu-build-sys]: https://www.gnu.org/software/automake/manual/html_node/index.html
