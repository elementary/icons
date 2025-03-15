sizes = ['16', '24', '32', '48', '64', '128', 'symbolic']

links = [
    # The first argument is the original icon name,
    # the second is the link
    ['folder', 'inode-directory'],
    ['folder-open', 'folder-drag-accept'],
    ['folder-open', 'user-desktop-open'],
    ['folder', 'user-desktop']
]

foreach link : links
    foreach size: sizes
        origin = link[0]
        destination = link[1]

        if (size == 'symbolic')
            origin += '-symbolic'
            destination += '-symbolic'
        endif

        if (fs.exists(size / origin + '.svg'))
            install_symlink(
                destination  + '.svg',
                install_dir: icon_dir / 'categories' / size,
                pointing_to: origin + '.svg',
            )
        else
            warning('@0@ does not exist'.format (size / origin))
        endif
    endforeach
endforeach
