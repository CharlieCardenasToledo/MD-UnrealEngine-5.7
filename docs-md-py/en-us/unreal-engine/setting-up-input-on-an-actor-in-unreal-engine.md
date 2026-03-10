# Setting Up Input on an Actor

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-input-on-an-actor-in-unreal-engine

> Application Version: 5.7

When developing your game, there may be instances when you want to allow the player to perform some form of **Input** on an Actor in your level. For example, perhaps you have a treasure chest that you want the player to be able to open when they approach it, or a light you want them to be able to turn on/off, or some other form of interactable object you want to affect in some way when the player presses a button.

Setting up Input for an Actor gives you a level of control over how and when the Actor responds to player input.

## Implementation Guide

```json
{
  "type": "include",
  "excerpt_id": 1709,
  "excerpt_assignment_id": 1419,
  "blocks": [
    {
      "type": "paragraph",
      "content": "This guide covers the basic methods on how to <strong>Enable Input</strong> or <strong>Disable Input</strong> for an Actor. By Enabling Input on an Actor, you can allow a player to press a button or key and execute events that affect the Actor in some way (be it turn a light on or off, open or close a door, activate something, etc.).",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The Enable/Disable Input Usage section also covers an approach to Enabling/Disabling Input using a <strong>Trigger Volume</strong> to determine if a player is near the Actor in the level. This is useful when you want a player to affect the Actor only when they are near or in range of the Actor to conceivably affect it in a real-world scenario.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Enabling Actor Input",
      "level": 3,
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
          "content": "For this example, we are using the <strong>Blueprint First Person Template with Starter Content</strong>.",
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
      "content": "The steps below will show you how to Enable Input for an Actor:",
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
            "content": "Inside the <strong>StarterContent/Blueprints</strong> folder, open the <strong>Blueprint_Effect_Fire</strong> asset.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "On the <strong>Event Graph</strong> tab, <strong>Right-click</strong> in the graph and search for then add the <strong>Event Begin Play</strong> node.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "In the graph, <strong>Right-click</strong> search for and add the <strong>Get Player Controller</strong> node.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "In the graph, <strong>Right-click</strong> search for and add the <strong>Enable Input</strong> node.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Connect the out pin of the <strong>Event Begin Play</strong> to the in pin of the <strong>Enable Input</strong> node.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Connect the <strong>Get Player Controller</strong> node to the in <strong>Player Controller</strong> pin on the <strong>Enable Input</strong> node.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25740150,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25740150,
              "file_name": "input_1.png",
              "file_size": 37218,
              "content_type": "image/png",
              "created_at": "2025-06-17T15:37:56.612+00:00",
              "height": 221,
              "width": 632,
              "storage_key": "5e16886c-9931-4887-90ca-fc0a606aff8b",
              "context": "documentation"
            },
            "storage_key": "5e16886c-9931-4887-90ca-fc0a606aff8b",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "This is the basic method in which you can enable input on an Actor.",
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
      "content": "The <strong>Enable Input</strong> node requires that a <strong>Target</strong> (usually Self - the Actor itself) as well as a <strong>Player Controller</strong> (the player that will be providing the input) be specified. With this setup, you could now search for and add <strong>Input Event</strong> nodes (such as a Key or Mouse Button press) and perform actions that affect the Actor when those keys are pressed.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "In the example above, the <strong>Event Begin Play</strong> node states that when the game is started (provided the Actor exists in the level), <strong>Enable Input</strong> for the <strong>Player Controller</strong> specified. The default Player Controller uses <strong>Player Index 0</strong> for Single Player games, if you were to have a multiplayer scenario, you could specify which player through the <strong>Player Index</strong> value.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Disabling Actor Input",
      "level": 3,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Just as you can Enable Input on an Actor, you can also Disable Input for an Actor by using the <strong>Disable Input</strong> node.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25740151,
      "caption": "",
      "alt_text": "",
      "image": {
        "id": 25740151,
        "file_name": "input_2.png",
        "file_size": 45089,
        "content_type": "image/png",
        "created_at": "2025-06-17T15:37:56.800+00:00",
        "height": 273,
        "width": 625,
        "storage_key": "d85d823b-2f33-446d-9d10-b90ea5cfc091",
        "context": "documentation"
      },
      "storage_key": "d85d823b-2f33-446d-9d10-b90ea5cfc091",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "In the example above, we used the aforementioned method of enabling input on the Actor then added an <strong>E</strong> Key Event. When the <strong>E</strong> key is pressed, we print to the screen some text then Disable Input on the Actor so that they can no longer provide input to the Actor.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "As with the <strong>Enable Input</strong> node, the <strong>Disable Input</strong> node requires that a <strong>Target</strong> and <strong>Player Controller</strong> be specified.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Enable/Disable Input Usage",
      "level": 3,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "While the methods noted above work for Enabling/Disabling Input, typically you would want some rules to govern when to allow the Actor to receive Input from a player. If we were to use the method above of Enabling Input on Event Begin Play and had a Key Press that turned on or off a light (for example), the player would be able to turn that light on/off from anywhere in the world.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "We would want to Enable/Disable Input based on if the player is near the light, similar to the below:",
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
            "content": "Inside the <strong>StarterContent/Blueprints</strong> folder, open the <strong>Blueprint_CeilingLight</strong> asset.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "In the <strong>Components</strong> panel, click the <strong>Add Component</strong>, then search for and add <strong>Sphere Collision</strong>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25740152,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25740152,
              "file_name": "input_3.png",
              "file_size": 16042,
              "content_type": "image/png",
              "created_at": "2025-06-17T15:37:56.852+00:00",
              "height": 296,
              "width": 286,
              "storage_key": "ab01e583-d9dc-4341-9f4c-fbd063228049",
              "context": "documentation"
            },
            "storage_key": "ab01e583-d9dc-4341-9f4c-fbd063228049",
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
            "content": "In the <strong>Details</strong> panel, set the <strong>Variable Name</strong> to <strong>Trigger</strong>, the <strong>Z Transform</strong> to <strong>-180.0</strong>, and <strong>Scale</strong> for <strong>X, Y, Z</strong> to <strong>8</strong>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25740153,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25740153,
              "file_name": "input_4.png",
              "file_size": 25145,
              "content_type": "image/png",
              "created_at": "2025-06-17T15:37:56.981+00:00",
              "height": 265,
              "width": 475,
              "storage_key": "03ba6861-7091-4653-b9f8-1f498f7355a8",
              "context": "documentation"
            },
            "storage_key": "03ba6861-7091-4653-b9f8-1f498f7355a8",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "We are going to Enable Input (when the player is inside) or Disable Input (when the player is outside) of the sphere.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Return to the <strong>Event Graph</strong>.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "In the <strong>MyBlueprint</strong> window, <strong>Right-click</strong> on the <strong>Trigger</strong> and choose <strong>Add Event -&gt; Add OnComponentBeginOverlap</strong>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25740154,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25740154,
              "file_name": "input_5.png",
              "file_size": 39244,
              "content_type": "image/png",
              "created_at": "2025-06-17T15:37:57.076+00:00",
              "height": 425,
              "width": 470,
              "storage_key": "31374d66-d764-400a-8c3a-17fa5d04c099",
              "context": "documentation"
            },
            "storage_key": "31374d66-d764-400a-8c3a-17fa5d04c099",
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
            "content": "<strong>Right-click</strong> on <strong>Trigger</strong> again and choose <strong>Add Event -&gt; Add OnComponentEndOverlap</strong>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25740155,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25740155,
              "file_name": "input_5b.png",
              "file_size": 33473,
              "content_type": "image/png",
              "created_at": "2025-06-17T15:37:57.189+00:00",
              "height": 378,
              "width": 286,
              "storage_key": "2ad610a2-b75a-4955-80bc-08b7f2df9800",
              "context": "documentation"
            },
            "storage_key": "2ad610a2-b75a-4955-80bc-08b7f2df9800",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "These two Event nodes should be added to the graph.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Drag off the <strong>Other Actor</strong> pin of the Begin Overlap node and search for and add the <strong>Cast To FirstPersonCharacter</strong> node.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25740156,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25740156,
              "file_name": "input_6.png",
              "file_size": 34727,
              "content_type": "image/png",
              "created_at": "2025-06-17T15:37:57.242+00:00",
              "height": 202,
              "width": 774,
              "storage_key": "6fd71573-613a-471b-987a-71684e6c5401",
              "context": "documentation"
            },
            "storage_key": "6fd71573-613a-471b-987a-71684e6c5401",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Here we are saying that when an Actor called <strong>FirstPersonCharacter</strong> (which is the default player character for the Project Template) overlaps the <strong>Trigger</strong>, do something.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Drag off the <strong>Other Actor</strong> pin of the End Overlap node and add the <strong>Cast To FirstPersonCharacter</strong> node.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "<strong>Right-click</strong> and add the <strong>Get Player Controller</strong> node, <strong>Enable Input</strong>, and <strong>Disable Input</strong> nodes.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Connect the nodes as shown below.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25740157,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25740157,
              "file_name": "input_7.png",
              "file_size": 123373,
              "content_type": "image/png",
              "created_at": "2025-06-17T15:37:57.319+00:00",
              "height": 433,
              "width": 849,
              "storage_key": "e9a84b37-c48d-4121-806c-bf1ff199701e",
              "context": "documentation"
            },
            "storage_key": "e9a84b37-c48d-4121-806c-bf1ff199701e",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Input will now only be enabled when the player enters the trigger and is disabled when the player leaves the trigger. This prevents the player from affecting the Actor from anywhere in the world and confines it to only when they are inside the trigger volume we created.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "<strong>Right-click</strong> and add the <strong>E</strong> Key Event and it to a <strong>Print String</strong> node.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25740158,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25740158,
              "file_name": "input_8.png",
              "file_size": 15586,
              "content_type": "image/png",
              "created_at": "2025-06-17T15:37:57.371+00:00",
              "height": 150,
              "width": 333,
              "storage_key": "e2b68314-fdd9-46e4-8952-41f18ec5f8f0",
              "context": "documentation"
            },
            "storage_key": "e2b68314-fdd9-46e4-8952-41f18ec5f8f0",
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
            "content": "<strong>Compile</strong> and <strong>Save</strong>, then close the Blueprint. (If you receive a Warning, ignore it and proceed to the next step.)",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Drag the <strong>Blueprint_CeilingLight</strong> into the level, then click the <strong>Play</strong> Button to play in the Editor.",
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
      "content": "When playing, if you press <strong>E</strong> when far away from the light, nothing should happen. When you get close to the light (inside the trigger) and press <strong>E</strong>, the text <strong>Hello</strong> should appear in the upper left corner of the window. For this example, we hooked up a <strong>Print String</strong> node, however you could toggle the light color, intensity, or other settings when the key is pressed and the player is inside the trigger sphere.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Input Details",
      "level": 3,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Replace the <strong>E</strong> Key Event in the example above and try using a <strong>Space Bar</strong> Key Event instead. When you play in the Editor, notice what happens. You can Jump by pressing <strong>Space Bar</strong> when outside of the trigger for the light, however when you enter the trigger and press <strong>Space Bar</strong>, you no longer Jump but instead call the <strong>Print String</strong> and text <strong>Hello</strong>; this is due to <strong>Input Priority</strong>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "When Input commands are shared (as is the case here with Jump and the input we assigned in our Light both tied to <strong>Space Bar</strong>), lower priority actions are ignored. Inside the light Blueprint, if you click on the <strong>Space Bar</strong> Key Event and look in the <strong>Details</strong> panel, you should see an option for <strong>Consume Input</strong>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25740159,
      "caption": "",
      "alt_text": "",
      "image": {
        "id": 25740159,
        "file_name": "input_9.png",
        "file_size": 21502,
        "content_type": "image/png",
        "created_at": "2025-06-17T15:37:57.418+00:00",
        "height": 197,
        "width": 534,
        "storage_key": "cae9eade-b4db-4e98-8f40-8464db0427be",
        "context": "documentation"
      },
      "storage_key": "cae9eade-b4db-4e98-8f40-8464db0427be",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "If you un-check the <strong>Consume Input</strong> checkbox and play in the Editor again, you should now be able to Jump both inside and outside of the light's trigger volume. When inside the light's trigger volume, by pressing <strong>Space Bar</strong> you will also call the <strong>Print String</strong> node and the <strong>Hello</strong> text to be displayed.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Also in the <strong>Input Details</strong> window are options for <strong>Execute when Paused</strong> (which allows you to press the Key during the paused state and execute commands) and <strong>Override Parent Binding</strong> (which allows you to remove any bindings set in any parent classes).",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "G5B",
  "settings": {
    "is_hidden": false
  }
}
```
