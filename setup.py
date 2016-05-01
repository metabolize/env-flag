# https://coderwall.com/p/qawuyq
# Thanks James.

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ''
    print 'warning: pandoc or pypandoc does not seem to be installed; using empty long_description'

from setuptools import setup

setup(
    name='env-flag',
    version=__import__('env_flag').__version__,
    author='Body Labs',
    author_email='paul.melnikow@bodylabs.com',
    description='Get boolean values from environment variables.',
    long_description=long_description,
    url='https://github.com/bodylabs/env-flag',
    license='MIT',
    py_modules=[
        'env_flag',
    ],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
