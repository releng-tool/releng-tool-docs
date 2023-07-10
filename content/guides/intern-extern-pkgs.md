# Internal/external packages

Packages are either internal packages or external packages. All packages are
considered external packages by default unless explicitly configured as
internal through either the package option [](pkg-opt-internal) or using
the project configuration [`default_internal`](conf-default-internal) (see
also [](pkg-opt-external)). Both package types are treated the same except
for the following:

- An internal package will not generate output warnings if the package is
  missing [hash information](packages/hash-file) or an
  [ASCII-armor](packages/ascii-armor).
- An internal package will not generate output warnings if the package is
  missing [licenses](licenses).
- When configured for [local-sources mode](local-sources-mode), only internal
  packages which have local sources configured will have their fetch,
  extract and patch stages skipped.
