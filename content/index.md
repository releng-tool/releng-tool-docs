---
hide-toc: true
---

# releng-tool

releng-tool aims to provide a way for developers to tailor the building of
multiple software components to help prepare packages for desired runtime
environments (e.g. cross-platform portable packages, embedded targets, etc.).
When building a package, assets may be located in multiple locations and may
require various methods to extract, build and more. releng-tool allows
developers to define a set of packages, specifying where resources should be
fetched from, how packages should be extracted and the processes for
patching, configuring, building and installing each package for a target
sysroot.

:::{raw} html
:file: _static/overview-furo.svg
:::

The structure of a package depends on the specific project. The simplest
type is a script-based package, where users can define custom scripts for
various stages. A package does not need to handle every stage. Helper
package types are available (e.g. Autotools, Cargo, CMake, Make, Meson,
various Python types and SCons) for projects using common build systems.

While releng-tool assists in configuring and building projects, it does not
aim to provide a perfect sandbox for the process. Users are responsible
for defining the compilers/toolchains used and managing the interaction
between the staging/target area with the host system.

:::{toctree}
:maxdepth: 5

requirements
install
getting-started/getting-started
guides/guides
examples/examples
help
contributors
:::

:::{toctree}
:maxdepth: 1

release-notes
annex-a
:::
