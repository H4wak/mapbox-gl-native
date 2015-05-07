{
  'includes': [
    '../gyp/common2.gypi',
  ],
  'targets': [
    { 'target_name': 'winapp',
      'product_name': 'mapbox-gl',
      'type': 'executable',

      'dependencies': [
        '../mbgl.gyp:core',
        '../mbgl.gyp:platform-<(platform_lib)'
        '../mbgl.gyp:http-<(http_lib)',
        '../mbgl.gyp:asset-<(asset_lib)',
        '../mbgl.gyp:cache-<(cache_lib)',
        '../mbgl.gyp:bundle_styles',
        '../mbgl.gyp:copy_certificate_bundle',
      ],

      'sources': [
        'main.cpp',
        '../platform/default/settings_json.cpp',
        '../platform/default/glfw_view.cpp',
        '../platform/default/log_stderr.cpp',
      ],

      'variables' : {
        'cflags_cc': [   
          '<@(glfw3_cflag)'
        ],
        'ldflags': [
          '<@(glfw3_ldflags)'
        ],
        'libraries': [
          '<@(glfw3_static_libs)'
        ],
      },

      'conditions': [
        ['OS == "mac"', {
          'libraries': [ '<@(libraries)' ],
          'xcode_settings': {
            'SDKROOT': 'macosx',
            'SUPPORTED_PLATFORMS':'macosx',
            'OTHER_CPLUSPLUSFLAGS': [ '<@(cflags_cc)' ],
            'OTHER_LDFLAGS': [ '<@(ldflags)' ],
            'SDKROOT': 'macosx',
            'MACOSX_DEPLOYMENT_TARGET': '10.9',
          }
        }, {
          'cflags_cc': [ '<@(cflags_cc)' ],
          'libraries': [ '<@(libraries)', '<@(ldflags)' ],
        }]
      ],
    },
  ],
}
