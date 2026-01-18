# Autotools package examples

An example [Autotools package](/guides/packages/pkg-type-autotools) definition:

__package/libfoo/libfoo.rt__

```python
LIBFOO_NEEDS = [
    'libbar',
]

LIBFOO_INSTALL_TYPE = 'staging'
LIBFOO_LICENSE = ['BSD-2-Clause']
LIBFOO_LICENSE_FILES = ['COPYING']
LIBFOO_SITE = 'https://www.example.com/download/libfoo-1.2.4.tar.xz'
LIBFOO_TYPE = 'autotools'
LIBFOO_VERSION = '1.2.4'

LIBFOO_CONF_ENV = {
    'PKG_CONFIG': 'pkg-config --static',
    'PKG_CONFIG_PATH': STAGING_DIR / '$PREFIX/lib/pkgconfig',
}

LIBFOO_CONF_OPTS = [
    # static only
    '--disable-shared',
    # features
    '--without-feature-a',
    '--without-feature-c',
    # disable extras and miscellaneous
    '--disable-docs',
]
```
