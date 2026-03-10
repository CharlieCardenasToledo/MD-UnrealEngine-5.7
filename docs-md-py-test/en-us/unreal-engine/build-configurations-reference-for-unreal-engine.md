# Build Configurations Reference

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/build-configurations-reference-for-unreal-engine

> Application Version: 5.7

```json
{
  "type": "include",
  "excerpt_id": 61,
  "excerpt_assignment_id": 2290,
  "blocks": [
    {
      "type": "callout",
      "callout_type": "note",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Google has informed developers of a vulnerability in versions (earlier than M102) of WebRTC. Impacts, workarounds, and updates can be found <a href=\"https://eoshelp.epicgames.com/s/news/eos-news-article-MCVDBTZSVM7VAJHF4ZGJVXZM52I4?language=en_US\">here</a>.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "WYq",
  "settings": {
    "is_hidden": false
  }
}
```

## Build Configuration Descriptions

**Unreal Engine (UE)** uses a custom building method via the **Unreal Build Tool (UBT)**. This tool processes the information necessary to build the engine's reflection system, integrating your C++ code with Blueprints, replication, serialization, and garbage collection.

```json
{
  "type": "include",
  "excerpt_id": 1541,
  "excerpt_assignment_id": 2291,
  "blocks": [
    {
      "type": "paragraph",
      "content": "Every build configuration contains two keywords. The first keyword indicates the state of the engine and your game project. For instance, if you compile using a <strong>Debug</strong> configuration, the build process forgoes optimization making it easer to debug. To be clear, every configuration, even Shipping builds, produce symbols for debugging if built form Visual Studio or if <strong>Project Settings &gt; Project &gt; Packaging &gt; Project &gt; Include Debug Files</strong> is turned on in the Unreal Editor. This means that you can still debug Development and Shipping configurations, they just may not be as easy to debug as the Debug configuration. The second keyword indicates the target you are building for. For example, if you want to open a project in Unreal, you need to build with the <strong>Editor</strong> target keyword.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "enhanced_table",
      "widths": null,
      "rows": [
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Build Configuration - State",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "Description",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Debug</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This configuration builds both engine and game code in debug configuration without optimizations. This makes things slower, but is easier to debug.  If you compile your project using the <strong>Debug</strong> configuration and want to open the project with the Unreal Editor, you must use the <code>-debug</code> flag in order to see your code changes reflected in your project.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>DebugGame</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This configuration builds game code without optimizations. This configuration is ideal for debugging only game modules.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Development</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This configuration enables all but the most time-consuming engine and game code optimizations, which makes it ideal for development and performance reasons. Unreal Editor uses the <strong>Development</strong> configuration by default. Compiling your project using the <strong>Development</strong> configuration enables you to see code changes made to your project reflected in the editor.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Shipping</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This is the configuration for optimal performance and shipping your game.  This configuration strips out console commands, stats, and profiling tools.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Test</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This configuration is the <strong>Shipping</strong> configuration, but with some console commands, stats, and profiling tools enabled.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ]
      ],
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "enhanced_table",
      "widths": null,
      "rows": [
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Build Configuration - Target",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "Description",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Game</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This configuration builds a stand-alone executable version of your project, but requires cooked content specific to the platform. Please refer to the <a href=\"understanding-the-basics/packaging-projects\"></a> Reference page to learn more about cooked content.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Editor</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "To open a project in Unreal Editor and see all code changes reflected, the project must be built in an <strong>Editor</strong> configuration.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Client</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "If you are working on a multiplayer project using UE networking features, this target designates the specified project as being a Client in UE's client-server model for multiplayer games. If there is a <code>&lt;GAME_NAME&gt;Client.Target.cs</code> file, the <strong>Client</strong> build configurations will be valid.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Server</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "If you are working on a multiplayer project using UE networking features, this target designates the specified project as being a Server in UE's client-server model for multiplayer games. If there is a <code>&lt;GAME_NAME&gt;Server.Target.cs</code> file, the <strong>Server</strong> build configurations will be valid.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ]
      ],
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "xbN",
  "settings": {
    "is_hidden": false
  }
}
```

### Build Configuration for UE Solution

When compiling a UE solution, you are compiling our engine's source code together with your project's source code. The following build configurations are available when building your project this way:

|   | Debug | DebugGame | Development | Shipping | Test |
| --- | --- | --- | --- | --- | --- |
| **Game** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Editor** | ✓ | ✓ | ✓ |   |   |
| **Client** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Server** | ✓ | ✓ | ✓ | ✓ | ✓ |

### Build Configuration for UE Project

When compiling a UE project, you are only compiling your project's source code. The following build configurations are available when building your project this way:

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "enhanced_table",
        "widths": null,
        "rows": [
          [
            [
              {
                "type": "enhanced_table_header",
                "content": " ",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [
              {
                "type": "enhanced_table_header",
                "content": "Debug",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [
              {
                "type": "enhanced_table_header",
                "content": "DebugGame",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [
              {
                "type": "enhanced_table_header",
                "content": "Development",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [
              {
                "type": "enhanced_table_header",
                "content": "Shipping",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [
              {
                "type": "enhanced_table_header",
                "content": "Test",
                "settings": {
                  "is_hidden": false
                }
              }
            ]
          ],
          [
            [
              {
                "type": "paragraph",
                "content": "<strong>Game</strong>",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [],
            [
              {
                "type": "paragraph",
                "content": "✓",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [
              {
                "type": "paragraph",
                "content": "✓",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [
              {
                "type": "paragraph",
                "content": "✓",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            []
          ],
          [
            [
              {
                "type": "paragraph",
                "content": "<strong>Editor</strong>",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [],
            [
              {
                "type": "paragraph",
                "content": "✓",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [
              {
                "type": "paragraph",
                "content": "✓",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [],
            []
          ],
          [
            [
              {
                "type": "paragraph",
                "content": "<strong>Client</strong>",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [],
            [],
            [],
            [],
            []
          ],
          [
            [
              {
                "type": "paragraph",
                "content": "<strong>Server</strong>",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [],
            [],
            [],
            [],
            []
          ]
        ],
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "enhanced_table",
        "widths": null,
        "rows": [
          [
            [
              {
                "type": "enhanced_table_header",
                "content": " ",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [
              {
                "type": "enhanced_table_header",
                "content": "Debug",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [
              {
                "type": "enhanced_table_header",
                "content": "DebugGame",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [
              {
                "type": "enhanced_table_header",
                "content": "Development",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [
              {
                "type": "enhanced_table_header",
                "content": "Shipping",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [
              {
                "type": "enhanced_table_header",
                "content": "Test",
                "settings": {
                  "is_hidden": false
                }
              }
            ]
          ],
          [
            [
              {
                "type": "paragraph",
                "content": "<strong>Game</strong>",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [],
            [
              {
                "type": "paragraph",
                "content": "✓",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [
              {
                "type": "paragraph",
                "content": "✓",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [
              {
                "type": "paragraph",
                "content": "✓",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            []
          ],
          [
            [
              {
                "type": "paragraph",
                "content": "<strong>Editor</strong>",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [],
            [
              {
                "type": "paragraph",
                "content": "✓",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [
              {
                "type": "paragraph",
                "content": "✓",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [],
            []
          ],
          [
            [
              {
                "type": "paragraph",
                "content": "<strong>Client</strong>",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [],
            [],
            [],
            [],
            []
          ],
          [
            [
              {
                "type": "paragraph",
                "content": "<strong>Server</strong>",
                "settings": {
                  "is_hidden": false
                }
              }
            ],
            [],
            [],
            [],
            [],
            []
          ]
        ],
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "linux": [
      {
        "type": "callout",
        "callout_type": "warning",
        "blocks": [
          {
            "type": "paragraph",
            "content": "We do not currently provide a binary installer of Unreal Engine for Linux.<br>\n\t\tLinux users should refer to the <a data-document-id=\"3228639\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/build-configurations-reference-for-unreal-engine?application_version=5.5\">Build Configuration for UE Solution</a> section.<br>\n        Refer to our <a href=\"understanding-the-basics/installing-unreal-engine\"></a> documentation to learn how to build Unreal Engine from source.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "settings": {
          "is_hidden": false
        }
      }
    ]
  },
  "settings": {
    "is_hidden": false
  }
}
```
