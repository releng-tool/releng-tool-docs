(quirk-releng.bzr.certifi)=
# Quirk `releng.bzr.certifi`

When a package is configured to fetch [bzr][bzr] sources, select environments
may have issues attempting to download from Launchpad (or other hosting) due
to legacy certificates.

> See `bzr help ssl.ca_certs` for how to specify trusted CAcertificates.\
> Pass -Ossl.cert_reqs=none to disable certificate verification entirely.

If a user's environment has [`certifi`][certifi] installed, a user can invoke
releng-tool with the quirk `releng.bzr.certifi` enabled to use certifi's
certificates instead. For example:

```
releng-tool --quirk releng.bzr.certifi
```

## See also

- [GNU Bazaar][bzr]
- [GNU Bazaar (The Wayback Machine)][bzr-wbm]
- [](quirks)


[bzr-wbm]: https://web.archive.org/web/http://bazaar.canonical.com/
[bzr]: https://en.wikipedia.org/wiki/GNU_Bazaar
[certifi]: https://pypi.org/project/certifi/
