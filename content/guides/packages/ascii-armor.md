# ASCII armor

```{note}
An alternative to using an ASCII-armor to validate a package's cache is to
use [hashes](hash-file) instead.
```

When downloading assets from a remote instance, an ASCII-armor file can be
used to help verify the integrity of any fetched content. For example, if
a package lists a site with a `my-archive.tgz` to download, the fetch
process will download the archive and verify its contents with an associated
ASCII-armor file (if one is provided). If the integrity of the file cannot
be verified, the build process stops indicating an unexpected asset was
downloaded.

To include an ASCII-armor file for a package, add a `<my-package>.asc`
file inside the package's directory. For example, for a `libfoo` package,
the following would be expected:

```
└── my-releng-tool-project/
    ├── package/
    │   └── libfoo/
    │       └── libfoo
    │       └── libfoo.asc            <----
    ...
```

Verification is performed using the host system's `gpg`. For
verification's to succeed, the system must already have the required
public keys registered.
