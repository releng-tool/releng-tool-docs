# MAINTAINERS

This document serves as a guide for maintainers. For users wishes to contribute
to this repository, please see [CONTRIBUTING.md](CONTRIBUTING.md).

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
