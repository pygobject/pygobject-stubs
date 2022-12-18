# Typing Stubs for PyGObject

[![image](https://travis-ci.org/pygobject/pygobject-stubs.svg?branch=master)](https://travis-ci.org/pygobject/pygobject-stubs)
[![PyPI](https://img.shields.io/pypi/v/pygobject-stubs)](https://pypi.org/project/PyGObject-stubs)

## Installation
```
pip install PyGObject-stubs
```

### Installation of Multi Version stubs

Some libraries exist in multiple versions like Gtk3/4. As both libraries are
currently imported under the namespace `Gtk` only stubs for one can be installed.

You need to decide this at install time with setting the ENV var
`PYGOBJECT_STUB_CONFIG`.

If you install from pypi the most current version of a library is installed
by default without any further configuration needed. 

If you want older versions installed, currently you need to install from git
and specify them.

Example:
`PYGOBJECT_STUB_CONFIG=Gtk3,Soup2 pip install git+https://github.com/pygobject/pygobject-stubs.git`

## Contributing

[Guide](./CONTRIBUTING.md)
