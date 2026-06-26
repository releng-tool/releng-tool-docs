# Revision Overrides in CI

A releng-tool project will typically have packages configured to stable
versions to produce a consistent build. There is also support for operating
in a [development mode](/guides/development-mode) to help support tailoring
development or canary builds. However, developers may be looking for a simple
means to tweak a build to use a specific version/branch for a component. While
users could locally tweak a revision for testing or utilize
[local-sources mode](/guides/local-sources-mode), such approaches are not
great when trying to utilize when performing continuous integration (CI).

The recommended approach for overriding revisions for packages in a CI context
is to utilize package-specific force revision options. An invoke of releng-tool
accepts the [`<pkg>_FORCE_REVISION`](pkg-opt-force-revision) option which can
override the revision used for a specific package. Forced revisions take
priority over any other revision/version configuration, even when operating
in a development mode.

Consider the following example of a project with three packages:

```
└── my-releng-tool-project/
    ├── package/
    │   ├── liba/
    │   │   └── ...
    │   ├── libb/
    │   │   └── ...
    │   └── my-app/
    │       └── ...
    ...
```

A developer may be in a scenario where they want to quickly test a build
with changes to the library `liba` and an application `my-app`. To do so,
the following environment variables can be set:

```none
LIBA_FORCE_REVISION=v2.3.4
MY_APP_FORCE_REVISION=feature/new-stuff
```

The above shows a developer wanting to use a v2.3.4 tag for the library and a
feature branch named `feature/new-stuff` for the application. When set,
releng-tool will utilize these revisions for these packages. The `libb` library
will use its existing revision in the package definition.

This can be demonstrated in a shell as follows:

````{tab} Linux/OS X
```{eval-rst}
.. only:: latex

    **Linux/OS X**
```
```shell-session
$ export LIBA_FORCE_REVISION=v2.3.4
$ export MY_APP_FORCE_REVISION=feature/new-stuff
$ releng-tool
...
```
````

````{tab} Windows
```{eval-rst}
.. only:: latex

    **Windows**
```
```doscon
> set LIBA_FORCE_REVISION=v2.3.4
> set MY_APP_FORCE_REVISION=feature/new-stuff
> releng-tool
...
```
````

The approach to providing revision overrides in a CI configuration would
commonly use inputs to accept revision values and using these inputs to
ensure environment variables are configured. Consider the following CI
definition examples:

````{tab} GitHub
```{eval-rst}
.. only:: latex

    **GitHub**
```
```yaml
on:
  workflow_dispatch:
    inputs:
      LIBA_FORCE_REVISION:
        description: "Force the revision of liba to the provided value."
      LIBB_FORCE_REVISION:
        description: "Force the revision of libb to the provided value."
      MY_APP_FORCE_REVISION:
        description: "Force the revision of my-application to the provided value."

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: releng-tool
        env:
          LIBA_FORCE_REVISION: ${{ inputs.LIBA_FORCE_REVISION }}
          LIBB_FORCE_REVISION: ${{ inputs.LIBB_FORCE_REVISION }}
          MY_APP_FORCE_REVISION: ${{ inputs.MY_APP_FORCE_REVISION }}

```
````

````{tab} GitLab (Inputs)
```{eval-rst}
.. only:: latex

    **GitLab (Inputs)**
```
```yaml
spec:
  inputs:
    LIBA_FORCE_REVISION:
      default: ""
      description: "Force the revision of liba to the provided value."
    LIBB_FORCE_REVISION:
      default: ""
      description: "Force the revision of libb to the provided value."
    MY_APP_FORCE_REVISION:
      default: ""
      description: "Force the revision of my-application to the provided value."
---

variables:
  LIBA_FORCE_REVISION: $[[ inputs.LIBA_FORCE_REVISION ]]
  LIBB_FORCE_REVISION: $[[ inputs.LIBB_FORCE_REVISION ]]
  MY_APP_FORCE_REVISION: $[[ inputs.MY_APP_FORCE_REVISION ]]

test:
  script: releng-tool
```
````

````{tab} GitLab (Variables)
```{eval-rst}
.. only:: latex

    **GitLab (Variables)**
```
```yaml
variables:
  LIBA_FORCE_REVISION:
    description: "Force the revision of liba to the provided value."
  LIBB_FORCE_REVISION:
    description: "Force the revision of libb to the provided value."
  MY_APP_FORCE_REVISION:
    description: "Force the revision of my-application to the provided value."

test:
  script: releng-tool
```
````

````{tab} Jenkins
```{eval-rst}
.. only:: latex

    **Jenkins**
```
```groovy
pipeline {
    agent any

    parameters {
        string(name: 'LIBA_FORCE_REVISION', 
               description: 'Force the revision of liba to the provided value.')
        string(name: 'LIBB_FORCE_REVISION', 
               description: 'Force the revision of libb to the provided value.')
        string(name: 'MY_APP_FORCE_REVISION', 
               description: 'Force the revision of my-application to the provided value.')
    }

    stages {
        stage('Test') {
            steps {
                sh 'releng-tool'
            }
        }
    }
}
```
````

When a `<PKG>_FORCE_REVISION` environment variable is empty, the variable
will be ignored.

:::{tip}
Developers can utilize [`printvars`](action-printvars) to easily list all
applicable force-revision variables for a project:

```shell
releng-tool printvars | grep FORCE_REVISION
 (or)
releng-tool printvars | findstr FORCE_REVISION
```
:::

