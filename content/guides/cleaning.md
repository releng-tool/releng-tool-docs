# Cleaning

```{tip}
If using package-specific cleaning actions, users are recommended to see
[Understanding rebuilds](/getting-started/rebuilds).
```

A user can invoke various cleaning actions to help start fresh. There are
multiple cleaning approaches that can be performed to help start from a
pristine state or avoid unnecessary fetches/rebuilds.

The following cleaning-related actions are supported:

- [`<pkg>-clean`](action-pkg-clean)
- [`<pkg>-distclean`](action-pkg-distclean)
- [`clean`](action-clean)
- [`mrproper`](action-mrproper)
- [`distclean`](action-distclean)

The list is order of how much cleaning is performed.

Cleaning operations will remove files based off the configured root and output
directory. If an output directory is provided (i.e. `--out-dir <dir>`)
during a clean event, select folders inside this directory will be removed
instead of the output directory (if any) found in the root directory.

```{raw} latex
\newpage
```

Consider the following output content and which paths are applicable for
a given cleaning mode:

```none
                                    [clean]  [mrproper]  [distclean]
(example file tree)
└── my-releng-tool-project/            ☐         ☐           ☐
    ├── cache/                         ☐         ☐           ☒
    │   ├── .cargo/                    ☐         ☐           ☒
    │   │   └── ...                    ☐         ☐           ☒
    │   ├── .cargo-vendor/             ☐         ☐           ☒
    │   │   └── ...                    ☐         ☐           ☒
    │   ├── libfoo/                    ☐         ☐           ☒
    │   │   ├── index                  ☐         ☐           ☒
    │   │   └── ...                    ☐         ☐           ☒
    │   ├── .dvcsdb                    ☐         ☐           ☒
    │   └── ...                        ☐         ☐           ☒
    ├── dl/                            ☐         ☐           ☒
    │   ├── libbar/                    ☐         ☐           ☒
    │   │   └── libbar-1.2.3.tgz       ☐         ☐           ☒
    │   └── ...                        ☐         ☐           ☒
    ├── output/                        ☐         ☒           ☒
    │   ├── build/                     ☒         ☒           ☒
    │   │   ├── libfoo                 ☒         ☒           ☒
    │   │   │   └── ...                ☒         ☒           ☒
    │   │   ├── libbar                 ☒         ☒           ☒
    │   │   │   └── ...                ☒         ☒           ☒
    │   │   └── ...                    ☒         ☒           ☒
    │   ├── host/                      ☒         ☒           ☒
    │   │   └── ...                    ☒         ☒           ☒
    │   ├── images/                    ☐         ☒           ☒
    │   │   └── ...                    ☐         ☒           ☒
    │   ├── licenses/                  ☒         ☒           ☒
    │   │   └── ...                    ☒         ☒           ☒
    │   ├── misc/                      ☐         ☒           ☒
    │   │   └── ...                    ☐         ☒           ☒
    │   ├── staging/                   ☒         ☒           ☒
    │   │   └── ...                    ☒         ☒           ☒
    │   ├── symbols/                   ☒         ☒           ☒
    │   │   └── ...                    ☒         ☒           ☒
    │   ├── target/                    ☒         ☒           ☒
    │   │   └── ...                    ☒         ☒           ☒
    │   ├── sbom.txt                   ☐         ☒           ☒
    │   └── ...                        ☐         ☒           ☒
    ├── package/                       ☐         ☐           ☐
    │   └── ...                        ☐         ☐           ☐
    ├── .releng-flag-devmode           ☐         ☒           ☒
    ├── releng-tool.rt                 ☐         ☐           ☐
    ...                                ☐         ☐           ☐
```

```{raw} latex
\newpage
```
