#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description='Create a symlink')
parser.add_argument('--src', nargs=1)
parser.add_argument('--dest', nargs=1)
args = parser.parse_args()

inst_prefix = os.environ['MESON_INSTALL_PREFIX']
dest_prefix = os.environ['MESON_INSTALL_DESTDIR_PREFIX']

src = os.path.basename(os.path.join(inst_prefix, args.src[0]))
dest = os.path.join(dest_prefix, args.dest[0])

if os.path.exists(dest):
    if os.path.isdir(dest):
        print('Folder "' + dest + '" already exists, no symlink will be created')
    else:
        print('File "' + dest + '" already exists, no symlink will be created')
else:
    print('Linking ' + dest + ' to ' + src)
    os.symlink(src, dest)
