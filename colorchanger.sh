#!/bin/bash
# change colors in svg icon themes
# usage ./this_file.sh '#000000' '#ffffff'
# in the theme dir

for file in */*/*.svg; do
	mv $file $file.bak
	sed 's/'$1'/'$2'/g' $file.bak > $file
	echo 'file '$file' processed'
	#rm -f $file.bak
done
