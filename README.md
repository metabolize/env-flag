env-flag
========

Get boolean values from environment variables in Python.

```py
from env_flag import env_flag

# When unset, default to `False`.
debug = not env_flag('PRODUCTION')

# When unset, use explicit default.
is_local = get_bool('IS_LOCAL', default=True)
```

Values are coerced as follows:

- When the variable is unset, or set to the empty string, return `default`.
- When the variable is set to a truthy value, return `True`.
  These are the truthy values:
      - 1
      - true, yes, on
- When the variable is set to the anything else, return `False`.
  Example falsy values:
      - 0
      - no
- Ignore case and leading/trailing whitespace.


Development
-----------

```sh
pip install -r requirements_dev.txt
rake test
rake lint
```


Contribute
----------

- Issue Tracker: github.com/bodylabs/env-flag/issues
- Source Code: github.com/bodylabs/env-flag

Pull requests welcome!


Support
-------

If you are having issues, please let us know.


License
-------

The project is licensed under the two-clause BSD license.
