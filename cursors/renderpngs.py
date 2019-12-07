#!/usr/bin/env python2
#
# SVGSlice
#
# Released under the GNU General Public License, version 2.
# Email Lee Braiden of Digital Unleashed at lee.b@digitalunleashed.com
# with any questions, suggestions, patches, or general uncertainties
# regarding this software.
#

usageMsg = """You need to add a layer called "slices", and draw rectangles on it to represent the areas that should be saved as slices.  It helps when drawing these rectangles if you make them translucent.

If you name these slices using the "id" field of Inkscape's built-in XML editor, that name will be reflected in the slice filenames.

Please remember to HIDE the slices layer before exporting, so that the rectangles themselves are not drawn in the final image slices."""

# How it works:
#
# Basically, svgslice just parses an SVG file, looking for the tags that define
# the slices should be, and saves them in a list of rectangles.  Next, it generates
# an XHTML file, passing that out stdout to Inkscape.  This will be saved by inkscape
# under the name chosen in the save dialog.  Finally, it calls
# inkscape again to render each rectangle as a slice.
#
# Currently, nothing fancy is done to layout the XHTML file in a similar way to the
# original document, so the generated pages is essentially just a quick way to see
# all of the slices in once place, and perhaps a starting point for more layout work.
#

from optparse import OptionParser

optParser = OptionParser()
optParser.add_option('-d','--debug',action='store_true',dest='debug',help='Enable extra debugging info.')
optParser.add_option('-t','--test',action='store_true',dest='testing',help='Test mode: leave temporary files for examination.')
optParser.add_option('-p','--sliceprefix',action='store',dest='sliceprefix',help='Specifies the prefix to use for individual slice filenames.')

from xml.sax import saxutils, make_parser, SAXParseException, handler
from xml.sax.handler import feature_namespaces
import os, sys, tempfile, shutil

svgFilename = None


def dbg(msg):
	if options.debug:
		sys.stderr.write(msg)

def cleanup():
	if svgFilename != None and os.path.exists(svgFilename):
		os.unlink(svgFilename)

def fatalError(msg):
	sys.stderr.write(msg)
	cleanup()
	sys.exit(20)


class SVGRect:
	"""Manages a simple rectangular area, along with certain attributes such as a name"""
	def __init__(self, x1,y1,x2,y2, name=None):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.name = name
		dbg("New SVGRect: (%s)" % name)
	
	def renderFromSVG(self, svgFName, sliceFName):
		rc = os.system('inkscape --without-gui --export-id="%s" --export-png="pngs/24x24/%s" "%s"' % (self.name, sliceFName, svgFName))
		if rc > 0:
			fatalError('ABORTING: Inkscape failed to render the slice.')
		rc = os.system('inkscape -w 32 -h 32 --without-gui --export-id="%s" --export-png="pngs/32x32/%s" "%s"' % (self.name, sliceFName, svgFName))
		if rc > 0:
			fatalError('ABORTING: Inkscape failed to render the slice.')
		rc = os.system('inkscape -w 48 -h 48 --without-gui --export-id="%s" --export-png="pngs/48x48/%s" "%s"' % (self.name, sliceFName, svgFName))
		if rc > 0:
			fatalError('ABORTING: Inkscape failed to render the slice.')
#		rc = os.system('inkscape -w 128 -h 128 --without-gui --export-id="%s" --export-png="pngs/128x128/%s" "%s"' % (self.name, sliceFName, svgFName))
#		if rc > 0:
#			fatalError('ABORTING: Inkscape failed to render the slice.')


class SVGHandler(handler.ContentHandler):
	"""Base class for SVG parsers"""
	def __init__(self):
		self.pageBounds = SVGRect(0,0,0,0)

	def isFloat(self, stringVal):
		try:
			return (float(stringVal), True)[1]
		except (ValueError, TypeError), e:
			return False
	
	def parseCoordinates(self, val):
		"""Strips the units from a coordinate, and returns just the value."""
		if val.endswith('px'):
			val = float(val.rstrip('px'))
		elif val.endswith('pt'):
			val = float(val.rstrip('pt'))
		elif val.endswith('cm'):
			val = float(val.rstrip('cm'))
		elif val.endswith('mm'):
			val = float(val.rstrip('mm'))
		elif val.endswith('in'):
			val = float(val.rstrip('in'))
		elif val.endswith('%'):
			val = float(val.rstrip('%'))
		elif self.isFloat(val):
			val = float(val)
		else:
			fatalError("Coordinate value %s has unrecognised units.  Only px,pt,cm,mm,and in units are currently supported." % val)
		return val
	
	def startElement_svg(self, name, attrs):
		"""Callback hook which handles the start of an svg image"""
		dbg('startElement_svg called')
		width = attrs.get('width', None)
		height = attrs.get('height', None)
		self.pageBounds.x2 = self.parseCoordinates(width)
		self.pageBounds.y2 = self.parseCoordinates(height)
	
	def endElement(self, name):
		"""General callback for the end of a tag"""
		dbg('Ending element "%s"' % name)


class SVGLayerHandler(SVGHandler):
	"""Parses an SVG file, extracing slicing rectangles from a "slices" layer"""
	def __init__(self):
		SVGHandler.__init__(self)
		self.svg_rects = []
		self.layer_nests = 0
	
	def inSlicesLayer(self):
		return (self.layer_nests >= 1)
	
	def add(self, rect):
		"""Adds the given rect to the list of rectangles successfully parsed"""
		self.svg_rects.append(rect)
	
	def startElement_layer(self, name, attrs):
		"""Callback hook for parsing layer elements
		
		Checks to see if we're starting to parse a slices layer, and sets the appropriate flags.  Otherwise, the layer will simply be ignored."""
		dbg('found layer: name="%s" id="%s"' % (name, attrs['id']))
		if attrs.get('inkscape:groupmode', None) == 'layer':
			if self.inSlicesLayer() or attrs['inkscape:label'] == 'slices':
				self.layer_nests += 1
	
	def endElement_layer(self, name):
		"""Callback for leaving a layer in the SVG file
	
		Just undoes any flags set previously."""
		dbg('leaving layer: name="%s"' % name)
		if self.inSlicesLayer():
			self.layer_nests -= 1
	
	def startElement_rect(self, name, attrs):
		"""Callback for parsing an SVG rectangle
		
		Checks if we're currently in a special "slices" layer using flags set by startElement_layer().  If we are, the current rectangle is considered to be a slice, and is added to the list of parsed
		rectangles.  Otherwise, it will be ignored."""
		if self.inSlicesLayer():
			x1 = self.parseCoordinates(attrs['x'])
			y1 = self.parseCoordinates(attrs['y'])
			x2 = self.parseCoordinates(attrs['width']) + x1
			y2 = self.parseCoordinates(attrs['height']) + y1
			name = attrs['id']
			rect = SVGRect(x1,y1, x2,y2, name)
			self.add(rect)
	
	def startElement(self, name, attrs):
		"""Generic hook for examining and/or parsing all SVG tags"""
		if options.debug:
			dbg('Beginning element "%s"' % name)
		if name == 'svg':
			self.startElement_svg(name, attrs)
		elif name == 'g':
			# inkscape layers are groups, I guess, hence 'g'
			self.startElement_layer(name, attrs)
		elif name == 'rect':
			self.startElement_rect(name, attrs)
	
	def endElement(self, name):
		"""Generic hook called when the parser is leaving each SVG tag"""
		dbg('Ending element "%s"' % name)
		if name == 'g':
			self.endElement_layer(name)
	
	def generateXHTMLPage(self):
		"""Generates an XHTML page for the SVG rectangles previously parsed."""
		write = sys.stdout.write
		write('<?xml version="1.0" encoding="UTF-8"?>\n')
		write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "DTD/xhtml1-strict.dtd">\n')
		write('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n')
		write('    <head>\n')
		write('        <title>Sample SVGSlice Output</title>\n')
		write('    </head>\n')
		write('    <body>\n')
		write('        <p>Sorry, SVGSlice\'s XHTML output is currently very basic.  Hopefully, it will serve as a quick way to preview all generated slices in your browser, and perhaps as a starting point for further layout work.  Feel free to write it and submit a patch to the author :)</p>\n')
		
		write('        <p>')
		for rect in self.svg_rects:
			write('            <img src="%s" alt="%s (please add real alternative text for this image)" longdesc="Please add a full description of this image" />\n' % (sliceprefix + rect.name + '.png', rect.name))
		write('        </p>')
		
		write('<p><a href="http://validator.w3.org/check?uri=referer"><img src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0!" height="31" width="88" /></a></p>')
		
		write('    </body>\n')
		write('</html>\n')


if __name__ == '__main__':
	# parse command line into arguments and options
	(options, args) = optParser.parse_args()

	if len(args) != 1:
		fatalError("\nCall me with the SVG as a parameter.\n\n")
	originalFilename = args[0]

	svgFilename = originalFilename + '.svg'
	shutil.copyfile(originalFilename, svgFilename)
	
	# setup program variables from command line (in other words, handle non-option args)
	basename = os.path.splitext(svgFilename)[0]
	
	if options.sliceprefix:
		sliceprefix = options.sliceprefix
	else:
		sliceprefix = ''
	
	# initialise results before actually attempting to parse the SVG file
	svgBounds = SVGRect(0,0,0,0)
	rectList = []
	
	# Try to parse the svg file
	xmlParser = make_parser()
	xmlParser.setFeature(feature_namespaces, 0)
	
	# setup XML Parser with an SVGLayerHandler class as a callback parser ####
	svgLayerHandler = SVGLayerHandler()
	xmlParser.setContentHandler(svgLayerHandler)
	try:
		xmlParser.parse(svgFilename)
	except SAXParseException, e:
		fatalError("Error parsing SVG file '%s': line %d,col %d: %s.  If you're seeing this within inkscape, it probably indicates a bug that should be reported." % (svgfile, e.getLineNumber(), e.getColumnNumber(), e.getMessage()))
	
	# verify that the svg file actually contained some rectangles.
	if len(svgLayerHandler.svg_rects) == 0:
		fatalError("""No slices were found in this SVG file.  Please refer to the documentation for guidance on how to use this SVGSlice.  As a quick summary:

""" + usageMsg)
	else:
		dbg("Parsing successful.")
	
	#svgLayerHandler.generateXHTMLPage()
	
	# loop through each slice rectangle, and render a PNG image for it
	for rect in svgLayerHandler.svg_rects:
		sliceFName = sliceprefix + rect.name + '.png'
		
		dbg('Saving slice as: "%s"' % sliceFName)
		rect.renderFromSVG(svgFilename, sliceFName)

	cleanup()

	dbg('Slicing complete.')
