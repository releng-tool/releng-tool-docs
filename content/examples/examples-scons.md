# SCons package examples

An example [SCons package](/guides/packages/pkg-type-scons) definition:

__package/exampleprj/exampleprj.rt__

```python
EXAMPLEPRJ_INTERNAL = True
EXAMPLEPRJ_SCONS_NOINSTALL = True
EXAMPLEPRJ_SITE = 'svn+https://svn.example.com/repos/exampleprj/c/branches/prj-3.4.5'
EXAMPLEPRJ_TYPE = 'scons'
```
