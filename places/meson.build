sizes = ['16', '24', '32', '48', '64', '128', 'symbolic']

links = [
    # The first argument is the original icon name,
    # the second is the link
    ['folder-documents-open', 'folder-documents-drag-accept'],
    ['folder-download-open', 'folder-download-drag-accept'],
    ['folder', 'inode-directory'],
    ['folder-music-open', 'folder-music-drag-accept'],
    ['folder-open', 'folder-drag-accept'],
    ['folder-open', 'user-desktop-open'],
    ['folder-pictures-open', 'folder-pictures-drag-accept'],
    ['folder-pictures-open', 'folder-pictures-drag-accept'],
    ['folder-publicshare-open', 'folder-publicshare-drag-accept'],
    ['folder-remote', 'gtk-network'],
    ['folder-remote-open', 'folder-remote-drag-accept'],
    ['folder-tag', 'tag'],
    ['folder-templates-open', 'folder-templates-drag-accept'],
    ['folder', 'user-desktop'],
    ['folder-videos-open', 'folder-videos-drag-accept'],
    ['library-music', 'folder-music'],
    ['user-home-open', 'user-home-drag-accept']
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
                install_dir: icon_dir / 'places' / size,
                pointing_to: origin + '.svg',
            )
        else
            warning('@0@ does not exist'.format (size / origin))
        endif
    endforeach
endforeach


links = [
    # The first argument is the original directory,
    # The second is the original icon name,
    # the third is the link
    ['actions', 'edit-find', 'start-here'],
    ['actions', 'help-about', 'user-bookmarks'],
    ['actions', 'mail-send', 'mail-sent'],
    ['devices', 'video-display', 'network-server']
]

foreach link : links
    foreach size: sizes
        directory = link[0]
        origin = link[1]
        destination = link[2]

        if (size == 'symbolic')
            origin += '-symbolic'
            destination += '-symbolic'
        endif

        if (fs.exists(meson.project_source_root() / directory / size / origin + '.svg'))
            install_symlink(
                destination  + '.svg',
                install_dir: icon_dir / 'places' / size,
                pointing_to: '..' / '..' / directory / size / origin + '.svg',
            )
        else
            warning('@0@ does not exist'.format (size / origin))
        endif
    endforeach
endforeach
