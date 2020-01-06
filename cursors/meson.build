cursor_dir = join_paths(icon_dir, 'cursors')
inkscape = find_program('inkscape')
xcursorgen = find_program('xcursorgen')

cursors = [
    'bd_double_arrow',
    'bottom_left_corner',
    'bottom_right_corner',
    'bottom_side',
    'bottom_tee',
    'circle',
    'copy',
    'cross',
    'crossed_circle',
    'crosshair',
    'dnd-ask',
    'dnd-copy',
    'dnd-link',
    'dnd-move',
    'dnd-none',
    'dotbox',
    'fd_double_arrow',
    'grabbing',
    'hand1',
    'hand2',
    'left_ptr',
    'left_side',
    'left_tee',
    'link',
    'll_angle',
    'lr_angle',
    'move',
    'no-drop',
    'pencil',
    'plus',
    'question_arrow',
    'right_ptr',
    'right_side',
    'right_tee',
    'sb_down_arrow',
    'sb_h_double_arrow',
    'sb_left_arrow',
    'sb_right_arrow',
    'sb_up_arrow',
    'sb_v_double_arrow',
    'tcross',
    'top_left_corner',
    'top_right_corner',
    'top_side',
    'top_tee',
    'ul_angle',
    'ur_angle',
    'X_cursor',
    'xterm'
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
    run_command('mkdir', join_paths (meson.build_root(), 'cursors', size + 'x' + size))

    foreach cursor : cursors
            message('rendering: ' + size + 'x' + size + '/' + cursor + '.png')

            run_command(
                inkscape, '--without-gui',
                '--export-width=@0@'.format(size), '--export-height=@0@'.format(size),
                '--export-png=@0@.png'.format(join_paths (meson.build_root(), 'cursors', size + 'x' + size, cursor)),
                join_paths ('24', cursor + '.svg')
            )
    endforeach

    foreach watch : watches
            message('rendering: ' + size + 'x' + size + '/' + watch + '.png')

            run_command(
                inkscape, '--without-gui',
                '--export-width=@0@'.format(size), '--export-height=@0@'.format(size),
                '--export-png=@0@.png'.format(join_paths (meson.build_root(), 'cursors', size + 'x' + size, watch)),
                join_paths ('24', watch + '.svg')
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
        join_paths (meson.build_root(), 'cursors', cursor)
    )

    install_data(
        join_paths (meson.build_root(), 'cursors', cursor),
        install_dir: cursor_dir
    )
endforeach

links = []

links += [[
  'left_ptr',
  [
      'top_left_arrow',
      'arrow'
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
  'dotbox',
  [
      'target',
      'icon',
      'draped_box',
      'dot_box_mask'
  ]
]]

links += [[
  'X_cursor',
  [
      'pirate'
  ]
]]

links += [[
  'question_arrow',
  [
      'left_ptr_help',
      'help',
      'd9ce0ab605698f320427677b458ad60b',
      '5c6cd98b3f3ebcb1f9c7f1c204630408'
  ]
]]

links += [[
  'sb_v_double_arrow',
  [
      'v_double_arrow',
      'double_arrow',
      '00008160000006810000408080010102',
      '2870a09082c103050810ffdffffe0204'
  ]
]]

links += [[
  'sb_h_double_arrow',
  [
      'h_double_arrow',
      '028006030e0e7ebffc7f7070c0600140',
      '14fef782d02440884392942c11205230'
  ]
]]

links += [[
  'fd_double_arrow',
  [
      'fcf1c3c7cd4491d801f1e1c78f100000'
  ]
]]

links += [[
  'bd_double_arrow',
  [
      'c7088f0f3e6c8088236ef8e1e3e70000'
  ]
]]

links += [[
  'hand2',
  [
      'hand',
      '9d800788f1b08800ae810202380a0822'
  ]
]]

links += [[
  'grabbing',
  [
      'fleur'
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
  'crossed_circle',
  [
      '03b6e0fcb3499374a867c041f52298f0'
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
  'copy',
  [
      '6407b0e94181790501fd1e167b474872',
      '1081e37283d90000800003c07f3ef6bf'
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
  'left_ptr',
  [
      '08e8e1c95fe2fc01f976f1e063a24ccd',
      '3ecb610c1bf2410f44200f48c40d3599'
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
