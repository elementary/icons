# Scripts/Icon Tools

## Naming Spec Tools

Icons in many Linux desktop environments use the naming specifications from FreeDesktop.org

https://specifications.freedesktop.org/icon-naming/latest/


> The Icon Theme Specification has been in use now for a while, in several desktops, including KDE and Gnome. However, there has never been any centralized direction on how to name the icons that are available for use by applications, when creating a theme. This has meant that artists have historically had to duplicate many icons, in order for their themes to work across desktop environments.

> This specification aims to solve this problem, by laying out a standard naming scheme for icon creation, as well as providing a minimal list of must have icons. Addendums to this specification will provide additional icon lists for extended sets, such as devices and MIME types.

The specs are available in the FreeDesktop.org Gitlab instance here:

https://gitlab.freedesktop.org/xdg/default-icon-theme/-/raw/master/spec/icon-naming-spec.xml

This directory contains a script called `naming_spec_tools.py` that will attempt to pull down this file, parse the icon names and the different sections, and then build a JSON structure with all the spec sections and icon names. This structure is saved in `icon-naming-spec.json`.

### Usage

```shell
$ python3 naming_spec_tools.py -h
usage: naming_spec_tools.py [-h] [-s] [-v]

Tools for working with the Freedesktop.org Icons Naming Spec.By default, downloads the spec and
formats as JSON for use in other tools.

options:
  -h, --help     show this help message and exit
  -s, --save     Save the content of the naming spec Docbook file to icon-naming-spec.xml
  -v, --verbose  Enable verbose output
```

### Script Output

The script generates the file `icon-naming-spec.json`:

```json
{
  "actions": {
    "section": "Standard Action Icons",
    "entries": [
      {
        "name": "address-book-new",
        "description": "The icon used for the action to create a new address book."
      },
      {
        "name": "application-exit",
        "description": "The icon used for exiting an application. Typically this is seen\nin the application's menus as File->Quit."
      },
      {
        "name": "appointment-new",
        "description": "The icon used for the action to create a new appointment\nin a calendaring application."
      },
      // ...
    ]
  },
  // ...
}
```

### Save or Update the local DocBook file

Passing `-s|--save` to the script will save the fetched file in `icon-naming-spec.xml` locally so we have a reference copy.

```shell
$ cd scripts/
$ python3 naming_spec_tools.py -s
```

Both icon spec files (when updated) should be committed so that they can be used by other tools.