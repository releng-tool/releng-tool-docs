# License generation

At the end of a `releng-tool` invoke, the final stages will compile a list of
package license information (if licenses are defined). If a user wishes to
compile a project's list of license information without performing an entire
build, the `licenses` action can be used:

```shell
releng-tool licenses
```

License information can then be found in the root directory's
`<root>/licenses` folder.
