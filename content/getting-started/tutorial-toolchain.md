# Tutorial "A toolchain example"

This tutorial shows an example creating an application using a
pre-built toolchain. In this example, we will use a pre-built toolchain
which (in theory) has been used to prepare a Linux image for an embedded
device. With the same toolchain, we can define a releng-tool project that
prepares an application that can run on this embedded device.

This example will attempt to prepare a static build of [htop][htop] that
can run on an aarch64 system.

## Preparing the host environment

```{note}
A releng-tool project may create a package to download/setup a toolchain
package to use for a build. However, for this example, we will keep the
installation/availability of the toolchain outside of the releng-tool
project (for simplicity of this tutorial).
```

First, we will prepare a toolchain on a host system to be used by our
releng-tool project. For this tutorial, we will use a
[toolchain provided by Bootlin][bootlin-tcs]. Download the following
toolchain package:

- Architecture: aarch64
- libc: glibc
- <https://toolchains.bootlin.com/downloads/releases/toolchains/aarch64/tarballs/aarch64--glibc--stable-2022.08-1.tar.bz2>
- <https://toolchains.bootlin.com/downloads/releases/toolchains/aarch64/tarballs/aarch64--glibc--stable-2022.08-1.sha256>
- (sha256: 844df3c99508030ee9cb1152cb182500bb9816ff01968f2e18591d51d766c9e7)

Extract and place the toolchain into a desired location. In this example,
we will place the toolchain under `/opt`. However, users can install the
toolchain to whatever path they desire:

```shell-session
$ tar -vxf <toolchain-archive>
$ mv aarch64--glibc--stable-2022.08-1 /opt
$ cd /opt/aarch64--glibc--stable-2022.08-1
$ relocate-sdk.sh
```

Verify the ability to invoke GCC from the toolchain installation:

```shell-session
$ /opt/aarch64--glibc--stable-2022.08-1/bin/aarch64-linux-gcc --version
aarch64-linux-gcc.br_real (Buildroot 2021.11-4428-g6b6741b) 11.3.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

## Preparing a new releng-tool project

To build [htop][htop], this requires two dependencies:

- [Ncurses][ncurses]
- [Netlink Protocol Library Suite (libnl)][libnl]

Build a new project with the following structure to support our `htop`
package, dependencies and project configuration:


```
└── my-tc-project/
    ├── package/
    │   ├── htop/
    │   │   ├── htop
    │   │   └── htop.hash
    │   ├── libnl/
    │   │   ├── libnl
    │   │   └── libnl.hash
    │   └── ncurses/
    │       ├── ncurses
    │       └── ncurses.hash
    └── releng
```

## The configuration

The first changes we will make to our releng-tool project is to define the
specifics of the project configuration in `releng`. Apply the following
contents to the configuration:

```python
packages = [
    'htop',
]

# location of the toolchain to use
MY_TOOLCHAIN_ROOT = '/opt/aarch64--glibc--stable-2022.08-1'
MY_TOOLCHAIN_SYSROOT = releng_join(
    MY_TOOLCHAIN_ROOT, 'aarch64-buildroot-linux-gnu/sysroot')

# flag buildroot toolchain to be strict with includes
releng_env('BR_COMPILER_PARANOID_UNSAFE_PATH', '1')

MY_TOOLCHAIN_CONF_ENV = {
    # configure compiler/linker options
    'CC': f'{MY_TOOLCHAIN_ROOT}/bin/aarch64-linux-gcc',
    'CXX': f'{MY_TOOLCHAIN_ROOT}/bin/aarch64-linux-g++',
    'CFLAGS': f'--sysroot={MY_TOOLCHAIN_SYSROOT} -I${{STAGING_INCLUDE_DIR}}',
    'CXXLAGS': f'--sysroot={MY_TOOLCHAIN_SYSROOT} -I${{STAGING_INCLUDE_DIR}}',
    'LDFLAGS': f'--sysroot={MY_TOOLCHAIN_SYSROOT} -L${{STAGING_LIB_DIR}}',
    # configure pkg-config to use staging directory
    'PKG_CONFIG_DIR': '',
    'PKG_CONFIG_LIBDIR': '${STAGING_LIB_DIR}/pkgconfig',
    'PKG_CONFIG_SYSROOT_DIR': '${STAGING_DIR}',
}

MY_TOOLCHAIN_CONF_DEFS = {
    # configure for cross compiling
    '--host': 'aarch64-buildroot-linux',
}
```

- Create a package list which defines `htop` as a required package to build.
  Since we plan to make `libnl` and `ncurses` dependencies to `htop`, they do
  not need to be included.
- This project will rely on the host system having the toolchain installed.
  We create some variables to help point to the toolchain's path and sysroot.
  Developers can make this flexible by allowing these options to be
  configured by environment variables or using command line arguments, but
  this will not be done here to simplify this tutorial.
- We configure `BR_COMPILER_PARANOID_UNSAFE_PATH`, an option supported by
  the generated Bootlin (Buildroot) toolchain to error when using an unsafe
  path when performing a build (i.e. throw an error when using the system's
  `/usr/include` path over a releng-tool sysroot path).
- Prepares two variables `MY_TOOLCHAIN_CONF_ENV` and `MY_TOOLCHAIN_CONF_DEFS`
  which we can later use for the Autotools packages we have. These values
  help configure toolchain and desired releng-tool paths. Variables set
  in the root configuration can later be used inside package scripts and
  post-build scripts. The options specified here are applicable to Autotools
  packages. Options can vary for other types (e.g. CMake projects typically
  are configured with a CMake toolchain file).

The releng-tool project's configuration is ready. Now to define the package
definitions/hashes for each package.

## The libnl package

Update the `libnl` package definition (`my-tc-project/libnl/libnl`) with
the following contents:

```python
LIBNL_INSTALL_TYPE = 'staging'
LIBNL_LICENSE = ['LGPL-2.1-or-later']
LIBNL_LICENSE_FILES = ['COPYING']
LIBNL_SITE = 'https://github.com/thom311/libnl/releases/download/libnl3_7_0/libnl-3.7.0.tar.gz'
LIBNL_TYPE = 'autotools'
LIBNL_VERSION = '3.7.0'

LIBNL_CONF_ENV = MY_TOOLCHAIN_CONF_ENV
LIBNL_CONF_DEFS = MY_TOOLCHAIN_CONF_DEFS

LIBNL_CONF_OPTS = [
    # static lib
    '--enable-static',
    '--disable-shared',
    # disable features that are not required
    '--disable-cli',
    '--disable-debug',
    '--disable-pthreads',
]
```

- The libnl library uses a LGPL-2.1+ license. We configure `LIBNL_LICENSE`
  to the equivalent [SPDX][spdx] license identifier, as well as define
  `LIBNL_LICENSE_FILES` to point to a copy of the license text. Specifying
  license information is not required, but can be helpful when generating
  license data or software bill of materials (SBOM) for a project.
- This example uses libnl v3.7.0, which we set in the `LIBNL_VERSION` option.
  The version value is useful for managing output folders and logging versions
  of packages.
- We specify the location to download sources in `LIBNL_SITE`.
- The libnl library uses Autotools. This means we can use `LIBNL_TYPE` to
  configure the helper type and avoid the need to create custom
  configure/build scripts to run `./configure`, etc. (since releng-tool
  will handle this for us).
- We configure `LIBNL_CONF_ENV` and `LIBNL_CONF_DEFS` to use the configuration
  options we prepared in the root configuration. This allows this Autotools
  package to use the desired toolchain.
- This package is configured to install (`LIBNL_INSTALL_TYPE`) into the
  staging area (instead of, by default, into the target directory). Since
  we are creating a static library for `htop` to link against, there is no
  need to place any generated content from the `libnl` package into the
  target area.
- Finally, we configure `LIBNL_CONF_OPTS` to tweak other options supported
  by this package. We only need a static library, so we explicitly indicate
  to enable static builds and disable shared builds. We also disable a series
  of other features not needed for this example.
  
  Using configuration options can be useful for disabling certain project
  options such as disabling unit tests (which may not be desired for these
  types of builds). It is always good to explicitly define configuration
  entries when possible, just in case default values change for an option.

The above `libnl` package specifies a remote URL to download library
sources. These sources should be validated to ensure data is not corrupted
or manipulated. To do this, create a hash file alongside the package
definition called `libnl.hash` with the contents:

```text
# https://github.com/thom311/libnl/releases/download/libnl3_7_0/libnl-3.7.0.tar.gz.sha256sum
sha256 9fe43ccbeeea72c653bdcf8c93332583135cda46a79507bfd0a483bb57f65939 libnl-3.7.0.tar.gz
# locally computed
sha256 dc626520dcd53a22f727af3ee42c770e56c97a64fe3adb063799d8ab032fe551 COPYING
```

In this hash file, expected hashes for resources can be configured and checked
when releng-tool attempts to fetch resources from remote sources. Ideally,
hashes provided from a third-party package release can be directly added into
these files (`<hash-type> <hash> <file>`). In this example, libnl provides
expected hashes for archives when they make a release. We copy the hash
contents into our local hash file (with a helpful comment to indicate where
it came from).

In addition, we also provide a hash of the license document. While not
required, this can be useful in detecting if the license of a package
changes between versions.

## The ncurses package

Update the `ncurses` package definition (`my-tc-project/ncurses/ncurses`)
with the following contents:

```python
NCURSES_INSTALL_TYPE = 'staging'
NCURSES_LICENSE = ['X11']
NCURSES_LICENSE_FILES = ['COPYING']
NCURSES_SITE = 'https://invisible-mirror.net/archives/ncurses/ncurses-${NCURSES_VERSION}.tar.gz'
NCURSES_TYPE = 'autotools'
NCURSES_VERSION = '6.4'

NCURSES_CONF_ENV = MY_TOOLCHAIN_CONF_ENV
NCURSES_CONF_DEFS = MY_TOOLCHAIN_CONF_DEFS

NCURSES_CONF_OPTS = [
    # static lib
    '--with-normal',
    '--without-shared',
    # disable features that are not required
    '--disable-db-install',
    '--without-ada',
    '--without-curses-h',
    '--without-cxx',
    '--without-cxx-binding',
    '--without-debug',
    '--without-gpm',
    '--without-manpages',
    '--without-progs',
    '--without-sysmouse',
    '--without-tack',
    '--without-tclib',
    '--without-termlib',
    '--without-tests',
]
```

The above almost mimics the previous `libnl` package with the exception of
this package having a different license and different configuration options
available.

Since `ncurses` package specifies a remote URL to download library
sources, we also want to update `ncurses.hash` with the contents:

```text
# locally computed after verification with:
#  https://invisible-island.net/archives/ncurses/ncurses-6.4.tar.gz.asc
#  19882D92DDA4C400C22C0D56CC2AF4472167BE03
sha256 6931283d9ac87c5073f30b6290c4c75f21632bb4fc3603ac8100812bed248159 ncurses-6.4.tar.gz
# locally computed
sha256 63de87399e9fc8860236082b6b0520e068e9eb1fad0ebd30202aa30bb6f690ac COPYING
```

In the previous `libnl` package, maintainers provided an official SHA-256
hash to use for our local hash file. For `ncurses`, maintainers provide a
GPG signature of their archives instead. To handle this, we manually
download the archive and signature file to verify its contents. Once
verified, we generated our own SHA-256 sum and place it into this hash file
(with a helpful comment). And as done in the previous package, we also
provide a hash of the license document.

## The htop package

Update the `htop` package definition (`my-tc-project/htop/htop`) with the
following contents:

```python
HTOP_NEEDS = [
    'libnl',
    'ncurses',
]

HTOP_LICENSE = ['GPL-2.0-or-later']
HTOP_LICENSE_FILES = ['COPYING']
HTOP_SITE = 'https://github.com/htop-dev/htop/releases/download/${HTOP_VERSION}/htop-${HTOP_VERSION}.tar.xz'
HTOP_TYPE = 'autotools'
HTOP_VERSION = '3.2.2'

HTOP_CONF_ENV = MY_TOOLCHAIN_CONF_ENV
HTOP_CONF_DEFS = MY_TOOLCHAIN_CONF_DEFS

HTOP_CONF_OPTS = [
    # disable features that are not required
    '--disable-capabilities',
    '--disable-dependency-tracking',
    '--disable-hwloc',
    '--disable-openvz',
    '--disable-pcp',
    '--disable-sensors',
    '--disable-unicode',
    '--disable-vserver',
]
```

- This package defines a list of package dependencies for `htop`.
  Specifically, we list `libnl` and `ncurses`, which will force releng-tool
  to configure/build these packages before processing the `htop` package.

Since `htop` package specifies a remote URL to download library sources,
we also want to update `htop.hash` with the contents:

```text
# https://github.com/htop-dev/htop/releases/download/3.2.2/htop-3.2.2.tar.xz.sha256
sha256 bac9e9ab7198256b8802d2e3b327a54804dc2a19b77a5f103645b11c12473dc8 htop-3.2.2.tar.xz
# locally computed
sha256 8177f97513213526df2cf6184d8ff986c675afb514d4e68a404010521b880643 COPYING
```

## Performing a build

With a configuration and packages prepared, the project should be ready to
be built. While in the `my-tc-project` folder, invoke `releng-tool`:

```shell-session
$ releng-tool
fetching libnl...
configuring libnl...
building libnl...
...
building htop...
installing htop...
generating sbom information...
generating license information...
(success) completed (0:01:15)
```

Once completed, the target directory will have a compiled `htop` executable
that can be copied over to and run on an aarch64-running target.

This concludes this tutorial.


[bootlin-tcs]: https://toolchains.bootlin.com/
[htop]: https://htop.dev/
[libnl]: https://www.infradead.org/~tgr/libnl/
[ncurses]: https://invisible-island.net/ncurses/
[spdx]: https://spdx.org/licenses/
