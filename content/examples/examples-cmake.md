# CMake package examples

An example [CMake package](/guides/packages/pkg-type-cmake) definition:

__package/libfoo/libfoo.rt__

```python
LIBFOO_NEEDS = [
    'libbar',
]

LIBFOO_LICENSE = ['Apache-2.0']
LIBFOO_LICENSE_FILES = ['LICENSE.txt']
LIBFOO_REVISION = 'sdk-1.2.170.0'
LIBFOO_SITE = 'https://git.example.com/example/example.git'
LIBFOO_TYPE = 'cmake'
LIBFOO_VERSION = '1.2.170'

LIBFOO_CONF_DEFS = {
    'BUILD_FEATURE_A': 'ON',
    'BUILD_SAMPLES': 'OFF',
    'LIBBAR_INSTALL_DIR': STAGING_DIR,
}
```
