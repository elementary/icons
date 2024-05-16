sizes = ['16', '24', '32', '48', '64', '128']

links = [
    # The first argument is the original icon name,
    # the second is the link
    ['applications-internet', 'preferences-desktop-online-accounts'],
    ['multimedia-volume-control', 'preferences-desktop-sound'],
    ['preferences-desktop-locale', 'config-language'], # gnome language selector
    ['preferences-system-power', 'gnome-power-manager']
]

foreach link : links
    foreach size: sizes
        if (fs.exists(link[1] + '.svg'))
            install_symlink(
                link[1] + '.svg',
                install_dir: icon_dir / 'apps' / size,
                pointing_to: link[0] + '.svg',
            )
        endif
    endforeach
endforeach
