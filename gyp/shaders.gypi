{
  'targets': [
    {
      'target_name': 'shaders',
      'type': 'none',
      'hard_dependency': 1,
      'actions': [
        {
          'action_name': 'Build Shaders',
          'inputs': [
            '<(toto)/scripts/build-shaders.py', # MGDESIGN
             '<!@(python includeglsl.py)'  # find src "*.glsl"
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/include/mbgl/shader/shaders.hpp',
            '<(SHARED_INTERMEDIATE_DIR)/src/shader/shaders_gl.cpp',
            '<(SHARED_INTERMEDIATE_DIR)/src/shader/shaders_gles2.cpp',
          ],
          'action': ['<@(_inputs)', '<(SHARED_INTERMEDIATE_DIR)', '<@(_inputs)'],
        }
      ],
      'direct_dependent_settings': {
        'sources': [
            '<(SHARED_INTERMEDIATE_DIR)/include/mbgl/shader/shaders.hpp',
            '<(SHARED_INTERMEDIATE_DIR)/src/shader/shaders_gl.cpp',
            '<(SHARED_INTERMEDIATE_DIR)/src/shader/shaders_gles2.cpp'
        ],
        'include_dirs': [
          '<(SHARED_INTERMEDIATE_DIR)/include/',
        ]
      }
    },
  ]
}
