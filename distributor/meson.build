hicolor_dir = join_paths(get_option('datadir'), 'icons', 'hicolor')

icon_sizes = ['16', '24', '32', '48', '64', '128']

foreach i : icon_sizes
    install_data(
        i + '.svg',
        install_dir: join_paths(hicolor_dir, i + 'x' + i, 'places'),
        rename: meson.project_name() + '.svg'
    )
    install_data(
        i + '.svg',
        install_dir: join_paths(hicolor_dir, i + 'x' + i + '@2', 'places'),
        rename: 'distributor-logo.svg'
    )
endforeach

install_data(
    'symbolic.svg',
    install_dir: join_paths(hicolor_dir, 'symbolic', 'places'),
    rename: 'distributor-logo-symbolic.svg'
)

