# Artist Quick Start

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-quick-start-in-unreal-engine

> Application Version: 5.7

![Materials Header](https://dev.epicgames.com/community/api/documentation/image/713a4888-70a7-4d53-98cb-c06fb6539dfa)

_Click image for full size._

This quick start guide shows you how to add assets to your **Unreal Engine (UE5)** games. By the end of this guide, you'll know how to use the **Project Browser** to create new projects and navigate the **Content Browser** to find and add content. You'll also know where to find information on the **FBX Content Pipeline** while learning how to use the **Material Editor** to modify **Materials** before applying them to a **Static Mesh Actor**.

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "include",
        "excerpt_id": 113,
        "excerpt_assignment_id": 321,
        "blocks": [
          {
            "type": "header",
            "content": "1. Required Project Setup",
            "level": 2,
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
                  "content": "Open <b>Unreal Engine</b> from the Launcher.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Create a new Project using the <b>Games &gt; Blank</b> template using the following settings:",
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
                        "content": "<b>C++</b> enabled",
                        "settings": {
                          "is_hidden": false
                        }
                      }
                    ],
                    [
                      {
                        "type": "paragraph",
                        "content": "<b>With Starter Content</b> enabled",
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
                  "content": "You'll need to enter a project name, so use <b>Artist_QuickStart</b>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "You can now click <b>Create Project</b> and get started.",
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
            "content": "The <strong>Unreal Editor</strong> now opens your new project. <strong>Visual Studio</strong> also opens and loads the solution file your project created.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "2. Creating Folders",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "It's always good practice to keep your project's content organized. \nThe first thing you're going to learn is how to create a folder that \nwill store your imported content.",
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
          },
          {
            "type": "callout",
            "callout_type": "note",
            "blocks": [
              {
                "type": "paragraph",
                "content": "Before you get started: Download Quick Start Assets from the following link.",
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
                      "content": "<a href=\"https://d1iv7db44yhgxn.cloudfront.net/documentation/attachments/7ba2327f-a20d-4f14-af5a-23617888fb2e/quickstartsampleassets.zip\">Sample Assets</a>",
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
                  "content": "Extract the downloaded assets to a location on your computer. <br>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24446489,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24446489,
                    "file_name": "02-extracted-content.png",
                    "file_size": 50530,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T16:32:02.222+00:00",
                    "height": 496,
                    "width": 1188,
                    "storage_key": "46c21a9e-691c-4591-97e0-d86396d2fb79",
                    "context": "documentation"
                  },
                  "storage_key": "46c21a9e-691c-4591-97e0-d86396d2fb79",
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
                  "content": "From the <b>Content Browser</b> inside the Editor, click the <b>Add New</b> button.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24446563,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24446563,
                    "file_name": "03-add-new-button.png",
                    "file_size": 49865,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T16:34:10.476+00:00",
                    "height": 516,
                    "width": 954,
                    "storage_key": "6e470953-a5fb-4326-9167-a033dde0aa5f",
                    "context": "documentation"
                  },
                  "storage_key": "6e470953-a5fb-4326-9167-a033dde0aa5f",
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
                  "content": "Select <b>New Folder</b> to create a new folder. <br>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24446636,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24446636,
                    "file_name": "04-new-folder-selection.png",
                    "file_size": 44236,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T16:35:45.026+00:00",
                    "height": 816,
                    "width": 428,
                    "storage_key": "f6f6ac45-c7f7-4d46-9928-266e7e29aedb",
                    "context": "documentation"
                  },
                  "storage_key": "f6f6ac45-c7f7-4d46-9928-266e7e29aedb",
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
                  "content": "Name the folder <b>QuickStartContent.</b>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24446643,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24446643,
                    "file_name": "05-name-quick-start-content-folder.png",
                    "file_size": 56352,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T16:38:29.909+00:00",
                    "height": 512,
                    "width": 953,
                    "storage_key": "5c11c0ac-1d97-4719-98fc-836c605fb26c",
                    "context": "documentation"
                  },
                  "storage_key": "5c11c0ac-1d97-4719-98fc-836c605fb26c",
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
                  "content": "Double-click the <b>QuickStartContent</b> folder.",
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
            "callout_type": "tip",
            "blocks": [
              {
                "type": "paragraph",
                "content": "\n<em>Naming conventions matter! Be consistent when naming folders and files.</em>\n\n",
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
            "type": "header",
            "content": "3. Importing Meshes",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "There are a few ways to add content to your UE5 project; however, we'll focus on the Content Browser's <strong>Import</strong> functionality.",
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
                  "content": "Now that you're inside the <b>QuickStartContent</b> folder, click the Content Browser's <b>Import</b> button to open a file dialog box. <br>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24446694,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24446694,
                    "file_name": "06-content-browser-import-button.png",
                    "file_size": 53530,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T16:44:03.541+00:00",
                    "height": 512,
                    "width": 952,
                    "storage_key": "f3bc1a11-a06e-43c8-8578-700e44bcf139",
                    "context": "documentation"
                  },
                  "storage_key": "f3bc1a11-a06e-43c8-8578-700e44bcf139",
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
                  "content": "Locate and select the <b>Basic_Asset1</b> and <b>Basic_Asset2</b> FBX mesh files.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24447423,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24447423,
                    "file_name": "07-import-mesh-dialog-box.png",
                    "file_size": 47291,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T17:22:13.256+00:00",
                    "height": 552,
                    "width": 1107,
                    "storage_key": "3d3accfb-efae-4fc0-b294-bbfc975781c4",
                    "context": "documentation"
                  },
                  "storage_key": "3d3accfb-efae-4fc0-b294-bbfc975781c4",
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
                  "content": "Click <b>Open</b> to begin importing the FBX mesh files to your project.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Inside the editor, the <b>FBX Import Options</b> dialog box appears. Clicking <b>Import</b> or <b>Import All</b> adds your meshes to the Project.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24447426,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24447426,
                    "file_name": "08-fbx-import-options-dialog-box.png",
                    "file_size": 64729,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T17:23:38.996+00:00",
                    "height": 1080,
                    "width": 556,
                    "storage_key": "cf8472cf-1246-439b-a05c-09b0c84e1032",
                    "context": "documentation"
                  },
                  "storage_key": "cf8472cf-1246-439b-a05c-09b0c84e1032",
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
                  "content": "Click <b>Save All</b> to save your imported meshes.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24447428,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24447428,
                    "file_name": "09-save-all-meshes-button.png",
                    "file_size": 132456,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T17:24:44.902+00:00",
                    "height": 512,
                    "width": 954,
                    "storage_key": "4de352cc-d520-41a5-b6ac-928d87f88f81",
                    "context": "documentation"
                  },
                  "storage_key": "4de352cc-d520-41a5-b6ac-928d87f88f81",
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
                  "content": "A <b>Save Content</b> dialog box appears. Click <b>Save Selected</b> to save your imported assets.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24447446,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24447446,
                    "file_name": "10-save-selected-dialog-box.png",
                    "file_size": 49894,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T17:25:49.019+00:00",
                    "height": 665,
                    "width": 1171,
                    "storage_key": "79a030d5-f179-409a-b926-df588077abf1",
                    "context": "documentation"
                  },
                  "storage_key": "79a030d5-f179-409a-b926-df588077abf1",
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
                  "content": "Navigate to the <b>QuickStartContent</b> folder, then verify UE5 created the corresponding <b>.uasset files</b>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24447448,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24447448,
                    "file_name": "11-quick-start-content-folder.png",
                    "file_size": 46155,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T17:29:03.537+00:00",
                    "height": 496,
                    "width": 1057,
                    "storage_key": "e9e2a86d-f562-4dc3-9434-47f568381e5c",
                    "context": "documentation"
                  },
                  "storage_key": "e9e2a86d-f562-4dc3-9434-47f568381e5c",
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
            "type": "callout",
            "callout_type": "tip",
            "blocks": [
              {
                "type": "paragraph",
                "content": "\n<em>Organize your assets so that you can easily find them.</em>\n\n",
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
            "type": "header",
            "content": "4. Importing Textures",
            "level": 2,
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
                  "content": "Navigate to the <b>QuickStartContent</b> folder in the Editor, then click the Content Browser's <b>Import</b> button to open a file dialog box.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24450505,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24450505,
                    "file_name": "15-save-all-textures.png",
                    "file_size": 196472,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T19:31:17.059+00:00",
                    "height": 514,
                    "width": 1377,
                    "storage_key": "68a6f950-1cd3-4be7-841b-94bc61567ffe",
                    "context": "documentation"
                  },
                  "storage_key": "68a6f950-1cd3-4be7-841b-94bc61567ffe",
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
                  "content": "Locate and select the <b>T_Rock_04_D</b> and <b>T_Rock_04_n</b> Targa (TGA) image files.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24447855,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24447855,
                    "file_name": "13-import-texture-dialog-box.png",
                    "file_size": 46850,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T17:33:37.945+00:00",
                    "height": 552,
                    "width": 1107,
                    "storage_key": "ad478237-5bc8-458b-ba65-8755c3224300",
                    "context": "documentation"
                  },
                  "storage_key": "ad478237-5bc8-458b-ba65-8755c3224300",
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
                  "content": "Click <b>Open</b> to begin importing the TGA image files to your project.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "A confirmation box appears in the lower right corner of the Unreal Editor.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24447881,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24447881,
                    "file_name": "14-texture-normal-confirmation.png",
                    "file_size": 16585,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T17:34:37.601+00:00",
                    "height": 132,
                    "width": 572,
                    "storage_key": "0819795e-1751-413f-8fb9-d9290d88fbd1",
                    "context": "documentation"
                  },
                  "storage_key": "0819795e-1751-413f-8fb9-d9290d88fbd1",
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
                  "content": "Click <b>OK</b> to accept the <b>T_Rock_04_n.TGA</b> normal map's settings.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Click <b>Save All</b> to save your imported images.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24447981,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24447981,
                    "file_name": "15-save-all-textures.png",
                    "file_size": 196472,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T17:36:32.255+00:00",
                    "height": 514,
                    "width": 1377,
                    "storage_key": "18c788b2-944b-4e48-8a12-883df1de645d",
                    "context": "documentation"
                  },
                  "storage_key": "18c788b2-944b-4e48-8a12-883df1de645d",
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
                  "content": "A <b>Save Content</b> dialog box appears.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Click <b>Save Selected</b> to save your imported assets.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to the <b>QuickStartContent</b> folder, then verify UE5 created the corresponding <b>.uasset files</b>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24448044,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24448044,
                    "file_name": "16-quick-start-content-folder-2.png",
                    "file_size": 51541,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T17:38:00.190+00:00",
                    "height": 496,
                    "width": 1057,
                    "storage_key": "e540856e-7398-4af0-8692-1f86079f8884",
                    "context": "documentation"
                  },
                  "storage_key": "e540856e-7398-4af0-8692-1f86079f8884",
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
            "type": "callout",
            "callout_type": "tip",
            "blocks": [
              {
                "type": "paragraph",
                "content": "\n<a href=\"https://www.fab.com/\">Fab</a><em> (also accessible from the <strong>Epic Launcher</strong>) is a great place to find and share content.</em>\n\n",
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
        "excerpt_hash_id": "YWa",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "include",
        "excerpt_id": 114,
        "excerpt_assignment_id": 322,
        "blocks": [
          {
            "type": "header",
            "content": "1. Required Project Setup",
            "level": 2,
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
                  "content": "Open <b>Unreal Engine</b> from the Launcher.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Create a new Project using the <b>Games &gt; Blank</b> template using the following settings:",
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
                        "content": "<b>C++</b> enabled",
                        "settings": {
                          "is_hidden": false
                        }
                      }
                    ],
                    [
                      {
                        "type": "paragraph",
                        "content": "<b>With Starter Content</b> enabled",
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
                  "content": "You'll need to enter a project name, so use <b>Artist_QuickStart</b>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "You can now click <b>Create Project</b> and get started.",
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
            "content": "The Unreal Editor now opens your new project. Visual Studio also opens and loads the solution file your project created.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "2. Creating Folders",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "It's always good practice to keep your project's content organized. \nThe first thing you're going to learn is how to create a folder that \nwill store your imported content.",
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
                "content": "Before you get started: Download Quick Start Assets from the following link.",
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
                      "content": "<a href=\"https://d1iv7db44yhgxn.cloudfront.net/documentation/attachments/7ba2327f-a20d-4f14-af5a-23617888fb2e/quickstartsampleassets.zip\">Sample Assets</a>",
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
                  "content": "Extract the downloaded assets to a location on your computer. ",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24449412,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24449412,
                    "file_name": "ExtractedContent_Mac.png",
                    "file_size": 56157,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T18:25:58.658+00:00",
                    "height": 262,
                    "width": 668,
                    "storage_key": "edd73c4d-ddce-444a-af77-68d2b398b60d",
                    "context": "documentation"
                  },
                  "storage_key": "edd73c4d-ddce-444a-af77-68d2b398b60d",
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
                  "content": "\nFrom the <b>Content Browser</b> inside the Editor, click the <b>Add New</b> button.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24449513,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24449513,
                    "file_name": "03-add-new-button.png",
                    "file_size": 49865,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T18:29:33.159+00:00",
                    "height": 516,
                    "width": 954,
                    "storage_key": "93b16c63-af4a-4e47-8145-87349550952e",
                    "context": "documentation"
                  },
                  "storage_key": "93b16c63-af4a-4e47-8145-87349550952e",
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
                  "content": "\nSelect <b>New Folder</b> to create a new folder. \n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24449532,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24449532,
                    "file_name": "04-new-folder-selection.png",
                    "file_size": 44236,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T18:31:12.150+00:00",
                    "height": 816,
                    "width": 428,
                    "storage_key": "13ece773-b319-47a2-b976-2511cb6b402c",
                    "context": "documentation"
                  },
                  "storage_key": "13ece773-b319-47a2-b976-2511cb6b402c",
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
                  "content": "\nName the folder <b>QuickStartContent.</b>\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24449533,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24449533,
                    "file_name": "05-name-quick-start-content-folder.png",
                    "file_size": 56352,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T18:33:01.142+00:00",
                    "height": 512,
                    "width": 953,
                    "storage_key": "a74de6b3-7d90-4982-b0e4-d20523ea1e9f",
                    "context": "documentation"
                  },
                  "storage_key": "a74de6b3-7d90-4982-b0e4-d20523ea1e9f",
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
                  "content": "Double-click the <b>QuickStartContent</b> folder.",
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
            "callout_type": "tip",
            "blocks": [
              {
                "type": "paragraph",
                "content": "\n<em>Naming conventions matter! Be consistent when naming folders and files.</em>\n\n",
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
            "content": "<br>",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "3. Importing Meshes",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "There are a few ways to add content to your UE5 project; however, we'll focus on the Content Browser's <strong>Import</strong> functionality.",
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
                  "content": "\nNow that you're inside the <b>QuickStartContent</b> folder, click the Content Browser's <b>Import</b> button to open a file dialog box. \n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24449699,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24449699,
                    "file_name": "06-content-browser-import-button.png",
                    "file_size": 53530,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T18:42:10.594+00:00",
                    "height": 512,
                    "width": 952,
                    "storage_key": "90a8983d-b2c9-40c2-93e2-a2fd249f5778",
                    "context": "documentation"
                  },
                  "storage_key": "90a8983d-b2c9-40c2-93e2-a2fd249f5778",
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
                  "content": "\nLocate and select the <b>Basic_Asset1</b> and <b>Basic_Asset2</b> FBX mesh files.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24449700,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24449700,
                    "file_name": "ImportMeshDialogBox_Mac.png",
                    "file_size": 55163,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T18:44:09.179+00:00",
                    "height": 242,
                    "width": 799,
                    "storage_key": "e6e780a3-79ad-47cb-b838-2b34d90cb230",
                    "context": "documentation"
                  },
                  "storage_key": "e6e780a3-79ad-47cb-b838-2b34d90cb230",
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
                  "content": "Click <b>Open</b> to begin importing the FBX mesh files to your project.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "\nInside the editor, the <b>FBX Import Options</b> dialog box appears. Clicking <b>Import</b> or <b>Import All</b> adds your meshes to the Project.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24449734,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24449734,
                    "file_name": "08-fbx-import-options-dialog-box.png",
                    "file_size": 64729,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T18:45:39.818+00:00",
                    "height": 1080,
                    "width": 556,
                    "storage_key": "497f2dc4-01d4-4611-b8ab-cc43de0ed6a8",
                    "context": "documentation"
                  },
                  "storage_key": "497f2dc4-01d4-4611-b8ab-cc43de0ed6a8",
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
                  "content": "\nClick <b>Save All</b> to save your imported meshes.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24449756,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24449756,
                    "file_name": "09-save-all-meshes-button.png",
                    "file_size": 132456,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T18:47:44.207+00:00",
                    "height": 512,
                    "width": 954,
                    "storage_key": "09b26c95-7332-4fa6-8864-233f447b2c75",
                    "context": "documentation"
                  },
                  "storage_key": "09b26c95-7332-4fa6-8864-233f447b2c75",
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
                  "content": "\nA <b>Save Content</b> dialog box appears. Click <b>Save Selected</b> to save your imported assets.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24449775,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24449775,
                    "file_name": "10-save-selected-dialog-box.png",
                    "file_size": 49894,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T18:48:47.480+00:00",
                    "height": 665,
                    "width": 1171,
                    "storage_key": "fe3b4083-c3b0-4962-b268-8823d19d3c64",
                    "context": "documentation"
                  },
                  "storage_key": "fe3b4083-c3b0-4962-b268-8823d19d3c64",
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
                  "content": "\nNavigate to the <b>QuickStartContent</b> folder, then verify UE5 created the corresponding <b>.uasset files</b>.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24449776,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24449776,
                    "file_name": "QuickStartContentFolder_Mac.png",
                    "file_size": 55706,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T18:50:44.590+00:00",
                    "height": 259,
                    "width": 668,
                    "storage_key": "fa24b4c3-17ec-49d5-a745-bfb49892e01c",
                    "context": "documentation"
                  },
                  "storage_key": "fa24b4c3-17ec-49d5-a745-bfb49892e01c",
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
            "type": "callout",
            "callout_type": "tip",
            "blocks": [
              {
                "type": "paragraph",
                "content": "\n<em>Organize your assets so that you can easily find them.</em>\n\n",
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
            "type": "header",
            "content": "4. Importing Textures",
            "level": 2,
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
                  "content": "\nNavigate to the <b>QuickStartContent</b> folder in the Editor, then click the Content Browser's <b>Import</b> button to open a file dialog box.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24450483,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24450483,
                    "file_name": "15-save-all-textures.png",
                    "file_size": 196472,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T19:30:44.441+00:00",
                    "height": 514,
                    "width": 1377,
                    "storage_key": "35ee0b2d-6e6b-4215-b09f-97d2083c1f3d",
                    "context": "documentation"
                  },
                  "storage_key": "35ee0b2d-6e6b-4215-b09f-97d2083c1f3d",
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
                  "content": "\nLocate and select the <b>T_Rock_04_D</b> and <b>T_Rock_04_n</b> Targa (TGA) image files.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24450558,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24450558,
                    "file_name": "ImportTextureDialogBox_Mac.png",
                    "file_size": 55639,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T19:34:42.100+00:00",
                    "height": 242,
                    "width": 799,
                    "storage_key": "27fde4dc-0854-4325-a1ab-375da95a4a89",
                    "context": "documentation"
                  },
                  "storage_key": "27fde4dc-0854-4325-a1ab-375da95a4a89",
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
                  "content": "Click <b>Open</b> to begin importing the TGA image files to your project.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "A confirmation box appears in the lower right corner of the Unreal Editor.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24450658,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24450658,
                    "file_name": "14-texture-normal-confirmation.png",
                    "file_size": 16585,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T19:37:04.694+00:00",
                    "height": 132,
                    "width": 572,
                    "storage_key": "fc7c553a-0614-4feb-9c68-cdae97f990de",
                    "context": "documentation"
                  },
                  "storage_key": "fc7c553a-0614-4feb-9c68-cdae97f990de",
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
                  "content": "Click <b>OK</b> to accept the <b>T_Rock_04_n.TGA</b> normal map's settings.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "\nClick <b>Save All</b> to save your imported images.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24450671,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24450671,
                    "file_name": "15-save-all-textures.png",
                    "file_size": 196472,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T20:04:43.857+00:00",
                    "height": 514,
                    "width": 1377,
                    "storage_key": "25e5d5bd-863b-4fa9-ab74-6c62583d6361",
                    "context": "documentation"
                  },
                  "storage_key": "25e5d5bd-863b-4fa9-ab74-6c62583d6361",
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
                  "content": "A <b>Save Content</b> dialog box appears.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Click <b>Save Selected</b> to save your imported assets.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "\nNavigate to the <b>QuickStartContent</b> folder, then verify UE5 created the corresponding <b>.uasset files</b>.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24450672,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24450672,
                    "file_name": "QuickStartContentFolder2_Mac.png",
                    "file_size": 63922,
                    "content_type": "image/png",
                    "created_at": "2025-04-03T20:08:07.196+00:00",
                    "height": 259,
                    "width": 668,
                    "storage_key": "9867159d-3820-4315-a4e4-b7661e4ece76",
                    "context": "documentation"
                  },
                  "storage_key": "9867159d-3820-4315-a4e4-b7661e4ece76",
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
            "type": "callout",
            "callout_type": "tip",
            "blocks": [
              {
                "type": "paragraph",
                "content": "\n<a href=\"https://www.fab.com/\">Fab</a><em> (also accessible from the <strong>Epic Launcher</strong>) is a great place to find and share content.</em>\n\n",
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
        "excerpt_hash_id": "V74",
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

## 5. Preparing Meshes for Import

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you have your own meshes to import, this section is for you.",
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

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The UE5 FBX import pipeline uses <strong>FBX 2018</strong>. Using a different version during export may result in incompatibilities.",
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

```json
{
  "type": "switch",
  "switch_type": "3d_art_tool",
  "switchable_blocks": {
    "autodesk_maya": [
      {
        "type": "include",
        "excerpt_id": 111,
        "excerpt_assignment_id": 314,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Select the mesh(es) to be exported in the viewport.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24441960,
                  "caption": "Click image for full size.",
                  "alt_text": "Maya Export",
                  "image": {
                    "id": 24441960,
                    "file_name": "17-maya-export-1.png",
                    "file_size": 89609,
                    "content_type": "image/png",
                    "created_at": "2025-04-02T18:11:06.924+00:00",
                    "height": 549,
                    "width": 946,
                    "storage_key": "687ebb46-af4d-4f3e-b373-0df667b10bbf",
                    "context": "documentation"
                  },
                  "storage_key": "687ebb46-af4d-4f3e-b373-0df667b10bbf",
                  "context": "documentation",
                  "width": 700,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "In the <strong>File</strong> menu, choose <strong>Export Selection</strong> (or <strong>Export All</strong> if you want to export everything in the scene regardless of selection).",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24441961,
                  "caption": "Click image for full size.",
                  "alt_text": "Maya Export",
                  "image": {
                    "id": 24441961,
                    "file_name": "18-maya-export-2.png",
                    "file_size": 117060,
                    "content_type": "image/png",
                    "created_at": "2025-04-02T18:11:07.143+00:00",
                    "height": 502,
                    "width": 204,
                    "storage_key": "d9668f1a-3fee-4ae9-b48f-754b58714282",
                    "context": "documentation"
                  },
                  "storage_key": "d9668f1a-3fee-4ae9-b48f-754b58714282",
                  "context": "documentation",
                  "width": 250,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "In the <strong>Export</strong> dialog box:",
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
                        "content": "Choose the <strong>Content</strong> folder inside your UE5 Project (1)",
                        "settings": {
                          "is_hidden": false
                        }
                      }
                    ],
                    [
                      {
                        "type": "paragraph",
                        "content": "Enter a name for the file and set it to FBX Export (2)",
                        "settings": {
                          "is_hidden": false
                        }
                      }
                    ],
                    [
                      {
                        "type": "paragraph",
                        "content": "Set your Export Options (3)",
                        "settings": {
                          "is_hidden": false
                        }
                      }
                    ],
                    [
                      {
                        "type": "paragraph",
                        "content": "Click <strong>Export All</strong> (4)",
                        "settings": {
                          "is_hidden": false
                        }
                      },
                      {
                        "type": "image",
                        "image_id": 24441962,
                        "caption": "Click image for full size.",
                        "alt_text": "Maya Export",
                        "image": {
                          "id": 24441962,
                          "file_name": "19-maya-export-3.png",
                          "file_size": 231056,
                          "content_type": "image/png",
                          "created_at": "2025-04-02T18:11:07.355+00:00",
                          "height": 566,
                          "width": 860,
                          "storage_key": "db7b6d6e-51a1-4297-8973-05dd824d9591",
                          "context": "documentation"
                        },
                        "storage_key": "db7b6d6e-51a1-4297-8973-05dd824d9591",
                        "context": "documentation",
                        "width": 700,
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
                  "content": "<em>The settings in the Geometry category above are the most basic requirements for exporting <strong>Static Meshes</strong> to Unreal Engine 5.</em>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "<em>You can use the default options for importing. Refer to <a data-document-id=\"3223267\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-import-options-reference-in-unreal-engine\">FBX Import Options Reference</a> for more information on each option.</em>",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Your asset has now been imported and you can drag-and-drop it from the <strong>Content Browser</strong> into your level.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24441963,
                  "caption": "Click image for full size.",
                  "alt_text": "Asset into your Level",
                  "image": {
                    "id": 24441963,
                    "file_name": "20-max-export-7.png",
                    "file_size": 761949,
                    "content_type": "image/png",
                    "created_at": "2025-04-02T18:11:07.698+00:00",
                    "height": 810,
                    "width": 1214,
                    "storage_key": "3d8ab278-b9eb-4e4b-aa02-3921e33b6849",
                    "context": "documentation"
                  },
                  "storage_key": "3d8ab278-b9eb-4e4b-aa02-3921e33b6849",
                  "context": "documentation",
                  "width": 700,
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "<em>In the example above (as part of our Import Options), we imported <strong>Materials</strong> and <strong>Textures</strong>.</em>",
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
        "excerpt_hash_id": "nPg",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "autodesk_3ds_max": [
      {
        "type": "include",
        "excerpt_id": 112,
        "excerpt_assignment_id": 315,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Select the mesh(es) to be exported in the viewport.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24441964,
                  "caption": "Click image for full size.",
                  "alt_text": "Export",
                  "image": {
                    "id": 24441964,
                    "file_name": "max_export_1.png",
                    "file_size": 34133,
                    "content_type": "image/png",
                    "created_at": "2025-04-02T18:11:08.131+00:00",
                    "height": 554,
                    "width": 780,
                    "storage_key": "c43f6025-0f80-4a2b-ae79-cbcb9a1bbe69",
                    "context": "documentation"
                  },
                  "storage_key": "c43f6025-0f80-4a2b-ae79-cbcb9a1bbe69",
                  "context": "documentation",
                  "width": 720,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "In the <strong>File</strong> menu, choose <strong>Export Selected</strong> (or <strong>Export</strong> if you want to export everything in the scene regardless of selection).",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24441965,
                  "caption": "Click image for full size.",
                  "alt_text": "Export Selected",
                  "image": {
                    "id": 24441965,
                    "file_name": "max_export_2.png",
                    "file_size": 39004,
                    "content_type": "image/png",
                    "created_at": "2025-04-02T18:11:08.231+00:00",
                    "height": 576,
                    "width": 425,
                    "storage_key": "6c9accd3-826c-4674-a500-b526d5336e67",
                    "context": "documentation"
                  },
                  "storage_key": "6c9accd3-826c-4674-a500-b526d5336e67",
                  "context": "documentation",
                  "width": 424,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Choose the <strong>Content</strong> folder inside your UE5 Project (1) and a name for the FBX file (2) then click the  button.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24441966,
                  "caption": "Click image for full size.",
                  "alt_text": "Export Selected",
                  "image": {
                    "id": 24441966,
                    "file_name": "20-max-export-3-autodesk.png",
                    "file_size": 137760,
                    "content_type": "image/png",
                    "created_at": "2025-04-02T18:11:08.328+00:00",
                    "height": 456,
                    "width": 573,
                    "storage_key": "93c095f7-872e-4da4-b8fe-62a005153466",
                    "context": "documentation"
                  },
                  "storage_key": "93c095f7-872e-4da4-b8fe-62a005153466",
                  "context": "documentation",
                  "width": 600,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Set your options in the <strong>FBX Export</strong> dialog, then click the  button to create the FBX file containing the mesh(es).",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24441967,
                  "caption": "Click image for full size.",
                  "alt_text": "FBX Export dialog",
                  "image": {
                    "id": 24441967,
                    "file_name": "22-max-export-4-autodesk.png",
                    "file_size": 127680,
                    "content_type": "image/png",
                    "created_at": "2025-04-02T18:11:08.602+00:00",
                    "height": 600,
                    "width": 700,
                    "storage_key": "99c6046f-e665-496c-9f4f-e70566316844",
                    "context": "documentation"
                  },
                  "storage_key": "99c6046f-e665-496c-9f4f-e70566316844",
                  "context": "documentation",
                  "width": 600,
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "<em>The settings in the Geometry category above are the most basic requirements for exporting <strong>Static Meshes</strong> to Unreal Engine 4.</em>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "\n<em>You can leave the default options for importing. Refer to <a data-document-id=\"3223267\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-import-options-reference-in-unreal-engine\">FBX Import Options Reference</a> for more information on each option.</em>\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Your asset has now been imported and you can drag-and-drop it from the <strong>Content Browser</strong> into your level.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24441968,
                  "caption": "Click image for full size.",
                  "alt_text": "Asset into your Level",
                  "image": {
                    "id": 24441968,
                    "file_name": "20-max-export-7.png",
                    "file_size": 761949,
                    "content_type": "image/png",
                    "created_at": "2025-04-02T18:11:08.897+00:00",
                    "height": 810,
                    "width": 1214,
                    "storage_key": "767f23aa-c25d-4554-9ca1-a4d03a0743fd",
                    "context": "documentation"
                  },
                  "storage_key": "767f23aa-c25d-4554-9ca1-a4d03a0743fd",
                  "context": "documentation",
                  "width": 800,
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "<em>In the example above (as part of our Import Options), we imported <strong>Materials</strong> and <strong>Textures</strong>.</em>",
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
        "excerpt_hash_id": "OWj",
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

Well done! You've learned how to prepare meshes for import into UE5.

✓ [Click here if you want to learn more about the FBX content pipeline.](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-content-pipeline).

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<em>Clean modeling improves a game's performance.</em>",
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

## 6. Creating Materials

**Materials** are assets applied to meshes, contributing to a scene's visual aesthetic.
There are a few ways to create and edit materials for your UE5 project; however, we'll focus on using the **Material Editor**.

1. Navigating to your **Content Browser**, click **Add New** and select **Material**. ![New Create Material](https://dev.epicgames.com/community/api/documentation/image/635f6975-697f-468d-bb72-a8b1d8ae189d)
2. Name your material **Rock**. ![Material Naming](https://dev.epicgames.com/community/api/documentation/image/c48d76c6-102a-400b-b220-39223dd8b4d6)
3. Your **Rock Material** is now ready to be used. ![New Rock Material](https://dev.epicgames.com/community/api/documentation/image/6900c1b1-5dd2-4f46-83c5-2ebe589a2f61)
4. Double-clicking the **Rock Material** will open the [Material Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-editor-user-guide). ![Material Editor](https://dev.epicgames.com/community/api/documentation/image/f4d7596e-e48b-4a52-a0ee-1978d0c3d07b) Read our [Material - How-to](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-materials-tutorials) documentation if you want to learn more about working with material nodes.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<em>Size your textures using powers of two.</em>",
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

## 7. Editing Materials

At this point, you should have created a new material and opened the **Material Editor**.

![Material Editor](https://dev.epicgames.com/community/api/documentation/image/e14abe35-e001-4065-a699-ef70a39a11d1)

_Click image for full size._

You can define a material's color, shininess, transparency, and much more in the [Material Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-editor-user-guide). You're now ready to edit the **Rock Material** you created.

1. Select the **Main Material Node** in the center of the **Material Graph**. The **Material Editor** will highlight the node for you when you select it. ![Main Material Node](https://dev.epicgames.com/community/api/documentation/image/03495866-43be-4869-b429-e748263b4931) *It is the only node in the graph (named after your material).*
2. Inside the **Details** panel, change the **Shading Model** from **Default Lit** to **Subsurface**. ![Select Subsurface](https://dev.epicgames.com/community/api/documentation/image/926a3397-e4f0-47ac-989a-67395540aec3)
3. The **Subsurface Shading Model** enables two more pins in the **Main Material Node**: **Opacity** and **Subsurface Color**. ![New More Pins](https://dev.epicgames.com/community/api/documentation/image/5e847a59-8b95-422f-b3c5-d2660f50f871)
4. Get your textures into the Graph. Hold the **T** key and left-click inside the Editor's Graph area. A **Texture Sample Node** should appear inside the graph. ![Texture Sample](https://dev.epicgames.com/community/api/documentation/image/7d17a80e-44de-437d-b89a-a4a5df07125d)
5. You'll want at least 2 textures. Repeat Step 4 until your graph looks like the image below. ![New Texture Sample Nodes](https://dev.epicgames.com/community/api/documentation/image/a8bb136a-0e3e-4131-99ed-c31df0386389)
6. Select one of the **Texture Sample Nodes** and locate the **Details Panel** under the **Material Expression Texture Base** category. ![Material Expression Texture Base](https://dev.epicgames.com/community/api/documentation/image/499e66b7-4d5e-41bf-a90f-b4ec5f4f43e3) Under the texture property, left-click the pull down menu labeled **None** and select the color texture named **T\_Rock\_04\_D**.
7. Repeat Step 6 for the other **Texture Sample Node**, making sure to select the normal map texture named **T\_Rock\_04\_n**. ![New Both Textures Selected](https://dev.epicgames.com/community/api/documentation/image/88eb915c-a750-466b-b08c-7de06d0328d6) *The Material Graph should resemble the image pictured above.*
8. Connect the **T\_Rock\_04\_D** Texture Sample's **Color pin (white)** to the Rock Material's **Base Color pin**. ![New Connect Color Pin](https://dev.epicgames.com/community/api/documentation/image/4416f60b-ccad-404a-a8ee-ea587c0e4c21) *The newly connected **white pin** contains the texture's color channels.*
9. Connect the **T\_Rock\_04\_n** Texture Sample's **Normal pin (white)** to the Rock Material's **Normal pin**. ![New Connect Normal Pin](https://dev.epicgames.com/community/api/documentation/image/5bd3f0bb-77d0-4e4c-9c34-2da051386b5e) *The newly connected **white pin** contains information for the texture's normal map*.
10. The **Preview** should look similar to the image pictured below. ![New Preview DN](https://dev.epicgames.com/community/api/documentation/image/368eaa44-5863-4fe3-8941-0a55eb5bd971)
11. Hold the **1** key and left-click in the **Graph Panel** to create three (**3**) **Constant** nodes. ![Constants](https://dev.epicgames.com/community/api/documentation/image/1e37744a-92fe-4e7c-b272-e67150549521) *The **Constant Node** is a modifiable scalar float variable.*
12. Hold the **3** key and left-click in the Graph Panel to create one (**1**) **Constant3Vector**. ![Constant 3](https://dev.epicgames.com/community/api/documentation/image/5a77b930-72fd-4f1c-a07d-22bc40da76d9) *The **Constant3Vector** node is a modifiable vector corresponding to color without an alpha channel.*
13. Your nodes should be arranged so that connections can be easily made without wires crossing or sliding beneath each other. ![New Mat Constants Added](https://dev.epicgames.com/community/api/documentation/image/88df501c-b06c-413e-9ced-5d71dbc30c93)
14. Connect all of the **Constant** and **Constant3Vector** nodes to corresponding pins in the **Rock Material Main Node**. ![New All Nodes Connected NoVal](https://dev.epicgames.com/community/api/documentation/image/fcab4173-51a2-4189-bfa2-b04cdb13bac3)
15. Change the values of each **Constant** and **Constant3Vector** by updating their **Value** parameter in the **Details** panel. **Specular Value** = 0.0 **Roughness Value** = 0.8 **Opacity Value** = 0.95 **Subsurface Color** = Red(1,0,0) ![New All Connected All Adjusted](https://dev.epicgames.com/community/api/documentation/image/a314aa40-235e-4791-9ae5-773abd2da678)
16. The **Preview** should look similar to the image pictured below. ![New Preview All](https://dev.epicgames.com/community/api/documentation/image/0c79e864-a609-46d6-a7de-3beb84304743)

You're almost done! You've just used the **Material Editor** to edit your **Rock Material**.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<em>A list of all Material Editor Keyboard Shortcuts can be found by going to <strong>Edit Menu &gt; Editor Preferences &gt; Keyboard Shortcuts &gt; \"Material Editor\" and \"Material Editor-Spawn Nodes\"</strong> categories.</em>",
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

## 8. Applying Materials to Static Mesh Actors

You're now ready to bring things together!

The objective of this step is to apply our **Material** to the Static Mesh we imported. Specifically, you'll learn how to:

- [Set an Actor's default Material](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-quick-start-in-unreal-engine)
- [Change Materials used by an Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-quick-start-in-unreal-engine)

### Setting an Actor's Default Material

This section will show you how to set a **Static Mesh Actor's** default material. The default material will be used whenever an **Actor** is placed in the level.

1. Inside the **Content Browser**, double-click the asset you imported earlier in this guide. ![New Browser Conten Asset](https://dev.epicgames.com/community/api/documentation/image/a121fc28-e076-4234-b531-f710c781fccf) The [Static Mesh Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/static-mesh-editor-ui-in-unreal-engine) will load your asset for editing. ![Static Mesh Editor](https://dev.epicgames.com/community/api/documentation/image/f73f7417-786b-41e1-b1d5-e2823eb4f8a3)
2. Inside the **Details** panel under **LOD0**, left-click the material's drop-down menu. ![LOD 0](https://dev.epicgames.com/community/api/documentation/image/59ad046d-d8fe-43f5-8e95-864e5ae461b5)
3. Select the **Rock Material** you created earlier. The material should be available in the selection window. ![Select Rock Material](https://dev.epicgames.com/community/api/documentation/image/d306ef10-2e48-4b8d-bc57-65b0248ab660) Your **Preview Pane** will update to reflect the newly applied material. ![New Default Material](https://dev.epicgames.com/community/api/documentation/image/c06aa877-b853-4af3-b627-5a26d9df7fbf)
4. Clicking the **Save** button first, close the **Material Editor**.
5. Inside the **Content Browser**, drag-and-drop the newly textured **Static Mesh Actor** into your level. ![New Material In Level](https://dev.epicgames.com/community/api/documentation/image/5e1176b9-2090-4a16-a548-0b11b017381a) *The specified **Material** will be used anytime you place this asset in the level.*

### Changing Material Used by an Actor

When we placed a **Static Mesh** object in our level, we created an instance of our object (an [Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/actors-and-geometry-in-unreal-engine)). For every instance of that **Actor**, we're able to specify its **Material**.

Here's how you change a **Static Mesh Actor's** Material.

1. Select your **Static Mesh Actor**. ![New Statis Mesh Selected](https://dev.epicgames.com/community/api/documentation/image/39750ad4-98a2-4e47-915f-6d5bba387c06)
2. Inside the **Details** panel, locate the **Materials** section and click the **Materials** dropdown menu. ![Material DropDown](https://dev.epicgames.com/community/api/documentation/image/52cc5e33-f351-423e-b760-195bdc2c1e6c)
3. Inside the pop-up menu, select a different Material. ![Select Tutorial Asset Material](https://dev.epicgames.com/community/api/documentation/image/ccc54d06-d3d9-45e8-8cb1-d8137c1ee9e0)
4. Alternatively, drag-and-drop a new Material onto the **Static Mesh Actor**. ![New Material Drop](https://dev.epicgames.com/community/api/documentation/image/c399522a-37d1-4b6d-a636-77caaa68d2bf)

You've just applied materials to your Static Mesh Actors by:

- Setting your Actor's Default Material
- Changing Material used by your Actor

We've now reached the end of the Artist Quick Start Guide. By now, you should have the skills needed to:

✓ Set-up a Project
  
✓ Create Materials
  
✓ Edit Materials
  
✓ Apply Materials to a Static Mesh Actor

Are you ready to do some exercises on your own?

## 9. On your own!

Using what you know, create a new **Material** similar to this graph:

![Plastic Material Network](https://dev.epicgames.com/community/api/documentation/image/299118da-c3ac-4719-a3f4-1ae1b11a99ad)

_Click image for full size._

The Main Material node settings simulate a plastic material.

Add **Basic\_Asset1** to the level, apply the Material to it, and update the Material to apply a "Brick" Normal Map Texture.

![Normal Map Added](https://dev.epicgames.com/community/api/documentation/image/595a4282-8538-4dc8-8e01-3267979bef40)

_Click image for full size._

For information on importing different types of content, refer to:

- Information on the FBX pipeline (in general): [FBX Content Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-content-pipeline).
- Information on the FBX Skeletal Mesh pipeline: [FBX Skeletal Mesh Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-skeletal-mesh-pipeline-in-unreal-engine).
- Information on the FBX Animation pipeline: [FBX Animation Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-animation-pipeline-in-unreal-engine).
- Information on the FBX Morph Target pipeline: [FBX Morph Target Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-morph-target-pipeline-in-unreal-engine).
- Information on the FBX Material pipeline: [FBX Material Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-material-pipeline-in-unreal-engine).
- Information on Importing Audio: [Audio Files](https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-audio-files).

For specifics covered in this Quick Start Guide, refer to:

- Information on Supported Image Types: [Texture Import Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/textures-in-unreal-engine).
- Information on Materials: [Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-materials).
- Information on the Content Browser: [Content Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-in-unreal-engine).
- Information on the Static Mesh Editor: [Static Mesh Editor UI](https://dev.epicgames.com/documentation/en-us/unreal-engine/static-mesh-editor-ui-in-unreal-engine).
