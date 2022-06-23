i18n.merge_file(
    input: 'icons.appdata.xml.in',
    output: meson.project_name() + '.appdata.xml',
    po_dir: meson.source_root() / 'po',
    install_dir: get_option('datadir') / 'metainfo',
    install: true
)

if (get_option ('palettes'))
    install_data(
        'elementary.gpl',
        install_dir: join_paths (get_option('datadir'), 'gimp', '2.0', 'palettes')
    )

    install_data(
        'elementary.gpl',
        install_dir: join_paths (get_option('datadir'), 'inkscape', 'palettes')
    )
endif
