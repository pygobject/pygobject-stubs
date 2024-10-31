# 2.12.0 (31 Oct 2024)

## Feature

* Add Spelling 1
* Add GstRtp and GstRtps ([#188](https://github.com/pygobject/pygobject-stubs/issues/188)) (#188)

## Typing

* Improve type hints for
    - Flatpak: Update to 1.15.10
    - Gdk3
    - GdkPixbuf: Update to 2.42.12
    - Gio
    - GIRepository: Update to 1.80.1
    - GLib: Update to 2.80.5
    - Graphene
    - Gsk
    - Gst
    - Gst: Update to 1.24.7
    - GstRtspServer
    - Gtk3
    - Gtk4: Update to 4.16.2
    - GtkSource5: Update to 5.12.1
    - Pango: Update to 1.54.0

# 2.11.0 (03 Apr 2024)

## Feature

* Add Goa ([#163](https://github.com/pygobject/pygobject-stubs/issues/163)) (#163)
* Add JavaSciptCore 6.0 for WebKit
* Add Notify 0.7 ([#175](https://github.com/pygobject/pygobject-stubs/issues/175)) (#175)
* Add Panel
* Add Poppler ([#180](https://github.com/pygobject/pygobject-stubs/issues/180)) (#180)
* Add Secret ([#163](https://github.com/pygobject/pygobject-stubs/issues/163)) (#163)
* Add XApp
* Add Xdp ([#178](https://github.com/pygobject/pygobject-stubs/issues/178)) (#178)
* Add WebKit-6.0

## Improvements

* Generator: Rename optional argument

## Typing

* Improve type hints for
    - Adw: Upgrade stubs to 1.5 ([#181](https://github.com/pygobject/pygobject-stubs/issues/181)) (#181)
    - Gtk3
    - Gtk4: Upgrade stubs to 4.14 ([#182](https://github.com/pygobject/pygobject-stubs/issues/182)) (#182)

## Bug Fixes

* Gsk: Use pyi extension
* Generator: Fix regex class pattern (#168)

# 2.10.0 (16 Nov 2023)

## Feature

* Add Handy
* Add GstWebRTC
* Add GstSdp

## Improvements

* Generator: Require GIRepository 2.0

## Typing

* Improve type hints for
    - Adw
    - Gio
    - GLib
    - GstPbutils
    - Gtk4

## Bug Fixes

* Allow GObject.emit to return value
* generator: Fix array length param for functions

# 2.9.0 (14 Sep 2023)

## Feature

* Add AyatanaAppIndicator3
* Add AppStream and OSTree ([#152](https://github.com/pygobject/pygobject-stubs/issues/152)) (#152)
* Add Flatpak

## Improvements

* generator: Strip documentation strings

## Typing

* Improve type hints for
    - AppIndicator3
    - Cairo
    - Gdk4
    - GObject
    - Gtk3
    - PangoCairo

## Bug Fixes

* generator: Fix documentation if empty

# 2.8.0 (24 May 2023)

## Improvements

* generator: Check nullability for __init__

## Typing

* Improve type hints for
    - Adw
    - Gtk4

## Bug Fixes

* generate: Force varargs if function has closure
* parse: Ignore documentation

# 2.7.0 (28 Apr 2023)

## Improvements

* Extract class' docstring

## Typing

* Improve type hints for
    - Gdk4
    - Gtk3

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
