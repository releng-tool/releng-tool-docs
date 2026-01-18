# Cargo package examples

An example [Cargo package](/guides/packages/pkg-type-cargo) definition:

__package/libfoo/libfoo.rt__

```python
LIBFOO_LICENSE = ['BSD-2-Clause']
LIBFOO_LICENSE_FILES = ['LICENSE']
LIBFOO_SITE = 'git+git@example.com:base/libfoo.git'
LIBFOO_TYPE = 'cargo'

LIBFOO__CUSTOM_FEATURES = [
    # tailor specific features
    '--no-default-features',
    '--features', 'feature-a,feature-b',
]

LIBFOO_BUILD_OPTS = [
    *LIBFOO__CUSTOM_FEATURES,
]

LIBFOO_INSTALL_OPTS = [
    *LIBFOO__CUSTOM_FEATURES,
]
```
