# Setting Up Inputs

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-user-inputs-in-unreal-engine

> Application Version: 5.7

In this tutorial, you will create a [Character](https://dev.epicgames.com/documentation/en-us/unreal-engine/characters-in-unreal-engine) and set it up to receive input, then assign the character to a [GameMode](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-mode-and-game-state-in-unreal-engine) so that it is the default pawn during gameplay. After you create your Character, you will define how it reacts to Player Input.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Unreal provides for more complex Input mappings for a variety of project types. Refer to <a data-document-id=\"3229202\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine\">Enhanced Input</a> for additional documentation.",
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

## Project Setup

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1710,
        "excerpt_assignment_id": 1420,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Create a new <strong>Games</strong> &gt; <strong>Blank &gt; Blueprint</strong> project named \"<strong>SettingUpInput</strong>\".",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "From the Editor, navigate to <strong>Edit</strong> &gt; <strong>Project Settings</strong> &gt; <strong>Input &gt; Bindings</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741125,
                  "caption": "",
                  "alt_text": "project-settings",
                  "image": {
                    "id": 25741125,
                    "file_name": "ProjectSettingsBindings.png",
                    "file_size": 53311,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:03.495+00:00",
                    "height": 488,
                    "width": 849,
                    "storage_key": "3cd64c4a-077c-41c9-a071-0dfe5a28a297",
                    "context": "documentation"
                  },
                  "storage_key": "3cd64c4a-077c-41c9-a071-0dfe5a28a297",
                  "context": "documentation",
                  "width": 600,
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
        "excerpt_hash_id": "Z77",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1711,
        "excerpt_assignment_id": 1421,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Create a new <strong>Games</strong> &gt; <strong>Blank &gt; C++ </strong>project named \"<strong>SettingUpInput</strong>\".",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "In the <strong>Editor</strong>, navigate to <strong>Edit</strong> &gt; <strong>Project Settings</strong> &gt; <strong>Input &gt; Bindings</strong>.",
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
            "type": "image",
            "image_id": 25741126,
            "caption": "",
            "alt_text": "project-settings",
            "image": {
              "id": 25741126,
              "file_name": "ProjectSettingsBindings.png",
              "file_size": 53311,
              "content_type": "image/png",
              "created_at": "2025-06-17T19:23:03.769+00:00",
              "height": 488,
              "width": 849,
              "storage_key": "a4a03478-a6b7-4f7e-b021-687fb91586ba",
              "context": "documentation"
            },
            "storage_key": "a4a03478-a6b7-4f7e-b021-687fb91586ba",
            "context": "documentation",
            "width": 600,
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "ny4",
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

### Action and Axis Mapping Setup

Defining Input is done through user-defined **Bindings** of **Action** and **Axis Mappings**. Both mappings provide a mechanism to conveniently map keys and axes to input behaviors by inserting a layer of indirection between the input behavior and the keys that invoke it.

Action Mappings are for key presses and releases, while Axis Mappings allow for inputs that have a continuous range. Once you have defined your Mappings, you can then bind them to behaviors in Blueprints or C++.

1. Click **Add**(**+**) next to **Action Mappings** to create a new Action named **Jump.** ![action-mapping-jump](https://dev.epicgames.com/community/api/documentation/image/d5509b18-bef6-473e-b480-579ee17ae675)
2. From either the drop down arrow(1) or the **Select Key Value** button(2), search for and select the **Space Bar** key value. ![key-map-select](https://dev.epicgames.com/community/api/documentation/image/943c4a2b-8e5a-4804-9c40-a116cebdf587)
3. Navigate to the **Axis mappings** and click **Add**(**+**) to create the following **Axis Mapping** names, **Key** values,and **Scale** values: ![input-settings](https://dev.epicgames.com/community/api/documentation/image/98e132be-61c4-48b3-a77d-3e99cef8be86)

## Creating the Example Character

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1712,
        "excerpt_assignment_id": 1422,
        "blocks": [
          {
            "type": "paragraph",
            "content": "A <a data-document-id=\"3229531\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/characters-in-unreal-engine\">Character</a> is a special type of <strong>Pawn</strong> that has the ability to walk around. Characters extend from the Pawn class, and inherit similar properties such as physical representation of a player or AI entity within the world.",
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
                "content": "Refer to the <a data-document-id=\"3229534\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/pawn-in-unreal-engine\">Pawn</a> and <a data-document-id=\"3229155\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/input-in-unreal-engine\">Input</a> pages for additional documentation.",
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
                  "content": "From the <strong>Content Drawer</strong>, Click <strong>Add</strong>(<strong>+</strong>), then from the <strong>Pick Parent Class</strong> menu choose <strong>Character </strong>as your parent class.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741127,
                  "caption": "",
                  "alt_text": "blueprint-choose-parent-class",
                  "image": {
                    "id": 25741127,
                    "file_name": "ChooseParentClassBP.png",
                    "file_size": 43500,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:03.963+00:00",
                    "height": 458,
                    "width": 626,
                    "storage_key": "d0acfd45-5d3c-4b5b-aa9b-0718303d8daa",
                    "context": "documentation"
                  },
                  "storage_key": "d0acfd45-5d3c-4b5b-aa9b-0718303d8daa",
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
                  "content": "Name your Blueprint <strong>BP_ExampleCharacter</strong>, and double-click it to open its class defaults.",
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
        "excerpt_hash_id": "On8",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1713,
        "excerpt_assignment_id": 1423,
        "blocks": [
          {
            "type": "paragraph",
            "content": "A <a data-document-id=\"3229531\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/characters-in-unreal-engine\">Character</a> is a special type of <strong>Pawn</strong> that has the ability to walk around. Characters extend from the Pawn class, and inherit similar properties such as physical representation of a player or AI entity within the world.",
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
                "content": "Refer to the <a data-document-id=\"3229534\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/pawn-in-unreal-engine\">Pawn</a> and <a data-document-id=\"3229155\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/input-in-unreal-engine\">Input</a> pages for additional documentation.",
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
                  "content": "From the <strong>Content Drawer</strong>, navigate to the <strong>C++ classes</strong> folder, right-click and select <strong>New C++ Class</strong>, then choose <strong>Character</strong> as your parent class.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741128,
                  "caption": "",
                  "alt_text": "choose-parent-class",
                  "image": {
                    "id": 25741128,
                    "file_name": "ChooseParentClass.png",
                    "file_size": 38351,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:04.176+00:00",
                    "height": 580,
                    "width": 946,
                    "storage_key": "4f9c1a27-938e-4fdc-9e06-01a0fca73399",
                    "context": "documentation"
                  },
                  "storage_key": "4f9c1a27-938e-4fdc-9e06-01a0fca73399",
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
                  "content": "Name your character class \"<strong>ExampleCharacter</strong>\", then click <strong>Create Class</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741129,
                  "caption": "",
                  "alt_text": "name-your-new-character",
                  "image": {
                    "id": 25741129,
                    "file_name": "NameYourCharacter.png",
                    "file_size": 35766,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:04.258+00:00",
                    "height": 580,
                    "width": 946,
                    "storage_key": "2e109cdc-017a-4d7c-a1d3-2bc4e1c17d45",
                    "context": "documentation"
                  },
                  "storage_key": "2e109cdc-017a-4d7c-a1d3-2bc4e1c17d45",
                  "context": "documentation",
                  "width": 600,
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
        "excerpt_hash_id": "Y87",
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

### Creating the SpringArm and Camera Components

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1714,
        "excerpt_assignment_id": 1424,
        "blocks": [
          {
            "type": "header",
            "content": "Creating the SpringArm and Camera Components",
            "level": 4,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "When the <strong>Camera</strong> and <strong>SpringArm Components </strong>are used together, they provide functionality for a third-person perspective that can dynamically adjust to your game world. The camera component contains a camera that represents the player's point of view or how the player sees the world. The SpringArm component is used as a \"camera boom\" to keep the camera for a player from colliding into the world.",
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
                  "content": "In the <strong>Components</strong> tab, click <strong>Add(+)</strong>, then from the drop down search for and select <strong>Spring Arm</strong>. Rename your Spring Arm component <strong>CameraBoom</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741130,
                  "caption": "",
                  "alt_text": "add-spring-arm-component",
                  "image": {
                    "id": 25741130,
                    "file_name": "AddSpringArmComp.png",
                    "file_size": 18015,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:04.600+00:00",
                    "height": 289,
                    "width": 390,
                    "storage_key": "76c51955-ffdd-4bf9-a5f2-42f30576c72f",
                    "context": "documentation"
                  },
                  "storage_key": "76c51955-ffdd-4bf9-a5f2-42f30576c72f",
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
                  "content": "Repeat step 1, but search for and select the <strong>Camera</strong>. Rename your Camera component <strong>FollowCamera</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741131,
                  "caption": "",
                  "alt_text": "add-follow-camera",
                  "image": {
                    "id": 25741131,
                    "file_name": "AddFollowCamera.png",
                    "file_size": 19186,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:04.824+00:00",
                    "height": 285,
                    "width": 398,
                    "storage_key": "6202ca5d-6140-4d6f-9bb2-fe152a805153",
                    "context": "documentation"
                  },
                  "storage_key": "6202ca5d-6140-4d6f-9bb2-fe152a805153",
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
                  "content": "From the <strong>Components</strong> tab, drag your <strong>FollowCamera</strong> onto the <strong>CameraBoom</strong> to attach it.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741132,
                  "caption": "",
                  "alt_text": "attaching-the-follow-camera",
                  "image": {
                    "id": 25741132,
                    "file_name": "AttachFollowCamera.png",
                    "file_size": 22157,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:04.901+00:00",
                    "height": 283,
                    "width": 392,
                    "storage_key": "3038ad50-283a-4509-90b8-eab83be0ba60",
                    "context": "documentation"
                  },
                  "storage_key": "3038ad50-283a-4509-90b8-eab83be0ba60",
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
                  "content": "Select the CameraBoom in the Components tab, then navigate to the <strong>Details</strong> &gt;  <strong>Camera Settings</strong> and click the checkbox to enable the <strong>Use Pawn Control Rotation</strong> variable. When enabled, the Camera parent uses the view / control rotation of the pawn (<strong>ExampleCharacter</strong>).",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741133,
                  "caption": "",
                  "alt_text": "using-pawn-control-rotation",
                  "image": {
                    "id": 25741133,
                    "file_name": "UsePawnControlRotation.png",
                    "file_size": 15569,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:04.971+00:00",
                    "height": 336,
                    "width": 451,
                    "storage_key": "87aa7f66-0b20-4b2b-91fb-72032abaf95c",
                    "context": "documentation"
                  },
                  "storage_key": "87aa7f66-0b20-4b2b-91fb-72032abaf95c",
                  "context": "documentation",
                  "width": null,
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
                      "content": "For additional Spring arm and Camera settings that you could use for your Character's perspective. Refer to the <a data-document-id=\"3229391\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/using-cameras-in-unreal-engine\">Using Cameras</a> documentation",
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
                  "content": "<strong>Compile</strong> and <strong>Save</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741134,
                  "caption": "",
                  "alt_text": "compile-and-save",
                  "image": {
                    "id": 25741134,
                    "file_name": "CompileSave.png",
                    "file_size": 2818,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:05.076+00:00",
                    "height": 41,
                    "width": 196,
                    "storage_key": "1b1e34d0-2094-41cb-a8d5-d1c1aa3eccf8",
                    "context": "documentation"
                  },
                  "storage_key": "1b1e34d0-2094-41cb-a8d5-d1c1aa3eccf8",
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
        "excerpt_hash_id": "V2J",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1715,
        "excerpt_assignment_id": 1425,
        "blocks": [
          {
            "type": "paragraph",
            "content": "When the <strong>Camera</strong> and <strong>SpringArm Components</strong> are used together, they provide functionality for a third-person perspective that can dynamically adjust to your game world. The camera component contains a camera that represents the player's point of view or how the player sees the world. The SpringArm component is used as a \"camera boom\" to keep the camera for a player from colliding into the world.",
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
                  "content": "In your code editor, navigate to ExampleCharacter.h<strong>. </strong>In the <strong>Class defaults,</strong> declare the following classes.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "protected:\n         UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = &quot;Components&quot;)\n         class USpringArmComponent* CameraBoom;\n\t\t\n         UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = &quot;Components&quot;)\n         class UCameraComponent* FollowCamera; |",
                  "lines_of_code": 6,
                  "id": 60603,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYwMywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ0KzAwOjAwIn0=--6c62a2f9046440d7aebd493dd6cf911c94e0d77aee6690775c42a5dc37e83371",
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
                      "content": "<a data-document-id=\"3227224\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-uproperties\">UProperty Specifiers</a> are used to provide visibility of the component in the Blueprint Editor.",
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
                  "content": "Navigate to your <code>ExampleCharacter.cpp</code> file.  Add the following libraries to the include line.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "#include &quot;GameFramework/SpringArmComponent.h&quot;\n         #include &quot;Camera/CameraComponent.h&quot;",
                  "lines_of_code": 2,
                  "id": 60604,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYwNCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ0KzAwOjAwIn0=--b7f20b3435cdd45e9a3aa297fef9c2020aaba508a3ccc4c40735baf3490c5925",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Next, implement the following in the  <code>AExampleCharacter</code> constructor.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "AExampleCharacter::AExampleCharacter()\n        {\n        //Initialize the Camera Boom\n        CameraBoom = CreateDefaultSubobject&lt;USpringArmComponent&gt;(TEXT(&quot;CameraBoom&quot;));\n\t\t\n        //Setup Camera Boom attachment to the Root component of the class\n        CameraBoom-&gt;SetupAttachment(RootComponent);\n\t\t\n        //Set the boolean to use the PawnControlRotation to true.\n        CameraBoom-&gt;bUsePawnControlRotation = true;\n",
                  "lines_of_code": 17,
                  "id": 60605,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYwNSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ0KzAwOjAwIn0=--f0507a5782e2ad2a36de45d55426fa0fa1ce5bfbfdb0b3c075cdafce3e9a93a3",
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
                      "content": "The component calls the <a data-document-id=\"3562911\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject/FObjectInitializer/CreateDefaultSubobject?application_version=5.5\">FObjectInitializer::CreateDefaultSubobject</a>template, then uses the <a data-document-id=\"3580590\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/Components/USceneComponent/SetupAttachment?application_version=5.5\">SetupAttachment</a> method to attach to a parent Scene Component. When setting the Camera Boom to use the Pawn's <a data-document-id=\"3938471\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/USpringArmComponent/bUsePawnControlRotation?application_version=5.5\">control rotation</a>, it uses its parent pawn's rotation instead of its own.",
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
                  "content": "Compile your code.",
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
        "excerpt_hash_id": "38A",
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

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1716,
        "excerpt_assignment_id": 1426,
        "blocks": [
          {
            "type": "header",
            "content": "Setting the Character Mesh",
            "level": 4,
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
                  "content": "In the <strong>Components</strong> panel, select the <strong>Mesh</strong> Skeletal Mesh Component.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741135,
                  "caption": "",
                  "alt_text": "components-mesh-select",
                  "image": {
                    "id": 25741135,
                    "file_name": "CharacterMeshSelect.png",
                    "file_size": 21804,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:05.495+00:00",
                    "height": 287,
                    "width": 382,
                    "storage_key": "c6be6aa6-a35b-4628-8648-e9bc6bd20cf0",
                    "context": "documentation"
                  },
                  "storage_key": "c6be6aa6-a35b-4628-8648-e9bc6bd20cf0",
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
                  "content": "Navigate to<strong> Details</strong> &gt; <strong>Mesh</strong> &gt; <strong>Skeletal Mesh</strong> and expand the drop-down menu. Select  <strong>Browse Asset Options</strong> &gt; <strong>Content</strong> &gt; <strong>Show Engine Content</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741136,
                  "caption": "",
                  "alt_text": "show-engine-content",
                  "image": {
                    "id": 25741136,
                    "file_name": "DetailsOptionsPanel.png",
                    "file_size": 38704,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:05.577+00:00",
                    "height": 629,
                    "width": 479,
                    "storage_key": "87807a22-0f98-4472-91d3-3a200b71d014",
                    "context": "documentation"
                  },
                  "storage_key": "87807a22-0f98-4472-91d3-3a200b71d014",
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
                  "content": "Search for and select the <strong>TutorialTPP </strong>Skeletal Mesh.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741137,
                  "caption": "",
                  "alt_text": "details-skeletalmesh-select",
                  "image": {
                    "id": 25741137,
                    "file_name": "DetailsPanel.png",
                    "file_size": 47791,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:05.705+00:00",
                    "height": 653,
                    "width": 651,
                    "storage_key": "fd9c0bc2-74a5-49ac-96f9-b73149fe335f",
                    "context": "documentation"
                  },
                  "storage_key": "fd9c0bc2-74a5-49ac-96f9-b73149fe335f",
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
                  "content": "Navigate to the <strong>Transform</strong> category, then set the <strong>Location</strong> and <strong>Rotation</strong> vector values to  (<strong>0.0, 0.0, -90</strong>)",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741138,
                  "caption": "",
                  "alt_text": "transform-details",
                  "image": {
                    "id": 25741138,
                    "file_name": "DetailsTransform.png",
                    "file_size": 11576,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:05.868+00:00",
                    "height": 203,
                    "width": 355,
                    "storage_key": "6331d8e0-3f27-4120-9e90-45709e9dad91",
                    "context": "documentation"
                  },
                  "storage_key": "6331d8e0-3f27-4120-9e90-45709e9dad91",
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
                  "content": "<strong>Compile</strong> and <strong>Save</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741139,
                  "caption": "",
                  "alt_text": "compile-and-save",
                  "image": {
                    "id": 25741139,
                    "file_name": "CompileSave.png",
                    "file_size": 2818,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:05.945+00:00",
                    "height": 41,
                    "width": 196,
                    "storage_key": "862de5f4-155a-4ee9-a3f4-0cc9c5e3357e",
                    "context": "documentation"
                  },
                  "storage_key": "862de5f4-155a-4ee9-a3f4-0cc9c5e3357e",
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
        "excerpt_hash_id": "ARL",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1717,
        "excerpt_assignment_id": 1427,
        "blocks": [
          {
            "type": "header",
            "content": "Creating the Action/Axis Functions to your Input Component",
            "level": 4,
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
                  "content": "In your <code>ExampleCharacter.h</code> class defaults, declare the following Input functions.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "protected:\n\t\t\n         void MoveForward(float AxisValue);\n\t\t\n         void MoveRight(float AxisValue);",
                  "lines_of_code": 5,
                  "id": 60606,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYwNiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ0KzAwOjAwIn0=--fa25ca7b8d64fbcb3d16f30627b445f57a770018b857197417515d15d5e1c03d",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to your <code>ExampleCharacter.cpp</code> and implement your <code>MoveForward</code> and <code>MoveRight</code> methods.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void AExampleCharacter::MoveForward(float AxisValue)\n         {\n             if ((Controller != NULL) &amp;&amp; (AxisValue != 0.0f))\n             {\n                 // find out which direction is forward\n                 const FRotator Rotation = Controller-&gt;GetControlRotation();\n                 const FRotator YawRotation(0, Rotation.Yaw, 0);\n\t\t\n                 // get forward vector\n                 const FVector Direction = FRotationMatrix(YawRotation).GetUnitAxis(EAxis::X);\n",
                  "lines_of_code": 30,
                  "id": 60607,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYwNywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ0KzAwOjAwIn0=--6a98b28d016efb222216f74003332180c6d46a565bd32a854452bd275a1d1cbe",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to the SetupPlayerInputComponent(UInputComponent* PlayerInputComponent) method, then implement the following code.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void AExampleCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)\n         {\n             Super::SetupPlayerInputComponent(PlayerInputComponent);\n\t\t\n             PlayerInputComponent-&gt;BindAction(&quot;Jump&quot;, IE_Pressed, this, &amp;ACharacter::Jump);\n             PlayerInputComponent-&gt;BindAction(&quot;Jump&quot;, IE_Released, this, &amp;ACharacter::StopJumping);\n\t\t\n             PlayerInputComponent-&gt;BindAxis(&quot;MoveForward&quot;, this, &amp;AExampleCharacter::MoveForward);\n             PlayerInputComponent-&gt;BindAxis(&quot;MoveRight&quot;, this, &amp;AExampleCharacter::MoveRight);\n             PlayerInputComponent-&gt;BindAxis(&quot;Turn&quot;, this, &amp;APawn::AddControllerYawInput);\n",
                  "lines_of_code": 12,
                  "id": 60608,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYwOCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ0KzAwOjAwIn0=--65d8de75619cebb1ab8f07fab9a1f1e53d37ae8a6b831552d4790d0da3c509c4",
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
                      "content": "The <a data-document-id=\"3229203\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/input-overview-in-unreal-engine\">Player Input Component</a> links the AxisMappings and ActionMappings in your project to game actions. Both the Pawn and Character class contain methods that are inherited and can be used or extended for your custom characters.\n     In our example, we've used the Pawn's AddControllerYawInput and AddControllerPitchInput functions, and the Character's Jump and StopJumping functions.",
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
                  "content": "Compile your code.",
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
        "excerpt_hash_id": "WEY",
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

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1718,
        "excerpt_assignment_id": 1428,
        "blocks": [
          {
            "type": "header",
            "content": "Creating the Action/Axis Functions to your Input Events",
            "level": 4,
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
                  "content": "Navigate to<strong> My Blueprint</strong> &gt; <strong>Functions</strong>, click <strong>Add</strong>(<strong>+</strong>) to add two new functions. <strong>MoveForward</strong> and <strong>MoveRight</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741140,
                  "caption": "",
                  "alt_text": "move-function",
                  "image": {
                    "id": 25741140,
                    "file_name": "MoveFunctions.png",
                    "file_size": 13526,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:06.272+00:00",
                    "height": 207,
                    "width": 376,
                    "storage_key": "b867f122-24b3-4076-8aab-0aa5cf40bc7e",
                    "context": "documentation"
                  },
                  "storage_key": "b867f122-24b3-4076-8aab-0aa5cf40bc7e",
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
                  "content": "Select the <strong>MoveForward</strong> function, navigate to the <strong>Details</strong> &gt;<strong> Inputs</strong>, then click <strong>Add</strong>(<strong>+</strong>) to add a new <strong>float</strong> value input named<strong> AxisValue</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741141,
                  "caption": "",
                  "alt_text": "image alt text",
                  "image": {
                    "id": 25741141,
                    "file_name": "MoveFunctions_2.png",
                    "file_size": 10152,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:06.371+00:00",
                    "height": 174,
                    "width": 465,
                    "storage_key": "f9bb2ea2-5c27-4964-aa25-1ed23caba86a",
                    "context": "documentation"
                  },
                  "storage_key": "f9bb2ea2-5c27-4964-aa25-1ed23caba86a",
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
                  "content": "Copy or Implement the logic below for the <strong>MoveForward</strong> function.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_FunctionEntry Name=&quot;K2Node_FunctionEntry_0&quot;\n     ExtraFlags=201457664\n     FunctionReference=(MemberName=&quot;MoveForward&quot;)\n     bIsEditable=True\n     NodePosX=-32\n     NodePosY=16\n     NodeGuid=A0FF87524A53EDAA6CBEC48FEE0D9464\n     CustomProperties Pin (PinId=B427E05D444F66A59DA68E9A5D09AB7B,PinName=&quot;then&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_7346 B27FCDDF43B9261BD870CE965B82DF38,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=F01767A145595ED17A3E438A7F7BEFA2,PinName=&quot;AxisValue&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;real&quot;,PinType.PinSubCategory=&quot;double&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_7346 D95413A34BE985375A5C2F905CD8109F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties UserDefinedPin (PinName=&quot;AxisValue&quot;,PinType=(PinCategory=&quot;real&quot;,PinSubCategory=&quot;double&quot;),DesiredPinDirection=EGPD_Output)\n",
                  "lines_of_code": 17,
                  "id": 60609,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYwOSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ0KzAwOjAwIn0=--9305b158fa33f165b233fe9ab1375ff53c1978b71b41c85f9a93d5643ee56ab4",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Select the <strong>MoveRight</strong> function, and add a new <strong>float </strong>value as instructed in step 2.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741142,
                  "caption": "",
                  "alt_text": "image alt text",
                  "image": {
                    "id": 25741142,
                    "file_name": "MoveFunctions_2.png",
                    "file_size": 10152,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:06.448+00:00",
                    "height": 174,
                    "width": 465,
                    "storage_key": "264c95b2-dfa3-48b5-a00a-3ec2aa822236",
                    "context": "documentation"
                  },
                  "storage_key": "264c95b2-dfa3-48b5-a00a-3ec2aa822236",
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
                  "content": "Copy or Implement the logic below for the <strong>MoveRight</strong> function.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_FunctionEntry Name=&quot;K2Node_FunctionEntry_0&quot;\n     ExtraFlags=201457664\n     FunctionReference=(MemberName=&quot;MoveRight&quot;)\n     bIsEditable=True\n     NodePosX=64\n     NodePosY=-48\n     NodeGuid=5846746C4FEEF77A895638939B0C845C\n     CustomProperties Pin (PinId=09949021438E59AA6E23A8B112C93B0D,PinName=&quot;then&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_7346 B27FCDDF43B9261BD870CE965B82DF38,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=0FE0FC0344DE295574151E8BA52B9628,PinName=&quot;AxisValue&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;real&quot;,PinType.PinSubCategory=&quot;double&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_7346 D95413A34BE985375A5C2F905CD8109F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties UserDefinedPin (PinName=&quot;AxisValue&quot;,PinType=(PinCategory=&quot;real&quot;,PinSubCategory=&quot;double&quot;),DesiredPinDirection=EGPD_Output)\n",
                  "lines_of_code": 18,
                  "id": 60610,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYxMCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ0KzAwOjAwIn0=--ccf049fc4adf16dd28cc7b4c0251097aa1fea6a25f7830db1be259efe3a0d870",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to the <strong>Event Graph</strong>. You need to set up your Axis and Action input events to call their respective functions. Copy or implement the logic below.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name=&quot;K2Node_CallFunction_0&quot;\n     FunctionReference=(MemberName=&quot;MoveForward&quot;,MemberGuid=C0341673464A891BBAB256A597CC129B,bSelfContext=True)\n     NodePosX=752\n     NodePosY=96\n     NodeGuid=F58C25A840CC8F0AFBDAF29C9156738F\n     CustomProperties Pin (PinId=0AB1925F4322FE3D3E6EB4A491889FC9,PinName=&quot;execute&quot;,PinToolTip=&quot;\\nExec&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_InputAxisEvent_0 C6162D6E4C41B2636D72DB955E9701A2,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=75B681B34A8D4B3145A6B88572E666E2,PinName=&quot;then&quot;,PinToolTip=&quot;\\nExec&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=A75F913B4741D285583415B3E8CFF56F,PinName=&quot;self&quot;,PinFriendlyName=NSLOCTEXT(&quot;K2Node&quot;, &quot;Target&quot;, &quot;Target&quot;),PinToolTip=&quot;Target\\nSelf Object Reference&quot;,PinType.PinCategory=&quot;object&quot;,PinType.PinSubCategory=&quot;self&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUOb",
                  "lines_of_code": 8,
                  "id": 60611,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYxMSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ0KzAwOjAwIn0=--71ac99bcd4ec852cfa855935d6cf62bfe711d91e58d38300cbfd1121d8035add",
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
        "excerpt_hash_id": "2oN",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1719,
        "excerpt_assignment_id": 1429,
        "blocks": [
          {
            "type": "header",
            "content": "Finished Code",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "ExampleCharacter.h",
            "level": 4,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "#pragma once\n\n\t\t#include &quot;CoreMinimal.h&quot;\n\t\t#include &quot;GameFramework/Character.h&quot;\n\t\t#include &quot;ExampleCharacter.generated.h&quot;\n\n\t\tUCLASS()\n\t\tclass SETTINGUPINPUT_API AExampleCharacter : public ACharacter\n\t\t{\n\t\t\tGENERATED_BODY()\n",
            "lines_of_code": 37,
            "id": 60612,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYxMiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ0KzAwOjAwIn0=--d143103ccaaf0ede1fe4ca515fc0a469ed6431f9cb83015a43b7e5b8e29eff3d",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "ExampleCharacter.cpp",
            "level": 4,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "// Sets default values\n\t\tAExampleCharacter::AExampleCharacter()\n\t\t{\n\t\t\t//Initialize the Camera Boom\n\t\t\tCameraBoom = CreateDefaultSubobject&lt;USpringArmComponent&gt;(TEXT(&quot;CameraBoom&quot;));\n\n\t\t\t//Setup its attachment to the Root component of the class\n\t\t\tCameraBoom-&gt;SetupAttachment(RootComponent);\n\n\t\t\t//Set the boolean to use the PawnControlRotation to true.\n",
            "lines_of_code": 76,
            "id": 60613,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYxMywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ0KzAwOjAwIn0=--ec4e397357b40b7d9508f1682642ebdeb893248fc5b5310d419e855fd4fe7144",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Creating the Character Blueprint",
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
                  "content": "Navigate to your <strong>C++ Classes Folder</strong> and right click your <strong>ExampleCharacter</strong>, from the drop down menu select <strong>Create Blueprint class based on ExampleCharacter</strong>. Name your Blueprint <strong>BP_ExampleCharacter</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741143,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741143,
                    "file_name": "CreateBPCharacter.png",
                    "file_size": 38736,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:06.643+00:00",
                    "height": 459,
                    "width": 568,
                    "storage_key": "680f2cea-e066-4e17-ae6e-9458ce19802b",
                    "context": "documentation"
                  },
                  "storage_key": "680f2cea-e066-4e17-ae6e-9458ce19802b",
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
                  "content": "In the <strong>Components</strong> panel, select the <strong>Mesh</strong> Skeletal Mesh Component.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741144,
                  "caption": "",
                  "alt_text": "components-mesh-select",
                  "image": {
                    "id": 25741144,
                    "file_name": "CharacterMeshSelect.png",
                    "file_size": 21804,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:06.740+00:00",
                    "height": 287,
                    "width": 382,
                    "storage_key": "d037f9e0-e8b8-4ebb-b8bd-584d54ebec8a",
                    "context": "documentation"
                  },
                  "storage_key": "d037f9e0-e8b8-4ebb-b8bd-584d54ebec8a",
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
                  "content": "Navigate to<strong> Details</strong> &gt; <strong>Mesh</strong> &gt; <strong>Skeletal Mesh</strong> and expand the drop-down menu.  In the Browser section, click the <strong>Settings</strong> Icon. Then from the context menu, select <strong>Content</strong> &gt; <strong>Show Engine Content</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741145,
                  "caption": "",
                  "alt_text": "show-engine-content",
                  "image": {
                    "id": 25741145,
                    "file_name": "DetailsOptionsPanel.png",
                    "file_size": 38704,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:06.839+00:00",
                    "height": 629,
                    "width": 479,
                    "storage_key": "ddbb30c9-a1dd-4366-84ac-0dc4ca0adcb8",
                    "context": "documentation"
                  },
                  "storage_key": "ddbb30c9-a1dd-4366-84ac-0dc4ca0adcb8",
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
                  "content": "Search for and select the <strong>TutorialTPP </strong>Skeletal Mesh.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741146,
                  "caption": "",
                  "alt_text": "details-skeletalmesh-select",
                  "image": {
                    "id": 25741146,
                    "file_name": "DetailsPanel.png",
                    "file_size": 47791,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:06.933+00:00",
                    "height": 653,
                    "width": 651,
                    "storage_key": "982297b0-962d-43f4-9f38-2f548184e2e2",
                    "context": "documentation"
                  },
                  "storage_key": "982297b0-962d-43f4-9f38-2f548184e2e2",
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
                  "content": "Navigate to the <strong>Transform</strong> category, then set the <strong>Location</strong> and <strong>Rotation</strong> vector values to  (<strong>0.0, 0.0, -90</strong>)",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741147,
                  "caption": "",
                  "alt_text": "transform-details",
                  "image": {
                    "id": 25741147,
                    "file_name": "DetailsTransform.png",
                    "file_size": 11576,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:07.041+00:00",
                    "height": 203,
                    "width": 355,
                    "storage_key": "9b3fbeb7-279c-44bb-968b-6bbadfccf061",
                    "context": "documentation"
                  },
                  "storage_key": "9b3fbeb7-279c-44bb-968b-6bbadfccf061",
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
        "excerpt_hash_id": "l4X",
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

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1720,
        "excerpt_assignment_id": 1430,
        "blocks": [
          {
            "type": "header",
            "content": "Finished Blueprint",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "MoveForward",
            "level": 4,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25741148,
            "caption": "",
            "alt_text": "move-function",
            "image": {
              "id": 25741148,
              "file_name": "MoveForward.png",
              "file_size": 91990,
              "content_type": "image/png",
              "created_at": "2025-06-17T19:23:07.221+00:00",
              "height": 716,
              "width": 1084,
              "storage_key": "0c0bb9ea-cfe1-4b46-98db-bdc4822bfa47",
              "context": "documentation"
            },
            "storage_key": "0c0bb9ea-cfe1-4b46-98db-bdc4822bfa47",
            "context": "documentation",
            "width": 600,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "MoveRight",
            "level": 4,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25741149,
            "caption": "",
            "alt_text": "move-right",
            "image": {
              "id": 25741149,
              "file_name": "MoveRight.png",
              "file_size": 84770,
              "content_type": "image/png",
              "created_at": "2025-06-17T19:23:07.449+00:00",
              "height": 532,
              "width": 961,
              "storage_key": "85d9f0bc-ba65-4118-b73f-2d90e37a41f3",
              "context": "documentation"
            },
            "storage_key": "85d9f0bc-ba65-4118-b73f-2d90e37a41f3",
            "context": "documentation",
            "width": 600,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Event Graph",
            "level": 4,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25741150,
            "caption": "",
            "alt_text": "event-graph",
            "image": {
              "id": 25741150,
              "file_name": "EventGraph.png",
              "file_size": 69082,
              "content_type": "image/png",
              "created_at": "2025-06-17T19:23:07.645+00:00",
              "height": 467,
              "width": 587,
              "storage_key": "f11ee407-dffe-46d7-9194-6964e909c500",
              "context": "documentation"
            },
            "storage_key": "f11ee407-dffe-46d7-9194-6964e909c500",
            "context": "documentation",
            "width": 600,
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "9J6",
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

## Creating the GameMode Blueprint

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1721,
        "excerpt_assignment_id": 1431,
        "blocks": [
          {
            "type": "paragraph",
            "content": "The <a data-document-id=\"3229533\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/game-mode-and-game-state-in-unreal-engine\">GameMode</a> defines the game's set of rules. These rules include what default pawn the player will spawn as when the game is launched. You need to set up these rules to spawn the Player Character you created.",
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
                  "content": "In the <strong>Content Drawer</strong>, click <strong>Add(+)</strong> to create a new <strong>Blueprint Class</strong>, then from the drop down menu choose <strong>Game Mode Base </strong>as your <strong>Parent Class</strong>. Name your game mode \"<strong>BP_InputGameMode</strong>\".",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741151,
                  "caption": "",
                  "alt_text": "image alt text",
                  "image": {
                    "id": 25741151,
                    "file_name": "ChooseParentClassBP.png",
                    "file_size": 43500,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:07.831+00:00",
                    "height": 458,
                    "width": 626,
                    "storage_key": "ceafe88b-a9dc-4077-bcbb-afb7daae5205",
                    "context": "documentation"
                  },
                  "storage_key": "ceafe88b-a9dc-4077-bcbb-afb7daae5205",
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
                  "content": "In the <strong>Class</strong> defaults, navigate to <strong>Classes</strong> &gt; <strong>Default Pawn Class</strong>, and select <strong>BP_ExampleCharacter</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741152,
                  "caption": "",
                  "alt_text": "image alt text",
                  "image": {
                    "id": 25741152,
                    "file_name": "DefaultPawnClass.png",
                    "file_size": 59860,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:07.900+00:00",
                    "height": 483,
                    "width": 829,
                    "storage_key": "331a6c43-bab7-4d91-a9e2-3557790a1192",
                    "context": "documentation"
                  },
                  "storage_key": "331a6c43-bab7-4d91-a9e2-3557790a1192",
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
                  "content": "<strong>Compile</strong> and <strong>Save</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741153,
                  "caption": "",
                  "alt_text": "compile-and-save",
                  "image": {
                    "id": 25741153,
                    "file_name": "CompileSave.png",
                    "file_size": 2818,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:08.038+00:00",
                    "height": 41,
                    "width": 196,
                    "storage_key": "19b0c468-a08a-4e8d-8980-7d71101af48c",
                    "context": "documentation"
                  },
                  "storage_key": "19b0c468-a08a-4e8d-8980-7d71101af48c",
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
                  "content": "Navigate to <strong>Edit</strong> &gt; <strong>Project Settings</strong> &gt; <strong>Maps and Modes</strong>. Set the <strong>Default GameMode</strong> to <strong>BP_InputGameMode</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741154,
                  "caption": "",
                  "alt_text": "image alt text",
                  "image": {
                    "id": 25741154,
                    "file_name": "ProjectSettings.png",
                    "file_size": 59114,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:08.126+00:00",
                    "height": 490,
                    "width": 842,
                    "storage_key": "bc924800-0696-4a4c-b231-db2c76b9712f",
                    "context": "documentation"
                  },
                  "storage_key": "bc924800-0696-4a4c-b231-db2c76b9712f",
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
                  "content": "Navigate to the <strong>Editor</strong> and select <strong>Play</strong> (<strong>Play in Editor</strong>)",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741155,
                  "caption": "",
                  "alt_text": "play-in-editor",
                  "image": {
                    "id": 25741155,
                    "file_name": "Play.png",
                    "file_size": 11255,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:08.293+00:00",
                    "height": 103,
                    "width": 565,
                    "storage_key": "d9eb6ec6-9ce1-440b-b7af-d71eddde00ed",
                    "context": "documentation"
                  },
                  "storage_key": "d9eb6ec6-9ce1-440b-b7af-d71eddde00ed",
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
            "content": "You can now control your character's movement using the W, A, S, D keys. Moving the mouse moves the camera, and pressing the spacebar causes the character to jump.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "8ar",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1722,
        "excerpt_assignment_id": 1432,
        "blocks": [
          {
            "type": "paragraph",
            "content": "The <a data-document-id=\"3229533\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/game-mode-and-game-state-in-unreal-engine\">GameMode</a> defines the game's set of rules. These rules include what default pawn the player will spawn when the game is launched. You need to set up these rules to spawn the Player Character you created.",
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
                  "content": "In the <strong>Content Drawer</strong>, navigate to your <strong>C++ Classes</strong> folder, right-click the <strong>SettingUpInputGameModeBase</strong>, then in the drop-down menu select <strong>Create Blueprint Based on SettingUpInputGameModeBase</strong>. Name your game mode Blueprint \"<strong>BP_InputGameMode</strong>\".",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741156,
                  "caption": "",
                  "alt_text": "image alt text",
                  "image": {
                    "id": 25741156,
                    "file_name": "SettingUpInputGameModeBase.png",
                    "file_size": 46823,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:08.588+00:00",
                    "height": 506,
                    "width": 654,
                    "storage_key": "f0aafd85-1990-43f1-8fec-4f8c8d79620d",
                    "context": "documentation"
                  },
                  "storage_key": "f0aafd85-1990-43f1-8fec-4f8c8d79620d",
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
                  "content": "In the <strong>Class</strong> defaults, navigate to <strong>Classes</strong> &gt; <strong>Default Pawn Class</strong>, and select the <strong>BP_ExampleCharacter</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741157,
                  "caption": "",
                  "alt_text": "image alt text",
                  "image": {
                    "id": 25741157,
                    "file_name": "DefaultPawnClass.png",
                    "file_size": 59860,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:08.663+00:00",
                    "height": 483,
                    "width": 829,
                    "storage_key": "bde9f279-d26f-4867-ae4b-2e10463f0a67",
                    "context": "documentation"
                  },
                  "storage_key": "bde9f279-d26f-4867-ae4b-2e10463f0a67",
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
                  "content": "<strong>Compile</strong> and <strong>Save</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741158,
                  "caption": "",
                  "alt_text": "compile-and-save",
                  "image": {
                    "id": 25741158,
                    "file_name": "CompileSave.png",
                    "file_size": 2818,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:08.799+00:00",
                    "height": 41,
                    "width": 196,
                    "storage_key": "aca49ed0-1e48-4ff4-b6dc-b2f599adaa23",
                    "context": "documentation"
                  },
                  "storage_key": "aca49ed0-1e48-4ff4-b6dc-b2f599adaa23",
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
                  "content": "Navigate to <strong>Edit</strong> &gt; <strong>Project Settings</strong> &gt; <strong>Maps and Modes</strong>. Set the <strong>Default GameMode</strong> to <strong>BP_InputGameMode.</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741159,
                  "caption": "",
                  "alt_text": "project-settings",
                  "image": {
                    "id": 25741159,
                    "file_name": "ProjectSettings.png",
                    "file_size": 59114,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:08.861+00:00",
                    "height": 490,
                    "width": 842,
                    "storage_key": "e82a3220-df1b-458f-b47e-cc6560d0c34e",
                    "context": "documentation"
                  },
                  "storage_key": "e82a3220-df1b-458f-b47e-cc6560d0c34e",
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
                  "content": "Navigate to the <strong>Editor</strong> and select <strong>Play</strong> (<strong>Play in Editor</strong>)",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741160,
                  "caption": "",
                  "alt_text": "play-in-editor",
                  "image": {
                    "id": 25741160,
                    "file_name": "Play.png",
                    "file_size": 11255,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:23:08.975+00:00",
                    "height": 103,
                    "width": 565,
                    "storage_key": "03403fa6-4cae-4883-b161-8a90ac3b5865",
                    "context": "documentation"
                  },
                  "storage_key": "03403fa6-4cae-4883-b161-8a90ac3b5865",
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
            "content": "You can now control your character's movement using the W, A, S, D keys. Moving the mouse moves the camera, and pressing the spacebar causes the character to jump.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "7Mo",
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

## Result

![image alt text](https://dev.epicgames.com/community/api/documentation/image/41c81ff4-98c1-4264-b64e-623f3a4bd691)
