{ # MGDESIGN
  'targets': [
    { 'target_name': 'platform-win',
      'product_name': 'mbgl-platform-win',
      'type': 'static_library',
      'standalone_static_library': 1,
      'hard_dependency': 1,
      'dependencies': [
        'version',
      ],

      'sources': [
        '../platform/default/log_stderr.cpp',
        '../platform/default/string_stdlib.cpp',
        '../platform/default/application_root.cpp',
        '../platform/default/asset_root.cpp',
        '../platform/default/image.cpp',
        '../platform/default/image_reader.cpp',
        '../platform/default/png_reader.cpp',
        '../platform/default/jpeg_reader.cpp',
      ],

      'variables': {
        'cflags_cc': [
          '<@(png_cflags)',
          '<@(jpeg_cflags)',
          '<@(uv_cflags)',
          '<@(nu_cflags)',
          '<@(boost_cflags)',
        ],
        'ldflags': [
          '<@(png_ldflags)',
          '<@(jpeg_ldflags)',
          '<@(uv_ldflags)',
          '<@(nu_ldflags)',
        ],
        'libraries': [
          '<@(png_static_libs)',
          '<@(jpeg_static_libs)',
          '<@(uv_static_libs)',
          '<@(nu_static_libs)',
        ],
      },

      'include_dirs': [
        '../include',
        '../src',
        '../libs/boost_1_55_0', #MGDESIGN
        '../libs/lpng1617',
        '../libs/libuv-1.x',
        '../libs/libuv-1.x/include'
      ],

      'conditions': [
        ['OS == "mac"', {
          'xcode_settings': {
            'OTHER_CPLUSPLUSFLAGS': [ '<@(cflags_cc)' ],
          }
        }, {
          'cflags_cc': [ '<@(cflags_cc)' ],
        }]
      ],

      'link_settings': {
        'conditions': [
          ['OS == "mac"', {
            'libraries': [ '<@(libraries)' ],
            'xcode_settings': { 'OTHER_LDFLAGS': [ '<@(ldflags)' ] }
          }, {
            'libraries': [ '<@(libraries)', '<@(ldflags)' ],
          }]
        ],
      },

      'direct_dependent_settings': {
        'include_dirs': [
          '../include'          
        ],
      },
    },
  ],
}
