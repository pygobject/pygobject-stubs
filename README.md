# Typing Stubs for PyGObject

[![PyPI](https://img.shields.io/pypi/v/pygobject-stubs)](https://pypi.org/project/PyGObject-stubs)

## Installation

With uv:
```shell
uv add --dev pygobject-stubs
```

With pip:
```shell
pip install pygobject-stubs
```

### Configuration

Some libraries exist in multiple versions like Gtk3/4.
As both libraries are currently imported under the namespace `Gtk` only stubs for one can be installed.

You need to decide this at install time either by using the `--config-settings` option with pip:

```shell
pip install pygobject-stubs --no-cache-dir --config-settings=config=Gtk3,Gdk3,Soup2
```

or by setting the `PYGOBJECT_STUB_CONFIG` env variable:

```shell
PYGOBJECT_STUB_CONFIG=Gtk3,Gdk3,Soup2 pip install --no-cache-dir pygobject-stubs
```

If no configuration is set, the most recent version of each library is installed.

`--no-cache-dir` is only necessary on subsequent reinstalls, otherwise the stubs will not be rebuild and a cache of a previous installation is used.

#### uv

```
[tool.uv]
config-settings-package = { pygobject-stubs = { config = "Gtk3,Gdk3,Soup2" } }
```

#### poetry

https://python-poetry.org/docs/configuration/#installerbuild-config-settingspackage-name


### Project Integration

Usually you want the stubs to be installed as part of the development dependencies.
`pyproject.toml` does not allow to pass `config-settings` to requirements.
If you need specific versions of some libraries you can use a `requirements.txt` file instead, which allows to pass `config-settings` per requirement as of pip >= 23.1.0.

```shell
pip install . -r dev.txt
```

## Contributing

[Guide](./CONTRIBUTING.md)
