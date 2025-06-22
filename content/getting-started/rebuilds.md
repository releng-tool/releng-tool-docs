# Understanding rebuilds

- Completed stages for a package are not executed again when releng-tool is
  re-run.
- Users looking to re-run a completed stage for a specific package need to
  manually re-trigger the stage (e.g.
  [`releng-tool <pkg>-rebuild`](action-pkg-rebuild),
  [`releng-tool <pkg>-reconfigure`](action-pkg-reconfigure),
  [`releng-tool <pkg>-reinstall`](action-pkg-reinstall)).
- Users can also invoke [`releng-tool punch`](action-punch) for force
  re-trigger all package stages.

## Details

As packages are processed in order (based off of detected dependencies, if any),
each package will go through their respective stages:

1. Fetching
1. Extraction
1. Patching
1. Configuration
1. Building
1. Installation

While a package may not take advantage of each stage, the releng-tool will
step through each stage to track its progress. Due to the vast number of
ways a package can be defined, the ability for releng-tool to determine
when a previously executed stage is "stale" is non-trivial. Instead of
attempting to manage "stale" package stages, releng-tool leaves the
responsibility to the builder to deal with these scenarios. This idea is
important for developers to understand how it is possible to perform
rebuilds of packages to avoid a full rebuild of the entire project.

Consider the following example: a project has three packages which are
C++-based packages:

```
└── my-releng-tool-project/
    ├── package/
    │   ├── module-a/
    │   │   └── ...
    │   ├── module-b/
    │   │   └── ...
    │   └── module-c/
    │       └── ...
    └── releng-tool.rt
```

For this example, project `module-b` depends on `module-a` and project
`module-c` depends on `module-b`. Therefore, releng-tool will process
packages in the order `module-a -> module-b -> module-c`. In this example,
the project is built until a failure is detected in package `module-c`:

```shell-session
$ releng-tool
[module-a built]
[module-b built]
ERROR: unable to build module-c
```

A developer notices that it is due to an issue found in `module-b`; however,
instead of attempting to redo everything from a fresh start, the developer
wishes to test the process by manually making local changes in `module-b` to
complete the build process. The developer makes the change, re-invokes
`releng-tool` but still notices the build error occurs:

```shell-session
$ releng-tool
ERROR: unable to build module-c
```

The issue here is that since `module-b` has already been processed, none of
the interim changes made will be available for `module-c` to use. To take
advantage of the new implementation in `module-b`, the builder can signal for
the updated package to be rebuilt:

```shell-session
$ releng-tool module-b-rebuild
[module-b rebuilt]
```

With `module-b` in a more desired state, a re-invoke of `releng-tool` can
allow `module-c` to be built.

```shell-session
$ releng-tool
[module-c built]
```

This is a very simple example to consider, and attempts to rebuild can vary
based on the packages, changes made and languages used.
