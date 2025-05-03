# Python package

A Python package provides support for processing a [Python][python]
supported module.

```python
LIBFOO_TYPE = 'python'
```

Only the build and installation phases are used when processing the sources
for a Python package (i.e. no configuration stage is invoked). The
[`LIBFOO_PYTHON_SETUP_TYPE`](pkg-opt-python-setup-type) configuration dictates
which build approach is performed for a package. The installation stage
for all Python packages uses the [`installer`][installer] module. When a Python
package is processed, it will use the same Python interpreter used by
releng-tool.

````{note}
For environments where releng-tool has been installed using `pipx`, a user
will need to install any required build backend desired using the
[`pipx inject`][pipx-inject] command. For example, packages requiring
[Flit][flit] can install the build backend for their isolated environment
using:

```
pipx inject releng-tool flit-core
```
````

A developer can override what Python interpreter to use by
configuring the [`LIBFOO_PYTHON_INTERPRETER`](pkg-opt-python-interpreter)
option in a package:

```python
LIBFOO_PYTHON_INTERPRETER = '/opt/my-custom-python-build/python'
```

The following sections outline configuration options are available for a
Python package.

(pkg-opt-python-build-defs)=
:::{include} _pkg-build-defs.md
:::
:::{include} _pkg-build-defs-example-default.md
:::

(pkg-opt-python-build-env)=
:::{include} _pkg-build-env.md
:::

(pkg-opt-python-build-opts)=
:::{include} _pkg-build-opts.md
:::

(pkg-opt-python-env)=
:::{include} _pkg-env.md
:::

## `LIBFOO_INSTALL_DEFS`

:::{versionremoved} 2.0
No longer applicable as all Python packages are  installed using the
[`installer`][installer] module.
:::

## `LIBFOO_INSTALL_ENV`

:::{versionremoved} 2.0
No longer applicable as all Python packages are installed using the
[`installer`][installer] module.
:::

## `LIBFOO_INSTALL_OPTS`

:::{versionremoved} 2.0
No longer applicable as all Python packages are installed using the
[`installer`][installer] module.
:::

(pkg-opt-python-dist-path)=
## `LIBFOO_PYTHON_DIST_PATH`

:::{versionadded} 2.0
:::
:::{versionchanged} 2.2 Support added for path-like values.
:::

When a Python package is built, it will scan the `dist/` directory in
package's output directory for a wheel package. It is possible for some
Python packages to configure their projects to output built wheels into an
alternative path. If an alternative path is configured, releng-tool will
fail to find and install the package.

This option informs releng-tool what container folder hosts the provided
wheel package. For example, if the Python package configures itself to
output into `build/dist`, the following configuration can be used:

```
LIBFOO_PYTHON_DIST_PATH = 'build/dist'
```

(pkg-opt-python-installer-interpreter)=
## `LIBFOO_PYTHON_INSTALLER_INTERPRETER`

:::{versionadded} 2.3
:::

Configures the interpreter path to use when generating launcher scripts
when installing a Python package. This is passed into [`installer`][installer]
which handles the creations of launchers for an application (if a given
Python package defines project scripts).

The default interpreter used for project scripts is as follows:

| Type | Value |
| -: | :- |
| Non-Windows | `/usr/bin/python` |
| Windows | `python.exe` |

An example using a custom interpreter `/opt/custom/python` for project
scripts can be done using:

```
LIBFOO_PYTHON_INSTALLER_INTERPRETER = '/opt/custom/python'
```

Which should generate project scripts with a shebang:

```
#!/opt/custom/python
...
```

Before the introduction of this variable, the interpreter used would
be configured to the same interpreter used by releng-tool.

(pkg-opt-python-installer-launcher-kind)=
## `LIBFOO_PYTHON_INSTALLER_LAUNCHER_KIND`

:::{versionadded} 2.0
:::

Defines the launcher-kind to build when generating any executable scripts
defined in the Python package's project configuration (`pyproject.toml`).
By default, the launcher-kind is chosen based on the host platform building
the package. Supported options are dictated by [`installer`][installer].
Options may include:

- `posix`
- `win-amd64`
- `win-arm64`
- `win-arm`
- `win-ia32`

For example, to explicitly build POSIX executable scripts, the following
configuration can be defined:

```
LIBFOO_PYTHON_INSTALLER_SCHEME = 'posix'
```

(pkg-opt-python-installer-scheme)=
## `LIBFOO_PYTHON_INSTALLER_SCHEME`

:::{versionadded} 2.0
:::

Defines the installation scheme used for Python packages. By default,
releng-tool uses the following scheme entries:

| Path        | Installation directory |
| ----------: | :- |
| data        | `prefix`
| include     | `prefix/include/python`
| platinclude | `prefix/include/python`
| platlib     | `prefix/lib/python`
| platstdlib  | `prefix/lib/python`
| purelib     | `prefix/lib/python`
| scripts     | `prefix/bin`
| stdlib      | `prefix/lib/python`

A package can be configured with a scheme `native` to use the default
install target based on the native system:

```
LIBFOO_PYTHON_INSTALLER_SCHEME = 'native'
```

Packages can also use schemes supported by Python's [`sysconfig`][sysconfig]
module. For example:

```
LIBFOO_PYTHON_INSTALLER_SCHEME = 'posix_prefix'
```

A package may also define a custom scheme:

```
LIBFOO_PYTHON_INSTALLER_SCHEME = {
    'data':        '',
    'include':     'include/python',
    'platinclude': 'include/python',
    'platlib':     'lib/python',
    'platstdlib':  'lib/python',
    'purelib':     'lib/python',
    'scripts':     'bin',
    'stdlib':      'lib/python',
}
```

(pkg-opt-python-interpreter)=
## `LIBFOO_PYTHON_INTERPRETER`

:::{versionchanged} 2.2 Support added for path-like values.
:::

Defines a specific Python interpreter when processing the build and
installation stages for a package. If not specified, the system's Python
interpreter will be used. This field is optional.

```python
LIBFOO_PYTHON_INTERPRETER = '<path>'
```

(pkg-opt-python-setup-type)=
## `LIBFOO_PYTHON_SETUP_TYPE`

:::{versionadded} 0.13
:::
:::{versionchanged} 0.14 Support added for `poetry`.
:::
:::{versionchanged} 2.0
Use of [`installer`][installer] is required for all package types.
:::
:::{deprecated} 2.0
Support for `distutils` packages is deprecated.
:::

The setup type will configure how a Python package is built and installed.
The default setup type used for a Python package is a distutils package. It
is recommended to always configure a setup type for a Python package.
The following outlines available setup types in releng-tool:

| Type                        | Value |
| --------------------------: | :- |
| [Flit][flit]                | `flit`
| [Hatch][hatch]              | `hatch`
| [PDM][pdm]                  | `pdm`
| [PEP 517 build][pypa-build] | `pep517`
| [Poetry][poetry]            | `poetry`
| [Setuptools][setuptools]    | `setuptools`
| [distutils][distutils]      | `distutils` (default)

For example:

```python
LIBFOO_PYTHON_SETUP_TYPE = 'setuptools'
```

Host environments are required to pre-install needed packages in their
running Python environment to support setup types not available in a
standard Python distribution. For example, if a PDM setup type is set,
the host system will need to have `pdm` Python module installed on
the system.

The [`installer`][installer] module will be used to install packages to
their destination folders. For  Setuptools/distutils packages, ensure
[`wheel`][wheel] is available to help build as packages will be built
with `bdist_wheel`.


[distutils]: https://docs.python.org/3.11/library/distutils.html
[flit]: https://flit.pypa.io
[hatch]: https://hatch.pypa.io
[installer]: https://installer.pypa.io/
[pdm]: https://pdm-project.org/
[pipx-inject]: https://pipx.pypa.io/#inject-a-package
[poetry]: https://python-poetry.org/
[pypa-build]: https://build.pypa.io/
[python]: https://www.python.org/
[setuptools]: https://setuptools.pypa.io
[sysconfig]: https://docs.python.org/3/library/sysconfig.html
[wheel]: https://wheel.readthedocs.io/
