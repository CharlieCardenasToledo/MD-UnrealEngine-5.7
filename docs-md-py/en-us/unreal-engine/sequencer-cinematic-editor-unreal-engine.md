# Sequencer Editor

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine

> Application Version: 5.7

The **Sequencer Editor** is the main interface you can use to edit [Level Sequences assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview), in order to create cinematic content in **Unreal Engine**.

The following document provides an overview of the Sequencer Editor's user Interface, tools, and properties.

![sequencer editor overview with highlights](https://dev.epicgames.com/community/api/documentation/image/4fae29f8-a06e-46a8-8825-38fd79949801)

1. [Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.5#toolbar)
2. [Outliner](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.5#outliner)
3. [Timeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.5#timeline)
4. [Playback Controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.5#playback-controls)

## Toolbar

The Sequencer Editor Toolbar contains a suite of tools, options and settings you can use to interface with Level Sequence assets.

![sequencer toolbar overview with highlights](https://dev.epicgames.com/community/api/documentation/image/9183e3c2-43eb-4fa3-a663-f6cbbc7e36c5)

```json
{
  "type": "include",
  "excerpt_id": 2727,
  "excerpt_assignment_id": 2643,
  "blocks": [
    {
      "type": "enhanced_table",
      "widths": null,
      "rows": [
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Name",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "Icon",
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
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<a data-document-id=\"3231539\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine\">World</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395362,
              "caption": "",
              "alt_text": "sequencer world",
              "image": {
                "id": 26395362,
                "file_name": "World.png",
                "file_size": 751,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:27.430+00:00",
                "height": 25,
                "width": 24,
                "storage_key": "dc5caa23-d662-4f46-9e8a-f33f95c24a36",
                "context": "documentation"
              },
              "storage_key": "dc5caa23-d662-4f46-9e8a-f33f95c24a36",
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
              "content": "Lists information on the current world context, Level Sequence Actor, and playback realm. It contains options for specifying whether you want your sequence to autobind to Play In Editor (PIE), Simulation, or other runtime sessions.",
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
              "content": "<strong>Save</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395363,
              "caption": "",
              "alt_text": "sequencer save",
              "image": {
                "id": 26395363,
                "file_name": "Save.png",
                "file_size": 281,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:27.618+00:00",
                "height": 25,
                "width": 24,
                "storage_key": "1eefd7cc-eb88-4f34-85df-853b00128fc8",
                "context": "documentation"
              },
              "storage_key": "1eefd7cc-eb88-4f34-85df-853b00128fc8",
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
              "content": "Saves the current sequence and any subscenes or shots.",
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
              "content": "<strong>Find in Content Browser</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395364,
              "caption": "",
              "alt_text": "sequencer find",
              "image": {
                "id": 26395364,
                "file_name": "FindCB.png",
                "file_size": 814,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:27.696+00:00",
                "height": 25,
                "width": 24,
                "storage_key": "bf37f8bc-8f92-405c-a0aa-6a5b6c1702f9",
                "context": "documentation"
              },
              "storage_key": "bf37f8bc-8f92-405c-a0aa-6a5b6c1702f9",
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
              "content": "Locates the current sequence's Level Sequence asset in the Content Browser.",
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
              "content": "<a data-document-id=\"3231539\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine\">Create Camera</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395365,
              "caption": "",
              "alt_text": "sequencer camera",
              "image": {
                "id": 26395365,
                "file_name": "Camera.png",
                "file_size": 838,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:27.793+00:00",
                "height": 25,
                "width": 24,
                "storage_key": "52b93f05-a804-4d5b-9b92-1b5940186aa6",
                "context": "documentation"
              },
              "storage_key": "52b93f05-a804-4d5b-9b92-1b5940186aa6",
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
              "content": "Creates a new <strong><a data-document-id=\"3231737\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine\">Cine Camera Actor</a></strong>. A new <strong><a data-document-id=\"3231594\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-camera-cut-track-in-unreal-engine\">Camera Cut Track</a></strong> will also be created and will reference this camera if one had not already been created.",
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
              "content": "<a data-document-id=\"3231539\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine\">Render</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395366,
              "caption": "",
              "alt_text": "sequencer render",
              "image": {
                "id": 26395366,
                "file_name": "Render.png",
                "file_size": 767,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:27.918+00:00",
                "height": 25,
                "width": 24,
                "storage_key": "7359ff39-ee0a-4abc-8d7d-f30933b5a58b",
                "context": "documentation"
              },
              "storage_key": "7359ff39-ee0a-4abc-8d7d-f30933b5a58b",
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
              "content": "Opens the <strong><a href=\"animating-characters-and-objects/Sequencer/Overview/RenderMovieSettings\"></a></strong> Settings dialog, or the <strong><a href=\"animating-characters-and-objects/Sequencer/movie-render-pipeline#movierenderqueue\">Movie Render Queue</a></strong> if its plugin is enabled.",
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
              "content": "<a data-document-id=\"3231539\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine\">Director Blueprint</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395367,
              "caption": "",
              "alt_text": "sequencer director",
              "image": {
                "id": 26395367,
                "file_name": "DirectorBP.png",
                "file_size": 711,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:27.990+00:00",
                "height": 25,
                "width": 24,
                "storage_key": "fd2fee70-e35a-4ec3-b9b8-3534e9670e3f",
                "context": "documentation"
              },
              "storage_key": "fd2fee70-e35a-4ec3-b9b8-3534e9670e3f",
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
              "content": "Opens the Director Blueprint for this sequence, from which <strong><a data-document-id=\"3231545\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-event-track-in-unreal-engine\">Event Track</a></strong> logic can be accessed.",
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
              "content": "<a data-document-id=\"3231539\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine\">Actions</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395368,
              "caption": "",
              "alt_text": "sequencer actions",
              "image": {
                "id": 26395368,
                "file_name": "Actions.png",
                "file_size": 614,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:28.071+00:00",
                "height": 25,
                "width": 24,
                "storage_key": "d8b0d06e-04a0-41b7-9d4f-feb727e323f3",
                "context": "documentation"
              },
              "storage_key": "d8b0d06e-04a0-41b7-9d4f-feb727e323f3",
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
              "content": "Lists various sequence editor actions such as saving, import/export, baking, and selection editing.",
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
              "content": "<a data-document-id=\"3231539\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine\">View Options</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395369,
              "caption": "",
              "alt_text": "sequencer view options",
              "image": {
                "id": 26395369,
                "file_name": "View.png",
                "file_size": 753,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:28.182+00:00",
                "height": 25,
                "width": 24,
                "storage_key": "49a637c6-35d5-4a8a-94ab-1dc61d84e4c9",
                "context": "documentation"
              },
              "storage_key": "49a637c6-35d5-4a8a-94ab-1dc61d84e4c9",
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
              "content": "Lists various sequence view options.",
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
              "content": "<a data-document-id=\"3231539\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine\">Playback Options</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395370,
              "caption": "",
              "alt_text": "sequencer playback options",
              "image": {
                "id": 26395370,
                "file_name": "Playback.png",
                "file_size": 394,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:28.231+00:00",
                "height": 25,
                "width": 24,
                "storage_key": "c1072739-d497-4cb7-bf75-5e08aa27d982",
                "context": "documentation"
              },
              "storage_key": "c1072739-d497-4cb7-bf75-5e08aa27d982",
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
              "content": "Lists various playback options such as playrate, start/end times, and playhead behavior.",
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
              "content": "<a data-document-id=\"3231539\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine\">Keyframe Options</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395371,
              "caption": "",
              "alt_text": "sequencer keyframe options",
              "image": {
                "id": 26395371,
                "file_name": "Keying.png",
                "file_size": 526,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:28.296+00:00",
                "height": 25,
                "width": 24,
                "storage_key": "7f634ee6-8154-46f0-90b7-a30b2dd91bcb",
                "context": "documentation"
              },
              "storage_key": "7f634ee6-8154-46f0-90b7-a30b2dd91bcb",
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
              "content": "Lists settings for Auto Key transform keyframing behavior, and what default tangents are created.",
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
              "content": "<a data-document-id=\"3231539\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine\">Auto Key</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395372,
              "caption": "",
              "alt_text": "sequencer autokey",
              "image": {
                "id": 26395372,
                "file_name": "Autokey.png",
                "file_size": 756,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:28.358+00:00",
                "height": 25,
                "width": 24,
                "storage_key": "ebeaa4ec-51e6-483a-ac39-a718afc452e9",
                "context": "documentation"
              },
              "storage_key": "ebeaa4ec-51e6-483a-ac39-a718afc452e9",
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
              "content": "Enables Autokey mode, where keyframes are automatically created whenever a property or transform changes.",
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
              "content": "<a data-document-id=\"3231539\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine\">Edit Options</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395373,
              "caption": "",
              "alt_text": "sequencer edit options",
              "image": {
                "id": 26395373,
                "file_name": "Edits.png",
                "file_size": 543,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:28.416+00:00",
                "height": 25,
                "width": 24,
                "storage_key": "48d756c5-0538-40e1-974f-c36f0a4a9415",
                "context": "documentation"
              },
              "storage_key": "48d756c5-0538-40e1-974f-c36f0a4a9415",
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
              "content": "Lists settings for how edits from the Details panel are interpreted by Sequencer when using Auto Key.",
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
              "content": "<a data-document-id=\"3231539\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine\">Snapping</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395374,
              "caption": "",
              "alt_text": "sequencer snapping",
              "image": {
                "id": 26395374,
                "file_name": "Snapping.png",
                "file_size": 677,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:28.496+00:00",
                "height": 25,
                "width": 24,
                "storage_key": "e8e50238-8312-46bd-a3c6-be3d7282f0d0",
                "context": "documentation"
              },
              "storage_key": "e8e50238-8312-46bd-a3c6-be3d7282f0d0",
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
              "content": "Enables snapping. The dropdown menu next to this lists options for setting snapping rules for keyframes, sections, and the timeline.",
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
              "content": "<a data-document-id=\"3231539\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine\">Frames Per Second</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395375,
              "caption": "",
              "alt_text": "sequencer fps",
              "image": {
                "id": 26395375,
                "file_name": "PlaybackOptions.png",
                "file_size": 832,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:28.582+00:00",
                "height": 25,
                "width": 59,
                "storage_key": "0c206d89-4346-49c9-bc74-3d3ba82bea2e",
                "context": "documentation"
              },
              "storage_key": "0c206d89-4346-49c9-bc74-3d3ba82bea2e",
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
              "content": "Lists settings for various Frames Per Second (FPS) targets at runtime. Also contains options to enable the runtime to lock to the chosen frame rate.",
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
              "content": "<a data-document-id=\"3231539\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine\">Curve Editor</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395376,
              "caption": "",
              "alt_text": "sequencer curve editor",
              "image": {
                "id": 26395376,
                "file_name": "CurveEditor.png",
                "file_size": 564,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:28.639+00:00",
                "height": 25,
                "width": 24,
                "storage_key": "502793cc-5899-4338-bb55-dbb51548ce3c",
                "context": "documentation"
              },
              "storage_key": "502793cc-5899-4338-bb55-dbb51548ce3c",
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
              "content": "Opens the <strong><a data-document-id=\"3231544\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine\">Curve Editor</a></strong> which is used for fine tuning of animation keyframes and tangents.",
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
              "content": "<a data-document-id=\"3231539\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine\">Breadcrumbs</a>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395377,
              "caption": "",
              "alt_text": "sequencer breadcrumbs",
              "image": {
                "id": 26395377,
                "file_name": "Breadcrumbs.png",
                "file_size": 3436,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:28.717+00:00",
                "height": 25,
                "width": 210,
                "storage_key": "b8b6bfcb-cd15-4563-b81c-e9561d9a2a45",
                "context": "documentation"
              },
              "storage_key": "b8b6bfcb-cd15-4563-b81c-e9561d9a2a45",
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
              "content": "Displays the current sequence name, and is used to navigate master sequences and shots.",
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
              "content": "<strong>Lock</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 26395378,
              "caption": "",
              "alt_text": "sequencer lock",
              "image": {
                "id": 26395378,
                "file_name": "Lock.png",
                "file_size": 392,
                "content_type": "image/png",
                "created_at": "2026-01-19T19:24:28.800+00:00",
                "height": 25,
                "width": 25,
                "storage_key": "e42accf1-0fe4-488f-983b-5e0e90db20ad",
                "context": "documentation"
              },
              "storage_key": "e42accf1-0fe4-488f-983b-5e0e90db20ad",
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
              "content": "Locks the entire sequence to prevent editing.",
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
  "excerpt_hash_id": "j1L4",
  "settings": {
    "is_hidden": false
  }
}
```

Refer to [Sequence Editor toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) for more information about Sequencer's toolbar.

## Outliner

The Sequencer Editor's Outliner contains a list of the Level Sequence asset's tracks, as well as tools to add, filter, and search for tracks. Tracks can represent Actors attached to your Level Sequence such as Cameras, Characters, Audio, and Effects.

![sequencer outliner overview with highlights](https://dev.epicgames.com/community/api/documentation/image/30e697d1-4fa4-4701-b6db-84a323350bf7)

Refer to [Sequencer Tracks](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine) for more information about different types of tracks.

## Timeline

The Sequencer's Timeline is a non-linear editing environment that represents the entire playable region of your Level Sequence asset. The Timeline includes horizontal regions for each Track, and can include assets, keyframes and timeline controls.

The playback range of your Level Sequence asset is contained within **Start** (Green) and **End** (Red) markers. The current location of your playback is indicated by the [Playhead](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.5#playhead).

![sequencer overview with highlights](https://dev.epicgames.com/community/api/documentation/image/8db0e44f-a6d1-43cc-b2d1-3ffc50f04d94)

### Navigation

To navigate your Level Sequence asset in the Sequencer Editor, you can [pan](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.5#panning) and [zoom](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.5#zooming) within the timeline.

#### Panning

You can pan your Timeline view vertically, to see additional track regions, by dragging the right-side scrollbar up and down.

![sequencer vertical pan scroll bar](https://dev.epicgames.com/community/api/documentation/image/1bdc4fa0-d883-4718-9c42-66ea1f278855)

You can pan and zoom the Timeline view horizontally, to see different content in the playback, using the **Range Slider** at the bottom of the timeline.

Dragging the middle area of the slider pans, while dragging the left/right margins will zoom your view.

[Video: V_axy6oN](https://dev.epicgames.com/community/api/cms/videos/V_axy6oN/embed.html)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The Range Slider is enabled by default and can be disabled from the <strong>View Options</strong> dropdown in the Sequencer toolbar.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Image",
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

Holding the right mouse button and dragging along the timeline enables panning horizontally and vertically.

[Video: V_M3cV2W](https://dev.epicgames.com/community/api/cms/videos/V_M3cV2W/embed.html)

Scrolling will pan the timeline up and down, while holding **Shift** and scrolling the mouse wheel will pan the timeline left and right.

[Video: V_haUc7R](https://dev.epicgames.com/community/api/cms/videos/V_haUc7R/embed.html)

#### Zooming

You can zoom in the timeline by holding **CTRL** and scrolling the mouse wheel.

![horizontal scrolling](https://dev.epicgames.com/community/api/documentation/image/e6ece45e-f77e-4097-9e4f-7e2a96cdaaa7)

By holding **ALT** + **Shift** and clicking and dragging left and right with the Right Mouse Button, you can free-form zoom.

![horizontal scrolling](https://dev.epicgames.com/community/api/documentation/image/29332988-b823-4e4d-a8ef-b22892442013)

By holding **CTRL** and dragging along the time bar to the **right**, you can define a zoom region. Holding **CTRL** and dragging the time bar to the **left** resets the zoom back to full.

![horizontal scrolling](https://dev.epicgames.com/community/api/documentation/image/3e325ea9-2739-4dee-9b02-42fe87b74e8d)

The zoom pivot is relative to the playhead by default and can be changed by locating the **Zoom Position** preference in the **Level Sequence Editor** section of the **Editor Preferences**.

If your zoom and timeline framing have overextended, you can reset your zoom and timeline framing by pressing the **Home** key, which also resets the bounds of the range slider.

![home button horizontal zoom scrolling](https://dev.epicgames.com/community/api/documentation/image/c06b816b-8cbc-4c81-813f-90227526c025)

### Playhead

The playhead displays the current time in the sequence and is one of the main controls for timeline interactions. During playback it will move across the timeline at the specified playrate and can be stopped in place by pausing.

![sequencer playhead](https://dev.epicgames.com/community/api/documentation/image/4ea8f932-a876-42e4-9342-886dc180b02d)

You can **Left Mouse Button** (**LMB**)drag the playhead to change the current time in the sequence, and preview changes in the viewport. This is commonly referred to as "scrubbing". See [Scrubbing Responsiveness](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine#scrubbing-responsiveness) and [Synchronous Scrubbing](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine#synchronous-scrubbing) below for more information.

[Video: V_xePSCW](https://dev.epicgames.com/community/api/cms/videos/V_xePSCW/embed.html)

**Middle Mouse Button** (**MMB**) dragging causes the playhead to change to the selected position without causing the sequence to evaluate. This technique is used to change time, without changing property values and can be used to create same-value keyframes quickly. When manipulating the playhead in this way, it will change its color to **yellow**, to indicate the sequence is not evaluating.

[Video: V_DlO9bx](https://dev.epicgames.com/community/api/cms/videos/V_DlO9bx/embed.html)

The current time of the playhead is displayed and can be manipulated from the sequence outliner. You can press **CTRL + T** to focus selection to this field and type in a new time value.

![sequencer playhead values](https://dev.epicgames.com/community/api/documentation/image/5a6f89ae-ee15-48bc-b519-36d426911b28)

You can also right-click the playhead or anywhere on the time bar to reveal additional options.

![sequencer timeline playhead context menu](https://dev.epicgames.com/community/api/documentation/image/6faca2c9-d85e-4f0d-9cb3-8f985958716e)

| Name | Description | Hotkey |
| --- | --- | --- |
| **Set Start Time** | Set the start time of the sequence to the current position of your cursor. | **[** |
| **Set End Time** | Set the end time of the sequence to your cursor. | **]** |
| **Set Selection Start** | Set the start point of a custom timeline selection range to your cursor. | **i** |
| **Set Selection End** | Set the endpoint of a custom timeline selection range to your cursor. | **o** |
| **Clear Selection Range** | Remove the selected range. |   |
| **Add Mark** | Create a custom timeline mark at the current playhead time. | **m** |
| **Delete All Marks** | Remove all custom marks from the sequence. |   |
| **Locked** | When enabled, all marks will be locked, which prevents marks from being edited allowing you to scrub the timeline slider freely. |   |

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The Playhead time indicator can display with an <strong>asterisk</strong> (*) if the current time is on a sub-frame or in-between frame. This can happen if <a data-document-id=\"3231539\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine\">snapping</a> is disabled.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26395506,
      "caption": "",
      "alt_text": "sequencer sub frames asterisk",
      "image": {
        "id": 26395506,
        "file_name": "Asterix.png",
        "file_size": 29735,
        "content_type": "image/png",
        "created_at": "2026-01-19T20:14:32.687+00:00",
        "height": 260,
        "width": 791,
        "storage_key": "330ed548-b33d-439a-a39f-978652b414c7",
        "context": "documentation"
      },
      "storage_key": "330ed548-b33d-439a-a39f-978652b414c7",
      "context": "documentation",
      "width": null,
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

#### Scrubbing Responsiveness

Seeking a specific location and scrubbing along a track in Sequencer are both asynchronous non-blocking operations, whose responsiveness depends on the video codec used.

- **Apple Pro Res** provides the best scrubbing experience.
- **H.264/5** is effective, but shows a few frames of lag even when you enable hardware decoding.

#### Media Player Info

For convenience, Media Sections display media player and media file information directly in the Sequencer UI. This provides visual confirmation of the media player in use for playback.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Certain GOP codecs (H.264 in the screenshot below) might cause slow scrubbing performance; a yellow warning message is shown in such cases.",
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

![Codec warning message in Sequencer UI](https://dev.epicgames.com/community/api/documentation/image/bfaf05ac-00d9-48a6-a317-723f31921f62)

#### Synchronous Scrubbing

For use-cases where you need perfect frame alignment while scrubbing, for example when animating in Sequencer against reference video footage, you can enable the **Synchronous Scrubbing** Sequencer media track option. It aligns the video and animation frames exactly where the playhead is located, which ensures perfect alignment at some editor scrubbing responsiveness cost. This option is disabled by default to favor speed and responsiveness.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "This setting only affects scrubbing, it has no impact on playback which is always frame accurate.",
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

![Synchronous Scrubbing](https://dev.epicgames.com/community/api/documentation/image/181c1ed1-d593-47e5-a1b4-0e2aa8c9ac78)

### Selection Ranges

Selection ranges are custom regions you can define in a sequence to assist with timeline selection and playback.

To create a selection range, right- click a point in the timeline bar and set a **Start** and **End Selection Range**.

![sequencer selection range start end](https://dev.epicgames.com/community/api/documentation/image/92a430cf-7659-48d2-9862-857cb3ed37b7)

The selection range handles can be adjusted similarly to the start and end times of the sequence.

![sequencer selection range manipulation](https://dev.epicgames.com/community/api/documentation/image/3892428b-6c0f-4bb0-81fe-a16496fc73ee)

You can also set the playback of the sequence to loop within the section range.

[Video: V_r1E6JA](https://dev.epicgames.com/community/api/cms/videos/V_r1E6JA/embed.html)

Selection ranges can also be used to select keyframes and sections within them by clicking the **Actions** toolbar button and selecting **Select Keys in Selection Range** or **Select Sections in Selection Range**.

![sequencer selection range settings](https://dev.epicgames.com/community/api/documentation/image/93080a2a-9489-419c-bd41-bf80372818ac)

To remove a selection range, right-click the time bar and select **Clear Selection Range**.

### Custom Frame Marks

Custom frame marks are points you can add to call attention to areas or provide annotation for your sequence.

To create a mark, right-click a point in the timeline bar and select **Add Mark**.

![sequencer add mark option](https://dev.epicgames.com/community/api/documentation/image/8370360f-07c1-411d-b3ee-b47c81eec64c)

Frame Marks can be selected and multi-selected in the Sequencer Timeline in order to edit their location.

[Video: V_r5tY72](https://dev.epicgames.com/community/api/cms/videos/V_r5tY72/embed.html)

To edit a mark, right-click the mark flag in the Sequencer Timeline to access its context menu. Here you can customize its properties such as **Frame Number, Label,** and **Color**.

![sequencer mark properties](https://dev.epicgames.com/community/api/documentation/image/0c8dc224-a6e6-4a3b-bd6d-723c0a7aa54b)

Use these properties to observe and set Custom Frame Mark behavior when creating cinematics in the Sequencer Editor:

| Property | Description |
| --- | --- |
| **Marked Frame** | Sets or reference the **frame number** the mark is located in your Level Sequence. |
| **Label** | Sets a name for the Custom Frame Mark. The value set will be visible in the Sequencer Timeline at the top of the Mark flag. |
| **Comment** | Adds comments associated with the custom mark. |
| **Color** | Sets a custom color for the Mark flag in the Sequencer Timeline. |
| **Is Determinism Fence?** | When enabled, the Mark is treated as a **Determinism Fence**, which ensures that all Sequencer Components are evaluated at the Mark's location in the Sequencer Timeline. Determinism Fences cannot be crossed with a single evaluation, and force the evaluation to be conducted in two separate parts, ensuring an accurate evaluation of all present Sequencer components. |
| **Add Mark** | Creates a new custom mark at the timecode your cursor is at. |
| **Delete Mark** | Deletes the currently selected mark. |
| **Delete All Marks** | Deletes all custom marks within the level sequence asset. |

## Playback Controls

The playback controls can be found in the bottom-left corner of Sequencer and function similarly to standard media playback applications.

Buttons for toggling playing, pausing, and other playback-related functions are found here.

![sequencer add mark option](https://dev.epicgames.com/community/api/documentation/image/3926b3db-f6b6-4245-8784-32c6b74e409b)

| Icon | Description |
| --- | --- |
| ![sequencer record button take recorder](https://dev.epicgames.com/community/api/documentation/image/cc94a050-e237-4998-9d39-1694ec05e5e8) | Records the motion of a selected actor in the Sequencer Outliner, using **Take Recorder**. |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/3bb153c8-ed46-4fd7-9815-57305b61d04a) | Sets the start time of the sequence to the current location of the playhead. |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/6e7afc35-7521-4196-b982-b2c6e4a74d07) | Jumps to the start of the sequence. |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/978d84c3-fd2f-4772-a96c-f316508665cb) | Jumps to the previous keyframe in the selected track. |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/bc026067-a2da-4ed5-a837-5424527a22ea) | Jumps to the previous frame. |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/bba7777e-e832-446a-b803-86f45bb23e50) | Plays or pauses the sequence in reverse from the current position of the playhead. |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/14cb2dff-62a1-4075-a619-9632f8b6add7) | Plays or pauses the sequence from the position of the playhead. |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/c6f917ac-0bca-431c-aed7-44e9feeea47b) | Jumps to the next frame. |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/addb5590-e488-475f-bbb9-e96c590436cd) | Jumps to the next keyframe in the selected track. |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/feaef4ee-ccf5-4cf9-9cc3-5015cc2669fb) | Jumps to the end of the sequence. |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/5402563c-d45d-4cc9-bb0a-7896695dcf1f) | Sets the end time of the sequence to the current location of the playhead. |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/47872e36-ea6b-4806-af82-0139903e80f5) | Toggles between looping and no looping. Selection range looping is added if selection ranges are being used in the timeline. |

### Playback and Looping

Playback and looping performance are the most important functions of video playback. However, the Sequencer timeline makes a wide variety of Media Track section configurations possible, including native, cropped, extended, extended and cropped, with or without pre-roll and post-roll. These create edge-cases which cause problems for looping. The examples below are the currently-supported use cases for looping.

#### Baseline Looping

Baseline looping applies for use cases where:

- The Media Section length is unaltered, that is, it corresponds to the duration of the video clip.
- The Sequencer playback range fits within the Media Section pre-roll and post-roll bounds.

![Sequencer baseline looping](https://dev.epicgames.com/community/api/documentation/image/bb70062e-aced-401d-ab02-70f832e369ea)

In this configuration, the video clip is at full length and located at T=0, which prevents using the pre-roll section. Since the red and green crop lines are located at clip edges, the Media Section implementation keeps the Player alive and can perform proper seamless looping when the playhead reaches the end of the Sequencer’s playback range.

To prevent user error and because it is difficult to precisely set the red crop line in Sequencer, we recommend you use special care in placing the red line or to use the Media Section post-roll feature to prevent the Player unallocating prematurely.

#### Internal Clipped Looping

Internal clipped looping applies for use cases where you have done either of the following:

- Cropped a video in Sequencer by moving the green and red crop lines within the Media Section. For example, placing the green line at frame 100 and red line at frame 700 while the Media Section has 1000 Frames.
- Manually cropped the Media Section by adjusting its start and end points inside the video clip’s duration. For example, starting at frame 100 and ending at frame 700 if the Media Section had 1000 frames to begin with.

![Sequencer internal clipped looping](https://dev.epicgames.com/community/api/documentation/image/ec8c56bc-41fd-446f-be9a-b1773469e152)

This use case is fully supported because the media player is properly notified of those new start and end frames, and can cache the correct frames accordingly.
