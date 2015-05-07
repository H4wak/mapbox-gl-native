set CONFIG_win32=-Dhost=win -Iconfig/win.gypi -Dinstall_prefix=/test

set LIBS_win32=-Dheadless_lib=none -Dplatform_lib=win -Dasset_lib=zip -Dhttp_lib=curl -Dcache_lib=sqlite --depth=. -Goutput_dir=.


::LIBS_win32+=-Dasset_lib=$(word 1,$(ASSET) fs)
::LIBS_win32+=-Dhttp_lib=$(word 1,$(HTTP) nsurl)
::LIBS_win32+=-Dcache_lib=$(word 1,$(CACHE) sqlite)
::LIBS_win32+=--depth=. -Goutput_dir=.





gyp %CONFIG_win32% %LIBS_win32% --generator-output=./build/win -f msvs -G msvs_version=2013


pause