cursor_dir = join_paths(icon_dir, 'cursors')
rsvg = find_program('rsvg-convert')
xcursorgen = find_program('xcursorgen')

cursors = [
    'alias',
    'all-scroll',
    'cell',
    'context-menu',
    'copy',
    'crosshair',
    'default',
    'ew-resize',
    'grab',
    'grabbing',
    'help',
    'move',
    'nesw-resize',
    'no-drop',
    'not-allowed',
    'ns-resize',
    'nw-resize',
    'nwse-resize',
    'pointer',
    'text',
    'vertical-text',
    'zoom-in',
    'zoom-out'
]

watches = [
    'progress_01',
    'progress_02',
    'progress_03',
    'progress_04',
    'progress_05',
    'progress_06',
    'progress_07',
    'progress_08',
    'progress_09',
    'progress_10',
    'progress_11',
    'progress_12',
    'progress_13',
    'progress_14',
    'progress_15',
    'progress_16',
    'wait_0001',
    'wait_0002',
    'wait_0003',
    'wait_0004',
    'wait_0005',
    'wait_0006',
    'wait_0007',
    'wait_0008',
    'wait_0009',
    'wait_0010',
    'wait_0011',
    'wait_0012',
    'wait_0013',
    'wait_0014',
    'wait_0015',
    'wait_0016'
]

sizes = [
    '24',
    '32',
    '48',
    '64',
    '96'
]

foreach size: sizes
    run_command('mkdir', join_paths (meson.project_build_root(), 'cursors', size + 'x' + size), check: false)

    foreach cursor : cursors
            message('rendering: ' + size + 'x' + size + '/' + cursor + '.png')

            run_command(
                rsvg, '--format', 'png',
                '--width=@0@'.format(size), '--height=@0@'.format(size),
                '--output', '@0@.png'.format(join_paths (meson.project_build_root(), 'cursors', size + 'x' + size, cursor)),
                join_paths ('24', cursor + '.svg'),
                check: true,
            )
    endforeach

    foreach watch : watches
            message('rendering: ' + size + 'x' + size + '/' + watch + '.png')

            run_command(
                rsvg, '--format', 'png',
                '--width=@0@'.format(size), '--height=@0@'.format(size),
                '--output', '@0@.png'.format(join_paths (meson.project_build_root(), 'cursors', size + 'x' + size, watch)),
                join_paths ('24', watch + '.svg'),
                check: true,
            )
    endforeach
endforeach

cursors += [
    'progress',
    'wait'
]

foreach cursor : cursors
    message('generating: ' + cursor)

    run_command(
        xcursorgen,
        cursor + '.in',
        '-p', join_paths (meson.project_build_root(), 'cursors'),
        join_paths (meson.project_build_root(), 'cursors', cursor)
    )

    install_data(
        join_paths (meson.project_build_root(), 'cursors', cursor),
        install_dir: cursor_dir
    )
endforeach

links = []

links += [[
    'ew-resize',
    [
        'col-resize',
        'e-resize',
        'w-resize',
    ]
]]

links += [[
    'nesw-resize',
    [
        'ne-resize',
        'sw-resize',
    ]
]]

links += [[
    'ns-resize',
    [
        'row-resize',
        'n-resize',
        's-resize',
    ]
]]

links += [[
    'nwse-resize',
    [
        'se-resize',
    ]
]]

foreach link_entry : links
    src = link_entry[0]
    foreach dest : link_entry[1]
        install_symlink(
            dest,
            install_dir: cursor_dir,
            pointing_to: src,
        )
    endforeach
endforeach

install_data(
    'cursor.theme',
    install_dir: icon_dir
)
