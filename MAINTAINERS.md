# MAINTAINERS

This document serves as a guide for maintainers. For users wishes to contribute
to this repository, please see [CONTRIBUTING.md](CONTRIBUTING.md).

## Local Builds and Checks

To locally build documentation:

```
cd content
./build
```

To easily open documentation in a browser, invoke:

```
./open
```

To spellcheck the documentation, invoke:

```
./build spelling
```

## Synchronization

When attempting to update the persisted state of this repository, first
move into the `locale` folder:

```shell-session
cd locale
```

Update the locale messages:

```shell-session
./update
```

Synchronize messages with transifex:

```shell-session
./sync
```

Commit any made to the working tree.

## Release commands

Prepare a release tag on the news event commit:

```shell-session
git tag -s -a v<version> <hash> -m "releng-tool <version> news"
git verify-tag <tag>
```

Push up the release tag:

```shell-session
git push origin <tag>
```

Wait and verify the published documentation.

In the event additional changes/tweaks are needed after a main version release,
perform the same steps above but append a `-N` suffix on the tag. Always start
with `-2` and higher. For example, if originally using a `v3.0` tag, now use a
`v3.0-2` tag.
