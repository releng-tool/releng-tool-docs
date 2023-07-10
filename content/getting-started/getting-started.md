# Getting started

This documentation will outline what releng-tool is, how it can be used
to create projects with various package definitions, with the end goal
of creating release artifacts for a project.

releng-tool is made on Python. Package configurations, scripts, etc. are
Python-compatible scripts, which releng-tool accepts for processing
configuration files and invoking other tools on a host system. While
releng-tool supports running on various host systems (e.g. Linux, OS X,
Windows, etc.), this guide will primarily show examples following a
Unix-styled file system.

## Running releng-tool

Depending on the host and how releng-tool has been [installed](/install),
this tool can be either executed using the call `releng-tool` (if supported) or
explicitly through a Python invoke `python -m releng-tool`. This guide will
assume the former option is available for use. If the alias command is not
available on the host system, the latter call can be used instead. For example,
the two commands shown below can be considered equivalent:

```text
releng-tool --version
 (or)
python -m releng-tool --version
```

## Overview

A project will typically be defined by a `releng` configuration file along
with one or more packages found inside a `package/` folder. This location
can be referred to as the "root directory".

:::{note}
releng-tool supports extensionless configuration/script files (e.g. `releng`),
as well as configuration/scripts using a `.py` or `.releng` extension. For
more information, please see
[alternative extensions](/guides/tips/alternative-extensions).
:::

When invoking `releng-tool`, the tool will look in the current working
directory for project information to process. For example, if a folder
`my-project` had a skeleton such as:

```
└── my-project/
    ├── package/
    │   └── package-a/
    │       └── ...
    └── releng
```

The following output may be observed when running releng-tool:

```shell-session
$ cd my-project
$ releng-tool
extracting package-a...
patching package-a...
configuring package-a...
building package-a...
installing package-a...
generating license information...
(success) completed (0:01:30)
```

On a successful execution, it is most likely that the releng-tool process
will have an asset (or multiple) generated into a `images/` location. It is
up to the developer of a releng-tool project to decide where generated
files will be stored.

If a user wishes to pass the directory of a project location via command line,
the argument `--root-dir` can be used:

```shell
releng-tool --root-dir my-project/
```

For a complete list of actions and other argument options provided by the tool,
the `--help` option can be used to show this information:

```shell
releng-tool --help
```

## Topics

:::{toctree}
:maxdepth: 1

prelude
tutorials
rebuilds
fetching
:::
