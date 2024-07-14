(quirk-releng.git.no_quick_fetch)=
# Quirk `releng.git.no_quick_fetch`

When fetching sources for a Git-site-defined package, releng-tool will
attempt to acquire these sources by only pulling applicable revision
references needed for a build (i.e. "quick fetching", in the context of
releng-tool). For example, if a project defines a Git tag to fetch, only
the `refs/tags/<tag>` reference will be fetched.

If a user does not want to utilizing quick-fetching for Git packages, this
can be disabled by using the `releng.git.no_quick_fetch` quirk.

```
releng-tool --quirk releng.git.no_quick_fetch
```

## See also

- [](quirks)
