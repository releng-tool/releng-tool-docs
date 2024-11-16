(quirk-releng.disable_prerequisites_check)=
# Quirk `releng.disable_prerequisites_check`

A releng-tool project may require various dependencies. For example, if
a package define a Git-based site for sources, the `git` client will be
required to clone these sources into a build directory. To help inform users
of issues in the early stage of a build, releng-tool will perform a
prerequisites check for certain dependencies. If a prerequisite cannot be
found, the build process stops immediately.

In select scenarios, the prerequisite check may wish to be skipped. For
example, if the running environment is not expected to perform a specific
action in a project that requires an application. To avoid triggering a
run error at start, users may set the `releng.disable_prerequisites_check`
quirk to skip any prerequisite check:

```
releng-tool --quirk releng.disable_prerequisites_check
```

## See also

- [](quirks)
