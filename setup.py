from setuptools import setup

readme = open("README.md", "rb").read().decode("utf-8")

setup(
    name="env-flag",
    version=__import__("env_flag").__version__,
    author="Body Labs & Metabolize",
    author_email="github@paulmelnikow.com",
    description="Get boolean values from environment variables",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/metabolize/env-flag",
    license="BSD-2-Clause",
    py_modules=["env_flag"],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
)
