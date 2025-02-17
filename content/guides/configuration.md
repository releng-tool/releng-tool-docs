# Configuration

A releng-tool project defines its configuration options inside the a
`releng-tool.rt` file at the root of a project (or other defaults; see
[alternative extensions](tips/alternative-extensions)). The primary
configuration option for a developer to define is `packages`, which is used
to hold a list of packages to be processed. For example, a project structure
such as follows:

```
└── my-project/
    ├── package/
    │   ├── package-a/
    │   │   └── ...
    │   ├── package-b/
    │   │   └── ...
    │   └── package-c/
    │       └── ...
    └── releng-tool.rt                <----
```

Can have a configuration (`releng`) such as:

```python
packages = [
    'package-a',
    'package-b',
    'package-c',
]
```

Packages can be loaded implicitly. If other packages depend on each other,
a project may only list a subset of packages in a `packages` configuration.
For example, if the above had `package-b` dependent on both `package-a` and
`package-c`, then only `package-b` would need to be defined in the main
configuration file:

```python
packages = [
    'package-b',
]
```

## Common options

A series of additional configuration options are available to be defined inside
the project's configuration. A list of common configuration options are as
follows:

(conf-default-internal)=
### `default_internal`

A flag to indicate that projects are implicitly loaded as internal projects.
By default, packages not explicitly configured as internal or external are
assumed to be external packages.

```python
default_internal = True
```

See also [internal and external packages](intern-extern-pkgs).

(conf-environment)=
### `environment`

:::{versionadded} 1.3
:::

A dictionary to define environment variables to apply to all stages of
releng-tool.

```python
environment = {
    'MY_ENV_1': 'First example',
    'MY_ENV_2': 'Another example',
}
```

(conf-extensions)=
### `extensions`

A list of extensions to load before processing a releng-tool project. If an
extension cannot be loaded, releng-tool will stop with information on why
an extension could not be loaded.

```python
extensions = [
    'ext-a',
    'ext-b',
]
```

See also [extensions](extensions/extensions).

(conf-external-packages)=
### `external_packages`

A list of external package locations. By default, packages for a project
will be searched for in root directory's package folder (`<root>/package`).
In some build environments, some packages may be required or may be preferred
to be located in another location/repository. To allow packages to be
loaded from another package container directory, one or more package
locations can be provided. For example:

```python
external_packages = [
    releng_env('MY_EXTERNAL_PKG_DIR'),
]
```

(conf-license-header)=
### `license_header`

As the releng-tool build process is finalized, a license document can be
generated containing each package's license information. If a developer
wishes to add a custom header to the generated document, a header can be
defined by project's configuration. For example:

```python
license_header = 'my leading content'
```

See also [licenses](licenses).

(conf-packages)=
### `packages`

A list of packages to process. Packages listed will be processed by
releng-tool till their completion. Package dependencies not explicitly
listed will be automatically loaded and processed as well.

```python
packages = [
    'package-a',
    'package-b',
    'package-c',
]
```

(conf-prerequisites)=
### `prerequisites`

:::{versionadded} 0.6
:::

A list of host tools to check for before running a releng-tool project.
Allows a developer to identify tools to check and fail-fast if missing,
instead of waiting for a stage which requires a specific tool and failing
later during a building, packaging, etc. phase.

```python
prerequisites = [
    'tool-a',
    'tool-b',
    'tool-c',
]
```

(conf-sbom-format)=
### `sbom_format`

:::{versionadded} 0.15
:::
:::{versionchanged} 0.16 Support added for `json-spdx` and `rdp-spdx`.
:::

Configures the default format to use when generating a software build of
materials (SBOM). By default, `text` format SBOMs are generated for a
project.

```python
sbom_format = 'xml'
```

The following lists the available formats supported:

| Type | Value |
| -: | :- |
| CSV | `csv` |
| HTML | `html` |
| JSON | `json` |
| JSON (SPDX) | `json-spdx` |
| RDP (SPDX) | `rdp-spdx` |
| Text | `text` (default) |
| XML | `xml` |

Multiple formats can be provided. For example:

```python
sbom_format = [
    'html',
    'json',
]
```

(conf-sysroot-prefix)=
### `sysroot_prefix`

Define a custom sysroot prefix to provide to packages during their
configuration, build and installation stages. By default, the sysroot
prefix is typically set to `/usr`; for Windows, the value is empty.

```python
sysroot_prefix = '/usr'
```

See also [`LIBFOO_PREFIX`](pkg-opt-prefix) and [`PREFIX`](env-prefix).

(conf-url-mirror)=
### `url_mirror`

Specifies a mirror base site to be used for URL fetch requests. If this
option is set, any URL fetch requests will first be tried on the configured
mirror before attempting to acquired from the defined site in a package
definition.

```python
url_mirror = 'ftp://mirror.example.org/data/'
```

The `url_mirror` configuration also accepts the following format options:

- `name`: the name of a package
- `version`: the version of a package

For example:

```python
url_mirror = 'ftp://mirror.example.org/cache/{name}/'
```

Where `{name}` will be replaced by the package name being fetched.

## Advanced options

A list of more advanced configuration options are as follows:

(conf-cache-ext)=
### `cache_ext`

A transform for cache extension interpreting. This is an advanced
configuration and is not recommended for use except for special use cases
outlined below.

When releng-tool fetches assets from remote sites, the site value can used
to determine the resulting filename of a cached asset. For example,
downloading an asset from `https://example.org/my-file.tgz`, the locally
downloaded file will result in a `.tgz` extension. However, not all defined
sites will result in an easily interpreted cache extension. While
releng-tool will attempt its best to determine an appropriate extension
value to use, some use cases may not be able to be handled. To deal with
these cases, a developer can define a transform method to help translate
a site value into a known cache extension value.

Consider the following example: a host is used to acquire assets from a
content server. The URI to download an asset uses a unique request format
`https://static.example.org/fetch/25134`. releng-tool may not be able to
find the extension for the fetched asset, but if a developer knows the
expected archive types for these calls, a custom transform can be defined.
For example:

```python
def my_translator(site):
    if 'static.example.org' in site:
        return 'tgz'
    return None

cache_ext = my_translator
```

The above transform indicates that all packages using the
`static.example.org` site will be `tgz` archives.

(conf-default-devmode-ignore-cache)=
### `default_devmode_ignore_cache`

:::{versionadded} 2.1
:::

When operating in [development mode](/guides/development-mode), packages may
configure [`LIBFOO_DEVMODE_IGNORE_CACHE`](pkg-opt-devmode-ignore-cache) to
indicate that a package should ignore any generated cache when operating
from a clean state. If a developer is managing a package set in a project
where most (if not all) packages would want to use this feature, a global
override can be configured.

```python
default_devmode_ignore_cache = True
```

Setting this value to `True` will default all packages to operate with a
manner as if `LIBFOO_DEVMODE_IGNORE_CACHE = True`. Individual packages may
opt-out in this scenario by configuring `LIBFOO_DEVMODE_IGNORE_CACHE = False`.

See also [`LIBFOO_DEVMODE_IGNORE_CACHE`](pkg-opt-devmode-ignore-cache).

(conf-extra-license-exceptions)=
### `extra_license_exceptions`

:::{versionadded} 0.14
:::

A dictionary to define extra license exceptions that are permitted in
package definitions. Packages which define license exceptions in a
[`LIBFOO_LICENSE`](pkg-opt-license) option are expected to use
[SPDX License Exceptions][spdx-exceptions]. If not, a warning is generated
by default. A project can define their own custom exceptions by adding them
into a project's `extra_license_exceptions` option to avoid this warning:

```python
extra_license_exceptions = {
    'My-Exception-ID': 'Exception Name',
}
```

See also [licenses](licenses).

(conf-extra-licenses)=
### `extra_licenses`

:::{versionadded} 0.14
:::

A dictionary to define extra licenses that are permitted in package
definitions. Packages which define licenses in a
[`LIBFOO_LICENSE`](pkg-opt-license) option are expected to use a licensed
defined in the [SPDX License List][spdx-licenses]. If not, a warning is
generated by default. A project can define their own custom license by
adding them into a project's `extra_licenses` option to avoid this warning:

```python
extra_licenses = {
    'My-License-ID': 'License Name',
}
```

See also [licenses](licenses).

(conf-override-extract-tools)=
### `override_extract_tools`

A dictionary to be provided to map an extension type to an external tool
to indicate which tool should be used for extraction. For example, when a
`.zip` archive is being processed for extraction, releng-tool will
internally extract the archive. However, a user may wish to override this
tool with their own extraction utility. Consider the following example:

```python
override_extract_tools = {
    'zip': '/opt/my-custom-unzip {file} {dir}',
}
```

The `{file}` key will be replaced with the file to be extracted, and the
`{dir}` key will be replaced where the contents should extract to.

(conf-quirks)=
### `quirks`

A list of configuration quirks to apply to deal with corner cases which
can prevent releng-tool operating on a host system.

```python
quirks = [
    'releng.<special-quirk-id>',
]
```

For a list of available quirks, see [quirks](quirks/quirks).

(conf-urlopen-context)=
### `urlopen_context`

:::{versionadded} 0.10
:::

Allows a project to specify a custom SSL context [^urlopen] to apply for
URL fetch requests. This can be useful for environments which may
experience `CERTIFICATE_VERIFY_FAILED` errors when attempting to fetch
files. A custom SSL context can be created and tailored for a build
environment. For example:

```python
import ssl
...

urlopen_context = ssl.create_default_context()
```

[^urlopen]: <https://docs.python.org/library/urllib.request.html#urllib.request.urlopen>

(conf-vsdevcmd)=
### `vsdevcmd`

:::{note}
The option is ignored in non-Windows environments.
:::

:::{versionadded} 1.4
:::

Allows a project to automatically load Visual Studio Developer Command
Prompt (`VsDevCmd.bat`) variables into the releng-tool process. This will
allow packages and post-build scripts to invoke commands as if releng-tool
was started from within a Visual Studio Developer Command Prompt.

```python
vsdevcmd = True
```

Projects looking to use an explicit version of Visual Studio can specify a
version string that is compatible with [Visual Studio Locator's][vswhere]
(vswhere) `-version` argument.

```python
vsdevcmd = '[17.0,18.0)'
```

See also [`LIBFOO_VSDEVCMD`](pkg-opt-vsdevcmd).

## Deprecated options

The following outlines deprecated configuration options. It is not
recommended to use these options.

(conf-override-revisions)=
### `override_revisions`

:::{deprecated} 2.0
The use of revision overrides is deprecated.
Users wanting to override revisions without source modification are
recommended to use [variable injection](arg-variable-injection).
:::

:::{warning}
The use of an override option should only be used in special cases (see
also [configuration overrides](configuration-overrides)).
:::

Allows a dictionary to be provided to map a package name to a new revision
value. Consider the following example: a project defines `module-a` and
`module-b` packages with package `module-b` depending on package
`module-a`. A developer may be attempting to tweak package `module-b` on
the fly to test a new capabilities against the current stable version of
`module-a`. However, the developer does not want to explicitly change the
revision inside package `module-b`'s definition. To avoid this, an override
can be used instead:

```python
override_revisions = {
    'module-b': '<test-branch>',
}
```

The above example shows that package `module-b` will fetch using a test
branch instead of what is defined in the actual package definition.

(conf-override-sites)=
### `override_sites`

:::{deprecated} 2.0
The use of site overrides is deprecated.
Users wanting to override sites without source modification are
recommended to use [variable injection](arg-variable-injection).
:::

:::{warning}
The use of an override option should only be used in special cases (see
also [configuration overrides](configuration-overrides)).
:::

A dictionary to be provided to map a package name to a new site value. There
may be times where a host may not have access to a specific package site. To
have a host to use a mirror location without having to adjust the package
definition, the site override option can be used. For example, consider a
package pulls from site `git@example.com:myproject.git`. However, the host
`example.com` cannot be access from the host machine. If a mirror location
has been setup at `git@example.org:myproject.git`, the following override
can be used:

```python
override_sites = {
    '<pkg>': 'git@example.org:mywork.git',
}
```


[spdx-exceptions]: https://spdx.org/licenses/exceptions-index.html
[spdx-licenses]: https://spdx.org/licenses/
[vswhere]: https://github.com/microsoft/vswhere
