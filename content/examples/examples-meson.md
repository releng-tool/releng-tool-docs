# Meson package examples

An example [Meson package](/guides/packages/pkg-type-meson) definition:

__package/scantool/scantool.rt__

```python
SCANTOOL_LICENSE = 'OSL-2.1'
SCANTOOL_LICENSE_FILES = 'COPYING'
SCANTOOL_MESON_BUILD_TYPE = 'release'
SCANTOOL_REVISION = 'v3.1'
SCANTOOL_SITE = 'hg+https://example.com/scantool'
SCANTOOL_TYPE = 'meson'

SCANTOOL_ENV = {
    'SCANTOOL_OPT_MODE': 'final',
}
```
