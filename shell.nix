let
  sources = import ./npins;
  pkgs = import sources.nixpkgs {};
in
pkgs.mkShell {
  nativeBuildInputs = [
    pkgs.gobject-introspection
    (pkgs.python3.withPackages (pp: [
      pp.black
      pp.isort
      pp.mypy
      pp.pygobject3
    ]))
  ];

  buildInputs = [
    pkgs.appstream
    pkgs.atk
    pkgs.cinnamon.xapp
    pkgs.farstream
    pkgs.flatpak
    pkgs.gdk-pixbuf
    pkgs.geoclue2
    pkgs.glib
    pkgs.gnome-online-accounts
    pkgs.gobject-introspection
    pkgs.graphene
    pkgs.gsound
    pkgs.gspell
    pkgs.gst_all_1.gst-plugins-bad # GstWebRTC
    pkgs.gst_all_1.gst-plugins-base
    pkgs.gst_all_1.gstreamer
    pkgs.gtk3
    pkgs.gtk4
    pkgs.gtksourceview4
    pkgs.gtksourceview5
    pkgs.libgudev # required by manette
    pkgs.libadwaita
    pkgs.libappindicator-gtk3
    pkgs.libayatana-appindicator
    pkgs.libgit2-glib
    pkgs.libhandy
    pkgs.libmanette
    pkgs.libnotify
    pkgs.libpanel
    pkgs.libportal
    pkgs.librsvg
    pkgs.libsecret
    pkgs.libsoup
    pkgs.libsoup_3
    pkgs.ostree
    pkgs.pango
    pkgs.vte
    pkgs.webkitgtk_6_0
  ];

  env = {
    # Ensure the environment is not contaminated.
    XDG_DATA_DIRS = "";
    GI_GIR_PATH = "";
    GI_TYPELIB_PATH = "";
  };
}
