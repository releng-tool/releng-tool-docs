# API Mode

:::{versionadded} 2.10
:::

Running releng-tool can be invoked in an "API mode" where an execution will
generate a programmatic response for a caller. When in an API mode,
the resulting standard output stream will contain a JSON-compatible output
for external applications to process. All other messages that may typically
be generated on the standard output stream will instead be written to the
standard error stream.

Running releng-tool with `--api` enables API mode for that run:

```
releng-tool --api
```

Responses may vary on the action and other options used. Callers will always
get a `code` response (matching the return value):

```
{
    "code": 0,
    ...
}
```

There is no definitive schema for this output at this time. Results may
vary as this feature evolves.

Due to the flexibility of how projects/extensions can manipulate a run and
generate data on the standard output stream, it is recommended that
developers utilize logging calls provided by this tooling to ensure
the standard output stream is not populated during an API mode run.

## Example

The following shows an example API mode:

```
{
    "code": 0,
    "releng-tool": "...",
    "packages": {
        "my-app": {
            "build-dir": ".../output/build/my-app-1.2.4",
            "build-output-dir": ".../output/build/my-app-1.2.4/releng-output",
            "def-dir": ".../package/my-app",
            "def-file": ".../package/my-app/my-app.rt",
            "durations": {
                "extract": 0,
                "patch": 0,
                "fetch-post": 0,
                "boot": 0,
                "configure": 4,
                "build": 32,
                "install": 0,
                "post": 0
            },
            "install-type": "target",
            "internal": false,
            "license": [
                "Apache-2.0"
            ],
            "license-files": [
                "LICENSE.txt"
            ],
            "revision": "v1.2.4.0",
            "site": "https://git.example.com/grp/my-app.git",
            "stages": [
                "extract",
                "patch",
                "fetch-post",
                "boot",
                "configure",
                "build",
                "install",
                "post"
            ],
            "type": "cmake",
            "vcs-type": "git",
            "version": "1.2.4"
        }
    }
}
```
