# Setting Up a Game Mode

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-a-game-mode-in-unreal-engine

> Application Version: 5.7

The **GameMode** defines the game's set of rules. The rules can include how players join the game, game pausing, and level transition, as well as any game-specific behavior such as win conditions. The GameMode is set for each level, and GameModes can be reused in multiple levels.

## Implementation Guide

```json
{
  "type": "include",
  "excerpt_id": 1548,
  "excerpt_assignment_id": 1339,
  "blocks": [
    {
      "type": "paragraph",
      "content": "This guide covers how to create a GameMode Blueprint and set default values for it, how to assign a Default GameMode for your game, and how to override the Default GameMode through the World Settings and GameMode Override option.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Creating a Game Mode Blueprint",
      "level": 3,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The steps below will guide you in creating and setting up defaults for a <strong>Game Mode</strong> Blueprint.",
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
          "content": "For this example, we are using the <strong>Blueprint Third Person Template</strong>; however you can use any project you wish.",
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
            "content": "In the <strong>Content Browser</strong>, click the <strong>Add New</strong> button.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25711725,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25711725,
              "file_name": "ContentBrowserAddNew.png",
              "file_size": 11907,
              "content_type": "image/png",
              "created_at": "2025-06-03T20:09:34.084+00:00",
              "height": 98,
              "width": 457,
              "storage_key": "08732cc7-a2d3-4e5f-8313-0796637dbd41",
              "context": "documentation"
            },
            "storage_key": "08732cc7-a2d3-4e5f-8313-0796637dbd41",
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
            "content": "Select <strong>Blueprint Class</strong> from the <strong>Create Basic Asset</strong> section of the dropdown menu.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25711726,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25711726,
              "file_name": "ContentBrowserDropDown.png",
              "file_size": 22935,
              "content_type": "image/png",
              "created_at": "2025-06-03T20:09:34.218+00:00",
              "height": 371,
              "width": 213,
              "storage_key": "e93cfb34-4d9c-4c09-ba5c-4c2084c751d5",
              "context": "documentation"
            },
            "storage_key": "e93cfb34-4d9c-4c09-ba5c-4c2084c751d5",
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
                "content": "You can create several different <a href=\"programming-and-scripting/blueprints-visual-scripting/UserGuide/Types\">types of Blueprint Assets</a> from the <strong>Blueprints</strong> option under <strong>Create Advanced Asset</strong>.",
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
            "content": "Choose a <strong>Parent Class</strong> for your Blueprint Asset. See <a data-document-id=\"3228035\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-class-assets-in-unreal-engine\">Parent Classes</a> for more information.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25711727,
            "caption": "",
            "alt_text": "Choose a Parent Class",
            "image": {
              "id": 25711727,
              "file_name": "new_asset_parent_class.png",
              "file_size": 49979,
              "content_type": "image/png",
              "created_at": "2025-06-03T20:09:34.301+00:00",
              "height": 379,
              "width": 514,
              "storage_key": "dbc1917c-a4a6-4986-a658-4179c2ccc8d0",
              "context": "documentation"
            },
            "storage_key": "dbc1917c-a4a6-4986-a658-4179c2ccc8d0",
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
      "content": "In the <strong>Pick Parent Class</strong> window, select the <strong>Game Mode Base</strong> Class. This is the parent class for all Game Modes.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Editing the Game Mode Defaults",
      "level": 3,
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
            "content": "<strong>Double-click</strong> on the Blueprint to open it, click the <strong>Class Defaults</strong>  button to open the Blueprint Defaults in the <strong>Details</strong> panel.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Under the <strong>Game Mode</strong> are several options that you can set as the game's default settings (default character, HUD, etc.).",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25711728,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25711728,
              "file_name": "GameMode_5.png",
              "file_size": 47701,
              "content_type": "image/png",
              "created_at": "2025-06-03T20:09:34.391+00:00",
              "height": 589,
              "width": 502,
              "storage_key": "6159dbd0-d0ea-4090-a442-04bffb11555a",
              "context": "documentation"
            },
            "storage_key": "6159dbd0-d0ea-4090-a442-04bffb11555a",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Here we are assigning the Character Blueprint called ThirdPersonCharacter as the Default Pawn Class for players to use in the game.",
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
                "content": "The <strong>Game Mode</strong> Blueprint points to existing Blueprints of the Character, HUD, PlayerController, Spectator, and Game State Classes. You will need to create these separately then specify them for use in the Game Mode Blueprint in order to actually use them in your game.",
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
    },
    {
      "type": "header",
      "content": "Assigning a Default Game Mode",
      "level": 3,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "In the previous section, we created a Game Mode Blueprint. Once you have a Game Mode Blueprint, you can assign it as the Default Game Mode to use in your game. The steps below will guide you through assigning the Default Game Mode through the Project Settings option.",
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
            "content": "From the Main Editor Window, click the <strong>Edit</strong> button from the Menu Bar, then select <strong>Project Settings</strong>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25711729,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25711729,
              "file_name": "GameMode_6.png",
              "file_size": 118901,
              "content_type": "image/png",
              "created_at": "2025-06-03T20:09:34.509+00:00",
              "height": 820,
              "width": 1044,
              "storage_key": "2bb6c3ae-3d14-466b-b079-111f850587ff",
              "context": "documentation"
            },
            "storage_key": "2bb6c3ae-3d14-466b-b079-111f850587ff",
            "context": "documentation",
            "width": 400,
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "In the <strong>Project Settings</strong> window, click the <strong>Maps & Modes</strong> option.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25711730,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25711730,
              "file_name": "GameMode_7.png",
              "file_size": 13268,
              "content_type": "image/png",
              "created_at": "2025-06-03T20:09:34.660+00:00",
              "height": 174,
              "width": 244,
              "storage_key": "c4b7e9f8-9cfa-4704-8bb6-7ff5179b9815",
              "context": "documentation"
            },
            "storage_key": "c4b7e9f8-9cfa-4704-8bb6-7ff5179b9815",
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
            "content": "In <strong>Maps & Modes</strong> under <strong>Default Modes</strong>, click the <strong>Default GameMode</strong> drop-down box and assign the <strong>GameMode</strong> you wish to use.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25711731,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25711731,
              "file_name": "GameMode_8.png",
              "file_size": 26118,
              "content_type": "image/png",
              "created_at": "2025-06-03T20:09:34.730+00:00",
              "height": 156,
              "width": 561,
              "storage_key": "9481267e-284d-498b-bbd4-84fba7a1302a",
              "context": "documentation"
            },
            "storage_key": "9481267e-284d-498b-bbd4-84fba7a1302a",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "This will assign the <strong>GameMode</strong> you select as the <strong>Default Game Mode</strong> whenever the project is loaded.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "If you click the arrow next to <strong>Selected GameMode</strong>, you will see the current settings used by the assigned <strong>GameMode</strong>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25711732,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25711732,
              "file_name": "GameMode_9.png",
              "file_size": 21650,
              "content_type": "image/png",
              "created_at": "2025-06-03T20:09:34.828+00:00",
              "height": 177,
              "width": 429,
              "storage_key": "93fc7305-9c28-4536-9d2f-cbabeebbb39f",
              "context": "documentation"
            },
            "storage_key": "93fc7305-9c28-4536-9d2f-cbabeebbb39f",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Here we can see that <strong>ThirdPersonCharacter</strong> is being used as the <strong>Default Pawn Class</strong>.",
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
      "type": "header",
      "content": "Overriding the Default Game Mode",
      "level": 3,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "When you have a Default Game Mode assigned, you can overwrite it on a per level basis through the World Settings menu under the GameMode Override section. The steps below will show you how to override the default Game Mode.",
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
            "content": "From the Main Editor Window, click the <strong>World Settings</strong> button from the Main Toolbar.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25711733,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25711733,
              "file_name": "GameMode_10.png",
              "file_size": 38847,
              "content_type": "image/png",
              "created_at": "2025-06-03T20:09:34.914+00:00",
              "height": 307,
              "width": 236,
              "storage_key": "42d59bac-6915-4a86-a60d-789fdb9680d0",
              "context": "documentation"
            },
            "storage_key": "42d59bac-6915-4a86-a60d-789fdb9680d0",
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
            "content": "This will open the <strong>World Settings</strong> option which will appear in the bottom right window where the <strong>Details</strong> tab is located.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Inside the <strong>World Settings</strong>, under <strong>Game Mode</strong>, you can click the <strong>GameMode Override</strong> drop-down box to change the <strong>GameMode</strong> used.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25711734,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25711734,
              "file_name": "GameMode_11.png",
              "file_size": 26697,
              "content_type": "image/png",
              "created_at": "2025-06-03T20:09:35.040+00:00",
              "height": 263,
              "width": 378,
              "storage_key": "dbaca3e3-bf80-44f0-a454-191f3ebbca80",
              "context": "documentation"
            },
            "storage_key": "dbaca3e3-bf80-44f0-a454-191f3ebbca80",
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
  "excerpt_hash_id": "yze",
  "settings": {
    "is_hidden": false
  }
}
```
