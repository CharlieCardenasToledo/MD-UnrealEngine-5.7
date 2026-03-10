# iOS and tvOS Development Requirements

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ios-ipados-and-tvos-development-requirements-for-unreal-engine

> Application Version: 5.7

This page contains the software development kit (SDK) requirements needed to develop Unreal Engine (UE) projects for iOS, iPadOS, and tvOS devices, as well as compatible hardware for the current version of UE.

## SDK Information

```json
{
  "type": "include",
  "excerpt_id": 1063,
  "excerpt_assignment_id": 2253,
  "blocks": [
    {
      "type": "enhanced_list",
      "style": "unordered",
      "items": [
        [
          {
            "type": "paragraph",
            "content": "Current UE Version: 5.6",
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
                  "content": "Supported Target SDK versions: iOS 15 or later",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Recommended macOS and Xcode Versions",
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
                        "content": "macOS Sonoma 14.7",
                        "settings": {
                          "is_hidden": false
                        }
                      }
                    ],
                    [
                      {
                        "type": "paragraph",
                        "content": "Xcode \n\n16.1",
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
                  "content": "Minimum macOS and Xcode Versions",
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
                        "content": "macOS Sonoma 14.5 ",
                        "settings": {
                          "is_hidden": false
                        }
                      }
                    ],
                    [
                      {
                        "type": "paragraph",
                        "content": "Xcode 16",
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
        ]
      ],
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "llQ",
  "settings": {
    "is_hidden": false
  }
}
```

## Compatible Devices

UE 5.5 supports iOS, iPadOS, and tvOS devices that support the operating system version 15 and higher for their respective SDKs and use an Apple A8 processor or later. The following are the minimum compatible device models:

```json
{
  "type": "include",
  "excerpt_id": 976,
  "excerpt_assignment_id": 2254,
  "blocks": [
    {
      "type": "enhanced_list",
      "style": "unordered",
      "items": [
        [
          {
            "type": "paragraph",
            "content": "iOS 15",
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
                  "content": "iPhone 6S or later",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "iPod Touch 7th generation",
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
            "content": "iPadOS 15",
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
                  "content": "iPad 5th generation or later",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "iPad Air 2 or later",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "iPad Mini 4 or later",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "iPad Pro (all models)",
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
            "content": "tvOS 15",
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
                  "content": "Apple TV HD",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Apple TV 4K (first generation)",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Apple TV 4K (second generation)",
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
    },
    {
      "type": "callout",
      "callout_type": "note",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Apple A8/A8X-based devices (iPad Air 2, iPad Mini 4 and Apple TV HD) require a project setting for support to be enabled. Some rendering features may be limited on A8/A8X devices.",
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
  "excerpt_hash_id": "XbP",
  "settings": {
    "is_hidden": false
  }
}
```

## Version History

| UE Version | Supported macOS Versions | Xcode Version |
| --- | --- | --- |
| 5.6 | macOS Sonoma 14.5 Latest macOS 14 | Xcode 16 |
| 5.5 | macOS Ventura 13 Latest macOS 14 | Xcode 15.2 |
| 5.4 | macOS Ventura 13 Latest macOS 14 | Xcode 14.1 |
| 5.2-5.3 | macOS Monterey 12.5 Latest macOS Ventura 13 | Xcode 14.1 |
| 5.1 | macOS Monterey 12 Latest macOS 13 Ventura | Xcode 14, Xcode 13.4.1 |
| 5.0 | macOS Catalina 10.15.7 macOS Big Sur 11.6.4 Latest macOS Monterey 12 | Xcode 13, Xcode 12.4 |
