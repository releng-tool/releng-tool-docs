# Making a custom package type extension

This is an extension example for the following use case:

> I'm using several packages in a project which use a custom package type
> (i.e. they are not a typical autotools or CMake project). I want to have
> an extension so that I can trigger custom prepare and build actions for
> project that is downloaded from version control.

## Prelude

:::{include} _tutorial-prelude.md
:::

This tutorial assumes the existence of an already prepared releng-tool
project, which had one or more packages planned to use a newly introduced
package type. The package type operates as follows:

- A repository will have a `prepare` script at its root, to be run before
  any builds are triggered.
- For builds, a `build` script exists at the root, which expects a type of
  build (e.g. `release` or `debug`) to be passed as an argument.
- There is no standard installation script/process to perform.

The example extension below will be designed to handle the above package type
requirements.

## Creating a custom package type extension

### Initial skeleton

A first step is to setup the initial file structure for the extension. Assuming
there exists a checked out releng-tool project (`my-releng-tool-project`) to
be tested against, create a new extension folder named `my-awesome-extension`
alongside the releng-tool project:

```
├── my-awesome-extension/
│   ├── my_awesome_extension/
│   │   ├── __init__.py
│   │   └── MyAwesomePackageType.py
│   ├── LICENSE
│   ├── README.md
│   ...
└── my-releng-tool-project/
```

Inside this folder, create any base documents desired as well as preparing a
`my_awesome_extension` Python package folder to hold the extension
implementation. For the `__init__.py` file, add the following contents:

```python
from my_awesome_extension import mapt

def releng_setup(app):
    app.add_package_type('ext-mapt', mapt.MyAwesomePackageType)
```

The above adds a function `releng_setup`, which releng-tool uses to register
the extension into the releng-tool engine. The function is invoked during
initialization by passing an application context (`app`) which the extension
can use to hook onto events and more.

This extension registers a new package type `ext-mapt`. When this new package
type is registered into releng-tool, the `MyAwesomePackageType` class
definition will be created/used to handle various stages of a package.

:::{note}
All extension package types must be prefixed with `ext-`.
:::

For `MyAwesomePackageType.py`, add the following contents:

```python
class MyAwesomePackageType:
    def configure(self, name, opts):
        print('TODO -- configure stage:', name)
        return True

    def build(self, name, opts):
        print('TODO -- build stage:', name)
        return True

    def install(self, name, opts):
        # do nothing for installation
        return True
```

The above package type provides a skeleton implementation for the pending
configuration and build stages for this new package type. The installation
stage is also required, but will only return `True` since it is not required
for this package type example.

### Initial testing

To test that the new package type is triggered at desired stages, use an
existing releng-tool project and register this new example extension into
the releng-tool process:

```python
import os
import sys

...

extensions = [
    'my_awesome_extension',
]

# add local extension path into system path
container_dir = os.path.dirname(ROOT_DIR)
ext_dir = os.path.join(container_dir, 'my-awesome-extension')
sys.path.append(ext_dir)
```

Next, we will create/update a package which will use this new type. For
example, for a `libfoo` package, we will configure the package type to
`ext-mapt` and track a custom extension option `mapt-build-type` with a
value of `release` (which we can later use to forward to our build script).

```python
LIBFOO_SITE = 'https://example.com/libfoo.git'
LIBFOO_TYPE = 'ext-mapt'

LIBFOO_EXTOPT = {
    'mapt-build-type': 'release',
}
```

When running releng-tool, the following messages should be printed during
a run:

```shell-session
$ releng-tool libfoo
patching libfoo...
configuring libfoo...
TODO -- configure stage: libfoo
building libfoo...
TODO -- build stage: libfoo
installing libfoo...
```

### Implement the configuration stage

With the extension being triggered at expected locations, we can now provide
implementation for these hooks to trigger the required `prepare` and `build`
scripts. The following steps will edit the existing
`MyAwesomePackageType.py` file.

First, add some utility calls for the upcoming implementation:

```python
from releng_tool import releng_execute
from releng_tool import releng_exists
from releng_tool import releng_exit
from releng_tool import releng_join
from releng_tool import verbose

# script shell to invoke
SHELL_BIN = 'sh'


class MyAwesomePackageType:
    ...
```

The above adds the following:

- `SHELL_BIN`: we define the shell executable to be invoked
- `releng_execute`: to be used to invoke our prepare/build scripts
- `releng_exists`: to help check if a package has expected scripts
- `releng_exit`: to help exit configure/build events on error
- `releng_join`: to help join paths for script targets
- `verbose`: some verbose message support to help development/error cases

Developers can use any supported Python packages/modules for this running
environment, and this example uses a series of helper functions provided
by releng-tool for convenience. Using releng-tool helper functions is not
required if implementations wish to use another approach for their
implementation.

We will implement the configuration event for our extension:

```python
class MyAwesomePackageType:
    def configure(self, name, opts):
        verbose('invoking a mapt prepare for package: {}', name)
        prepare_script = releng_join(opts.build_dir, 'prepare')
        if not releng_exists(prepare_script):
            releng_exit('project is missing "prepare" script')

        return releng_execute([SHELL_BIN, prepare_script])

    ...
```

The above will:

- Trigger a verbose message (if releng-tool is running with `--verbose`).
- Build the `prepare` script path expected in the project's build directory.
- Verify that the script exists. If not, stop the configuration event.
- Execute the prepare shell script.

### Implement the build stage

With the configuration stage completed, we will now implement the build
stage:

```python
class MyAwesomePackageType:
    ...

    def build(self, name, opts):
        verbose('invoking a mapt build for package: {}', name)
        build_script = releng_join(opts.build_dir, 'build')
        if not releng_exists(build_script):
            releng_exit('project is missing "build" script')

        build_type = opts.ext.get('mapt-build-type')
        if not build_type:
            releng_exit('project is missing "mapt-build-type" option')

        return releng_execute([SHELL_BIN, build_script, build_type])
```

The above will:

- Trigger a verbose message (if releng-tool is running with `--verbose`).
- Build the `build` script path expected in the project's build directory.
- Verify that the script exists. If not, stop the build event.
- Extract the expected `mapt-build-type` option from the package definition.
  If the option does not exist, the build event will be stopped.
- Execute the build shell script.

### Final testing

With the extension events implemented, re-run the releng-tool project from
the package's configuration stage to see expected output:

```shell-session
$ releng-tool libfoo-reconfigure
configuring libfoo...
building libfoo...
installing libfoo...
```

Based on the package's `prepare` and `build` script, inspect the console
output and build output to verify the respective scripts have performed
their tasks.

:::{include} _tutorial-footer.md
:::
