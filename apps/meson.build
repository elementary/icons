sizes = ['16', '24', '32', '48', '64', '128', 'symbolic']

links = [
    # The first argument is the original icon name,
    # the second is the link
    ['accessories-screenshot-tool', 'applets-screenshooter'],
]

foreach link : links
    foreach size: sizes
        meson.add_install_script(
            symlink,
            '--src', icon_dir / 'apps' / size / link[0] + '.svg',
            '--dest', icon_dir / 'apps' / size / link[1] + '.svg'
        )
    endforeach
endforeach
