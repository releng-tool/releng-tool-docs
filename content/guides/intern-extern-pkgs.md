# Internal/external packages

Packages are either internal or external packages. All packages are
considered external by default unless explicitly configured as internal
through either a project configuration or a package option. Internal
or external packages are treated the same except for the following:

- An internal package will not generate output warnings if the package is
  missing [hash information](packages/hash-file) or an
  [ASCII-armor](packages/ascii-armor).
- An internal package will not generate output warnings if the package is
  missing [licenses](licenses).
- When configured for [local-sources mode](local-sources-mode), only internal
  packages which have local sources configured will have their fetch,
  extract and patch stages skipped.

An individual package can be configured as internal using
[`LIBFOO_INTERNAL`](pkg-opt-internal). For example:

```
LIBFOO_INTERNAL = True
```

Developers may want to instead use the project configuration
[`default_internal`](conf-default-internal) to configure all packages as
internal by default:

```
default_internal = True
```

See also [`LIBFOO_EXTERNAL`](pkg-opt-external).
