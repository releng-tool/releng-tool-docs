# Parallel builds

A stage for a package (such as a build stage) can take advantage of multiple
cores to perform the step. By default, releng-tool will attempt to run as many
jobs for a stage equal to the amount of physical cores on the host system. The
amount of jobs available for a stage can be configured using the `--jobs`
argument. For example, if a user wishes to override the amount of jobs attempted
for stages to two jobs, the following can be used:

```shell
releng-tool --jobs 2
```

Note that a developer may restrict the amount of jobs allowed for a specific
package if a package cannot support parallel processing using the
[`LIBFOO_FIXED_JOBS`](pkg-opt-fixed-jobs) package option.
