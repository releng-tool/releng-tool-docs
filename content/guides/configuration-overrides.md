# Configuration overrides

If a builder needs to (for example) override a tool location or package site, a
user can define either environment options or setup a configuration override
script `releng-overrides`:

```
└── my-releng-tool-project/
    ├── package/
    │   └── ...
    ├── LICENSE
    ├── README.md
    ├── releng-tool.rt
    ├── releng-overrides     <-- an override script
    ...
```

It is never recommended to persist a configuration overrides file into a
project's source repository. Overrides are intended for dealing with specific
hosts (e.g. injecting overrides when running with legacy build images).

## Extraction tool overrides

The `override_extract_tools` option inside a configuration override script
allows a dictionary to be provided to map an extension type to an external tool
to indicate which tool should be used for extraction. For example, when a
`.zip` archive is being processed for extraction, releng-tool will internally
extract the archive. However, a user may wish to override this tool with their
own extraction utility. Consider the following example:

```python
override_extract_tools = {
    'zip': '/opt/my-custom-unzip {file} {dir}',
}
```

The `{file}` key will be replaced with the file to be extracted, and the
`{dir}` key will be replaced where the contents should extract to.

## Revision overrides

The `override_revisions` option inside a configuration override script allows
a dictionary to be provided to map a package name to a new revision value.
Consider the following example: a project defines `module-a` and `module-b`
packages with package `module-b` depending on package `module-a`. A
developer may be attempting to tweak package `module-b` on the fly to test a
new capabilities against the current stable version of `module-a`. However,
the developer does not want to explicitly change the revision inside package
`module-b`'s definition. To avoid this, an override can be used instead:

```python
override_revisions = {
    'module-b': '<test-branch>',
}
```

The above example shows that package `module-b` will fetch using a test branch
instead of what is defined in the actual package definition.

## Site overrides

The `override_sites` option inside a configuration override script allows a
dictionary to be provided to map a package name to a new site value. There may
be times where a host may not have access to a specific package site. To have a
host to use a mirror location without having to adjust the package definition,
the site override option can be used. For example, consider a package pulls from
site `git@example.com:myproject.git`. However, the host `example.com` cannot
be access from the host machine. If a mirror location has been setup at
`git@example.org:myproject.git`, the following override can be used:

```python
override_sites = {
    '<package-name>': 'git@example.org:myproject.git',
}
```

## Tool overrides

Environment variables can be used to help override external tool invoked by the
releng-tool process. For example, when invoking CMake-based projects, the tool
`cmake` will be invoked. However, if a builder is running on CentOS and CMake
v3.x is desired, the tool `cmake3` needs to be invoked instead. To configure
this, an environment variable can be set to switch which tool to invoke.
Consider the following example:

```shell-session
$ export RELENG_CMAKE=cmake3
$ releng-tool
[cmake3 will be used for cmake projects]
```
