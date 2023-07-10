# Contributor guide

The following outlines common directory locations:

- `Documentation` - Project documentation
- `releng_tool/api/` - API for supporting releng-tool extensions
- `releng_tool/engine/` - Core implementation
- `releng_tool/ext/` - Extensions that are maintained in the official tree
- `releng_tool/extract/` - Translate fetched content to a build's working area
- `releng_tool/fetch/` - Support for fetching content from package sites
- `releng_tool/tool/` - Definitions for host tools used by tool features
- `test/` - Testing-related content for this project's implementation

releng-tool is built on the Python language and aims to be the minimum
dependency for users of the tool. Specific features enabled by a developer's
project may require additional tools (e.g. using [Git][git] to fetch sources
requires `git` to be installed); however, a user should not be required to
install tools for features that are not being used.

## Contributing

Developers are free to submit contributions for this project. Developers wishing
to contribute should read this project's [CONTRIBUTING][CONTRIBUTING] document.
A reminder that any contributions must be signed off with the
[Developer Certificate of Origin][dco].

Implementation (source, comments, commits, etc.) submitted to this project
should be provided in English.

## Root directory

A user invoking releng-tool will attempt to operate in a project root directory.
Any content managed by this tool (e.g. creating directories, downloading
sources, etc.) should all be performed inside the root directory. Some
exceptions exist where a user requests to adjust the download directory (e.g.
providing the `--dl-dir` argument).

## Fetching design

Packages can describe where external content should be fetched from. The most
common fetching method is a simple URI-style fetch such as downloading an
archive from an HTTP/FTP location. Assets acquired in this manner are downloaded
into the root directory's download folder (e.g. `<ROOT>/dl`). The extraction
phase will later use this folder to find package content to prepare against.

releng-tool also supports the fetching of content from version control systems.
Sources can either be fetched and placed into an archive, in a similar fashion
as fetching an archive from HTTP/FTP locations, or sources can be fetched into a
"cache directory" if supported (typically distributed version controlled
sources). For example, [Git][git] repositories (see also Git's
[`--git-dir`][--git-dir] will be stored in the root directory's cache folder
(e.g. `<ROOT>/cache`). During the extraction stage, target revisions will
be pulled from the cache location using the `git` client.

Not all packages will fetch content (e.g. placeholder packages).

## Extraction design

In most cases, the extraction phase will process archives (e.g. `.tar.gz`,
`.zip`, etc.) and place their contents into a package's build working
directory. Implementation will vary for fetching implementation which stores
content into a cache directory. For example, [Git][git] and
[Mercurial][mercurial] sources have their own extraction implementations to
pull content from their respective distributed file systems into a package's
build working directory.

## Host and Build environment

releng-tool attempts to minimize the impact of a host system's environment on a
project's build. For example, the build phase of a package should not be pulling
compiler flags provided from the host system's environment. These flags should
be provided from the package definition. Tools invoked by releng-tool will
attempt to be invoked to ignore these external environment variables. Some
exceptions apply such as environment variables dealing with authorization
tokens.

## Documentation

Improvements to this project's documentation are always welcome -- not only
for adding/updating documentation for releng-tool features but also
translations.

For users interested in documentation for this project, please see the
following repository:

> releng-tool -- Documentation\
> <https://github.com/releng-tool/releng-tool-docs>

[--git-dir]: https://git-scm.com/docs/git#Documentation/git.txt---git-dirltpathgt
[CONTRIBUTING]: https://github.com/releng-tool/releng-tool/blob/main/CONTRIBUTING.md
[dco]: https://developercertificate.org/
[git]: https://git-scm.com/
[mercurial]: https://www.mercurial-scm.org/
