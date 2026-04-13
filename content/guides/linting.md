# Linting

:::{versionadded} 2.7
:::
:::{versionchanged} 3.0 Support maximum lint version checks.
:::

The releng-tool application provides linting actions to allow developers to
help sanity check their project configuration. For example:

```
releng-tool lint
```

The goal of this action is to:

- Help warn about unexpected configuration issues.
- Inform users of deprecated features being used.

The action will cycle through packages configured for a project, checking both
project configuration, package configurations and more for notable issues.

For scenarios where a user wants to ignore lines based on preference or
false-positives, lines can be commented with a `noqa` keyword to not be
flagged. For example:

```python
UNEXPECTED_KEY = True  # noqa
```

As releng-tool adds lint checks over time, new lint checks are mapped to the
release version of releng-tool that introduces the check. For example, if
releng-tool v3 adds two new checks, both checks will be mapped to v3.0. If
a build environment wants to perform CI without utilizing new lint checks,
they can do so by configuring a maximum version for lint checks to use. This
can be configured in the [`lint_max_version`](conf-lint-max-version) project
configuration:

```
lint_max_version = '2.8'
```

Or configured with a [`RELENG_LINT_MAX_VERSION`](env-releng-lint-max-version)
environment variable:

```
export RELENG_LINT_MAX_VERSION=2.8
releng-tool lint
```

This should allow developers to maintain a working CI pipeline that may lint
their project configurations while still utilizing newer versions of
releng-tool. Developers can bump to newer link-check versions when they are
ready to handle new checks that may be introduced.
