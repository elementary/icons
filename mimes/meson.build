mime_sizes = ['16', '24', '32', '48', '64', '128']

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
        meson.add_install_script(
            symlink,
            '--src', icon_dir / 'mimes' / size / link[0] + '.svg',
            '--dest', icon_dir / 'mimes' / size / link[1] + '.svg'
        )
    endforeach
endforeach
