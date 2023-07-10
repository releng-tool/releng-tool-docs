# VCS Ignore

When invoking releng-tool on a project, the project's root directory will be
populated with cached assets and other output files. A series of standard
ignore patterns can be applied to a repository to prevent observing these
generated files using VCS tools. The following is an example ignore
configuration which can be applied for Git-based repositories (via
`.gitignore`):

```
# releng-tool
/cache/
/dl/
/output/
.releng-flag-*
```
