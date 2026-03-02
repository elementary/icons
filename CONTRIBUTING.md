## Contributing Icons
It is recommended to use the free and open source [Inkscape](http://inkscape.org) vector editor to create elementary icons. Any and all icons must follow the elementary [Icon Design Guidelines](https://docs.elementary.io/hig/reference/iconography).

An elementary color palette is provided, it is recommended to copy it into your Inkscape settings before you get started.

_(Run these from the root of the icons repo)_
```bash
cp data/elementary.gpl ~/.config/inkscape/palettes/
```

For flatpak installations, use one of the following.

```bash
# Local
cp data/elementary.gpl ~/.local/share/flatpak/app/org.inkscape.Inkscape/current/active/files/share/inkscape/palettes/
```

To contribute to the elementary icon set, open a pull request to this repository with your icon(s).

It is strongly encouraged to vacuum all vectors with [Inkscape](http://inkscape.org). This keeps the repository lean, clean, and fast for everyone. For convenience, a git pre-commit hook is included. To install, run these commands from your local repository folder:
```bash
$ cp pre-commit .git/hooks/
$ chmod +x .git/hooks/pre-commit
```

## Not a Universal Icon Set
Since this set is designed specifically for elementary OS, pull requests to add icons or symlinks that are specific to other desktop environments (such as `xfce-*` or `gnome-*` named icons) will be rejected.

Use of icon names in line with the [FreeDesktop.Org Icon Naming Specification](http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html) is encouraged.

To monitor coverage, an auditing python script is included under `/scripts`. While this
script can be used without any extra dependencies, setting up a virtual
environment and installing `requests` and `BeautifulSoup4` enables functionality
that ensures all resources pulled are as current as possible. To do this:

1. If not already installed, run `apt install python3 python3.12-venv`
2. From the repository root, run `python3 -m venv .venv`. This sets up a python
   virtual environment in a hidden folder, scoped to this repository. 
3. To activate the venv, run `source .venv/bin/activate`.
4. To install `requests` and `BeautifulSoup4`, run `python3 -m pip install requests
   BeautifulSoup4`
5. Run the script with `python3 scripts/audit.py <path to theme folder>`

Note that for accurate results, the fully built theme directory has to be
targeted, not the development files. Many symlinks are created by the build
system, so will not be picked up if this script is run on the development files.

## Third-Party Brand Preservation
elementary icons do not attempt to supply icons for third-party apps. Pull requests to add icons or symbolic links that would overwrite the branding of third-party apps will be rejected.
