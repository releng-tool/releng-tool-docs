# Environment variables

:::{tip}
Avoid using external environment variables for a project to configure
package options such as compiler flags or interpreters. Managing these
options inside a releng-tool project configuration or package
definitions can improve configuration management.
:::

## Common

When configuration, package definitions or various scripts are invoked by
releng-tool, the following environment variables are available:

### `BUILD_DIR`

The build directory. By default, this will be a folder `build` found inside
the configured output directory. For example:

```none
<root-dir>/output/build
```

### `CACHE_DIR`

The cache directory. By default, this will be a folder `cache` found inside
the configured root directory. For example:

```none
<root-dir>/cache
```

### `DL_DIR`

The download directory. By default, this will be a folder `dl` found inside
the configured root directory. For example:

```none
<root-dir>/dl
```

### `HOST_BIN_DIR`

The host directory's prefixed bin directory. For example:

```none
<root-dir>/output/build
```

### `HOST_DIR`

The host directory. By default, this will be a folder `host` found inside
the configured output directory. For example:

```none
<root-dir>/output/host
```

### `HOST_INCLUDE_DIR`

The host directory's prefixed include directory.

### `HOST_LIB_DIR`

The host directory's prefixed library directory.

### `IMAGES_DIR`

The images directory. By default, this will be a folder `images` found inside
the configured output directory. For example:

```none
<root-dir>/output/images
```

### `LICENSE_DIR`

The licenses directory. By default, this will be a folder `licenses` found
inside the configured output directory. For example:

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

### `OUTPUT_DIR`

The output directory.  By default, this will be a folder `output` found inside
the configured root directory. For example:

```none
<root-dir>/output
```

(env-pkg-build-base-dir)=
### `PKG_BUILD_BASE_DIR`

The directory for a specific package's base directory for buildable content.
In most cases, this value will be the same as
[`PKG_BUILD_DIR`](env-pkg-build-dir). However, if [](pkg-opt-build-subdir)
is configured, [`PKG_BUILD_DIR`](env-pkg-build-dir) will also include the
configured sub-directory. The value of [](pkg-opt-build-subdir) does not
adjust the value of `PKG_BUILD_BASE_DIR`.

See also [`PKG_BUILD_DIR`](env-pkg-build-dir).

(env-pkg-build-dir)=
### `PKG_BUILD_DIR`

The directory for a specific package's buildable content.

See also [`PKG_BUILD_BASE_DIR`](env-pkg-build-base-dir) and
[`PKG_BUILD_OUTPUT_DIR`](env-pkg-build-output-dir).

(env-pkg-build-output-dir)=
### `PKG_BUILD_OUTPUT_DIR`

The directory for where a package's build output will be stored.

See also [`PKG_BUILD_DIR`](env-pkg-build-dir).

### `PKG_CACHE_DIR`

The location of the cache directory for a package. If a package defines
a fetch from a repository which can be locally cached, this cache
directory represents the location where the local cache of content will
be held. For example, if a provide defines a Git-based site, a local
cache of the Git repository will be stored in this location. Typically,
packages should not need to operate on the cache directory except for
advanced cases.

### `PKG_CACHE_FILE`

The location of the cache file for a package. If a package defines a fetch
of an archive from a remote source, after the fetch stage is completed, the
archive can be found in this location.

For example, if a package defines a site `https://www.example.com/test.tgz`,
the resulting cache file may be `<root>/output/dl/test-1.0.tgz`.

### `PKG_DEFDIR`

The package's definition directory.

For example, for a package `test`, the definition directory would be
`<root>/package/test`.

### `PKG_DEVMODE`

Whether the package is configured for development mode. If a package is
configured for development mode, the environment variable will be set to a
value of one (i.e. `PKG_DEVMODE=1`).

See also [development mode](development-mode).

### `PKG_INTERNAL`

Whether or not the package is considered "internal". If internal, the
environment variable will be set to a value of one (i.e. `PKG_INTERNAL=1`).

See also [internal and external packages](intern-extern-pkgs).

### `PKG_LOCALSRCS`

Whether the package is configured for local-sources mode. If a package is
configured for local-sources, the environment variable will be set to a
value of one (i.e. `PKG_LOCALSRCS=1`).

See also [local-sources mode](local-sources-mode).

### `PKG_NAME`

The name of the package.

### `PKG_REVISION`

The site revision of the package.

See also [](pkg-opt-revision).

### `PKG_SITE`

The site of the package.

See also [](pkg-opt-site).

### `PKG_VERSION`

The version of the package.

See also [](pkg-opt-version).

### `PREFIX`

The sysroot prefix for the package. By default, this value is configured
to `/usr`; with the exception of Windows builds where this value is empty
by default.

### `PREFIXED_HOST_DIR`

The host directory with the prefix applied. An example prefixed
directory may be as follows:

```none
<root-dir>/output/host/usr
```

### `PREFIXED_STAGING_DIR`

The staging area directory with the prefix applied. An example prefixed
directory may be as follows:

```none
<root-dir>/output/staging/usr
```

### `PREFIXED_TARGET_DIR`

The target area directory with the prefix applied. An example prefixed
directory may be as follows:

```none
<root-dir>/output/target/usr
```

### `RELENG_CLEAN`

Flag set if performing a clean request.

### `RELENG_DEBUG`

Flag set if debug-related information should be shown.

### `RELENG_DEVMODE`

The development mode or flag set if in [development mode](development-mode).

### `RELENG_DISTCLEAN`

Flag set if performing an extreme pristine clean request.

### `RELENG_FORCE`

Flag set if performing a forced request from the command line.

### `RELENG_LOCALSRCS`

Flag set if in [local-sources mode](local-sources-mode).

### `RELENG_MRPROPER`

Flag set if performing a pristine clean request.

### `RELENG_REBUILD`

Flag set if performing a re-build request.

### `RELENG_RECONFIGURE`

Flag set if performing a re-configuration request.

### `RELENG_REINSTALL`

Flag set if performing a re-install request.

### `RELENG_SCRIPT`

The path of the script currently being executed.

### `RELENG_SCRIPT_DIR`

The path of the directory holding the script currently being executed.

### `RELENG_TARGET_PKG`

The name of the target package (if any) provided by the command line.

### `RELENG_VERBOSE`

Flag set if verbose-related information should be shown.

### `RELENG_VERSION`

The version of releng-tool.

### `ROOT_DIR`

The root directory.

### `STAGING_BIN_DIR`

The staging area directory's prefixed bin directory. An example binary
directory may be as follows:

```none
<root-dir>/output/staging/usr/bin
```

### `STAGING_DIR`

The staging area directory. By default, this will be a folder `staging` found
inside the configured output directory. For example:

```none
<root-dir>/output/staging
```

### `STAGING_INCLUDE_DIR`

The staging area directory's prefixed include directory. An example include
directory may be as follows:

```none
<root-dir>/output/staging/usr/include
```

### `STAGING_LIB_DIR`

The staging area directory's prefixed library directory. An example library
directory may be as follows:

```none
<root-dir>/output/staging/usr/lib
```

### `SYMBOLS_DIR`

The symbols area directory. By default, this will be a folder `symbols` found
inside the configured output directory. For example:

```none
<root-dir>/output/symbols
```

### `TARGET_BIN_DIR`

The target area directory's prefixed bin directory. An example binary
directory may be as follows:

```none
<root-dir>/output/target/usr/bin
```

### `TARGET_DIR`

The target area directory. By default, this will be a folder `target` found
inside the configured output directory. For example:

```none
<root-dir>/output/target
```

### `TARGET_INCLUDE_DIR`

The target area directory's prefixed include directory. An example include
directory may be as follows:

```none
<root-dir>/output/target/usr/include
```

### `TARGET_LIB_DIR`

The target area directory's prefixed library directory. An example library
directory may be as follows:

```none
<root-dir>/output/target/usr/lib
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

### `<PKG>_BUILD_DIR`

The directory for a defined package's buildable content.

For most packages, this path will match the value specified in
`<PKG>_BUILD_OUTPUT_DIR`. For package types that do not support in-tree
building (e.g. CMake), this path may be the parent of the value specified
in `<PKG>_BUILD_OUTPUT_DIR`:

```
└── my-releng-tool-project/
    ├── output/
    │   └── build/
    │       └── libfoo-1.0.0          <---- LIBFOO_BUILD_DIR
    │           └── releng-output     <---- LIBFOO_BUILD_OUTPUT_DIR
    │               └── ...
    ├── package/
    │   └── libfoo/
    │       └── libfoo.py
    ├── releng
    ...
```

For cases where a package uses local sources, this path may change to
point to the specified local source path. For example, when configured for
[local-sources mode](local-sources-mode), the build directory may exist
out of the root directory:

```
└── libfoo/                           <---- LIBFOO_BUILD_DIR
│   └── ...
└── my-releng-tool-project/
    ├── output/
    │   └── build/
    │       └── libfoo-1.0.0          <---- LIBFOO_BUILD_OUTPUT_DIR
    │           └── ...
    ├── package/
    │   └── libfoo/
    │       └── libfoo.py
    ├── releng
    ...
```

Or, when using a `local` VCS type, the path may be set for a folder inside
the package's definition directory:

```
└── my-releng-tool-project/
    ├── output/
    │   └── build/
    │       └── libfoo-1.0.0          <---- LIBFOO_BUILD_OUTPUT_DIR
    │           └── ...
    ├── package/
    │   └── libfoo/
    │       └── local/                <---- LIBFOO_BUILD_DIR
    │           └── ...
    │       └── libfoo.py
    ├── releng
    ...
```

### `<PKG>_BUILD_OUTPUT_DIR`

The directory for where a defined package's build output will be stored.

This location is a path is a folder inside the project's `output/build`
directory. The name is typically a combination of the package's name and
version (e.g. `libfoo-1.0.0`):

```
└── my-releng-tool-project/
    ├── output/
    │   └── build/
    │       └── libfoo-1.0.0          <---- LIBFOO_BUILD_OUTPUT_DIR
    │           └── ...
    ├── package/
    │   └── libfoo/
    │       └── libfoo.py
    ├── releng
    ...
```

However, if no version is specified for a package, the folder name may
just be `libfoo`:

```
└── my-releng-tool-project/
    ├── output/
    │   └── build/
    │       └── libfoo                <---- LIBFOO_BUILD_OUTPUT_DIR
    │           └── ...
    ├── package/
    │   └── libfoo/
    │       └── libfoo.py
    ├── releng
    ...
```

Note for some package types, the build output directory may be changed to
have an additional path (e.g. `output/build/libfoo-1.0.0/releng-output`)
for package types like CMake. For example:

```
└── my-releng-tool-project/
    ├── output/
    │   └── build/
    │       └── libfoo-1.0.0
    │           └── releng-output     <---- LIBFOO_BUILD_OUTPUT_DIR
    │               └── ...
    ├── package/
    │   └── libfoo/
    │       └── libfoo.py
    ├── releng
    ...
```

### `<PKG>_DEFDIR`

The directory where a defined package's definition is stored.

For example, if a package `libfoo` exists, the `LIBFOO_DEFDIR` environment
variable will contain a directory path matching the path seen below:

```
└── my-releng-tool-project/
    ├── package/
    │   └── libfoo/                   <---- LIBFOO_DEFDIR
    │       └── libfoo.py
    ├── releng
    ...
```

### `<PKG>_NAME`

The name of the package.

For example, if a package `libfoo` exists, the `LIBFOO_NAME` environment
variable will have a value of `libfoo`.

### `<PKG>_REVISION`

The revision of a defined package. If a package does not define a revision,
the value used will match the version value (if set). If no version value
exists, this variable may be empty.

### `<PKG>_VERSION`

The version of a defined package. If a package does not define a version,
the value used will match the revision value (if set). If no revision value
exists, this variable may be empty.

## Other variables

releng-tool also accepts environment variables for configuring specific
features of the releng-tool process. The following environment variables are
accepted:

(env-releng-assets-dir)=
### `RELENG_ASSETS_DIR=<dir>`

The asset directory to use. The asset directory is the container directory
to use for both cache and download content. By default, no asset directory
is configured. If a user does not override an asset directory using the
[`--assets-dir` argument](arg-assets-dir), the `RELENG_ASSETS_DIR` can be
used as the container directory override for both cache and download
content.

(env-releng-cache-dir)=
### `RELENG_CACHE_DIR=<dir>`

The cache directory to use. By default, the cache directory used is configured
to `<root>/cache`. If a user does not override a cache directory using the
[`--cache-dir` argument](arg-cache-dir), the `RELENG_CACHE_DIR` option can
be used to override this location.

(env-releng-dl-dir)=
### `RELENG_DL_DIR=<dir>`

The download directory to use. By default, the download directory used is
configured to `<root>/dl`. If a user does not override a download directory
using the [`--dl-dir` argument](arg-dl-dir), the `RELENG_DL_DIR` option
can be used to override this location.

(env-releng-ignore-running-as-root)=
### `RELENG_IGNORE_RUNNING_AS_ROOT=1`

Suppress the [warning](tips/privileged-builds) generated when running
releng-tool with an elevated user.
