# Android Development Requirements

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/android-development-requirements-for-unreal-engine

> Application Version: 5.7

This page contains the software development kit (SDK) requirements needed to develop Unreal Engine (UE) projects for Android devices, as well as compatible hardware for the current version of UE.

## Current SDK Information

```json
{
  "type": "include",
  "excerpt_id": 2662,
  "excerpt_assignment_id": 2605,
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
                  "content": "Minimum for compilation: SDK 35",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Default target SDK for shipping on devices: 35",
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
  "excerpt_hash_id": "260E",
  "settings": {
    "is_hidden": false
  }
}
```

## Current Compatible Devices

UE supports Android devices meeting the following specifications:

```json
{
  "type": "include",
  "excerpt_id": 1061,
  "excerpt_assignment_id": 2602,
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

```json
{
  "type": "include",
  "excerpt_id": 1062,
  "excerpt_assignment_id": 2603,
  "blocks": [
    {
      "type": "header",
      "content": "Version History",
      "level": 2,
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
              "content": "UE Version",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "Android Studio Version",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "Minimum Android SDK Version",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "Android NDK Version",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "Notes",
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
              "content": "5.7",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Koala 2024.1.2 Patch 1 September 17, 2024",
              "settings": {
                "is_hidden": false
              }
            }
          ],
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
              "content": "NDK r27c",
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
              "content": "5.6",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "paragraph",
              "content": "<br>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Koala 2024.1.2 August 29, 2024",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Recommended: SDK 34 ",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "paragraph",
              "content": "Minimum: SDK 34",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "NDK r27c",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Supports 16kb memory page size.",
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
              "content": "5.5",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Koala 2024.1.2 August 29, 2024",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Recommended: SDK 34\n",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "paragraph",
              "content": "Minimum: SDK 34",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "NDK r25b",
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
              "content": "5.3-5.4",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Flamingo 2022.2.1 Patch 2 May 24, 2023",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Recommended: SDK 33\n",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "paragraph",
              "content": "Minimum: SDK 30",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "NDK r25b",
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
              "content": "5.1-5.2",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Android Studio 4.0",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Recommended: SDK 32\n",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "paragraph",
              "content": "Minimum: SDK 30",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "NDK r25b",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "While SDK 30 is the minimum needed to compile on your system, SDK 26 is the minimum SDK you can target for shipping projects on devices.",
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
              "content": "5.0",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Android Studio 4.0",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "SDK 23",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "NDK r21e",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Minimum SDK version required to use Android File Server (AFS) is 26.",
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
  "excerpt_hash_id": "2Gx",
  "settings": {
    "is_hidden": false
  }
}
```
