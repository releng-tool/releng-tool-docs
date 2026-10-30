# Profile

A build profile provide a way to support tailoring the execution of a
releng-tool run for select project requirements. A user can define a profile tag
to enable by providing a [`--profile` argument](arg-profile). A profile tag can
then be read by a project's configuration or various package stages to
manipulate a run as desired. Note that releng-tool does not use any provided
profile tags other than normalizing profile strings to be forwarded to
project/package scripts. For example, consider the following run that adds a
profile tag named `awesome-mode`:

```
releng-tool --profile awesome-mode
```

A project configuration or package stage can then check the
[`RELENG_PROFILES`](env-releng-profiles) variable to determine if a
conditional event should be performed. To continue with this example, if
looking to add an additional package when using this profile tag, the following
can be added in a project's `releng-tool.rt` file:

```python
extra_packages = [
    'example',
]

if 'awesome-mode' in RELENG_PROFILES:
    extra_packages.append('awesome-mods')

releng_config(
    ...
    packages=[
        'package-a',
        'package-b',
        'package-c',
        *extra_packages,
    ],
)
```

Multiple profile tags can be provided as well:

```
releng-tool --profile awesome-mode --profile another-example
 (or)
releng-tool --profile awesome-mode,another-example
 (or)
releng-tool --profile "awesome-mode;another-example"
```

The script environment provides a list of known profile tags. However, if
reading the environment variable `RELENG_PROFILES`, note that if more than one
profile tag is defined, the environment string will be semicolon-separated
values. Considering the above example, the environment variable would be
populated as follows:

```
awesome-mode;another-example
```

Profile tags are normalized when processed by releng-tool. A profile tag
will replace special characters with dashes and will lowercase the resulting
value. The following shows an example of normalized profile tags that are all
equivalent:

- `red-backed-shrike` (normalized form)
- `Red_Backed_Shrike`
- `Red Backed Shrike`
