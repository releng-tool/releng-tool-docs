# Patching

:::{note}
Patches are ignored when in [development mode](development-mode) by default
for packages with a development revision, for `local` VCS packages or when
in [local-sources mode](local-sources-mode) for internal packages.
:::

:::{versionchanged} 2.9
Additional configuration modes to permit development revisions to have
patches applied.
:::
:::{versionchanged} 3.1
The working directory will now be updated to account for
[`PKG_BUILD_DIR`](env-pkg-build-dir) (and possibly
[`LIBFOO_PATCH_SUBDIR`](pkg-opt-patch-subdir)) when using a patch script.
:::

The patching stage for a package provides the ability for a developer to apply
one or more patches to extracted sources. A project may take advantage of
acquiring sources from one or more externally managed implementations.
Fetched sources may not be able to build in a developer's releng-tool
project due to limitations of the implementation or build scripts provided
by the package. A developer can prepare a series of patches to apply to a
package and submit changes upstream to correct the issue. However, the
developer is then left to either wait for the changes to be merged in or
needs to make a custom archive with the appropriate modifications already
applied. To avoid this, a developer can include patches directly in the
package folder to be automatically applied during patching stage.

When a package's patch stage is reached, releng-tool will look for patches
found inside the package folder with the extension `.patch`. Patches found
inside a package folder are applied in ascending order. It is recommended
to prefix patch filenames with a numerical value for clarity. For example,
the following package patches:

```shell-session
$ cd package/liba
$ ls *.patch
0001-accept-linker-flags.patch
0002-correct-output-path.patch
0003-support-disabling-test-build.patch
liba
liba.hash
```

With be applied in the following order:

1. `0001-accept-linker-flags.patch`
2. `0002-correct-output-path.patch`
3. `0003-support-disabling-test-build.patch`

If a user configures their build environment in
[development mode](development-mode), patches will not be applied by default
if a package defines a development revision. The idea is that a development
revision is most likely the bleeding edge source of a package and does not
need any patches. If a user configures their build environment in
[local-sources mode](local-sources-mode) and a package is defined as
internal, patches will not be applied to the sources. This is to prevent the
patching system from making unexpected modifications to a developer's local
sources.

In the scenario where a developer does want to override when patches are
applied, there are a couple of advanced options. First, the option
[`LIBFOO_IGNORE_PATCHES`](pkg-opt-ignore-patches) allows a developer to avoid
the automatic application of patches on a package during normal runs. Second,
the option [`LIBFOO_DEVMODE_PATCHES`](pkg-opt-devmode-patches) can be
configured to permit a package to utilize patches in a development mode.

For example, the following configuration will instead only apply patches on
a package when releng-tool is operating in a development mode and the package
defines a development revision:

```python
LIBFOO_DEVMODE_PATCHES = True
LIBFOO_IGNORE_PATCHES = True
```

An alternative to using patch files is supported via a patch script. Similar
to [script-based packages](packages/pkg-type-script), all package can opt for
using a Python-based `<package>-patch.rt` script.

For example, a `libfoo` package could have the following patch file:

```
└── my-releng-tool-project/
    ├── package/
    │   └── libfoo/
    │       ├── libfoo.rt
    │       └── libfoo-patch.rt
    ...
```

When a patch script is defined, no patch files are automatically applied. It
is assumed developers want to control any type of patching from a provided
script.

The patch script is typically invoked with a
[`PKG_BUILD_DIR`](env-pkg-build-dir) working directory. In the event
[`LIBFOO_PATCH_SUBDIR`](pkg-opt-patch-subdir) is configured, the working
directory will be adjusted for the configured sub-directory.
