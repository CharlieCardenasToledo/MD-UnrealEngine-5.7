# Building Unreal Engine from Source

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source

> Application Version: 5.7

## Building Unreal Engine from Source

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "paragraph",
        "content": "\nRead about <a data-document-id=\"3222194\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-and-software-specifications-for-unreal-engine?application_version=5.5\">Hardware and Software Specifications</a>, and make sure that <strong>Microsoft Visual Studio</strong> is installed prior to building <strong>Unreal Engine (UE)</strong> from source. Also, depending on your system's specifications, it may take between 10 and 40 minutes to compile the Engine.\n\n",
        "settings": {
          "is_hidden": false
        }
      },
      {
        "type": "enhanced_list",
        "style": "ordered",
        "items": [
          [
            {
              "type": "paragraph",
              "content": "\nInside the root directory, where you <a data-anchor-id=\"22364\" data-document-id=\"3228589\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine#downloading-the-source-code\">downloaded and adjusted the UE Source Code</a> run <code>GenerateProjectFiles.bat</code> to set-up your project files.\n\n",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 26388915,
              "caption": "",
              "alt_text": "Generate project files",
              "image": {
                "id": 26388915,
                "file_name": "image.png",
                "file_size": 64047,
                "content_type": "image/png",
                "created_at": "2026-01-14T18:40:13.717+00:00",
                "height": 509,
                "width": 674,
                "storage_key": "5811d4a1-3f26-416b-8dba-b09fd5392af6",
                "context": "documentation"
              },
              "storage_key": "5811d4a1-3f26-416b-8dba-b09fd5392af6",
              "context": "documentation",
              "width": null,
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "callout",
              "callout_type": "warning",
              "blocks": [
                {
                  "type": "paragraph",
                  "content": "\nAll project files are intermediate (<code>[UERoot]\\Engine\\Intermediate\\ProjectFiles</code>). You must generate project files each time you sync a new build to ensure they are up to date. If you delete your <code>Intermediate</code> folder, you must regenerate project files using the <code>GenerateProjectFiles</code> batch file.\n\n",
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
          [
            {
              "type": "paragraph",
              "content": "Load the project into Visual Studio by double-clicking <code>UE5.sln</code>.",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 26388916,
              "caption": "",
              "alt_text": "Load the project",
              "image": {
                "id": 26388916,
                "file_name": "image.png",
                "file_size": 71472,
                "content_type": "image/png",
                "created_at": "2026-01-14T18:41:59.848+00:00",
                "height": 559,
                "width": 674,
                "storage_key": "ec3836b4-dd49-46d3-99ea-4f16335ca57d",
                "context": "documentation"
              },
              "storage_key": "ec3836b4-dd49-46d3-99ea-4f16335ca57d",
              "context": "documentation",
              "width": null,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Set your solution configuration to <strong>Development Editor</strong>.",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 26388931,
              "caption": "",
              "alt_text": "Set solution configuration to Development Editor",
              "image": {
                "id": 26388931,
                "file_name": "image.png",
                "file_size": 30713,
                "content_type": "image/png",
                "created_at": "2026-01-14T18:43:55.128+00:00",
                "height": 422,
                "width": 645,
                "storage_key": "41110de2-2463-4416-b584-a3dd94b23e5a",
                "context": "documentation"
              },
              "storage_key": "41110de2-2463-4416-b584-a3dd94b23e5a",
              "context": "documentation",
              "width": null,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Set your solution platform to <strong>Win64</strong>.",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 26388932,
              "caption": "",
              "alt_text": "Set solution platform to Win64",
              "image": {
                "id": 26388932,
                "file_name": "image.png",
                "file_size": 13733,
                "content_type": "image/png",
                "created_at": "2026-01-14T18:45:07.663+00:00",
                "height": 175,
                "width": 645,
                "storage_key": "dc34475c-5847-48ce-94e5-6458e3f01504",
                "context": "documentation"
              },
              "storage_key": "dc34475c-5847-48ce-94e5-6458e3f01504",
              "context": "documentation",
              "width": null,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Right-click the <strong>UE5</strong> target and select <strong>Build</strong>.",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 26388933,
              "caption": "",
              "alt_text": "Build the UE target",
              "image": {
                "id": 26388933,
                "file_name": "image.png",
                "file_size": 24759,
                "content_type": "image/png",
                "created_at": "2026-01-14T18:45:49.055+00:00",
                "height": 419,
                "width": 479,
                "storage_key": "f58079aa-393a-4c4a-b3f3-c36957549ebd",
                "context": "documentation"
              },
              "storage_key": "f58079aa-393a-4c4a-b3f3-c36957549ebd",
              "context": "documentation",
              "width": null,
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
    "macos": [
      {
        "type": "paragraph",
        "content": "Read about <a data-document-id=\"3222194\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-and-software-specifications-for-unreal-engine?application_version=5.5\">Hardware and Software Specifications</a>, \n\n and make sure that <strong>XCode</strong> is installed prior to building <strong>Unreal Engine (UE)</strong> from source. Also, depending on your system's specifications, it may take between 10 and 40 minutes to compile the Engine.\n",
        "settings": {
          "is_hidden": false
        }
      },
      {
        "type": "enhanced_list",
        "style": "ordered",
        "items": [
          [
            {
              "type": "paragraph",
              "content": "\nInside the root directory, run <code>GenerateProjectFiles.command</code> to set up your project files.\n\n",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "\nLoad the project into XCode by double-clicking <code>UE5.xcodeproj</code>.\n\n",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "\nTo set your build target, select <strong>UnrealEditor - Mac</strong> for <strong>My Mac</strong> in the title bar.\n\n",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 26389011,
              "caption": "",
              "alt_text": "Set your Mac build target",
              "image": {
                "id": 26389011,
                "file_name": "image.png",
                "file_size": 181173,
                "content_type": "image/png",
                "created_at": "2026-01-14T18:52:50.716+00:00",
                "height": 739,
                "width": 544,
                "storage_key": "af909bf0-0b7f-4dc8-a5da-4272135ea618",
                "context": "documentation"
              },
              "storage_key": "af909bf0-0b7f-4dc8-a5da-4272135ea618",
              "context": "documentation",
              "width": null,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "\nTo build the project, select <strong>Product &gt; Build</strong>.\n\n",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 26389012,
              "caption": "",
              "alt_text": "Build project",
              "image": {
                "id": 26389012,
                "file_name": "image.png",
                "file_size": 93658,
                "content_type": "image/png",
                "created_at": "2026-01-14T18:53:51.562+00:00",
                "height": 338,
                "width": 867,
                "storage_key": "65879e2d-d685-4b88-8a16-6243ab7ac806",
                "context": "documentation"
              },
              "storage_key": "65879e2d-d685-4b88-8a16-6243ab7ac806",
              "context": "documentation",
              "width": null,
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
    "linux": [
      {
        "type": "paragraph",
        "content": "\n<strong>Unreal Engine (UE)</strong> development and support teams currently use the latest version of <strong>Ubuntu</strong>;\n as a result, we may not be able to provide support for other Linux \ndistributions (including other versions of Ubuntu). Additionally, read \nabout , and make sure your system has at least one hundred (100) gigabytes of disk space before performing\nthe following steps.\n\n",
        "settings": {
          "is_hidden": false
        }
      },
      {
        "type": "enhanced_list",
        "style": "ordered",
        "items": [
          [
            {
              "type": "paragraph",
              "content": "\nInside the root directory, run <code>Setup.sh</code> from the terminal to setup the files needed to generate the project files.\n\n",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 26389013,
              "caption": "",
              "alt_text": "Set up project files",
              "image": {
                "id": 26389013,
                "file_name": "image.png",
                "file_size": 26747,
                "content_type": "image/png",
                "created_at": "2026-01-14T18:55:08.605+00:00",
                "height": 87,
                "width": 789,
                "storage_key": "d0f6e69d-394d-45c6-9cba-0d819b00efdc",
                "context": "documentation"
              },
              "storage_key": "d0f6e69d-394d-45c6-9cba-0d819b00efdc",
              "context": "documentation",
              "width": null,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "\nNow, run <code>GenerateProjectFiles.sh</code> from the terminal to generate your project files.\n\n",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 26389014,
              "caption": "",
              "alt_text": "Run GenerateProjectFiles",
              "image": {
                "id": 26389014,
                "file_name": "image.png",
                "file_size": 71525,
                "content_type": "image/png",
                "created_at": "2026-01-14T18:55:56.534+00:00",
                "height": 201,
                "width": 789,
                "storage_key": "7fcbb564-531b-4227-b1b4-ede74d3150f7",
                "context": "documentation"
              },
              "storage_key": "7fcbb564-531b-4227-b1b4-ede74d3150f7",
              "context": "documentation",
              "width": null,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "To build the project, run <strong>make</strong> from the terminal.",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 26389015,
              "caption": "",
              "alt_text": "Build the project using the make command",
              "image": {
                "id": 26389015,
                "file_name": "image.png",
                "file_size": 63144,
                "content_type": "image/png",
                "created_at": "2026-01-14T18:58:01.281+00:00",
                "height": 172,
                "width": 789,
                "storage_key": "b290a7d7-7e83-45e6-84c9-886886f63b12",
                "context": "documentation"
              },
              "storage_key": "b290a7d7-7e83-45e6-84c9-886886f63b12",
              "context": "documentation",
              "width": null,
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
        "type": "paragraph",
        "content": "Depending on your system's specifications, it may take anywhere from ten minutes to over an hour to compile the engine. If you want to shorten the time it takes to compile the engine from source, we recommend compiling the source code on a machine that has at least eight (8) gigabytes of RAM, with a multi-core processor having at least eight (8) cores (including hyperthreading).",
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

## Running the Editor

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "enhanced_list",
        "style": "ordered",
        "items": [
          [
            {
              "type": "paragraph",
              "content": "\nSet your startup project by right-clicking the <strong>UE5</strong> target and selecting <strong>Set as StartUp Project</strong>.\n\n",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 26389080,
              "caption": "",
              "alt_text": "Set as Startup Project",
              "image": {
                "id": 26389080,
                "file_name": "image.png",
                "file_size": 35657,
                "content_type": "image/png",
                "created_at": "2026-01-14T19:02:33.761+00:00",
                "height": 624,
                "width": 479,
                "storage_key": "17b98744-84b8-4a22-8cf0-8e30851abcc9",
                "context": "documentation"
              },
              "storage_key": "17b98744-84b8-4a22-8cf0-8e30851abcc9",
              "context": "documentation",
              "width": null,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "\nRight-click the <strong>UE5</strong> project, then select <strong>Debug &gt; Start New Instance</strong> to launch the Editor.\n\n",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 26389083,
              "caption": "",
              "alt_text": "Start New Instance",
              "image": {
                "id": 26389083,
                "file_name": "image.png",
                "file_size": 43376,
                "content_type": "image/png",
                "created_at": "2026-01-14T19:04:51.936+00:00",
                "height": 648,
                "width": 582,
                "storage_key": "3faf0f64-cfa3-47ca-977c-1714fbe7aa26",
                "context": "documentation"
              },
              "storage_key": "3faf0f64-cfa3-47ca-977c-1714fbe7aa26",
              "context": "documentation",
              "width": null,
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "callout",
              "callout_type": "tip",
              "blocks": [
                {
                  "type": "paragraph",
                  "content": "Alternatively, you can <strong>press the F5 key</strong> on your keyboard to start a new instance of the Editor.",
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
          [
            {
              "type": "paragraph",
              "content": "Congratulations! You've compiled and launched the Engine from source.",
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
    "macos": [
      {
        "type": "enhanced_list",
        "style": "ordered",
        "items": [
          [
            {
              "type": "paragraph",
              "content": "Select <strong>Product &gt; Run</strong> to launch the Editor.",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 26389084,
              "caption": "",
              "alt_text": "Launch the Editor using Run",
              "image": {
                "id": 26389084,
                "file_name": "image.png",
                "file_size": 114159,
                "content_type": "image/png",
                "created_at": "2026-01-14T19:06:30.686+00:00",
                "height": 335,
                "width": 669,
                "storage_key": "fef8e792-f64b-41da-9c14-71a2bb9966e2",
                "context": "documentation"
              },
              "storage_key": "fef8e792-f64b-41da-9c14-71a2bb9966e2",
              "context": "documentation",
              "width": null,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Congratulations! You've compiled and launched the Engine from source.",
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
    "linux": [
      {
        "type": "enhanced_list",
        "style": "ordered",
        "items": [
          [
            {
              "type": "paragraph",
              "content": "\nNavigate to the Editor's binary path by entering <code>cd Engine/Binaries/Linux/</code> into the terminal.\n\n",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "\nRun <strong>UnrealEditor</strong> to launch the editor.\n\n",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 26389085,
              "caption": "",
              "alt_text": "Launch the Editor",
              "image": {
                "id": 26389085,
                "file_name": "image.png",
                "file_size": 42842,
                "content_type": "image/png",
                "created_at": "2026-01-14T19:14:11.111+00:00",
                "height": 205,
                "width": 789,
                "storage_key": "9cc50530-1d2c-4d89-b8f9-915397d22de8",
                "context": "documentation"
              },
              "storage_key": "9cc50530-1d2c-4d89-b8f9-915397d22de8",
              "context": "documentation",
              "width": null,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Congratulations! You've compiled and launched the Engine from source.",
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
  },
  "settings": {
    "is_hidden": false
  }
}
```

## Getting Started with Unreal Engine

Learn how to use Unreal Engine by referring to the [Understanding the Basics](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine) documentation!

If you're looking to quickly get started with UE, refer to the following tutorials:

- [Programming Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-cpp-quick-start)
- [Level Designer Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "UE's in-editor help features are a great way to get your questions answered.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```
