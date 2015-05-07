{
  'targets': [
    {
      'target_name': 'version',
      'type': 'none',
      'hard_dependency': 1,
      'actions': [
        {
          'action_name': 'Build Version Header',
          'inputs': [
            '../scripts/build-version.py',
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/include/mbgl/util/version.hpp',
          ],
          'action': ['<@(_inputs)', '<(SHARED_INTERMEDIATE_DIR)', '<!@(git describe --tags --always --abbrev=0)', '<!@(git rev-parse HEAD)'],
          #'action': ['<@(_inputs)', '<(SHARED_INTERMEDIATE_DIR)', 'ios-v0.2.16', '5ca44d145597d7e94c49a57d8638f9fcd9b9ba3e'],
        }
      ],
      'direct_dependent_settings': {
        'sources': [
          '<(SHARED_INTERMEDIATE_DIR)/include/mbgl/util/version.hpp',
        ],
        'include_dirs': [
          '<(SHARED_INTERMEDIATE_DIR)/include',
        ]
      }
    },
  ]
}
