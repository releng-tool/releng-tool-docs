# Local-sources mode

:::{note}
Clean events (such as `releng-tool clean`) will not touch packages using
sources found alongside the output directory
:::

Local-sources mode provides a way for a developer to build internal-flagged
packages using sources found alongside the root directory (or a specific
provided directory), instead of having releng-tool attempt to fetch them
from remote instances. This is primarily for developers who desire to
manually manage source content outside the releng-tool environment.
Local-sources mode only works for internally flagged packaged. Consider
the following example: a releng-tool project has a package called
`liba`. When releng-tool is invoked in normal configurations, the
package will do fetching, extraction and patching to prepare the directory
`<root>/output/build/liba-<version>`. However, if a builder has
configured the working root for local-sources mode, sources for `liba`
will be used from the folder `<root>/../liba` instead:

```
├── liba/
│   └── ...
└── my-releng-tool-project/
    ├── package/
    │   └── liba/
    │       └── ...
    ├── LICENSE
    ├── README.md
    └── releng-tool.rt
```

When in local-sources mode, an internal package will skip the fetching,
extraction and patching stages in order to prevent undesired manipulation
of developer-prepared sources. Another consideration to note is the use
of clean operators while in local-sources mode. Continuing with the above
example, if a user invokes `releng-tool liba-clean`, the operation will
not remove the `<root>/../liba` folder. Responsibility to managing a
clean `liba` package will be left with the user.

To enable local-sources mode, invoking `releng-tool` with the
`--local-sources` (or `-L`) argument will enable the mode. Future calls to
releng-tool for the project will use local sources for packages defined as
internal packages. For example:

```shell-session
$ releng-tool --local-sources
(*) <parent>
(success) configured root for local-sources mode
$ releng-tool
~building against local sources~
...
```

Local-sources mode is persisted through the use of a file flag in the root
directory.

If a user provides a directory for the `--local-sources` argument, packages
will be looked for in the provided folder instead of the parent of the
configured root directory. For example:

```shell-session
$ releng-tool --local-sources ~/workdir2
(*) ~/workdir2
(success) configured root for local-sources mode
$ releng-tool
~building against local sources~
...
```

In the above example, if a project had an internal package `liba`,
sources for `liba` will be used from the folder `~/workdir2/liba`:

```
├── workdir/
│   └── my-releng-tool-project/
│       ├── package/
│       │   └── liba/
│       │       └── ...
│       ├── LICENSE
│       ├── README.md
│       └── releng-tool.rt
└── workdir2/
    └── liba/
        └── ...
```

Users can also provide package-specific overrides. If a user provides a
path which is prefixed with a package's name with either a colon (`:`) or
at sign (`@`), the sources for the provided package will be used from
the respective folder:

```shell-session
$ releng-tool -L ~/workdir2
$ releng-tool -L libb:/mnt/sources/libb
$ releng-tool -L libc:
(*) ~/workdir2
(libb) /mnt/sources/libb
(libc) <unset>
(success) configured root for local-sources mode
$ releng-tool
~building against local sources~
...
```

In the above example, if a project had internal packages `liba`,
`libb` and `libc`, the following paths will be used:

```
/
├── home/
│   └── <user>/
│       ├── workdir/
│       │   └── my-releng-tool-project/
│       │       ├── package/
│       │       │   ├── liba/
│       │       │   │   └── ...
│       │       │   ├── libb/
│       │       │   │   └── ...
│       │       │   └── libc/
│       │       │       └── ...
│       │       ├── LICENSE
│       │       ├── README.md
│       │       └── releng-tool.rt
│       └── workdir2/
│           └── liba/
│               └── ...
└── mnt/
    ├── sources/
    │   └── libb/
    │       └── ...
    ...
```

- Sources for `liba` will be used from the folder `~/workdir2/liba`,
- Sources for `libb` will be used from the folder `/mnt/sources/libb`; and,
- Sources for `libc` will not be fetched locally.

A user can either disable local sources mode by:

- Providing a local-source path of `-` or `unset`;
- Invoking [`mrproper`](action-mrproper); or,
- By manually removing the file flag found at the root of the project.
