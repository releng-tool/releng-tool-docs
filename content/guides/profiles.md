# Profiles

Profiles provide a way to support tailoring the execution of a releng-tool
run for select project requirements. A user can define a profile to enable by
providing a [`--profile` argument](arg-profile). A profile value can then be
read by a project's configuration or various package stages to
manipulate a run as desired. Note that releng-tool does not use any provided
profile values other than normalizing profile strings to be forwarded to
project/package scripts. For example, consider the following run that flags
a profile named `awesome-mode`:

```
releng-tool --profile awesome-mode
```

A project configuration or package stage can then check the
[`RELENG_PROFILES`](env-releng-profiles) variable to determine if a
conditional event should be performed. To continue with this example, if
looking to add an additional package when using this profile, the following
can be added in a project's `releng-tool.rt` file:

```python
packages = [
    'example',
]

if 'awesome-mode' in RELENG_PROFILES:
	packages.append('awesome-mods')
```

Multiple profiles can be provided as well:

```
releng-tool --profile awesome-mode --profile another-example
 (or)
releng-tool --profile awesome-mode,another-example
 (or)
releng-tool --profile "awesome-mode;another-example"
```

The script environment provides a list of known profiles. However, if reading
the environment variable `RELENG_PROFILES`, note that if more than one profile
is defined, the environment string will be semicolon-separated values.
Considering the above example, the environment variable would be populated
as follows:

```
awesome-mode;another-example
```

Profile names are normalized when processed by releng-tool. A profile
value will replace special characters with dashes and will lowercase the
resulting value. The following shows an example of normalized profile names
that are all equivalent:

- `red-backed-shrike` (normalized form)
- `Red_Backed_Shrike`
- `Red Backed Shrike`
