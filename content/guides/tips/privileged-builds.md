# Privileged builds

It is never recommended to invoke a build with elevated (e.g. root) privileges.
A builder invoking in an elevated environment runs the risk of a misconfigured
releng-tool project *dirtying or destroying* the builder's host environment.

releng-tool will generate a warning when an elevated run has been detected.
For certain cases when using a container image that operates in a single-user
mode, the image can define the environment variable
[`RELENG_IGNORE_RUNNING_AS_ROOT`](env-releng-ignore-running-as-root) to
suppress these warnings.
