# Common package options

The following outlines common configuration options available for packages.

(pkg-opt-install-type)=
## `LIBFOO_INSTALL_TYPE`

Defines the installation type of this package. A package may be designed to be
built and installed for just the target area, the stage area, both or maybe in
the host directory. The following options are available for the installation
type:

| Type                 | Description |
| -------------------: | :- |
| `host`               | The host directory.
| `images`             | The images directory.
| `staging`            | The staging area.
| `staging_and_target` | Both the staging an target area.
| `target`             | The target area.

The default installation type is `target`.

```python
LIBFOO_INSTALL_TYPE = 'target'
```

See also [`LIBFOO_HOST_PROVIDES`](pkg-opt-host-provides).

(pkg-opt-license)=
## `LIBFOO_LICENSE`

A string or list of strings outlining the license information for a package.
Outlining the license of a package is recommended.
It is recommended to use [SPDX registered licenses][spdx-licenses].

```python
LIBFOO_LICENSE = ['GPL-2.0-only', 'MIT']
```

or

```python
LIBFOO_LICENSE = 'GPL-2.0-or-later WITH Bison-exception-2.2'
```

or

```python
LIBFOO_LICENSE = 'LicenseRef-MyCompanyLicense'
```

See also [`LIBFOO_LICENSE_FILES`](pkg-opt-license-files).

(pkg-opt-license-files)=
## `LIBFOO_LICENSE_FILES`

A string or list of strings identifying the license files found inside the
package sources which typically would match up to the defined `LICENSE`
entries (respectively).

```python
LIBFOO_LICENSE_FILES = [
    'LICENSE.GPLv2',
    'LICENSE.MIT',
]
```

or

```python
LIBFOO_LICENSE_FILES = 'LICENSE'
```

See also [`LIBFOO_LICENSE`](pkg-opt-license).

(pkg-opt-needs)=
## `LIBFOO_NEEDS`

:::{note}
The option replaces the legacy
[`LIBFOO_DEPENDENCIES`](pkg-opt-dependencies) option.
:::

:::{versionadded} 1.3
:::

List of package dependencies a given project has. If a project depends on
another package, the package name should be listed in this option. This ensures
releng-tool will process packages in the proper order. The following shows an
example package `libfoo` being dependent on `liba` and `libb` being
processed first:

```python
LIBFOO_NEEDS = [
    'liba',
    'libb',
]
```

(pkg-opt-site)=
## `LIBFOO_SITE`

The site where package sources/assets can be found. The site can be a URL
of an archive, or describe a source control URL such as Git or SVN. The
following outline a series of supported site definitions:

:::{versionchanged} 0.10 Support added for `rsync+`.
:::
:::{versionchanged} 0.17 Support added for `perforce+`.
:::
:::{versionchanged} 1.4 Support added for `brz+`.
:::
:::{versionchanged} 2.0 Support added for `file+`.
:::
:::{deprecated} 2.0 Support for Bazaar sites is deprecated.
:::

| Type                        | Prefix/Postfix |
| --------------------------: | :- |
| [Breezy](site-breezy)       | `brz+`
| [Bazaar](site-bazaar)       | `bzr+` *(deprecated)*
| [CVS](site-cvs)             | `cvs+`
| [File](site-file)           | `file+` or `file://`
| [Git](site-git)             | `git+` or `.git`
| [Mercurial](site-mercurial) | `hg+`
| [Perforce](site-perforce)   | `perforce+`
| [rsync](site-rsync)         | `rsync+`
| [SCP](site-scp)             | `scp+`
| [SVN](site-svn)             | `svn+`
| [URL](site-url)             | `(wildcard)`

Examples include:

```python
LIBFOO_SITE = 'https://example.com/libfoo.git'
LIBFOO_SITE = 'cvs+:pserver:anonymous@cvs.example.com:/var/lib/cvsroot mymodule'
LIBFOO_SITE = 'svn+https://svn.example.com/repos/libfoo/c/branches/libfoo-1.2'
LIBFOO_SITE = 'https://www.example.com/files/libfoo.tar.gz'
LIBFOO_SITE = {
    DEFAULT_SITE: 'https://pkgs.example.com/releases/libfoo-${LIBFOO_VERSION}.tar.gz',
    '<mode>': 'https://git.example.com/libfoo.git',
}
```

A developer can also use [`LIBFOO_VCS_TYPE`](pkg-opt-vcs-type) to
explicitly define the version control system type without the need for a
prefix hint. The use of a dictionary value is only useful when operating in
[development mode](/guides/development-mode).

Using a specific type will create a dependency for a project that the
respective host tool is installed on the host system. For example, if a
Git site is set, the host system will need to have `git` installed on the
system.

If no site is defined for a package, it will be considered a virtual package
(i.e. has no content). If applicable, loaded extensions may provide support
for custom site protocols.

Specifying a [local site](site-local) value with `local` will automatically
configure a VCS-type of `local`.

See also [`LIBFOO_VCS_TYPE`](pkg-opt-vcs-type) and
[site definitions](site-definitions).

(pkg-opt-type)=
## `LIBFOO_TYPE`

:::{versionchanged} 0.13 Support added for `make`.
:::
:::{versionchanged} 0.16 Support added for `meson`.
:::
:::{versionchanged} 1.3 Support added for `cargo`.
:::

The package type. The default package type is a (Python) script-based package.
releng-tool also provides a series of helper package types for common
frameworks. The following outline a series of supported type definitions:

| Type                            | Value |
| ------------------------------: | :- |
| [Autotools](pkg-type-autotools) | `autotools`
| [Cargo](pkg-type-cargo)         | `cargo`
| [CMake](pkg-type-cmake)         | `cmake`
| [Make](pkg-type-make)           | `make`
| [Meson](pkg-type-meson)         | `meson`
| [Python](pkg-type-python)       | `python`
| [SCons](pkg-type-scons)         | `scons`
| [Script](pkg-type-script)       | `script`

For example:

```python
LIBFOO_TYPE = 'script'
```

If no type is defined for a package, it will be considered a script-based
package. If applicable, loaded extensions may provide support for custom
types.

Using a specific type will create a dependency for a project that the
respective host tool is installed on the host system. For example, if a
CMake type is set, the host system will need to have `cmake` installed on
the system.

(pkg-opt-version)=
## `LIBFOO_VERSION`

The version of the package. Typically the version value should be formatted
in a semantic versioning style, but it is up to the developer to decide
the best version value to use for a package. It is important to note that
the version value is used to determine build output folder names, cache
files and more.

```python
LIBFOO_VERSION = '1.0.0'
```

For some VCS types, the version value will be used to acquire a specific
revision of sources. If for some case the desired version value cannot be
gracefully defined (e.g. a version value `libfoo-v1.0` will produce output
directories such as `libfoo-libfoo-v1.0`),
[`LIBFOO_REVISION`](pkg-opt-revision) can be used.

See also [`LIBFOO_DEVMODE_REVISION`](pkg-opt-devmode-revision) and
[`LIBFOO_REVISION`](pkg-opt-revision).


[spdx-licenses]: https://spdx.org/licenses/
