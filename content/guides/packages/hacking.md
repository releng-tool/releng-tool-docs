# Package hacking

Package types may define various command line defines and options to help
support certain features or practices that best fit with releng-tool's
staged processing. In some advanced scenarios, developers may wish to override
these defines/options due to corner cases or preferences. Developers can
perform overrides by hinting in configurations for things to remove.

For example, [Make](/guides/packages/pkg-type-make)-based packages will
include a `PREFIX` variable assignment based on the project's or package's
configured prefix. This can result in the following installation command to
be invoked:

```
make DESTDIR=<output>/target install PREFIX=/usr
```

If the assignment of `PREFIX` causes issues for a package, a developer can
hint to remove such an option by configuring
[`LIBFOO_INSTALL_DEFS`](pkg-opt-make-install-defs) to be as follows:

```
LIBFOO_INSTALL_DEFS = {
    'PREFIX': None,
}
```

This will then result in the following installation command for the package:

```
make DESTDIR=<output>/target install
```

Overrides are typically support on each configuration, build and
install-related configurations. Not all defines/options can be overridden.
As such overrides are advanced, developers are recommended to refer to the
implementation for specifics. Developers can also use the
[`--debug`](arg-debug) argument to see explicit commands invoked:

```
releng-tool --debug
```
