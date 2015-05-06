{
  'includes': [
    '../gyp/common2.gypi',
  ],
  'targets': [
    { 'target_name': 'mbgl-render',
      'product_name': 'mbgl-render',
      'type': 'executable',

      'dependencies': [
        '../mbgl.gyp:core',
        '../mbgl.gyp:platform', # '../mbgl.gyp:platform-<(platform_lib)'
        '../mbgl.gyp:headless', # '../mbgl.gyp:headless-<(headless_lib)',
        '../mbgl.gyp:http', #'../mbgl.gyp:http-<(http_lib)',
        '../mbgl.gyp:asset', # '../mbgl.gyp:asset-<(asset_lib)',
        '../mbgl.gyp:cache', # '../mbgl.gyp:cache-<(cache_lib)',
        '../mbgl.gyp:copy_certificate_bundle',
      ],

      'include_dirs': [
        '../src',
      ],

      'sources': [
        './render.cpp',
      ],

      'variables' : {
        'cflags_cc': [
          '""', # '<@(glfw3_cflags)',
          '""', #  '<@(uv_cflags)',
          '""', # '<@(boost_cflags)',
        ],
        'ldflags': [
          '""', # '<@(glfw3_ldflags)',
          '""', #  '<@(uv_ldlags)',
          '""', # '<@(boost_ldflags)',
          '-lboost_program_options'
        ],
        'libraries': [
          '""', #'<@(glfw3_static_libs)',
          '""', # '<@(uv_static_libs)'
        ],
      },

      'conditions': [
        ['OS == "mac"', {
          'libraries': [ '<@(libraries)' ],
          'xcode_settings': {
            'OTHER_CPLUSPLUSFLAGS': [ '<@(cflags_cc)' ],
            'OTHER_LDFLAGS': [ '<@(ldflags)' ],
          }
        }, {
          'cflags_cc': [ '<@(cflags_cc)' ],
          'libraries': [ '<@(libraries)', '<@(ldflags)' ],
        }]
      ],
    },
  ],
}
