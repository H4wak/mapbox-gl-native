set CONFIG_win32=-Dhost=win -Iconfig/win.gypi -Dinstall_prefix=/test

set LIBS_win32=-Dheadless_lib=none -Dplatform_lib=win -Dasset_lib=fs -Dhttp_lib=curl -Dcache_lib=sqlite --depth=. -Goutput_dir=.
set TOTO=-Dtoto="C:\Users\test\Desktop\Fork_MapBox\mapbox-gl-native"
::set TOTO=-Dtoto="titi"

:: # MGDESIGN


gyp %TOTO% %CONFIG_win32% %LIBS_win32% --generator-output=./build/win -f msvs -G msvs_version=2015


pause