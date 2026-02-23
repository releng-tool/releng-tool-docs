# Waf package

:::{versionadded} 2.8
:::

A Waf package provides support to easily invoke [Waf][waf] commands at
various stages of a package.

```python
LIBFOO_TYPE = 'waf'
```

During the configuration stage of a Waf package, `waf configure` will be
invoked to prepare a build. For the build stage, `waf build` will invoke the
build event. For the installation stage (if enabled), `waf install` will be
used. Each stage can be configured to manipulate environment variables and
options used by Waf.

The following shows the default arguments used in stages and outlines
configuration options that are available for a Waf package to set.
See also the [Waf package examples](/examples/examples-waf). All stages
are invoked with a [`PKG_BUILD_DIR`](env-pkg-build-dir) working directory.

````{tab} Configuration
```{eval-rst}
.. only:: latex

    Configuration stage
    -------------------
```

The configuration stage invokes `waf` with the arguments:

```none
waf configure \
    --bindir=bin \
    --libdir=lib \
    --out=<BUILD_OUTPUT_DIR> \
    --prefix=<PREFIX>
```

The prefix arguments are configured to [`LIBFOO_PREFIX`](pkg-opt-prefix).

The build output directory is configured to
[`PKG_BUILD_OUTPUT_DIR`](env-pkg-build-output-dir).
````

````{tab} Build
```{eval-rst}
.. only:: latex

    Build stage
    -----------
```

The build stage invokes `waf` with the arguments:

```none
waf build --jobs <NJOBS>
```

The number of jobs is populated by either the [`--jobs` argument](arg-jobs),
[`LIBFOO_FIXED_JOBS`](pkg-opt-fixed-jobs) or
[`LIBFOO_MAX_JOBS`](pkg-opt-max-jobs). Although, if the configuration results
in a single job, the argument will not be used.
````

````{tab} Install
```{eval-rst}
.. only:: latex

    Install stage
    -------------
```

The install stage invokes `waf` with an `install` target:

```none
waf install --destdir <TARGET_DIR>
```

With the following environment variables set:

```none
DESTDIR=<TARGET_DIR>
```

The `--destdir` argument and `DESTDIR` environment path will be set to the
target sysroot the package should install into (see also
[`LIBFOO_INSTALL_TYPE`](pkg-opt-install-type)). `waf install` may be invoked
multiple times for each target it needs to install into.

The installation stage can be skipped by configuring
[`LIBFOO_WAF_NOINSTALL`](pkg-opt-waf-noinstall).
````

(pkg-opt-waf-build-defs)=
:::{include} _pkg-build-defs.md
:::
:::{include} _pkg-build-defs-example-default.md
:::

(pkg-opt-waf-build-env)=
:::{include} _pkg-build-env.md
:::

(pkg-opt-waf-build-opts)=
:::{include} _pkg-build-opts.md
:::

(pkg-opt-waf-conf-defs)=
:::{include} _pkg-conf-defs.md
:::
:::{include} _pkg-conf-defs-example-default.md
:::

(pkg-opt-waf-conf-env)=
:::{include} _pkg-conf-env.md
:::

(pkg-opt-waf-conf-opts)=
:::{include} _pkg-conf-opts.md
:::

(pkg-opt-waf-env)=
:::{include} _pkg-env.md
:::

(pkg-opt-waf-install-defs)=
:::{include} _pkg-install-defs.md
:::
:::{include} _pkg-install-defs-example-default.md
:::

(pkg-opt-waf-install-env)=
:::{include} _pkg-install-env.md
:::

(pkg-opt-waf-install-opts)=
:::{include} _pkg-install-opts-with-install.md
:::

(pkg-opt-waf-noinstall)=
## `LIBFOO_WAF_NOINSTALL`

Specifies whether the Waf package should skip an attempt to invoke the
install command. Ideally, projects can support an install invoke to help
install files into a target (or staging) environment. Not all Waf projects
may support an install stage, or there can be cases where installation stage
for a package to fail due to issues with some host environments. A developer
can specify this no-install flag to skip a Waf-driven install request and
manage installation actions through other means (such as post-processing).
By default, the installation stage is invoked with a value of `False`.

```python
LIBFOO_WAF_NOINSTALL = True
```


[waf]: https://waf.io/
