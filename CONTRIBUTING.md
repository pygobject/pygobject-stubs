# Contributing

## Generating base stubs for module

You can generate stubs with `tools/generate.py`.

Usage:

```shellsession
$ python tools/generate.py -h
usage: generate.py [-h] [-o OUTPUT] module version

Generate module stubs Usage: generate.py Gdk 3.0 > Gdk.py

positional arguments:
  module      Gdk, Gtk, ...
  version     3.0, 4.0, ...

options:
  -h, --help  show this help message and exit
  -o OUTPUT   Output file
```

To re-generate all known stubs, run `tools/update_all.py`.
You can comment out the libraries you are not interested in.

## Install development dependencies

    $ pip install .[dev]

Using editable install `pip install -e .` does not currently work for libraries which have multiple versions

## Use pre-commit

pre-commit is a library which executes checks defined in this repository.

    $ pre-commit install

## Commit Messages

A good article regarding [good commit messages](https://chris.beams.io/posts/git-commit/)

Every commit message must be prefixed with one of the following tags:

Changelog relevant

- feat      (a new feature was added)
- fix       (something was fixed)
- imprv     (improvements)
- change    (existing functionality was changed)
- typing    (whenever type hints are added to a module, Example: typing: GLib: Add hints)

Prefixes for development

- new       (new code, but the end user will not notice)
- ci        (ci related changes)
- cq        (code quality changes e.g. formatting, codestyle)
- cfix      (code fixes which should not show up in the changelog)
- refactor  (code was changed, but the end user will not notice)
- chore     (reoccuring tasks which need to be done)
- release   (only used for release commits)
- other     (everything which does not fit any categories)

Example:

`feat: New Button which does something`
