# Xmake package examples

An example [Xmake package](/guides/packages/pkg-type-xmake) definition:

__package/libfoo/libfoo.rt__

```python
LIBFOO_NEEDS = [
    'libbar',
]

LIBFOO_LICENSE = ['Apache-2.0']
LIBFOO_LICENSE_FILES = ['LICENSE.txt']
LIBFOO_REVISION = 'v4.5'
LIBFOO_SITE = 'https://git.example.org/example/example.git'
LIBFOO_TYPE = 'xmake'
LIBFOO_XMAKE_BUILD_TYPE = 'releasedbg'
```
