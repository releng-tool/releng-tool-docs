(quirk-releng.disable_spdx_check)=
# Quirk `releng.disable_spdx_check`

When package definitions are being processed, any license configurations will
be checked to see if they conform with [SPDX license identifiers][spdx]. If
not, a warning will be generated.

If a user wishes to ignore all SPDX license warnings, the
`releng.disable_spdx_check` quirk can be used:
  
```
releng-tool --quirk releng.disable_spdx_check
```

## See also

- [](quirks)
- [SPDX license identifiers][spdx]


[spdx]: https://spdx.org/licenses/
