# env-flag

[![version](https://img.shields.io/pypi/v/env-flag?style=flat-square)][pypi]
[![python versions](https://img.shields.io/pypi/pyversions/env-flag?style=flat-square)][pypi]
[![license](https://img.shields.io/pypi/l/env-flag?style=flat-square)][pypi]
[![build](https://img.shields.io/circleci/project/github/metabolize/env-flag/master?style=flat-square)][build]
[![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg?style=flat-square)][coverage]
[![code style](https://img.shields.io/badge/code%20style-black-black?style=flat-square)][black]

Get boolean values from environment variables in Python.

[pypi]: https://pypi.org/project/env-flag/
[build]: https://circleci.com/gh/metabolize/env-flag/tree/master
[coverage]: https://github.com/metabolize/env-flag/blob/master/.coveragerc
[black]: https://black.readthedocs.io/en/stable/

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
./dev.py init
./dev.py test-both
./dev.py lint
./dev.py black
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
