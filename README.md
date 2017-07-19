<div>
    <img title="Mail icon" src="http://elementary.io/images/docs/human-interface-guidelines/icons/64/internet-mail.svg" />
    <img title="RSS reader icon" src="http://elementary.io/images/docs/human-interface-guidelines/icons/64/internet-news-reader.svg" />
    <img title="Web browser icon" src="http://elementary.io/images/docs/human-interface-guidelines/icons/64/internet-web-browser.svg" />
    <img title="Photos icon" src="http://elementary.io/images/docs/human-interface-guidelines/icons/64/multimedia-photo-manager.svg" />
    <img title="Network error icon" src="http://elementary.io/images/docs/human-interface-guidelines/icons/64/network-error.svg" />
    <img title="Calendar icon" src="http://elementary.io/images/docs/human-interface-guidelines/icons/64/office-calendar.svg" />
    <img title="Warning icon" src="http://elementary.io/images/docs/human-interface-guidelines/icons/64/dialog-warning.svg" />
    <img title="Chat icon" src="http://elementary.io/images/docs/human-interface-guidelines/icons/64/internet-chat.svg" />
    <img title="Photos icon" src="http://elementary.io/images/docs/human-interface-guidelines/icons/64/multimedia-photo-manager.svg" />
    <img title="Videos icon" src="http://elementary.io/images/docs/human-interface-guidelines/icons/64/multimedia-video-player.svg" />
    <img title="Online Accounts icon" src="http://elementary.io/images/docs/human-interface-guidelines/icons/64/preferences-desktop-online-accounts.svg" />
    <img title="Terminal icon" src="http://elementary.io/images/docs/human-interface-guidelines/icons/64/utilities-terminal.svg" />
 </div>

# elementary Icons

[![Bountysource](https://www.bountysource.com/badge/tracker?tracker_id=27377189)](https://www.bountysource.com/trackers/27377189-elementary-icons)

An original set of vector icons designed specifically for [elementary OS](http://elementary.io) and its desktop environment: Pantheon.

These icons are licensed openly under the terms of the [GNU General Public License](COPYING). Redistributing, forking, remixing, etc. are encouraged!

If you feel the desire to compensate the artists who maintain these icons for your usage, [please see this page](http://elementary.io/get-involved#funding) and thank you!

## Contributing Icons
It is recommended to use the free and open source [Inkscape](http://inkscape.org) vector editor to create elementary icons. Any and all icons must follow the elementary [Icon Design Guidelines](http://elementary.io/docs/human-interface-guidelines#iconography).

To contribute to the elementary icon set, open a pull request to this repository with your icon(s).

It is strongly encouraged to vacuum all vectors with [Inkscape](http://inkscape.org). This keeps the repository lean, clean, and fast for everyone. For convenience, a git pre-commit hook is included. To install, run these commands from your local repository folder:
```bash
$ cp pre-commit .git/hooks/
$ chmod +x .git/hooks/pre-commit
```

## Installation
You need the [CMake](https://cmake.org) build system to install it.
Once you've installed it, run these commands in the root of the icon set.
```bash
$ mkdir build && cd build
$ cmake .. -DCMAKE_INSTALL_PREFIX=/usr
$ sudo make install
```

## Not a Universal Icon Set
Since this set is designed specifically for elementary OS, pull requests to add icons or symlinks that are specific to other desktop environments (such as `xfce-*` or `gnome-*` named icons) will be rejected.

Use of icon names in line with the [FreeDesktop.Org Icon Naming Specification](http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html) is encouraged.

## Third-Party Brand Preservation
elementary icons do not attempt to supply icons for third-party apps. Pull requests to add icons or symbolic links that would overwrite the branding of third-party apps will be rejected.

