# Post-processing

```{warning}
A post-processing script (if used) will be invoked each time `releng-tool`
reaches the final stage of a build.
```

```{admonition} Prospect
At this time, releng-tool supports only post-build scripts. It is planned to
introduced support for some image-related helpers (i.e. package helpers).
This may introduce a reserved `releng-tool-post-image.rt` script in
future releases.
```

After each package has been processed, a project has the ability to perform
post-processing. Post-processing allows a developer to cleanup the target
directory, build an archive/package from generated results and more. If a
project contains a `releng-tool-post-build.rt` inside the root directory,
the post-processing script will be invoked in the final stage of a build.

A developer may start out with the following post-processing script
`<root>/releng-tool-post-build.rt`:

```
└── my-releng-tool-project/
    ├── package/
    │   └── ...
    ├── releng-tool.rt
    └── releng-tool-post-build.rt     <----
```

With the contents:

```python
print('post processing...')
```

The above script will output the newly inserted print message at the end
of a build process:

```shell-session
$ releng-tool
...
generating license information...
post processing...
(success) completed (0:01:30)
```

A developer can take advantage of [environment variables](environment) and
[script helpers](script-helpers) for additional support.

It is important to note that post-processing scripts will be invoked each
time a `releng-tool` invoke reaches the final stage of a build. A developer
should attempt to implement the post-processing scripts in a way that it can
be invoked multiple times. For example, if a developer decides to move a
file out of the target directory into an interim directory when building
an archive, it is most likely that a subsequent request to build may fail
since the file can no longer be found inside the target directory.
