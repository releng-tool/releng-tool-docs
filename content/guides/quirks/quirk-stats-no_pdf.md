(quirk-releng.stats.no_pdf)=
# Quirk `releng.stats.no_pdf`

releng-tool will generate statistics for a build (such as the duration it
takes to build a specific package) and place this information in the
output directory. If an environment has [Matplotlib][matplotlib] installed,
PDF-format statistics may be generated for a more visual inspection of this
information.

If a user does not want PDF statistics to be created, the quirk
`releng.stats.no_pdf` can be used:

```
releng-tool --quirk releng.stats.no_pdf
```

## See also

- [Matplotlib][matplotlib]
- [](quirks)


[matplotlib]: https://matplotlib.org/
