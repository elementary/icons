cmake_minimum_required (VERSION 3.3)
cmake_policy (VERSION 3.3)
project (elementary NONE)

list (APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake)
include (InstallSymlink)

include (GNUInstallDirs)
set (DATADIR "${CMAKE_INSTALL_FULL_DATAROOTDIR}")

###
#   This is the configuration (Designers, it's for you)
###

set (ICONDIR "${DATADIR}/icons/${CMAKE_PROJECT_NAME}")
set (VERSION "4.3.1")

# Just add a 3 or 4 to create new symlinks for very-hi-dpi.

set (DPI_ARRAY 1 2)

# Add a directory here to the list if needed.

set (DIRECTORIES actions apps categories devices emblems emotes mimes places status)
set (DIRECTORIES_CONTEXTS Actions Applications Categories Devices Emblems Emotes MimeTypes Places Status)

# Add a directory here to the list if needed.

set (SIZES 16 24 32 48 64 128 symbolic)

# Symbolic icons are made to have a maximum size.

set (MAX_SIZE_SYMBOLIC 512)

# This is the minimal size all icons can theorically have.

set (MIN_SIZE_EVER 8)

###
#   This is the actual work (Programmers, it's for you)
###

add_subdirectory (cursors)
add_subdirectory (volumeicon)

list (LENGTH DIRECTORIES LENGTH_1)
list (LENGTH DIRECTORIES_CONTEXTS LENGTH_2)
if (NOT (${LENGTH_1} STREQUAL ${LENGTH_2}))
    message (FATAL_ERROR "DIRECTORIES should have the same number of elements than DIRECTORIES_CONTEXTS")
endif ()
foreach (DIRECTORY ${DIRECTORIES})
    file (GLOB SUBDIRS "${CMAKE_SOURCE_DIR}/${DIRECTORY}/*")
    install (DIRECTORY ${SUBDIRS} DESTINATION ${ICONDIR}/${DIRECTORY})
endforeach ()

foreach (DPI ${DPI_ARRAY})
    if (${DPI} GREATER 1)
        foreach (DIRECTORY ${DIRECTORIES})
            InstallSymlink (${DIRECTORY} ${ICONDIR}/${DIRECTORY}@${DPI}x)
        endforeach ()
    endif ()
endforeach ()

# Creating all the variables for the .theme file

set (DIRECTORY_DETAILS "")

set (DIRECTORY_LIST)

foreach (DIRECTORY ${DIRECTORIES})
    # We need to look at the directory because all directories don't have all icon sizes…
    file (GLOB SIZES_DIR "${CMAKE_SOURCE_DIR}/${DIRECTORY}/*")
    foreach (SIZE ${SIZES})
        if (NOT ("${CMAKE_SOURCE_DIR}/${DIRECTORY}/${SIZE}" IN_LIST SIZES_DIR))
            message (STATUS "INFO: Directory ${DIRECTORY}/${SIZE} doesn't exist and won't be listed in the theme file.")
            continue ()
        endif ()

        foreach (DPI ${DPI_ARRAY})
            # The Scale=1 is useless, don't add it
            if (${DPI} GREATER 1)
                set (SCALE_ENTRY "Scale=${DPI}\n")
                set (DIRECTORY_NAME "${DIRECTORY}@${DPI}x/${SIZE}")
            else ()
                set (SCALE_ENTRY "")
                set (DIRECTORY_NAME "${DIRECTORY}/${SIZE}")
            endif ()

            # Generates the Directories= line
            list (APPEND DIRECTORY_LIST ${DIRECTORY_NAME})

            # Get the corresponding element in DIRECTORIES_CONTEXTS
            list (FIND DIRECTORIES ${DIRECTORY} INDEX_NUMBER)
            list (GET DIRECTORIES_CONTEXTS ${INDEX_NUMBER} CONTEXT)

            # Get the size of the next element, the MaxSize of the current size is the size of the next element minus one.
            # Symbolic icons are a special case and have always a MaxSize of MAX_SIZE_SYMBOLIC.
            if ("${SIZE}" STREQUAL "symbolic")
                set (SIZE_ENTRY 16)
                set (MAX_SIZE ${MAX_SIZE_SYMBOLIC})
            else ()
                set (SIZE_ENTRY ${SIZE})
                list (FIND SIZES ${SIZE} SIZE_INDEX_NUMBER)
                math (EXPR SIZE_INDEX_NUMBER "${SIZE_INDEX_NUMBER} + 1")
                list (GET SIZES ${SIZE_INDEX_NUMBER} NEXT_SIZE)
                # If next size if symbolic, we fallback to the MAX_SIZE_SYMBOLIC size
                if ("${NEXT_SIZE}" STREQUAL "symbolic")
                    set (MAX_SIZE ${MAX_SIZE_SYMBOLIC})
                else ()
                    math (EXPR MAX_SIZE "${NEXT_SIZE} - 1")
                endif ()
            endif ()
            set (DIRECTORY_DETAILS 
                "${DIRECTORY_DETAILS}\n"
                "[${DIRECTORY_NAME}]\n"
                "Size=${SIZE_ENTRY}\n"
                "${SCALE_ENTRY}"
                "Context=${CONTEXT}\n"
                "MinSize=${MIN_SIZE_EVER}\n"
                "MaxSize=${MAX_SIZE}\n"
                "Type=Scalable\n")
        endforeach ()
    endforeach ()
endforeach ()

string (REPLACE ";" "" DIRECTORY_DETAILS "${DIRECTORY_DETAILS}")
string (REPLACE ";" "," DIRECTORY_LIST "${DIRECTORY_LIST}")
configure_file (${CMAKE_SOURCE_DIR}/index.theme.in ${CMAKE_BINARY_DIR}/index.theme)

install (FILES ${CMAKE_BINARY_DIR}/index.theme DESTINATION ${ICONDIR})
