# 2.6.0 (08 Apr 2023)

## Improvements

* Generator: Correctly type optional props

## Typing

* Improve type hints for
    - Adw
    - GObject
    - Graphene
    - Gsk
    - Gtk3
    - Gtk4
    - GtkSource5
    - Pango

## Bug Fixes

* Generator: Correct arg info for setter

# 2.5.0 (21 Mar 2023)

## Feature

* Add Vte (#7)
* Add Rsvg (#116)

## Improvements

* generator: Make file executable
* generator: Add TypeVar _SomeSurface
* generator: Better hints for functions

## Typing

* Improve type hints for
    - Gdk4
    - Gio
    - Gio
    - Gtk3
    - Gtk4
    - GtkSource4

## Bug Fixes

* generator: Fix hash maps
* generator: Use GObject.GInterface for ifaces

# 2.4.0 (19 Feb 2023)

## Feature

* Add Ggit

## Improvements

* Use GObject introspection to generate more accurate stubs ([#98](https://github.com/pygobject/pygobject-stubs/issues/98)) (#98)

## Typing

* Improve type hints for
    - Adw
    - Atk
    - Gdk3
    - Gdk4
    - GdkPixbuf
    - Geoclue
    - Gio
    - GLib
    - GSound
    - Soup3

# 2.3.1 (08 Feb 2023)

## Bug Fixes

* Fix installing multilib stubs

# 2.3.0 (08 Feb 2023)

## Feature

* Add GtkSource5

## Typing

* Improve type hints for
    - Adw
    - Gdk3
    - GeoClue
    - GObject
    - Gtk3
    - Gtk4
    - Manette

## Bug Fixes

* Default to GtkSource5 when installing
* Overwrite existing files when building from source

# 2.2.0 (03 Jan 2023)

## Feature

* Build with a PEP517 in-tree backend
* Add Manette
* Add Adwaita
* Add Gdk4

## Typing

* Improve type hints for
    - Gtk4
    - Gdk4
    - Gtk3
    - Soup
    - Gio
    - GObject
    - Soup3

# 2.1.0 (18 Dec 2022)

## Changes

* Port to pyproject.toml

# 2.0.0 (18 Dec 2022)

## Changes

* Add install option for multi version libs
* Newest version of lib is installed by default
