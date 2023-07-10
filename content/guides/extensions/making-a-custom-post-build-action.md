# Making a custom post-build action extension

This is an extension example for the following use case:

> After performing a build for any of my releng-tool projects, I want to
> automatically add a series of files into the output directory before we
> attempt to package the contents. I want to do this using an extension to
> avoid the need to repeat the process across all my releng-tool projects.

## Prelude

:::{include} _tutorial-prelude.md
:::

## Creating the post-build action extension

A first step is to setup the initial file structure for the extension. Assuming
there exists a checked out releng-tool project (`my-releng-tool-project`) to
be tested against, create a new extension folder named `my-awesome-extension`
alongside the releng-tool project(s):

```
├── my-awesome-extension/
│   ├── my_awesome_extension/
│   │   ├── assets/
│   │   │   └── NOTICE.pdf
│   │   └── __init__.py
│   ├── LICENSE
│   ├── README.md
│   ...
└── my-releng-tool-project/
```

Inside this folder, create any base documents desired, a sample PDF, as well
as preparing a `my_awesome_extension` Python package folder to hold the
extension implementation. For the `__init__.py` file, add the following
contents:

```python
import os
import shutil

def releng_setup(app):
    app.connect('post-build-finished', my_awesome_postbuild_handler)

def my_awesome_postbuild_handler(env):
    print('post-build triggered!')
```

The above adds a function `releng_setup`, which releng-tool uses to register
the extension into the releng-tool engine. The function is invoked during
initialization by passing an application context (`app`) which the extension
can use to hook onto events and more. This extension implements a function
`my_awesome_postbuild_handler`, which is registered on the `post-build-finished`
event. This allows the handler to be triggered when a post-build stage has
completed for a project.

To test that the post-build event is triggered, use an existing releng-tool
project and register this new example extension into the releng-tool process:

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

When running releng-tool, the following message should be printed at the end of
a run:

```shell-session
$ releng-tool
...
post-build triggered!
(success) completed (0:00:00)
```

Next, we can now adjust our handler to help modify the output directory
when the event is triggered. In this example, we want to copy an
extension-managed `NOTICE.pdf` file and place it into the output directory.
Update the extension with the following:

```python
def my_awesome_postbuild_handler(env):
    # find the NOTICE PDF document
    ext_dir = os.path.dirname(os.path.realpath(__file__))
    assets_dir = os.path.join(ext_dir, 'assets')
    notice_pdf = os.path.join(assets_dir, 'NOTICE.pdf')

    # copy this file into the target directory
    target = os.path.join(env['TARGET_DIR'], 'NOTICE.pdf')
    shutil.copyfile(notice_pdf, target)
```

With this change, a re-run of the releng-tool project should have the
`NOTICE.pdf` document copied into the target directory for the project.

:::{include} _tutorial-footer.md
:::
