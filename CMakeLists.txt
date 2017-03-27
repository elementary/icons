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
set (VERSION "4.0.1")

# Just add a "@3x" or "@4x" (don't forget the double quotes) to create new symlinks.

set (DPI_ARRAY  "@2x")

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
    foreach (DIRECTORY ${DIRECTORIES})
        InstallSymlink (${ICONDIR}/${DIRECTORY} ${ICONDIR}/${DIRECTORY}${DPI})
    endforeach ()
endforeach ()

# Creating all the variables for the .theme file

set (DIRECTORY_DETAILS "")

set (DIRECTORY_LIST "")

foreach (DIRECTORY ${DIRECTORIES})
    # We need to look at the directory because all directories don't have all icon sizes…
    file (GLOB SIZES_DIR "${CMAKE_SOURCE_DIR}/${DIRECTORY}/*")
    foreach (SIZE ${SIZES})
        if (NOT ("${CMAKE_SOURCE_DIR}/${DIRECTORY}/${SIZE}" IN_LIST SIZES_DIR))
            message (STATUS "INFO: Directory ${DIRECTORY}/${SIZE} doesn't exist and won't be listed in the theme file.")
            continue ()
        endif ()
        # We need the blank quotes to add the @1 DPI to the list
        foreach (DPI "" ${DPI_ARRAY})

            set (COMMA ",")
            if ("${DIRECTORY_LIST}" STREQUAL "")
                set (COMMA "")
            endif ()
            set (DIRECTORY_LIST ${DIRECTORY_LIST}${COMMA}${DIRECTORY}${DPI}/${SIZE}) # Generates the Directories= line

            # Get the corresponding element in DIRECTORIES_CONTEXTS
            list (FIND DIRECTORIES ${DIRECTORY} INDEX_NUMBER)
            list (GET DIRECTORIES_CONTEXTS ${INDEX_NUMBER} CONTEXT)

            # Get the size of the next element, the MaxSize of the current size is the size of the next element minus one.
            # Symbolic icons are a special case and have always a MaxSize of MAX_SIZE_SYMBOLIC.
            if ("${SIZE}" STREQUAL "symbolic")
                set (MAX_SIZE ${MAX_SIZE_SYMBOLIC})
            else ()
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
                "[${DIRECTORY}${DPI}/${SIZE}]\n"
                "Size=${SIZE}\n"
                "Context=${CONTEXT}\n"
                "MinSize=${MIN_SIZE_EVER}\n"
                "MaxSize=${MAX_SIZE}\n"
                "Type=Scalable\n")
        endforeach ()
    endforeach ()
endforeach ()

string (REPLACE ";" "" DIRECTORY_DETAILS "${DIRECTORY_DETAILS}")
configure_file (${CMAKE_SOURCE_DIR}/index.theme.in ${CMAKE_BINARY_DIR}/index.theme)

install (FILES ${CMAKE_BINARY_DIR}/index.theme DESTINATION ${ICONDIR})

