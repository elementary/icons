mime_sizes = ['16', '24', '32', '48', '64', '128']

python3 = find_program('python3', required: true)

# Copy src dir to build dir, to give a base to work on

mime_types = [
    # The first argument is the icon name,
    # the second is the base that should be used
    ['application-illustrator', 'base-generic'],
    ['application-javascript', 'base-generic'],
    ['application-json', 'base-generic'],
    ['application-msword', 'base-generic'],
    ['application-octet-stream', 'base-generic'],
    ['application-pdf', 'base-generic'],
    ['application-pgp', 'base-generic'],
    ['application-typescript', 'base-generic'],

    ['application-vnd.debian.binary-package', 'base-package'],
    ['application-vnd.flatpak.ref', 'base-generic'],
    ['application-vnd.flatpak', 'base-package'],
    ['application-vnd.ms-access', 'base-generic'],
    ['application-vnd.ms-excel', 'base-generic'],
    ['application-vnd.ms-powerpoint', 'base-generic'],
    ['application-vnd.oasis.opendocument.chart', 'base-generic'],
    ['application-vnd.openxmlformats-officedocument.presentationml.template', 'base-generic'],
    ['application-vnd.openxmlformats-officedocument.spreadsheetml.template', 'base-generic'],
    ['application-vnd.openxmlformats-officedocument.wordprocessingml.template', 'base-generic'],

    ['application-x-bittorrent', 'base-generic'],
    ['application-x-cd-image', 'base-generic'],
    ['application-x-desktop', 'base-generic'],
    ['application-x-executable', 'base-executable'],
    ['application-x-ms-dos-executable', 'base-executable'],
    ['application-x-partial-download', 'base-generic'],
    ['application-x-php', 'base-generic'],
    ['application-x-ruby', 'base-generic'],
    ['application-x-sharedlib', 'base-generic'],

    ['audio-x-generic', 'base-generic'],
    ['audio-x-playlist', 'base-generic'],
    ['audio-x-playlist-rtl', 'base-generic'],

    ['font-x-generic', 'base-generic'],

    ['image-vnd.adobe.photoshop', 'base-generic'],
    ['image-x-xcf', 'base-generic'],

    ['internet-feed', 'base-generic'],
    ['model', 'base-generic'],
    ['office-contact', 'base-generic'],

    ['text-css', 'base-generic'],
    ['text-html', 'base-generic'],
    ['text-markdown', 'base-generic'],
    ['text-x-bibtex', 'base-generic'],
    ['text-x-changelog', 'base-generic'],
    ['text-x-chdr', 'base-generic'],
    ['text-x-copying', 'base-generic'],
    ['text-x-csrc', 'base-generic'],
    ['text-x-generic', 'base-generic'],
    ['text-x-generic-rtl', 'base-generic'],
    ['text-x-generic-template', 'base-generic'],
    ['text-x-generic-template-rtl', 'base-generic'],
    ['text-x-gettext-translation', 'base-generic'],
    ['text-x-gettext-translation-template', 'base-generic'],
    ['text-x-go', 'base-generic'],
    ['text-x-install', 'base-generic'],
    ['text-x-makefile', 'base-generic'],
    ['text-x-preview', 'base-generic'],
    ['text-x-python', 'base-generic'],
    ['text-x-readme', 'base-generic'],
    ['text-x-readme', 'base-generic'],
    ['text-x-sass', 'base-generic'],
    ['text-x-script', 'base-generic'],
    ['text-x-ssa', 'base-generic'],
    ['text-x-tex', 'base-generic'],
    ['text-x-vala', 'base-generic'],

    ['unknown', 'base-generic'],

    ['x-office-drawing', 'base-generic'],
    ['x-office-drawing-template', 'base-generic'],

    ['x-office-spreadsheet', 'base-generic'],
    ['x-office-spreadsheet-template', 'base-generic']
]

foreach size: mime_sizes
    run_command('mkdir', join_paths(meson.project_build_root(), 'mimes', size), check: false)
endforeach

foreach type : mime_types
    foreach size: mime_sizes
        if fs.is_file(size / type[0] + '.svg')
            message('compositing: ' + type[0] + '.svg and ' + type[1] + '.svg @ ' + size )

            output_file = '@0@.svg'.format(join_paths(meson.project_build_root(), 'mimes', size, type[0]))
            run_command('touch', output_file)

            run_command(
                python3,
                '@0@.py'.format(join_paths(meson.project_source_root(), 'scripts', 'composite-svg')), 
                '@0@.svg'.format(join_paths(meson.current_source_dir(), size, type[0])),
                '@0@.svg'.format(join_paths(meson.current_source_dir(), size, type[1])),
                output_file,
                check: true 
            )       
        endif
    endforeach
endforeach

# Adding the template decoration to template mimes
templates = [
    'application-vnd.openxmlformats-officedocument.presentationml.template',
    'application-vnd.openxmlformats-officedocument.spreadsheetml.template',
    'application-vnd.openxmlformats-officedocument.wordprocessingml.template',
    'text-x-generic-template',
    'text-x-generic-template-rtl',
    'text-x-gettext-translation-template',
    'x-office-document-template',
    'x-office-document-template-rtl',
    'x-office-drawing-template',
    'x-office-presentation-template',
    'x-office-presentation-template-rtl',
    'x-office-spreadsheet-template'
]

foreach template : templates
    foreach size: mime_sizes
        if fs.is_file(meson.project_build_root() / 'mimes' / size / template + '.svg')
            message('adding template decoration: ' + template + '.svg @ ' + size)

            run_command(
                python3, 
                '@0@.py'.format(join_paths(meson.project_source_root(), 'scripts', 'composite-svg')), 
                '@0@.svg'.format(join_paths(meson.current_source_dir(), size, 'decoration-template')), 
                # We operate entirely in the build directory here, because we are
                # cascading off of a previously composited file
                '@0@.svg'.format(join_paths(meson.project_build_root(), 'mimes', size, template)),
                '@0@.svg'.format(join_paths(meson.project_build_root(), 'mimes', size, template)),
                check: true 
            )
        endif
    endforeach
endforeach

install_subdir(
    meson.project_build_root() / 'mimes',
    install_dir: icon_dir,
    strip_directory: false
)

mime_links = [
    # The first argument is the original icon name,
    # the second is the link
    ['application-javascript', 'application-x-javascript'],

    ['application-msword', 'application-vnd.openxmlformats-officedocument.wordprocessingml.document'],

    # Fallback naming doesn't appear to work reliably
    ['application-pgp', 'application-pgp-encrypted'],
    ['application-pgp', 'application-pgp-keys'],

    ['application-vnd.ms-excel', 'application-vnd.openxmlformats-officedocument.spreadsheetml.sheet'],

    ['application-vnd.ms-powerpoint', 'application-vnd.ms-powerpoint.presentation.macroEnabled.12'],
    ['application-vnd.ms-powerpoint', 'application-vnd.openxmlformats-officedocument.presentationml.presentation'],
    ['application-vnd.ms-powerpoint', 'application-vnd.openxmlformats-officedocument.presentationml.slideshow'],

    ['application-x-addon', 'application-vnd.openofficeorg.extension'],
    ['application-x-addon', 'application-x-xpinstall'],
    ['application-x-addon', 'extension'],
    ['application-x-addon', 'libpeas-plugin'],

    ['application-x-cd-image', 'application-x-raw-disk-image'],

    ['application-x-executable', 'application-x-object'],
    ['application-x-executable', 'application-x-python-bytecode'],
    ['application-x-executable', 'binary'],
    ['application-x-executable', 'exec'],

    ['application-x-ms-dos-executable', 'application-x-msi'],

    ['audio-x-generic', 'audio-mpeg'],

    ['audio-x-playlist', 'audio-x-mp3-playlist'],
    ['audio-x-playlist', 'audio-x-mpegurl'],
    ['audio-x-playlist', 'audio-x-scpls'],

    ['audio-x-playlist-rtl', 'audio-x-mp3-playlist-rtl'],
    ['audio-x-playlist-rtl', 'audio-x-mpegurl-rtl'],
    ['audio-x-playlist-rtl', 'audio-x-scpls-rtl'],

    ['image-x-generic', 'image'],

    ['image-x-xcf', 'image-x-compressed-xcf'],

    ['internet-feed', 'application-atom+xml'],
    ['internet-feed', 'application-rss+xml'],

    ['model', 'application-x-blender'],
    ['model', 'image-x-3ds'],

    ['office-contact', 'text-directory'],
    ['office-contact', 'vcard'],

    ['office-database', 'application-sql'],
    ['office-database', 'application-vnd.oasis.opendocument.database'],
    ['office-database', 'application-x-sqlite2'],
    ['office-database', 'application-x-sqlite3'],
    ['office-database', 'text-x-sql'],

    ['package-x-generic', 'application-x-java-archive'],
    ['package-x-generic', 'package'],

    ['text-x-generic', 'application-x-gnome-theme-package'],
    ['text-x-generic', 'application-x-theme'],
    ['text-x-generic', 'document'],
    ['text-x-generic', 'text'],
    ['text-x-generic', 'text-plain'],
    ['text-x-generic', 'wordprocessing'],

    ['text-x-generic-rtl', 'application-x-gnome-theme-package-rtl'],
    ['text-x-generic-rtl', 'application-x-theme-rtl'],
    ['text-x-generic-rtl', 'document-rtl'],
    ['text-x-generic-rtl', 'text-rtl'],
    ['text-x-generic-rtl', 'text-plain-rtl'],
    ['text-x-generic-rtl', 'wordprocessing-rtl'],

    ['text-html', 'application-vnd.oasis.opendocument.text-web'],
    ['text-html', 'application-x-class-file'],
    ['text-html', 'application-x-java'],
    ['text-html', 'application-xml'],
    ['text-html', 'html'],
    ['text-html', 'text-htmlh'],
    ['text-html', 'text-x-java'],
    ['text-html', 'text-x-java-source'],
    ['text-html', 'text-xml'],
    ['text-html', 'www'],

    ['text-x-changelog', 'text-x-patch'],

    ['text-x-makefile', 'text-x-cmake'],
    ['text-x-makefile', 'text-x-meson'],

    ['text-x-preview', 'application-vnd.cups-pdf-banner'],
    ['text-x-preview', 'empty'],
    ['text-x-preview', 'application-x-generic'],

    ['text-x-python', 'text-x-python3'],

    ['text-x-sass', 'text-x-scss'],

    ['text-x-ssa', 'application-x-subrip'],

    ['text-x-script', 'application-x-m4'],
    ['text-x-script', 'application-x-shellscript'],
    ['text-x-script', 'shellscript'],
    ['text-x-script', 'text-x-c++'],
    ['text-x-script', 'text-x-csharp'],
    ['text-x-script', 'text-x-c++src'],
    ['text-x-script', 'text-x-source'],

    ['video-x-generic', 'application-vnd.rn-realmedia'],
    ['video-x-generic', 'application-x-matroska'],
    ['video-x-generic', 'media-video'],

    ['x-office-calendar', 'vcalendar'],
    ['x-office-calendar', 'text-calendar'],

    ['x-office-document', 'application-rtf'],
    ['x-office-document', 'application-vnd.oasis.opendocument.text'],
    ['x-office-document', 'application-vnd.sun.xml.writer'],
    ['x-office-document', 'application-vnd.wordperfect'],
    ['x-office-document', 'office-document'],
    ['x-office-document', 'text-enriched'],
    ['x-office-document', 'text-richtext'],

    ['x-office-document-rtl', 'application-rtf-rtl'],
    ['x-office-document-rtl', 'application-vnd.oasis.opendocument.text-rtl'],
    ['x-office-document-rtl', 'application-vnd.sun.xml.writer-rtl'],
    ['x-office-document-rtl', 'application-vnd.wordperfect-rtl'],
    ['x-office-document-rtl', 'office-document-rtl'],
    ['x-office-document-rtl', 'text-enriched-rtl'],
    ['x-office-document-rtl', 'text-richtext-rtl'],

    ['x-office-document-template', 'application-vnd.oasis.opendocument.text-template'],

    ['x-office-document-template-rtl', 'application-vnd.oasis.opendocument.text-template-rtl'],

    ['x-office-drawing', 'application-vnd.oasis.opendocument.drawing'],
    ['x-office-drawing', 'application-vnd.oasis.opendocument.graphics'],
    ['x-office-drawing', 'application-vnd.sun.xml.draw'],
    ['x-office-drawing', 'image-svg+xml'],
    ['x-office-drawing', 'office-illustration'],

    ['x-office-drawing-template', 'application-vnd.oasis.opendocument.graphics-template'],

    ['x-office-presentation', 'application-vnd.oasis.opendocument.presentation'],

    ['x-office-presentation-rtl', 'application-vnd.oasis.opendocument.presentation-rtl'],

    ['x-office-presentation-template', 'application-vnd.oasis.opendocument.presentation-template'],

    ['x-office-presentation-template-rtl', 'application-vnd.oasis.opendocument.presentation-template-rtl'],

    ['x-office-spreadsheet', 'application-vnd.oasis.opendocument.spreadsheet'],
    ['x-office-spreadsheet', 'application-vnd.sun.xml.calc'],
    ['x-office-spreadsheet', 'application-x-gnumeric'],
    ['x-office-spreadsheet', 'office-spreadsheet'],
    ['x-office-spreadsheet', 'text-csv'],
    ['x-office-spreadsheet', 'text-spreadsheet'],

    ['x-office-spreadsheet-template', 'application-vnd.oasis.opendocument.spreadsheet-template']
]

foreach link : mime_links
    foreach size: mime_sizes
        install_symlink(
            link[1] + '.svg',
            install_dir: icon_dir / 'mimes' / size,
            pointing_to: link[0] + '.svg',
        )
    endforeach
endforeach
