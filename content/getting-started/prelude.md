# Prelude

A releng-tool project can define multiple packages, each can be based off of
different languages, configured to use custom toolchains and more. Every
package has multiple stages (such as fetching, configuring, building, etc.)
which can help contribute to a target sysroot. Once all packages are
processed, the target sysroot can be packaged for distribution.

The following outlines the common directory/file locations for a releng-tool
project:

- `cache/` - Cached content from select package sources (e.g. DVCS, etc.)
- `dl/` - Archives for select package sources (e.g. `.tgz`, `.zip`, etc.)
- `package/` - Container for packages
- `package/<package>/` - A package-specific folder
- `package/<package>/<package>` - A package definition
- `output/` - Container for all output content
- `output/build/` - Container for package building
- `output/host/` - Area to hold host-specific content
- `output/images/` - Container for final images/archives
- `output/staging/` - Area to hold staged sysroot content
- `output/target/` - Area to hold target sysroot content
- `releng-tool.rt` - Project configuration

How these directories and files are used can vary on how a developer defines a
releng-tool project. Consider the following process:

1. releng-tool will load the project's configuration and respective package
   definitions to determine what steps need to be performed.
2. Package sources can be downloaded into either the `cache/` or `dl/`
   folder, depending on what type of sources will be fetched. For example, Git
   sources will be stored inside of the `cache/` to take advantage of its
   distributable nature, and archive files (such as `.tgz`, `.zip`, etc.)
   will be stored inside the `dl/` directory.
3. Each package will be extracted into its own output directory inside
   `output/build/`. The working areas for packages allow a package to be
   patched, configured and built based on how the developer configures the
   respective packages.
4. Once packages are built, their final executables, libraries, etc. can be
   installed into either the host area (`output/host/`), staging area
   (`output/staging/`) or the target area (`output/target/`) depending on
   what has been built. The target area is designed for the final set of assets
   produced from a build; the intent is that the files contained inside this
   folder are planned to be used on a target system (stripped, cross-compiled,
   etc.). A staging area is like a target area but may contain more content such
   as headers not intended for a final target, interim development assets and
   more. Host content is designed for content built for the host system which
   other packages may depend on.
5. At the end of the releng-tool process, a post-stage script can be invoked to
   help archive/package content from the target area (`output/target/`) into
   the images folder (`output/images/`). For example, generating an archive
   `output/images/my-awesome-project-v1.0.0.tgz`.

Not all projects may use each of these folders or take advantage of each stage.
While various capabilities exist, it does not mean releng-tool will handle all
the nitty-gritty details to make a proper build of a project. For example:

- If a developer wishes to cross-compile a package to a target, they must ensure
  the package is configured in the proper manner to use a desired toolchain.
- If a developer wants to process a Python package, they must ensure the proper
  interpreter is used if they cannot rely on the host's default interpreter.
- If a developer creates script-based packages, they must ensure that these
  scripts properly handle multiple re-invokes (e.g. if a user performs a
  rebuild on a package).

releng-tool will attempt to provide an easy way to deal with fetching sources,
ensuring projects are invoked in order, and more; however, the more advanced
features/actions a developer may want in their project (such as the examples
mentioned above), the more a developer will need to manage their project.
