import os, csv
from sys import argv

ignoreList = []

if argv[1] == "-h":
    print("USAGE: python (-O) audit.py <path-to-icon-spec-file> <path-to-root-dir-of-theme> (<report-file-name>)")
    exit()

try:
    viewWidth = os.get_terminal_size().columns
except:
    viewWidth = 80

try:
    outputFName = argv[4]
except:
    outputFName = "report.csv"

def padList(iterable: list, length: int) -> list:
    extensionLength = max(length - len(iterable), 0)
    if __debug__: print(f"Extending list by {extensionLength} elements")
    for _ in range(extensionLength):
        iterable.append(None)

    return iterable

def populateFromDir(dir: os.DirEntry) -> set:
    # This function is called recursively to populate a list
    tree = []

    for entry in os.scandir(dir.path):
        if entry.name not in ignoreList:
            if entry.is_dir():
                if __debug__: print(f"Found dir at {entry.path}, going deeper")
                # A spoonful of recursion to help the medicine go down
                tree.extend(populateFromDir(entry))
            else:
                if __debug__: print(f"Adding file {entry.path}, named {entry.name} to SubTree")
                tree.append(entry.name.removesuffix(".svg"))

    if __debug__: print(f"The SubTree for Dir {dir.name} is {tree}")
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
    # Save the cwd so we can switch back later
    scriptDir = os.getcwd()
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
    if __debug__: print(f"Values contained: {ignoreList}")

print('-' * viewWidth)

# Generate the contents of the relevant directory tree
contents = []

for entry in os.scandir():
    if entry.name not in ignoreList:
        if entry.is_dir():
            if __debug__: print(f"Found dir at {entry.path}")
            subDirTree = populateFromDir(entry)
            contents.extend(subDirTree)
        else:
            if __debug__: print(f"Adding file {entry.path} to tree")
            if entry.name.endswith(".svg"):
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
existantColorEntries = list(specification.values()).count(True)

print(f"{existantColorEntries / totalEntries * 100:.2f}% coverage of FD.o specification, color entries")

print('-' * viewWidth)

# Check whether things are included in symbolic entries
for entry in symbolicSpecification.keys():
    extendedEntry = entry + "-symbolic"
    if extendedEntry in contents:
        print(f"Found {extendedEntry}")
        symbolicSpecification |= {entry: True}
    else:
        print(f"[!!] {extendedEntry} is missing!")

existantSymbolicEntries = list(symbolicSpecification.values()).count(True)

print(f"{existantSymbolicEntries / totalEntries * 100:.2f}% coverage of FD.o specification, symbolic entries")

print('-' * viewWidth)

# Merging results and comparing all entries
colorResults = list(specification.values())
symbolicResults = list(symbolicSpecification.values())
results = []
for i, value in enumerate(colorResults):
    results.append(symbolicResults[i] | value)

existantEntries = results.count(True)

print(f"{existantEntries / totalEntries * 100:.2f}% coverage of FD.o specification, all entries")


print('-' * viewWidth)
os.chdir(scriptDir)

# Write report file with Found, Missing, and Out-of-Spec information
specList = list(specification.keys())
foundEntries = []
missingEntries = []
outOfSpecEntries = []

# We only look at the color entry results, as symbolic is not officially in the spec
for i, result in enumerate(colorResults):
    # If the result is true, then it was found
    # If the result is false, then it is missing
    name = specList[i]
    if result:
        if __debug__: print(f"Adding {name} to Found...")
        foundEntries.append(name)
    else:
        if __debug__: print(f"Adding {name} to Missing...")
        missingEntries.append(name)

# Now we want to go through all of the entries we found in the initial contents and
# point out those that aren't in the spec
for entry in contents:
    if entry not in specList and not entry.endswith("-symbolic"):
        if __debug__: print(f"Adding {entry} to Out of Spec")
        outOfSpecEntries.append(entry)

# Pad all lists to be the same length, then zip all three lists together
length = max(len(foundEntries), len(missingEntries), len(outOfSpecEntries))

foundEntries = padList(foundEntries, length)
missingEntries = padList(missingEntries, length)
outOfSpecEntries = padList(outOfSpecEntries, length)

zippedLists = [(a, b, c) for a, b, c in zip(foundEntries, missingEntries,
                                            outOfSpecEntries)]

with open(outputFName, 'w', newline='') as file:
    fWriter = csv.writer(file)
    fWriter.writerow(["Found", "Missing", "Out of Spec"])
    fWriter.writerows(zippedLists)
    print(f"Report written to {os.getcwd()}/{outputFName}")

