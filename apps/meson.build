sizes = ['16', '24', '32', '48', '64', '128']

links = [
    # The first argument is the original icon name,
    # the second is the link
    ['accessories-screenshot-tool', 'applets-screenshooter'],
]

foreach link : links
    foreach size: sizes
        install_symlink(
            link[1] + '.svg',
            install_dir: icon_dir / 'apps' / size,
            pointing_to: link[0] + '.svg',
        )
    endforeach
endforeach
