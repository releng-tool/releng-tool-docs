# Passthrough options

It is recommended to self-contain as many configuration options, if not all,
inside a releng-tool project configuration. This can help promote a more
consistent build for a project across various developer and CI environments.
However, there may be a desire for certain per-execution hints to set when
looking to help identify a given build or perform variant/debug-tailored builds.

## Build identifier

:::{versionadded} 4.2
:::
:::{versionchanged} 4.3
Allow accepting a pre-set `RELENG_BUILD_ID` environment variable.
:::
:::{versionchanged} 4.3 Support implicit build identifier detection.
:::

A releng-tool run can accept a build identifier (a.k.a. job identifier) to
help identify a specific build execution. Typically used in a CI context where
an identifier is provided to releng-tool, which in-turn is used in a project's
post-build phase to help package with a unique name.

A build identifier can be provided for a run using either the
[`--build-id <id>`](arg-build-id) argument or pre-set using the
[`RELENG_BUILD_ID`](env-releng-build-id-set) environment variable. For example:

```none
releng-tool --build-id=123
```

With the above example, [`RELENG_BUILD_ID`](env-releng-build-id) will be set
in both the script environment and executed calls with a value of `123`.

When operating in a common CI context (e.g. Jenkins), the `RELENG_BUILD_ID`
value will be pre-populated with a respective build identifier (if not
explicitly set). The following table outlines supported tool checks. A
environment variable is used to detect if running in a CI context. If a CI
context is detected, a respective environment variable will be parsed for
a build identifier.

| Type                | Detection            | Key |
| ------------------- | -------------------- | --- |
| AWS CodeBuild       | `CODEBUILD_BUILD_ID` | `CODEBUILD_BUILD_NUMBER`
| Azure Pipelines     | `TF_BUILD`           | `BUILD_BUILDID`
| Bitbucket Pipelines | `CI`                 | `BITBUCKET_BUILD_NUMBER`
| CircleCI            | `CIRCLECI`           | `CIRCLE_BUILD_NUM`
| Forgejo             | `FORGEJO_ACTIONS`    | `FORGEJO_RUN_ID`
| GitHub              | `GITHUB_ACTIONS`     | `GITHUB_RUN_ID`
| GitLab              | `GITLAB_CI`          | `CI_PIPELINE_ID`
| Jenkins             | `JENKINS_URL`        | `BUILD_NUMBER`
| Travis CI           | `TRAVIS`             | `TRAVIS_BUILD_ID`
| Woodpecker          | `CI`                 | `CI_PIPELINE_NUMBER`

Developers can opt-out of an implicit build identifier by setting the
`RELENG_BUILD_ID_NO_IMPLICIT` environment variable:

```
RELENG_BUILD_ID_NO_IMPLICIT=1
```

## Build variant

:::{versionadded} 4.3
:::

A build variant (string) can be provided into a releng-tool run. This is
typically used to help identify special variant builds such as enabling a
custom feature or enabling certain debugging capabilities in a build.

A build variant can be provided for a run using either the
[`--build-variant <variant>`](arg-build-variant) argument or pre-set using the
[`RELENG_BUILD_VARIANT`](env-releng-build-variant-set) environment variable.
For example:

```none
releng-tool --build-variant=.debug
```

With the above example, [`RELENG_BUILD_VARIANT`](env-releng-build-variant)
will be set in both the script environment and executed calls with a value
of `.debug`.

## Build profiles

:::{versionadded} 2.5
:::

Build profile tags can be provided for a run to tailor for one or more features
(which can be used in combination with a build variant hint).

For more information on profile tags, see [build profile](/guides/profile).

## Other

See also:

- [Revision overrides in CI](revision-overrides-in-ci)
- [Variable injection](arg-variable-injection)
