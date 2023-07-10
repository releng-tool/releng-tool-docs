# Patching

:::{note}
Patches are ignored when in [development mode](development-mode) for
packages with a development revision, for `local` VCS packages or when in
[local-sources mode](local-sources-mode) for internal packages.
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
[development mode](development-mode), patches will not be applied if a
package defines a development revision. The idea is that a development
revision is most likely the bleeding edge source of a package and does not
need any patches. If a user configures their build environment in
[local-sources mode](local-sources-mode) and a package is defined as
internal, patches will not be applied to the sources. This is to prevent the
patching system from making unexpected modifications to a developer's local
sources.
