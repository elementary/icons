sizes = ['16', '24', '32', '48', '64', '128', 'symbolic']

links = [
    # The first argument is the original icon name,
    # the second is the link
    ['applications-internet', 'preferences-desktop-online-accounts'],
    ['multimedia-volume-control', 'preferences-desktop-sound'],
    ['preferences-desktop-locale', 'config-language'], # gnome language selector
    ['preferences-system', 'applications-system'],
    ['preferences-system-power', 'gnome-power-manager']
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
