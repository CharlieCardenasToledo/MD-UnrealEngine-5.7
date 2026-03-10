# Android Support

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/android-support-for-unreal-engine

> Application Version: 5.7

**Unreal Engine** supports publishing to **Android** mobile devices and has several features to help in publishing to the **Google Play Store**. This section contains guides for setting up your Android development environment, how to use Android features and services, and how to prepare your game to ship.

## Current SDK Requirements

```json
{
  "type": "include",
  "excerpt_id": 1060,
  "excerpt_assignment_id": 1382,
  "blocks": [
    {
      "type": "callout",
      "callout_type": "warning",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Since August 31, 2024, Google Play Store requires apps to target Android 14, which requires API level 34. To publish new apps on the Google Play Store, you must update to UE 5.4.4 or newer for target SDK 34 support. Apps built with previous versions of UE will no longer submit successfully.  <br><br>For more information, see the <a href=\"https://developer.android.com/google/play/requirements/target-sdk\">Android documentation on Google Play's target API level requirement</a>.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "enhanced_list",
      "style": "unordered",
      "items": [
        [
          {
            "type": "paragraph",
            "content": "Current UE Version: 5.7",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Android Studio Version: Koala 2024.1.2 Patch 1 September 17, 2024",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Android SDK:",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "enhanced_list",
            "style": "unordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Recommended: SDK 35",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Minimum for compilation: SDK 34",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Default target SDK for shipping on devices: 34",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Minimum install SDK level: 26",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "callout",
                  "callout_type": "note",
                  "blocks": [
                    {
                      "type": "paragraph",
                      "content": "Different stores have their own target SDK minimum requirements, which may differ from that mentioned above.",
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
            ],
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "NDK Version:  r27c",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Build-tools: 35.0.1",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Java runtime: OpenJDK 21.0.3 2024-04-16",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "AGDE v23.2.91+  required for <a data-document-id=\"3235552\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/debugging-unreal-engine-projects-for-android-in-visual-studio-with-the-agde-plugin\">AGDE debugging</a>. ",
            "settings": {
              "is_hidden": false
            }
          }
        ]
      ],
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "Aja",
  "settings": {
    "is_hidden": false
  }
}
```

## Current Device Compatibility

The current version of Unreal Engine supports Android devices meeting the following specifications:

```json
{
  "type": "include",
  "excerpt_id": 1061,
  "excerpt_assignment_id": 1383,
  "blocks": [
    {
      "type": "enhanced_list",
      "style": "unordered",
      "items": [
        [
          {
            "type": "paragraph",
            "content": "Android 8 or higher",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "64-bit Arm-based CPU",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "  UE 5.6 supports both 4KB and 16KB page sizes",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Compatible GPUs",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "enhanced_list",
            "style": "unordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Mali T8xx, G68, G71, G72, G76, G77, G78, or G7xx series",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Adreno 5xx, 6xx or 7xx series",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "PowerVR GM9xxx series",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Samsung Xclipse 9xx series",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ]
            ],
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Compatible Graphics APIs",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "enhanced_list",
            "style": "unordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "OpenGL ES 3.2",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Vulkan 1.1 on Android 10 or later devices with compatible drivers",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ]
            ],
            "settings": {
              "is_hidden": false
            }
          }
        ]
      ],
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "WjP",
  "settings": {
    "is_hidden": false
  }
}
```

## Getting Started

- [Related Document](en-us/unreal-engine/getting-started-and-setup-for-android-projects-in-unreal-engine.md)

## Development Guides

- [Related Document](en-us/unreal-engine/developing-guides-for-android-in-unreal-engine.md)

## Packaging and Publishing

- [Related Document](en-us/unreal-engine/packaging-and-publishing-android-projects-in-unreal-engine.md)

## Debugging

- [Related Document](en-us/unreal-engine/debugging-for-android-devices-in-unreal-engine.md)

## Optimization

- [Related Document](en-us/unreal-engine/optimization-guides-for-android-in-unreal-engine.md)
