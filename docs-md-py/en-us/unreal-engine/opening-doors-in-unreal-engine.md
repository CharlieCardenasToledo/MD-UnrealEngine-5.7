# Opening Doors

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/opening-doors-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 706,
        "excerpt_assignment_id": 419,
        "blocks": [
          {
            "type": "paragraph",
            "content": "This tutorial demonstrates the use of a <strong><a href=\"programming-and-scripting/blueprints-visual-scripting/UserGuide/Timelines\">Timeline</a></strong> Blueprint to set up a proximity-based opening door.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24528061,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24528061,
              "file_name": "image_23.gif",
              "file_size": 106092,
              "content_type": "image/gif",
              "created_at": "2025-04-22T18:32:46.705+00:00",
              "height": 360,
              "width": 640,
              "storage_key": "8af6ac4f-61dc-453b-856f-ad34222763c6",
              "context": "documentation"
            },
            "storage_key": "8af6ac4f-61dc-453b-856f-ad34222763c6",
            "context": "documentation",
            "width": null,
            "autoplay": true,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Creating the Door Actor",
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
                  "content": "Create the new <strong>Blueprint</strong> project based on <strong>Blank</strong> template with <strong>Starter Content</strong> enabled, name it <strong>TimelineDoorActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528062,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528062,
                    "file_name": "01_CreateBPProject.png",
                    "file_size": 455460,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:47.051+00:00",
                    "height": 751,
                    "width": 1067,
                    "storage_key": "769de71d-f8f8-43b3-83ad-7289a3441539",
                    "context": "documentation"
                  },
                  "storage_key": "769de71d-f8f8-43b3-83ad-7289a3441539",
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
                  "content": "Navigate to <strong>Content Browser</strong> and click the <strong>Add (+)</strong> button to create a new Blueprint.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528063,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528063,
                    "file_name": "02_AddBPClass.png",
                    "file_size": 25402,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:47.318+00:00",
                    "height": 308,
                    "width": 600,
                    "storage_key": "268c78e1-81b4-496a-9c11-29485f1871fe",
                    "context": "documentation"
                  },
                  "storage_key": "268c78e1-81b4-496a-9c11-29485f1871fe",
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
                  "content": "Select <strong>Actor</strong> as a Parent Class and name created blueprint <strong>BP_DoorActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528064,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528064,
                    "file_name": "03_SelectParentClass.png",
                    "file_size": 61256,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:47.421+00:00",
                    "height": 438,
                    "width": 600,
                    "storage_key": "e6e1d111-829f-4c56-96dc-1ef047d2fa0a",
                    "context": "documentation"
                  },
                  "storage_key": "e6e1d111-829f-4c56-96dc-1ef047d2fa0a",
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
                  "content": "Double-click the <strong>BP_DoorActor</strong> from the <strong>Content Browser</strong> to open it in the <strong>Blueprint Editor</strong> and open the <strong>Class Defaults</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528065,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528065,
                    "file_name": "04_BlueprintEditor.png",
                    "file_size": 190912,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:47.499+00:00",
                    "height": 590,
                    "width": 1078,
                    "storage_key": "2b2effaf-2ef1-4331-bbb7-24bad0ab0b1e",
                    "context": "documentation"
                  },
                  "storage_key": "2b2effaf-2ef1-4331-bbb7-24bad0ab0b1e",
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
                  "content": "Next, from the <strong>Components</strong> tab click the <strong>Add</strong> button and select <strong>Static Mesh</strong> to add a new <strong>Static Mesh Component</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528066,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528066,
                    "file_name": "05_AddStaticMeshComponent.png",
                    "file_size": 19489,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:47.675+00:00",
                    "height": 290,
                    "width": 350,
                    "storage_key": "25819239-291f-4c56-abf5-1a353374ad02",
                    "context": "documentation"
                  },
                  "storage_key": "25819239-291f-4c56-abf5-1a353374ad02",
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
                  "content": "Right-click your created <strong>StaticMesh</strong> component and select <strong>Rename</strong> to rename it to <strong>DoorFrame</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528067,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528067,
                    "file_name": "06_NameStaticMeshComponent.png",
                    "file_size": 10293,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:47.737+00:00",
                    "height": 200,
                    "width": 350,
                    "storage_key": "e861b6af-5023-4575-b794-d359133b752b",
                    "context": "documentation"
                  },
                  "storage_key": "e861b6af-5023-4575-b794-d359133b752b",
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
                  "content": "Next, from the <strong>Components</strong> tab click the <strong>Add</strong> button and select <strong>Static Mesh</strong> to add a new <strong>Static Mesh Component</strong>. (Repeating step 3)",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Right-click your created <strong>StaticMesh</strong> component and select <strong>Rename</strong> to rename it to <strong>Door</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528068,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528068,
                    "file_name": "07_AddStaticMeshDoor.png",
                    "file_size": 11033,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:47.870+00:00",
                    "height": 200,
                    "width": 350,
                    "storage_key": "75a757c7-09a6-4b32-b5e0-08588e1119cb",
                    "context": "documentation"
                  },
                  "storage_key": "75a757c7-09a6-4b32-b5e0-08588e1119cb",
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
                  "content": "From the <strong>Components</strong> tab click the <strong>Add</strong> button again, select <strong>Box Collision</strong> from the dropdown menu and rename it to <strong>Box</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528069,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528069,
                    "file_name": "08_AddBoxCollision.png",
                    "file_size": 14183,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:47.957+00:00",
                    "height": 210,
                    "width": 350,
                    "storage_key": "ddabefd8-a6dc-49b3-9cbb-d93fc82eff42",
                    "context": "documentation"
                  },
                  "storage_key": "ddabefd8-a6dc-49b3-9cbb-d93fc82eff42",
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
                  "content": "Next, open the <strong>Event Graph</strong> in <strong>Blueprint Editor</strong>, <strong>right-click</strong> the <strong>Graph</strong>, search for and add <strong>Add Timeline</strong> from the action contex menu. Name your Timeline <strong>DoorTimelineComponent</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528070,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528070,
                    "file_name": "09_AddTimeLineComponent.png",
                    "file_size": 43442,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:48.041+00:00",
                    "height": 420,
                    "width": 600,
                    "storage_key": "b64e012c-4c37-4871-8539-7d906d22f999",
                    "context": "documentation"
                  },
                  "storage_key": "b64e012c-4c37-4871-8539-7d906d22f999",
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
            "content": "Setting Up the Door Static Mesh",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Next, you will need to set up the attachment hierarchy of your Components tab.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You will also need to set up the Static Mesh assets that will visually represent your DoorFrame and Door Static Mesh components.",
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
                  "content": "From the <strong>BP_DoorActor</strong>'s Components tab, select the <strong>DoorFrame</strong> static mesh and drag it over the <strong>DefaultSceneRoot</strong> component to make it the new <strong>root component</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528071,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528071,
                    "file_name": "11_DragAsRootComponent.png",
                    "file_size": 21513,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:48.171+00:00",
                    "height": 220,
                    "width": 600,
                    "storage_key": "39edc62c-4445-4b46-ad9e-10a6e049d4d7",
                    "context": "documentation"
                  },
                  "storage_key": "39edc62c-4445-4b46-ad9e-10a6e049d4d7",
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
                  "content": "Select the <strong>DoorFrame</strong> static mesh in the <strong>Components</strong> tab and from the <strong>Details</strong> panel change the <strong>Static Mesh</strong> to <strong>SM_DoorFrame</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528072,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528072,
                    "file_name": "12_SelectSMDoorFrame.png",
                    "file_size": 21357,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:48.344+00:00",
                    "height": 320,
                    "width": 350,
                    "storage_key": "a75dd6fe-26ec-4cda-a01f-01efe491ce40",
                    "context": "documentation"
                  },
                  "storage_key": "a75dd6fe-26ec-4cda-a01f-01efe491ce40",
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
                  "content": "From the <strong>Components</strong> tab select the <strong>Door</strong> component.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528073,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528073,
                    "file_name": "13_SelectDoor.png",
                    "file_size": 10350,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:48.432+00:00",
                    "height": 210,
                    "width": 350,
                    "storage_key": "fa4d449b-ce30-4dc5-8c0e-bd394b3e67a2",
                    "context": "documentation"
                  },
                  "storage_key": "fa4d449b-ce30-4dc5-8c0e-bd394b3e67a2",
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
                  "content": "Navigate to the <strong>Details</strong> panel and change the <strong>Static Mesh</strong> to <strong>SM_Door</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528074,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528074,
                    "file_name": "14_SelectSMDoor.png",
                    "file_size": 25115,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:48.698+00:00",
                    "height": 350,
                    "width": 350,
                    "storage_key": "7fd0f006-27bc-4b82-a82b-e0db194fef90",
                    "context": "documentation"
                  },
                  "storage_key": "7fd0f006-27bc-4b82-a82b-e0db194fef90",
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
                  "content": "Navigate to the <strong>Transform</strong> category and change the <strong>Y Location</strong> value to <strong>45.0</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528075,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528075,
                    "file_name": "15_TransformSettingsBP.png",
                    "file_size": 114832,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:48.764+00:00",
                    "height": 380,
                    "width": 630,
                    "storage_key": "87f7abfd-8947-4fa8-b141-6c1f8f4a0b46",
                    "context": "documentation"
                  },
                  "storage_key": "87f7abfd-8947-4fa8-b141-6c1f8f4a0b46",
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
                  "content": "Click <strong>Save </strong>and <strong>Compile</strong> to save these changes to the <strong>Bp_DoorActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528076,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528076,
                    "file_name": "26_CompileSaveButton.png",
                    "file_size": 13706,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:49.061+00:00",
                    "height": 100,
                    "width": 600,
                    "storage_key": "b7125c7c-2506-4122-b1b7-946b6b3f7802",
                    "context": "documentation"
                  },
                  "storage_key": "b7125c7c-2506-4122-b1b7-946b6b3f7802",
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
            "content": "Creating a Timeline Float Track",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "The Timeline Component requires a <a data-document-id=\"3227933\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/keys-and-curves-in-unreal-engine\">Timeline Curve</a> to describe its movement animation. Each curve can contain multiple keys that define a time and value. Curves interpolate these keys to calculate the value at any point during the Timeline.",
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
                  "content": "Double-click the <strong>DoorTimelineComponent</strong> in the <strong>Event Graph</strong> to open the <strong>Timeline Editor</strong>, then click <strong>Track &gt; Add Float Track</strong> to add a new curve to the track.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528077,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528077,
                    "file_name": "16_AddFloatTrack.png",
                    "file_size": 25292,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:49.187+00:00",
                    "height": 205,
                    "width": 710,
                    "storage_key": "d56d0067-1f18-44b7-9d06-9b5c498781c1",
                    "context": "documentation"
                  },
                  "storage_key": "d56d0067-1f18-44b7-9d06-9b5c498781c1",
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
                  "content": "Name the curve <strong>DoorRotationZ</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528078,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528078,
                    "file_name": "17_DoorRotationZCurve.png",
                    "file_size": 29457,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:49.323+00:00",
                    "height": 420,
                    "width": 710,
                    "storage_key": "bb3e3a39-efb0-42f5-9bae-2883397eee48",
                    "context": "documentation"
                  },
                  "storage_key": "bb3e3a39-efb0-42f5-9bae-2883397eee48",
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
                  "content": "Right-click to add two keys to your float curve track. One with the value <strong>(0, 0)</strong> and another with the value <strong>(5, 90)</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528079,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528079,
                    "file_name": "18_DoorRotationZCurveCoordinates.png",
                    "file_size": 35934,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:49.386+00:00",
                    "height": 420,
                    "width": 710,
                    "storage_key": "2b901492-7ef4-4e8b-8577-999cd2fb9951",
                    "context": "documentation"
                  },
                  "storage_key": "2b901492-7ef4-4e8b-8577-999cd2fb9951",
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
                  "content": "Press <strong>Shift</strong> and select both your keys, right-click, and from the <strong>Key Interpolation</strong> dropdown menu select <strong>Auto</strong> interpolation.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528080,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528080,
                    "file_name": "19_AdjustInterpolation.png",
                    "file_size": 39867,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:49.510+00:00",
                    "height": 420,
                    "width": 710,
                    "storage_key": "8420f0f5-79fc-415d-8b5f-b72d127051c7",
                    "context": "documentation"
                  },
                  "storage_key": "8420f0f5-79fc-415d-8b5f-b72d127051c7",
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
                  "content": "After all adjustment, your float track should look as following. Save your float track.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528081,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528081,
                    "file_name": "20_DoorRotationZPresentation.png",
                    "file_size": 42721,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:49.608+00:00",
                    "height": 420,
                    "width": 710,
                    "storage_key": "4f492aa1-999b-4dc7-9bfb-d73f3b383e39",
                    "context": "documentation"
                  },
                  "storage_key": "4f492aa1-999b-4dc7-9bfb-d73f3b383e39",
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
            "content": "Update Event Track Logic",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You will now need to create the update logic to rotate your Door static mesh.",
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
                  "content": "Navigate to the <strong>BP_DoorActor's Components</strong> tab, drag the <strong>Door</strong> static mesh into the <strong>Event Graph</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_VariableGet Name=&quot;K2Node_VariableGet_0&quot;\n     VariableReference=(MemberName=&quot;Door&quot;,bSelfContext=True)\n     NodePosX=1408\n     NodePosY=480\n     NodeGuid=F639C745401E942C7FF257A62DE60E71\n     CustomProperties Pin (PinId=5946646742BACD33C24E8FA068BE0F82,PinName=&quot;Door&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;object&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=Class&#39;&quot;/Script/Engine.StaticMeshComponent&quot;&#39;,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_1 4B4057124CF1E3234E8B9284FBDE48F0,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=B11D2610425FB6A669A61B9EBCD7D00F,PinName=&quot;self&quot;,PinFriendlyName=NSLOCTEXT(&quot;K2Node&quot;, &quot;Target&quot;, &quot;Target&quot;),PinType.PinCategory=&quot;object&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=BlueprintGeneratedClass&#39;&quot;/Game/Blueprints/BP_DoorActor.BP_DoorActor_C&quot;&#39;,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     End Object",
                  "lines_of_code": 8,
                  "id": 40450,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ1MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--e3328ea9b5306a25a263620f1bb03b711f4dd7b4902c2d9e501ec890295b4bc3",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Drag off the <strong>Door</strong> pin, search for and add <strong>SetRelativeRotation</strong> node from the actions context menu.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name=&quot;K2Node_CallFunction_1&quot;\n     FunctionReference=(MemberParent=Class&#39;&quot;/Script/Engine.SceneComponent&quot;&#39;,MemberName=&quot;K2_SetRelativeRotation&quot;)\n     NodePosX=1616\n     NodePosY=400\n     AdvancedPinDisplay=Hidden\n     NodeGuid=53A1DABD478618F4D9B683BB36694739\n     CustomProperties Pin (PinId=404456F84C7193707D9336B0E4A80336,PinName=&quot;execute&quot;,PinToolTip=&quot;\\nExec&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_Timeline_0 9BEFE34640037D3E43A02E9B826C77B4,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=DDA7E8E74F2D85FBC445F9A4EDCB987F,PinName=&quot;then&quot;,PinToolTip=&quot;\\nExec&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=4B4057124CF1E3234E8B9284FBDE48F0,PinName=&quot;self&quot;,PinFriendlyName=NSLOCTEXT(&quot;K2Node&quot;, &quot;Target&quot;, &quot;Target&quot;),PinToolTip=&quot;Target\\nScene Component Object Reference&quot;,PinType.PinCategory=&quot;object&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=Class&#39;&quot;/Script/Engine.SceneComponent&quot;&#39;,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_VariableGet_0 5946646742BACD33C24E8FA068BE0F82,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=CD34574448671ACA3A4EF99548D731D6,PinName=&quot;NewRotation&quot;,PinToolTip=&quot;New Rotation\\nRotator\\n\\nNew rotation of the component relative to its parent&quot;,PinType.PinCategory=&quot;struct&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=ScriptStruct&#39;&quot;/Script/CoreUObject.Rotator&quot;&#39;,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue=&quot;0, 0, 0&quot;,AutogeneratedDefaultValue=&quot;0, 0, 0&quot;,LinkedTo=(K2Node_CallFunction_2 853085C240613CE1093F039748599A8B,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n",
                  "lines_of_code": 14,
                  "id": 40451,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ1MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--78f96e1e47916fc1a66516ccdfd2259d4a5a8e09c2f2283bb2647ba1679f5960",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Right-click the <strong>Event Graph</strong>, search for and add <strong>Make Rotator</strong> node from the actions context menu.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name=&quot;K2Node_CallFunction_2&quot;\n     bIsPureFunc=True\n     FunctionReference=(MemberParent=Class&#39;&quot;/Script/Engine.KismetMathLibrary&quot;&#39;,MemberName=&quot;MakeRotator&quot;)\n     NodePosX=1360\n     NodePosY=544\n     NodeGuid=D96C6C9A4ED844DBFDED4C8FB2A22235\n     CustomProperties Pin (PinId=54E164B84AAD11DA6D2B388D156BE10C,PinName=&quot;self&quot;,PinFriendlyName=NSLOCTEXT(&quot;K2Node&quot;, &quot;Target&quot;, &quot;Target&quot;),PinToolTip=&quot;Target\\nKismet Math Library Object Reference&quot;,PinType.PinCategory=&quot;object&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=Class&#39;&quot;/Script/Engine.KismetMathLibrary&quot;&#39;,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject=&quot;/Script/Engine.Default__KismetMathLibrary&quot;,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=F346FA36478B67530C91F59587619054,PinName=&quot;Roll&quot;,PinFriendlyName=NSLOCTEXT(&quot;&quot;, &quot;080395114780BBB948664EA56BCEBCDE&quot;, &quot;X (Roll)&quot;),PinToolTip=&quot;X (Roll)\\nFloat (single-precision)&quot;,PinType.PinCategory=&quot;real&quot;,PinType.PinSubCategory=&quot;float&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue=&quot;0.0&quot;,AutogeneratedDefaultValue=&quot;0.0&quot;,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=C7C392CA42C8E8CF52EA9DA70BE4D534,PinName=&quot;Pitch&quot;,PinFriendlyName=NSLOCTEXT(&quot;&quot;, &quot;9779984143DDC05072AF75B9BF44ABB8&quot;, &quot;Y (Pitch)&quot;),PinToolTip=&quot;Y (Pitch)\\nFloat (single-precision)&quot;,PinType.PinCategory=&quot;real&quot;,PinType.PinSubCategory=&quot;float&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue=&quot;0.0&quot;,AutogeneratedDefaultValue=&quot;0.0&quot;,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=3F087F3C4D1F92FD54DD79A0D85E70B2,PinName=&quot;Yaw&quot;,PinFriendlyName=NSLOCTEXT(&quot;&quot;, &quot;9EE1C48F419DB03BEC25289BC79A55FD&quot;, &quot;Z (Yaw)&quot;),PinToolTip=&quot;Z (Yaw)\\nFloat (single-precision)&quot;,PinType.PinCategory=&quot;real&quot;,PinType.PinSubCategory=&quot;float&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue=&quot;0.0&quot;,AutogeneratedDefaultValue=&quot;0.0&quot;,LinkedTo=(K2Node_Timeline_0 D5512EC94961955B4DC7A89BC95476B4,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n",
                  "lines_of_code": 12,
                  "id": 40452,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ1MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--a3959f2ee6f649e7648ad506e22fa34ff155981644d4ff9fe4b5b676208561aa",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Connect the <strong>Door Rotation Z</strong> float pin of the <strong>DoorTimelineComponent</strong> node to the <strong>Z</strong>(<strong>Yaw</strong>) pin of the <strong>Make Rotator</strong> node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528082,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528082,
                    "file_name": "24_BPScript3.png",
                    "file_size": 69199,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:49.730+00:00",
                    "height": 290,
                    "width": 740,
                    "storage_key": "892296bb-bd66-4648-8578-0cd44f55be91",
                    "context": "documentation"
                  },
                  "storage_key": "892296bb-bd66-4648-8578-0cd44f55be91",
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
                  "content": "Connect the <strong>Update</strong> pin of the <strong>DoorTimelineComponent</strong> node to the input <strong>exec</strong> pin of the <strong>SetRelativeRotation</strong> node.  Connect the <strong>Return Value</strong> pin of the <strong>Make Rotator</strong> node to the <strong>New Rotation</strong> pin of the <strong>SetRelativeRotation</strong> node. Your Blueprint Script should look as following:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_Timeline Name=&quot;K2Node_Timeline_0&quot;\n     TimelineName=&quot;DoorTimelineComponent&quot;\n     TimelineGuid=CA17E1FC4C93F3D3F1C60FA461A6F628\n     NodePosX=1056\n     NodePosY=432\n     bCanRenameNode=True\n     NodeGuid=DB233DE34010C514EF2BB8B7FF16E8C8\n     CustomProperties Pin (PinId=D3EAEE29454A22A3868A028A5147A171,PinName=&quot;Play&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_ComponentBoundEvent_0 0F42A90B4A0FC8F6538A7A888216EAF5,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=1228CB48474D97E3962E50AF8799E5B1,PinName=&quot;PlayFromStart&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=4ABD8970456B5A2178957D84C5101C7D,PinName=&quot;Stop&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n",
                  "lines_of_code": 53,
                  "id": 40453,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ1MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--5874cda0a692069abd759d41d2117f4b8b0d0971b725a5dddf2f6321ddd99733",
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
                  "image_id": 24528083,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528083,
                    "file_name": "26_CompileSaveButton.png",
                    "file_size": 13706,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:49.931+00:00",
                    "height": 100,
                    "width": 600,
                    "storage_key": "efd7c466-9df6-490c-a830-cde00010bb0d",
                    "context": "documentation"
                  },
                  "storage_key": "efd7c466-9df6-490c-a830-cde00010bb0d",
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
            "content": "Creating Binding Box Collision Overlap Events",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "The Box component requires the ability to react when an Actor enters or leaves its collision bounds.",
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
                  "content": "Navigate to the <strong>Components</strong> tab of your <strong>BP_DoorActor</strong> and select the <strong>Box</strong> component.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528084,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528084,
                    "file_name": "27_SelectDoorComponent.png",
                    "file_size": 10303,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:50.033+00:00",
                    "height": 200,
                    "width": 350,
                    "storage_key": "837764de-2429-43d0-8a75-8ce903c3c649",
                    "context": "documentation"
                  },
                  "storage_key": "837764de-2429-43d0-8a75-8ce903c3c649",
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
                  "content": "From the <strong>Details</strong> panel, scroll down to the <strong>Events</strong> category and click the <strong>+</strong> icon next to the <strong>On Component Begin Overlap</strong> event.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528085,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528085,
                    "file_name": "28_AddEventBeginOverlap.png",
                    "file_size": 15329,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:50.155+00:00",
                    "height": 260,
                    "width": 350,
                    "storage_key": "39230b97-547e-4d6c-a034-464b0afdb72e",
                    "context": "documentation"
                  },
                  "storage_key": "39230b97-547e-4d6c-a034-464b0afdb72e",
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
                  "content": "Navigate to the <strong>Components</strong> tab of the <strong>BP_DoorActor</strong> and select the <strong>Box</strong> component.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528086,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528086,
                    "file_name": "29_SelectBoxComponent.png",
                    "file_size": 10398,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:50.313+00:00",
                    "height": 200,
                    "width": 350,
                    "storage_key": "2165d5ff-e115-4745-8fba-e3fcf368d37d",
                    "context": "documentation"
                  },
                  "storage_key": "2165d5ff-e115-4745-8fba-e3fcf368d37d",
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
                  "content": "From the <strong>Details</strong> panel, scroll down to the <strong>Events</strong> category and click <strong>+</strong> icon next to the <strong>On Component End Overlap</strong> event.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528087,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528087,
                    "file_name": "30_EventEndOverlap.png",
                    "file_size": 15738,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:50.382+00:00",
                    "height": 260,
                    "width": 350,
                    "storage_key": "529f2894-722f-4bb8-961a-a370f227600f",
                    "context": "documentation"
                  },
                  "storage_key": "529f2894-722f-4bb8-961a-a370f227600f",
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
                  "content": "Connect the <strong>exec</strong> pin of the <strong>On Component Begin Overlap(Box)</strong> node to the <strong>Play</strong> pin of the <strong>DoorTimelineComponent</strong> node. Connect the <strong>exec</strong> pin of the <strong>On Component End Overlap(Box)</strong> node to the <strong>Reverse</strong> pin of the <strong>DoorTimelineComponent</strong> node. Your Blueprint Script should look as following.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_Timeline Name=&quot;K2Node_Timeline_0&quot;\n     TimelineName=&quot;DoorTimelineComponent&quot;\n     TimelineGuid=CA17E1FC4C93F3D3F1C60FA461A6F628\n     NodePosX=1056\n     NodePosY=432\n     bCanRenameNode=True\n     NodeGuid=DB233DE34010C514EF2BB8B7FF16E8C8\n     CustomProperties Pin (PinId=D3EAEE29454A22A3868A028A5147A171,PinName=&quot;Play&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_ComponentBoundEvent_0 0F42A90B4A0FC8F6538A7A888216EAF5,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=1228CB48474D97E3962E50AF8799E5B1,PinName=&quot;PlayFromStart&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=4ABD8970456B5A2178957D84C5101C7D,PinName=&quot;Stop&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n",
                  "lines_of_code": 91,
                  "id": 40454,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ1NCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--3d6579d7e5ff6a51f4e24674a180abed21a60dbe14111d232042e9db32c49d91",
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
                  "image_id": 24528088,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528088,
                    "file_name": "26_CompileSaveButton.png",
                    "file_size": 13706,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:50.446+00:00",
                    "height": 100,
                    "width": 600,
                    "storage_key": "922279f1-838d-484f-9826-aae3148479ec",
                    "context": "documentation"
                  },
                  "storage_key": "922279f1-838d-484f-9826-aae3148479ec",
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
            "content": "Placing Your Actor into the Level",
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
                  "content": "Navigate to the <strong>Content Browser</strong>, select your <strong>BP_DoorActor</strong> and drag it to the <strong>Level</strong>. Navigate to the <strong>Detailed</strong> panel, select the <strong>Box</strong> component and adjust <strong>Location</strong> and <strong>Scale</strong> settings under <strong>Transform</strong> section as shown below.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528089,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528089,
                    "file_name": "32_DragInBPDoorActor.png",
                    "file_size": 298198,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:50.515+00:00",
                    "height": 736,
                    "width": 900,
                    "storage_key": "362371cf-3889-4095-8c36-980b180515e1",
                    "context": "documentation"
                  },
                  "storage_key": "362371cf-3889-4095-8c36-980b180515e1",
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
                  "content": "Click <strong>Play (PIE)</strong> button.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528090,
                  "caption": "Using the WASD keys, you can control your spectator Pawn. Upon navigating to the collision bounds of your DoorActor, you can observe the timeline play as the door opens. Upon exiting the bounds, you can observe it play in reverse.",
                  "alt_text": "",
                  "image": {
                    "id": 24528090,
                    "file_name": "image_23.gif",
                    "file_size": 106092,
                    "content_type": "image/gif",
                    "created_at": "2025-04-22T18:32:50.711+00:00",
                    "height": 360,
                    "width": 640,
                    "storage_key": "af2c95a5-1766-4056-a909-909a52ac5cac",
                    "context": "documentation"
                  },
                  "storage_key": "af2c95a5-1766-4056-a909-909a52ac5cac",
                  "context": "documentation",
                  "width": 720,
                  "autoplay": true,
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
            "type": "paragraph",
            "content": "<strong>BP_DoorActor</strong>",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "blueprint",
            "title": "context_graph",
            "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_Timeline Name=&quot;K2Node_Timeline_0&quot;\nTimelineName=&quot;DoorTimelineComponent&quot;\nTimelineGuid=CA17E1FC4C93F3D3F1C60FA461A6F628\nNodePosX=1056\nNodePosY=432\nbCanRenameNode=True\nNodeGuid=DB233DE34010C514EF2BB8B7FF16E8C8\nCustomProperties Pin (PinId=D3EAEE29454A22A3868A028A5147A171,PinName=&quot;Play&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_ComponentBoundEvent_0 0F42A90B4A0FC8F6538A7A888216EAF5,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\nCustomProperties Pin (PinId=1228CB48474D97E3962E50AF8799E5B1,PinName=&quot;PlayFromStart&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\nCustomProperties Pin (PinId=4ABD8970456B5A2178957D84C5101C7D,PinName=&quot;Stop&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n",
            "lines_of_code": 91,
            "id": 40455,
            "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ1NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--510ebe441b48a14c0e7a05caec0415b49235cab21e0c1f89aae03f190301182b",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "RZa",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 707,
        "excerpt_assignment_id": 420,
        "blocks": [
          {
            "type": "paragraph",
            "content": "An example C++ <strong><a href=\"programming-and-scripting/blueprints-visual-scripting/UserGuide/Timelines\">Timeline</a></strong> is used to set up a classic proximity-based opening door.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "video",
            "video_id": "V_GzQF3o",
            "provider": "kaltura",
            "caption": "",
            "autoplay": false,
            "loop": false,
            "width": null,
            "video": {
              "height": 406,
              "width": 720,
              "identifier": "V_GzQF3o"
            },
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Creating the Door Actor",
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
                  "content": "Create the new <strong>C++</strong> project based on <strong>Blank</strong> template with <strong>Starter Content</strong> enabled, name it <strong>TimelineDoorActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528091,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528091,
                    "file_name": "01_CreateCppProject.png",
                    "file_size": 455406,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:51.748+00:00",
                    "height": 751,
                    "width": 1067,
                    "storage_key": "16553dca-376a-4900-8d76-29f0a03467f3",
                    "context": "documentation"
                  },
                  "storage_key": "16553dca-376a-4900-8d76-29f0a03467f3",
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
                  "image_id": 24528092,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528092,
                    "file_name": "02_AddCppClass.png",
                    "file_size": 23063,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:52.001+00:00",
                    "height": 270,
                    "width": 600,
                    "storage_key": "d7793964-1e11-4c85-a05b-8d8c67d79be7",
                    "context": "documentation"
                  },
                  "storage_key": "d7793964-1e11-4c85-a05b-8d8c67d79be7",
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
                  "image_id": 24528093,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528093,
                    "file_name": "03_ChooseParentCppClass.png",
                    "file_size": 25068,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:52.184+00:00",
                    "height": 580,
                    "width": 946,
                    "storage_key": "85a7bf5a-6284-4c13-8ae3-f3425b84c06c",
                    "context": "documentation"
                  },
                  "storage_key": "85a7bf5a-6284-4c13-8ae3-f3425b84c06c",
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
                  "content": "Name created Actor as <strong>DoorActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528094,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528094,
                    "file_name": "04_NameCppActor.png",
                    "file_size": 32062,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:52.307+00:00",
                    "height": 580,
                    "width": 946,
                    "storage_key": "5f5c800d-9571-4fe2-a9d4-7f7d41f6c007",
                    "context": "documentation"
                  },
                  "storage_key": "5f5c800d-9571-4fe2-a9d4-7f7d41f6c007",
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
                  "content": "When new Actor is created, <strong>Visual Studio</strong> automatically  opens <code>DoorActor.h</code> and <code>DoorActor.cpp</code> files. Navigate to the <code>DoorActor.h</code> file and declare the following:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "DoorActor.h",
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
                  "id": 40456,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ1NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--81d70c19df54b05c46215839f7b52899ba448bda92ea1700a16ecb7b5d8d701c",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Next, in the <code>DoorActor</code> class definition, add the following code:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "DoorActor.h",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "protected:\n\n         //MeshComponents to represent Door assets\n         UPROPERTY(VisibleAnywhere, BlueprintReadWrite)\n         UStaticMeshComponent* DoorFrame;\n         UPROPERTY(VisibleAnywhere, BlueprintReadWrite)\n         UStaticMeshComponent* Door;\n\n         //TimelineComponent to animate Door meshes\n         UPROPERTY(VisibleAnywhere, BlueprintReadWrite)\n",
                  "lines_of_code": 15,
                  "id": 40457,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ1NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--b03c4eab1b6f1f0207ae72075c58ed2ec17f726519f84e5c526b55a1e3b4b371",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to the <code>DoorActor.cpp</code>. You will need to include the following class library to utilize your Box Component.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "DoorActor.cpp",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "#include &quot;Components/BoxComponent.h&quot;",
                  "lines_of_code": 1,
                  "id": 40458,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ1OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--3f3f4cfb9e37fb863e1b858e047a4c79a4a817e8bbb2c7eb2cfb807616799d35",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "In the constructor of your <code>ADoorActor::ADoorActor</code> declare the following:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "DoorActor.cpp",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "// Sets default values\n     ADoorActor::ADoorActor()\n     {\n         // Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n         PrimaryActorTick.bCanEverTick = true;\n\n         //Create our Default Components\n         DoorFrame = CreateDefaultSubobject&lt;UStaticMeshComponent&gt;(TEXT(&quot;DoorFrameMesh&quot;));\n         Door = CreateDefaultSubobject&lt;UStaticMeshComponent&gt;(TEXT(&quot;DoorMesh&quot;));\n         DoorTimelineComp = CreateDefaultSubobject&lt;UTimelineComponent&gt;(TEXT(&quot;DoorTimelineComp&quot;));\n",
                  "lines_of_code": 17,
                  "id": 40459,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ1OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--925b6379e78479563623b85f5c9a1d2eb30c33826e54a031d17c4e8a8806f51d",
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
                      "content": "<em>Note</em>: We keep the door's relative transform as an attachment rule, in order to manipulate it later with a custom method for our Door Actor.\n     For further documentation, see <a data-document-id=\"3584870\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/Engine/FAttachmentTransformRules?application_version=5.5\">FAttachmentTransformRules</a>.",
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
          },
          {
            "type": "header",
            "content": "Setting Up the Door Static Mesh",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You will need to set up the <strong>Static Mesh</strong> assets that will visually represent your DoorFrame and Door Static Mesh components.",
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
                  "content": "From the <strong>Content Browser</strong>, navigate to your <strong>C++ Classes folder</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528095,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528095,
                    "file_name": "05_OpenCppFolder.png",
                    "file_size": 25934,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:52.541+00:00",
                    "height": 270,
                    "width": 600,
                    "storage_key": "ce5d2e5d-69fb-4a06-a534-e0ad67b04565",
                    "context": "documentation"
                  },
                  "storage_key": "ce5d2e5d-69fb-4a06-a534-e0ad67b04565",
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
                  "content": "Right click your <strong>DoorActor</strong> class, select <strong>Create Blueprint Class based on DoorActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528096,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528096,
                    "file_name": "06_CreateBPBasedOnCpp.png",
                    "file_size": 31350,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:52.607+00:00",
                    "height": 260,
                    "width": 600,
                    "storage_key": "ebb5fc07-6cbb-4b32-82a6-885e692c638d",
                    "context": "documentation"
                  },
                  "storage_key": "ebb5fc07-6cbb-4b32-82a6-885e692c638d",
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
                  "content": "Name your Blueprint Actor <strong>Bp_DoorActor</strong> and place it in appropriate folder.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528097,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528097,
                    "file_name": "07_NamePlaceBPActor.png",
                    "file_size": 30221,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:52.700+00:00",
                    "height": 520,
                    "width": 946,
                    "storage_key": "7829189c-2502-479a-8d6e-0ce0a267d5c2",
                    "context": "documentation"
                  },
                  "storage_key": "7829189c-2502-479a-8d6e-0ce0a267d5c2",
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
                  "content": "From the <strong>Components</strong> tab, select the <strong>DoorFrame</strong> Static Mesh component.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528098,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528098,
                    "file_name": "08_SelectDoorFrameCom.png",
                    "file_size": 16445,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:52.782+00:00",
                    "height": 200,
                    "width": 400,
                    "storage_key": "9d690f91-0da4-44f3-98a8-ea53e647f363",
                    "context": "documentation"
                  },
                  "storage_key": "9d690f91-0da4-44f3-98a8-ea53e647f363",
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
                  "content": "Navigate to the <strong>Details panel</strong> and change the <strong>Static Mesh</strong> to <strong>SM_DoorFrame</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528099,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528099,
                    "file_name": "09_SelectSMDoorFrame.png",
                    "file_size": 31204,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:52.953+00:00",
                    "height": 366,
                    "width": 400,
                    "storage_key": "989ed7ef-dff8-4022-bf8c-bce785bd835e",
                    "context": "documentation"
                  },
                  "storage_key": "989ed7ef-dff8-4022-bf8c-bce785bd835e",
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
                  "content": "Navigate to the <strong>Components</strong> tab, select the <strong>DoorMesh</strong> component.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528100,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528100,
                    "file_name": "10_SelectDoorComponent.png",
                    "file_size": 16701,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:53.070+00:00",
                    "height": 200,
                    "width": 400,
                    "storage_key": "dd2c6e48-f119-4d1b-b0a8-11fb92a91f78",
                    "context": "documentation"
                  },
                  "storage_key": "dd2c6e48-f119-4d1b-b0a8-11fb92a91f78",
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
                  "content": "From the <strong>Details</strong> panel change the <strong>Static Mesh</strong> to <strong>SM_Door</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528101,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528101,
                    "file_name": "11_SelectSMDoor.png",
                    "file_size": 35895,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:53.198+00:00",
                    "height": 400,
                    "width": 400,
                    "storage_key": "c1cb7d28-9899-45fa-acce-030cc2ae6e38",
                    "context": "documentation"
                  },
                  "storage_key": "c1cb7d28-9899-45fa-acce-030cc2ae6e38",
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
                  "content": "Then navigate to the <strong>Transform</strong> category and change the <strong>Y Location</strong> value to <strong>45.0</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528102,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528102,
                    "file_name": "12_TransformSettingsBP.png",
                    "file_size": 116976,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:53.307+00:00",
                    "height": 380,
                    "width": 600,
                    "storage_key": "ee0d35ee-d1b3-41d3-ba80-1fa0dbcae1e3",
                    "context": "documentation"
                  },
                  "storage_key": "ee0d35ee-d1b3-41d3-ba80-1fa0dbcae1e3",
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
                  "image_id": 24528103,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528103,
                    "file_name": "13_CompileSaveButton.png",
                    "file_size": 13706,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:53.461+00:00",
                    "height": 100,
                    "width": 600,
                    "storage_key": "572f6135-0bea-4899-82ee-f3b3e0c0b3ca",
                    "context": "documentation"
                  },
                  "storage_key": "572f6135-0bea-4899-82ee-f3b3e0c0b3ca",
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
            "content": "Creating UCurveFloat and Timeline Event Tracks",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "The Timeline Component requires a <a data-document-id=\"3227933\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/keys-and-curves-in-unreal-engine\">Timeline Curve</a>. Each curve can contain multiple  keys that define a time and value.Curves interpolate these keys to calculate the value at any point during the Timeline.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "For this example, we will be using a <a data-document-id=\"3582655\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/Curves/UCurveFloat?application_version=5.5\">UCurveFloat</a>.",
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
                  "content": "Navigate to the <code>ADoorActor</code> class definition in <code>DoorActor.h</code> and declare the following variables:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "DoorActor.h",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "public:\n         // Variable to hold the Curve asset\n         UPROPERTY(EditAnywhere)\n         UCurveFloat* DoorTimelineFloatCurve;\n\n     private:\n         //Float Track Signature to handle our update track event\n         FOnTimelineFloat UpdateFunctionFloat;\n\n         //Function which updates our Door&#39;s relative location with the timeline graph\n",
                  "lines_of_code": 12,
                  "id": 40460,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ2MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--d5762820394e6e1b0d299d8cc183f38d806cb1c8f72abc89579606d333eadc2e",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to <code>DoorActor.cpp</code> and implement the <code>UpdateTimelineComp</code> method:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "DoorActor.cpp",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void ADoorActor::UpdateTimelineComp(float Output)\n     {\n         // Create and set our Door&#39;s new relative location based on the output from our Timeline Curve\n         FRotator DoorNewRotation = FRotator(0.0f, Output, 0.f);\n         Door-&gt;SetRelativeRotation(DoorNewRotation);\n     }",
                  "lines_of_code": 6,
                  "id": 40461,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ2MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--aee6aecdbc2028919d73f44bd502645ee6f5a6c4a076ffc2ce61236b0b86c698",
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
                  "content": "DoorActor.cpp",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "//Binding our float track to our UpdateTimelineComp Function&#39;s output\n     UpdateFunctionFloat.BindDynamic(this, &amp;ADoorActor::UpdateTimelineComp);\n\n     //If we have a float curve, bind it&#39;s graph to our update function\n     if (DoorTimelineFloatCurve)\n     {\n        DoorTimelineComp-&gt;AddInterpFloat(DoorTimelineFloatCurve, UpdateFunctionFloat);\n     }",
                  "lines_of_code": 8,
                  "id": 40462,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ2MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--4cfeefda35637d8a1637fca6320dcbdfc18923375485052153f8279d600b45c6",
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
            "content": "Work-In-Progress Code",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "DoorActor.h",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "// Copyright 1998-2022 Epic Games, Inc. All Rights Reserved.\n\t#pragma once\n\t#include &quot;Components/TimelineComponent.h&quot;\n\t#include &quot;CoreMinimal.h&quot;\n\t#include &quot;GameFramework/Actor.h&quot;\n\t#include &quot;DoorActor.generated.h&quot;\n\n\tUCLASS()\n\tclass TIMELINEDOORACTOR_API ADoorActor : public AActor\n\t{\n",
            "lines_of_code": 53,
            "id": 40463,
            "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ2MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--27fc99286406a2ecb9412a93ddeb2c46e688c28a1475c861ac8ce9e0327f5c98",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "DoorActor.cpp",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "//Copyright 1998-2022 Epic Games, Inc. All Rights Reserved.\n\n\t#include &quot;DoorActor.h&quot;\n\t#include &quot;Components/BoxComponent.h&quot;\n\n\t// Sets default values\n\tADoorActor::ADoorActor()\n\t{\n\t\t// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n\t\tPrimaryActorTick.bCanEverTick = true;\n",
            "lines_of_code": 51,
            "id": 40464,
            "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ2NCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--6b80b5f6cc48426c77d9953ba75364d2e979233eb1c38b4d45a0a9c24e6c4b4b",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Creating and Binding Collision Overlap Events",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "The Box Component requires the ability to react when an Actor enters or leaves its collision bounds.",
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
                  "content": "Navigate to the class definition of your <code>DoorActor.h</code> file and declare the following:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "DoorActor.h",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "// Begin and End Overlap Events for our DoorProxVolume\n     UFUNCTION()\n     void OnOverlapBegin(class UPrimitiveComponent* OverlappedComp, class AActor* OtherActor, class UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult&amp; SweepResult);\n\n     UFUNCTION()\n     void OnOverlapEnd(class UPrimitiveComponent* OverlappedComp, class AActor* OtherActor, class UPrimitiveComponent* OtherComp, int32 OtherBodyIndex);",
                  "lines_of_code": 6,
                  "id": 40465,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ2NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--4cb97072f06f0eec9e9bba89119defa30451689a8d171b86e811a2269b26e383",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Next, navigate to your <code>DoorActor.cpp</code> file to implement your <code>OnOverlapBegin</code> and <code>OnOverlapEnd</code> class methods:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "DoorActor.cpp",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void ADoorActor::OnOverlapBegin(UPrimitiveComponent * OverlappedComp, AActor * OtherActor, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult &amp; SweepResult)\n     {\n         DoorTimelineComp-&gt;Play();\n     }\n\n     void ADoorActor::OnOverlapEnd(UPrimitiveComponent * OverlappedComp, AActor * OtherActor, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex)\n     {\n         DoorTimelineComp-&gt;Reverse();\n     }",
                  "lines_of_code": 9,
                  "id": 40466,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ2NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--a3cca4495d8d84b41719c92388cf17e6e1e87d10f906d16e568adb20e9e3bfe8",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Bind your overlap functions in the <code>BeginPlay</code> method, as following:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "DoorActor.cpp",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void ADoorActor::BeginPlay()\n     {\n         Super::BeginPlay();\n\n         //Binding our float track to our UpdateTimelineComp Function&#39;s output\n         UpdateFunctionFloat.BindDynamic(this, &amp;ADoorActor::UpdateTimelineComp);\n\n         //If we have a float curve, bind it&#39;s graph to our update function\n         if (DoorTimelineFloatCurve)\n         {\n",
                  "lines_of_code": 17,
                  "id": 40467,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ2NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--16a1fb103f8c4421dabd3b95be6fd30b8fa3e15ef67a5f340a56084a743e6245",
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
            "content": "Creating a Curve Asset in the Unreal Editor",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You must create a <strong>Curve Asset</strong> in the <strong>Unreal Editor</strong> to assign it to your Timeline Actor Blueprint.",
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
                  "image_id": 24528104,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528104,
                    "file_name": "14_AddCurveAsset.png",
                    "file_size": 60066,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:53.535+00:00",
                    "height": 451,
                    "width": 600,
                    "storage_key": "94f94f8c-14e7-4b9f-b71c-3e5d34712d2e",
                    "context": "documentation"
                  },
                  "storage_key": "94f94f8c-14e7-4b9f-b71c-3e5d34712d2e",
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
                  "content": "Select <strong>CurveFloat</strong> and name the Asset <strong>DoorCurveFloat</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528105,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528105,
                    "file_name": "15_ParentClassFloatCurve.png",
                    "file_size": 18627,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:53.708+00:00",
                    "height": 294,
                    "width": 600,
                    "storage_key": "b179ae03-d970-401c-b9c8-9d41b24c0957",
                    "context": "documentation"
                  },
                  "storage_key": "b179ae03-d970-401c-b9c8-9d41b24c0957",
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
                  "content": "Double-click created <strong>DoorCurveFloat</strong> to open the <strong>Timeline Editor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Add two keys to the Float Curve, by right clicking on the <strong>Graph</strong>, then select <strong>Add Key</strong>. Adjust time-value of the first key to the <strong>(0, 0)</strong>. Adjust time-value of the second key to the <strong>(4, 90)</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528106,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528106,
                    "file_name": "16_DoorCurveFloatCoords.png",
                    "file_size": 36180,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:53.888+00:00",
                    "height": 450,
                    "width": 750,
                    "storage_key": "de5198c0-9ecb-4fed-8ffd-f4291a3c5d79",
                    "context": "documentation"
                  },
                  "storage_key": "de5198c0-9ecb-4fed-8ffd-f4291a3c5d79",
                  "context": "documentation",
                  "width": 600,
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
                      "content": "For more information on editing <strong>Timeline</strong> curves, see <a data-document-id=\"3227933\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/keys-and-curves-in-unreal-engine\">Keys and Curves</a>.",
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
                  "content": "Press <strong>Shift</strong> and click to select both your keys, right click on the <strong>Graph</strong> and set them to <strong>Auto</strong> interpolation.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528107,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528107,
                    "file_name": "17_DoorCurveFloatInterp.png",
                    "file_size": 41444,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:54.009+00:00",
                    "height": 450,
                    "width": 750,
                    "storage_key": "11d8a328-9b33-43e5-bee1-01180bc2a0a2",
                    "context": "documentation"
                  },
                  "storage_key": "11d8a328-9b33-43e5-bee1-01180bc2a0a2",
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
                  "content": "Your Curve now should look as following. Save your <strong>DoorCuveFloat</strong> and close <strong>Timeline Editor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528108,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528108,
                    "file_name": "18_DoorCurveFloat.png",
                    "file_size": 38571,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:54.154+00:00",
                    "height": 450,
                    "width": 750,
                    "storage_key": "efa3df1d-e9fa-42c7-beb7-2c76979fb28c",
                    "context": "documentation"
                  },
                  "storage_key": "efa3df1d-e9fa-42c7-beb7-2c76979fb28c",
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
                  "content": "Open your <strong>Bp_DoorActor</strong> and select the <strong>Bp_DoorActor</strong> from the <strong>Components</strong> tab.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528109,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528109,
                    "file_name": "19_Select_BPDoorActor.png",
                    "file_size": 14953,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:54.249+00:00",
                    "height": 200,
                    "width": 350,
                    "storage_key": "2fa63d46-d20b-46c6-8fbe-fc3fc0d5e1cb",
                    "context": "documentation"
                  },
                  "storage_key": "2fa63d46-d20b-46c6-8fbe-fc3fc0d5e1cb",
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
                  "content": "Navigate to the <strong>Details</strong> panel and select <strong>DoorCurveFloat</strong> from the <strong>Door Timeline Float Curve</strong> dropdown menu of the <strong>Door Action</strong> section.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528110,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528110,
                    "file_name": "20_SelectCurveAsset.png",
                    "file_size": 24071,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:32:54.347+00:00",
                    "height": 338,
                    "width": 450,
                    "storage_key": "4d89235f-3ec6-458f-b7e5-54caa3d2d137",
                    "context": "documentation"
                  },
                  "storage_key": "4d89235f-3ec6-458f-b7e5-54caa3d2d137",
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
                  "content": "Navigate to the <strong>Content Browser</strong> and place the <strong>Bp_DoorActor</strong> into the <strong>Level</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Compile and Save, then press PIE.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "video",
                  "video_id": "V_2PfTKI",
                  "provider": "kaltura",
                  "caption": "",
                  "autoplay": false,
                  "loop": false,
                  "width": null,
                  "video": {
                    "height": 406,
                    "width": 720,
                    "identifier": "V_2PfTKI"
                  },
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "<em>Using input with WASD, you can control your spectator Pawn. Upon navigating to the collision bounds of your DoorActor, you can observe the timeline play, and upon exiting the bounds, you can observe it play in reverse.</em>",
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
            "content": "DoorActor.h",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "// Copyright 1998-2022 Epic Games, Inc. All Rights Reserved.\n\n\t#pragma once\n\t#include &quot;Components/TimelineComponent.h&quot;\n\t#include &quot;CoreMinimal.h&quot;\n\t#include &quot;GameFramework/Actor.h&quot;\n\t#include &quot;DoorActor.generated.h&quot;\n\n\tUCLASS()\n\tclass TIMELINEDOORACTOR_API ADoorActor : public AActor\n",
            "lines_of_code": 61,
            "id": 40468,
            "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ2OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--e85c5597f8992c89edff7c93a68a3113ab202973a0f8258368fe903b9e169e3c",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "DoorActor.cpp",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "// Copyright 1998-2022 Epic Games, Inc. All Rights Reserved.\n\n\t#include &quot;DoorActor.h&quot;\n\t#include &quot;Components/BoxComponent.h&quot;\n\n\t// Sets default values\n\tADoorActor::ADoorActor()\n\t{\n\t\t// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n\t\tPrimaryActorTick.bCanEverTick = true;\n",
            "lines_of_code": 64,
            "id": 40469,
            "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ2OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjUwKzAwOjAwIn0=--48942d345c8e042a72e2c9ccd953d50740a05250c297286d060656b0fcf8cfd1",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "PQX",
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
