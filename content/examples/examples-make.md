# Make package examples

An example [Make package](/guides/packages/pkg-type-make) definition:

__package/libfoo/libfoo.rt__

```python
LIBFOO_LICENSE = 'GPL-3.0-or-later'
LIBFOO_LICENSE_FILES = 'README'
LIBFOO_SITE = 'https://git.example.com/eng/support/libfoo.git'
LIBFOO_TYPE = 'make'
LIBFOO_VERSION = '0.23'

LIBFOO_INSTALL_OPTS = [
    'install-minimal',
]
```
