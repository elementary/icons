import os
from sys import argv

ignoreList = []

try:
    viewWidth = os.get_terminal_size().columns
except:
    viewWidth = 80

def populateFromDir(dir: os.DirEntry) -> set:
    # This function is called recursively to populate a list
    tree = []

    for entry in os.scandir(dir.path):
        if entry.name not in ignoreList:
            if entry.is_dir():
                if __debug__:
                    print(f"Found dir at {entry.path}, going deeper")
                # A spoonful of recursion to help the medicine go down
                tree.extend(populateFromDir(entry))
            else:
                if __debug__:
                    print(f"Adding file {entry.path}, named {entry.name} to SubTree")
                tree.append(entry.name.removesuffix(".svg"))

    if __debug__:
        print(f"The SubTree for Dir {dir.name} is {tree}")
    return list(set(tree))


# Load a text stream of the spec into a dictionary, where KEY=icon_name &
# VALUE=a bool denoting whether the file was found in the file tree
# Iterate over the list, checking to see if the specified file can be found.
fName = argv[1]
specification = {}

with open(fName, "r") as file:
    print(f"Loading specification in file: {fName}...")
    for line in file:
        if line.startswith(("//", " ", "\n")):
            continue
        specification.setdefault(line.removesuffix("\n"), False)

symbolicSpecification = specification.copy()
print("Successfully loaded specfication file!")

# Change the working dir to our target dir, to make it easier to traverse the
# tree. Try to find the file `.auditignore` in the dir root and load it into
# a list. Anything in this list doesn't exist as far as this script is
# concerned.
try:
    targetDir = argv.pop(2)
except:
    print("Please specify a directory")
    exit()
else:
    dir = os.fspath(targetDir)
    os.chdir(dir)

try:
    with open(".auditignore", "r") as file:
        print("Found .auditignore file!")
        for line in file:
            ignoreList.append(line.removesuffix("\n"))
except:
    print("No .auditignore file found in root")
else:
    print("Loaded .auditignore file!")
    if __debug__:
        print(f"Values contained: {ignoreList}")

print('-' * viewWidth)

# Generate the contents of the relevant directory tree
contents = []


for entry in os.scandir():
    if entry.name not in ignoreList:
        if entry.is_dir():
            if __debug__:
                print(f"Found dir at {entry.path}")
            subDirTree = populateFromDir(entry)
            contents.extend(subDirTree)
        else:
            if __debug__:
                print(f"Adding file {entry.path} to tree")
            contents.append(entry.name.removesuffix(".svg"))

# remove duplicate names from the list
contents = list(set(contents))

if __debug__:
    print(f"The full dirTree is {contents}")
    print('-' * viewWidth)

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
totalEntries = len(specification.keys())
existantColorEntries = 0

for value in specification.values():
    # Increase the number of existant entries if value=True
    existantColorEntries += 1 if value else 0

print(f"{existantColorEntries / totalEntries * 100:.2f}% coverage of FD.o specification, color entries")

print('-' * viewWidth)

existantSymbolicEntries = 0

# Check whether things are included in symbolic entries
for entry in symbolicSpecification.keys():
    extendedEntry = entry + "-symbolic"
    if extendedEntry in contents:
        print(f"Found {extendedEntry}")
        symbolicSpecification |= {entry: True}
    else:
        print(f"[!!] {extendedEntry} is missing!")


for value in symbolicSpecification.values():
    # Increase the number of existant entries if value=True
    existantSymbolicEntries += 1 if value else 0

print(f"{existantSymbolicEntries / totalEntries * 100:.2f}% coverage of FD.o specification, symbolic entries")

print('-' * viewWidth)

# Merging results and comparing all entries
colorResults = list(specification.values())
symbolicResults = list(symbolicSpecification.values())
results = []
for i, value in enumerate(colorResults):
    results.append(symbolicResults[i] | value)

existantEntries = 0

for value in results:
    # Increase the number of existant entries if value=True
    existantEntries += 1 if value else 0

print(f"{existantEntries / totalEntries * 100:.2f}% coverage of FD.o specification, all entries")

