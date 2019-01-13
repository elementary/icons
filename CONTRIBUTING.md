## Contributing Icons
To contribute to the elementary icon set, open a pull request to this repository with your icon(s).
All icons must follow the elementary [Icon Design Guidelines](http://elementary.io/docs/human-interface-guidelines#iconography).

It is recommended to use the free and open source [Inkscape](http://inkscape.org) vector editor to create elementary icons.

An [elementary color palette](elementary.gpl) ([rendered version](https://elementary.io/docs/human-interface-guidelines#color)) is provided.
You can copy it into your Inkscape settings with the following command:
```bash
$ cp elementary.gpl ~/.config/inkscape/palettes/
```

It is strongly encouraged to vacuum all vectors with Inkscape. This keeps the repository lean, clean, and fast for everyone.
For convenience, a git pre-commit hook to do so is included in this repo. To install it, run these commands from your local repository folder:
```bash
$ cp pre-commit .git/hooks/
$ chmod +x .git/hooks/pre-commit
```

## Not a Universal Icon Set
Since this set is designed specifically for elementary OS, pull requests to add icons or symlinks that are specific to other desktop environments (such as `xfce-*` or `gnome-*` named icons) will be rejected.

Use of icon names in line with the [FreeDesktop.Org Icon Naming Specification](http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html) is encouraged.

## Third-Party Brand Preservation
elementary icons do not attempt to supply icons for third-party apps. Pull requests to add icons or symbolic links that would overwrite the branding of third-party apps will be rejected.
