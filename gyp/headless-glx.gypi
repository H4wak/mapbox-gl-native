{
  'targets': [
    { 'target_name': 'headless-glx',
      'product_name': 'mbgl-headless-glx',
      'type': 'static_library',
      'standalone_static_library': 1,

      'sources': [
        '../platform/default/headless_view.cpp',
        '../platform/default/headless_display.cpp',
      ],

      'include_dirs': [
        '../include',
          # FIXME: Allow layer violation temporally until we
          # split the Map object into two. Only the implementation
          # will depend on ./src (and will be also placed there).
          '../src',
      ],

      'cflags_cc': [ '<@(opengl_cflags)' ],

      'link_settings': {
        'libraries': [ '<@(opengl_ldflags)' ],
      },
    },
  ],
}
