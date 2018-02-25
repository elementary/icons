
###
#   This is the configuration (Designers, it's for you)
###

set (CURSORSDIR "${ICONDIR}/cursors")

# To define a symlink, just create a list named MyTargetFileName_LINKS containing all the symlinks.


set (left_ptr_LINKS
    top_left_arrow
    arrow
)

set (right_ptr_LINKS
    draft_small
    draft_large
)

set (dotbox_LINKS
    target
    icon
    draped_box
    dot_box_mask
)

set (X_cursor_LINKS
    pirate
)

set (question_arrow_LINKS
    left_ptr_help
    help
    d9ce0ab605698f320427677b458ad60b
    5c6cd98b3f3ebcb1f9c7f1c204630408
)

set (sb_v_double_arrow_LINKS
    v_double_arrow
    double_arrow
    00008160000006810000408080010102
    2870a09082c103050810ffdffffe0204
)

set (sb_h_double_arrow_LINKS
    h_double_arrow
    028006030e0e7ebffc7f7070c0600140
    14fef782d02440884392942c11205230
)

set (fd_double_arrow_LINKS
    fcf1c3c7cd4491d801f1e1c78f100000
)

set (bd_double_arrow_LINKS
    c7088f0f3e6c8088236ef8e1e3e70000
)

set (hand2_LINKS
    hand1
    hand
    fcf1c3c7cd4491d801f1e1c78f100000
    9d800788f1b08800ae810202380a0822
)

set (grabbing_LINKS
    fleur
)

set (cross_LINKS
    diamond_cross
    cross_reverse
)

set (crossed_circle_LINKS
    03b6e0fcb3499374a867c041f52298f0
)

set (move_LINKS
    9081237383d90e509aa00f00170e968f
    4498f0e0c1937ffe01fd06f973665830
)

set (copy_LINKS
    6407b0e94181790501fd1e167b474872
    1081e37283d90000800003c07f3ef6bf
)

set (link_LINKS
    3085a0e285430894940527032f8b26df
    640fb0e74195791501fd1ed57b41487f
)

set (left_ptr_watch
    08e8e1c95fe2fc01f976f1e063a24ccd
    3ecb610c1bf2410f44200f48c40d3599
)

###
#   This is the actual work (Programmers, it's for you)
###

install (FILES ${CMAKE_CURRENT_SOURCE_DIR}/cursor.theme DESTINATION ${ICONDIR})

file (GLOB CURSORS "${CMAKE_CURRENT_SOURCE_DIR}/*")
list (REMOVE_ITEM CURSORS "${CMAKE_CURRENT_SOURCE_DIR}/cursor.theme")
list (REMOVE_ITEM CURSORS "${CMAKE_CURRENT_SOURCE_DIR}/CMakeLists.txt")
install (FILES ${CURSORS} DESTINATION ${CURSORSDIR})


# Create the aweful symlinks
foreach (CURSOR ${CURSORS})
    get_filename_component (BASE_NAME ${CURSOR} NAME)
    if (DEFINED ${BASE_NAME}_LINKS)
        foreach (LINK ${${BASE_NAME}_LINKS})
            InstallSymlink (${CURSORSDIR}/${BASE_NAME} ${CURSORSDIR}/${LINK})
        endforeach ()
    endif ()
endforeach ()
