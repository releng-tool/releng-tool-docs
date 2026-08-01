# Network isolation

:::{versionadded} 3.1
:::

Developers can configure projects to run in a network isolation mode for
non-fetch stages. This helps promote the use of using only fetch-related
stages to acquire remote sources, and help support capabilities such as
[offline builds](tips/offline-builds).

When this feature is enabled, proxy-related environment variables are
configured in non-fetch stages to help restrict/limit network interaction.
This can cause remote-related requests to almost immediately timeout, causing
an execution failure. If a build stage attempts to use utilities that perform
a network request, the build stage would fail.

Network isolation mode can be configured at the project-level using
the [`network_isolation`](conf-network-isolation) project configuration:

```python
releng_config(
    ...
    network_isolation=True,
)
```

Developers may also tailor individual packages for network isolation mode
using the [`LIBFOO_NETWORK_ISOLATION`](pkg-opt-network-isolation) option.
For example, to enable it for the `myapp` package (if not configured at a
project level):

```python
MYAPP_NETWORK_ISOLATION = True
```

Developers can also opt-out of network-isolation if the project is configured
to isolate but a specific package still relies on networking outside of the
fetch stage:

```python
MYAPP_NETWORK_ISOLATION = False
```

Restricting networking is not intended to be a perfect isolation
capability, only a helper to support promoted practice. The
implementation will configure common proxy values to a local socket to
drop connections. Tools which do not utilize proxy options will not be
restricted.
