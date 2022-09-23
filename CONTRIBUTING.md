## Rules for a great git commit message style

- Separate subject from body with a blank line
- Do not end the subject line with a period
- Capitalize the subject line and each paragraph
- Use the imperative mood in the subject line
- Wrap lines at 72 characters
- Use the body to explain what and why you have done something. In most cases, you can leave out details about how a change has been made.

## Generating base stubs for module

You can generate stubs with `tools/generate.py`.

Usage:

```shellsession
$ python tools/generate.py -h
usage: generate.py [-h] module version

Generate module stubs Usage: generate.py Gdk 3.0 > Gdk.pyi

positional arguments:
  module      Gdk, Gtk, ...
  version     3.0, 4.0, ...

options:
  -h, --help  show this help message and exit
```

To generate `Gdk` stubs based on PyGObject 3.0 and save to `Gdk.py`:

```bash
pip install mypy PyGObject
python generate.py Gdk 3.0 > Gdk.py
```

## Testing generated stubs are correctly typed

```bash
mypy examples
```
