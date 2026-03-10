# Event Dispatchers and Delegates Quick Start Guide

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/event-dispatchers-and-delegates-quick-start-guide-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1723,
        "excerpt_assignment_id": 1433,
        "blocks": [
          {
            "type": "header",
            "content": "Overview",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Event Dispatchers are an Actor communication method where one Actor dispatches an event and other Actors that are listening to that event are notified.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Using this method, the notifying Actor creates an <strong>Event Dispatcher</strong> to which the listening Actors subscribe. This communication method uses a one to many relationship, where the working Actor triggers the Event Dispatcher and many listening Actors are notified.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Goals",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this Quick Start guide, you will learn how to use Event Dispatchers to create an <strong>OnBossDied </strong>event that will trigger on two Actors in your Level.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Objectives",
            "level": 2,
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
                  "content": "Create the <strong>BossDied </strong>Actor that will create the Event Dispatcher.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Create a door Actor that will bind to the <strong>OnBossDied </strong>event.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Modify the <strong>Blueprint_Effect_Explosion </strong>Blueprint to bind to the <strong>OnBossDied </strong>event.",
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
            "content": "1 - Required Setup",
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
                  "content": "In the <strong>New Project Categories</strong> section of the menu, select <strong>Games</strong> and click <strong>Next</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741264,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741264,
                    "file_name": "image_0.png",
                    "file_size": 80765,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:44.767+00:00",
                    "height": 774,
                    "width": 1110,
                    "storage_key": "b96d39a7-4069-4b8a-a5b9-1248c0038ea4",
                    "context": "documentation"
                  },
                  "storage_key": "b96d39a7-4069-4b8a-a5b9-1248c0038ea4",
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
                  "content": "Select the <strong>Third Person</strong> template and click <strong>Next</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741265,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741265,
                    "file_name": "image_1.png",
                    "file_size": 228409,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:45.049+00:00",
                    "height": 774,
                    "width": 1110,
                    "storage_key": "1a907c18-45b2-4485-bf22-2848c8a7f194",
                    "context": "documentation"
                  },
                  "storage_key": "1a907c18-45b2-4485-bf22-2848c8a7f194",
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
                  "content": "Select the <strong>Blueprint </strong>and <strong>With Starter Content</strong> options and click <strong>Create Project</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741266,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741266,
                    "file_name": "image_2.png",
                    "file_size": 70174,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:45.299+00:00",
                    "height": 774,
                    "width": 1110,
                    "storage_key": "8fd9e1be-5f26-4f25-93e0-aa1dc89b9700",
                    "context": "documentation"
                  },
                  "storage_key": "8fd9e1be-5f26-4f25-93e0-aa1dc89b9700",
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
            "content": "Section Results",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You have created a new Third Person project and are now ready to learn about Event Dispatchers.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "2 -  Creating the OnBossDied Event",
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
                  "content": "Right-click the <strong>Content Browser</strong> and click <strong>Blueprint Class </strong>under the<strong> Create Basic Asset </strong>section.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741267,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741267,
                    "file_name": "image_3.png",
                    "file_size": 27090,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:45.380+00:00",
                    "height": 610,
                    "width": 283,
                    "storage_key": "97e2abed-ec45-47ef-b467-1cc0ad0f4fa0",
                    "context": "documentation"
                  },
                  "storage_key": "97e2abed-ec45-47ef-b467-1cc0ad0f4fa0",
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
                  "content": "Select <strong>Actor </strong>class as your Parent Class and name the Blueprint <strong>BP_BossDied</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741268,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741268,
                    "file_name": "image_4.png",
                    "file_size": 49211,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:45.477+00:00",
                    "height": 442,
                    "width": 544,
                    "storage_key": "14efa038-7c93-4f66-8a24-4a2ff588d0c6",
                    "context": "documentation"
                  },
                  "storage_key": "14efa038-7c93-4f66-8a24-4a2ff588d0c6",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741269,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741269,
                    "file_name": "image_5.png",
                    "file_size": 9056,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:45.568+00:00",
                    "height": 174,
                    "width": 118,
                    "storage_key": "a6f331e0-791b-4438-ba07-66a4d5d82098",
                    "context": "documentation"
                  },
                  "storage_key": "a6f331e0-791b-4438-ba07-66a4d5d82098",
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
                  "content": "Open <strong>BP_BossDied </strong>in the Blueprint editor and from the <strong>Viewport</strong>, click the <strong>Add Component</strong> button then search for and select <strong>Box Collision</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741270,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741270,
                    "file_name": "image_6.png",
                    "file_size": 9081,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:45.674+00:00",
                    "height": 118,
                    "width": 381,
                    "storage_key": "f160f2b7-8d00-42c6-a74f-c22ac3ab6bbd",
                    "context": "documentation"
                  },
                  "storage_key": "f160f2b7-8d00-42c6-a74f-c22ac3ab6bbd",
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
                  "content": "With the <strong>Box </strong>collision selected, change the scale to X = <strong>4</strong>, Y = <strong>4</strong>, and Z = <strong>2</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741271,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741271,
                    "file_name": "image_7.png",
                    "file_size": 10604,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:45.769+00:00",
                    "height": 133,
                    "width": 619,
                    "storage_key": "bef7901c-afb0-48c3-84ef-41063614b1eb",
                    "context": "documentation"
                  },
                  "storage_key": "bef7901c-afb0-48c3-84ef-41063614b1eb",
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
                  "content": "With the <strong>Box </strong>collision selected, go to the <strong>Rendering </strong>section of the <strong>Details </strong>panel and deselect the <strong>Hidden in Game checkbox</strong>. This will display the collision box during gameplay.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741272,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741272,
                    "file_name": "image_8.png",
                    "file_size": 3012,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:45.876+00:00",
                    "height": 85,
                    "width": 343,
                    "storage_key": "5dc3259c-5a9b-44e5-ae30-d32bf5035f20",
                    "context": "documentation"
                  },
                  "storage_key": "5dc3259c-5a9b-44e5-ae30-d32bf5035f20",
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
                  "content": "Right-click the <strong>Box </strong>collision and select <strong>Add OnComponentBeginOverlap</strong>. You will see the node added to the <strong>Event Graph</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741273,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741273,
                    "file_name": "image_9.png",
                    "file_size": 37724,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:45.946+00:00",
                    "height": 307,
                    "width": 517,
                    "storage_key": "a323c1f9-1f6e-419d-a59f-d7dd85471d0a",
                    "context": "documentation"
                  },
                  "storage_key": "a323c1f9-1f6e-419d-a59f-d7dd85471d0a",
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
                  "content": "From the <strong>My Blueprint</strong> panel on the left, navigate to the <strong>Event Dispatchers</strong> section and click  <strong>+ Add New </strong>to add a new event. Name this event <strong>OnBossDied</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741274,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741274,
                    "file_name": "image_10.png",
                    "file_size": 2989,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:46.086+00:00",
                    "height": 53,
                    "width": 382,
                    "storage_key": "55a3fe3b-26ad-4c84-95d4-36ccbf076c17",
                    "context": "documentation"
                  },
                  "storage_key": "55a3fe3b-26ad-4c84-95d4-36ccbf076c17",
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
                  "content": "Drag <strong>OnBossDied </strong>to the <strong>Event Graph</strong> and select <strong>Call </strong>to add the node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741275,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741275,
                    "file_name": "image_11.png",
                    "file_size": 27932,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:46.173+00:00",
                    "height": 239,
                    "width": 400,
                    "storage_key": "ba7324dc-4cca-43f1-a7e0-3d0fb6d1f7be",
                    "context": "documentation"
                  },
                  "storage_key": "ba7324dc-4cca-43f1-a7e0-3d0fb6d1f7be",
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
                  "content": "Connect the <strong>On Component Begin Overlap</strong> node to the <strong>Call OnBossDied</strong> node. <strong>Compile </strong>and <strong>Save </strong>the Blueprint.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741276,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741276,
                    "file_name": "image_12.png",
                    "file_size": 37725,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:46.284+00:00",
                    "height": 249,
                    "width": 507,
                    "storage_key": "5192e278-c237-4dba-9b10-21c3b36140fb",
                    "context": "documentation"
                  },
                  "storage_key": "5192e278-c237-4dba-9b10-21c3b36140fb",
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
                  "content": "Drag the <strong>BP_BossDied </strong>Blueprint into the Level.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741277,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741277,
                    "file_name": "image_13.png",
                    "file_size": 916212,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:46.415+00:00",
                    "height": 1041,
                    "width": 1609,
                    "storage_key": "e747b5f8-06cc-476b-a58c-dac30d9fe367",
                    "context": "documentation"
                  },
                  "storage_key": "e747b5f8-06cc-476b-a58c-dac30d9fe367",
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
            "content": "Section Results",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this section you created the <strong>BP_BossDied </strong>Actor to simulate what would happen if a boss character died in your game. In this Actor you created the <strong>OnBossDied </strong>Event Dispatcher which will be used to signal to other Actors when this event is triggered.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "3 - Creating an Interactive Door",
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
                  "content": "Right-click the <strong>Content Browser</strong> and click <strong>Blueprint Class </strong>under the<strong> Create Basic Asset </strong>section.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741278,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741278,
                    "file_name": "image_14.png",
                    "file_size": 27090,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:46.647+00:00",
                    "height": 610,
                    "width": 283,
                    "storage_key": "c040c4f9-7345-4dae-9d34-9aadcb3df7db",
                    "context": "documentation"
                  },
                  "storage_key": "c040c4f9-7345-4dae-9d34-9aadcb3df7db",
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
                  "content": "Select the <strong>Actor </strong>class as your Parent Class and name the Blueprint <strong>BP_BossDoor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741279,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741279,
                    "file_name": "image_15.png",
                    "file_size": 49211,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:46.937+00:00",
                    "height": 442,
                    "width": 544,
                    "storage_key": "7aaa33cb-9a81-4fe1-9ee5-49f06a2862a2",
                    "context": "documentation"
                  },
                  "storage_key": "7aaa33cb-9a81-4fe1-9ee5-49f06a2862a2",
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
                  "content": "Open <strong>BP_BossDoor </strong>and from the <strong>Viewport </strong>click the <strong>Add Component</strong> dropdown then search for and select <strong>Static Mesh</strong>. Name the component <strong>Frame</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741280,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741280,
                    "file_name": "image_16.png",
                    "file_size": 14692,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:47.052+00:00",
                    "height": 194,
                    "width": 382,
                    "storage_key": "637ef1f9-0910-46ba-8360-0168032dcf3c",
                    "context": "documentation"
                  },
                  "storage_key": "637ef1f9-0910-46ba-8360-0168032dcf3c",
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
                  "content": "Add another <strong>Static Mesh </strong>component and name it <strong>Door</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Select the <strong>Frame </strong>component and from the <strong>Details </strong>panel click the <strong>Static Mesh</strong> dropdown then search for and select <strong>SM_DoorFrame</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741281,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741281,
                    "file_name": "image_17.png",
                    "file_size": 20502,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:47.227+00:00",
                    "height": 244,
                    "width": 623,
                    "storage_key": "9e88895e-655d-41e2-9e4f-e957f1e8d2c5",
                    "context": "documentation"
                  },
                  "storage_key": "9e88895e-655d-41e2-9e4f-e957f1e8d2c5",
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
                  "content": "Repeat the step above for the <strong>Door </strong>component and add the <strong>SM_Door </strong>static mesh.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "With the <strong>Door </strong>component still selected, set the <strong>Y</strong> location to 45 as seen below. You should see the door aligned with the frame.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741282,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741282,
                    "file_name": "image_18.png",
                    "file_size": 10716,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:47.334+00:00",
                    "height": 136,
                    "width": 614,
                    "storage_key": "57acc793-5b56-48ff-be65-ce284efe0f58",
                    "context": "documentation"
                  },
                  "storage_key": "57acc793-5b56-48ff-be65-ce284efe0f58",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741283,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741283,
                    "file_name": "image_19.png",
                    "file_size": 110248,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:47.423+00:00",
                    "height": 446,
                    "width": 364,
                    "storage_key": "8e36368f-1475-40f2-bf2b-298b8107d8f1",
                    "context": "documentation"
                  },
                  "storage_key": "8e36368f-1475-40f2-bf2b-298b8107d8f1",
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
                  "content": "Right-click the <strong>Event Graph</strong> then search for and select <strong>Add Custom Event</strong>. Name the event <strong>OpenDoor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741284,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741284,
                    "file_name": "image_20.png",
                    "file_size": 7785,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:47.635+00:00",
                    "height": 118,
                    "width": 432,
                    "storage_key": "004a514d-f09a-4065-a11d-eb8c0acdeff7",
                    "context": "documentation"
                  },
                  "storage_key": "004a514d-f09a-4065-a11d-eb8c0acdeff7",
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
                  "content": "Drag from the <strong>OpenDoor </strong>event then search for and select <strong>Add Timeline</strong>. Name the Timeline <strong>TM_Door</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741285,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741285,
                    "file_name": "image_21.png",
                    "file_size": 37247,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:47.730+00:00",
                    "height": 291,
                    "width": 498,
                    "storage_key": "1af33987-f4d4-4bb2-9c42-071415808a45",
                    "context": "documentation"
                  },
                  "storage_key": "1af33987-f4d4-4bb2-9c42-071415808a45",
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
                  "content": "Double-click <strong>TM_Door </strong>to open it. Click on the <strong>Add Float Curve </strong> button to add a Float Track and name it <strong>Alpha</strong>. Set the length to <strong>1.0</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741286,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741286,
                    "file_name": "image_22.png",
                    "file_size": 119596,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:47.854+00:00",
                    "height": 395,
                    "width": 871,
                    "storage_key": "d1a3dd71-182b-4dee-8fda-bc4c7c0567b4",
                    "context": "documentation"
                  },
                  "storage_key": "d1a3dd71-182b-4dee-8fda-bc4c7c0567b4",
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
                  "content": "Right-click the graph and select <strong>Add key to CurveFloat_1 </strong>to add a new point. Set the <strong>Time </strong>and <strong>Value </strong>to <strong>0.0</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741287,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741287,
                    "file_name": "image_23.png",
                    "file_size": 5183,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:48.080+00:00",
                    "height": 111,
                    "width": 256,
                    "storage_key": "11501c32-3705-43f2-a5a8-45163db7ade6",
                    "context": "documentation"
                  },
                  "storage_key": "11501c32-3705-43f2-a5a8-45163db7ade6",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741288,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741288,
                    "file_name": "image_24.png",
                    "file_size": 2897,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:48.145+00:00",
                    "height": 53,
                    "width": 275,
                    "storage_key": "b4916dbc-798f-4c3f-8e05-51a8b40772d7",
                    "context": "documentation"
                  },
                  "storage_key": "b4916dbc-798f-4c3f-8e05-51a8b40772d7",
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
                  "content": "Repeat the steps above to add another point with <strong>Time </strong>and <strong>Value </strong>set to <strong>1.0</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Go back to the <strong>Event Graph</strong> and drag the <strong>Door </strong>Static Mesh component into the <strong>Event Graph</strong> to create a node. Drag from the <strong>Door </strong>node then search for and select <strong>SetRelativeRotation</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741289,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741289,
                    "file_name": "image_25.png",
                    "file_size": 68381,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:48.218+00:00",
                    "height": 304,
                    "width": 1135,
                    "storage_key": "4afcbe96-3e74-4259-80b5-6ce15d10ff76",
                    "context": "documentation"
                  },
                  "storage_key": "4afcbe96-3e74-4259-80b5-6ce15d10ff76",
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
                  "content": "Connect the <strong>Update </strong>pin from <strong>TM_Door </strong>to the <strong>SetRelativeRotation </strong>node. Right-click the <strong>New Rotation</strong> pin and select <strong>Split Struct Pin</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741290,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741290,
                    "file_name": "image_26.png",
                    "file_size": 83316,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:48.330+00:00",
                    "height": 337,
                    "width": 984,
                    "storage_key": "4fa724bf-e206-493d-90c3-9603bfdf413e",
                    "context": "documentation"
                  },
                  "storage_key": "4fa724bf-e206-493d-90c3-9603bfdf413e",
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
                  "content": "Right-click the <strong>Event Graph</strong> then search for and select <strong>Lerp Float</strong>. Connect the <strong>Return Value</strong> to the <strong>Yaw </strong>pin on the <strong>SetRelativeRotation </strong>node. Connect the <strong>Alpha </strong>pin from <strong>TM_Door </strong>to the <strong>Alpha </strong>pin on the <strong>Lerp </strong>node. Lastly, set the value of <strong>B</strong> to <strong>90.0</strong> as shown below.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741291,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741291,
                    "file_name": "image_27.png",
                    "file_size": 94813,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:48.509+00:00",
                    "height": 305,
                    "width": 1014,
                    "storage_key": "25185eae-68da-49e7-b474-9006cccc8daa",
                    "context": "documentation"
                  },
                  "storage_key": "25185eae-68da-49e7-b474-9006cccc8daa",
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
                  "content": "Add a new variable by clicking the <strong>+ button </strong>next to the<strong> Variable </strong>section. Name the variable <strong>BossDiedReference</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741292,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741292,
                    "file_name": "image_28.png",
                    "file_size": 6467,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:48.676+00:00",
                    "height": 99,
                    "width": 390,
                    "storage_key": "181e9dfb-1d74-4f6d-9b95-45729d03d8eb",
                    "context": "documentation"
                  },
                  "storage_key": "181e9dfb-1d74-4f6d-9b95-45729d03d8eb",
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
                  "content": "On the <strong>Details </strong>panel click the <strong>Variable Type</strong> dropdown then search for and select the <strong>Object Reference</strong> of <strong>BP_BossDied</strong>. Check the <strong>Instance Editable</strong> checkbox.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741293,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741293,
                    "file_name": "image_29.png",
                    "file_size": 19455,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:48.822+00:00",
                    "height": 224,
                    "width": 515,
                    "storage_key": "5e4340c7-6aa4-4f38-a50f-9933d3bbeda6",
                    "context": "documentation"
                  },
                  "storage_key": "5e4340c7-6aa4-4f38-a50f-9933d3bbeda6",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741294,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741294,
                    "file_name": "image_30.png",
                    "file_size": 7583,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:48.909+00:00",
                    "height": 116,
                    "width": 369,
                    "storage_key": "a9dbb02a-be9d-44da-b1e1-37fa0c9abf7f",
                    "context": "documentation"
                  },
                  "storage_key": "a9dbb02a-be9d-44da-b1e1-37fa0c9abf7f",
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
                  "content": "Drag <strong>BossDiedReference </strong>to the <strong>Event Graph</strong> and select <strong>Get BossDiedRerence</strong>. From the node, drag then search for and select <strong>Bind Event to On Boss Died</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741295,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741295,
                    "file_name": "image_31.png",
                    "file_size": 34618,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:48.976+00:00",
                    "height": 171,
                    "width": 801,
                    "storage_key": "38f72e1e-0213-4b4c-87d1-edf084cb1fdb",
                    "context": "documentation"
                  },
                  "storage_key": "38f72e1e-0213-4b4c-87d1-edf084cb1fdb",
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
                  "content": "From the red <strong>Event </strong>pin of <strong>Bind Event to On Boss Died,</strong> drag then search for and select <strong>Add Custom Event</strong>. Name the event <strong>BossDied</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741296,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741296,
                    "file_name": "image_32.png",
                    "file_size": 42495,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:49.059+00:00",
                    "height": 248,
                    "width": 686,
                    "storage_key": "439a375a-8494-4308-b7d1-c36fa21e2339",
                    "context": "documentation"
                  },
                  "storage_key": "439a375a-8494-4308-b7d1-c36fa21e2339",
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
                  "content": "From the <strong>BossDied </strong>event node, drag then search for and select <strong>Open Door</strong>. Connect <strong>Event Begin Play</strong> to the <strong>Bind Event to On Boss Died</strong> node as seen below.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741297,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741297,
                    "file_name": "image_33.png",
                    "file_size": 66490,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:49.190+00:00",
                    "height": 272,
                    "width": 625,
                    "storage_key": "7732abbd-7abf-4f0e-9aca-5abe8d9376a1",
                    "context": "documentation"
                  },
                  "storage_key": "7732abbd-7abf-4f0e-9aca-5abe8d9376a1",
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
                  "content": "<strong>Compile </strong>and <strong>Save </strong>the Blueprint.",
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
            "content": "Section Results",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this section you created an interactive door Actor that binds to the <strong>On Boss Died</strong> Event Dispatcher found in the <strong>BP_BossDied </strong>Actor. This binding occurs on Begin Play, but is executed at runtime whenever this event is triggered by <strong>BP_BossDied</strong>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "4 -  Creating an Interactive Explosion",
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
                  "content": "Go to <strong>Starter Content &gt; Blueprints</strong> and select <strong>Blueprint_Effect_Explosion</strong>. Drag it into your gameplay folder and select <strong>Copy Here</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741298,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741298,
                    "file_name": "image_34.png",
                    "file_size": 31709,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:49.281+00:00",
                    "height": 174,
                    "width": 406,
                    "storage_key": "b2abeba6-068b-4d89-b501-31232179856b",
                    "context": "documentation"
                  },
                  "storage_key": "b2abeba6-068b-4d89-b501-31232179856b",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741299,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741299,
                    "file_name": "image_35.png",
                    "file_size": 28256,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:49.377+00:00",
                    "height": 168,
                    "width": 316,
                    "storage_key": "fbcf70a4-914a-4b23-9a92-50f8a1f2e08c",
                    "context": "documentation"
                  },
                  "storage_key": "fbcf70a4-914a-4b23-9a92-50f8a1f2e08c",
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
                  "content": "Open <strong>Blueprint_Effect_Explosion</strong> in the Blueprint editor. From the <strong>Viewport</strong>, select the <strong>P_Explosion </strong>component and on the <strong>Details </strong>panel go to the <strong>Activation </strong>section and disable <strong>Auto Activate</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741300,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741300,
                    "file_name": "image_36.png",
                    "file_size": 2915,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:49.501+00:00",
                    "height": 67,
                    "width": 291,
                    "storage_key": "5e92bc8f-a2be-457d-ab15-086faa358e74",
                    "context": "documentation"
                  },
                  "storage_key": "5e92bc8f-a2be-457d-ab15-086faa358e74",
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
                  "content": "Repeat the step above for the <strong>Explosion Audio</strong> component.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Add a new variable by clicking the <strong>+ button </strong>next to the<strong> Variable </strong>section. Name the variable <strong>BossDiedReference</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741301,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741301,
                    "file_name": "image_37.png",
                    "file_size": 6467,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:49.580+00:00",
                    "height": 99,
                    "width": 390,
                    "storage_key": "445546c3-e820-468b-aefc-d1f573d0e1a6",
                    "context": "documentation"
                  },
                  "storage_key": "445546c3-e820-468b-aefc-d1f573d0e1a6",
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
                  "content": "From the <strong>Details </strong>panel click the <strong>Variable Type</strong> dropdown then search for and select the <strong>Object Reference</strong> of <strong>BP_BossDied</strong>. Check the <strong>Instance Editable</strong> checkbox.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741302,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741302,
                    "file_name": "image_38.png",
                    "file_size": 19455,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:49.666+00:00",
                    "height": 224,
                    "width": 515,
                    "storage_key": "d7376324-ad3e-493f-bd07-50a8938a42ac",
                    "context": "documentation"
                  },
                  "storage_key": "d7376324-ad3e-493f-bd07-50a8938a42ac",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741303,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741303,
                    "file_name": "image_39.png",
                    "file_size": 7583,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:49.769+00:00",
                    "height": 116,
                    "width": 369,
                    "storage_key": "915caf96-60f5-4a7c-9afe-677a4df81091",
                    "context": "documentation"
                  },
                  "storage_key": "915caf96-60f5-4a7c-9afe-677a4df81091",
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
                  "content": "From the <strong>Event Graph</strong> right-click then search for and select <strong>Event Begin Play</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Drag <strong>BossDiedReference </strong>to the <strong>Event Graph</strong> and select <strong>Get BossDiedReference</strong>. From the node, drag then search for and select <strong>Assign On Boss Died</strong>. Name the custom event <strong>BossDied</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741304,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741304,
                    "file_name": "image_40.png",
                    "file_size": 34378,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:49.840+00:00",
                    "height": 193,
                    "width": 788,
                    "storage_key": "96acc1ad-0e56-4db3-9548-b5f470511ec3",
                    "context": "documentation"
                  },
                  "storage_key": "96acc1ad-0e56-4db3-9548-b5f470511ec3",
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
                  "content": "Connect <strong>Event Begin Play</strong> to the <strong>Bind Event to Boss Died</strong> node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741305,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741305,
                    "file_name": "image_41.png",
                    "file_size": 49978,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:49.933+00:00",
                    "height": 262,
                    "width": 591,
                    "storage_key": "2e834499-24de-476b-970d-955fb6c43fad",
                    "context": "documentation"
                  },
                  "storage_key": "2e834499-24de-476b-970d-955fb6c43fad",
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
                      "content": "When you select the Assign option for the Event Dispatcher, a binding will be created as well as a custom event.",
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
                  "content": "Drag the <strong>P_Explosion </strong>and <strong>Explosion Audio</strong> components to the <strong>Event Graph</strong>. Drag from <strong>P_Explosion </strong>then search for and select <strong>Activate</strong>. Connect <strong>Explosion Sound</strong> to the <strong>Target </strong>pin of the <strong>Activate </strong>node.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Connect the <strong>BossDied </strong>event node to the <strong>Activate </strong>node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741306,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741306,
                    "file_name": "image_42.png",
                    "file_size": 89410,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:50.082+00:00",
                    "height": 345,
                    "width": 759,
                    "storage_key": "c437f750-ca77-4fd7-a2cd-59464587dfad",
                    "context": "documentation"
                  },
                  "storage_key": "c437f750-ca77-4fd7-a2cd-59464587dfad",
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
                  "content": "<strong>Compile </strong>and <strong>Save </strong>the Blueprint.",
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
            "content": "Section Results",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this section you modified <strong>Blueprint_Effect_Explosion </strong>to activate when the <strong>OnBossDied </strong>event is executed.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "5 - Testing the Event Dispatcher",
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
                  "content": "Drag the <strong>BP_BossDoor </strong>Actor into your Level. Go to the <strong>Details </strong>panel and click the <strong>Boss Reference Died</strong> dropdown then search for and select <strong>BP_BossDied</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741307,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741307,
                    "file_name": "image_43.png",
                    "file_size": 977335,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:50.270+00:00",
                    "height": 1045,
                    "width": 1609,
                    "storage_key": "61cdc8a9-2db8-4d72-8e14-97725276c74d",
                    "context": "documentation"
                  },
                  "storage_key": "61cdc8a9-2db8-4d72-8e14-97725276c74d",
                  "context": "documentation",
                  "width": 600,
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741308,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741308,
                    "file_name": "image_44.png",
                    "file_size": 21868,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:50.436+00:00",
                    "height": 275,
                    "width": 511,
                    "storage_key": "8095e28e-0fe7-4d22-b3bc-890b3a9c9d52",
                    "context": "documentation"
                  },
                  "storage_key": "8095e28e-0fe7-4d22-b3bc-890b3a9c9d52",
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
                  "content": "Drag several instances of <strong>Blueprint_Effect_Explosion </strong>into your Level. Go to the <strong>Details </strong>panel and click the <strong>Boss Reference Died</strong> dropdown then search for and select <strong>BP_BossDied</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741309,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741309,
                    "file_name": "image_45.png",
                    "file_size": 929905,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:50.536+00:00",
                    "height": 1035,
                    "width": 1606,
                    "storage_key": "b2ab2be4-88b1-4446-aafa-a35fcfeeef3d",
                    "context": "documentation"
                  },
                  "storage_key": "b2ab2be4-88b1-4446-aafa-a35fcfeeef3d",
                  "context": "documentation",
                  "width": 600,
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741310,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741310,
                    "file_name": "image_46.png",
                    "file_size": 21868,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:50.762+00:00",
                    "height": 275,
                    "width": 511,
                    "storage_key": "ffca2bb4-f3ed-4054-bcd1-c8264ae6e5e8",
                    "context": "documentation"
                  },
                  "storage_key": "ffca2bb4-f3ed-4054-bcd1-c8264ae6e5e8",
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
                  "content": "Press <strong>Play </strong>and walk over the <strong>BP_BossDied </strong>trigger to simulate your boss dying in the game.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741311,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741311,
                    "file_name": "image_47.gif",
                    "file_size": 817654,
                    "content_type": "image/gif",
                    "created_at": "2025-06-17T19:53:50.893+00:00",
                    "height": 256,
                    "width": 512,
                    "storage_key": "7c771974-56e4-4207-b279-48b95f20dd46",
                    "context": "documentation"
                  },
                  "storage_key": "7c771974-56e4-4207-b279-48b95f20dd46",
                  "context": "documentation",
                  "width": null,
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
            "content": "Section Results",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this section you tested the <strong>BP_BossDoor </strong>and <strong>Blueprint_Effect_Explosion </strong>Actors in the Level. You confirmed that each Actor responds to the <strong>OnBossDied </strong>event when the <strong>BP_BossDied </strong>Actor triggers it.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this guide you learned how to use Event Dispatchers to communicate between one working Actor to many target Actors. You also learned how to create Event Dispatchers and how to bind Actors to the event in order to trigger specific functionality.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Next Steps",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Now that you know how to use Event Dispatchers, take a look at the other types of communication referenced in the <strong><a href=\"making-interactive-experiences\\interactive-framework\\actors\\actor-communication\"></a></strong> documentation page.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "kx7",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1724,
        "excerpt_assignment_id": 1434,
        "blocks": [
          {
            "type": "header",
            "content": "Overview",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Delegates can call methods in Actor class Blueprints in a type-safe way. A delegate can be bound dynamically to form a communication where one Actor triggers an event on another Actor that is listening to be notified for that event.",
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
                "content": "See <a data-document-id=\"3227461\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/delegates-and-lambda-functions-in-unreal-engine\">Delegates</a> for additional documentation.",
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
            "type": "header",
            "content": "Goals",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this Quick Start guide, you will learn how to use Delegates to create an <strong>OnBossDied </strong>event that will trigger two Actor class Blueprints in your Level.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Objectives",
            "level": 2,
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
                  "content": "Create the <strong>Boss </strong>Actor that will contain an OnBossDied Delegate.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Create an interactive door Actor with a timeline component that will bind to the <strong>OnBossDied </strong>event.",
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
            "content": "1 - Required Setup",
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
                  "content": "In the <strong>New Project Categories</strong> section of the menu, select <strong>Games</strong> and click <strong>Next</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741312,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741312,
                    "file_name": "image_0.png",
                    "file_size": 80765,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:51.479+00:00",
                    "height": 774,
                    "width": 1110,
                    "storage_key": "afaded5c-e4c7-4c19-8263-90ef9dd8249f",
                    "context": "documentation"
                  },
                  "storage_key": "afaded5c-e4c7-4c19-8263-90ef9dd8249f",
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
                  "content": "Select the <strong>Third Person</strong> template and click <strong>Next</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741313,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741313,
                    "file_name": "image_1.png",
                    "file_size": 228409,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:51.695+00:00",
                    "height": 774,
                    "width": 1110,
                    "storage_key": "5121fa66-9c55-4822-80b4-8ead407b17b4",
                    "context": "documentation"
                  },
                  "storage_key": "5121fa66-9c55-4822-80b4-8ead407b17b4",
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
                  "content": "Select the <strong>C++ </strong>and <strong>With Starter Content</strong> options and click <strong>Create Project</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741314,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741314,
                    "file_name": "image_2.png",
                    "file_size": 233661,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:51.907+00:00",
                    "height": 1428,
                    "width": 2048,
                    "storage_key": "5474c94a-4404-4a16-86e9-134d02d887ba",
                    "context": "documentation"
                  },
                  "storage_key": "5474c94a-4404-4a16-86e9-134d02d887ba",
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
            "content": "Section Results",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You have created a new C++ Third Person project and are now ready to learn about Delegates.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "2 -  Creating the Boss Actor and OnBossDied Delegate",
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
                  "content": "From the <a data-document-id=\"3228682\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-cplusplus-class-wizard-in-unreal-engine\">C++ Class Wizard</a>, create a new Actor class named BossActor.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741315,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741315,
                    "file_name": "image_3.png",
                    "file_size": 271113,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:52.157+00:00",
                    "height": 1237,
                    "width": 2048,
                    "storage_key": "bd6733d4-fa27-488d-ba1a-8c1c5ebc9866",
                    "context": "documentation"
                  },
                  "storage_key": "bd6733d4-fa27-488d-ba1a-8c1c5ebc9866",
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
                  "content": "Navigate to your <strong>BossActor.h</strong>. Underneath your library includes, declare the following Delegate.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "DECLARE_DELEGATE(FOnBossDiedDelegate);",
                  "lines_of_code": 1,
                  "id": 60614,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYxNCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjMwKzAwOjAwIn0=--c099534a8596562c20a0fd2ab3f91f53538fffd2f36127ad9a7475fdcb63a22a",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "In your class defaults, declare the following",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "protected:\n             UFUNCTION()\n             void HandleBossDiedEvent();\n             UPROPERTY(EditInstanceOnly, BlueprintReadWrite)\n             class UBoxComponent* BoxComp;\n             virtual void NotifyActorBeginOverlap(AActor* OtherActor);\n\t\t\n         public:\n             FOnBossDiedDelegate OnBossDied;",
                  "lines_of_code": 9,
                  "id": 60615,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYxNSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjMwKzAwOjAwIn0=--ec040b9d9ed8d4ebc3b459af62358a748af3590e1a258aab3911da47c9df36f4",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to your BossActor.cpp and add the following class library.",
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
                  "id": 60616,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYxNiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjMwKzAwOjAwIn0=--87dfe1d63080eea350b790654f06f42bfbde55dcbebc21479b2b0bac4a38f6eb",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Implement the following class definitions.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "ABossActor::ABossActor()\n         {\n             BoxComp = CreateDefaultSubobject&lt;UBoxComponent&gt;(TEXT(&quot;BoxComp&quot;));\n             BoxComp-&gt;SetBoxExtent(FVector(128, 128, 64));\n             BoxComp-&gt;SetVisibility(true);\n         }\n\t\t\n         void ABossActor::HandleBossDiedEvent()\n         {\n             OnBossDied.ExecuteIfBound();\n",
                  "lines_of_code": 16,
                  "id": 60617,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYxNywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjMwKzAwOjAwIn0=--bccf6213235110d3c79bad286b9152e2641157755b73c0ef55d558a79705a72f",
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
              ],
              [
                {
                  "type": "paragraph",
                  "content": "From the <strong>C++ Classes folder</strong>, right-click your <strong>BossActor</strong>, then from the <strong>C++ Class Actions</strong> dropdown menu, select <strong>Create Blueprint class based on BossActor</strong>. Name your Blueprint class <strong>BP_BossActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741316,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741316,
                    "file_name": "image_4.png",
                    "file_size": 213271,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:52.379+00:00",
                    "height": 766,
                    "width": 2004,
                    "storage_key": "73a42edd-65cd-4612-9436-4c1e129707ec",
                    "context": "documentation"
                  },
                  "storage_key": "73a42edd-65cd-4612-9436-4c1e129707ec",
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
                  "content": "Drag an instance of your <strong>BossActor</strong> into the Level.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741317,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741317,
                    "file_name": "image_5.png",
                    "file_size": 1099561,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:52.620+00:00",
                    "height": 1421,
                    "width": 2048,
                    "storage_key": "f23b989f-68df-42b4-a931-98db32a7549b",
                    "context": "documentation"
                  },
                  "storage_key": "f23b989f-68df-42b4-a931-98db32a7549b",
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
            "content": "Finished Code",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "BossActor.h",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "#pragma once\n\t#include &quot;CoreMinimal.h&quot;\n\t#include &quot;GameFramework/Actor.h&quot;\n\t#include &quot;BossActor.generated.h&quot;\n\n\tDECLARE_DELEGATE(FOnBossDiedDelegate);\n\tUCLASS()\n\n\tclass BPCOMMUNICATION_API ABossActor : public AActor\n\t{\n",
            "lines_of_code": 33,
            "id": 60618,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYxOCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjMwKzAwOjAwIn0=--6d54f74c219311d629a6c1c3b135ef19f30acfd5c84e2be1c7f0d7cfb1026497",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "<strong>BossActor.cpp</strong>",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "#include &quot;BossActor.h&quot;\n\t#include &quot;Components/BoxComponent.h&quot;\n\t#include &quot;BPCommunicationGameMode.h&quot;\n\n\t// Sets default values\n\tABossActor::ABossActor()\n\t{\n\t\t// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n\t\tPrimaryActorTick.bCanEverTick = true;\n\t\tBoxComp = CreateDefaultSubobject&lt;UBoxComponent&gt;(TEXT(&quot;BoxComp&quot;));\n",
            "lines_of_code": 35,
            "id": 60619,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYxOSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjMwKzAwOjAwIn0=--89a98f0c129d550bbb207761d0b21b851303a00f18122f148c3607003afc27b4",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Section Results",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this section you created the <strong>BossActor </strong>class, which contains a Box Component, and Delegate for a <strong>OnBossDied</strong> event, which will be used to signal other Actor classes when the event has been executed.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "3 - Creating an Interactive Door",
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
                  "content": "From the <strong>C++ Class Wizard</strong>, create a new <strong>Actor</strong> class named <strong>DoorActor.</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to your DoorActor.h file and declare the following include:",
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
                  "id": 60620,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYyMCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjMwKzAwOjAwIn0=--7a64481c2b30e01552df8e16f66cf31e8394d75f72f8c676a9d5de6121aba725",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Then declare the following class definitions.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "// Variable to hold the Curve asset\n             UPROPERTY(EditInstanceOnly)\n             UCurveFloat* DoorTimelineFloatCurve;\n\t\t\n         protected:\n\t\t\n             void BossDiedEventFunction();\n             UPROPERTY(EditInstanceOnly,BlueprintReadWrite)\n             class ABossActor* BossActorReference;\n\t\t\n",
                  "lines_of_code": 26,
                  "id": 60621,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYyMSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjMwKzAwOjAwIn0=--6fddc7a3417bb572a45e1feab85819f80e40a62a98c7ac734d933410352ad12a",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Inside of <strong>DoorActor.cpp</strong> declare the following class library.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "#include &quot;BossActor.h&quot;",
                  "lines_of_code": 1,
                  "id": 60622,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYyMiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjMwKzAwOjAwIn0=--0619d40e68bf9e748ce18bcce659c52f47a06adb979d5a292b5820b6c24fb66e",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Implement the following class definitions.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "ADoorActor::ADoorActor()\n        {\n            //Create our Default Components\n            DoorFrame = CreateDefaultSubobject&lt;UStaticMeshComponent&gt;(TEXT(&quot;DoorFrameMesh&quot;));\n            Door = CreateDefaultSubobject&lt;UStaticMeshComponent&gt;(TEXT(&quot;DoorMesh&quot;));\n            DoorTimelineComp = CreateDefaultSubobject&lt;UTimelineComponent&gt;(TEXT(&quot;DoorTimelineComp&quot;));\n\t\t\n            //Setup our Attachments\n            DoorFrame-&gt;SetupAttachment(RootComponent);\n            Door-&gt;AttachToComponent(DoorFrame, FAttachmentTransformRules::KeepRelativeTransform);\n",
                  "lines_of_code": 44,
                  "id": 60623,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYyMywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjMwKzAwOjAwIn0=--a76664e9ded41d4028240ba142884b4312e12fabc00a09a3be7842ee798c3b44",
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
                  "content": "From the <strong>Content Browser</strong>, select <strong>Add/Import </strong>&gt; <strong>Miscellaneous</strong> &gt; <strong>Curve.</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741318,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741318,
                    "file_name": "image_6.png",
                    "file_size": 56205,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:52.884+00:00",
                    "height": 623,
                    "width": 341,
                    "storage_key": "f454d363-cc53-4c4f-b197-2c7ca44d75bb",
                    "context": "documentation"
                  },
                  "storage_key": "f454d363-cc53-4c4f-b197-2c7ca44d75bb",
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
                  "content": "Select <strong>CurveFloat</strong> and name your CurveFloat asset <strong>DoorCurveFloat, </strong>then double-click your DoorCurveFloat asset. Add two keys to your Float Curve and give one key the time-value (0,0), and the other key the time-value of (4,90).",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741319,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741319,
                    "file_name": "image_7.png",
                    "file_size": 340259,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:53.045+00:00",
                    "height": 1648,
                    "width": 2500,
                    "storage_key": "5fe1c406-d6d5-4f1e-a15f-83ac10fb6589",
                    "context": "documentation"
                  },
                  "storage_key": "5fe1c406-d6d5-4f1e-a15f-83ac10fb6589",
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
                  "content": "Shift-click to select both your keys, and set them to <strong>Auto Cubic interpolation</strong>, then save your Curve.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741320,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741320,
                    "file_name": "image_8.png",
                    "file_size": 154520,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:53.283+00:00",
                    "height": 1758,
                    "width": 2131,
                    "storage_key": "2af275a4-aecf-4394-98e6-4e36472b57eb",
                    "context": "documentation"
                  },
                  "storage_key": "2af275a4-aecf-4394-98e6-4e36472b57eb",
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
                  "content": "Save your DoorCurveFloat.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "From the Content Browser, navigate to your <strong>C++ Classes folder</strong>, right-click your DoorActor class, then select <strong>Create Blueprint Class based on Door Actor</strong>. Name your Blueprint Actor <strong>Bp_DoorActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741321,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741321,
                    "file_name": "image_9.png",
                    "file_size": 230247,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:53.422+00:00",
                    "height": 628,
                    "width": 2048,
                    "storage_key": "39ec4b94-1365-4e97-873f-d552e6470ee4",
                    "context": "documentation"
                  },
                  "storage_key": "39ec4b94-1365-4e97-873f-d552e6470ee4",
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
                  "content": "Inside <strong>BP_DoorActor</strong>'s <strong>class defaults</strong>, find the <strong>Components </strong>tab, and select the <strong>DoorFrame</strong> <strong>Static Mesh component</strong>, navigate to the <strong>Details </strong>panel and change the Static Mesh to <strong>SM_DoorFrame</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741322,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741322,
                    "file_name": "image_10.png",
                    "file_size": 116728,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:53.637+00:00",
                    "height": 839,
                    "width": 1447,
                    "storage_key": "a339f756-8ac7-48df-bede-fceef4a68c31",
                    "context": "documentation"
                  },
                  "storage_key": "a339f756-8ac7-48df-bede-fceef4a68c31",
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
                  "content": "Next, from the Components tab, select the DoorMesh component. Navigate to the Details panel and change the static mesh to <strong>SM_Door</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741323,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741323,
                    "file_name": "image_11.png",
                    "file_size": 121054,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:53.804+00:00",
                    "height": 947,
                    "width": 1442,
                    "storage_key": "3376b638-02ca-45a7-a15d-b2c0c3ddb746",
                    "context": "documentation"
                  },
                  "storage_key": "3376b638-02ca-45a7-a15d-b2c0c3ddb746",
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
                  "content": "From the Details panel, select DoorCurveFloat from the Door Timeline Float Curve dropdown menu.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741324,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741324,
                    "file_name": "image_12.png",
                    "file_size": 106801,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:53.938+00:00",
                    "height": 1029,
                    "width": 1197,
                    "storage_key": "abc57df7-0f55-4aae-ac4e-459400d97fa3",
                    "context": "documentation"
                  },
                  "storage_key": "abc57df7-0f55-4aae-ac4e-459400d97fa3",
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
                  "content": "Compile and save your Blueprint.",
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
            "code_preview": "#include &quot;CoreMinimal.h&quot;\n\t#include &quot;GameFramework/Actor.h&quot;\n\t#include &quot;Components/TimelineComponent.h&quot;\n\t#include &quot;DoorActor.generated.h&quot;\n\n\tUCLASS()\n\tclass BPCOMMUNICATION_API ADoorActor : public AActor\n\t{\n\t\tGENERATED_BODY()\n\n",
            "lines_of_code": 46,
            "id": 60624,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYyNCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjMwKzAwOjAwIn0=--fb4d46cf6853bb436f7c10f5b6057196cbcdcce31873e434e3d5f210a1fe3be8",
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
            "code_preview": "#include &quot;DoorActor.h&quot;\n\t#include &quot;BossActor.h&quot;\n\n\t// Sets default values\n\tADoorActor::ADoorActor()\n\t{\n\t\t// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n\t\tPrimaryActorTick.bCanEverTick = true;\n\n\t\t//Create our Default Components\n",
            "lines_of_code": 56,
            "id": 60625,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2MDYyNSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjE3OjMwKzAwOjAwIn0=--c3681be3934230d0e7216c8ce1738740838b23de5b44a17f61a1824466513b8c",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Section Results",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this section you created an interactive <strong>DoorActor</strong> that binds to the <strong>OnBossDied</strong> Event Dispatcher found in the <strong>BossActor</strong> class. This binding occurs in Begin Play, but is executed at runtime whenever this event is triggered by an overlap in BossActor's<strong> Box Component</strong>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "5 - Testing the Event Dispatcher",
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
                  "content": "Drag the <strong>BP_Door </strong>Blueprint into your Level. Go to the <strong>Details </strong>panel and click the <strong>Boss Reference Died</strong> dropdown and search for and select <strong>BP_BossDied</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741325,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741325,
                    "file_name": "image_13.png",
                    "file_size": 1189960,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T19:53:54.095+00:00",
                    "height": 1330,
                    "width": 2048,
                    "storage_key": "7cfc0642-f3a1-4c0a-8e74-9ea2da10bade",
                    "context": "documentation"
                  },
                  "storage_key": "7cfc0642-f3a1-4c0a-8e74-9ea2da10bade",
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
                  "content": "With your Bp_DoorActor selected, navigate to the <strong>Details </strong>panel, click the <strong>Boss Actor Reference </strong>dropdown arrow, then search for and select <strong>BP_BossActpr</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Press Play and walk over the <strong>BP_BossActor </strong>trigger to simulate your boss dying in the game.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25741326,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25741326,
                    "file_name": "image_14.gif",
                    "file_size": 4480302,
                    "content_type": "image/gif",
                    "created_at": "2025-06-17T19:53:54.270+00:00",
                    "height": 360,
                    "width": 640,
                    "storage_key": "ecfe4be0-dfc6-4cde-9799-0abd0abf464f",
                    "context": "documentation"
                  },
                  "storage_key": "ecfe4be0-dfc6-4cde-9799-0abd0abf464f",
                  "context": "documentation",
                  "width": null,
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
            "content": "Section Results",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this section you tested the <strong>BP_DoorActor </strong>in the Level. You confirmed that the Actor responds to the <strong>OnBossDied </strong>event when the <strong>BP_BossActor's Box Component</strong> overlaps with another Actor to trigger the Delegate.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this guide you learned how to use Delegates to communicate between multiple Actor class Blueprints.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Next Steps",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Now that you know how to use Delegates, take a look at the other communication types referenced in the <strong><a href=\"making-interactive-experiences\\interactive-framework\\actors\\actor-communication\"></a></strong> documentation page.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "r4r",
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
