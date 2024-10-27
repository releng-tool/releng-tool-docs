# Script helpers

releng-tool provides a series of helper functions which can be used in
script-based packages, post-processing and more. Helper functions provided
are listed below:

## Available functions

```{eval-rst}

.. _script-debug:

.. automodule:: releng_tool
    :members: debug
    :noindex:

.. _script-err:

.. automodule:: releng_tool
    :members: err
    :noindex:

.. _script-hint:

.. automodule:: releng_tool
    :members: hint
    :noindex:

.. _script-log:

.. automodule:: releng_tool
    :members: log
    :noindex:

.. _script-note:

.. automodule:: releng_tool
    :members: note
    :noindex:

.. _script-releng_cat:

.. automodule:: releng_tool
    :members: releng_cat
    :noindex:

.. _script-releng_copy:

.. automodule:: releng_tool
    :members: releng_copy
    :noindex:

.. _script-releng_copy_into:

.. automodule:: releng_tool
    :members: releng_copy_into
    :noindex:

.. _script-releng_env:

.. automodule:: releng_tool
    :members: releng_env
    :noindex:

.. _script-releng_execute:

.. automodule:: releng_tool
    :members: releng_execute
    :noindex:

.. _script-releng_execute_rv:

.. automodule:: releng_tool
    :members: releng_execute_rv
    :noindex:

.. _script-releng_exists:

.. automodule:: releng_tool
    :members: releng_exists
    :noindex:

.. _script-releng_exit:

.. automodule:: releng_tool
    :members: releng_exit
    :noindex:

.. _script-releng_expand:

.. automodule:: releng_tool
    :members: releng_expand
    :noindex:

.. _script-releng_include:

.. automodule:: releng_tool
    :members: releng_include
    :noindex:

.. _script-releng_tool:

.. automodule:: releng_tool
    :noindex:

    .. method:: releng_join(path, *paths)
        :noindex:

        An alias for ``os.path.join``. See also
        https://docs.python.org/library/os.path.html#os.path.join.

.. _script-releng_ls:

.. automodule:: releng_tool
    :members: releng_ls
    :noindex:

.. _script-releng_mkdir:

.. automodule:: releng_tool
    :members: releng_mkdir
    :noindex:

.. _script-releng_move:

.. automodule:: releng_tool
    :members: releng_move
    :noindex:

.. _script-releng_move_into:

.. automodule:: releng_tool
    :members: releng_move_into
    :noindex:

.. _script-releng_remove:

.. automodule:: releng_tool
    :members: releng_remove
    :noindex:

.. _script-releng_symlink:

.. automodule:: releng_tool
    :members: releng_symlink
    :noindex:

.. _script-releng_require_version:

.. automodule:: releng_tool
    :members: releng_require_version
    :noindex:

.. _script-releng_tmpdir:

.. automodule:: releng_tool
    :members: releng_tmpdir
    :noindex:

.. _script-releng_touch:

.. automodule:: releng_tool
    :members: releng_touch
    :noindex:

.. _script-releng_wd:

.. automodule:: releng_tool
    :members: releng_wd
    :noindex:

.. _script-success:

.. automodule:: releng_tool
    :members: success
    :noindex:

.. _script-verbose:

.. automodule:: releng_tool
    :members: verbose
    :noindex:

.. _script-warn:

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
