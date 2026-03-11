# Configuration overrides

:::{deprecated} 2.0
The use of a `releng-overrides` script is deprecated. Various override
capabilities noted below can either be supported in a `releng-tool.rt`
configuration or have alternative approaches to performing overrides.
:::

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

See [`override_extract_tools`](conf-override-extract-tools).

## Tool overrides

See [Environment — Tool overrides](env-tool-overrides).
