{
  'targets': [
    { 'target_name': 'everything',
      'type': 'none',
      'hard_dependency': 1,

      'dependencies': [
        'core',
        'platform', #'platform-<(platform_lib)',
        'http', #'http-<(http_lib)',
        'asset', #'asset-<(asset_lib)',
        'cache', #'cache-<(cache_lib)',
        'headless', #'headless-<(headless_lib)',
      ],
    },

    { 'target_name': 'standalone',
      'product_name': 'libmbgl.a',
      'type': 'executable',
      'hard_dependency': 1,

      'dependencies': [
        'core',
        'platform', #'platform-<(platform_lib)',
        'http', #'http-<(http_lib)',
        'asset', #'asset-<(asset_lib)',
        'cache', #'cache-<(cache_lib)',
        'headless', #'headless-<(headless_lib)',
      ],
    },
  ],
}