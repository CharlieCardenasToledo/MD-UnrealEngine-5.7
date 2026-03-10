# Timelines

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/timelines-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 702,
        "excerpt_assignment_id": 415,
        "blocks": [
          {
            "type": "paragraph",
            "content": "<strong>Timeline nodes</strong> are special nodes within Blueprints that provide time-based animation to be quickly designed and played back based on <strong>events</strong>, <strong>floats</strong>,<strong>vectors</strong>, or <strong>colors</strong> that can be triggered at keyframes along the timeline.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Timelines can be edited directly inside the Blueprint editor by <strong>Double-clicking</strong> on the Timeline in the Graph tab or in the My Blueprint tab. They are specifically built for handling simple, non-cinematic tasks such as opening doors, altering lights, or performing other time-centric manipulations to Actors within a scene.They are similar to <a data-document-id=\"3231482\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview\">level sequences</a> as they both provide values such as floats, vectors, and colors to be interpolated between keyframes along the timeline.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Inputs and Outputs",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24528012,
            "caption": "",
            "alt_text": "image alt text",
            "image": {
              "id": 24528012,
              "file_name": "image_0.jpg",
              "file_size": 15601,
              "content_type": "image/jpeg",
              "created_at": "2025-04-22T18:16:18.396+00:00",
              "height": 267,
              "width": 337,
              "storage_key": "4265bc4d-151d-4597-a271-12fb895bdd74",
              "context": "documentation"
            },
            "storage_key": "4265bc4d-151d-4597-a271-12fb895bdd74",
            "context": "documentation",
            "width": 336,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Timelines come with the following input and output pins:",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "<strong>Input Pins</strong>",
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
                    "content": "Item",
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
                ],
                [
                  {
                    "type": "enhanced_table_header",
                    "content": " ",
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
                    "content": "<strong>Play</strong>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Causes the Timeline to play forward from its current time.",
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
                    "content": "<strong>Play from Start</strong>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Causes the Timeline to play forward from the beginning.",
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
                    "content": "<strong>Stop</strong>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Freezes the playback of the Timeline at the current time.",
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
                    "content": "<strong>Reverse</strong>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Plays the Timeline backwards from its current time.",
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
                    "content": "<strong>Reverse from End</strong>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Plays the Timeline backwards starting from the end.",
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
                    "content": "<strong>Set New Time</strong>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Sets the current time to the value set (or input) in the New Time input.",
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
                    "content": "<strong>New Time</strong>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "This data pin takes a float value representing time in seconds, to which the Timeline can jump when the Set New Time input is called.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                []
              ]
            ],
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "<strong>Output Pins</strong>",
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
                    "content": "Item",
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
                ],
                [
                  {
                    "type": "enhanced_table_header",
                    "content": " ",
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
                    "content": "<strong>Update</strong>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Outputs an execution signal as soon as the Timeline is called.",
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
                    "content": "<strong>Finished</strong>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Outputs an execution signal when playback ends. This is not triggered by the Stop function.",
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
                    "content": "<strong>Direction</strong>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Outputs enum data indicating the direction the Timeline is playing.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                []
              ]
            ],
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Timelines may have any number of additional output data pins reflecting the types of tracks created within them. These include Float, Vector, and Event tracks.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "z2L",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 703,
        "excerpt_assignment_id": 416,
        "blocks": [
          {
            "type": "header",
            "content": "Overview (C++)",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "<strong>UTimelineComponent</strong> holds a series of <strong>events</strong>, <strong>floats</strong>, <strong>vectors</strong> or <strong>colors</strong> with their associated <strong>keyframes</strong>. They are inherited from <a data-document-id=\"3578419\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/Components/UActorComponent?application_version=5.5\">UActorComponents</a>",
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
                "content": "For further documentation, please see the overview about <a data-document-id=\"3229485\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/components-in-unreal-engine\">Actor Components</a>",
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
            "type": "paragraph",
            "content": "Timelines allow for time-based animation which are played from Events that can be triggered at keyframes along the timeline. They can be used to handle simple, non-cinematic tasks such as opening doors, altering lights, or performing other time-centric manipulations to Actors within a scene. They are similar to <a data-document-id=\"3231482\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview\">level sequences</a> as they both provide values such as floats, vectors, and colors to be interpolated between keyframes along the timeline.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Inputs and Outputs",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "UTimelineComponents have robust methods that can be extended in native code, refer to the <a data-document-id=\"3582043\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/Components/UTimelineComponent?application_version=5.5\">UTimelineComponent</a> API reference for further documentation. If you would like to see examples on how to utilize Timeline Components in the engine, see one of the Timeline Example links in the section below.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "ExampleTimeline.h",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "/** Start playback of timeline */\n\tUFUNCTION(BlueprintCallable, Category=&quot;Components|Timeline&quot;)\n\tENGINE_API void Play();\n\n\t/** Start playback of timeline from the start */\n\tUFUNCTION(BlueprintCallable, Category=&quot;Components|Timeline&quot;)\n\tENGINE_API void PlayFromStart();\n\n\t/** Start playback of timeline in reverse */\n\tUFUNCTION(BlueprintCallable, Category=&quot;Components|Timeline&quot;)\n",
            "lines_of_code": 37,
            "id": 40436,
            "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQzNiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjA4OjExKzAwOjAwIn0=--dd42d4f0250ba95d1606cc127d728bcc49dc02ecc0faef09965048df95e1f8ba",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "5V9",
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

## Timeline Examples

- [Related Document](en-us/unreal-engine/timelines-in-unreal-engine.md)
