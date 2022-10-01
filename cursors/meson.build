cursor_dir = join_paths(icon_dir, 'cursors')
rsvg = find_program('rsvg-convert')
xcursorgen = find_program('xcursorgen')

cursors = [
    'all-scroll',
    'bd_double_arrow',
    'bottom_tee',
    'circle',
    'copy',
    'cross',
    'crosshair',
    'dnd-ask',
    'dnd-copy',
    'dnd-link',
    'dnd-move',
    'dnd-none',
    'dotbox',
    'fd_double_arrow',
    'hand1',
    'help',
    'left_ptr',
    'left_tee',
    'link',
    'll_angle',
    'lr_angle',
    'move',
    'no-drop',
    'not-allowed',
    'pencil',
    'plus',
    'pointer',
    'right_ptr',
    'right_tee',
    'sb_down_arrow',
    'sb_h_double_arrow',
    'sb_left_arrow',
    'sb_right_arrow',
    'sb_up_arrow',
    'sb_v_double_arrow',
    'tcross',
    'text',
    'top_tee',
    'ul_angle',
    'ur_angle',
    'vertical-text',
    'X_cursor',
    'zoom-in',
    'zoom-out'
]

watches = [
    'left_ptr_watch_0001',
    'left_ptr_watch_0002',
    'left_ptr_watch_0003',
    'left_ptr_watch_0004',
    'left_ptr_watch_0005',
    'left_ptr_watch_0006',
    'left_ptr_watch_0007',
    'left_ptr_watch_0008',
    'watch_0001',
    'watch_0002',
    'watch_0003',
    'watch_0004',
    'watch_0005',
    'watch_0006',
    'watch_0007',
    'watch_0008',
    'watch_0009',
    'watch_0010',
    'watch_0011',
    'watch_0012',
    'watch_0013',
    'watch_0014',
    'watch_0015',
    'watch_0016'
]

sizes = [
    '24',
    '32',
    '48',
    '64',
    '96'
]

foreach size: sizes
    run_command('mkdir', join_paths (meson.build_root(), 'cursors', size + 'x' + size), check: false)

    foreach cursor : cursors
            message('rendering: ' + size + 'x' + size + '/' + cursor + '.png')

            run_command(
                rsvg, '--format', 'png',
                '--width=@0@'.format(size), '--height=@0@'.format(size),
                '--output', '@0@.png'.format(join_paths (meson.build_root(), 'cursors', size + 'x' + size, cursor)),
                join_paths ('24', cursor + '.svg'),
                check: false
            )
    endforeach

    foreach watch : watches
            message('rendering: ' + size + 'x' + size + '/' + watch + '.png')

            run_command(
                rsvg, '--format', 'png',
                '--width=@0@'.format(size), '--height=@0@'.format(size),
                '--output', '@0@.png'.format(join_paths (meson.build_root(), 'cursors', size + 'x' + size, watch)),
                join_paths ('24', watch + '.svg'),
                check: false
            )
    endforeach
endforeach

cursors += [
    'left_ptr_watch',
    'watch'
]

foreach cursor : cursors
    message('generating: ' + cursor)

    run_command(
        xcursorgen,
        cursor + '.in',
        '-p', join_paths (meson.build_root(), 'cursors'),
        join_paths (meson.build_root(), 'cursors', cursor),
        check: false
    )

    install_data(
        join_paths (meson.build_root(), 'cursors', cursor),
        install_dir: cursor_dir
    )
endforeach

links = []

links += [[
  'bd_double_arrow',
  [
      'bottom_right_corner',
      'top_left_corner',
      'c7088f0f3e6c8088236ef8e1e3e70000'
  ]
]]

links += [[
  'copy',
  [
      '6407b0e94181790501fd1e167b474872',
      '1081e37283d90000800003c07f3ef6bf'
  ]
]]

links += [[
  'cross',
  [
      'diamond_cross',
      'cross_reverse'
  ]
]]

links += [[
    'dnd-none',
    [
        'grabbing'
    ]
]]

links += [[
  'dotbox',
  [
      'target',
      'icon',
      'draped_box',
      'dot_box_mask'
  ]
]]

links += [[
  'fd_double_arrow',
  [
      'bottom_left_corner',
      'top_right_corner',
      'fcf1c3c7cd4491d801f1e1c78f100000'
  ]
]]

links += [[
  'grabbing',
  [
      'fleur'
  ]
]]

links += [[
  'hand1',
  [
      'grab'
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
  'left_ptr',
  [
      'arrow',
      'top_left_arrow',
      '08e8e1c95fe2fc01f976f1e063a24ccd',
      '3ecb610c1bf2410f44200f48c40d3599'
  ]
]]

links += [[
  'link',
  [
      '3085a0e285430894940527032f8b26df',
      '640fb0e74195791501fd1ed57b41487f'
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
  'not-allowed',
  [
      'crossed_circle',
      '03b6e0fcb3499374a867c041f52298f0'
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
  'plus',
  [
      'cell'
  ]
]]


links += [[
  'right_ptr',
  [
      'draft_small',
      'draft_large'
  ]
]]

links += [[
  'sb_h_double_arrow',
  [
      'h_double_arrow',
      'left_side',
      'right_side',
      '028006030e0e7ebffc7f7070c0600140',
      '14fef782d02440884392942c11205230'
  ]
]]

links += [[
  'sb_v_double_arrow',
  [
      'bottom_side',
      'double_arrow',
      'top_side',
      'v_double_arrow',
      '00008160000006810000408080010102',
      '2870a09082c103050810ffdffffe0204'
  ]
]]

links += [[
  'text',
  [
      'xterm'
  ]
]]

links += [[
  'X_cursor',
  [
      'pirate'
  ]
]]

foreach link_entry : links
    src = link_entry[0]
    foreach dest : link_entry[1]
        meson.add_install_script(
            symlink,
            '--src', join_paths (cursor_dir, src),
            '--dest', join_paths (cursor_dir, dest)
        )
    endforeach
endforeach

install_data(
    'cursor.theme',
    install_dir: icon_dir
)
