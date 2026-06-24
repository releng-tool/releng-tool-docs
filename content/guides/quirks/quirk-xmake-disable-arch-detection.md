(quirk-releng.xmake.disable_arch_detection)=
# Quirk `releng.xmake.disable_arch_detection`

In select environments, a generated Xmake project may fail to link due
to automatic architecture detection not working as expected. This can be
observed in Windows-based builds when using clang, where packages may build
64-bit applications but attempt to link against 32-bit MSVC. When Xmake
builds are explicitly pass in an architecture value, this issue is no longer
observed. To help handle this scenario, releng-tool will detect an applicable
architecture value of the native system that is compatible for Xmake and pass
this value during Xmake configuration stage.

Note, packages building for other hosts and using toolchains can still override
an architecture value using available package options.

If a developer experiences issues with the automatic detection and explicit
architecture configuration, this feature can be disabled using the quirk
`releng.xmake.disable_arch_detection` using the command line:

```
releng-tool --quirk releng.xmake.disable_arch_detection
```

Or adding in the project configuration:

```
quirks = [
    ...
    'releng.xmake.disable_arch_detection',
]
```

## See also

- [](quirks)
