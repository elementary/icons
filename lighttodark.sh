#!/bin/bash
# change colors in svg icon themes
# in the theme dir

for file in */*.svg; do
	mv $file $file.bak
	# shadow color
	sed 's/'#ffffff'/'#030303'/g' $file.bak > $file
	# gradient colors
	sed 's/'#000000'/'#ffffff'/g' $file.bak > $file	
	sed 's/'#363636'/'#e6e6e6'/g' $file.bak > $file
	# info colors
	sed 's/'#49a3d2'/'#5ac9ff'/g' $file.bak > $file
	sed 's/'#1b5699'/'#216bbd'/g' $file.bak > $file

	echo 'file '$file' processed'
	#rm -f $file.bak
done
