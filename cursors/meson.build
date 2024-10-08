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
    'wait_01',
    'wait_02',
    'wait_03',
    'wait_04',
    'wait_05',
    'wait_06',
    'wait_07',
    'wait_08',
    'wait_09',
    'wait_10',
    'wait_11',
    'wait_12',
    'wait_13',
    'wait_14',
    'wait_15',
    'wait_16'
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
        'nw-resize',
        'se-resize',
    ]
]]

# Legacy cursor names

links += [[
    'copy',
    [
        '6407b0e94181790501fd1e167b474872',
        '1081e37283d90000800003c07f3ef6bf'
    ]
]]

links += [[
    'crosshair',
    [
        'diamond_cross',
        'cross_reverse'
    ]
]]

links += [[
    'default',
    [
        'left_ptr',
        'arrow',
        'top_left_arrow',
        'X_cursor',
        '08e8e1c95fe2fc01f976f1e063a24ccd',
        '3ecb610c1bf2410f44200f48c40d3599'
    ]
]]

links += [[
    'ew-resize',
    [
        'h_double_arrow',
        'left_side',
        'right_side',
        'sb_h_double_arrow',
        '028006030e0e7ebffc7f7070c0600140',
        '14fef782d02440884392942c11205230'
    ]
]]

links += [[
    'grab',
    [
        'hand1'
    ]
]]

links += [[
    'grabbing',
    [
        'dnd-none',
        'fleur'
    ]
]]

links += [[
    'help',
    [
        'left_ptr_help',
        'question_arrow',
        'd9ce0ab605698f320427677b458ad60b',
        '5c6cd98b3f3ebcb1f9c7f1c204630408'
    ]
]]

links += [[
    'move',
    [
        '9081237383d90e509aa00f00170e968f',
        '4498f0e0c1937ffe01fd06f973665830'
    ]
]]

links += [[
    'nesw-resize',
    [
        'bottom_left_corner',
        'fd_double_arrow',
        'top_right_corner',
        'fcf1c3c7cd4491d801f1e1c78f100000'
    ]
]]

links += [[
    'not-allowed',
    [
        'crossed_circle',
        '03b6e0fcb3499374a867c041f52298f0'
    ]
]]

links += [[
    'ns-resize',
    [
        'bottom_side',
        'double_arrow',
        'sb_v_double_arrow',
        'top_side',
        'v_double_arrow',
        '00008160000006810000408080010102',
        '2870a09082c103050810ffdffffe0204'
    ]
]]

links += [[
    'nwse-resize',
    [
        'bd_double_arrow',
        'bottom_right_corner',
        'top_left_corner',
        'c7088f0f3e6c8088236ef8e1e3e70000'
    ]
]]

links += [[
    'pointer',
    [
        'hand',
        'hand2',
        '9d800788f1b08800ae810202380a0822'
    ]
]]

links += [[
    'progress',
    [
        'left_ptr_watch'
    ]
]]

links += [[
    'text',
    [
        'xterm'
    ]
]]

links += [[
    'wait',
    [
        'watch'
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

install_subdir(
    'cursors_scalable',
    install_dir: icon_dir
)
