# Development mode

Development mode provides a way for a user to request to process packages
against development versions of sources rather than using fixed versions.
A package will typically target a stable release, either pointing to a
specific archive to download or a specific tag to clone from. However, for
some builds, a user may wish to build a specific package against their main
development branch (e.g. the `main` branch of a Git repository) or a
long-term stable release branch. Packages can be defined to target these
specific revisions if running in development mode.

To enable development mode, invoking `releng-tool` with the `--development`
(or `-D`) argument will enable the mode. Future calls to releng-tool for the
project will use a development revision for packages where appropriate.
For example:

```shell-session
$ releng-tool --development [<mode>]
(success) configured root for development mode
$ releng-tool
~building against development sources~
...
```

Development mode is persisted through the use of a file flag in the root
directory.

Consider the following example: a package defines multiple revisions to
fetch sources from:

```python
LIBFOO_SITE = 'https://example.com/libfoo.git'
LIBFOO_REVISION = {
    DEFAULT_REVISION: '1.2',
    'develop': 'main',
    'lts': '1.1.x',
}
```

A build would normally use the `1.2` tag for this package. However, if
an environment is configured to use the `develop` development mode:

```shell-session
$ releng-tool --development develop
```

This package would use the `main` branch instead.

Projects can also target specific sites based off the development mode. This
can be useful if a package uses a built archive for a stable release, but
having development sources fetched from a repository. For example:

```python
LIBFOO_SITE = {
    DEFAULT_SITE: 'https://pkgs.example.com/releases/libfoo-${LIBFOO_VERSION}.tar.gz',
    'test': 'https://git.example.com/libfoo.git',
}

LIBFOO_REVISION = {
    'test': 'main',
}
```

In a normal execution, a tar.gz archive would be downloaded for the package.
However, if an environment is configured to use the `test` development
mode, sources will be fetched from the Git repository on the `main` branch.

Simple development modes are also supported. Packages can use the
`LIBFOO_DEVMODE_REVISION` option to hint at a development revision to pull.

```python
LIBFOO_DEVMODE_REVISION = 'main'
LIBFOO_REVISION = 'v3.0'
```

A build would normally use the `v3.0` tag for this package. However, if
an environment is configured a non-explicit development mode:

```shell-session
$ releng-tool --development
```

This package would use the `main` branch instead.

A user can either disable development mode by performing a
[`mrproper`](action-mrproper) or can manually remove the file flag
observed at the root of the project.
