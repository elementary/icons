import sys
import xml.etree.ElementTree as ET

svg = "{http://www.w3.org/2000/svg}"
fType = sys.argv[1]     # Type file
fBase = sys.argv[2]     # Base file
fTarget = sys.argv[3]   # Target file

# All svg elements and definitions are copied from file 1 to file 2
# File 1's contents will appear on top of File 2's contents, so File 2 should only be the base shape
# It is assumed that both files have the same dimensions, and that elements are aligned properly

tTree = ET.parse(fType)
tRoot = tTree.getroot()
defs = tRoot.find(f"{svg}defs")

# Find all elements in the svg namespace, then if they aren't defs or metadata, copy them
svgElements = tRoot.findall(f"{svg}*")
unwantedTags = [f"{svg}metadata", f"{svg}defs"]
shapes = []
for element in svgElements:
    if element.tag not in unwantedTags:
        shapes.append(element)

# Now we take all of those defs and shapes, then add them to the tree of our base file
bTree = ET.parse(fBase)
bRoot = bTree.getroot()
bDefs = bRoot.find(f"{svg}defs")

for element in defs.iter():
    bDefs.append(element)

bRoot.extend(shapes)

# Write out the tree to the target filename
with open(fTarget, 'w') as file:
    bTree.write(file)
