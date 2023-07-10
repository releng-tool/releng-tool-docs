# Quirk `releng.git.no_depth`

releng-tool may use the [`--depth`][git--depth] option for Git-based packages
to to perform shallow checkouts to improve fetch performance. If a user does
not want to perform shallow checkouts, the `releng.git.no_depth` quirk may be
used.

```
releng-tool --quirk releng.git.no_depth
```

## See also

- [Git clone's `--depth` option][git--depth]
- [](quirks)


[git--depth]: https://git-scm.com/docs/git-clone#Documentation/git-clone.txt---depthltdepthgt
