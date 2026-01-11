# Environment variables

Variables outlined below are available in both the environment and in
applicable script contexts (unless noted otherwise). For example, the
[`RELENG_VERSION`](env-releng-version) variable can be accessed by invoked
programs such as a Makefile definition:

```make
all:
	@echo Using version ${RELENG_VERSION}
```

Or an invoked shell script:

```sh
echo "Using version $RELENG_VERSION"
```

For package definitions and releng-tool scripts, these variables can be
directly used:

```python
print(f'Using version {RELENG_VERSION}')
```

:::{tip}
Avoid using external environment variables for a project to configure
package options such as compiler flags or interpreters. Managing these
options inside a releng-tool project configuration or package
definitions can improve configuration management.
:::

## Common

When configuration, package definitions or various scripts are invoked by
releng-tool, the following environment variables are available:

(env-build-dir)=
### `BUILD_DIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The build directory for a project. By default, this will be a folder `build`
found inside the configured output directory. For example:

```none
<root-dir>/output/build
```

For package-specific build directories, see
[`PKG_BUILD_DIR`](env-pkg-build-dir).

(env-cache-dir)=
### `CACHE_DIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The cache directory which holds distributed version control cache data (e.g.
Git data). By default, this will be a folder `cache` found inside the
configured root directory. For example:

```none
<root-dir>/cache
```

See also [`RELENG_CACHE_DIR`](env-releng-cache-dir) and the
[`--cache-dir` argument](arg-cache-dir).

(env-dl-dir)=
### `DL_DIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The download directory which holds a local copy of package artifacts. By
default, this will be a folder `dl` found inside the configured root
directory. For example:

```none
<root-dir>/dl
```

See also [`RELENG_DL_DIR`](env-releng-dl-dir) and the
[`--dl-dir` argument](arg-dl-dir).

(env-host-bin-dir)=
### `HOST_BIN_DIR`

:::{versionadded} 0.14
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The host directory's prefixed bin directory. For example:

```none
<root-dir>/output/host/usr/bin
```

(env-host-dir)=
### `HOST_DIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The host directory. By default, this will be a folder `host` found inside
the configured output directory. For example:

```none
<root-dir>/output/host
```

(env-host-include-dir)=
### `HOST_INCLUDE_DIR`

:::{versionadded} 0.12
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The host directory's prefixed include directory. An example include
directory may be as follows:

```none
<root-dir>/output/host/usr/include
```

(env-host-lib-dir)=
### `HOST_LIB_DIR`

:::{versionadded} 0.12
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The host directory's prefixed library directory. An example library
directory may be as follows:

```none
<root-dir>/output/host/usr/lib
```

(env-host-share-dir)=
### `HOST_SHARE_DIR`

:::{versionadded} 2.1
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The host directory's prefixed share directory. An example share
directory may be as follows:

```none
<root-dir>/output/host/usr/share
```

(env-images-dir)=
### `IMAGES_DIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The images directory which holds final images/packages from a run. By default,
this will be a folder `images` found inside the configured output directory.
For example:

```none
<root-dir>/output/images
```

See also [`RELENG_IMAGES_DIR`](env-releng-images-dir) and the
[`--images-dir` argument](arg-images-dir).

(env-license-dir)=
### `LICENSE_DIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The licenses directory which holds tracked license information from a run.
By default, this will be a folder `licenses` found inside the configured output
directory. For example:

```none
<root-dir>/output/licenses
```

See also [licenses](licenses).

(env-njobs)=
### `NJOBS`

Number of calculated jobs to allow at a given time. Unless explicitly set
by a system builder on the command line, the calculated number of jobs
should be equal to the number of physical cores on the host. When building
a specific package and the package overrides the number of jobs to use,
the [package-defined count](pkg-opt-fixed-jobs) will be used instead. This
configuration will always be a value of at least one (`1`).

(env-njobsconf)=
### `NJOBSCONF`

Number of jobs to allow at a given time. Unlike [`NJOBS`](env-njobs),
`NJOBSCONF` provides the requested configured number of jobs to use. The
value may be set to zero (`0`) to indicate an automatic detection of jobs
to use. This can be useful for tools which have their own automatic job
count implementation and do not want to rely on the value defined by
[`NJOBS`](env-njobs). When building a specific package and the package
overrides the number of jobs to use, the
[package-defined count](pkg-opt-fixed-jobs) will be used instead.

(env-output-dir)=
### `OUTPUT_DIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The output directory. By default, this will be a folder `output` found inside
the configured root directory. For example:

```none
<root-dir>/output
```

The output directory can be configured using either:

- The [`--out-dir` argument](arg-out-dir).
- The [`RELENG_OUTPUT_DIR`](env-releng-out-dir) environment variable.
- The
  [`RELENG_GLOBAL_OUTPUT_CONTAINER_DIR`](env-releng-global-out-container-dir)
  environment variable.

(env-pkg-build-base-dir)=
### `PKG_BUILD_BASE_DIR`

:::{versionadded} 0.12
:::

The directory for a specific package's base directory for buildable content.
In most cases, this value will be the same as
[`PKG_BUILD_DIR`](env-pkg-build-dir). However, if
[`LIBFOO_BUILD_SUBDIR`](pkg-opt-build-subdir) is configured,
[`PKG_BUILD_DIR`](env-pkg-build-dir) will also include the configured
sub-directory. The value of [`LIBFOO_BUILD_SUBDIR`](pkg-opt-build-subdir)
does not adjust the value of `PKG_BUILD_BASE_DIR`.

For example, for a package `test`, the package build base directory may be:

```none
<root>/build/test-1.0
```

See also [`PKG_BUILD_DIR`](env-pkg-build-dir).

(env-pkg-build-dir)=
### `PKG_BUILD_DIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The directory for a specific package's buildable content.

For example, for a package `test`, the package build directory may be:

```none
<root>/build/test-1.0
```

If [`LIBFOO_BUILD_SUBDIR`](pkg-opt-build-subdir) is configured, the
sub-directory path will be appended.

See also [`PKG_BUILD_BASE_DIR`](env-pkg-build-base-dir) and
[`PKG_BUILD_OUTPUT_DIR`](env-pkg-build-output-dir).

(env-pkg-build-output-dir)=
### `PKG_BUILD_OUTPUT_DIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The directory for where a package's build output will be stored.

For example, for a package `test`, the package build output directory may be:

```none
<root>/build/test-1.0/releng-output
```

See also [`PKG_BUILD_DIR`](env-pkg-build-dir).

(env-pkg-cache-dir)=
### `PKG_CACHE_DIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The location of the cache directory for a package. If a package defines
a fetch from a repository which can be locally cached, this cache
directory represents the location where the local cache of content will
be held. For example, if a provide defines a Git-based site, a local
cache of the Git repository will be stored in this location. Typically,
packages should not need to operate on the cache directory except for
advanced cases.

For example, for a package `test`, the package cache directory would be:

```none
<root>/cache/test
```

(env-pkg-cache-file)=
### `PKG_CACHE_FILE`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The location of the cache file for a package. If a package defines a fetch
of an archive from a remote source, after the fetch stage is completed, the
archive can be found in this location.

For example, if a package defines a site `https://www.example.com/test.tgz`,
the resulting cache file may be:

```none
<root>/output/dl/test-1.0.tgz
```

(env-pkg-defdir)=
### `PKG_DEFDIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The package's definition directory.

For example, for a package `test`, the definition directory would be:

```none
<root>/package/test
```

(env-pkg-devmode)=
### `PKG_DEVMODE`

:::{versionadded} 0.13
:::

Whether the package is configured for development mode. While runtime may be
configured in a development mode, not all packages may be designed for
development (e.g. [external packages](intern-extern-pkgs)). If both a package
is aimed for internal development and the runtime is configured in a
development mode, the environment variable will be set to a value of one
(i.e. `PKG_DEVMODE=1`).

See also [`RELENG_DEVMODE`](env-releng-devmode) and
[development mode](development-mode).

(env-pkg-internal)=
### `PKG_INTERNAL`

Whether or not the package is considered "internal". If internal, the
environment variable will be set to a value of one (i.e. `PKG_INTERNAL=1`).

See also [internal and external packages](intern-extern-pkgs).

(env-pkg-localsrcs)=
### `PKG_LOCALSRCS`

:::{versionadded} 0.13
:::

Whether the package is configured for local-sources mode. If a package is
configured for local-sources, the environment variable will be set to a
value of one (i.e. `PKG_LOCALSRCS=1`).

See also [local-sources mode](local-sources-mode).

(env-pkg-name)=
### `PKG_NAME`

The name of the package.

(env-pkg-revision)=
### `PKG_REVISION`

The site revision of the package.

See also [`LIBFOO_REVISION`](pkg-opt-revision).

(env-pkg-site)=
### `PKG_SITE`

The site of the package.

See also [`LIBFOO_SITE`](pkg-opt-site).

(env-pkg-version)=
### `PKG_VERSION`

The version of the package.

See also [`LIBFOO_VERSION`](pkg-opt-version).

(env-prefix)=
### `PREFIX`

The sysroot prefix for the package. By default, this value is configured
to `/usr`; with the exception of Windows builds where this value is empty
by default.

See also [`LIBFOO_PREFIX`](pkg-opt-prefix) and
[`sysroot_prefix`](conf-sysroot-prefix).

(env-prefixed-host-dir)=
### `PREFIXED_HOST_DIR`

:::{versionadded} 0.12
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The host directory with the prefix applied. An example prefixed
directory may be as follows:

```none
<root-dir>/output/host/usr
```

(env-prefixed-staging-dir)=
### `PREFIXED_STAGING_DIR`

:::{versionadded} 0.12
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The staging area directory with the prefix applied. An example prefixed
directory may be as follows:

```none
<root-dir>/output/staging/usr
```

(env-prefixed-target-dir)=
### `PREFIXED_TARGET_DIR`

:::{versionadded} 0.12
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The target area directory with the prefix applied. An example prefixed
directory may be as follows:

```none
<root-dir>/output/target/usr
```

(env-releng-clean)=
### `RELENG_CLEAN`

:::{versionadded} 0.7
:::

Flag set if performing a clean request.

This includes when a user invokes either a [`clean`](action-clean),
[`distclean`](action-distclean) or [`mrproper`](action-mrproper) action request.

(env-releng-debug)=
### `RELENG_DEBUG`

:::{versionadded} 0.7
:::

Flag set if debug-related information should be shown.

This flag is enabled when the [`--debug` argument](arg-debug) is configured.

(env-releng-devmode)=
### `RELENG_DEVMODE`

:::{versionadded} 0.2
:::

The development mode or flag set if in [development mode](development-mode).

See also [`PKG_DEVMODE`](env-pkg-devmode) and
[`--development`](arg-development).

(env-releng-distclean)=
### `RELENG_DISTCLEAN`

:::{versionadded} 0.7
:::

Flag set if performing an extreme pristine clean request.

This includes when a user invokes either the [`distclean`](action-distclean)
action request.

(env-releng-exec)=
### `RELENG_EXEC`

:::{versionadded} 1.4
:::

Flag set if performing a [`<pkg>-exec`](action-pkg-exec) request.

(env-releng-force)=
### `RELENG_FORCE`

:::{versionadded} 0.11
:::

Flag set if performing a forced request from the command line.

See also [`--force`](arg-force).

(env-releng-localsrcs)=
### `RELENG_LOCALSRCS`

:::{versionadded} 0.2
:::

Flag set if in [local-sources mode](local-sources-mode).

See also [`--local-sources`](arg-local-sources).

(env-releng-mrproper)=
### `RELENG_MRPROPER`

Flag set if performing a pristine clean request.

This includes when a user invokes either a [`distclean`](action-distclean) or
[`mrproper`](action-mrproper) action request.

(env-releng-profiles)=
### `RELENG_PROFILES`

:::{versionadded} 2.5
:::

Defines one or more semicolon-separated profile values actively configured
for a run.

See also [`--profile`](arg-profile) and [using profiles](profiles).

(env-releng-rebuild)=
### `RELENG_REBUILD`

Flag set if performing a re-build request.

See also [`<pkg>-rebuild`](action-pkg-rebuild) and
[`<pkg>-rebuild-only`](action-pkg-rebuild-only).

(env-releng-reconfigure)=
### `RELENG_RECONFIGURE`

Flag set if performing a re-configuration request.

See also [`<pkg>-reconfigure`](action-pkg-reconfigure) and
[`<pkg>-reconfigure-only`](action-pkg-reconfigure-only).

(env-releng-reinstall)=
### `RELENG_REINSTALL`

Flag set if performing a re-install request.

See also [`<pkg>-reinstall`](action-pkg-reinstall).

(env-releng-script)=
### `RELENG_SCRIPT`

:::{versionadded} 1.0
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The path of the script currently being executed.

See also [`RELENG_SCRIPT_DIR`](env-releng-script-dir).

(env-releng-script-dir)=
### `RELENG_SCRIPT_DIR`

:::{versionadded} 1.0
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The path of the directory holding the script currently being executed.

See also [`RELENG_SCRIPT`](env-releng-script).

(env-releng-target-dir)=
### `RELENG_TARGET_PKG`

:::{versionadded} 0.13
:::

The name of the target package (if any) provided by the command line.

For example, if running `libfoo-rebuild`, the target package would be:

```none
libfoo
```

See also [package actions](package-actions).

(env-releng-verbose)=
### `RELENG_VERBOSE`

:::{versionadded} 0.7
:::

Flag set if verbose-related information should be shown.

This flag is enabled when the [`--verbose` argument](arg-verbose) is configured.

(env-releng-version)=
### `RELENG_VERSION`

:::{versionadded} 0.7
:::

The version of releng-tool.

(env-root-dir)=
### `ROOT_DIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

Directory to process a releng-tool project.

The root directory can be configured using the
[`--root-dir` argument](arg-root-dir).

(env-staging-bin-dir)=
### `STAGING_BIN_DIR`

:::{versionadded} 0.14
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The staging area directory's prefixed bin directory. An example binary
directory may be as follows:

```none
<root-dir>/output/staging/usr/bin
```

(env-staging-dir)=
### `STAGING_DIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The staging area directory. By default, this will be a folder `staging` found
inside the configured output directory. For example:

```none
<root-dir>/output/staging
```

(env-staging-include-dir)=
### `STAGING_INCLUDE_DIR`

:::{versionadded} 0.12
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The staging area directory's prefixed include directory. An example include
directory may be as follows:

```none
<root-dir>/output/staging/usr/include
```

(env-staging-lib-dir)=
### `STAGING_LIB_DIR`

:::{versionadded} 0.12
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The staging area directory's prefixed library directory. An example library
directory may be as follows:

```none
<root-dir>/output/staging/usr/lib
```

(env-staging-share-dir)=
### `STAGING_SHARE_DIR`

:::{versionadded} 2.1
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The staging area directory's prefixed share directory. An example share
directory may be as follows:

```none
<root-dir>/output/staging/usr/share
```

(env-symbols-dir)=
### `SYMBOLS_DIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The symbols area directory. By default, this will be a folder `symbols` found
inside the configured output directory. For example:

```none
<root-dir>/output/symbols
```

(env-target-bin-dir)=
### `TARGET_BIN_DIR`

:::{versionadded} 0.14
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The target area directory's prefixed bin directory. An example binary
directory may be as follows:

```none
<root-dir>/output/target/usr/bin
```

(env-target-dir)=
### `TARGET_DIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The target area directory. By default, this will be a folder `target` found
inside the configured output directory. For example:

```none
<root-dir>/output/target
```

(env-target-include-dir)=
### `TARGET_INCLUDE_DIR`

:::{versionadded} 0.12
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The target area directory's prefixed include directory. An example include
directory may be as follows:

```none
<root-dir>/output/target/usr/include
```

(env-target-lib-dir)=
### `TARGET_LIB_DIR`

:::{versionadded} 0.12
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The target area directory's prefixed library directory. An example library
directory may be as follows:

```none
<root-dir>/output/target/usr/lib
```

(env-target-share-dir)=
### `TARGET_SHARE_DIR`

:::{versionadded} 2.1
:::
:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The target area directory's prefixed share directory. An example share
directory may be as follows:

```none
<root-dir>/output/target/usr/share
```

## Package-specific variables

Package-specific environment variables are also available if another package or
script needs to rely on the (generated) configuration of another package. For
example, if a package `LIBFOO` existed with a package definition:

```python
LIBFOO_VERSION = '1.0.0'
```

The environment variable `LIBFOO_VERSION` with a value of `1.0.0` can be used
in other configurations and script files. The following package-specific
environment variables are available for use, where `<PKG>` translates to a
releng-tool's determined package key:

(env-pkg-var-build-dir)=
### `<PKG>_BUILD_DIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The directory for a defined package's buildable content.

For most packages, this path will match the value specified in
`<PKG>_BUILD_OUTPUT_DIR`. For package types that do not support in-tree
building (e.g. CMake), this path may be the parent of the value specified
in `<PKG>_BUILD_OUTPUT_DIR`:

```none
└── my-releng-tool-project/
    ├── output/
    │   └── build/
    │       └── libfoo-1.0.0          <---- LIBFOO_BUILD_DIR
    │           └── releng-output     <---- LIBFOO_BUILD_OUTPUT_DIR
    │               └── ...
    ├── package/
    │   └── libfoo/
    │       └── libfoo.rt
    ├── releng-tool.rt
    ...
```

For cases where a package uses local sources, this path may change to
point to the specified local source path. For example, when configured for
[local-sources mode](local-sources-mode), the build directory may exist
out of the root directory:

```none
├── libfoo/                           <---- LIBFOO_BUILD_DIR
│   └── ...
└── my-releng-tool-project/
    ├── output/
    │   └── build/
    │       └── libfoo-1.0.0          <---- LIBFOO_BUILD_OUTPUT_DIR
    │           └── ...
    ├── package/
    │   └── libfoo/
    │       └── libfoo.rt
    ├── releng-tool.rt
    ...
```

Or, when using a `local` VCS type, the path may be set for a folder inside
the package's definition directory:

```none
└── my-releng-tool-project/
    ├── output/
    │   └── build/
    │       └── libfoo-1.0.0          <---- LIBFOO_BUILD_OUTPUT_DIR
    │           └── ...
    ├── package/
    │   └── libfoo/
    │       ├── local/                <---- LIBFOO_BUILD_DIR
    │       │   └── ...
    │       └── libfoo.rt
    ├── releng-tool.rt
    ...
```

(env-pkg-var-output-dir)=
### `<PKG>_BUILD_OUTPUT_DIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The directory for where a defined package's build output will be stored.

This location is a path is a folder inside the project's `output/build`
directory. The name is typically a combination of the package's name and
version (e.g. `libfoo-1.0.0`):

```none
└── my-releng-tool-project/
    ├── output/
    │   └── build/
    │       └── libfoo-1.0.0          <---- LIBFOO_BUILD_OUTPUT_DIR
    │           └── ...
    ├── package/
    │   └── libfoo/
    │       └── libfoo.rt
    ├── releng-tool.rt
    ...
```

However, if no version is specified for a package, the folder name may
just be `libfoo`:

```none
└── my-releng-tool-project/
    ├── output/
    │   └── build/
    │       └── libfoo                <---- LIBFOO_BUILD_OUTPUT_DIR
    │           └── ...
    ├── package/
    │   └── libfoo/
    │       └── libfoo.rt
    ├── releng-tool.rt
    ...
```

Note for some package types, the build output directory may be changed to
have an additional path (e.g. `output/build/libfoo-1.0.0/releng-output`)
for package types like CMake. For example:

```none
└── my-releng-tool-project/
    ├── output/
    │   └── build/
    │       └── libfoo-1.0.0
    │           └── releng-output     <---- LIBFOO_BUILD_OUTPUT_DIR
    │               └── ...
    ├── package/
    │   └── libfoo/
    │       └── libfoo.rt
    ├── releng-tool.rt
    ...
```

(env-pkg-var-defdir)=
### `<PKG>_DEFDIR`

:::{versionchanged} 2.2 Variable is path-like in a script environment.
:::

The directory where a defined package's definition is stored.

For example, if a package `libfoo` exists, the `LIBFOO_DEFDIR` environment
variable will contain a directory path matching the path seen below:

```none
└── my-releng-tool-project/
    ├── package/
    │   └── libfoo/                   <---- LIBFOO_DEFDIR
    │       └── libfoo.rt
    ├── releng-tool.rt
    ...
```

(env-pkg-var-name)=
### `<PKG>_NAME`

The name of the package.

For example, if a package `libfoo` exists, the `LIBFOO_NAME` environment
variable will have a value of `libfoo`.

(env-pkg-var-revision)=
### `<PKG>_REVISION`

The revision of a defined package. If a package does not define a revision,
the value used will match the version value (if set). If no version value
exists, this variable may be empty.

(env-pkg-var-version)=
### `<PKG>_VERSION`

The version of a defined package. If a package does not define a version,
the value used will match the revision value (if set). If no revision value
exists, this variable may be empty.

## Script-only variables

A series a script-only variables are also available at certain stages of
releng-tool.

(env-releng-generated-licenses)=
### `RELENG_GENERATED_LICENSES`

:::{versionadded} 1.3
:::

Defines a list of generated license files at the end of package processing
that is available for post-processing actions to use.

(env-releng-generated-sboms)=
### `RELENG_GENERATED_SBOMS`

:::{versionadded} 1.3
:::

Defines a list of generated software build of materials (SBOM) files at the
end of package processing that is available for post-processing actions
to use.

## Other variables

releng-tool also accepts environment variables for configuring specific
features of the releng-tool process. The following environment variables are
accepted:

(env-releng-assets-dir)=
### `RELENG_ASSETS_DIR=<dir>`

:::{versionadded} 0.10
:::

Configures the asset directory to use. The asset directory is the container
directory to use for both cache and download content. By default, no asset
directory is configured. If a user does not override an asset directory using
the [`--assets-dir` argument](arg-assets-dir), the `RELENG_ASSETS_DIR` can be
used as the container directory override for both cache and download
content.

(env-releng-cache-dir)=
### `RELENG_CACHE_DIR=<dir>`

:::{versionadded} 0.10
:::

Configures the cache directory to use. By default, the cache directory used is
configured to `<root>/cache`. If a user does not override a cache directory
using the [`--cache-dir` argument](arg-cache-dir), the `RELENG_CACHE_DIR`
option can be used to override this location.

See also [`CACHE_DIR`](env-cache-dir).

(env-releng-dl-dir)=
### `RELENG_DL_DIR=<dir>`

:::{versionadded} 0.10
:::

Configures the download directory to use. By default, the download directory
used is configured to `<root>/dl`. If a user does not override a download
directory using the [`--dl-dir` argument](arg-dl-dir), the `RELENG_DL_DIR`
option can be used to override this location.

See also [`DL_DIR`](env-dl-dir).

(env-releng-global-out-container-dir)=
### `RELENG_GLOBAL_OUTPUT_CONTAINER_DIR=<dir>`

```{note}
This environment variable is always ignored when either the
[`--out-dir` argument](arg-out-dir) or
[`RELENG_OUTPUT_DIR`](env-releng-out-dir) environment variable is used.
```

:::{versionadded} 1.1
:::

Configures a "global" container directory used to hold the output contents
of releng-tool projects. Projects will typically generate output contents
inside a project's `<root-dir>/output` directory. This can be overridden
using the [`--out-dir` argument](arg-out-dir) or
[`RELENG_OUTPUT_DIR`](env-releng-out-dir) environment variable, if a user
wishes to generate a build on a different path/partition. While these
overrides can help, users managing multiple releng-tool projects will need
to tailor a specific output directory value for each project they wish to
build. This may be less than ideal if projects typically build in an
output folder in a common directory. To help avoid this, this environment
variable can be used.

When configuring this option, the default output folder for projects will be
set to the provided container directory along with a project's root directory
name:

```none
$RELENG_GLOBAL_OUTPUT_CONTAINER_DIR/<root-directory-name>
```

This allows a user to build multiple releng-tool projects with output data
placed inside a common directory path without needing to explicitly configure
a specific output directory each project's build.

For example, if a user stores multiple projects inside a `~/projects/` path
and configures this option to the path `/mnt/extern-disk`:

```
export RELENG_GLOBAL_OUTPUT_CONTAINER_DIR=/mnt/extern-disk
```

The following folder structure should be expected:

```none
├── usr/
│   └── home/
│       └── myuser/
│           └── projects/
│               ├── my-project-a/
│               │   ├── ...
│               │   └── releng-tool.rt
│               └── my-project-b/
│                   ├── ...
│                   └── releng-tool.rt
└── mnt/
    └── extern-disk/
        ├── my-project-a/
        │   └── ...
        └── my-project-b/
            └── ...
```

(env-releng-ignore-running-as-root)=
### `RELENG_IGNORE_RUNNING_AS_ROOT=1`

:::{versionadded} 0.10
:::

Suppress the [warning](tips/privileged-builds) generated when running
releng-tool with an elevated user.

(env-releng-ignore-unknown-args)=
### `RELENG_IGNORE_UNKNOWN_ARGS=1`

:::{versionadded} 1.3
:::

Suppress the warning/error generated when running releng-tool with unknown
arguments.

See also the [`--relaxed-args` argument](arg-relaxed-args).

(env-releng-images-dir)=
### `RELENG_IMAGES_DIR=<dir>`

:::{versionadded} 0.13
:::

Configures the images directory to use. By default, the images directory used is
configured to `<root>/output/images`. If a user does not override a images
directory using the [`--images-dir` argument](arg-images-dir), the
`RELENG_IMAGES_DIR` option can be used to override this location.

See also [`IMAGES_DIR`](env-images-dir).

(env-releng-out-dir)=
### `RELENG_OUTPUT_DIR=<dir>`

:::{versionadded} 1.1
:::

Configures the output directory to use. By default, the output directory used is
configured to `<root>/output`. If a user does not override an output
directory using the [`--out-dir` argument](arg-out-dir), the
`RELENG_OUTPUT_DIR` option can be used to override this location.

See also
[`RELENG_GLOBAL_OUTPUT_CONTAINER_DIR`](env-releng-global-out-container-dir).

(env-releng-parallel-level)=
### `RELENG_PARALLEL_LEVEL=<level>`

:::{versionadded} 2.3
:::

Configures the number of jobs to use (defaults to `0`; automatic).

See also the [`--jobs` argument](arg-jobs), [`NJOBS`](env-njobs) and
[`NJOBSCONF`](env-njobsconf).

(env-tool-overrides)=
### Tool overrides

Environment variables can be used to help override external tool invoked by the
releng-tool process. For example, when invoking CMake-based projects, the tool
`cmake` will be invoked. However, if a builder is running on CentOS and CMake
v3.x is desired, the tool `cmake3` needs to be invoked instead. To configure
this, an environment variable can be set to switch which tool to invoke.
Consider the following example:

```shell-session
$ export RELENG_CMAKE=cmake3
$ releng-tool
[cmake3 will be used for cmake projects]
```
