# Hash file

```{note}
An alternative to using a hash to validate a package's cache is to use an
[ASCII-armor](ascii-armor) instead. Although users can benefit from
using both validation methods, if desired.
```

When downloading assets from a remote instance, a package's hash file can be
used to help verify the integrity of any fetched content. For example, if a
package lists a site with a `my-archive.tgz` to download, the fetch process
will download the archive and verify its hash to a listed entry before
continuing. If a hash does not match, the build process stops indicating an
unexpected asset was downloaded.

It is recommended that:

- Any URL-based site asset have a hash entry defined for the asset (to ensure
  the package sources are not corrupted or have been unexpectedly replaced).
- A hash entry should exist for license files (additional sanity check if a
  package's license has change).

To create a hash file for a package, add a `<my-package>.hash` file
inside the package's directory. For example, for a `libfoo` package, the
following would be expected:

```
└── my-releng-tool-project/
    ├── package/
    │   └── libfoo/
    │       ├── libfoo.hash           <----
    │       └── libfoo.rt
    ...
```

The hash file should be a UTF-8 encoded file and can contain multiple hash
entries. A hash entry is a 3-tuple defining the type of hash algorithm
used, the hash value expected and the asset associated with the hash. A
tuple entry is defined on a single line with each entry separated by
whitespace characters. For example:

```text
# from project's release notes: https://example.com/release-notes
sha1 f606cb022b86086407ad735bf4ec83478dc0a2c5 my-archive.tgz
# locally computed
sha1 602effb4893c7504ffee8a8efcd265d86cd21609 LICENSE
```

Comments are permitted in the file. Lines leading with a `#` character or
inlined leading `#` character after a whitespace character will be ignored.

Supported hash types will vary on the Python interpreter [^hashlib] used.
Typically, this include FIPS secure hash algorithms (e.g. `sha1`,
`sha224`, `sha256`, `sha384` and `sha512`) as well as (but not
recommended) RSA'S MD5 algorithm. For hash algorithms requiring a key length,
a user can define a hash entry using the format `<hash-type>:<key-length>`.
For example, `shake_128:32`. Other algorithms may be used if provided by
the system's OpenSSL library.

Multiple hash entries can be provided for the same file if desired. This
is to assist in scenarios where a checked out asset's content changes based
on the system it is checked out on. For example, a text file checked out
from Git may use Windows line-ending on Windows system, and Unix-line
endings on other systems:

```text
sha1 602effb4893c7504ffee8a8efcd265d86cd21609 LICENSE
sha1 9e79b84ef32e911f8056d80a311cf281b2121469 LICENSE
```


[^hashlib]: <https://docs.python.org/library/hashlib.html>
