ICON_DIRS = \
	actions \
	mimes \
	categories \
	devices \
	emotes \
	cursors \
	places \
	status \
	emblems \
	apps

EXTRA_DIST = \
	$(ICON_DIRS) \
	AUTHORS \
	COPYING \
	index.theme \
	cursor.theme \
	README.md

themedir = $(datadir)/icons/elementary
theme_DATA = \
	index.theme \
	cursor.theme

install-data-hook:
	test -d $(DESTDIR)$(themedir) || $(MKDIR_P) $(DESTDIR)$(themedir) ;
	for iconset in $(ICON_DIRS) ; do \
		cp -Rv $$iconset $(DESTDIR)$(themedir)/. ; \
		ln -sv $$iconset $(DESTDIR)$(themedir)/$$iconset@2x ; \
	done;
uninstall-hook:
	test -d $(DESTDIR)$(themedir) && rm -rvf $(DESTDIR)$(themedir)
