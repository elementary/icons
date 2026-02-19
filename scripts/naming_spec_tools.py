#!/usr/bin/env python3
"""
This script can be used to generate a version of the FreeDesktop.org Icon
Naming Spec as JSON for use in Elementary theme development and theme auditing.

The script captures the icon set sections and all icon entries.

The BeautifulSoup (bs4) python library is required, and processing will stop
and print a message saying so if the library is not available in the current
python environment.
"""

import argparse
import json
import sys
from urllib.request import urlopen
from collections import OrderedDict

SPEC_URL = "https://gitlab.freedesktop.org/xdg/default-icon-theme/-/raw/master/spec/icon-naming-spec.xml?ref_type=heads"
SPEC_XML = "icon-naming-spec.xml"
SPEC_JSON = "icon-naming-spec.json"


def check_deps() -> bool:
    """
    Confirm we have access to Beautiful Soup for parsing the
    DocBook spec file.
    """
    try:
        from bs4 import BeautifulSoup  # noqa
    except ImportError:
        return False
    return True


def fetch_spec(url: str) -> str | None:
    try:
        with urlopen(url) as resp:
            spec_content = resp.read()

    except Exception as e:
        print(
            f"Could not load icons-naming-spec.xml from {SPEC_URL.replace('https://', '')}, {e}"
        )
        return None

    return spec_content.decode("utf8")


def process_spec_docbook(content, verbose=False):
    from bs4 import BeautifulSoup

    # 'xml' instead of 'html' for DocBook
    soup = BeautifulSoup(content, "xml")

    tables = soup.find_all("table")

    # Use a dictionary so that later we can easily
    # get a subset of icon names based on section

    # OrderedDict preserves the order to make it easier
    # to read/understand later.
    data = OrderedDict()

    for table in tables:
        table_id = table.attrs.get("id")
        if not table_id:
            continue

        title = table.find("title")
        if verbose:
            print(f"Found section: {title.text} ({table_id})")

        data[table_id] = {"section": title.text, "entries": []}
        entries = data[table_id]["entries"]

        for tgroup in table.find_all("tgroup"):
            tbody = tgroup.find("tbody")
            if tbody:
                for row in tbody.find_all("row"):
                    name, description = [
                        entry.get_text(strip=True) for entry in row.find_all("entry")
                    ]

                    entries.append(
                        OrderedDict(
                            {
                                "name": name,
                                "description": description,
                            }
                        )
                    )
    return data


def main(args):
    if args.verbose:
        print("Checking dependencies...")

    if not check_deps():
        print("Couldn't find bs4 dependencies.")
        print("Use local spec file (icons-naming-spec.json)")

        sys.exit(1)

    print("Fetching icons-naming-spec.xml from FreeDesktop.org")
    if args.verbose:
        print(SPEC_URL)

    spec_content = fetch_spec(SPEC_URL)

    if args.save_local:
        print(f"Updating local file: {SPEC_XML}")
        with open(SPEC_XML, "w") as spec_file:
            spec_file.write(spec_content)

    print("Extracting spec data")
    data = process_spec_docbook(spec_content)

    print(f"Saving JSON spec file to {SPEC_JSON}")
    with open(SPEC_JSON, "w") as spec_json:
        json.dump(data, spec_json, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="naming_spec_tools.py",
        description=(
            "Tools for working with the Freedesktop.org Icons Naming Spec. "
            "By default, downloads the spec and formats as JSON for use in other tools."
        ),
    )

    parser.add_argument(
        "-s",
        "--save",
        dest="save_local",
        action="store_true",
        help=f"Save the content of the naming spec Docbook file to {SPEC_XML}",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )

    args = parser.parse_args()

    main(args)
