# elementary Icons
[![Translation status](https://l10n.elementary.io/widgets/desktop/-/icons-extra/svg-badge.svg)](https://l10n.elementary.io/engage/desktop/)

![Default App Icon](https://raw.githubusercontent.com/elementary/icons/master/apps/64/application-default-icon.svg)
![Locale Preferences Icon](https://raw.githubusercontent.com/elementary/icons/master/categories/64/preferences-desktop-locale.svg)
![Terminal App Icon](https://raw.githubusercontent.com/elementary/icons/master/apps/64/utilities-terminal.svg)
![Dialog Password Icon](https://raw.githubusercontent.com/elementary/icons/master/status/48/dialog-password.svg)
![Empty Battery Icon](https://raw.githubusercontent.com/elementary/icons/master/status/48/battery-empty.svg)
![High Security Icon](https://raw.githubusercontent.com/elementary/icons/master/status/48/security-high.svg)
![Revert Document Icon](https://raw.githubusercontent.com/elementary/icons/master/actions/24/document-revert.svg)
![Flag Icon](https://raw.githubusercontent.com/elementary/icons/master/actions/24/edit-flag.svg)
![Redo Icon](https://raw.githubusercontent.com/elementary/icons/master/actions/24/edit-redo.svg)
![Down Arrow Icon](https://raw.githubusercontent.com/elementary/icons/master/actions/24/go-down.svg)
![Reply All Icon](https://raw.githubusercontent.com/elementary/icons/master/actions/24/mail-reply-all.svg)
![Stop Process Icon](https://raw.githubusercontent.com/elementary/icons/master/actions/24/process-stop.svg)

An original set of vector icons designed specifically for [elementary OS](http://elementary.io) and its desktop environment: Pantheon.

## Building and Installation

You'll need the following dependencies:

* meson
* rsvg
* xcursorgen

Run `meson` to configure the build environment and then `ninja` to build

    meson build --prefix=/usr
    cd build
    ninja

To install, use `ninja install`

    sudo ninja install
