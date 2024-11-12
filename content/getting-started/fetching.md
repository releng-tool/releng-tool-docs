# Understanding fetching

The first stage packages go through is the "fetch" phase. For packages
which have content to acquire, files can be downloaded or version control
sources may be locally cached. For example, if a package has a link to a
file to download:

```python
LIBFOO_SITE = 'https://example.com/libfoo-1.0.tgz'
```

The file will be stored in the download folder, ready to be used for
extraction:

```
└── my-project/
    ├── dl/
    │   └── libfoo/
    │       └── libfoo-1.0.tgz       <----
    ├── package/
    │   └── libfoo/
    │       └── ...
    └── releng-tool.rt
```

And for DVCS-based sites:

```python
LIBFOO_SITE = 'git+git@example.com:base/libfoo.git'
```

The contents of the repository will be stored in the cache folder for later
use:

```
└── my-project/
    ├── cache/
    │   └── libfoo/
    │       └── ...                  <----
    ├── package/
    │   └── libfoo/
    │       └── ...
    └── releng-tool.rt
```

Once a package has completed its fetch stage, releng-tool should never need
to remotely fetch content for that package again (until site, version, etc.
changes). In the event that a user invokes a [`clean`](action-clean) action
followed by a full build:

```shell-session
$ releng-tool clean
$ releng-tool
...
```

No fetching may occur since package contents may already be stored in the
existing `dl/` and `cache/` folders.

A problem a user may experience is if they wish to re-acquire sources from
a site if they know the sources have changed. For example, if a remote
archive has been updated, if a tag has been moved or if a target branch
has been updated. The following will present a series of ways a user can
deal with these use cases.

## Start fresh!

```{tip}
While this approach ensures the most recent sources for the existing
package configurations are fetched, it can be time consuming to clear the
entire cache if, for example, only a single package has changed.

It is recommended to look at all available options to re-fetch content.
```

The easiest way to ensure all fresh sources are downloaded is to clean all
local downloads/cache for a project. This can be achieved using
[`distclean`](action-distclean):

```
releng-tool distclean
```

This will ensure all downloaded files, cached content, etc. are removed
from the local system, ensuring a next-build to download fresh sources.

## Full fetching

Most package sources are acquired during the fetch stage. However, some
packages define dependencies within their sources. This can require
releng-tool to first fetch a defined package's sources, extract the
package, followed by fetching any defined dependencies. Post-fetching
will be automatically performed for supported packages (e.g. Cargo) after
their extraction stage. Users can invoke the [`fetch-full`](action-fetch-full)
action to explicitly process releng-tool's fetch-post operations:

```
releng-tool fetch-full
```

## Force re-fetch of DVCS sources

When a DVCS-based package goes through its fetch stage, the contents can
be locally stored in the configured cache directory. For a package definition
as follows:

```python
LIBFOO_SITE = 'git+git@example.com:base/libfoo.git'
LIBFOO_REVISION = 'v1.0'
```

A cache of the `v1.0` tag will be fetched and stored locally. If a package
is cleaned and rebuilt again, releng-tool will referred to the locally
cached tag. In the event that the remote site changes the tag location,
clean builds will not be using the most recent tag location. If a user
knows the reference for a site has been updated, they can explicitly
request a [`<pkg>-fetch`](action-pkg-fetch) on a package which should
trigger a forced update from the remote site. For example:

```
releng-tool libfoo-fetch
```

The above can recognize the new tag update, and any future clean builds
made will use the new reference implementation.

## Force re-fetch of fixed sources

For packages which reference a fixed artifact, once a package has completed
its fetch stage, the artifact will no longer need to be downloaded
again. For example:

```python
LIBFOO_SITE = 'https://example.com/libfoo-1.0.tgz'
```

The archive `libfoo-1.0.tgz` will be locally store and used in future
builds. In the event where a site's archive is known to have been changed,
a user can force re-fetch these artifacts by using the
[`<pkg>-fetch`](action-pkg-fetch) action along with the
[`-F, --force`](arg-force) argument. For example, even if `libfoo-1.0.tgz`
was already downloaded locally, a request as follows will delete the local
cache file and re-download it from the configured site:

```
releng-tool libfoo-fetch --force
```

## Automatically re-fetch development branches

When operating in [development mode](/guides/development-mode) where a
package has a development-specific source based off a branch, it may be
preferred to always ensure the most recent sources are fetched. For
example, consider `libfoo` with a development revision `main`:

```python
LIBFOO_SITE = 'git+git@example.com:base/libfoo.git'
LIBFOO_REVISION = 'v1.0'
LIBFOO_DEVMODE_REVISION = 'main'
```

With the above configuration, if a builder cleans and rebuilds the project,
the originally cache of `main` would still be used, even if `main` has new
updates on the remote branch:

```shell-session
$ releng-tool
...
~using libfoo hash 1b100c825307730e2027398d70af7c84ce173238~
...
$ releng-tool clean
$ releng-tool
...
~still using libfoo hash 1b100c825307730e2027398d70af7c84ce173238~
...
```

If a user wants to automatically re-fetch new updates on a development
branch, they can take advantage of the
[`LIBFOO_DEVMODE_IGNORE_CACHE`](pkg-opt-devmode-ignore-cache) option. For
example, if a site definition had:

```python
LIBFOO_SITE = 'git+git@example.com:base/libfoo.git'
LIBFOO_REVISION = 'v1.0'
LIBFOO_DEVMODE_REVISION = 'main'
LIBFOO_DEVMODE_IGNORE_CACHE = True
```

A repeat of the rebuild actions will result in an automatic update of the
package's `main` branch (if updates are available):

```shell-session
$ releng-tool
...
~using libfoo hash 1b100c825307730e2027398d70af7c84ce173238~
...
$ releng-tool clean
$ releng-tool
...
~using libfoo hash 4cd6375c7464b6bdf166b4f27d5e2fbd937e4ad0~
...
```
