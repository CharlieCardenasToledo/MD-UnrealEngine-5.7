# Using Editor Viewports

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-editor-viewports-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "include",
  "excerpt_id": 2729,
  "excerpt_assignment_id": 2686,
  "blocks": [
    {
      "type": "paragraph",
      "content": "The <strong>Viewports</strong> are your window into the worlds you create in Unreal. They can be navigated just as you would in a game, or can be used in a more schematic design sense as you would for an architectural Blueprint. The Unreal Editor viewports contain a variety of tools and visualizers to help you see exactly the data you need.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "0NRN",
  "settings": {
    "is_hidden": false
  }
}
```

![Viewports Topic](https://dev.epicgames.com/community/api/documentation/image/b34724a9-e863-4739-a207-01c32bac9d47)

_Click image for full size._

## Viewport Types

There are two main types of Viewports in Unreal Editor: Perspective and Orthographic. The perspective view is a
3D window into the game world. The Orthographic views - Front, Side, and Top - are 2D Viewports that each look
down one of the main axes (X, Y, or Z).

```json
{
  "type": "include",
  "excerpt_id": 2730,
  "excerpt_assignment_id": 2687,
  "blocks": [
    {
      "type": "enhanced_table",
      "widths": null,
      "rows": [
        [
          [
            {
              "type": "enhanced_table_header",
              "content": " ",
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
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": " ",
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
              "type": "image",
              "image_id": 26449614,
              "caption": "",
              "alt_text": "View Perspective",
              "image": {
                "id": 26449614,
                "file_name": "02-view-perspective.png",
                "file_size": 1503531,
                "content_type": "image/png",
                "created_at": "2026-02-16T22:35:02.142+00:00",
                "height": 839,
                "width": 1290,
                "storage_key": "72f4a04a-27c0-417a-9208-3dd817b8915f",
                "context": "documentation"
              },
              "storage_key": "72f4a04a-27c0-417a-9208-3dd817b8915f",
              "context": "documentation",
              "width": 500,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26449615,
              "caption": "",
              "alt_text": "View Front",
              "image": {
                "id": 26449615,
                "file_name": "03-view-front.png",
                "file_size": 464739,
                "content_type": "image/png",
                "created_at": "2026-02-16T22:35:02.440+00:00",
                "height": 839,
                "width": 1290,
                "storage_key": "122afc15-e39a-43d2-bb34-8952ffb2133a",
                "context": "documentation"
              },
              "storage_key": "122afc15-e39a-43d2-bb34-8952ffb2133a",
              "context": "documentation",
              "width": 500,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26449616,
              "caption": "",
              "alt_text": "View Side",
              "image": {
                "id": 26449616,
                "file_name": "04-view-side.png",
                "file_size": 426869,
                "content_type": "image/png",
                "created_at": "2026-02-16T22:35:02.577+00:00",
                "height": 839,
                "width": 1290,
                "storage_key": "88924040-3127-424c-85e0-5d0474adde18",
                "context": "documentation"
              },
              "storage_key": "88924040-3127-424c-85e0-5d0474adde18",
              "context": "documentation",
              "width": 500,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26449617,
              "caption": "",
              "alt_text": "View Top",
              "image": {
                "id": 26449617,
                "file_name": "05-view-top.png",
                "file_size": 267084,
                "content_type": "image/png",
                "created_at": "2026-02-16T22:35:02.775+00:00",
                "height": 839,
                "width": 1290,
                "storage_key": "dd1f5ccb-a0e0-4010-8287-8b38f7c33a0b",
                "context": "documentation"
              },
              "storage_key": "dd1f5ccb-a0e0-4010-8287-8b38f7c33a0b",
              "context": "documentation",
              "width": 500,
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
              "content": "Perspective (3D)",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Front (X-Axis)",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Side (Y-Axis)",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Top (Z-Axis)",
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
  "excerpt_hash_id": "on3X",
  "settings": {
    "is_hidden": false
  }
}
```

You can cycle through the types of Viewports by pressing **Alt** and **G**, **H**, **J**, or **K**. These set the
Viewport to be Perspective, Front, Side, or Top, respectively.

## Viewport Layout

By default, you see a single Perspective Viewport when you open Unreal Editor.

![Viewport](https://dev.epicgames.com/community/api/documentation/image/93559232-4d3e-4382-a528-b077b810f42f)

_Click image for full size._

The **Viewport** panel actually contains multiple Viewports, which are laid out in a grid and any of which can be shown
maximized. The default layout is a 4x4 that consists of one of each type of Viewport - Perspective, Top, Front, and Side.

![Viewport](https://dev.epicgames.com/community/api/documentation/image/7988ebf2-629a-45e7-997a-7e774c5cebfa)

_Click image for full size._

The Viewports can be minimized and maximized using the and
buttons located in the top right corner of each Viewport.

## View Modes

```json
{
  "type": "include",
  "excerpt_id": 1929,
  "excerpt_assignment_id": 2688,
  "blocks": [
    {
      "type": "paragraph",
      "content": "The Unreal Editor viewports have a large number of visualization modes to help you see the type of data being processed in your scene, as well as to diagnose any errors or unexpected results. The more common view modes have their own hotkeys, but all can be accessed from the viewport within the <strong>View Mode</strong> menu.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25777817,
      "caption": "Click image for full size.",
      "alt_text": "Viewmode Menu",
      "image": {
        "id": 25777817,
        "file_name": "02-viewmode-menu.png",
        "file_size": 186118,
        "content_type": "image/png",
        "created_at": "2025-07-03T18:58:21.168+00:00",
        "height": 397,
        "width": 528,
        "storage_key": "f0b875c4-9e6f-4dde-828c-3a66f34d7cfe",
        "context": "documentation"
      },
      "storage_key": "f0b875c4-9e6f-4dde-828c-3a66f34d7cfe",
      "context": "documentation",
      "width": 300,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25777818,
      "caption": "Click image for full size.",
      "alt_text": "Viewmodes Submenu Button",
      "image": {
        "id": 25777818,
        "file_name": "03-viewmodes-sub-menu-button.png",
        "file_size": 99471,
        "content_type": "image/png",
        "created_at": "2025-07-03T18:58:21.465+00:00",
        "height": 842,
        "width": 431,
        "storage_key": "eb151b7a-b4f4-463f-84d2-ecd8caadad7b",
        "context": "documentation"
      },
      "storage_key": "eb151b7a-b4f4-463f-84d2-ecd8caadad7b",
      "context": "documentation",
      "width": 300,
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "0Za",
  "settings": {
    "is_hidden": false
  }
}
```

The most commonly used view modes are shown here:

|   |   |   |
| --- | --- | --- |
| ![Viewmode Lit](https://dev.epicgames.com/community/api/documentation/image/93363bec-15e2-49cf-96a8-58b5d63e0b59) | ![Viewmode Unlit](https://dev.epicgames.com/community/api/documentation/image/dd342f34-2445-4714-b371-6bb7df11fc66) | ![Viewmode Wireframe](https://dev.epicgames.com/community/api/documentation/image/2fda6fbf-1b45-41aa-ab7b-74f511230caf) |
| Lit | Unlit | Wireframe |

See [Viewport Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-modes-in-unreal-engine) for a listing and description of all available modes.

## Game View

**Game View** causes the Viewport to display the scene as it would appear in the game. This means that none of the
editor-specific elements - such as the Actor icons - are shown. It gives you an easy way to see just how your level
will look when you run it in the game.

```json
{
  "type": "sequence_slider",
  "caption": "Drag the slider to toggle Game View.",
  "images": [
    {
      "image_id": 26449626,
      "storage_key": "5937d1de-46c2-432a-80d0-0814508550b5",
      "context": "documentation",
      "image": {
        "id": 26449626,
        "file_name": "15-game-view.png",
        "file_size": 1132959,
        "content_type": "image/png",
        "created_at": "2026-02-16T22:35:04.705+00:00",
        "height": 725,
        "width": 1322,
        "storage_key": "5937d1de-46c2-432a-80d0-0814508550b5",
        "context": "documentation"
      }
    },
    {
      "image_id": 26449627,
      "storage_key": "35b6eb95-45f7-4007-b6b5-47b12834c022",
      "context": "documentation",
      "image": {
        "id": 26449627,
        "file_name": "16-game-view-1.png",
        "file_size": 1069346,
        "content_type": "image/png",
        "created_at": "2026-02-16T22:35:04.908+00:00",
        "height": 725,
        "width": 1322,
        "storage_key": "35b6eb95-45f7-4007-b6b5-47b12834c022",
        "context": "documentation"
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

To enable Game View, simply press the **G** key (by default) with the Viewport focused or choose the **Game View** option from the
Viewport Options menu:

![Gamemode Viewport](https://dev.epicgames.com/community/api/documentation/image/74df4105-6c0d-457b-a05e-4e00d69c9109)

_Click image for full size._

## Immersive Mode

Viewports have another state in addition to maximized and minimized that they can be in called **Immersive Mode**. This refers to
Viewport being maximized out to the full extents of the window containing the **Viewport** panel. When you have the Level editor
maximized, this enables you to have your Viewport run in full-screen for a truly *immersive* editing experience!

To enable Immersive Mode, simply press the **F11** key (by default) with the Viewport focused or choose the **Immersive Mode** option
from the Viewport Options menu:

![Immersive Mode Options](https://dev.epicgames.com/community/api/documentation/image/f10c8dd2-bcca-4238-84d5-1bdc1756592a)

_Click image for full size._

You can restore the Viewport to normal using the same procedure above or by pressing the
button located at the top right of the Viewport when in Immersive Mode.

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "sequence_slider",
        "caption": "Drag the slider to see Immersive Mode in action!",
        "images": [
          {
            "image_id": 26449628,
            "storage_key": "e858b9d6-1934-4deb-b523-f0978e3cab66",
            "context": "documentation",
            "image": {
              "id": 26449628,
              "file_name": "20-immersive-mode.png",
              "file_size": 768337,
              "content_type": "image/png",
              "created_at": "2026-02-16T22:35:05.096+00:00",
              "height": 759,
              "width": 1430,
              "storage_key": "e858b9d6-1934-4deb-b523-f0978e3cab66",
              "context": "documentation"
            }
          },
          {
            "image_id": 26449629,
            "storage_key": "f215697c-5137-4068-94c0-152d6cd591b4",
            "context": "documentation",
            "image": {
              "id": 26449629,
              "file_name": "21-immersive-mode-1.png",
              "file_size": 806819,
              "content_type": "image/png",
              "created_at": "2026-02-16T22:35:05.290+00:00",
              "height": 759,
              "width": 1430,
              "storage_key": "f215697c-5137-4068-94c0-152d6cd591b4",
              "context": "documentation"
            }
          },
          {
            "image_id": 26449630,
            "storage_key": "83c7358b-a06e-4956-ade3-0c98b5a2bf77",
            "context": "documentation",
            "image": {
              "id": 26449630,
              "file_name": "22-immersive-mode-2.png",
              "file_size": 756285,
              "content_type": "image/png",
              "created_at": "2026-02-16T22:35:05.560+00:00",
              "height": 759,
              "width": 1430,
              "storage_key": "83c7358b-a06e-4956-ade3-0c98b5a2bf77",
              "context": "documentation"
            }
          },
          {
            "image_id": 26449631,
            "storage_key": "e8b8f1ed-30fd-4406-85da-c424ac864413",
            "context": "documentation",
            "image": {
              "id": 26449631,
              "file_name": "23-immersive-mode-3.png",
              "file_size": 691129,
              "content_type": "image/png",
              "created_at": "2026-02-16T22:35:05.749+00:00",
              "height": 759,
              "width": 1430,
              "storage_key": "e8b8f1ed-30fd-4406-85da-c424ac864413",
              "context": "documentation"
            }
          },
          {
            "image_id": 26449632,
            "storage_key": "34744c5b-248f-4de4-b39a-56379d628091",
            "context": "documentation",
            "image": {
              "id": 26449632,
              "file_name": "24-immersive-mode-4.png",
              "file_size": 786861,
              "content_type": "image/png",
              "created_at": "2026-02-16T22:35:05.945+00:00",
              "height": 759,
              "width": 1430,
              "storage_key": "34744c5b-248f-4de4-b39a-56379d628091",
              "context": "documentation"
            }
          },
          {
            "image_id": 26449633,
            "storage_key": "5c3aec76-a0e1-4afe-bc79-09abd2ff2858",
            "context": "documentation",
            "image": {
              "id": 26449633,
              "file_name": "25-immersive-mode-5.png",
              "file_size": 815947,
              "content_type": "image/png",
              "created_at": "2026-02-16T22:35:06.098+00:00",
              "height": 759,
              "width": 1430,
              "storage_key": "5c3aec76-a0e1-4afe-bc79-09abd2ff2858",
              "context": "documentation"
            }
          }
        ],
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "sequence_slider",
        "caption": "Drag the slider to see Immersive Mode in action!",
        "images": [
          {
            "image_id": 26449634,
            "storage_key": "80b1b355-a66f-45f2-8f93-4860b8e15b35",
            "context": "documentation",
            "image": {
              "id": 26449634,
              "file_name": "mac_immersive_1.png",
              "file_size": 497913,
              "content_type": "image/png",
              "created_at": "2026-02-16T22:35:06.261+00:00",
              "height": 530,
              "width": 940,
              "storage_key": "80b1b355-a66f-45f2-8f93-4860b8e15b35",
              "context": "documentation"
            }
          },
          {
            "image_id": 26449635,
            "storage_key": "202dc2b4-b99f-454c-b7e8-b2e853eedf57",
            "context": "documentation",
            "image": {
              "id": 26449635,
              "file_name": "mac_immersive_2.png",
              "file_size": 540002,
              "content_type": "image/png",
              "created_at": "2026-02-16T22:35:06.477+00:00",
              "height": 530,
              "width": 940,
              "storage_key": "202dc2b4-b99f-454c-b7e8-b2e853eedf57",
              "context": "documentation"
            }
          },
          {
            "image_id": 26449636,
            "storage_key": "95e045b0-a67e-4a7e-a816-c899eb67da81",
            "context": "documentation",
            "image": {
              "id": 26449636,
              "file_name": "mac_immersive_3.png",
              "file_size": 565988,
              "content_type": "image/png",
              "created_at": "2026-02-16T22:35:06.717+00:00",
              "height": 530,
              "width": 940,
              "storage_key": "95e045b0-a67e-4a7e-a816-c899eb67da81",
              "context": "documentation"
            }
          },
          {
            "image_id": 26449637,
            "storage_key": "73459377-c1e5-47c0-bb42-3da4934b30ab",
            "context": "documentation",
            "image": {
              "id": 26449637,
              "file_name": "mac_immersive_4.png",
              "file_size": 692798,
              "content_type": "image/png",
              "created_at": "2026-02-16T22:35:06.913+00:00",
              "height": 530,
              "width": 940,
              "storage_key": "73459377-c1e5-47c0-bb42-3da4934b30ab",
              "context": "documentation"
            }
          },
          {
            "image_id": 26449638,
            "storage_key": "867a659e-6a0c-4a68-9843-fca981747e00",
            "context": "documentation",
            "image": {
              "id": 26449638,
              "file_name": "mac_immersive_5.png",
              "file_size": 736189,
              "content_type": "image/png",
              "created_at": "2026-02-16T22:35:07.093+00:00",
              "height": 530,
              "width": 940,
              "storage_key": "867a659e-6a0c-4a68-9843-fca981747e00",
              "context": "documentation"
            }
          }
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
