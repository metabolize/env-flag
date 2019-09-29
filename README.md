# env-flag

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


## Development

```sh
pip install -r requirements_dev.txt
rake test
rake lint
```


## Contribute

- Issue Tracker: https://github.com/metabolize/env-flag/issues
- Source Code: https://github.com/metabolize/env-flag

Pull requests welcome!


## Support

If you are having issues, please let us know.


## Acknowledgements

This function was inspired by [node-env-flag][], the equivalent for Node.js.
It was developed at Body Labs by [Paul Melnikow][] and later open sourced.
It was forked in 2019 by Paul Melnikow. Thanks to a repository and package
transfer from Body Labs, the fork has been merged back into the original.

[node-env-flag]: https://www.npmjs.com/package/node-env-flag
[paul melnikow]: https://github.com/paulmelnikow


## License

The project is licensed under the two-clause BSD license.
