project (
  'io.elementary.icons-inkscape',
  version: '0.1.0',
  license: 'GPL3+',
  meson_version: '>=0.61',
)

fs = import('fs')

# This assumes an elementary OS system
icon_dir = fs.expanduser('~/.var/app/org.inkscape.Inkscape/config/inkscape/icons/elementary')

scale_factors = get_option('scale_factors')

directories = [
  ['actions', 'Actions'],
]

sizes = ['16', '24', 'symbolic']
max_size_symbolic = '512'
min_size_ever='8'

foreach directory : directories
  install_subdir(
    directory[0],
    install_dir: icon_dir
  )
endforeach

template = '''
[@0@]
Size=@1@@2@
Context=@3@
MinSize=@4@
MaxSize=@5@
Type=Scalable'''

directory_path_list = []
directory_details = []

foreach directory_entry : directories
    directory = directory_entry[0]
    directory_context = directory_entry[1]
    foreach size: sizes
        if (fs.exists(meson.project_source_root () / directory / size))
            foreach scale_factor : scale_factors
                # The Scale=1 attribute is useless, don't add it
                if (scale_factor.to_int() > 1)
                    scale_entry = '\nScale=@0@'.format (scale_factor)
                    directory_name = join_paths('@0@@@1@x'.format (directory, scale_factor), size)
                else
                    scale_entry = ''
                    directory_name = join_paths(directory, size)
                endif

                # Append it to add it to the final Directories= line
                directory_path_list += directory_name

                if (size == 'symbolic')
                    size_entry = '16'
                    # symbolic covers the whole size panel by definition
                    max_size = max_size_symbolic
                else
                    size_entry = size
                    # Get the next size on the list
                    size_found = false
                    foreach lookup_size: sizes
                        if (size == lookup_size)
                            size_found = true
                        # if the next size if 'symbolic', that means that this is the biggest size.
                        elif (size_found == true)
                            if (lookup_size == 'symbolic')
                                max_size = max_size_symbolic
                            else
                                # the maximal icon size of an entry is the next available size minus 1
                                max_size = (lookup_size.to_int() - 1).to_string()
                            endif
                            size_found = false
                        endif
                    endforeach
                endif

                directory_details += template.format(
                    directory_name,
                    size_entry,
                    scale_entry,
                    directory_context,
                    min_size_ever,
                    max_size
                )
            endforeach
        else
            message ('Directory "@0@/@1@" doesn\'t exist and won\'t be listed in the theme file.'.format (directory, size))
        endif
    endforeach
endforeach

configuration_data_object = configuration_data()
configuration_data_object.set('DIRECTORY_LIST', ','.join (directory_path_list))
configuration_data_object.set('DIRECTORY_DETAILS', '\n'.join (directory_details))

# Create the symlinks
configure_file(
    input: 'index.theme.in',
    output: '@BASENAME@',
    configuration: configuration_data_object,
    install_dir: icon_dir
)

# Create the symlinks
foreach directoy_entry : directories
    foreach scale_factor : scale_factors
        # We only create a symlink to the @1 directory, it's all the point of using SVG assets...
        if (scale_factor.to_int() > 1)
            directory = directory_entry[0]
            install_symlink(
                '@0@@@1@x'.format(directory, scale_factor),
                install_dir: icon_dir,
                pointing_to: directory,
            )
        endif
    endforeach
endforeach

subdir('actions')

