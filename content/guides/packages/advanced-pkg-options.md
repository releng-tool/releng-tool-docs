# Advanced package options

The following outlines more advanced configuration options available for
packages.

(pkg-opt-build-subdir)=
## `LIBFOO_BUILD_SUBDIR`

Sub-directory where a package's extracted sources holds its buildable content.
Sources for a package may be nested inside one or more directories. A package
can specify the sub-directory where the configuration, build and installation
processes are invoked from.

```python
LIBFOO_BUILD_SUBDIR = 'subdir'
```

(pkg-opt-devmode-ignore-cache)=
## `LIBFOO_DEVMODE_IGNORE_CACHE`

:::{versionadded} 0.3
:::

Flag value to indicate that a package should ignore any generated cache
file when operating in [development mode](/guides/development-mode).
In most cases, users want to take advantage of cached sources to prevent
having to re-fetch the same content again between builds. However, some
packages may be configured in a way where their request for a package's
contents varies from a fresh stage. For example, when pulling from a
branch, releng-tool will not attempt to re-fetch from a site since a
cached content has already been fetched. If a developer configures a
package to use a revision value with dynamic content, they may wish to use
this option to have a user always force fetching new content from a
clean state.

```python
LIBFOO_DEVMODE_IGNORE_CACHE = True
```

By default, this option is not defined and results can vary based off the site
type being fetched. In most cases, fetch operations will treat the default case
of this option as disabled (`False`). DVCS site types may elect to enable this
option by default (`True`) if the target revision is a branch.

(pkg-opt-devmode-revision)=
## `LIBFOO_DEVMODE_REVISION`

Specifies a development revision for a package. When a project is being
built in [development mode](/guides/development-mode), the development
revision is used over the configured [`LIBFOO_REVISION`](pkg-opt-revision)
value. If a development revision is not defined for a project, a package
will still use the configured [`LIBFOO_REVISION`](pkg-opt-revision) while
in development mode.

```python
LIBFOO_DEVMODE_REVISION = 'feature/alpha'
```

See also [`LIBFOO_REVISION`](pkg-opt-revision) and
[`LIBFOO_VERSION`](pkg-opt-version).

(pkg-opt-extension)=
## `LIBFOO_EXTENSION`

Specifies a filename extension for the package. A package may be cached inside
the download directory to be used when the extraction phase is invoked.
releng-tool attempts to determine the most ideal extension for this cache file;
however some cases the detected extension may be incorrect. To deal with this
situation, a developer can explicitly specify the extension value using this
option.

```python
LIBFOO_EXTENSION = 'tgz'
```

(pkg-opt-external)=
## `LIBFOO_EXTERNAL`

Flag value to indicate that a package is an external package. External
packages will generate warnings if [hashes](hash-file), an
[ASCII-armor](ascii-armor) or [licenses](/guides/licenses) are missing. By
default, packages are considered external unless explicitly configured to
be internal.

```python
LIBFOO_EXTERNAL = True
```

See also [internal and external packages](/guides/intern-extern-pkgs).

(pkg-opt-extopt)=
## `LIBFOO_EXTOPT`

Specifies extension-specific options. Packages wishing to take advantage of
extension-specific capabilities can forward options to extensions by defining
a dictionary of values.

```python
LIBFOO_EXTOPT = {
    'option-a': True,
    'option-b': 'value',
}
```

(pkg-opt-extract-type)=
## `LIBFOO_EXTRACT_TYPE`

Specifies a custom extraction type for a package. If a configured extension
supports a custom extraction capability, the registered extraction type can
be explicitly registered in this option.

```python
LIBFOO_EXTRACT_TYPE = 'ext-custom-extract'
```

(pkg-opt-fetch-opts)=
## `LIBFOO_FETCH_OPTS`

Provides a means to pass command line options into the fetch process. This
option can be defined as a dictionary of string pairs or a list with strings
-- either way defined will generate argument values which may be included
in a fetch event. This field is optional. Not all site types may support
this option.

```python
LIBFOO_FETCH_OPTS = {
    # adds "--option value" to the command
    '--option': 'value',
}

# (or)

LIBFOO_FETCH_OPTS = [
    # adds "--some-option" to the command
    '--some-option',
]
```

(pkg-opt-fixed-jobs)=
## `LIBFOO_FIXED_JOBS`

Explicitly configure the total number of jobs a package can use. The
primary use case for this option is to help limit the total number of jobs
for a package that cannot support a large or any parallel build environment.

```python
LIBFOO_FIXED_JOBS = 1
```

(pkg-opt-git-config)=
## `LIBFOO_GIT_CONFIG`

:::{versionadded} 0.6
:::

Apply additional repository-specific Git configuration settings
([`git config`][git-config]) after a Git repository cache has been
initialized. By default, no repository-specific configurations are
introduced (i.e. all Git calls will use the global configuration set).

```python
LIBFOO_GIT_CONFIG = {
    'core.example': 'value',
}
```

(pkg-opt-git-depth)=
## `LIBFOO_GIT_DEPTH`

:::{versionadded} 0.4
:::

Limit fetching for a Git-based source to the specified number of commits. The
value provided will be used with the [`--depth`][git--depth] argument. By
default, the depth will be set to a value of `1`. If a developer wishes use
fetch all commits from all refspecs, a developer can specify a value of `0`.

While the default depth is a value of `1`, an exception is made when the depth
is not explicitly set and the [`LIBFOO_REVISION`](pkg-opt-revision) value
defined is a hash. For this case, if the revision is not found with the
implicitly-defined shallow depth of `1`, the entire history of the
repository will be fetched.

```python
LIBFOO_GIT_DEPTH = 0
```

See also [`LIBFOO_GIT_REFSPECS`](pkg-opt-git-refspecs) and
[configuration quirks](/guides/quirks/quirks).

(pkg-opt-git-refspecs)=
## `LIBFOO_GIT_REFSPECS`

:::{versionadded} 0.4
:::

List of addition refspecs to fetch when using a `git` VCS type. By default,
a Git fetch request will acquire all `heads` and `tags` refspecs. If a
developer wishes use revisions from different refspecs (for example, a pull
request), a developer can specify the additional refspecs to acquire when
fetching.

```python
LIBFOO_GIT_REFSPECS = ['pull/*']
```

(pkg-opt-git-submodules)=
## `LIBFOO_GIT_SUBMODULES`

:::{versionadded} 0.8
:::

Flag value to indicate whether a package's Git submodules should be
fetched/extracted during a package's own fetch/extraction stages. By default,
submodules are not fetched. Ideally, any dependencies for a package are
recommended to be defined in their own individual package; however, this
may not be ideal for all environments. When configured, submodules will be
cached in the same fashion as other Git-based packages. Note that submodule
caching is specific to the repository being processed (i.e. they cannot be
"shared" between other packages). If multiple packages have the same
dependency defined through a submodule, it is recommended to create a new
package and reference its contents instead.

```python
LIBFOO_GIT_SUBMODULES = True
```

(pkg-opt-git-verify-revision)=
## `LIBFOO_GIT_VERIFY_REVISION`

Flag value to indicate whether the target revision is required to be signed
before it can be used. When this value is set, the configured revision for a
repository will not be extracted unless the GPG signature is verified. This
includes if the public key for the author is not registered in the local
system or if the target revision is not signed.

```python
LIBFOO_GIT_VERIFY_REVISION = True
```

(pkg-opt-host-provides)=
## `LIBFOO_HOST_PROVIDES`

:::{versionadded} 0.13
:::

Hints at what host tools this package may be providing. A project may have a
series of prerequisites, which are checked at the start of a run. This is to
help ensure required host tools are available before attempting to build a
project. If a package is designed to provide a host package (e.g. when using
[`LIBFOO_INSTALL_TYPE`](pkg-opt-install-type) with the `host` option),
these packages can provide tools other packages may rely on. However,
prerequisites checks will occur before these packages may be built,
preventing a build from running. This option allows a developer to hint
at what tools a host package may provide. By specifying the name of a tool
in this option, an initial prerequisites check will not fail if a tool is
not available at the start of a run.

```python
LIBFOO_HOST_PROVIDES = 'some-tool'

# (or)

LIBFOO_HOST_PROVIDES = [
    'tool-a',
    'tool-b',
    'tool-c',
]
```

See also [`LIBFOO_INSTALL_TYPE`](pkg-opt-install-type).

(pkg-opt-internal)=
## `LIBFOO_INTERNAL`

Flag value to indicate that a package is an internal package. Internal
packages will not generate warnings if [hashes](hash-file), an
[ASCII-armor](ascii-armor) or [licenses](/guides/licenses) are missing.
When configured in [local-sources mode](/guides/local-sources-mode), package
sources are searched for in the local directory opposed to site fetched
sources. By default, packages are considered external unless explicitly
configured to be internal.

```python
LIBFOO_INTERNAL = True
```

See also [internal and external packages](/guides/intern-extern-pkgs).

(pkg-opt-no-extraction)=
## `LIBFOO_NO_EXTRACTION`

```{warning}
If `LIBFOO_NO_EXTRACTION` is configured for a package, the package cannot
define additional [hashes](hash-file), configure an
[ASCII-armor](ascii-armor), define a list of `LIBFOO_LICENSE_FILES` to
manage or expect to support various actions (such as building, since no
sources are available).
```

:::{versionadded} 0.3
:::

Flag value to indicate that a package should not extract the package
contents. This feature is primarily used when using releng-tool to fetch
content for one or more packages (into `DL_DIR`) to be used by another
package the releng-tool project defines.

```python
LIBFOO_NO_EXTRACTION = True
```

Limitations exist when using the `LIBFOO_NO_EXTRACTION` option. Since
releng-tool will not be used to extract a package's archive (if any), hash
entries for files found inside the archive cannot be checked against. If
any files other than the archive itself is listed, releng-tool will stop
processing due to a hash check failure. In addition, since releng-tool does
not have the extracted contents of an archive, it is unable to acquire a
copy of the project's license file. Specifying `LIBFOO_LICENSE_FILES` for
projects with the no-extraction flag enabled will result in a warning. By
default, this option is disabled with a value of `False`.

(pkg-opt-patch-subdir)=
## `LIBFOO_PATCH_SUBDIR`

:::{versionadded} 0.15
:::

Sub-directory where any package patches should be applied to. By default,
patches are applied to the root of the extracted sources for a package. This
option can be useful for packages which utilize
[`LIBFOO_BUILD_SUBDIR`](pkg-opt-build-subdir) to work in a container
directory for sources which contain multiple modules, but has prepared
patches tailored for the specific module being targeted.

```python
LIBFOO_PATCH_SUBDIR = 'subdir'
```

See also [`LIBFOO_BUILD_SUBDIR`](pkg-opt-build-subdir).

(pkg-opt-prefix)=
## `LIBFOO_PREFIX`

Specifies the sysroot prefix value to use for the package. An explicitly
provided prefix value will override the project-defined or default sysroot
prefix value.

```python
LIBFOO_PREFIX = '/usr'
```

See also [`sysroot_prefix`](conf-sysroot-prefix).

(pkg-opt-remote-config)=
## `LIBFOO_REMOTE_CONFIG`

Flag value to indicate that a package should attempt to load any package
configurations which may be defined in the package's source. If the package
includes a `.releng-tool` file at the root of their sources, supported
configuration options that have not been populated will be registered into
the package before invoking a package's configuration stage.

```python
LIBFOO_REMOTE_CONFIG = True
```

See also
[`releng.disable_remote_configs` quirk](quirk-releng.disable_remote_configs).

(pkg-opt-remote-scripts)=
## `LIBFOO_REMOTE_SCRIPTS`

Flag value to indicate that a package should attempt to load any package
scripts which may be defined in the package's source. Typically, a
script-based package will load configuration, build, etc. scripts from its
package definition folder. If a script-based package is missing a stage script
to invoke and finds an associated script in the package's source, the detected
script will be invoked. For example, if `libfoo` package may attempt to load
a `libfoo-configure` script for a configuration stage. In the event that the
script cannot be found and remote scripting is permitted for a package, the
script (if exists) `releng-configure` will be loaded from the root of the
package's contents.

```python
LIBFOO_REMOTE_CONFIG = True
```

See also
[`releng.disable_remote_scripts` quirk](quirk-releng.disable_remote_scripts).

(pkg-opt-revision)=
## `LIBFOO_REVISION`

Specifies a revision value for a package. When a package fetches content
using source management tools, the revision value is used to determine
which sources should be acquired (e.g. a tag). If a revision is not
defined package, a package will use the configured
[`LIBFOO_VERSION`](pkg-opt-version).

```python
LIBFOO_REVISION = 'libfoo-v2.1'
```

For users planning to take advantage of
[development mode](/guides/development-mode) capabilities, multiple
revisions can be configured based off the mode:

```python
LIBFOO_REVISION = {
    DEFAULT_REVISION: 'libfoo-v2.1',
    'develop': 'main',
}
```

See also [`LIBFOO_DEVMODE_REVISION`](pkg-opt-devmode-revision) and
[`LIBFOO_VERSION`](pkg-opt-version).

(pkg-opt-strip-count)=
## `LIBFOO_STRIP_COUNT`

Specifies the strip count to use when attempting to extract sources from an
archive. By default, the extraction process will strip a single directory
from an archive (value: `1`). If a package's archive has no container
directory, a strip count of zero can be set; likewise if an archive
contains multiple container directories, a higher strip count can be set.

```python
LIBFOO_STRIP_COUNT = 1
```

(pkg-opt-vcs-type)=
## `LIBFOO_VCS_TYPE`

:::{versionchanged} 0.4 Support added for `local`.
:::
:::{versionchanged} 0.10 Support added for `rsync`.
:::
:::{versionchanged} 0.17 Support added for `perforce`.
:::

Explicitly sets the version control system type to use when acquiring
sources. releng-tool attempts to automatically determine the VCS type of
a package based off a [`LIBFOO_SITE`](pkg-opt-site) value. In some
scenarios, a site value may be unable to specify a desired prefix/postfix.
A developer can instead explicitly set the VCS type to be used no matter
what the site value is configured as.

Supported types are as follows:

- `bzr` (Bazaar)
- `cvs` (CVS)
- `git` (Git)
- `hg`  (Mercurial)
- `local` (no VCS; local interim-development package)
- `none` (no VCS; virtual package)
- `perforce` (Perforce)
- `rsync` (rsync)
- `scp` (SCP)
- `svn` (SVN)
- `url` (URL)

```python
LIBFOO_VCS_TYPE = 'git'
```

If a project registers a custom extension which provides a custom VCS
type, the extension type can be set in this option.

For users planning to take advantage of
[development mode](/guides/development-mode) capabilities with mode-specific
sites, users can provide an explicit VCS type based off a configured mode:

```python
LIBFOO_VCS_TYPE = {
    DEFAULT_REVISION: 'git',
    'legacy': 'cvs',
}
```

Using a specific type will create a dependency for a project that the
respective host tool is installed on the host system. For example, if a
Git VCS-type is set, the host system will need to have `git` installed on
the system.

The use of the `local` type is designed to be a special/development-helper
type only. When set, this option allows placing the sources of a package
directly inside a `local` folder inside the definition folder. For example,
a package `libfoo` configured with a local type would be structured as
follows:

```
└── my-releng-tool-project/
    ├── package/
    │   └── libfoo/
    │       └── local/                <----
    │       │   └── src/
    │       │   |   └── ...
    │       │   └── Makefile
    │       └── libfoo.rt
    ...
```

This approach is similar to using
[local-sources mode](/guides/local-sources-mode), where it avoids the
need to have the module content located in a site to be fetched --
specifically, for initial development/testing/training scenarios.
It is never recommended to store the package's "main content" inside a
releng-tool project, thus using the `local` type will always generate a
warning message.


[git--depth]: https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---depthltdepthgt
[git-config]: https://git-scm.com/docs/git-config
