# Types of Blueprints

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/types-of-blueprints-in-unreal-engine

> Application Version: 5.7

Sometimes it is difficult to tell which type of **Blueprint** you should use at first glance, especially
when it comes to **Blueprint Macro Libraries** and **Blueprint Classes**. A good rule of thumb is to ask yourself:

- *Are there multiple instances?*

If you will have more than one or two instances (e.g., a TV set that can be shot or turned on/off),
then it probably makes sense to create a Blueprint Class, with associated code living there.
If not, and you just want to have some helper functions (like find all Actors within X units), those
are ideal to live in a Blueprint Macro Library.

```json
{
  "type": "include",
  "excerpt_id": 1058,
  "excerpt_assignment_id": 1276,
  "blocks": [
    {
      "type": "header",
      "content": "Level Blueprint",
      "level": 2,
      "settings": {
        "is_hidden": false,
        "anchor_id": 16826,
        "anchor": {
          "id": 16826,
          "name": "level-blueprint"
        }
      }
    },
    {
      "type": "image",
      "image_id": 24624314,
      "caption": "",
      "alt_text": "",
      "image": {
        "id": 24624314,
        "file_name": "level_blueprint_test_image.png",
        "file_size": 53104,
        "content_type": "image/png",
        "created_at": "2025-05-20T23:21:18.353+00:00",
        "height": 192,
        "width": 464,
        "storage_key": "983d2468-a6b6-4fb3-9034-0129a3084e54",
        "context": "documentation"
      },
      "storage_key": "983d2468-a6b6-4fb3-9034-0129a3084e54",
      "context": "documentation",
      "width": 250,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "A <strong>Level Blueprint</strong> is a specialized type of <strong>Blueprint</strong> that acts as a level-wide global event graph.\nEach level in your project has its own Level Blueprint created by default that can be edited within the Unreal Editor, however new Level Blueprints\ncannot be created through the editor interface.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Events pertaining to the level as a whole, or specific instances of Actors within the level, are\nused to fire off sequences of actions in the form of Function Calls or Flow Control operations.\nThose familiar with Unreal Engine 3 should be very familiar with this concept as this is very similar\nto how Kismet worked in Unreal Engine 3.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Level Blueprints also provide a control mechanism for level streaming and <a data-document-id=\"3233705\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/real-time-compositing-with-sequencer-in-unreal-engine\">Sequencer</a> as well\nas for binding events to Actors placed within the level.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "For more information on this section, please see <a data-document-id=\"3228029\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/level-blueprint-in-unreal-engine\">Level Blueprint</a>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Blueprint Class",
      "level": 2,
      "settings": {
        "is_hidden": false,
        "anchor_id": 16825,
        "anchor": {
          "id": 16825,
          "name": "blueprint-class"
        }
      }
    },
    {
      "type": "image",
      "image_id": 24624315,
      "caption": "",
      "alt_text": "",
      "image": {
        "id": 24624315,
        "file_name": "class_blueprint_test_image.png",
        "file_size": 57703,
        "content_type": "image/png",
        "created_at": "2025-05-20T23:21:18.458+00:00",
        "height": 192,
        "width": 464,
        "storage_key": "6e364b5d-0408-451b-97ce-df4f2975c91a",
        "context": "documentation"
      },
      "storage_key": "6e364b5d-0408-451b-97ce-df4f2975c91a",
      "context": "documentation",
      "width": 250,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "A <strong>Blueprint Class</strong>, often shortened as <strong>Blueprint</strong>, is an asset that allows content creators to easily add functionality on top of existing gameplay classes.\nBlueprints are created inside of Unreal Editor visually, instead of by typing code, and saved as assets in a content package.\nThese essentially define a new class or type of Actor which can then be placed into maps as instances that behave like any other type of Actor.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "For more information on this section, please see <a data-document-id=\"3228035\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-class-assets-in-unreal-engine\">Blueprint Class</a>.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "Vm7",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "include",
  "excerpt_id": 1059,
  "excerpt_assignment_id": 1277,
  "blocks": [
    {
      "type": "header",
      "content": "Data-Only Blueprint",
      "level": 2,
      "settings": {
        "is_hidden": false,
        "anchor_id": 16827,
        "anchor": {
          "id": 16827,
          "name": "data-only-blueprint"
        }
      }
    },
    {
      "type": "image",
      "image_id": 24624316,
      "caption": "",
      "alt_text": "",
      "image": {
        "id": 24624316,
        "file_name": "data_blueprint.png",
        "file_size": 31784,
        "content_type": "image/png",
        "created_at": "2025-05-20T23:21:19.001+00:00",
        "height": 232,
        "width": 462,
        "storage_key": "ec326bcd-2a42-43e4-b43f-2d49fa9524c6",
        "context": "documentation"
      },
      "storage_key": "ec326bcd-2a42-43e4-b43f-2d49fa9524c6",
      "context": "documentation",
      "width": 250,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "A <strong>Data-Only Blueprint</strong> is a Blueprint Class that contains only the code (in the form of node graphs), variables, and components\ninherited from its parent. These allow those inherited properties to be tweaked and modified, but no new elements can be added.\nThese are essentially a replacement for archetypes and can be used to allow designers to tweak properties or set items with variations.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Data-Only Blueprint are edited in a compact property editor, but can also be \"converted\" to full Blueprints by simply adding code,\nvariables, or components using the full <strong>Blueprint Editor</strong>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "For more information on this section, please see <a data-document-id=\"3228035\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-class-assets-in-unreal-engine\">Data-Only Blueprint</a>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Blueprint Interface",
      "level": 2,
      "settings": {
        "is_hidden": false,
        "anchor_id": 16828,
        "anchor": {
          "id": 16828,
          "name": "blueprint-interface"
        }
      }
    },
    {
      "type": "image",
      "image_id": 24624317,
      "caption": "",
      "alt_text": "",
      "image": {
        "id": 24624317,
        "file_name": "blueprint_interface.png",
        "file_size": 44537,
        "content_type": "image/png",
        "created_at": "2025-05-20T23:21:19.121+00:00",
        "height": 218,
        "width": 464,
        "storage_key": "47fe7c2e-95c3-48f7-8a12-33f611b57982",
        "context": "documentation"
      },
      "storage_key": "47fe7c2e-95c3-48f7-8a12-33f611b57982",
      "context": "documentation",
      "width": 250,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "A <strong>Blueprint Interface</strong> is a collection of one or more functions - name only, no implementation - that can be added to\nother Blueprints. Any Blueprint that has the Interface added is guaranteed to have those functions. The functions\nof the Interface can be given functionality in each of the Blueprints that added it. This is essentially like the\nconcept of an interface in general programming, which allows multiple different types of Objects to all share and be accessed\nthrough a common interface. Put simply, Blueprint Interfaces allow different Blueprints to share with and send data to one another.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Blueprint Interfaces can be made by content creators through the editor in a similar fashion to other Blueprints, but they\ncome with certain limitations in that they cannot:",
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
            "content": "Add new variables",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Edit graphs",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Add Components",
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
      "content": "For more information on this section, please see <a data-document-id=\"3227986\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-interface-in-unreal-engine\">Blueprint Interface</a>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Blueprint Macro Library",
      "level": 2,
      "settings": {
        "is_hidden": false,
        "anchor_id": 16829,
        "anchor": {
          "id": 16829,
          "name": "blueprint-macro-library"
        }
      }
    },
    {
      "type": "image",
      "image_id": 24624318,
      "caption": "",
      "alt_text": "",
      "image": {
        "id": 24624318,
        "file_name": "macro_blueprint.png",
        "file_size": 18460,
        "content_type": "image/png",
        "created_at": "2025-05-20T23:21:19.210+00:00",
        "height": 192,
        "width": 464,
        "storage_key": "1e390d83-f6bc-4278-885c-a1325aff0f43",
        "context": "documentation"
      },
      "storage_key": "1e390d83-f6bc-4278-885c-a1325aff0f43",
      "context": "documentation",
      "width": 250,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "A <strong>Blueprint Macro Library</strong> is a container that holds a collection of <strong>Macros</strong> or self-contained graphs that can\nbe placed as nodes in other Blueprints. These can be time-savers as they can store commonly used sequences of nodes\ncomplete with inputs and outputs for both execution and data transfer.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Macros are shared among all graphs that reference them, but they are auto-expanded into graphs as if they were a\ncollapsed node during compiling. This means that Blueprint Macro Libraries do not need to be compiled. However, changes\nto a Macro are only reflected in graphs that reference that Macro when the Blueprint containing those graphs is\nrecompiled.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "For more information on this section, please see <a data-document-id=\"3228034\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-macro-library-in-unreal-engine\">Blueprint Macro Library</a>.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "3Zv",
  "settings": {
    "is_hidden": false
  }
}
```
