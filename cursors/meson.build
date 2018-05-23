cursor_dir = join_paths(icon_dir, 'cursors')

cursors = files(
    'xterm',
    'X_cursor',
    'watch',
    'ur_angle',
    'ul_angle',
    'top_tee',
    'top_side',
    'top_right_corner',
    'top_left_corner',
    'tcross',
    'sb_v_double_arrow',
    'sb_up_arrow',
    'sb_right_arrow',
    'sb_left_arrow',
    'sb_h_double_arrow',
    'sb_down_arrow',
    'right_tee',
    'right_side',
    'right_ptr',
    'question_arrow',
    'plus',
    'pencil',
    'move',
    'lr_angle',
    'll_angle',
    'link',
    'left_tee',
    'left_side',
    'left_ptr_watch',
    'left_ptr',
    'hand2',
    'grabbing',
    'fd_double_arrow',
    'dotbox',
    'dnd-none',
    'dnd-move',
    'dnd-link',
    'dnd-copy',
    'dnd-ask',
    'crosshair',
    'crossed_circle',
    'cross',
    'copy',
    'circle',
    'bottom_tee',
    'bottom_side',
    'bottom_right_corner',
    'bottom_left_corner',
    'bd_double_arrow'
)

install_data(
    cursors,
    install_dir: cursor_dir
)

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
      'hand1',
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
