# Typing Stubs for PyGObject

[![image](https://travis-ci.org/pygobject/pygobject-stubs.svg?branch=master)](https://travis-ci.org/pygobject/pygobject-stubs)
[![PyPI](https://img.shields.io/pypi/v/pygobject-stubs)](https://pypi.org/project/PyGObject-stubs)

## Installation
```
pip install pygobject-stubs
```

### Configuration

Some libraries exist in multiple versions like Gtk3/4. As both libraries are
currently imported under the namespace `Gtk` only stubs for one can be installed.

You need to decide this at install time either by using the `--config-settings` option
with pip

	$ pip install pygobject-stubs --no-cache-dir --config-settings=config=Gtk3,Gdk3,Soup2

or by setting the `PYGOBJECT_STUB_CONFIG` env variable

	$ PYGOBJECT_STUB_CONFIG=Gtk3,Gdk3,Soup2 pip install --no-cache-dir pygobject-stubs

If no configuration is set, the most recent version of each library is installed.

`--no-cache-dir` is only necessary on subsequent reinstalls, otherwise the stubs will not
be rebuild and a cache of a previous installation is used.

## Contributing

[Guide](./CONTRIBUTING.md)
