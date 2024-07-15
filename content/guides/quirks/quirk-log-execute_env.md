(quirk-releng.log.execute_env)=
# Quirk `releng.log.execute_env`

When releng-tool is configured with [`--debug`](arg-debug), the tool
will log (among other things) process executions. Debugging can print
information such as working directory of an execution, as well as arguments
used for a call. The environment for an execution is not logged by default.
For users wishing to include this information as well before an invoked
process, the `releng.log.execute_env` quick can be used.

```
releng-tool --debug --quirk releng.log.execute_env
```

## See also

- [](quirks)
