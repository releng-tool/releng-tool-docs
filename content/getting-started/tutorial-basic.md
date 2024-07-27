# Tutorial "Basic packages"

This tutorial shows an example using very simple script-based packages.
This example will make a project with two packages, setup a dependency
between them and setup scripts to help show a developer how packages are
processed.

To start, make a new folder for the project, folders for each package and
move into the root folder:

```shell-session
$ mkdir -p my-project/package/liba
$ mkdir -p my-project/package/program-b
$ cd my-project/
```

Inside the `liba` package, a package definition and script-based files will
be created. First, build the package definition `my-project/liba/liba.py` with
the following contents:

```python
LIBA_VERSION = '1.0.0'
```

Next, create a build script for the `liba` project
`my-project/liba/liba-build.py` with the following contents:

```python
print('invoked liba package build stage')
```

Repeat the same steps for the `program-b` package with the file
`my-project/program-b/program-b.py` containing:

```python
PROGRAM_B_NEEDS = ['liba']
PROGRAM_B_VERSION = '2.1.0'
```

And `my-project/program-b/program-b-build.py` containing:

```python
print('invoked program-b package build stage')
```

The second package is a bit different since it indicates that package
`program-b` has a dependency on `liba`. Configuring a dependency ensures
releng-tool will process the `liba` package before `program-b`.

With this minimal set of packages, the project's releng-tool configuration
can now be created. At the root of the project, create a `releng.py`
configuration file with the following contents:

```python
packages = [
    'program-b',
]
```

The `packages` key indicates a list of required packages to be processed.
In this example, we only need to list `program-b` since `liba` will be
implicitly loaded through the dependency configuration set in program B's
package definition.

The file structure should now be as follows:

```
└── my-project/
    ├── package/
    │   ├── liba/
    │   │   ├── liba.py
    │   │   └── liba-build.py
    │   └── program-b/
    │       ├── program-b.py
    │       └── program-b-build.py
    └── releng.py
```

This sample project should be ready for a spin. While in the `my-project`
folder, invoke `releng-tool`:

```shell-session
$ releng-tool
configuring liba...
building liba...
invoked liba package build stage
installing liba...
configuring program-b...
building program-b...
invoked program-b package build stage
installing program-b...
generating sbom information...
generating license information...
(success) completed (0:00:01)
```

This above output shows that the `liba` stages are invoke followed by
`program-b` stages. For the build stage in each package, each respective
package script has been invoked. While this example only prints a message,
more elaborate scripts can be made to handle a package's source to build.

To clean the project, a `releng-tool clean` request can be invoked:

```shell-session
$ releng-tool clean
```

After a `clean` request, the project should be ready to perform a fresh
build.

This concludes this tutorial.
