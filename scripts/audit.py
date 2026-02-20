#!/usr/bin/env python3

# # Fd.o Icon Name Specification Audit
 
# ## Description:
# 
# Audit a Freedesktop.org icon specification-compatible theme against the icon
# naming specification, returning a csv report of what icons were included that are
# in-spec, what icons were included that are out-of-spec, and what icons were
# missing that are included in the spec.
 
# ## Dependencies:
#
# - requests (optional)
# - bs4 (optional)

import os, csv, argparse

parser = argparse.ArgumentParser(
    prog = "audit",
    description = "Audit a FreeDesktop.org compatible icon set against a specification"
)
parser.add_argument(
    "theme_path",
)
parser.add_argument(
    "-s",
    "--specification",
    dest="specf"
)
parser.add_argument(
    "-v",
    "--verbose",
    action="store_true"
)
parser.add_argument(
    "-r",
    "--report-name",
    dest="reportf",
    default="report"
)
args = parser.parse_args()

# make hrules pretty
try:
    view_width = os.get_terminal_size().columns
except:
    view_width = 80

# Check for optional dependencies to enable drawing the spec from the web.
# Otherwise fall back to included file
try:
    import requests
    from bs4 import BeautifulSoup
except:
    print("Couldn't find bs4 and requests dependencies, falling back to using spec file…")
    found_deps = False
else:
    print("Found bs4 and requests dependencies, pulling spec from the web…")
    found_deps = True

def get_soup(url: str) -> BeautifulSoup:
    page = session.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup

# This is kinda not great but it works
def parse_soup(soup: BeautifulSoup) -> list:
    result = []

    tables = soup.find_all("table")
    #remove the context description table, we don't care about it here
    tables.pop(0)
    for table in tables:
        rows = table.find_all("tr")
        for row in rows:
            text = row.contents
            name = text[0].text.strip().replace("\n", "")
            # skip the header row
            if name == "Name": continue
            result.append(name)

    return result

def get_iso_3166() -> list:
    result = []
    page = session.get("https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2")
    soup = BeautifulSoup(page.text, "html.parser")
    table = soup.find_all("table", class_="wikitable")[3].tbody
    rows = table.find_all("tr")
    for row in rows:
        code = row.text.strip().replace("\n", " ").split()[0]
        if code == "Code":
            continue
        result.append(f"flag-{code}")

    return result
        


def pad_list(iterable: list, length: int) -> list:
    extension_length = max(length - len(iterable), 0)
    if args.verbose: print(f"Extending list by {extension_length} elements")
    for _ in range(extension_length):
        iterable.append(None)

    return iterable

# Place this in a top level context so we don't have to pass it around
ignore_list = [] 

def populate_from_dir(dir: os.DirEntry) -> set:
    # This function is called recursively to populate a list
    tree = []

    for entry in os.scandir(dir.path):
        if entry.name in ignore_list:
            continue

        if entry.is_dir():
            if args.verbose: print(f"Found dir at {entry.path}, going deeper")
            # A spoonful of recursion to help the medicine go down
            tree.extend(populate_from_dir(entry))
        elif entry.name.endswith(".svg"):
            # We only check svg because that's the only type we use in elementary icons
            if args.verbose: print(f"Adding file {entry.path}, named {entry.name} to SubTree")
            tree.append(entry.name.removesuffix(".svg"))

    if args.verbose: print(f"The SubTree for Dir {dir.name} is {tree}")
    return list(set(tree))

# Load a text stream of the spec into a dictionary, where KEY=icon_name &
# VALUE=a bool denoting whether the file was found in the file tree
# Iterate over the list, checking to see if the specified file can be found.
specification = {}

if found_deps:
    url = "https://specifications.freedesktop.org/icon-naming-spec/latest/"
    headers = {
        'User-Agent': 'fdo-icon-name-spec-audit-script/1.0.0',
    }

    session = requests.Session()
    session.headers.update(headers)

    soup = get_soup(url)
    spec_list = parse_soup(soup)
    spec_list.extend(get_iso_3166())
    spec_list.remove("flag-aa")
    specification = specification.fromkeys(spec_list, False)
else:
    with open(args.specf, "r") as file:
        print(f"Loading specification in file: {args.specf}…")
        for line in file:
            if line.startswith(("//", " ", "\n")):
                continue
            specification.setdefault(line.remove_suffix("\n"), False)

print("Successfully loaded specification!")
symbolic_specification = specification.copy()

# Change the working dir to our target dir, to make it easier to traverse the
# tree. Try to find the file `.auditignore` in the dir root and load it into
# a list. Anything in this list doesn't exist as far as this script is
# concerned.
try:
    target_dir = args.theme_path 
except:
    print("Please specify a directory")
    exit()
else:
    # Save the cwd so we can switch back later
    script_dir = os.getcwd()
    dir = os.fspath(target_dir)
    os.chdir(dir)

try:
    with open(".auditignore", "r") as file:
        print("Found .auditignore file!")
        for line in file:
            ignore_list.append(line.strip())
except:
    print("No .auditignore file found in root")
else:
    print("Loaded .auditignore file!")
    if args.verbose: print(f"Values contained: {ignore_list}")

print('-' * view_width)

# Generate the contents of the relevant directory tree
contents = []

for entry in os.scandir():
    if entry.name not in ignore_list:
        if entry.is_dir():
            if args.verbose: print(f"Found dir at {entry.path}")
            sub_dir_tree = populate_from_dir(entry)
            contents.extend(sub_dir_tree)
        else:
            if entry.name.endswith(".svg"):
                if args.verbose: print(f"Adding file {entry.path} to tree")
                contents.append(entry.name.removesuffix(".svg"))

# remove duplicate names from the list
contents = list(set(contents))

if args.verbose:
    print(f"The full dirTree is {contents}")
    print('-' * view_width)

# Traverse the dir tree, checking whether the found file is in the spec list.
# This is so we don't have to traverse the entire dir tree of the set, just the
# specification list which is likely to be much smaller.

for entry in specification.keys():
    if entry in contents:
        print(f"Found {entry}")
        specification |= {entry: True}
    else:
        print(f"[!!] {entry} is missing!")


# Calculate percent spec coverage
total_entries = len(specification.keys())
existant_color_entries = list(specification.values()).count(True)

print(f"{existant_color_entries / total_entries * 100:.2f}% coverage of FD.o specification, color entries")

print('-' * view_width)

# Check whether things are included in symbolic entries
for entry in symbolic_specification.keys():
    extended_entry = entry + "-symbolic"
    if extended_entry in contents:
        print(f"Found {extended_entry}")
        symbolic_specification |= {entry: True}
    else:
        print(f"[!!] {extended_entry} is missing!")

existant_symbolic_entries = list(symbolic_specification.values()).count(True)

print(f"{existant_symbolic_entries / total_entries * 100:.2f}% coverage of FD.o specification, symbolic entries")

print('-' * view_width)

# Merging results and comparing all entries
color_results = list(specification.values())
symbolic_results = list(symbolic_specification.values())
results = []
for i, value in enumerate(color_results):
    results.append(symbolic_results[i] | value)

existant_entries = results.count(True)

print(f"{existant_entries / total_entries * 100:.2f}% coverage of FD.o specification, all entries")


print('-' * view_width)
os.chdir(script_dir)

# Write report file with Found, Missing, and Out-of-Spec information
spec_list = list(specification.keys())
found_entries = []
missing_entries = []
out_of_spec_entries = []

# We only look at the color entry results, as symbolic is not officially in the spec
for i, result in enumerate(color_results):
    # If the result is true, then it was found
    # If the result is false, then it is missing
    name = spec_list[i]
    if result:
        if args.verbose: print(f"Adding {name} to Found…")
        found_entries.append(name)
    else:
        if args.verbose: print(f"Adding {name} to Missing…")
        missing_entries.append(name)

# Now we want to go through all of the entries we found in the initial contents and
# point out those that aren't in the spec
for entry in contents:
    if entry not in spec_list and not entry.endswith("-symbolic"):
        if args.verbose: print(f"Adding {entry} to Out of Spec")
        out_of_spec_entries.append(entry)

# Pad all lists to be the same length, then zip all three lists together
length = max(len(found_entries), len(missing_entries), len(out_of_spec_entries))

found_entries = pad_list(found_entries, length)
missing_entries = pad_list(missing_entries, length)
out_of_spec_entries = pad_list(out_of_spec_entries, length)

zipped_lists = [(a, b, c) for a, b, c in zip(found_entries, missing_entries,
                                            out_of_spec_entries)]

with open(args.reportf, 'w', newline='') as file:
    fwriter = csv.writer(file)
    fwriter.writerow(["Found", "Missing", "Out of Spec"])
    fwriter.writerows(zipped_lists)
    print(f"Report written to {os.getcwd()}/{args.reportf}")

