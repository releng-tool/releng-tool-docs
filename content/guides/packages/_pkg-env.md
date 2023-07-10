## `LIBFOO_ENV`

Provides a means to pass environment variables into all stages for a
package. This option is defined as a dictionary with key-value pairs where
the key is the environment name and the value is the environment variable's
value. This field is optional.

```python
LIBFOO_ENV = {
    'OPTION': 'VALUE',
}
```
