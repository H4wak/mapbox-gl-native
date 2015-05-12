{
  'variables': {
    'install_prefix%': '',
    'conditions': [
      ['OS == "mac"', {
        'target_arch%': 'x64',
      }],
      ['OS == "win"', { # MGDESIGN
        'target_arch%': 'ia32',
      }],
    ['OS != "mac" and OS != "win"', { 
        'target_arch%': '<(target_arch)',
      }],
    ],
  },
  'target_defaults': {
    'default_configuration': 'Release',
    'conditions': [
      ['OS=="mac"', {
        'xcode_settings': {
          'CLANG_CXX_LIBRARY': 'libc++',
          'CLANG_CXX_LANGUAGE_STANDARD': 'c++11',
          'GCC_VERSION': 'com.apple.compilers.llvm.clang.1_0',
          'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
          'GCC_ENABLE_CPP_RTTI': 'YES',
          'OTHER_CPLUSPLUSFLAGS': [
            '-Werror',
            '-Wall',
            '-Wextra',
            '-Wshadow',
            '-Wno-variadic-macros',
            '-frtti',
            '-fexceptions',
          ],
          'GCC_WARN_PEDANTIC': 'YES',
          'GCC_WARN_UNINITIALIZED_AUTOS': 'YES_AGGRESSIVE',
          'MACOSX_DEPLOYMENT_TARGET': '10.9',
        },
      }, {
        'cflags_cc': [
          '-std=c++11',
          '-Werror',
          '-Wall',
          '-Wextra',
          '-Wshadow',
          '-Wno-variadic-macros',
          '-Wno-error=unused-parameter',
          '-Wno-unknown-warning-option',
          '-frtti',
          '-fexceptions',
        ],
      }],
      ['OS=="linux"', {
        'cflags_cc': [
          '-Wno-unknown-pragmas', # We are using '#pragma mark', but it is only available on Darwin.
        ],
      }],
      ['OS=="win"', { # # MGDESIGN
        'cflags_cc': [
          '-Wno-unknown-pragmas', # We are using '#pragma mark', but it is only available on Darwin.
        ],
        }],
      ['target_arch == "arm"', {
        # arm
      }], # target_archs == "arm"
      ['target_arch == "ia32"', {
        'xcode_settings': {
          'ARCHS': ['i386'],
        },
      }], # target_archs == "ia32"
      ['target_arch == "mipsel"', {
        # mipsel
      }], # target_archs == "mipsel"
      ['target_arch == "x64"', {
        'xcode_settings': {
          'ARCHS': ['x86_64'],
        },
      }],
    ],
    'target_conditions': [
      ['_type == "static_library"', {
        'conditions': [
          ['OS=="mac"', {
            'xcode_settings': {
              'OTHER_CPLUSPLUSFLAGS': [ '-fPIC' ],
              'SKIP_INSTALL': 'YES',
            },
          }, {
            'cflags_cc': [ '-fPIC' ],
          }],
          ['host == "ios"', { 
            'xcode_settings': {
              'SDKROOT': 'iphoneos',
              'SUPPORTED_S': 'iphonesimulator iphoneos',
              'IPHONEOS_DEPLOYMENT_TARGET': '7.0',
              'TARGETED_DEVICE_FAMILY': '1,2',
              'GCC_VERSION': 'com.apple.compilers.llvm.clang.1_0',
              'CODE_SIGN_IDENTITY': 'iPhone Developer',
            },
            'configurations': {
              'Release': {
                'xcode_settings': {
                  'ARCHS': [ "armv7", "armv7s", "arm64", "i386", "x86_64" ],
                },
              },
            },
          }],
        ],
      }],
    ],
    'configurations': {
      'Debug': {
        'defines':['DEBUG=1'],
        'cflags': ['-g', '-O0'],
        'msbuild_settings': {
          'ClCompile': {
            'Optimization': 'Disabled', # /Od
            'conditions': [
              ['OS == "win" and component == "shared_library"', {
                'RuntimeLibrary': 'MultiThreadedDebugDLL', # /MDd
              }, {
                'RuntimeLibrary': 'MultiThreadedDebug', # /MTd
              }],
            ],
          },
          'Link': {
            'GenerateDebugInformation' : 'true', # /POUR LE DEBUG WINDOWS VISUAL
            #'LinkIncremental': 'true', # /INCREMENTAL
          },
          #'': {
          # 'LinkIncremental': 'true', # /INCREMENTAL
          #},
        },
        'xcode_settings': {
          'GCC_OPTIMIZATION_LEVEL': '0', # -O0
        },
      }, # Debug
      'Release': {
        'cflags': ['-O3'], 
        'msbuild_settings':{
          'ClCompile': {
            'Optimization': 'MaxSpeed', # /O2
            'InlineFunctionExpansion': 'AnySuitable', # /Ob2
            'conditions': [
              ['OS == "win" and component == "shared_library"', {
                'RuntimeLibrary': 'MultiThreadedDLL', # /MD
              }, {
                'RuntimeLibrary': 'MultiThreaded', # /MT
              }],
            ],
          },
          'Link': {
            #'LinkIncremental': 'false', # /INCREMENTAL:NO
            'OptimizeReferences': 'true', # /OPT:REF
          },
          #'': {
          # 'LinkIncremental': 'false', # /INCREMENTAL:NO
          #},
        },
        'xcode_settings': {
          'GCC_OPTIMIZATION_LEVEL': '3', # -O3
        },
      }, # Release
    },
    'variables': {
      'component%': 'static_library',
    },
  }, # target_defaults
}
