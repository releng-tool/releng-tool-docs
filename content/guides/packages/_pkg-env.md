## `LIBFOO_ENV`

:::{versionadded} 0.17
:::
:::{versionchanged} 2.2 Support added for path-like values.
:::

Provides a means to pass environment variables into all stages for a
package. This option is defined as a dictionary with key-value pairs where
the key is the environment name and the value is the environment variable's
value. This field is optional.

```python
LIBFOO_ENV = {
    'OPTION': 'VALUE',
}
```
