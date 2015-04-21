{
  'targets': [
    { 'target_name': 'headless-cgl',
      'product_name': 'mbgl-headless-cgl',
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
    },
  ],
}
