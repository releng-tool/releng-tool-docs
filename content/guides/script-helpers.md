# Script helpers

releng-tool provides a series of helper functions which can be used in
script-based packages, post-processing and more. Helper functions provided
are listed below:

## Available functions

```{eval-rst}
.. currentmodule:: releng_tool
.. autofunction:: debug
.. autofunction:: err
.. autofunction:: hint
.. autofunction:: log
.. autofunction:: note
.. autofunction:: releng_cat
.. autofunction:: releng_copy
.. autofunction:: releng_copy_into
.. autofunction:: releng_env
.. autofunction:: releng_execute
.. autofunction:: releng_execute_rv
.. autofunction:: releng_exists
.. autofunction:: releng_exit
.. autofunction:: releng_expand
.. autofunction:: releng_include

.. method:: releng_join(path: str | bytes | PathLike, *paths: str | bytes | PathLike)

    An alias for ``os.path.join``. See also
    https://docs.python.org/library/os.path.html#os.path.join.

.. autofunction:: releng_ls
.. autofunction:: releng_mkdir
.. autofunction:: releng_move
.. autofunction:: releng_move_into

.. method:: releng_path(*pathsegments)

    .. versionadded:: 2.3

    An alias for ``pathlib.Path``. See also
    https://docs.python.org/3/library/pathlib.html#pathlib.Path.

.. autofunction:: releng_remove
.. autofunction:: releng_symlink
.. autofunction:: releng_require_version
.. autofunction:: releng_tmpdir
.. autofunction:: releng_touch
.. autofunction:: releng_wd
.. autofunction:: success
.. autofunction:: verbose
.. autofunction:: warn
```

## Available variables

The following variables are registered in the global context for any
project or package definition/script.

(vars-releng_args)=
### `releng_args`

:::{versionchanged} 2.5
Variable no longer populated when [`action-pkg-exec`](action-pkg-exec) is set.
:::

```{note}
When using [`<pkg>-exec "<cmd>"`](action-pkg-exec), the `releng_args` variable
will not be populated. This is to prevent conflicts from project-specific
argument processing and package-specific run arguments.
```

A list of arguments forwarded into a releng-tool invoke. If a caller uses
the `--` argument, all trailing arguments will be populated into
"forwarded argument" list. A project may use these arguments for their own
tailoring.

A user can use Python's [`argparse`][argparse] module to manage custom
arguments. For example, if trying to add a new flag `--custom` to a build,
the following can be added into a project's `releng-tool.rt` definition:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--custom', action='store_true')
args = parser.parse_args(args=releng_args)
print(args.custom)
```

The flag can be enabled by invoking releng-tool using:

```
releng-tool -- --custom
```

### `releng_version`

The version of releng-tool.

```python
print(f'Using version {releng_version}')
```

## Importing helpers

Scripts directly invoked by releng-tool will automatically have these helpers
registered in the script's globals module (i.e. no import is necessary). If a
project defines custom Python modules in their project and wishes to take
advantage of these helper functions, the following import can be used to, for
example, import a specific function:

```python
from releng_tool import releng_execute
```

Or, if desired, all helper methods can be imported at once:

```python
from releng_tool import *
```


[argparse]: https://docs.python.org/3/library/argparse.html
