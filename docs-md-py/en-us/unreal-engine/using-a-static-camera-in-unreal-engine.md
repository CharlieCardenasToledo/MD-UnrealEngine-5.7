# Using a Static Camera

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-a-static-camera-in-unreal-engine

> Application Version: 5.7

In this How-to tutorial you will create a static (or fixed) camera angle that is used for the player's perspective during gameplay in a third person example map, and then you will create a trigger volume which will transition your viewpoint to the new static camera once your character overlaps the volume. Upon completing this tutorial, you can take the process used here and apply it to your own game to set up a fixed perspective for a player.

## Creating The Static Camera Actor

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1542,
        "excerpt_assignment_id": 1333,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Begin by creating a <strong>New &gt; Games &gt; Third Person &gt; Blueprint</strong> project named <strong>StaticCameras</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Click <strong>Add/Import &gt; Blueprints &gt; Blueprint Class</strong>, the <strong>Pick Parent Class</strong> menu will appear. Click the arrow to expand all classes, then search for and select <strong>CameraActor</strong> to create a new Blueprint CameraActor class named <strong>BP_ExampleCameraActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711484,
                  "caption": "",
                  "alt_text": "pick-parent-class-menu-select-camera-actor",
                  "image": {
                    "id": 25711484,
                    "file_name": "CreateBPCameraActor.png",
                    "file_size": 53264,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:53.324+00:00",
                    "height": 597,
                    "width": 626,
                    "storage_key": "8adbb73d-3ae2-4d13-8e9a-ec215e5563b2",
                    "context": "documentation"
                  },
                  "storage_key": "8adbb73d-3ae2-4d13-8e9a-ec215e5563b2",
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
                  "content": "From the <strong>Content Browser</strong> panel, select and drag the <strong>BP_ExampleCameraActor</strong> into the Level.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711485,
                  "caption": "",
                  "alt_text": "drag-camera-actor-into-level",
                  "image": {
                    "id": 25711485,
                    "file_name": "DragBPCameraActor.png",
                    "file_size": 342536,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:53.504+00:00",
                    "height": 595,
                    "width": 750,
                    "storage_key": "37d9a3a8-4e81-48d0-a31c-8be071fcf177",
                    "context": "documentation"
                  },
                  "storage_key": "37d9a3a8-4e81-48d0-a31c-8be071fcf177",
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
        "excerpt_hash_id": "BJ2",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1543,
        "excerpt_assignment_id": 1334,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Begin by creating a <strong>New &gt; Games &gt; Third Person &gt; C++</strong> project named <strong>StaticCameras</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Launch the <strong>C++ Class Wizard</strong>, enable the checkbox for <strong>Show All Classes</strong>, then type <strong>CameraActor</strong> within the search field to select and create your new <strong>Camera Actor</strong> class named <strong>ExampleCameraActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711486,
                  "caption": "",
                  "alt_text": "New C++ Camera Actor class",
                  "image": {
                    "id": 25711486,
                    "file_name": "CreateCppCameraActor.png",
                    "file_size": 33192,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:53.794+00:00",
                    "height": 580,
                    "width": 946,
                    "storage_key": "fd83b67a-a0c9-42b5-8059-ee8a02d8ebf9",
                    "context": "documentation"
                  },
                  "storage_key": "fd83b67a-a0c9-42b5-8059-ee8a02d8ebf9",
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
                  "content": "From the <strong>C++ Class</strong> panel, right click on your <strong>ExampleCamera</strong> and from the dropdown <strong>C++ Class</strong> actions menu select <strong>Create a Blueprint class based on ExampleCameraActor</strong>. Then drag an instance of <strong>BP_ExampleCameraActor</strong> into the level.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711487,
                  "caption": "Click image to expand.",
                  "alt_text": "Place Actor in level",
                  "image": {
                    "id": 25711487,
                    "file_name": "DragCameraActor.png",
                    "file_size": 377993,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:53.910+00:00",
                    "height": 620,
                    "width": 750,
                    "storage_key": "41cb576c-8114-408e-9a5a-359c4ff9dd80",
                    "context": "documentation"
                  },
                  "storage_key": "41cb576c-8114-408e-9a5a-359c4ff9dd80",
                  "context": "documentation",
                  "width": 650,
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
        "excerpt_hash_id": "vg6",
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

## Level Setup

In order to demonstrate the transition of perspectives between the player's camera and the static camera Actor, you will need to set up the scene. You can accomplish this by modifying some of the static mesh geometry from the third person template level.

1. Begin by navigating to the world outliner panel, and shift select the **Floor** and the four **Wall** Static Mesh Actors from the **ArenaGeometry > Arena** folder. ![selecting-floors-and-walls-in-the-world-outliner](https://dev.epicgames.com/community/api/documentation/image/0ecebac2-5c25-46e9-b88c-fc6d87a6e6dd)
2. **Alt-click** and drag the **Transform** gizmo to create a duplicate floor and wall setup. [Video: 1_2968boqo](https://dev.epicgames.com/community/api/cms/videos/1_2968boqo/embed.html)
3. This will result in the creation of a second **Floor**, and four additional **Wall** Static Mesh Actors. ![Duplicated walls and floors](https://dev.epicgames.com/community/api/documentation/image/ce5fa026-0299-4984-a901-d1b54d9d88f4)
4. Move the newly duplicated static meshes to resemble the layout below, a new room duplicating the first but without any contents. ![Overhead view of new room](https://dev.epicgames.com/community/api/documentation/image/1f752c52-ec8e-49d3-a01b-93e7a8251cd2)
5. From the world outliner, select the two walls that connect the two rooms, and set their **X Scale** values to 14. ![x-scale-value-in-details-panel](https://dev.epicgames.com/community/api/documentation/image/c66e7f67-687f-45a0-90ec-2d1dde3c5428)
6. Select both the connecting walls, then move them using the **Transform** gizmo so that they form a partition between rooms with a gap as shown in the gif below. [Video: 1_a9alwyt9](https://dev.epicgames.com/community/api/cms/videos/1_a9alwyt9/embed.html)
7. Your completed level setup should look similar to the image below, with a second room connected to the first by an opening in the wall. ![Connected rooms](https://dev.epicgames.com/community/api/documentation/image/722667bc-ee28-47e9-b846-ef1468cd1381)

## Camera Perspective Setup

Now that you have completed the level setup, you can place the **BP\_ExampleCameraActor** in the level to get a better idea of the view the player will have once they overlap the trigger volume. You can take a First Person perspective from the Camera's Point of View by locking the **Viewport** to the Camera Actor and entering **Pilot** mode.

1. With the Camera selected in the level, right-click on it, then from the context menu select **Pilot CameraActor**. ![Context menu Pilot CameraActor](https://dev.epicgames.com/community/api/documentation/image/d726af6d-e9d8-4d47-a3d5-e6e98796a186)
2. You can now move around the Viewport using the **WASD** keys while holding the **Left** or **Right Mouse Button** down. While you fly around the level, the Camera's position will move along with your movement allowing you to get an idea of the perspective the camera will take during gameplay.
3. To unlock the Camera, click the **Unlock** button. ![Unlock button](https://dev.epicgames.com/community/api/documentation/image/1c93c882-69f1-4ef9-a5a5-8ae509ddd0e0) The camera will remain where it was positioned when you unlocked it. The icon next to the Unlock button allows you to toggle between showing the in-game camera view or the level editor view.
4. Pilot the Camera into a position looking down on the second room similar to the gif below. [Video: 1_h27hh09q](https://dev.epicgames.com/community/api/cms/videos/1_h27hh09q/embed.html)
5. Your completed camera scene setup should look similar to the image below, with a static camera looking down on the new room along with the original camera following the third-person actor. ![Completed Camera setup](https://dev.epicgames.com/community/api/documentation/image/379516ab-9569-4edc-8f6e-d84afd290289)

## Creating the Overlap Trigger Actor

In this example, the trigger Actor functions as the transition manager between the player's camera view point and the static camera view point, once the player overlaps its box component volume bounds, a transitional blend will occur between the perspectives.

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1544,
        "excerpt_assignment_id": 1335,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Begin by clicking <strong>Add/Import &gt; Blueprints &gt; Blueprint Class</strong>, and create a new Blueprint Actor class named <strong>BP_BlendTriggerVolume</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Double click the BP_BlendTriggerVolume to open its class defaults. From the <strong>Components</strong> tab, click the <strong>Add Component</strong> button and select <strong>Box Collision</strong> to add a new <strong>Box Component</strong> named <strong>OverlapVolume</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711488,
                  "caption": "",
                  "alt_text": "Adding new Box Collision Component",
                  "image": {
                    "id": 25711488,
                    "file_name": "AddBoxCollision.png",
                    "file_size": 16499,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:54.241+00:00",
                    "height": 275,
                    "width": 254,
                    "storage_key": "5066a794-f12a-4ab7-b34d-0ce5263413b6",
                    "context": "documentation"
                  },
                  "storage_key": "5066a794-f12a-4ab7-b34d-0ce5263413b6",
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
                  "content": "From the <strong>My Blueprint</strong> tab, navigate to the variables category and click the <strong>Add (+)</strong> button. Select your new variable and, from the Details panel, change its Variable type to a float and name your variable CameraBlendTime.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711489,
                  "caption": "",
                  "alt_text": "CameraBlendTime variable",
                  "image": {
                    "id": 25711489,
                    "file_name": "AddCameraBlendTimeVariable.png",
                    "file_size": 20464,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:54.335+00:00",
                    "height": 331,
                    "width": 380,
                    "storage_key": "5f0f48f7-7cd9-4b03-8bc9-bb6615716cec",
                    "context": "documentation"
                  },
                  "storage_key": "5f0f48f7-7cd9-4b03-8bc9-bb6615716cec",
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
                  "content": "Compile and save your Blueprint.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711490,
                  "caption": "",
                  "alt_text": "Compile button",
                  "image": {
                    "id": 25711490,
                    "file_name": "CompileBP.png",
                    "file_size": 11932,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:54.439+00:00",
                    "height": 100,
                    "width": 380,
                    "storage_key": "37216f64-6e74-4d10-afff-797c1c328948",
                    "context": "documentation"
                  },
                  "storage_key": "37216f64-6e74-4d10-afff-797c1c328948",
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
                  "content": "Re-select your CameraBlendTime variable and set its float value to 1.0f.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711491,
                  "caption": "",
                  "alt_text": "Set variable float value",
                  "image": {
                    "id": 25711491,
                    "file_name": "SettingCameraBlendTime.png",
                    "file_size": 33764,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:54.535+00:00",
                    "height": 531,
                    "width": 380,
                    "storage_key": "b369b7b7-fd12-425d-b084-9b002d5ca957",
                    "context": "documentation"
                  },
                  "storage_key": "b369b7b7-fd12-425d-b084-9b002d5ca957",
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
            "type": "header",
            "content": "Creating the On Component Begin Overlap Event",
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
                  "content": "From the <strong>Components</strong> tab, select the <strong>OverlapVolume</strong>, navigate to the <strong>Details</strong> panel, scroll down to the <strong>Events</strong> category and click the <strong>Add (+)</strong> button next to the <strong>On Component Begin Overlap</strong> event.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711492,
                  "caption": "",
                  "alt_text": "Select On Component Begin Overlap Event",
                  "image": {
                    "id": 25711492,
                    "file_name": "AddOnComponBeginOverlap.png",
                    "file_size": 24917,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:54.661+00:00",
                    "height": 520,
                    "width": 380,
                    "storage_key": "095bffdd-380a-4d8a-b349-82590e290b40",
                    "context": "documentation"
                  },
                  "storage_key": "095bffdd-380a-4d8a-b349-82590e290b40",
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
                  "content": "Click the <strong>On Component Begin Overlap(OverlapVolume)</strong> node and drag off the execution pin onto the event graph, an <strong>Executable</strong> actions drop down menu will appear. Search for and select <strong>Cast To ThirdPersonCharacter</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711493,
                  "caption": "",
                  "alt_text": "Executable actions dropdown menu",
                  "image": {
                    "id": 25711493,
                    "file_name": "BPScript01.png",
                    "file_size": 44274,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:54.737+00:00",
                    "height": 199,
                    "width": 610,
                    "storage_key": "950bae74-0be9-4712-8ead-6ab49acf7a12",
                    "context": "documentation"
                  },
                  "storage_key": "950bae74-0be9-4712-8ead-6ab49acf7a12",
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
                  "content": "From the <strong>On Component Begin Overlap</strong> node, click and drag off of the <strong>Other Actor</strong> pin and input it into the <strong>Object</strong> pin of the <strong>Cast To Third PersonCharacter</strong> node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711494,
                  "caption": "",
                  "alt_text": "Drag off Other Actor pin",
                  "image": {
                    "id": 25711494,
                    "file_name": "BPScript02.png",
                    "file_size": 45868,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:54.818+00:00",
                    "height": 221,
                    "width": 610,
                    "storage_key": "ca96724f-ed09-43e7-88ac-34e628fdcb76",
                    "context": "documentation"
                  },
                  "storage_key": "ca96724f-ed09-43e7-88ac-34e628fdcb76",
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
                  "content": "From the <strong>Cast To ThirdPersonCharacter</strong> node, select and drag off the <strong>As Third Person Character</strong> reference pin and from the actions drop down menu, search for and select <strong>Is Valid</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711495,
                  "caption": "",
                  "alt_text": "Actions dropd down menu Is Valid",
                  "image": {
                    "id": 25711495,
                    "file_name": "BPScript03.png",
                    "file_size": 19751,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:54.907+00:00",
                    "height": 194,
                    "width": 380,
                    "storage_key": "b9c87a05-2e2e-4e2c-9555-b6a9e8e19236",
                    "context": "documentation"
                  },
                  "storage_key": "b9c87a05-2e2e-4e2c-9555-b6a9e8e19236",
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
                  "content": "Select and drag from the <strong>Is Valid</strong> node's boolean return value. From the actions menu, search for and select a <strong>Branch</strong> node, then connect the execution pin from the <strong>Cast to ThirdPersonCharacter</strong> node to the Branch node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711496,
                  "caption": "",
                  "alt_text": "Is Valid connect to Branch",
                  "image": {
                    "id": 25711496,
                    "file_name": "BPScript04.png",
                    "file_size": 41413,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:55.055+00:00",
                    "height": 180,
                    "width": 610,
                    "storage_key": "7f39f168-c5e5-4a47-8a22-4c65f833ae08",
                    "context": "documentation"
                  },
                  "storage_key": "7f39f168-c5e5-4a47-8a22-4c65f833ae08",
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
                  "content": "From the <strong>Branch</strong> node, click and drag off the <strong>True</strong> pin and, from the actions menu, search and select <strong>Cast to PlayerController</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711497,
                  "caption": "",
                  "alt_text": "Executable actions Cast to PlayerController",
                  "image": {
                    "id": 25711497,
                    "file_name": "BPScript05.png",
                    "file_size": 35365,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:55.185+00:00",
                    "height": 221,
                    "width": 520,
                    "storage_key": "b57cebd9-5338-44ac-89f9-fd97861be82b",
                    "context": "documentation"
                  },
                  "storage_key": "b57cebd9-5338-44ac-89f9-fd97861be82b",
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
                  "content": "From the <strong>Cast To ThirdPerson Character</strong> node, click and drag off the <strong>As Third Person Character</strong> pin and, from the actions menu, search for and select <strong>Get Controller</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711498,
                  "caption": "",
                  "alt_text": "Actions menu Get Controller",
                  "image": {
                    "id": 25711498,
                    "file_name": "BPScript06.png",
                    "file_size": 77673,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:55.259+00:00",
                    "height": 392,
                    "width": 610,
                    "storage_key": "0547b46f-9434-4f41-b02c-5ca2af38e9f5",
                    "context": "documentation"
                  },
                  "storage_key": "0547b46f-9434-4f41-b02c-5ca2af38e9f5",
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
                  "content": "From the <strong>Get Controller Node</strong>, click and drag off of the <strong>Return Value</strong> and connect it to the <strong>Object</strong> pin of your <strong>Cast To PlayerController</strong> node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711499,
                  "caption": "",
                  "alt_text": "Get Controller Return Value",
                  "image": {
                    "id": 25711499,
                    "file_name": "BPScript07.png",
                    "file_size": 83532,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:55.401+00:00",
                    "height": 235,
                    "width": 900,
                    "storage_key": "f9426b29-c2b4-43f6-882b-54cefcb34f69",
                    "context": "documentation"
                  },
                  "storage_key": "f9426b29-c2b4-43f6-882b-54cefcb34f69",
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
                  "content": "From the <strong>CastToPlayerController</strong> node, drag off the <strong>As Player Controller</strong> pin, and repeat the <strong>Is Valid</strong> and <strong>Branch</strong> check described in steps 4 and 5.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711500,
                  "caption": "",
                  "alt_text": "Repeat Is Valid and Branch",
                  "image": {
                    "id": 25711500,
                    "file_name": "BPScript08.png",
                    "file_size": 75586,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:55.527+00:00",
                    "height": 218,
                    "width": 900,
                    "storage_key": "64a8e3a4-83d4-48f5-a701-66c0a8387b3f",
                    "context": "documentation"
                  },
                  "storage_key": "64a8e3a4-83d4-48f5-a701-66c0a8387b3f",
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
                  "content": "Select and drag off the <strong>True</strong> pin of the <strong>Branch</strong> node onto the event graph and, from the actions menu, search for and select <strong>Get Actor Of Class</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711501,
                  "caption": "",
                  "alt_text": "Actions menu Get Actor Of Class",
                  "image": {
                    "id": 25711501,
                    "file_name": "BPScript09.png",
                    "file_size": 69884,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:55.673+00:00",
                    "height": 282,
                    "width": 900,
                    "storage_key": "6bdf6399-0d65-4451-89e1-748ff7c2e760",
                    "context": "documentation"
                  },
                  "storage_key": "6bdf6399-0d65-4451-89e1-748ff7c2e760",
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
                  "content": "From the <strong>Actor Class</strong> pin's <strong>Select Class</strong> drop-down menu, search for and select your <strong>BP_ExampleCameraActor</strong> class.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711502,
                  "caption": "",
                  "alt_text": "Select your Actor class",
                  "image": {
                    "id": 25711502,
                    "file_name": "BPScript10.png",
                    "file_size": 29504,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:55.775+00:00",
                    "height": 200,
                    "width": 490,
                    "storage_key": "2bb262cf-5595-4dc1-9473-4d67d27ffd63",
                    "context": "documentation"
                  },
                  "storage_key": "2bb262cf-5595-4dc1-9473-4d67d27ffd63",
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
                  "content": "Navigate to your <strong>Cast To PlayerController</strong> node, click and drag off the <strong>As Player Controller</strong> pin and, from the actions menu, search for and select <strong>Set View Target With Blend</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711503,
                  "caption": "",
                  "alt_text": "Actions menu Set View Target With Blend",
                  "image": {
                    "id": 25711503,
                    "file_name": "BPScript11.png",
                    "file_size": 47767,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:55.841+00:00",
                    "height": 305,
                    "width": 585,
                    "storage_key": "cdee9987-ddd6-43c4-bca3-89bca78f2f33",
                    "context": "documentation"
                  },
                  "storage_key": "cdee9987-ddd6-43c4-bca3-89bca78f2f33",
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
                  "content": "From the <strong>Get Actor of Class</strong> node, click and drag the return value pin and plug it into the <strong>New View Target</strong> input pin of the <strong>Set View Target</strong> node, then connect the execution pin.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711504,
                  "caption": "",
                  "alt_text": "Connect nodes",
                  "image": {
                    "id": 25711504,
                    "file_name": "BPScript12.png",
                    "file_size": 76901,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:55.923+00:00",
                    "height": 260,
                    "width": 1170,
                    "storage_key": "659578f6-591c-40c6-b43b-36beb40eb92a",
                    "context": "documentation"
                  },
                  "storage_key": "659578f6-591c-40c6-b43b-36beb40eb92a",
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
                  "content": "Navigate to the <strong>My Blueprint</strong> tab and, from the <strong>Variables</strong> categories, click and drag the <strong>CameraBlendTime</strong> float variable onto the event graph. Then, from the drop-down menu select <strong>Get CameraBlendTime</strong> to get a reference to your variable.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711505,
                  "caption": "",
                  "alt_text": "CameraBlendTime variable added to graph",
                  "image": {
                    "id": 25711505,
                    "file_name": "BPScript13.png",
                    "file_size": 62196,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:56.048+00:00",
                    "height": 335,
                    "width": 585,
                    "storage_key": "9b254357-89b3-40a1-8965-706c8ca399a6",
                    "context": "documentation"
                  },
                  "storage_key": "9b254357-89b3-40a1-8965-706c8ca399a6",
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
                  "content": "Connect your <strong>Camera Blend Time</strong> variable pin into the <strong>Blend Time</strong> pin from the <strong>Set View Target</strong> node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711506,
                  "caption": "",
                  "alt_text": "Connect nodes",
                  "image": {
                    "id": 25711506,
                    "file_name": "BPScript14.png",
                    "file_size": 68674,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:56.154+00:00",
                    "height": 269,
                    "width": 585,
                    "storage_key": "45efefbd-fa49-48b4-b80d-12d8c54923c9",
                    "context": "documentation"
                  },
                  "storage_key": "45efefbd-fa49-48b4-b80d-12d8c54923c9",
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
                  "content": "Your VolumeTrigger On Component Begin Overlap logic should look as shown in the image below.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711507,
                  "caption": "Click image to expand.",
                  "alt_text": "full-volumetrigger-on-component-begin-overlap-logic",
                  "image": {
                    "id": 25711507,
                    "file_name": "BPScript15.png",
                    "file_size": 159963,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:56.273+00:00",
                    "height": 235,
                    "width": 1820,
                    "storage_key": "3a7bff9d-7218-4bee-b034-7e5d59c32dbc",
                    "context": "documentation"
                  },
                  "storage_key": "3a7bff9d-7218-4bee-b034-7e5d59c32dbc",
                  "context": "documentation",
                  "width": 800,
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
            "content": "Creating the On Component End Overlap Event",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "The <strong>On Component End Overlap</strong> event will transition your view back to the Player Character's camera when they exit the <strong>OverlapVolume</strong>.",
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
                  "content": "Navigate to the <strong>Components</strong> tab and select the <strong>Box</strong> component. Then from the <strong>Details</strong> panel, scroll down to the <strong>Events</strong> category and click the <strong>Add (+)</strong> button next to the <strong>On Component End Overlap</strong> event.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711508,
                  "caption": "",
                  "alt_text": "Add On Component End Overlap event to Box component",
                  "image": {
                    "id": 25711508,
                    "file_name": "AddOnComponEndOverlap.png",
                    "file_size": 25446,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:56.503+00:00",
                    "height": 520,
                    "width": 380,
                    "storage_key": "04d707af-161f-4df2-a6f9-ab8baed6da0b",
                    "context": "documentation"
                  },
                  "storage_key": "04d707af-161f-4df2-a6f9-ab8baed6da0b",
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
                  "content": "Duplicate the previous logic that you created for your <strong>On Component Begin Overlap Event</strong>, then delete the <strong>Get Actor Of Class</strong> node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711509,
                  "caption": "",
                  "alt_text": "Delete Get Actor Of Class node",
                  "image": {
                    "id": 25711509,
                    "file_name": "BPScript16.png",
                    "file_size": 65229,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:56.580+00:00",
                    "height": 279,
                    "width": 585,
                    "storage_key": "5b9f2e3a-d136-44cf-baf8-bf548dce42d5",
                    "context": "documentation"
                  },
                  "storage_key": "5b9f2e3a-d136-44cf-baf8-bf548dce42d5",
                  "context": "documentation",
                  "width": 800,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "From the <strong>Cast to ThirdPersonCharacter</strong> node, drag off from the <strong>As ThirdPersonCharacter</strong> output pin.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711510,
                  "caption": "",
                  "alt_text": "As ThirdPersonCharacter output pin",
                  "image": {
                    "id": 25711510,
                    "file_name": "BPScript17.png",
                    "file_size": 62166,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:56.693+00:00",
                    "height": 255,
                    "width": 865,
                    "storage_key": "5e4be8ca-6e3e-4d8d-a706-f80ab1d72176",
                    "context": "documentation"
                  },
                  "storage_key": "5e4be8ca-6e3e-4d8d-a706-f80ab1d72176",
                  "context": "documentation",
                  "width": 800,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Connect the pin to the <strong>Set View Target with Blend</strong> node's <strong>New View Target</strong> input pin.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711511,
                  "caption": "",
                  "alt_text": "Connect nodes",
                  "image": {
                    "id": 25711511,
                    "file_name": "BPScript18.png",
                    "file_size": 108475,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:56.794+00:00",
                    "height": 300,
                    "width": 1530,
                    "storage_key": "678b022f-3856-4069-b587-0bfb389b677f",
                    "context": "documentation"
                  },
                  "storage_key": "678b022f-3856-4069-b587-0bfb389b677f",
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
                  "content": "This logic will transition the camera back to the Third Person character view.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711512,
                  "caption": "Click image to expand.",
                  "alt_text": "Full VolumeTrigger On Component End Overlap logic",
                  "image": {
                    "id": 25711512,
                    "file_name": "BPScript19.png",
                    "file_size": 175254,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:56.956+00:00",
                    "height": 301,
                    "width": 1820,
                    "storage_key": "576ab6d3-f172-43b9-88ac-7eaa7a5b7b77",
                    "context": "documentation"
                  },
                  "storage_key": "576ab6d3-f172-43b9-88ac-7eaa7a5b7b77",
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
            "type": "header",
            "content": "Finished Blueprint",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "BP_BlendTriggerVolume",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25711513,
            "caption": "Click image to expand.",
            "alt_text": "Full BP_BlendTriggerVolume Blueprint",
            "image": {
              "id": 25711513,
              "file_name": "BPScript20.png",
              "file_size": 219078,
              "content_type": "image/png",
              "created_at": "2025-06-03T19:21:57.124+00:00",
              "height": 550,
              "width": 1820,
              "storage_key": "b09d90f1-3985-4c10-8217-87b209733c76",
              "context": "documentation"
            },
            "storage_key": "b09d90f1-3985-4c10-8217-87b209733c76",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Setting up the Overlap Trigger Actor",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Now that you have created your overlap Actor, you will need to place it into the Level and set up its bounds.",
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
                  "content": "From the <strong>Content Browser</strong>, drag an instance of your <strong>BP_BlendTriggerVolume</strong> into the Level.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711514,
                  "caption": "",
                  "alt_text": "Place Volume Actor instance",
                  "image": {
                    "id": 25711514,
                    "file_name": "DragBPBlendTriggerVolume.png",
                    "file_size": 482531,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:57.332+00:00",
                    "height": 664,
                    "width": 825,
                    "storage_key": "2d6be446-e802-465d-889b-2b07eff7d35d",
                    "context": "documentation"
                  },
                  "storage_key": "2d6be446-e802-465d-889b-2b07eff7d35d",
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
                  "content": "Move the <strong>BP_BlendTriggerVolume</strong> into the room with your <strong>BP_ExampleCameraActor</strong> and, from the Details panel, select the box component. Navigate to the <strong>Shape</strong> category and modify the <strong>Box Extent</strong> X, Y, and Z values so the volume will fit your room.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "From the <strong>Main Editor View</strong>, click the <strong>Play</strong> button to play in the Editor.",
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
        "excerpt_hash_id": "eW8",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1545,
        "excerpt_assignment_id": 1336,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Using the <strong>C++ Class Wizard</strong>, create a new Actor class named BlendTriggerVolume.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711515,
                  "caption": "",
                  "alt_text": "New C++ Blend Trigger Volume class",
                  "image": {
                    "id": 25711515,
                    "file_name": "AddActorClass.png",
                    "file_size": 38483,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:57.798+00:00",
                    "height": 580,
                    "width": 946,
                    "storage_key": "b0b57448-ca13-417b-aaae-ab111b793d33",
                    "context": "documentation"
                  },
                  "storage_key": "b0b57448-ca13-417b-aaae-ab111b793d33",
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
                  "content": "Navigate to your <code>BlendTriggerVolume.h</code> file, and declare the following code in your <strong>class definition</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "protected:\n\t\t\n         //Collision Bounds of the Actor Volume\n         UPROPERTY(EditAnywhere, BlueprintReadWrite)\n             class UBoxComponent* OverlapVolume;\n\t\t\n             //Camera Actor which the Actor Volume blends to\n             UPROPERTY(EditAnywhere, BlueprintReadWrite)\n             TSubclassOf&lt;ACameraActor&gt; CameraToFind;\n\t\t\n",
                  "lines_of_code": 18,
                  "id": 51942,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk0MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjUzKzAwOjAwIn0=--b783a711088c17f07412f49a4f8a84e305c1bc5f1a629242d971a26b2ead93d7",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Next, navigate to your <code>BlendTriggerVolume.cpp</code> file to set up your constructor and box component overlap methods. Declare the following include class libraries.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "`#include &quot;Components/BoxComponent.h&quot;`\n\t\t\n         `#include &quot;StaticCamerasCharacter.h&quot;`\n\t\t\n         `#include &quot;Camera/CameraActor.h&quot;`\n\t\t\n         `#include &quot;Runtime/Engine/Classes/Kismet/GameplayStatics.h&quot;`",
                  "lines_of_code": 7,
                  "id": 51943,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk0MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjUzKzAwOjAwIn0=--dffbd2edbd0c632b7bf0d896634ebb1ca750265f02d75f7b3f8e84d3875dc679",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "In the constructor <strong>ABlendTriggerVolume::ABlendTriggerVolume</strong>, declare the following code.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "ABlendTriggerVolume::ABlendTriggerVolume()\n         {\n         //Create box component default components\n         OverlapVolume = CreateDefaultSubobject&lt;UBoxComponent&gt;(TEXT(&quot;CameraProximityVolume&quot;));\n         //Set the box component attachment to the root component.\n         OverlapVolume-&gt;SetupAttachment(RootComponent);\n         }",
                  "lines_of_code": 7,
                  "id": 51944,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk0NCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjUzKzAwOjAwIn0=--0bc8e9b3f6f881b098b4802eab025156a9912065e0ce1763f381b8fe8ead1ee9",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Next, implement your <code>NotifyActorBeginOverlap</code> and <code>NotifyActorEndOverlap</code> class methods:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void ABlendTriggerVolume::NotifyActorBeginOverlap(AActor* OtherActor){\n         //Cast check to see if overlapped Actor is Third Person Player Character\n\t\t\n         if (AStaticCamerasCharacter* PlayerCharacterCheck = Cast&lt;AStaticCamerasCharacter&gt;(OtherActor))\n             {\n\t\t\n         //Cast to Player Character&#39;s PlayerController\n\t\t\n         if (APlayerController* PlayerCharacterController = Cast&lt;APlayerController&gt;(PlayerCharacterCheck-&gt;GetController()))\n                 {\n",
                  "lines_of_code": 35,
                  "id": 51945,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk0NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjUzKzAwOjAwIn0=--c352a7142212fa6466bb5f846c56aa9a64b48157b56f3e3c8d8bc7214dc7c44d",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "<strong>Compile</strong> your code.",
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
            "content": "Finished Code",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "BlendTriggerVolume.h",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "#pragma once\n\n\t#include &quot;CoreMinimal.h&quot;\n\t#include &quot;GameFramework/Actor.h&quot;\n\t#include &quot;BlendTriggerVolume.generated.h&quot;\n\n\tUCLASS()\n\tclass STATICCAMERAS_API ABlendTriggerVolume : public AActor\n\t{\n\t\tGENERATED_BODY()\n",
            "lines_of_code": 35,
            "id": 51946,
            "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk0NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjUzKzAwOjAwIn0=--dfe283068997648560192c2e7b1d42021cd58fe23170a691eb8eaa6156823233",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "BlendTriggerVolume.cpp",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "#include &quot;BlendTriggerVolume.h&quot;\n\t#include &quot;Components/BoxComponent.h&quot;\n\t#include &quot;StaticCamerasCharacter.h&quot;\n\t#include &quot;Camera/CameraActor.h&quot;\n\t#include &quot;Runtime/Engine/Classes/Kismet/GameplayStatics.h&quot;\n\n\t// Sets default values\n\tABlendTriggerVolume::ABlendTriggerVolume()\n\t{\n\n",
            "lines_of_code": 66,
            "id": 51947,
            "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk0NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjUzKzAwOjAwIn0=--e5237279fd532d0dcf3d3ee32dcb621431841a1d968f49eeda8634751bfb4a6e",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Setting up the Overlap Trigger Actor",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Now that you have created your overlap Actor, you will need to place it into the level and set up its bounds.",
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
                  "content": "Begin by navigating to your <strong>C++ Classes</strong> folder, right-click on your <strong>BlendTriggerVolume</strong> class, select <strong>Create Blueprint Class based on BlendTriggerVolume</strong>, then name your <strong>Blueprint Actor</strong> <strong>BP_BlendTriggerVolume</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711516,
                  "caption": "",
                  "alt_text": "Create Blueprint class",
                  "image": {
                    "id": 25711516,
                    "file_name": "CreateBPBlendTriggerVol.png",
                    "file_size": 50678,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:57.884+00:00",
                    "height": 369,
                    "width": 620,
                    "storage_key": "7ae1d43b-9e30-4821-a019-4ba4f5463dba",
                    "context": "documentation"
                  },
                  "storage_key": "7ae1d43b-9e30-4821-a019-4ba4f5463dba",
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
                  "content": "From the class defaults, navigate to <strong>Camera To Find</strong> in the <strong>Details</strong> panel, open the drop down menu, then select <strong>BP_ExampleCameraActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711517,
                  "caption": "",
                  "alt_text": "Finding the camera",
                  "image": {
                    "id": 25711517,
                    "file_name": "CameraToFind.png",
                    "file_size": 23761,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:57.964+00:00",
                    "height": 250,
                    "width": 500,
                    "storage_key": "4c4cc794-8fe1-4f20-8404-278eeb8de8ec",
                    "context": "documentation"
                  },
                  "storage_key": "4c4cc794-8fe1-4f20-8404-278eeb8de8ec",
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
                  "content": "Optionally, you can change the default blend time for this Blueprint without having to go back into the source code, or affecting other Blueprints with the same inherited parent class.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711518,
                  "caption": "",
                  "alt_text": "Change default Blend time",
                  "image": {
                    "id": 25711518,
                    "file_name": "DefaultBlendTime.png",
                    "file_size": 16971,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:58.031+00:00",
                    "height": 255,
                    "width": 500,
                    "storage_key": "d3e00370-39f3-4996-9280-13c8d97170c1",
                    "context": "documentation"
                  },
                  "storage_key": "d3e00370-39f3-4996-9280-13c8d97170c1",
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
                  "image_id": 25711519,
                  "caption": "",
                  "alt_text": "Compile button",
                  "image": {
                    "id": 25711519,
                    "file_name": "CompileBP.png",
                    "file_size": 12042,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:58.117+00:00",
                    "height": 100,
                    "width": 380,
                    "storage_key": "8bcedc39-47eb-4505-ab26-27407e4c8a6c",
                    "context": "documentation"
                  },
                  "storage_key": "8bcedc39-47eb-4505-ab26-27407e4c8a6c",
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
                  "content": "From the <strong>Content Browser</strong>, drag an instance of <strong>BP_BlendTriggerVolume</strong> into the level.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711520,
                  "caption": "Click image to expand.",
                  "alt_text": "Place Volume actor",
                  "image": {
                    "id": 25711520,
                    "file_name": "DragBPBlendTriggerVolume.png",
                    "file_size": 479211,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:58.180+00:00",
                    "height": 664,
                    "width": 825,
                    "storage_key": "b86cec6a-0061-4a92-bf7c-d48e26cc1236",
                    "context": "documentation"
                  },
                  "storage_key": "b86cec6a-0061-4a92-bf7c-d48e26cc1236",
                  "context": "documentation",
                  "width": 650,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Move the <strong>BP_BlendTriggerVolume</strong> into the room with your <strong>BP_ExampleCameraActor</strong>, and from the <strong>Details</strong> panel select the box component. Navigate to the <strong>Shape</strong> category and modify the <strong>Box Extent</strong> X, Y, and Z values so the volume will fit your room.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711521,
                  "caption": "Click image to expand.",
                  "alt_text": "Adjust Volume actor to fit room",
                  "image": {
                    "id": 25711521,
                    "file_name": "BoxExtent.png",
                    "file_size": 602942,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:21:58.366+00:00",
                    "height": 650,
                    "width": 1113,
                    "storage_key": "55f3e960-a289-404d-8943-ed813a1a349f",
                    "context": "documentation"
                  },
                  "storage_key": "55f3e960-a289-404d-8943-ed813a1a349f",
                  "context": "documentation",
                  "width": 650,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "From the <strong>Main Editor View</strong>, click the <strong>Play</strong> button to play in the Editor.",
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
        "excerpt_hash_id": "bV8",
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

## End Result

When the game starts, the player controls their character's movement using **WASD**. Upon overlapping the **BP\_BlendTriggerVolume** the camera view is assigned to the **Camera Actor** that you have created and placed in your level, and the view will switch to an overhead shot of the player-controlled character.

[Video: 1_eg6n8jtj](https://dev.epicgames.com/community/api/cms/videos/1_eg6n8jtj/embed.html)

You may have noticed that the view is Widescreen; you can disable this by un-checking the **Constrain Aspect Ratio** option inside the **Details** panel for the Camera Actor.

![Constrain Aspect Ratio checkbox](https://dev.epicgames.com/community/api/documentation/image/cbdeeda9-acff-481e-a05f-17e80f7e8912)
