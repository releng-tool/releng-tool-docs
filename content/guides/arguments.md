# Arguments

The command line can be used to specify a single action to perform or
provide various options to configure the releng-tool process. Options
can be provided before or after an action (if an explicit action is provided).
By default, if a user does not specify an action, it is assumed that all
steps are to be performed.

```shell
releng-tool <options> [action]
```

## Global actions

The following outlines available global actions:

(action-clean)=
### `clean`

Clean (removes) a series of folders holding content such as extracted
archives, built libraries and more.


```shell
releng-tool clean
```

Images and downloaded assets/cache are not removed (see
[`mrproper`](action-mrproper) for a more through all cleaning operation).
This clean operation will remove files based off the configured output
directory. If an output directory is provided (i.e. `--out-dir <dir>`)
during a clean event, select folders inside this directory will be removed
instead of the output directory (if any) found in the root directory.

(action-distclean)=
### `distclean`

Perform a more extreme pristine clean of the releng-tool project.

```shell
releng-tool distclean
```

This request removes the `cache/`, `dl/` and `output/` directories found
in the root directory or overridden by respective arguments, as well as
any mode file flags which may be set. See also the [`clean`](action-clean)
or [`mrproper`](action-mrproper) actions.

### `extract`

All packages will be processed up to the extraction phase (inclusive).

```shell
releng-tool extract
```

(action-fetch)=
### `fetch`

All packages will be processed up to the fetch phase (inclusive).

```shell
releng-tool fetch
```

```{tip}
When a `fetch` is explicitly requested for DVCS sources (e.g. Git), the
local cache kept for the repository will be updated against the
configured remote. This can be helpful for packages which use a branch
for their target revision, or wishing to use a tag which has been moved.

Users may also take advantage of explicit re-fetching of downloaded
artifacts when using this action in combination with the [](arg-force)
argument.
```

See also [offline builds](tips/offline-builds).

### `init`

Initialize an empty root directory with a sample project.

```shell
releng-tool init
```

### `licenses`

A request to generate all license information for the project.

```shell
releng-tool licenses
```

Note that license information requires acquiring license documents from
packages. Therefore, packages will be fetched/extracted if not already done.

(action-mrproper)=
### `mrproper`

Perform a pristine clean of the releng-tool project.

```shell
releng-tool mrproper
```

This request removes the `output/` directory found in the root directory or
overridden by the `--out-dir` argument, as well as any mode file flags
which may be set. The `cache/` and `dl/` directories will remain untouched.
See also the [`clean`](action-clean) or [`distclean`](action-distclean)
actions.

### `patch`

All packages will be processed up to the patch phase (inclusive).

```shell
releng-tool patch
```

(action-sbom)=
### `sbom`

A request to generate a software build of materials (SBOM) for the project.

```shell
releng-tool sbom
```

By default, a releng-tool run will generate an SBOM file at the end of a
run. This action can be used to generate an SBOM without requiring a build.

### `state`

A request to dump active state information for a project.

```shell
releng-tool state
```

A state request can be used to dump any active configuration and operating
modes.

## Package actions

The following outlines available package-specific actions:

### `<pkg>-build`

Performs the build stage for the package.

```shell
releng-tool <pkg>-build
```

On success, the specified package will have completed its build.
If a package has any package dependencies, these dependencies will be
processed before the specified package. If the provided package name does
not exist, a notification will be generated.

(action-pkg-clean)=
### `<pkg>-clean`

Cleans the build directory for package (if it exists).

```shell
releng-tool <pkg>-clean
```

See also the [`<pkg>-distclean`](action-pkg-distclean) action.

### `<pkg>-configure`

Performs the configure stage for the package.

```shell
releng-tool <pkg>-configure
```

On success, the specified package will have completed its configuration
stage. If a package has any package dependencies, these dependencies will
be processed before the specified package. If the provided package name
does not exist, a notification will be generated.

(action-pkg-distclean)=
### `<pkg>-distclean`

Perform a pristine clean of a releng-tool package.

```shell
releng-tool <pkg>-distclean
```

This request not only removes the build directory but also any cached file
or directory associated with the package. See also the
[`<pkg>-clean`](action-pkg-clean) action.

### `<pkg>-exec "<cmd>"`

Invokes a provided command in the package's build output directory. This
package action can be useful for developers attempting to develop/debug a
specific package, allowing an easy way to issue commands in a package's
directory without having to manually venture to a package's output
directory. Packages will need to be processed to at least the patch stage
before a provided command is issued.

An example is as follows:

```shell
releng-tool libfoo-exec "mycmd arg1 arg2"
```

Package environment variables will be available for the invoked command.

### `<pkg>-extract`

Performs the extraction stage for the package.

```shell
releng-tool <pkg>-extract
```

On success, the specified package will have completed its extraction stage.
If the provided package name does not exist, a notification will be
generated.

(action-pkg-fetch)=
### `<pkg>-fetch`

Performs the fetch stage for the package.

```shell
releng-tool <pkg>-fetch
```

On success, the specified package stage will have completed its fetch stage.
If the provided package name does not exist, a notification will be
generated.

### `<pkg>-install`

Performs the installation stage for the package.

```shell
releng-tool <pkg>-install
```

On success, the specified package will have completed its installation
stage. If a package has any package dependencies, these dependencies will
be processed before the specified package. If the provided package name
does not exist, a notification will be generated.

### `<pkg>-license`

A request to generate the license information for a specific package
in a project.

```shell
releng-tool <pkg>-license
```

Note that license information requires acquiring license documents from
the package itself. Therefore, the package will be fetched/extracted if
not already done.

### `<pkg>-patch`

Performs the patch stage for the package.

```shell
releng-tool <pkg>-patch
```

On success, the specified package will have completed its patch stage.
If the provided package name does not exist, a notification will be generated.

### `<pkg>-rebuild`

Force a rebuild of a specific package.

```shell
releng-tool <pkg>-rebuild
```

Once a package has been built, the package will not attempt to be built
again. Invoking a rebuild request will tell releng-tool to re-invoke the
build step again. This can be useful during times of development where a
developer attempts to change a package definition or sources between build
attempts. After completing a rebuild, releng-tool will perform the
remaining stages of the package (i.e. the installation phase). Users
wishing to perform only the rebuild stage are recommended to use
`<pkg>-rebuild-only` instead.

If using this action, ensure
[understanding rebuilds](/getting-started/rebuilds) has been read to
understand this action's effect.

### `<pkg>-rebuild-only`

Force a rebuild of a specific package.

```shell
releng-tool <pkg>-rebuild-only
```

Once a package has been built, the package will not attempt to be built
again. Invoking a rebuild request will tell releng-tool to re-invoke the
build step again. This can be useful during times of development where
a developer attempts to change a package definition or sources between
build attempts. After completing a rebuild, releng-tool will stop and
perform no other changes. Users wishing to perform a rebuild to the
installation phase are recommended to use `<pkg>-rebuild` instead.

If using this action, ensure
[understanding rebuilds](/getting-started/rebuilds) has been read to
understand this action's effect.

### `<pkg>-reconfigure`

Force a re-configuration of a specific package.

```shell
releng-tool <pkg>-rebuild-reconfigure
```

Once a package has been configured, the package will not attempt to
configure it again. Invoking a re-configuration request will tell
releng-tool to re-invoke the configuration step again. This can be useful
during times of development where a developer attempts to change a package
definition or sources between configuration attempts. After completing a
re-configuration, releng-tool will perform the remaining stages of the
package (i.e. all the way to the installation phase). Users wishing to
perform only the re-configuration stage are recommended to use
`<pkg>-reconfigure-only` instead.

If using this action, ensure
[understanding rebuilds](/getting-started/rebuilds) has been read to
understand this action's effect.

### `<pkg>-reconfigure-only`

Force a re-configuration of a specific package.

```shell
releng-tool <pkg>-reconfigure-only
```

Once a package has been configured, the package will not attempt to
configure it again. Invoking a re-configuration request will tell
releng-tool to re-invoke the configuration step again. This can be useful
during times of development where a developer attempts to change a package
definition or sources between configuration attempts. After completing a
re-configuration, releng-tool will stop and perform no other changes.
Users wishing to perform a re-configuration to the installation phase are
recommended to use `<pkg>-reconfigure` instead.

If using this action, ensure
[understanding rebuilds](/getting-started/rebuilds) has been read to
understand this action's effect.

### `<pkg>-reinstall`

Force a re-installation of a specific package.

```shell
releng-tool <pkg>-reinstall
```

Once a package has been installed, the package will not attempt to install
it again. Invoking a re-installation request will tell releng-tool to
re-invoke the installation step again. This can be useful during times of
development where a developer attempts to change a package definition or
sources between installation attempts.

If using this action, ensure
[understanding rebuilds](/getting-started/rebuilds) has been read to
understand this action's effect.

## Option arguments

The following outlines available options:

(arg-assets-dir)=
### `--assets-dir <dir>`

Directory to hold cache and download folders instead of using a configured
root directory.

```{note}
Configuring an asset directory override is only helpful when attempting to
configure a container for all assets. If a user also specifies `--cache-dir`
or `--dl-dir` overrides, this argument has no effect.
```

See also [](env-releng-assets-dir).

(arg-cache-dir)=
### `--cache-dir <dir>`

Directory for distributed version control cache information (defaults to
`<root>/cache`).

See also [](env-releng-cache-dir).

### `--config <file>`

Configuration file to load (defaults to `<root>/releng`).

### `--debug`

Show debug-related messages.

### `-D`, `--development [<mode>]`

Enables [development mode](development-mode).

(arg-dl-dir)=
### `--dl-dir <dir>`

Directory for download archives (defaults to `<root>/dl`).

See also [](env-releng-dl-dir).

(arg-force)=
### `-F`, `--force`

Triggers a forced request for the releng-tool invoke. This entails:

- Packages will be processed as if a re-configuration request has
  been made.
- If an explicit fetch request is made ([`fetch`](action-fetch) or
  [`<pkg>-fetch`](action-pkg-fetch)), any packages which cache to a file
  will have their cache files deleted to be re-fetched.

### `-h`, `--help`

Show a list of all arguments available by releng-tool.

### `--images-dir <dir>`

Directory for image outputs (defaults to `<root>/output/images`).

### `-j`, `--jobs <jobs>`

Numbers of jobs to handle (defaults to `0`; automatic).

### `-L`, `--local-sources [[<pkg>:]<dir>]`

Enables [local-sources mode](local-sources-mode).

Without a directory provided, sources of internal packages will be looked
for in the parent directory of the configured root directory. Users may
use this argument multiple times to override the local-sources
configuration. If a package-specific override is provided, sources for
that package will be looked for inside the provided path.

### `--nocolorout`

Explicitly disable colorized output.

```{tip}
releng-tool respects the `NO_COLOR` environment variable, if configured
in the running environment.
```

### `--out-dir <dir>`

Directory for output (builds, images, etc.; defaults to `<root>/output`).

### `--root-dir <dir>`

Directory to process a releng-tool project (defaults to the working
directory).

### `--sbom-format <fmt>`

The format to use when generating a software build of materials (SBOM).
Multiple formats can be provided (comma-separated).

| Type | Value |
| -: | :- |
| CSV | `csv` |
| HTML | `html` |
| JSON | `json` |
| JSON (SPDX) | `json-spdx` |
| RDP (SPDX) | `rdp-spdx` |
| Text | `text` (default) |
| XML | `xml` |

See also [`sbom`](action-sbom).

### `--quirk <quirk-id>`

Allows specifying a runtime [quirk](quirks/quirks) for the releng-tool
process. This option can be used multiple times to apply multiple quirks.

### `-V`, `--verbose`

Show additional messages.

### `--version`

Show releng-tool's version.

### `--werror`, `-Werror`

Treat warnings from releng-tool as errors.
