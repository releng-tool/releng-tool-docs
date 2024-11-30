# Licenses

A releng-tool project can defined multiple packages, each with the
possibility of having multiple licenses associated with them. Each project
may vary: some may have only proprietary sources and may not care about
tracking this information, some may only use open source software and
require to populate license information for a final package, or a mix.

When license information is populated for a project, each project's license
information ([`LIBFOO_LICENSE_FILES`](pkg-opt-license-files)) is will be
populated into a single license document. If a developer defines the
[`license_header`](conf-license-header) configuration, the generated
document will be prefixed with the header content. For example, developers
can create a new license header file `assets/license-header.tpl` in the
project folder:

```
└── my-releng-tool-project/
    ├── assets/
    │   └── license-header.tpl        <----
    ├── package/
    │   └── ...
    └── releng-tool.rt
```

Which then `releng-tool.rt` can be configured to use the header contents:

```python
import os

... (other configuration options)

root_dir = os.path.dirname(os.path.realpath(__file__))
license_header_file = os.path.join(root_dir, 'assets', 'license-header.tpl')

with open(license_header_file) as f:
   license_header = ''.join(f.readlines())
```

Licenses for a project are generated before the
[post-processing](post-processing) phase. This allows a developer to use
generated license document(s) when preparing final archives/packages.

See also [license generation](tips/license-generation).
