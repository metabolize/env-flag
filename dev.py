#!/usr/bin/env python

import os
import click
from executor import execute


def python_source_files():
    import glob

    include_paths = glob.glob("*.py")
    exclude_paths = []
    return [x for x in include_paths if x not in exclude_paths]


@click.group()
def cli():
    pass


@cli.command()
def init():
    execute("pip2 install --upgrade -r requirements_dev_py2.txt")
    execute("pip3 install --upgrade -r requirements_dev_py3.txt")


@cli.command()
def test():
    execute("nose2")


@cli.command()
def test_both():
    execute("python2 -m nose2")
    execute("python3 -m nose2")


@cli.command()
def lint():
    execute("flake8", *python_source_files())


@cli.command()
def black():
    execute("black", *python_source_files())


@cli.command()
def black_check():
    execute("black", "--check", *python_source_files())


@cli.command()
def publish():
    execute("rm -rf dist/")
    execute("python setup.py sdist")
    execute("twine upload dist/*")


if __name__ == "__main__":
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    cli()
