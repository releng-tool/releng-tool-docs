# Packages

Packages for a project are defined inside the `package/` directory.
Packages can consist of libraries, programs or even basic assets.

```
└── sample-releng-tool-project/
    ├── package/
    │   └── box-firmware/
    │   │   └── box-firmware
    │   │   └── box-firmware.hash
    │   └── libfw-uploader/
    │   │   └── libfw-uploader
    │   └── libsupport/
    │   │   └── libsupport
    │   └── rack-engine/
    │       └── rack-engine
    └── releng
```

## Overview

There is no explicit limit on the total number of packages a project can have.
Package names are recommended to be lower-case with dash-separated (`-`)
separators (if needed). For example, `package-a` is recommended over `PackageA`
or `package_a`; however, the choice is up to the developer making the
releng-tool project.

When making a package, a container folder for the package as well as a package
definition file needs to be made. For example, for a package `package-a`,
the file `package/package-a/package-a` should exist.

```
└── my-releng-tool-project/
    ├── package/
    │   └── package-a/                <---- Container
    │       └── package-a             <---- Definition
    ...
```

Package definition files are Python-based. Inside the definition file, a
series of configuration options can be set to tell releng-tool how to work
with the defined package. Each option is prefixed with a variable-safe
variant of the package name. The prefix value will be an uppercase string
based on the package name with special characters converted to underscores.
For example:

- `package-a` will have a prefix `PACKAGE_A_`
- `libfoo` will have a prefix `LIBFOO_`
- `MyAwesomeModule` will have a prefix `MYAWESOMEMODULE_`

For a package to take advantage of a configuration option, the package
definition will add a variable entry with the package's prefix followed by
the supported option name. Considering the same package with the name
`package-a` which has a prefix `PACKAGE_A_`; to use the
[`LIBFOO_VERSION`](pkg-opt-version) configuration option, the option
`PACKAGE_A_VERSION` should be defined:

```python
PACKAGE_A_VERSION = '1.0.0'
```

## Topics

:::{toctree}
:maxdepth: 1

Common options <common-pkg-options>
Advanced options <advanced-pkg-options>
Bootstrapping <bootstrapping>
Post-processing <post-processing>
site-definitions
hash-file
ascii-armor
pkg-type-script
pkg-type-autotools
pkg-type-cargo
pkg-type-cmake
pkg-type-make
pkg-type-meson
pkg-type-python
pkg-type-scons
Deprecated options <deprecated-pkg-options>
:::
