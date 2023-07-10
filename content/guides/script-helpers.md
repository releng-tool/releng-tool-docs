# Script helpers

releng-tool provides a series of helper functions which can be used in
script-based packages, post-processing and more. Helper functions provided
are listed below:

## Available functions

```{eval-rst}

.. automodule:: releng_tool
    :members: debug
    :noindex:

.. automodule:: releng_tool
    :members: err
    :noindex:

.. automodule:: releng_tool
    :members: hint
    :noindex:

.. automodule:: releng_tool
    :members: log
    :noindex:

.. automodule:: releng_tool
    :members: note
    :noindex:

.. automodule:: releng_tool
    :members: releng_cat
    :noindex:

.. automodule:: releng_tool
    :members: releng_copy
    :noindex:

.. automodule:: releng_tool
    :members: releng_copy_into
    :noindex:

.. automodule:: releng_tool
    :members: releng_env
    :noindex:

.. automodule:: releng_tool
    :members: releng_execute
    :noindex:

.. automodule:: releng_tool
    :members: releng_execute_rv
    :noindex:

.. automodule:: releng_tool
    :members: releng_exists
    :noindex:

.. automodule:: releng_tool
    :members: releng_exit
    :noindex:

.. automodule:: releng_tool
    :members: releng_expand
    :noindex:

.. automodule:: releng_tool
    :members: releng_include
    :noindex:

.. automodule:: releng_tool
    :noindex:

    .. method:: releng_join(path, *paths)
        :noindex:

        An alias for ``os.path.join``. See also
        https://docs.python.org/library/os.path.html#os.path.join.

.. automodule:: releng_tool
    :members: releng_ls
    :noindex:

.. automodule:: releng_tool
    :members: releng_mkdir
    :noindex:

.. automodule:: releng_tool
    :members: releng_move
    :noindex:

.. automodule:: releng_tool
    :members: releng_move_into
    :noindex:

.. automodule:: releng_tool
    :members: releng_remove
    :noindex:

.. automodule:: releng_tool
    :members: releng_require_version
    :noindex:

.. automodule:: releng_tool
    :members: releng_tmpdir
    :noindex:

.. automodule:: releng_tool
    :members: releng_touch
    :noindex:

.. automodule:: releng_tool
    :members: releng_wd
    :noindex:

.. automodule:: releng_tool
    :members: success
    :noindex:

.. automodule:: releng_tool
    :members: verbose
    :noindex:

.. automodule:: releng_tool
    :members: warn
    :noindex:
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
