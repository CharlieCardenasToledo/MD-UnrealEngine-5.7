# Fading Lights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/fading-lights-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 901,
        "excerpt_assignment_id": 601,
        "blocks": [
          {
            "type": "paragraph",
            "content": "This document describes how to set up a light Actor that changes color and slowly fades away on contact.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "This will be done using a <a data-document-id=\"3224974\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/point-lights-in-unreal-engine\">Point Light Component</a> containing a Box Component to serve as an overlap trigger and a Timeline component to manipulate the Point Light Actor.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "video",
            "video_id": "V_WDc7ON",
            "provider": "kaltura",
            "caption": "",
            "autoplay": false,
            "loop": false,
            "width": null,
            "video": {
              "height": 728,
              "width": 1286,
              "identifier": "V_WDc7ON"
            },
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Creating the Fading Light Actor",
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
                  "content": "Create the new <strong>Blueprint</strong> project based on <strong>Blank</strong> template, name it <strong>FadingLights</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559786,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559786,
                    "file_name": "01_CreateProject.png",
                    "file_size": 455122,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:25.767+00:00",
                    "height": 773,
                    "width": 1066,
                    "storage_key": "81523b3f-407d-4fab-9c04-7ed07a76f73c",
                    "context": "documentation"
                  },
                  "storage_key": "81523b3f-407d-4fab-9c04-7ed07a76f73c",
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
                  "content": "Navigate to the <strong>Content Browser</strong>, click the <strong>Add (+)</strong> button to create a new Blueprint <strong>Actor</strong> class named <strong>BP_LightActor.</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559787,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559787,
                    "file_name": "02_AddBPActorClass.png",
                    "file_size": 62172,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:26.030+00:00",
                    "height": 450,
                    "width": 600,
                    "storage_key": "d8d09f76-3984-488d-9c15-1b1e6f7090fc",
                    "context": "documentation"
                  },
                  "storage_key": "d8d09f76-3984-488d-9c15-1b1e6f7090fc",
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
                  "content": "<strong>Double-click</strong> the <strong>BP_LightActor</strong> from the <strong>Content Browser</strong> to open it in the <strong>Blueprint Editor</strong> and open the <strong>Class Defaults</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559788,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559788,
                    "file_name": "03_BPEditorWindow.png",
                    "file_size": 322607,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:26.166+00:00",
                    "height": 755,
                    "width": 1066,
                    "storage_key": "8a59370e-59b6-4c21-b28c-b68af9987bef",
                    "context": "documentation"
                  },
                  "storage_key": "8a59370e-59b6-4c21-b28c-b68af9987bef",
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
                  "content": "Navigate to the <strong>Component</strong> tab and click <strong>Add(+)</strong> button, select <strong>Box Collision</strong> from the dropdown menu, and rename it to <strong>OverlapCollision</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559789,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559789,
                    "file_name": "04_CreateOverlapCollision.png",
                    "file_size": 10947,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:26.394+00:00",
                    "height": 200,
                    "width": 350,
                    "storage_key": "7968c228-8e8a-4857-95eb-d1f7e8ea300b",
                    "context": "documentation"
                  },
                  "storage_key": "7968c228-8e8a-4857-95eb-d1f7e8ea300b",
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
                  "content": "Navigate to the <strong>Components</strong> tab, select and drag the <strong>OverlapCollision</strong> onto the <strong>DefaultSceneRoot</strong> to make <strong>OverlapCollision</strong> the new Root Component.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559790,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559790,
                    "file_name": "05_DraggingComponent.png",
                    "file_size": 23719,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:26.509+00:00",
                    "height": 200,
                    "width": 720,
                    "storage_key": "a881a49b-c10e-4da3-9c43-2c593576c481",
                    "context": "documentation"
                  },
                  "storage_key": "a881a49b-c10e-4da3-9c43-2c593576c481",
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
                  "content": "Click <strong>Add(+)</strong> in the <strong>Component</strong> tab, search for and select <strong>Point Light</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559791,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559791,
                    "file_name": "06_AddPointLight.png",
                    "file_size": 7812,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:26.615+00:00",
                    "height": 200,
                    "width": 350,
                    "storage_key": "f97b29bf-0c3b-4e8d-928c-36e8fcef1fe1",
                    "context": "documentation"
                  },
                  "storage_key": "f97b29bf-0c3b-4e8d-928c-36e8fcef1fe1",
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
                  "content": "Open the <strong>Event Graph</strong>, right-click the Graph, search for and select <strong>Add Timeline</strong> from the <strong>Blueprint Context Menu</strong>. Name the Timeline <strong>PointLightTimeline</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559792,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559792,
                    "file_name": "07_AddTimelineNode.png",
                    "file_size": 25689,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:26.713+00:00",
                    "height": 310,
                    "width": 350,
                    "storage_key": "006beb93-c751-4ddb-94ef-df582ce84214",
                    "context": "documentation"
                  },
                  "storage_key": "006beb93-c751-4ddb-94ef-df582ce84214",
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
                  "content": "Navigate to the <strong>My Blueprint</strong> tab and from the <strong>Variables</strong> category click the <strong>(+)</strong> button for adding a new variable of type <strong>float</strong>. Name the variable <strong>BrightnessMultiplier</strong> and compile blueprint. Set its <strong>Default Value</strong> to <strong>20.0</strong> in the <strong>Detail</strong> panel.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559793,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559793,
                    "file_name": "08_AddBrightnessMultiplier.png",
                    "file_size": 40613,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:26.850+00:00",
                    "height": 386,
                    "width": 669,
                    "storage_key": "8e7dd066-81f3-43a4-b822-9d3ccc294920",
                    "context": "documentation"
                  },
                  "storage_key": "8e7dd066-81f3-43a4-b822-9d3ccc294920",
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
                  "content": "Click <strong>Compile</strong> and <strong>Save</strong> buttons.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559794,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559794,
                    "file_name": "09_CompileSaveButtons.png",
                    "file_size": 14028,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:26.925+00:00",
                    "height": 100,
                    "width": 600,
                    "storage_key": "d3f8edb3-a706-4109-beb0-c3837f2b8344",
                    "context": "documentation"
                  },
                  "storage_key": "d3f8edb3-a706-4109-beb0-c3837f2b8344",
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
            "content": "Setting Up the Brightness Track",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "When the player overlaps with the light Actor's box component bounds, the Timeline component will require a float curve to manipulate the brightness value of the Point Light component.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "The luminosity will have an initial value of <strong>5000</strong> and will decrease to <strong>0</strong> over the span of <strong>5</strong> seconds.",
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
                  "content": "Double-click the <strong>PointLightTimeline</strong> node to open the <strong>Timeline Editor</strong>, click <strong>Track &gt; Add Float Track</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559795,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559795,
                    "file_name": "10_AddFloatTrack.png",
                    "file_size": 21117,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:27.001+00:00",
                    "height": 250,
                    "width": 720,
                    "storage_key": "a95f76e1-f041-4b4c-b7cc-d4597a1db0bc",
                    "context": "documentation"
                  },
                  "storage_key": "a95f76e1-f041-4b4c-b7cc-d4597a1db0bc",
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
                  "content": "Name the float curve track <strong>LightBrightnessFloatTrack</strong>, press <strong>Shift</strong> and click on the Graph for adding two keys to the track. Click on the first key and set its time-value to <strong>(0, 5000)</strong>, click the second key and set its time-value to <strong>(5, 0)</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559796,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559796,
                    "file_name": "11_LightBrightnessFloatTrack1.png",
                    "file_size": 35198,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:27.098+00:00",
                    "height": 420,
                    "width": 720,
                    "storage_key": "c24acd8e-44c2-41f7-936b-ae102ce1c315",
                    "context": "documentation"
                  },
                  "storage_key": "c24acd8e-44c2-41f7-936b-ae102ce1c315",
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
                  "content": "The completed LightBrightnessFloat track will appear as it does below.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559797,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559797,
                    "file_name": "12_LightBrightnessFloatTrack2.png",
                    "file_size": 30147,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:27.232+00:00",
                    "height": 420,
                    "width": 720,
                    "storage_key": "ed444551-aca7-4791-91cd-8b35e8b91c53",
                    "context": "documentation"
                  },
                  "storage_key": "ed444551-aca7-4791-91cd-8b35e8b91c53",
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
          },
          {
            "type": "header",
            "content": "Setting Up The Color Track",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "When the player overlaps with the light Actor's box component bounds, the PointLight Timeline will require a linear color curve track to manipulate the point light component's color property.",
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
                  "content": "From the <strong>Timeline Editor</strong> add a color curve track.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559798,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559798,
                    "file_name": "13_AddColorTrack.png",
                    "file_size": 24222,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:27.388+00:00",
                    "height": 250,
                    "width": 720,
                    "storage_key": "a2bd7cfe-f801-41cc-9ed7-aa82c173ac3b",
                    "context": "documentation"
                  },
                  "storage_key": "a2bd7cfe-f801-41cc-9ed7-aa82c173ac3b",
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
                  "content": "Name the new color track <strong>LightLinearColorTrack</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559799,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559799,
                    "file_name": "14_LightLinearColorTrack1.png",
                    "file_size": 33819,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:27.532+00:00",
                    "height": 445,
                    "width": 720,
                    "storage_key": "325c85e4-a9ec-49c0-a5f4-2ce501d8134b",
                    "context": "documentation"
                  },
                  "storage_key": "325c85e4-a9ec-49c0-a5f4-2ce501d8134b",
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
                  "content": "Double-click the first color key to modify it with a time of <strong>0</strong>, and <strong>RGB</strong> value of: (<strong>R</strong>:1,<strong>G:</strong>0.665,<strong>B</strong>:0.015).",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559800,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559800,
                    "file_name": "15_LightLinearColorTrackSetUp1.png",
                    "file_size": 74181,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:27.637+00:00",
                    "height": 512,
                    "width": 720,
                    "storage_key": "89128ae5-06a0-479b-b4c2-67f99cfa9d33",
                    "context": "documentation"
                  },
                  "storage_key": "89128ae5-06a0-479b-b4c2-67f99cfa9d33",
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
                  "content": "Double-click the second color key to modify it with a time of <strong>5</strong>, and <strong>RGB</strong> value of: (<strong>R</strong>: 0, <strong>G</strong>: 0, <strong>B</strong>: 0).",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559801,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559801,
                    "file_name": "16_LightLinearColorTrackSetUp2.png",
                    "file_size": 60959,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:27.806+00:00",
                    "height": 505,
                    "width": 720,
                    "storage_key": "b6330f09-a177-4d97-9257-22c291c59881",
                    "context": "documentation"
                  },
                  "storage_key": "b6330f09-a177-4d97-9257-22c291c59881",
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
                  "content": "Click <strong>Compile</strong> and <strong>Save</strong> buttons.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559802,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559802,
                    "file_name": "09_CompileSaveButtons.png",
                    "file_size": 14028,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:27.894+00:00",
                    "height": 100,
                    "width": 600,
                    "storage_key": "911810eb-7416-4bb8-8faa-ad2b91390269",
                    "context": "documentation"
                  },
                  "storage_key": "911810eb-7416-4bb8-8faa-ad2b91390269",
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
                  "content": "Your completed color track will appear as it does below.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559803,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559803,
                    "file_name": "17_LightLinearColorTrack2.png",
                    "file_size": 11968,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:28.002+00:00",
                    "height": 330,
                    "width": 720,
                    "storage_key": "2eb4ba95-bea9-498a-ad97-ade1be041568",
                    "context": "documentation"
                  },
                  "storage_key": "2eb4ba95-bea9-498a-ad97-ade1be041568",
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
          },
          {
            "type": "header",
            "content": "Work-In-Progress Blueprint",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24559804,
            "caption": "Click image for full size.",
            "alt_text": "",
            "image": {
              "id": 24559804,
              "file_name": "18_BPEditorWindow.png",
              "file_size": 110506,
              "content_type": "image/png",
              "created_at": "2025-05-02T19:10:28.099+00:00",
              "height": 691,
              "width": 1019,
              "storage_key": "6f84919f-81cf-44ed-8559-364f59062e7a",
              "context": "documentation"
            },
            "storage_key": "6f84919f-81cf-44ed-8559-364f59062e7a",
            "context": "documentation",
            "width": 600,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Creating the Collision Overlap Event and Update Logic",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "The Box Component requires the ability to trigger the TimelineComponent when an Actor enters its collision bounds.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Additionally, the PointLightTimeline will require update logic in order to change its luminosity and color.",
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
                  "content": "Navigate to the <strong>Components</strong> tab in the <strong>Blueprint Editor</strong> and select the <strong>OverlapCollision</strong> box component. From the <strong>Details</strong> panel, scroll down to the <strong>Events</strong> category and click the <strong>+</strong> icon next to the <strong>On Component Begin Overlap</strong> Event.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559805,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559805,
                    "file_name": "19_AddOnCompBeginOverlap.png",
                    "file_size": 17077,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:28.262+00:00",
                    "height": 280,
                    "width": 350,
                    "storage_key": "a7fae688-d8a9-4d3e-9054-4bf0dfa5e616",
                    "context": "documentation"
                  },
                  "storage_key": "a7fae688-d8a9-4d3e-9054-4bf0dfa5e616",
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
                  "content": "Drag off the <strong>On Component Begin Overlap (OverlapCollision)</strong> node's <strong>execution</strong> pin and connect it to the <strong>PointTimelineComponent</strong> node's <strong>Play</strong> pin.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_Timeline Name=&quot;K2Node_Timeline_0&quot;\n     TimelineName=&quot;PointLightTimeline&quot;\n     TimelineGuid=9B6871DF41CC70785FBD70A935625EAC\n     NodePosX=448\n     NodePosY=80\n     bCanRenameNode=True\n     ErrorType=1\n     NodeGuid=CD70BA9E43E1F7EB1FF420816FF55084\n     CustomProperties Pin (PinId=E50CDF574B8B5BE1ECFB4AB4CE506DCD,PinName=&quot;Play&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_ComponentBoundEvent_0 3608BECC49E96377DB2960B5B1108C19,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=7B459F68414F7C0977CD2191A446853E,PinName=&quot;PlayFromStart&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n",
                  "lines_of_code": 41,
                  "id": 44436,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQzNiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--1681cb697f2a23a5567d0c56559df094eec0b4116067a91af472e458b5d06c21",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "From the <strong>Components</strong> tab, drag the <strong>PointLight</strong> component into the <strong>Event Graph</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_VariableGet Name=&quot;K2Node_VariableGet_0&quot;\n     VariableReference=(MemberName=&quot;PointLight&quot;,bSelfContext=True)\n     NodePosX=848\n     NodePosY=144\n     NodeGuid=5EB41437410885083479FEB985CC498E\n     CustomProperties Pin (PinId=BE0F44F644A651B59B7B768F23043181,PinName=&quot;PointLight&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;object&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=Class&#39;&quot;/Script/Engine.PointLightComponent&quot;&#39;,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_2 B0B1479D4AF0E3B08F76A09E55059CE2,K2Node_Knot_0 F1E8A86F4F35354E9427F38B9E297E03,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=EF8864E146E66B02527255B9E06B6025,PinName=&quot;self&quot;,PinFriendlyName=NSLOCTEXT(&quot;K2Node&quot;, &quot;Target&quot;, &quot;Target&quot;),PinType.PinCategory=&quot;object&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=BlueprintGeneratedClass&#39;&quot;/Game/Blueprints/BP_LightActor.BP_LightActor_C&quot;&#39;,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     End Object",
                  "lines_of_code": 8,
                  "id": 44437,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQzNywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--4b9cbeed18c4e6ec8fc970f314b1bec63cc4db0b8f5f909983444745b063e8d7",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Drag off the <strong>PointLight</strong>'s pin, search for and add <strong>Set Intensity</strong> node in the actions menu.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name=&quot;K2Node_CallFunction_2&quot;\n     FunctionReference=(MemberParent=Class&#39;&quot;/Script/Engine.LightComponent&quot;&#39;,MemberName=&quot;SetIntensity&quot;)\n     NodePosX=1040\n     NodePosY=64\n     NodeGuid=23E0F4404C18096DF62804AFAA7BC709\n     CustomProperties Pin (PinId=9C312EB049C5A1020D6797A147DEABB8,PinName=&quot;execute&quot;,PinToolTip=&quot;\\nExec&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_Timeline_0 B34A88804DC700EB96C1A08A8BC63B0E,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=87A5CA2F43E3E67419AFD1A8953F299B,PinName=&quot;then&quot;,PinToolTip=&quot;\\nExec&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_3 744D0148419A07627F1A9F978A0C575D,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=B0B1479D4AF0E3B08F76A09E55059CE2,PinName=&quot;self&quot;,PinFriendlyName=NSLOCTEXT(&quot;K2Node&quot;, &quot;Target&quot;, &quot;Target&quot;),PinToolTip=&quot;Target\\nLight Component Object Reference&quot;,PinType.PinCategory=&quot;object&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=Class&#39;&quot;/Script/Engine.LightComponent&quot;&#39;,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_VariableGet_0 BE0F44F644A651B59B7B768F23043181,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=FDEA2486488BDE31C3E56B9DDFB9CD27,PinName=&quot;NewIntensity&quot;,PinToolTip=&quot;New Intensity\\nFloat (single-precision)&quot;,PinType.PinCategory=&quot;real&quot;,PinType.PinSubCategory=&quot;float&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue=&quot;0.0&quot;,AutogeneratedDefaultValue=&quot;0.0&quot;,LinkedTo=(K2Node_PromotableOperator_0 69A2EF8C4A59A02C101F58AD8511E67A,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     End Object",
                  "lines_of_code": 10,
                  "id": 44438,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQzOCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--0638a2e21167221d1f2ee7f5cc8c01eb82deeb7966dfc03ad1685a49c5e7fa31",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "From the <strong>PointLightTimeline</strong> node, drag off the <strong>Light Brightness Float Track</strong> pin, search for and add <strong>Multiply</strong> node in the actions menu.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_PromotableOperator Name=&quot;K2Node_PromotableOperator_0&quot;\n     bIsPureFunc=True\n     FunctionReference=(MemberParent=Class&#39;&quot;/Script/Engine.KismetMathLibrary&quot;&#39;,MemberName=&quot;Multiply_DoubleDouble&quot;)\n     NodePosX=864\n     NodePosY=192\n     NodeGuid=64A7E68440746F350AC19F86346C4452\n     CustomProperties Pin (PinId=82EF0A4B4E496697FA249BB6F7507FDF,PinName=&quot;A&quot;,PinToolTip=&quot;A\\nFloat (double-precision)&quot;,PinType.PinCategory=&quot;real&quot;,PinType.PinSubCategory=&quot;double&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_Timeline_0 5D3D277B4502D9621FEE289C0C2C69A1,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=75D0A21342595E689923BA87FB4EF370,PinName=&quot;B&quot;,PinToolTip=&quot;B\\nFloat (double-precision)&quot;,PinType.PinCategory=&quot;real&quot;,PinType.PinSubCategory=&quot;double&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_VariableGet_1 485EF0D44BC98AA6894EF282D5F53F5F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=69A2EF8C4A59A02C101F58AD8511E67A,PinName=&quot;ReturnValue&quot;,PinToolTip=&quot;Return Value\\nFloat (double-precision)\\n\\nMultiplication (A * B)&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;real&quot;,PinType.PinSubCategory=&quot;double&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_2 FDEA2486488BDE31C3E56B9DDFB9CD27,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     End Object",
                  "lines_of_code": 10,
                  "id": 44439,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQzOSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--75dc0d5ed90f55008ccdf2f53d33686b73870daf40b90a09c6237f97c35baad0",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "From the <strong>My Blueprint</strong> tab drag the <strong>BrightnessMultiplier</strong> float variable into the <strong>Event Graph</strong>, select <strong>Get Brightness Multiplier</strong>, then connect it to the <strong>Multiply</strong> node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_VariableGet Name=&quot;K2Node_VariableGet_1&quot;\n     VariableReference=(MemberName=&quot;BrightnessMultiplier&quot;,MemberGuid=FCCF7F5E4A6E4FD75FAA849998FE2E92,bSelfContext=True)\n     NodePosX=864\n     NodePosY=288\n     NodeGuid=3B08B13441FCF1AEDC7E3CA58137A9D2\n     CustomProperties Pin (PinId=485EF0D44BC98AA6894EF282D5F53F5F,PinName=&quot;BrightnessMultiplier&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;real&quot;,PinType.PinSubCategory=&quot;double&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue=&quot;0.0&quot;,AutogeneratedDefaultValue=&quot;0.0&quot;,LinkedTo=(K2Node_PromotableOperator_0 75D0A21342595E689923BA87FB4EF370,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=8978695144D2F58451CFF4858B5A8790,PinName=&quot;self&quot;,PinFriendlyName=NSLOCTEXT(&quot;K2Node&quot;, &quot;Target&quot;, &quot;Target&quot;),PinType.PinCategory=&quot;object&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=BlueprintGeneratedClass&#39;&quot;/Game/Blueprints/BP_LightActor.BP_LightActor_C&quot;&#39;,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     End Object",
                  "lines_of_code": 8,
                  "id": 44440,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ0MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--157714cf00cf3d2bbf6637c5808d09ac0bdbe55e05c0799210770e44890a3259",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Connect the <strong>Update</strong> pin of the <strong>PointLightTimeline</strong> to the <strong>Set Intensity</strong> node, then connect the <strong>Return Value</strong> pin of the <strong>Multiply</strong> node to the <strong>New Intensity</strong> input pin of the <strong>Set Intensity</strong> node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559806,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559806,
                    "file_name": "25_BPScript6.png",
                    "file_size": 73983,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:28.371+00:00",
                    "height": 350,
                    "width": 720,
                    "storage_key": "fe2032eb-ac08-494f-999c-1de0da8ffcb5",
                    "context": "documentation"
                  },
                  "storage_key": "fe2032eb-ac08-494f-999c-1de0da8ffcb5",
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
                  "content": "Drag off the <strong>PointLight</strong> node, search for and select <strong>Set Light Color</strong> from the actions menu.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name=&quot;K2Node_CallFunction_3&quot;\n     FunctionReference=(MemberParent=Class&#39;&quot;/Script/Engine.LightComponent&quot;&#39;,MemberName=&quot;SetLightColor&quot;)\n     NodePosX=1296\n     NodePosY=64\n     NodeGuid=43D9BD7C4283FC673F36A1930C3243C6\n     CustomProperties Pin (PinId=744D0148419A07627F1A9F978A0C575D,PinName=&quot;execute&quot;,PinToolTip=&quot;\\nExec&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_2 87A5CA2F43E3E67419AFD1A8953F299B,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=D792D59441A56ECC8C3D4CB3900F9C66,PinName=&quot;then&quot;,PinToolTip=&quot;\\nExec&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=FE00319941A34DE91479318F2093ECE0,PinName=&quot;self&quot;,PinFriendlyName=NSLOCTEXT(&quot;K2Node&quot;, &quot;Target&quot;, &quot;Target&quot;),PinToolTip=&quot;Target\\nLight Component Object Reference&quot;,PinType.PinCategory=&quot;object&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=Class&#39;&quot;/Script/Engine.LightComponent&quot;&#39;,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_Knot_1 808A85F1410FB25AEFC0C8B494E8DA53,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=BD932EBD48DCC38B6CA11F9AED634AB2,PinName=&quot;NewLightColor&quot;,PinToolTip=&quot;New Light Color\\nLinear Color Structure&quot;,PinType.PinCategory=&quot;struct&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=ScriptStruct&#39;&quot;/Script/CoreUObject.LinearColor&quot;&#39;,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_Knot_3 912593C04753CE1C51DEF2B3D7CFA5AD,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=6602709A43E5CCC5AB675882406E458C,PinName=&quot;bSRGB&quot;,PinToolTip=&quot;SRGB\\nBoolean&quot;,PinType.PinCategory=&quot;bool&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue=&quot;true&quot;,AutogeneratedDefaultValue=&quot;true&quot;,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n",
                  "lines_of_code": 11,
                  "id": 44441,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ0MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--2f3fd528c112523411f2c356aedb2019984725144a6d707d3fc780b812126627",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Connect the <strong>Light Linear Color Track</strong> pin of the <strong>PointLightTimeline</strong> node to the <strong>New Light Color</strong> pin of the <strong>Set Light Color</strong> node. Then connect the <strong>execution</strong> pin from the <strong>Set Intensity</strong> node to the <strong>Set Light Color</strong> node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559807,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559807,
                    "file_name": "27_BPScript8.png",
                    "file_size": 88738,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:28.495+00:00",
                    "height": 300,
                    "width": 900,
                    "storage_key": "9801c2fd-7233-471b-bd6a-135453ed496a",
                    "context": "documentation"
                  },
                  "storage_key": "9801c2fd-7233-471b-bd6a-135453ed496a",
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
                  "content": "Click <strong>Compile</strong> and <strong>Save</strong> buttons.",
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
            "image_id": 24559808,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24559808,
              "file_name": "09_CompileSaveButtons.png",
              "file_size": 14028,
              "content_type": "image/png",
              "created_at": "2025-05-02T19:10:28.720+00:00",
              "height": 100,
              "width": 600,
              "storage_key": "fed8461c-d636-4d6b-9791-f99744a1dbe6",
              "context": "documentation"
            },
            "storage_key": "fed8461c-d636-4d6b-9791-f99744a1dbe6",
            "context": "documentation",
            "width": null,
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
            "type": "code_snippet",
            "description": "",
            "snippet_type": "blueprint",
            "title": "context_graph",
            "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_Timeline Name=&quot;K2Node_Timeline_0&quot;\nTimelineName=&quot;PointLightTimeline&quot;\nTimelineGuid=9B6871DF41CC70785FBD70A935625EAC\nNodePosX=448\nNodePosY=80\nbCanRenameNode=True\nErrorType=1\nNodeGuid=CD70BA9E43E1F7EB1FF420816FF55084\nCustomProperties Pin (PinId=E50CDF574B8B5BE1ECFB4AB4CE506DCD,PinName=&quot;Play&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_ComponentBoundEvent_0 3608BECC49E96377DB2960B5B1108C19,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\nCustomProperties Pin (PinId=7B459F68414F7C0977CD2191A446853E,PinName=&quot;PlayFromStart&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n",
            "lines_of_code": 116,
            "id": 44442,
            "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ0MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--297879e19490237df42c6c11081309360702954f621e2f522415961412083e29",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Level Setup",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "To best demonstrate the functionality of the code you have written, you will need to remove all Light Sources Actors from the Level.",
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
                  "content": "In the <strong>Content Browser</strong> navigate to the <strong>BP_LightActor</strong> Asset, select it and drag it into the <strong>Level</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559809,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559809,
                    "file_name": "29_DragBPLightActortoLevel.png",
                    "file_size": 333673,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:28.823+00:00",
                    "height": 595,
                    "width": 700,
                    "storage_key": "4a45db11-9891-4d6f-9131-61d4b94c6f72",
                    "context": "documentation"
                  },
                  "storage_key": "4a45db11-9891-4d6f-9131-61d4b94c6f72",
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
                  "content": "Select the <strong>BP_LightActor</strong> in the <strong> World Outliner</strong>, navigate to the <strong>Details</strong> panel and set the <strong>Location</strong> settings to <strong>(0, 0, 300)</strong> and the <strong>Scale</strong> settings to <strong>(10, 10, 10)</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559810,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559810,
                    "file_name": "30_GeneralSetUpActor.png",
                    "file_size": 27071,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:29.017+00:00",
                    "height": 350,
                    "width": 600,
                    "storage_key": "dd1013e6-85a2-43c0-8f71-4099fa4d2ec3",
                    "context": "documentation"
                  },
                  "storage_key": "dd1013e6-85a2-43c0-8f71-4099fa4d2ec3",
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
                  "content": "Delete the <strong>DirectionalLight Actor</strong> in the <strong>World Outliner</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559811,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559811,
                    "file_name": "31_DelDirectLight.png",
                    "file_size": 37888,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:29.115+00:00",
                    "height": 300,
                    "width": 600,
                    "storage_key": "f3de7e71-da0b-4c87-b0ad-5bc6a87a23f7",
                    "context": "documentation"
                  },
                  "storage_key": "f3de7e71-da0b-4c87-b0ad-5bc6a87a23f7",
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
                  "content": "Level should look as following.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559812,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559812,
                    "file_name": "32_FinishedLevel.png",
                    "file_size": 92483,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:29.206+00:00",
                    "height": 445,
                    "width": 975,
                    "storage_key": "6791eb26-1764-498a-bd1c-defa68031425",
                    "context": "documentation"
                  },
                  "storage_key": "6791eb26-1764-498a-bd1c-defa68031425",
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
          },
          {
            "type": "header",
            "content": "End Result",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Now that the Light Actor and Level have been set up, click <strong>Play (PIE)</strong> to automatically take possession of the spectator Pawn.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You can control the spectator Pawn and navigate into the Light Actor's box component bounds.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Once the Timeline Component's Play function has been triggered, the light's color and luminosity should begin to change over a 5-second timespan.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "video",
            "video_id": "V_QiFZio",
            "provider": "kaltura",
            "caption": "",
            "autoplay": false,
            "loop": false,
            "width": null,
            "video": {
              "height": 728,
              "width": 1286,
              "identifier": "V_QiFZio"
            },
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "bNy",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 902,
        "excerpt_assignment_id": 602,
        "blocks": [
          {
            "type": "paragraph",
            "content": "This document describes how to set up a light Actor that changes color and slowly fades away on contact.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "This will be done using a <a data-document-id=\"3224974\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/point-lights-in-unreal-engine\">Point Light Component</a> containing a Box Component to serve as an overlap trigger and a Timeline component to manipulate the Point Light Actor.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "video",
            "video_id": "V_Kl41aZ",
            "provider": "kaltura",
            "caption": "",
            "autoplay": false,
            "loop": false,
            "width": null,
            "video": {
              "height": 728,
              "width": 1286,
              "identifier": "V_Kl41aZ"
            },
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Creating the Fading Light Actor",
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
                  "content": "Create the new <strong>C++</strong> project based on <strong>Blank</strong> template, name it <strong>FadingLights</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559813,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559813,
                    "file_name": "01_CreateProject.png",
                    "file_size": 455083,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:30.103+00:00",
                    "height": 773,
                    "width": 1066,
                    "storage_key": "eccb0c73-253b-49bb-8992-5a0f6680a749",
                    "context": "documentation"
                  },
                  "storage_key": "eccb0c73-253b-49bb-8992-5a0f6680a749",
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
                  "content": "Navigate to the <strong>Content Browser</strong>, click <strong>C++ Classes</strong> folder, then click <strong>Add (+)</strong> button and select <strong>New C++ Class</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559814,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559814,
                    "file_name": "02_AddCppClass.png",
                    "file_size": 26126,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:30.260+00:00",
                    "height": 335,
                    "width": 600,
                    "storage_key": "b972f34c-6497-4494-8ac2-e271ee0ec17b",
                    "context": "documentation"
                  },
                  "storage_key": "b972f34c-6497-4494-8ac2-e271ee0ec17b",
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
                  "content": "Select <strong>Actor</strong> as a <strong>Parent Class</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559815,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559815,
                    "file_name": "02_ChooseParentCppClass.png",
                    "file_size": 38045,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:30.340+00:00",
                    "height": 580,
                    "width": 946,
                    "storage_key": "54633a02-de33-4b04-9370-36dabac38e10",
                    "context": "documentation"
                  },
                  "storage_key": "54633a02-de33-4b04-9370-36dabac38e10",
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
                  "content": "Name created Actor as <strong>LightActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559816,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559816,
                    "file_name": "03_NameCppActor.png",
                    "file_size": 32717,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:30.499+00:00",
                    "height": 580,
                    "width": 946,
                    "storage_key": "07ba1cb1-4263-4811-b3a4-78d31aec16f8",
                    "context": "documentation"
                  },
                  "storage_key": "07ba1cb1-4263-4811-b3a4-78d31aec16f8",
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
                  "content": "When new Actor is created, <strong>Visual Studio</strong> automatically  opens <code>LightActor.h</code> and <code>LightActor.cpp</code> files. Navigate to the <code>LightActor.h</code> file and declare the following:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "LightActor.h",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "#include &quot;Components/TimelineComponent.h&quot;",
                  "lines_of_code": 1,
                  "id": 44443,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ0MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--66ed3cbca80e8d97581283462df6f792df66d269636ea2c3f319251945fb0930",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Next, in the <code>LightActor</code> class definition, add the following code:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "LightActor.h",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "public:\n\n             UPROPERTY(EditAnywhere)\n             UCurveFloat* PointLightFloatCurve;\n\n             UPROPERTY(EditAnywhere)\n             UCurveLinearColor* PointLightColorCurve;\n\n     protected:\n\n",
                  "lines_of_code": 37,
                  "id": 44444,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ0NCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--73e20b6cf55fb2afc40c60fd81587c51accfafc59a34b223459bb33c9c3f820d",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to <code>LightActor.cpp</code> and add the following class libraries.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "LightActor.cpp",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "#include &quot;Components/BoxComponent.h&quot;\n     #include &quot;Components/PointLightComponent.h&quot;",
                  "lines_of_code": 2,
                  "id": 44445,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ0NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--f5f306b523dead1eabeca13f182283fab2e0b90f3314c0f1c8aa116e58ad8e63",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "In the constructor for <code>ALightActor::ALightActor</code> declare the following:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "LightActor.cpp",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "ALightActor::ALightActor()\n     {\n         // Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n         PrimaryActorTick.bCanEverTick = true;\n\n         //Create our Default Components\n         PointLightComp = CreateDefaultSubobject&lt;UPointLightComponent&gt;(TEXT(&quot;PointLightComp&quot;));\n         LightTimelineComp = CreateDefaultSubobject&lt;UTimelineComponent&gt;(TEXT(&quot;LightTimelineComp&quot;));\n         LightOverlapVolume = CreateDefaultSubobject&lt;UBoxComponent&gt;(TEXT(&quot;LightOverlapVolume&quot;));\n\n",
                  "lines_of_code": 17,
                  "id": 44446,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ0NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--b37434429ce1679a72dd353cf5411f0aa3a743393c7545bcae1d830072d40c10",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Next, implement the Point Light component's <code>UFunction</code> methods:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "LightActor.cpp",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void ALightActor::UpdateLightBrightness(float BrightnessOutput)\n     {\n         PointLightComp-&gt;SetLightBrightness(BrightnessOutput * 20.0f);\n     }\n\n     void ALightActor::UpdateLightColor(FLinearColor ColorOutput)\n     {\n         PointLightComp-&gt;SetLightColor(ColorOutput);\n     }",
                  "lines_of_code": 9,
                  "id": 44447,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ0NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--f5a880c680b6d34b5704d2ccdcae78f220166502485f014841ec5fcbba7299dd",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Then, in the <code>BeginPlay</code> method, add the following code:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "LightActor.cpp",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void ALightActor::BeginPlay()\n     {\n         Super::BeginPlay();\n\n         //Binding our float and color track to their respective functions\n         UpdateBrightnessTrack.BindDynamic(this, &amp;ALightActor::UpdateLightBrightness);\n         UpdateColorTrack.BindDynamic(this, &amp;ALightActor::UpdateLightColor);\n\n         //If we have a float curve, bind it&#39;s graph to our update function\n         if (PointLightFloatCurve)\n",
                  "lines_of_code": 20,
                  "id": 44448,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ0OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--ed4207a3ab77653da924dfded0eea2eb501da3dfc91cb8b0ce1018bf14551cd6",
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
              ],
              [
                {
                  "type": "paragraph",
                  "content": "From the <strong>Content Browser</strong>, navigate to the <strong>C++ Classes folder</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Right click the <strong>LightActor</strong>, select <strong>Create Blueprint Class based on LightActor</strong>, and name the Blueprint Actor <strong>BP_LightActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559817,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559817,
                    "file_name": "04_CreatBPBasedOnActor.png",
                    "file_size": 41861,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:30.581+00:00",
                    "height": 350,
                    "width": 600,
                    "storage_key": "913e8a6e-4b3e-4e32-aec3-2271dd21b7af",
                    "context": "documentation"
                  },
                  "storage_key": "913e8a6e-4b3e-4e32-aec3-2271dd21b7af",
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
            "content": "The BP_LightActor's Class Defaults will appear as they do below:",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24559818,
            "caption": "Click image for full size.",
            "alt_text": "",
            "image": {
              "id": 24559818,
              "file_name": "05_BlueprintEditorWindow.png",
              "file_size": 186599,
              "content_type": "image/png",
              "created_at": "2025-05-02T19:10:30.676+00:00",
              "height": 563,
              "width": 1061,
              "storage_key": "6c6b3acd-bc09-4a36-bfbf-6e0704bf7e40",
              "context": "documentation"
            },
            "storage_key": "6c6b3acd-bc09-4a36-bfbf-6e0704bf7e40",
            "context": "documentation",
            "width": 600,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Work-In-Progress Code",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "LightActor.h",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "//Copyright 1998-2022 Epic Games, Inc. All Rights Reserved.\n\n\t#pragma once\n\t#include &quot;Components/TimelineComponent.h&quot;\n\t#include &quot;CoreMinimal.h&quot;\n\t#include &quot;GameFramework/Actor.h&quot;\n\t#include &quot;LightActor.generated.h&quot;\n\n\tUCLASS()\n\tclass FADINGLIGHTS_API ALightActor : public AActor\n",
            "lines_of_code": 63,
            "id": 44449,
            "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ0OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--1f5083c2d1aeea780ea731261faf6c43ea409711a763fa97a11cac812285b070",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "LightActor.cpp",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "//Copyright 1998-2022 Epic Games, Inc. All Rights Reserved.\n\n\t#include &quot;LightActor.h&quot;\n\t#include &quot;Components/BoxComponent.h&quot;\n\t#include &quot;Components/PointLightComponent.h&quot;\n\n\t// Sets default values\n\tALightActor::ALightActor()\n\t{\n\t\t// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n",
            "lines_of_code": 63,
            "id": 44450,
            "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ1MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--7e2ce1239b195bfb8ca0264af9f811af6850886ec3e793b51ba325d3e7bf4001",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Creating and Binding the Collision Overlap Event",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "The Box Component requires the ability to trigger the <strong>TimelineComponent</strong> when an Actor enters its collision bounds.",
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
                  "content": "Navigate to the class definition of the <code>LightActor.h</code> file and declare the following under <code>BrightnessMultiplier</code>:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "LightActor.h",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "protected:\n\n         UFUNCTION()\n         void OnOverlapBegin(class UPrimitiveComponent* OverlappedComp, class AActor* OtherActor, class UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult&amp; SweepResult);",
                  "lines_of_code": 4,
                  "id": 44451,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ1MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--a93cafcf3f6461338b27a619fdaa45f73db976d1817263e3a6d4ae963e65cba3",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Next, navigate to the <code>LightActor.cpp</code> file and implement the <code>OnOverlapBegin</code> function.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "LightActor.cpp",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void ALightActor::OnOverlapBegin(class UPrimitiveComponent* OverlappedComp, class AActor* OtherActor, class UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult&amp; SweepResult)\n     {\n         LightTimelineComp-&gt;Play();\n     }",
                  "lines_of_code": 4,
                  "id": 44452,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ1MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--909cb908daca4301579351fcff7a5666597813e66d3bbf4424dd4a50ccc36e32",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Bind the overlap function in the <code>BeginPlay</code> method:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "LightActor.cpp",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "//Binding our Box Component to our Light Actor&#39;s Overlap Function\n     LightOverlapVolume-&gt;OnComponentBeginOverlap.AddDynamic(this, &amp;ALightActor::OnOverlapBegin);",
                  "lines_of_code": 2,
                  "id": 44453,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ1MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--51810ddbbc2d9d1bf1a605f3a0005e82bf2d71f9543691f15d1142f1731e6169",
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
            "type": "paragraph",
            "content": "LightActor.h",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "//Copyright 1998-2022 Epic Games, Inc. All Rights Reserved.\n\n\t#pragma once\n\t#include &quot;Components/TimelineComponent.h&quot;\n\t#include &quot;CoreMinimal.h&quot;\n\t#include &quot;GameFramework/Actor.h&quot;\n\t#include &quot;LightActor.generated.h&quot;\n\n\tUCLASS()\n\tclass FADINGLIGHTS_API ALightActor : public AActor\n",
            "lines_of_code": 68,
            "id": 44454,
            "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ1NCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--fbd7b7f1ed097ba25da3c7997db22c9975961dcf3b509b5bec3aaf06b50bf782",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "LightActor.cpp",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "//Copyright 1998-2022 Epic Games, Inc. All Rights Reserved.\n\n\t// Fill out your copyright notice in the Description page of Project Settings.\n\n\t#include &quot;LightActor.h&quot;\n\t#include &quot;Components/BoxComponent.h&quot;\n\t#include &quot;Components/PointLightComponent.h&quot;\n\n\t// Sets default values\n\tALightActor::ALightActor()\n",
            "lines_of_code": 70,
            "id": 44455,
            "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ1NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjQwKzAwOjAwIn0=--dc5ddf5c67d76652c470ad73d9e0cb87099e5b530bc14c7c1e2f045854fab697",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Setting Up the Brightness Track",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "When the player overlaps with the light Actor's box component bounds, the Timeline component will require a float curve to manipulate the Point Light component's brightness value.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "The luminosity will have an initial value of <strong>5000</strong> and will decrease to <strong>0</strong> over the span of <strong>5</strong> seconds.",
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
                  "content": "Navigate to the <strong>Content Browser</strong>, select <strong>Add (+) &gt; Miscellaneous &gt; Curve</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559819,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559819,
                    "file_name": "06_AddCurveAsset.png",
                    "file_size": 60066,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:30.891+00:00",
                    "height": 451,
                    "width": 600,
                    "storage_key": "687c5b7f-1f03-4b8d-9af8-168fce9cf379",
                    "context": "documentation"
                  },
                  "storage_key": "687c5b7f-1f03-4b8d-9af8-168fce9cf379",
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
                  "content": "Select <strong>CurveFloat</strong> and name the Asset <strong>BrightnessCurveFloat</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559820,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559820,
                    "file_name": "07_ParentClassFloatCurve.png",
                    "file_size": 18627,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:31.056+00:00",
                    "height": 294,
                    "width": 600,
                    "storage_key": "182995c7-4d6d-4de2-a172-a0cf6b6faa48",
                    "context": "documentation"
                  },
                  "storage_key": "182995c7-4d6d-4de2-a172-a0cf6b6faa48",
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
                  "content": "Double-click the <strong>BrightnessCurveFloat</strong> to open the <strong>Timeline Editor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Add two keys to the Float Curve, by right clicking on the <strong>Graph</strong>, then select <strong>Add Key</strong>. Adjust time-value of the first key to the <strong>(0, 5000)</strong>. Adjust time-value of the second key to the <strong>(5, 0)</strong>. Your <strong>BrightnessCurveFloat</strong> should look as following:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559821,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559821,
                    "file_name": "08_BrightnessCurveFloat.png",
                    "file_size": 40958,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:31.147+00:00",
                    "height": 530,
                    "width": 880,
                    "storage_key": "ffcf364f-6234-4b8e-9127-1a18a4e718d8",
                    "context": "documentation"
                  },
                  "storage_key": "ffcf364f-6234-4b8e-9127-1a18a4e718d8",
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
                  "content": "Save the <strong>BrightnessCurveFloat</strong>, then navigate back to the <strong>Content Browser</strong> and double-click the <strong>BP_LightActor</strong> to open its <strong>Class Defaults</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to the <strong>Details</strong> panel and select <strong>Brightness Curve Float</strong> from the <strong>Point Light Float Curve</strong> dropdown menu.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559822,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559822,
                    "file_name": "09_SelectPointLightCurve.png",
                    "file_size": 15207,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:31.287+00:00",
                    "height": 236,
                    "width": 460,
                    "storage_key": "bb3657e2-d830-4f2f-841b-aacf0ebcc0dd",
                    "context": "documentation"
                  },
                  "storage_key": "bb3657e2-d830-4f2f-841b-aacf0ebcc0dd",
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
                  "content": "Click <strong>Compile</strong> and <strong>Save</strong> buttons.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559823,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559823,
                    "file_name": "10_SaveCompileButtons.png",
                    "file_size": 12619,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:31.368+00:00",
                    "height": 100,
                    "width": 460,
                    "storage_key": "f92a17c8-6694-447d-9797-58d476e9914e",
                    "context": "documentation"
                  },
                  "storage_key": "f92a17c8-6694-447d-9797-58d476e9914e",
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
            "content": "Setting Up the Color Track",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "When the player overlaps with the light Actor's box component bounds, the PointLight Timeline will require a linear color curve track to manipulate the Point Light component's color property.",
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
                  "content": "Navigate to the <strong>Content Browser</strong>, select <strong>Add (+) &gt; Miscellaneous &gt; Curve</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559824,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559824,
                    "file_name": "06_AddCurveAsset.png",
                    "file_size": 60066,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:31.493+00:00",
                    "height": 451,
                    "width": 600,
                    "storage_key": "5f3cfb32-a7cd-4435-b574-e77d8f5497b1",
                    "context": "documentation"
                  },
                  "storage_key": "5f3cfb32-a7cd-4435-b574-e77d8f5497b1",
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
                  "content": "Select <strong>CurveLinearColor</strong> and name the asset <strong>LinearColorCurve</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559825,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559825,
                    "file_name": "11_ParentClassColorCurve.png",
                    "file_size": 18628,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:31.687+00:00",
                    "height": 294,
                    "width": 600,
                    "storage_key": "f44ca31d-00cc-405e-afc6-6dbd9a514c6f",
                    "context": "documentation"
                  },
                  "storage_key": "f44ca31d-00cc-405e-afc6-6dbd9a514c6f",
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
                  "content": "Double-click the <strong>LinearColorCurve</strong> to open the <strong>Timeline Editor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Double-click the first color key to modify it, set <strong>RGB</strong> value of: (<strong>R</strong>:1, <strong>G:</strong>0.665, <strong>B</strong>:0.015).",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559826,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559826,
                    "file_name": "12_KeyCurveAdjustment1.png",
                    "file_size": 76789,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:31.765+00:00",
                    "height": 635,
                    "width": 790,
                    "storage_key": "4e667786-6e4f-433f-8da7-78a0425ab15c",
                    "context": "documentation"
                  },
                  "storage_key": "4e667786-6e4f-433f-8da7-78a0425ab15c",
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
                  "content": "Double-click the second color key to modify it, set <strong>RGB</strong> value of: (<strong>R</strong>:0, <strong>G:</strong>0, <strong>B</strong>:0).",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559827,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559827,
                    "file_name": "13_KeyCurveAdjustment2.png",
                    "file_size": 95916,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:31.971+00:00",
                    "height": 630,
                    "width": 790,
                    "storage_key": "f16a3fb6-b808-464b-b34d-90b06955343e",
                    "context": "documentation"
                  },
                  "storage_key": "f16a3fb6-b808-464b-b34d-90b06955343e",
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
                  "content": "Select second <strong>Point</strong> on the <strong>Graph</strong> by clicking on it and set the time to <strong>5</strong> seconds.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559828,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559828,
                    "file_name": "14_SetTimeColoreCurve.png",
                    "file_size": 47287,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:32.141+00:00",
                    "height": 526,
                    "width": 790,
                    "storage_key": "74991829-98df-4a1b-b070-a104df241083",
                    "context": "documentation"
                  },
                  "storage_key": "74991829-98df-4a1b-b070-a104df241083",
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
                  "content": "Your <strong>LinearColorCurve</strong> should look as following:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559829,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559829,
                    "file_name": "15_LinearColorCurve.png",
                    "file_size": 48664,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:32.288+00:00",
                    "height": 509,
                    "width": 790,
                    "storage_key": "e4ad3c11-1e41-40f9-8615-aeeb2e5f57a3",
                    "context": "documentation"
                  },
                  "storage_key": "e4ad3c11-1e41-40f9-8615-aeeb2e5f57a3",
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
                  "content": "Save the <strong>LinearColorCurve</strong>, then navigate back to the Content Browser and double-click the <strong>BP_LightActor</strong> to open its class defaults.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to the <strong>Details Panel</strong> and select <strong>Brightness Curve Float</strong> from the <strong>Point Light Float Curve</strong> dropdown menu.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559830,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559830,
                    "file_name": "16_selectLinearColorCurve.png",
                    "file_size": 14928,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:32.373+00:00",
                    "height": 235,
                    "width": 460,
                    "storage_key": "5da4ab70-cee2-4934-9a0b-3ce217705013",
                    "context": "documentation"
                  },
                  "storage_key": "5da4ab70-cee2-4934-9a0b-3ce217705013",
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
                  "content": "Click <strong>Compile</strong> and <strong>Save</strong> buttons.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559831,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559831,
                    "file_name": "10_SaveCompileButtons.png",
                    "file_size": 12619,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:32.569+00:00",
                    "height": 100,
                    "width": 460,
                    "storage_key": "919826a2-0719-4b17-a180-370287615fcf",
                    "context": "documentation"
                  },
                  "storage_key": "919826a2-0719-4b17-a180-370287615fcf",
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
            "content": "Level Setup",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "To best demonstrate the functionality of the code you have written, you will need to remove all Light Sources Actors from the Level.",
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
                  "content": "In the <strong>Content Browser</strong> navigate to the <strong>BP_LightActor</strong> Asset, select it and drag it into the <strong>Level</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559832,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559832,
                    "file_name": "17_DragBPLightActortoLevel.png",
                    "file_size": 334684,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:32.711+00:00",
                    "height": 595,
                    "width": 700,
                    "storage_key": "0ddf77e3-eb7b-4e4a-800e-c9f791fea353",
                    "context": "documentation"
                  },
                  "storage_key": "0ddf77e3-eb7b-4e4a-800e-c9f791fea353",
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
                  "content": "Select the <strong>BP_LightActor</strong> in the <strong>World Outliner</strong>, navigate to the <strong>Details</strong> panel and set the <strong>Location</strong> settings to <strong>(0, 0, 300)</strong> and the <strong>Scale</strong> settings to <strong>(10, 10, 10)</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559833,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559833,
                    "file_name": "30_GeneralSetUpActor.png",
                    "file_size": 27071,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:32.924+00:00",
                    "height": 350,
                    "width": 600,
                    "storage_key": "2029bc21-e6a2-457b-a006-e75e20a53343",
                    "context": "documentation"
                  },
                  "storage_key": "2029bc21-e6a2-457b-a006-e75e20a53343",
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
                  "content": "Delete the <strong>DirectionalLight Actor</strong> in the <strong>World Outliner</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559834,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559834,
                    "file_name": "31_DelDirectLight.png",
                    "file_size": 37888,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:33.069+00:00",
                    "height": 300,
                    "width": 600,
                    "storage_key": "71a4986e-bc4a-4c96-849d-40c47cad32a9",
                    "context": "documentation"
                  },
                  "storage_key": "71a4986e-bc4a-4c96-849d-40c47cad32a9",
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
                  "content": "The Level should look as the following.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559835,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559835,
                    "file_name": "32_FinishedLevel.png",
                    "file_size": 92483,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:10:33.209+00:00",
                    "height": 445,
                    "width": 975,
                    "storage_key": "c2cb3c7a-c8ed-462a-807f-98bb3d78de16",
                    "context": "documentation"
                  },
                  "storage_key": "c2cb3c7a-c8ed-462a-807f-98bb3d78de16",
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
          },
          {
            "type": "header",
            "content": "End Result",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Now that the Light Actor and Level have been set up, click <strong>Play (PIE)</strong> to automatically take possession of the spectator Pawn.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You can control the spectator Pawn and navigate into the Light Actor's box component bounds.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Once the Timeline Component's Play function has been triggered, the light's color and luminosity should begin to change over a 5-second timespan.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "video",
            "video_id": "V_sNH6u1",
            "provider": "kaltura",
            "caption": "",
            "autoplay": false,
            "loop": false,
            "width": null,
            "video": {
              "height": 728,
              "width": 1286,
              "identifier": "V_sNH6u1"
            },
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "zqB",
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
