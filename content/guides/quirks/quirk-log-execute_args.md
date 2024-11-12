(quirk-releng.log.execute_args)=
# Quirk `releng.log.execute_args`

When releng-tool is configured with [`--debug`](arg-debug), the tool
will log (among other things) process executions. Debugging can print
information such as working directory of an execution, as well as arguments
used for a call. For some commands, the command line and arguments can be
long and may be difficult to quickly scan for issues. To help improve the
use experience, the `releng.log.execute_args` quick can be used to print
each argument on their own line.

```
releng-tool --debug --quirk releng.log.execute_args
```

## See also

- [](quirks)
