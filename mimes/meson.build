mime_sizes = ['16', '24', '32', '48', '64', '128']

mime_links = [
    # The first argument is the original icon name,
    # the second is the link
    ['text-x-makefile', 'text-x-cmake'],
    ['text-x-makefile', 'text-x-meson']
]

foreach link : mime_links
    foreach size: mime_sizes
        meson.add_install_script(
            symlink,
            '--src', icon_dir / 'mimes' / size / link[0] + '.svg',
            '--dest', icon_dir / 'mimes' / size / link[1] + '.svg'
        )
    endforeach
endforeach
