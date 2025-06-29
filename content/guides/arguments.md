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

:::{versionadded} 0.6
:::

Perform a more extreme pristine clean of the releng-tool project.

```shell
releng-tool distclean
```

This request removes the `cache/`, `dl/` and `output/` directories found
in the root directory or overridden by respective arguments, as well as
any mode file flags which may be set. See also the [`clean`](action-clean)
or [`mrproper`](action-mrproper) actions.

(action-extract)=
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

See also [offline builds](tips/offline-builds) and the
[`fetch-full`](action-fetch-full) action.

(action-fetch-full)=
### `fetch-full`

:::{versionadded} 1.3
:::

All packages will be processed up to the extraction phase, as well as any
post-extraction fetch operations for supported package types (e.g. fetching
Cargo dependencies).

```shell
releng-tool fetch-full
```

See also the [`fetch`](action-fetch) action.

(action-init)=
### `init`

:::{versionadded} 0.6
:::

Initialize an empty root directory with a sample project.

```shell
releng-tool init
```

(action-licenses)=
### `licenses`

A request to generate all license information for the project.

```shell
releng-tool licenses
```

Note that license information requires acquiring license documents from
packages. Therefore, packages will be fetched/extracted if not already done.

(action-mrproper)=
### `mrproper`

:::{versionadded} 0.6
:::

Perform a pristine clean of the releng-tool project.

```shell
releng-tool mrproper
```

This request removes the `output/` directory found in the root directory or
overridden by the `--out-dir` argument, as well as any mode file flags
which may be set. The `cache/` and `dl/` directories will remain untouched.
See also the [`clean`](action-clean) or [`distclean`](action-distclean)
actions.

(action-patch)=
### `patch`

All packages will be processed up to the patch phase (inclusive).

```shell
releng-tool patch
```

See also [Patching](patching).

(action-punch)=
### `punch`

:::{versionadded} 1.2
:::

A punch request acts in a similar fashion as if no global action was provided.
All configured packages will be processed to their completion and any post
actions will be run. The difference between a default run and a punch run is
when a punch run is requested, any packages that have already been processed
will be re-invoked as if a re-configuration request has been made.

This allows a developer to easily attempt to rebuild all packages in their
project when multiple packages have been updated.

```shell
releng-tool punch
```

(action-sbom)=
### `sbom`

:::{versionadded} 0.14
:::

A request to generate a software build of materials (SBOM) for the project.

```shell
releng-tool sbom
```

By default, a releng-tool run will generate an SBOM file at the end of a
run. This action can be used to generate an SBOM without requiring a build.

See also [`--sbom-format <fmt>`](arg-sbom-format) (argument) and
[`sbom_format`](conf-sbom-format) (configuration).

(action-state)=
### `state`

:::{versionadded} 0.17
:::

A request to dump active state information for a project.

```shell
releng-tool state
```

A state request can be used to dump any active configuration and operating
modes.

## Package actions

The following outlines available package-specific actions:

(action-pkg-build)=
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

(action-pkg-configure)=
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

:::{versionadded} 0.8
:::

Perform a pristine clean of a releng-tool package.

```shell
releng-tool <pkg>-distclean
```

This request not only removes the build directory but also any cached file
or directory associated with the package. See also the
[`<pkg>-clean`](action-pkg-clean) action.

(action-pkg-exec)=
### `<pkg>-exec "<cmd>"`

:::{versionadded} 0.12
:::
:::{versionchanged} 1.4 Support accepting arguments after `--`.
:::
:::{versionchanged} 2.5
When using `--` with this call, [`releng_args`](vars-releng_args) is no
longer populated.
:::

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

Alternatively, arguments can be passed using the format:

```shell
releng-tool libfoo-exec -- mycmd arg1 arg2
```

Package environment variables will be available for the invoked command.

See also [`RELENG_EXEC`](env-releng-exec) and [`releng_args`](vars-releng_args).

(action-pkg-extract)=
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

(action-pkg-fetch-full)=
### `<pkg>-fetch-full`

:::{versionadded} 1.3
:::

Performs the fetch and extraction stages for the package, as well as any
post-extraction fetch operations for the supported package type (e.g.
fetching Cargo dependencies).

```shell
releng-tool <pkg>-fetch-full
```

If the provided package name does not exist, a notification will be
generated.

(action-pkg-fresh)=
### `<pkg>-fresh`

:::{versionadded} 1.4
:::

Prepares a package to be ready to invoke its configuration stage. A
successful end state results in the specified package will have
completed its patch stage. If the package has already been processed
before, it will be cleaned ahead of time to start fresh.

```shell
releng-tool <pkg>-fresh
```

If the provided package name does not exist, a notification will be
generated.

(action-pkg-install)=
### `<pkg>-install`

Performs the installation stage for the package.

```shell
releng-tool <pkg>-install
```

On success, the specified package will have completed its installation
stage. If a package has any package dependencies, these dependencies will
be processed before the specified package. If the provided package name
does not exist, a notification will be generated.

(action-pkg-license)=
### `<pkg>-license`

:::{versionadded} 0.8
:::

A request to generate the license information for a specific package
in a project.

```shell
releng-tool <pkg>-license
```

Note that license information requires acquiring license documents from
the package itself. Therefore, the package will be fetched/extracted if
not already done.

(action-pkg-patch)=
### `<pkg>-patch`

Performs the patch stage for the package.

```shell
releng-tool <pkg>-patch
```

On success, the specified package will have completed its patch stage.
If the provided package name does not exist, a notification will be generated.

(action-pkg-rebuild)=
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

(action-pkg-rebuild-only)=
### `<pkg>-rebuild-only`

:::{versionadded} 0.7
:::

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

(action-pkg-reconfigure)=
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

(action-pkg-reconfigure-only)=
### `<pkg>-reconfigure-only`

:::{versionadded} 0.7
:::

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

(action-pkg-reinstall)=
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

:::{versionadded} 0.10
:::

Directory to hold cache and download folders instead of using a configured
root directory.

```{note}
Configuring an asset directory override is only helpful when attempting to
configure a container for all assets. If a user also specifies `--cache-dir`
or `--dl-dir` overrides, this argument has no effect.
```

See also [`RELENG_ASSETS_DIR`](env-releng-assets-dir).

(arg-cache-dir)=
### `--cache-dir <dir>`

Directory for distributed version control cache information (defaults to
`<root>/cache`).

See also [`RELENG_CACHE_DIR`](env-releng-cache-dir).

(arg-config)=
### `--config <file>`

:::{versionadded} 0.13
:::

Configuration file to load (defaults to `<root>/releng-tool.rt`).

See also [alternative extensions](/guides/tips/alternative-extensions) that
may apply when detecting the default configuration file.

(arg-debug)=
### `--debug`

Show debug-related messages.

(arg-debug-extended)=
### `--debug-extended`

Show extended debug-related messages, such as process execution arguments and
environment variables.

(arg-development)=
### `--development [<mode>]`, `-D [<mode>]`

:::{versionchanged} 0.13 Support configurable modes.
:::

Enables [development mode](development-mode).

(arg-dl-dir)=
### `--dl-dir <dir>`

Directory for download archives (defaults to `<root>/dl`).

See also [`RELENG_DL_DIR`](env-releng-dl-dir).

(arg-force)=
### `--force`, `-F`

:::{versionadded} 0.11
:::

Triggers a forced request for the releng-tool invoke. This entails:

- Packages will be processed as if a re-configuration request has
  been made.
- If an explicit fetch request is made ([`fetch`](action-fetch) or
  [`<pkg>-fetch`](action-pkg-fetch)), any packages which cache to a file
  will have their cache files deleted to be re-fetched.

(arg-help)=
### `--help`, `-h`

Show a list of all arguments available by releng-tool.

(arg-images-dir)=
### `--images-dir <dir>`

:::{versionadded} 0.13
:::

Directory for image outputs (defaults to `<root>/output/images`).

See also [`RELENG_IMAGES_DIR`](env-releng-images-dir).

(arg-jobs)=
### `--jobs <jobs>`, `-j <jobs>`

Numbers of jobs to handle (defaults to `0`; automatic).

See also [`RELENG_PARALLEL_LEVEL`](env-releng-parallel-level).

(arg-local-sources)=
### `--local-sources [[<pkg>:]<dir>]`, `-L [[<pkg>:]<dir>]`

:::{versionchanged} 0.13 Support configurable packages and directories.
:::
:::{versionchanged} 0.16 Support `:` (new) or `@` (original) as a separator.
:::

Enables [local-sources mode](local-sources-mode).

Without a directory provided, sources of
[internal packages](/guides/intern-extern-pkgs) will be looked for in the
parent directory of the configured root directory. Users may use this
argument multiple times to override the local-sources configuration. If
a package-specific override is provided, sources for that package will be
looked for inside the provided path.

(arg-nocolorout)=
### `--nocolorout`

Explicitly disable colorized output.

```{tip}
releng-tool respects the [`NO_COLOR`][no-color] environment variable, if
configured in the running environment.
```

(arg-only-mirror)=
### `--only-mirror`

:::{versionadded} 2.0
:::

Only fetch [external](pkg-opt-external) projects with configured mirror.

When releng-tool is fetching sources with [`url_mirror`](conf-url-mirror)
configured, package downloads will be first attempted on the mirror before
using their package-defined site. If a developer wishes to enforce a build
to only download external packages from the configured mirror, this option
can be provided when invoking releng-tool.

(arg-out-dir)=
### `--out-dir <dir>`

Directory for output (builds, images, etc.; defaults to `<root>/output`).

See also [`RELENG_OUTPUT_DIR`](env-releng-out-dir).

(arg-profile)=
### `--profile [<profile>]`, `-P [<profile>]`

:::{versionadded} 2.5
:::

Configure a profile to run with. Providing this option is only applicable if
a project accepts custom profile options. Multiple profiles can be provided
by repeating this argument. Multiple profiles can also be provided in a
single argument where profiles are separated by a comma (`,`) or a
semicolon (`;`).

See also [using profiles](profiles).

(arg-relaxed-args)=
### `--relaxed-args`

:::{versionadded} 1.3
:::

Do not throw an error when releng-tool is provided unknown arguments.

See also [`RELENG_IGNORE_UNKNOWN_ARGS`](env-releng-ignore-unknown-args).

(arg-root-dir)=
### `--root-dir <dir>`

Directory to process a releng-tool project (defaults to the working
directory).

(arg-sbom-format)=
### `--sbom-format <fmt>`

:::{versionadded} 0.14
:::
:::{versionchanged} 2.4 `rdp-spdx` renamed to `rdf-spdx`.
:::

The format to use when generating a software build of materials (SBOM).
Multiple formats can be provided (comma-separated).

| Type | Value |
| -: | :- |
| CSV | `csv` |
| HTML | `html` |
| JSON | `json` |
| JSON (SPDX) | `json-spdx` |
| RDF (SPDX) | `rdf-spdx` |
| Text | `text` (default) |
| XML | `xml` |

See also [`sbom`](action-sbom) (action) and [`sbom_format`](conf-sbom-format)
(configuration).

(arg-quirk)=
### `--quirk <quirk-id>`

:::{versionadded} 0.4
:::

Allows specifying a runtime [quirk](quirks/quirks) for the releng-tool
process. This option can be used multiple times to apply multiple quirks.

(arg-verbose)=
### `--verbose`, `-V`

Show additional messages.

(arg-version)=
### `--version`

Show releng-tool's version.

(arg-werror)=
### `--werror`, `-Werror`

:::{versionadded} 0.14
:::

Treat warnings from releng-tool as errors.

(arg-variable-injection)=
## Variable injection

:::{versionadded} 0.12
:::

Users can override a select set of variables by defining them in the command
line arguments. For example, consider a project that defines a `libfoo`
package with a version `1.0`:

```python
LIBFOO_VERSION = '1.0'
```

If a user wants to override this a run with `1.1`, the following can be used:

```shell
releng-tool LIBFOO_VERSION=1.1
```


[no-color]: https://no-color.org/
