# Cinematic Shortcuts and Tips

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine

> Application Version: 5.7

To improve your cinematic animation productivity, several shortcuts have been built into the Sequencer Editor. This document provides tips for common workflows, overcoming problems, and other helpful features of Sequencer.

## Playback

### Spacebar Playback Toggle

By default, using the **Space Bar** as a hotkey to toggle playback of your sequence only works if your window focus is on Sequencer. If your focus is on the Viewport, then pressing the Space Bar will instead cycle between transform manipulation modes.

You can make the Space Bar toggle playback of Sequencer regardless of window focus by following these steps:

### Inclusive and Exclusive Frames

Animation within Unreal Engine uses the concepts of "inclusive" and "exclusive" frames, which determine if a full frame is being included or evaluated fully. Typically this matters when defining **start** and **end frames** in your sequence, such as for [animations](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-animation-track-in-unreal-engine), [shots](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequences-shots-and-takes-in-unreal-engine), or overall Sequencer playback times.

For Sequencer, the start frame is inclusive and the end frame is exclusive, which causes all frame data up to the end frame to be evaluated. In this example, where the start time is set to **0**, and the end time is set to **10**, this means that the actual elapsed time is **9.999** (repeating) frames. In other words, it evaluates up to, but not completely to, the end time. This mimics behavior seen in most non-linear editing software such as Adobe Premiere.

![sequencer exclusive frame](https://dev.epicgames.com/community/api/documentation/image/523967be-ebd1-441d-8404-0921f20c7e20)

Because of this functionality, you can expect the following behavior:

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Sequencer's treatment of inclusive and exclusive frames differs from <a data-document-id=\"3230904\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine\">Animation Sequences</a>, which includes both start and end frames. When an animation FBX is imported, Unreal Engine will include a small amount of data beyond the final frame, which causes the final frame to be fully included. This can be observed in Sequencer if you zoom in far enough on the end of an unedited Animation Section.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24618978,
      "caption": "",
      "alt_text": "animation sequence inclusive",
      "image": {
        "id": 24618978,
        "file_name": "Exclusive5.gif",
        "file_size": 39915,
        "content_type": "image/gif",
        "created_at": "2025-05-19T21:48:56.878+00:00",
        "height": 100,
        "width": 350,
        "storage_key": "e0114b06-0869-4f46-85a7-39856743dfd4",
        "context": "documentation"
      },
      "storage_key": "e0114b06-0869-4f46-85a7-39856743dfd4",
      "context": "documentation",
      "width": null,
      "autoplay": true,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "However, trimming, and other <a data-document-id=\"3231687\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine\">section editing</a> operations on the animation will restore Sequencer's end frame exclusive behavior.",
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

## Workflow Shortcuts

### Middle-Mouse Scrubbing

Similar to Autodesk Maya, you can change your current time without causing updates or evaluations to occur by clicking and dragging the **middle mouse button** in the timeline. This can be useful when you want to set additional bracketing keyframes at the same value but at different times. When manipulating the playhead in this way, it will change its color to **yellow** to indicate the sequence is not evaluating.

![middle mouse scrub](https://dev.epicgames.com/community/api/documentation/image/2e24f221-7fc1-40d6-8198-1e1b7c455a60)

### Adding Actors to Sequencer

When dragging new Actors into your Level from the [Content Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-in-unreal-engine) or by [placing Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine), pressing certain keys will also add them to Sequencer. Depending on the pressed key, it will add the Actor as either a [spawnable or possessable](https://dev.epicgames.com/documentation/en-us/unreal-engine/spawn-temporary-actors-in-unreal-engine-cinematics?application_version=5.5).

- Holding **Ctrl** will add the new actor to Sequencer as a possessable.
- Holding **Shift** will add the new actor to Sequencer as a spawnable.

[Video: V_gUPipF](https://dev.epicgames.com/community/api/cms/videos/V_gUPipF/embed.html)

### Default Tracks

```json
{
  "type": "include",
  "excerpt_id": 1038,
  "excerpt_assignment_id": 1131,
  "blocks": [
    {
      "type": "paragraph",
      "content": "When adding certain Actors to Sequencer, you may notice that tracks are automatically created with them. For example:",
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
            "content": "<strong><a data-document-id=\"3223007\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/static-mesh-actors-in-unreal-engine\">Static Mesh Actors</a></strong> will automatically create a <a data-document-id=\"3231642\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine\">Transform Track</a>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24618962,
            "caption": "",
            "alt_text": "static mesh sequencer auto track",
            "image": {
              "id": 24618962,
              "file_name": "StaticMesh.png",
              "file_size": 2815,
              "content_type": "image/png",
              "created_at": "2025-05-19T21:48:54.104+00:00",
              "height": 51,
              "width": 329,
              "storage_key": "69c97169-46c3-4757-a6b3-822743a5d0d0",
              "context": "documentation"
            },
            "storage_key": "69c97169-46c3-4757-a6b3-822743a5d0d0",
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
            "content": "<strong><a data-document-id=\"3223048\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-actors-in-unreal-engine\">Skeletal Mesh Actors</a></strong> will automatically create a <a data-document-id=\"3231642\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine\">Transform Track</a> and an <strong><a data-document-id=\"3231546\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-animation-track-in-unreal-engine\">Animation Track</a></strong>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24618963,
            "caption": "",
            "alt_text": "skeletal mesh sequencer auto track",
            "image": {
              "id": 24618963,
              "file_name": "SkellyMesh.png",
              "file_size": 3236,
              "content_type": "image/png",
              "created_at": "2025-05-19T21:48:54.183+00:00",
              "height": 74,
              "width": 329,
              "storage_key": "9d4be243-1dca-49ca-8320-16a2a89cdf7a",
              "context": "documentation"
            },
            "storage_key": "9d4be243-1dca-49ca-8320-16a2a89cdf7a",
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
            "content": "<strong><a data-document-id=\"3231737\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine\">Cine Camera Actors</a></strong> will automatically create a <a data-document-id=\"3231642\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine\">Transform Track</a> and a <strong>Camera Component</strong> with <strong>Aperture</strong>, <strong>Focal Length</strong>, and <strong>Focus Distance</strong> property tracks.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24618964,
            "caption": "",
            "alt_text": "camera actor sequencer auto track",
            "image": {
              "id": 24618964,
              "file_name": "CineCamera.png",
              "file_size": 8387,
              "content_type": "image/png",
              "created_at": "2025-05-19T21:48:54.265+00:00",
              "height": 148,
              "width": 329,
              "storage_key": "37fd134c-4036-4150-841e-0d2931ac62e7",
              "context": "documentation"
            },
            "storage_key": "37fd134c-4036-4150-841e-0d2931ac62e7",
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
            "content": "<strong><a data-document-id=\"3224971\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine\">Light Actors</a></strong> will automatically create a <strong>Light Component</strong> with <strong>Intensity </strong>and <strong>Light Color</strong> property tracks.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24618965,
            "caption": "",
            "alt_text": "lights sequencer auto track",
            "image": {
              "id": 24618965,
              "file_name": "Light.png",
              "file_size": 5354,
              "content_type": "image/png",
              "created_at": "2025-05-19T21:48:54.359+00:00",
              "height": 102,
              "width": 329,
              "storage_key": "acafaeac-584a-4556-a389-a4755c53961e",
              "context": "documentation"
            },
            "storage_key": "acafaeac-584a-4556-a389-a4755c53961e",
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
      "content": "This occurs because of the <strong>Tracks Settings</strong> located in the <a data-document-id=\"3231690\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-editor-and-project-settings-in-unreal-engine\">Sequencer Plugins Project Settings</a>. You can locate these settings by opening the <strong>Project Settings</strong> window, and locating <strong>Level Sequencer</strong> in the <strong>Plugins </strong>category.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24618966,
      "caption": "",
      "alt_text": "sequencer track settings",
      "image": {
        "id": 24618966,
        "file_name": "ProjectSettings.png",
        "file_size": 80689,
        "content_type": "image/png",
        "created_at": "2025-05-19T21:48:54.441+00:00",
        "height": 358,
        "width": 1109,
        "storage_key": "494d01a5-5dce-426b-97ca-6b57155311b4",
        "context": "documentation"
      },
      "storage_key": "494d01a5-5dce-426b-97ca-6b57155311b4",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <strong>Track Settings</strong> array is populated by default with settings for the previously mentioned tracks. You can click the <strong>Add (+)</strong> button to add a new array item, and each array has the following categories:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24618967,
      "caption": "",
      "alt_text": "add track setting",
      "image": {
        "id": 24618967,
        "file_name": "TrackSettingsAdd.png",
        "file_size": 23031,
        "content_type": "image/png",
        "created_at": "2025-05-19T21:48:54.575+00:00",
        "height": 354,
        "width": 473,
        "storage_key": "cd60bb81-c9a4-4c3b-b5f4-0402065a99e9",
        "context": "documentation"
      },
      "storage_key": "cd60bb81-c9a4-4c3b-b5f4-0402065a99e9",
      "context": "documentation",
      "width": null,
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
              "content": "Name",
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
              "content": "<strong>Matching Actor Class</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This is where you specify the Actor class to automatically create tracks for when adding it to Sequencer.",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 24618968,
              "caption": "",
              "alt_text": "matching actor class",
              "image": {
                "id": 24618968,
                "file_name": "MatchingClass.png",
                "file_size": 3298,
                "content_type": "image/png",
                "created_at": "2025-05-19T21:48:54.668+00:00",
                "height": 28,
                "width": 379,
                "storage_key": "eefa2b71-4383-43f1-904e-aa6fe1c0f204",
                "context": "documentation"
              },
              "storage_key": "eefa2b71-4383-43f1-904e-aa6fe1c0f204",
              "context": "documentation",
              "width": null,
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
              "content": "<strong>Default Tracks</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This array is where you specify the tracks that are added when the <strong>Matching Actor Class</strong> is added to Sequencer. Click the <strong>Add (+)</strong> button and click the dropdown menu to browse <strong>Sequencer's</strong> track types.",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 24618969,
              "caption": "",
              "alt_text": "default tracks",
              "image": {
                "id": 24618969,
                "file_name": "DefaultTracks.png",
                "file_size": 7946,
                "content_type": "image/png",
                "created_at": "2025-05-19T21:48:54.721+00:00",
                "height": 93,
                "width": 432,
                "storage_key": "3e2eef31-19db-46d4-b824-9b4858f07b5a",
                "context": "documentation"
              },
              "storage_key": "3e2eef31-19db-46d4-b824-9b4858f07b5a",
              "context": "documentation",
              "width": null,
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
              "content": "<strong>Exclude Default Tracks</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This array is where you specify tracks you don't want added for this Actor class. You may want to use this if you are specifying different tracks to add, such as when your class is inheriting from a parent class which also has its default tracks specified here.",
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
              "content": "<strong>Default Property Tracks</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This array is where you specify the property tracks that are added when the Actor is added to Sequencer. Click the <strong>Add (+)</strong> button to add a new property item to the array.",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 24618970,
              "caption": "",
              "alt_text": "default property tracks",
              "image": {
                "id": 24618970,
                "file_name": "PropertyTracks.png",
                "file_size": 8985,
                "content_type": "image/png",
                "created_at": "2025-05-19T21:48:54.820+00:00",
                "height": 178,
                "width": 327,
                "storage_key": "6ab5f728-a5c1-47eb-b4dc-ec7dd0b74753",
                "context": "documentation"
              },
              "storage_key": "6ab5f728-a5c1-47eb-b4dc-ec7dd0b74753",
              "context": "documentation",
              "width": null,
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
                    "content": "<strong>Component Path</strong> is where you specify the Actor's component you want to add the property from.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<strong>Property Path</strong> is where you specify the property name you want to automatically add.",
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
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Exclude Default Property Tracks</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This array is where you specify property tracks you don't want added for this Actor class. You may want to use this if you are specifying different tracks to add, such as when your class is inheriting from a parent class which also has its default property tracks specified here.",
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
  "excerpt_hash_id": "6vG",
  "settings": {
    "is_hidden": false
  }
}
```

### Auto Size Shots

When adjusting start and end times of shots internally, you can automatically match the parent shot section to these edits using the **Auto Size** command. To do this, right-click the shot and select **Edit > Auto Size**. This can be useful if you are retiming your shot and want the shot section to match, without needing to re-trim manually.

[Video: V_3R83oM](https://dev.epicgames.com/community/api/cms/videos/V_3R83oM/embed.html)

### Shift Snapping and Alignment

When dragging section assets onto Sequencer tracks, such as [audio](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-audio-track-in-unreal-engine), [subsequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-subscequences-track-in-unreal-engine), or [animation](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-animation-track-in-unreal-engine) tracks, holding **Shift** will snap the dropped section to the Playhead location.

![shift dragging](https://dev.epicgames.com/community/api/documentation/image/cbd8f241-7c96-43d0-a0f7-b5b1010dada4)

If **Snap to the Pressed Key** is disabled, you can still align the Playhead to keyframes by holding **Shift** and clicking the keyframe. This makes it easy to perform subsequent actions, such as changing the value of this keyframe, or aligning other keys to it.

![shift alignment](https://dev.epicgames.com/community/api/documentation/image/32723209-ff2a-4509-83d7-9f050696a179)

## Workflow Tips

### Ultrawide Monitor Framing

When making cinematics with unconstrained aspect ratios, you may encounter situations where your shot composition can change if a monitor's aspect ratio differs greatly from the aspect ratio you originally intended. For example, if you created the following shot in a cinematic:

![Image](https://dev.epicgames.com/community/api/documentation/image/0a50dff9-299b-46e0-8c8d-d9ea4cb8b233)

Then, if this shot was played on an ultrawide monitor, the drastic change in aspect ratio may severely disrupt the original framing.

![Image](https://dev.epicgames.com/community/api/documentation/image/6c6ff67b-22fe-40f3-804a-2e6552230371)

In this situation, where maintaining the vertical framing is important, you can resolve this by navigating to the **Level Sequence Actor's Details** and do the following:

- Enable **Override Aspect Ratio Axis Constraint**.
- Set **Aspect Ratio Axis Constraint** to **Maintain Y-Axis FOV**.

![Image](https://dev.epicgames.com/community/api/documentation/image/a7a3efcd-9c9f-40d7-97bf-9e8a30384787)

Once done, your vertical frame-space is constrained, maintaining the framing on these characters no matter the aspect ratio.

![Image](https://dev.epicgames.com/community/api/documentation/image/1e2551fe-f561-4f00-8205-9c7660c3f348)

## Warm-Up Rendering

When creating pre-rendered sequences with [Movie Render Queue](animating-characters-and-objects/Sequencer/movie-render-pipeline#movierenderqueue) (MRQ), it may be necessary to "warm up" each shot in order for various aspects of your scene to render correctly. For example, some common problems can be:

- Particles and other effects activating at the start of the shot, instead of already being active.
- Cloth and other physics-driven entities exhibit a noticeable "settle" at the start of the shot.
- The first rendered frame of a shot can exhibit noticeable aliasing or other temporal artifacts (sparkles).

You can use various warm-up properties within Movie Render Queue's [Anti-Aliasing Render Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine) to resolve these scenarios. Depending on the scenario, there may also be different considerations to take into account that will determine which settings are best to use.

### Particles

In some cases, you may want particles and other effects to be active for a certain duration of time before a shot begins. While real-time previewing might show the correct behavior, rendering with MRQ may cause your particle system to activate at the start of the shot, which is undesirable.

|   |   |
| --- | --- |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/f59c1506-3688-4a5d-bf62-bd7795837d7a) | ![Image](https://dev.epicgames.com/community/api/documentation/image/fce10c79-135b-493d-a6f9-ddb5518685dc) |
| Particle with no warm-up | Particle with warm-up |

For this particle scenario, you can resolve it in either of the following ways:

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If your particle is <strong>GPU-based</strong>, then you will also need to enable <strong>Render Warm Up Frames</strong>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24618988,
      "caption": "",
      "alt_text": "render warm up frames",
      "image": {
        "id": 24618988,
        "file_name": "WarmupParticle3.png",
        "file_size": 24886,
        "content_type": "image/png",
        "created_at": "2025-05-19T21:48:59.305+00:00",
        "height": 342,
        "width": 501,
        "storage_key": "e5891dab-d171-43df-ad85-1eb553e6647f",
        "context": "documentation"
      },
      "storage_key": "e5891dab-d171-43df-ad85-1eb553e6647f",
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

### Cloth and Physics

For cloth and other physics objects, a common problem when rendering is that they can exhibit a noticeable settle at the start of a shot. This is due to the game simulation not starting until the rendering begins, therefore physics needs time to settle to its true simulated state.

|   |   |
| --- | --- |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/8c12181d-c270-4e05-9953-14f44593423e) | ![Image](https://dev.epicgames.com/community/api/documentation/image/d3fbb4fa-1435-45ff-a731-17816308c2fd) |
| Cloth settles at start (no warm-up) | No cloth settling (with warm-up) |

#### No Starting Motion

For shots where the character or physics object is not initially moving, such as being in an idle pose, you can fix this by setting a frame value on **Engine Warm Up Count**. This value can be arbitrary depending on how many frames are needed for your physics to settle. Typically, a value greater than 30 should be used.

![engine warm up count](https://dev.epicgames.com/community/api/documentation/image/46a22cff-5951-447c-b73b-49789190eb8a)

#### Starting Motion

In scenarios where shots start with the physics object in motion, such as running or jumping, then **Engine Warm Up Count** will not produce an accurate result. This is because it only "warms up" the starting frame and does not take into account motion that may be occurring beforehand. Here you can observe the cloth in the left example starting at an unnatural rest position, then correcting as the simulation reacts to the motion.

|   |   |
| --- | --- |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/b5f405a8-96a5-49cf-bfe5-f3adac8cefe5) | ![Image](https://dev.epicgames.com/community/api/documentation/image/80b54f38-7c6d-4f00-ba57-e1949b31aa26) |
| Cloth starts at rest (incorrect warm-up settings) | Cloth starts correctly behind (using correct warm-up settings) |

In order to resolve this, you must do the following:

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "This technique can be used to also build a movement history for other things, such as trail particles.",
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

### Temporal Artifacts

Aliasing and other artifacts caused by rendering features that have a temporal component, such as Temporal Anti Aliasing (TAA), Temporal Super Resolution (TSR), or raytracing denoisers, can also occur on the first few frames of your shots. Typically, this issue appears as noticeable hard edges or grainy sparkling on reflective surfaces. This is due to the lack of temporal history being accumulated at the start of a render.

|   |   |
| --- | --- |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/3cb4d108-1ae0-45a1-888f-1146dc3efef4) | ![Image](https://dev.epicgames.com/community/api/documentation/image/dc25c96b-5897-4d70-8259-ebca1135a4ae) |
| Sparkling and jagged edges (no warm-up) | Smooth edges and highlights (with warm-up) |

To resolve this issue, you can do either of the following:
