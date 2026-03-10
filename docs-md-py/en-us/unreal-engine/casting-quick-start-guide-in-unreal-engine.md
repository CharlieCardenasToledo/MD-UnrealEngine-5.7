# Casting Quick Start Guide

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/casting-quick-start-guide-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1693,
        "excerpt_assignment_id": 1403,
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
            "content": "Casting is a common communication method where you take a reference to an Actor and try to convert it to a different class. If the conversion is successful, then you can use Direct Actor communication to access its information and functionality.\nThis method requires a reference to the Actor in your Level so you can use the <strong>Cast </strong>node to try to convert it to a specific class. This communication method uses a one-to-one relationship between your working Actor and your target Actor.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Setup",
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
                  "content": "Begin by creating a new <strong>Games</strong> &gt; <strong>Third Person</strong> &gt; <strong>Blueprint</strong> project named <strong>BPCommunication</strong>..",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740000,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740000,
                    "file_name": "ProjectSetupBp.png",
                    "file_size": 474016,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:31.856+00:00",
                    "height": 719,
                    "width": 1099,
                    "storage_key": "07a3cafd-aadb-4ff5-b537-cdf3b4b69e3b",
                    "context": "documentation"
                  },
                  "storage_key": "07a3cafd-aadb-4ff5-b537-cdf3b4b69e3b",
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
            "content": "Creating a Rotating Actor",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "For this example, you will create an Actor that begins rotating a Static Mesh when the player is nearby.",
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
                  "content": "Right-click in the <strong>Content Browser</strong> and click <strong>Blueprint Class </strong>under the<strong> Create Basic Asset </strong>section.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740001,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740001,
                    "file_name": "BlueprintClass.png",
                    "file_size": 27361,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:32.118+00:00",
                    "height": 713,
                    "width": 307,
                    "storage_key": "e90212c3-d3f8-412c-99fc-82b1e533f0c9",
                    "context": "documentation"
                  },
                  "storage_key": "e90212c3-d3f8-412c-99fc-82b1e533f0c9",
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
                  "content": "Select <strong>Actor </strong>as your Parent Class and name the Blueprint <strong>BP_RotateActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740002,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740002,
                    "file_name": "ParentClassActor.png",
                    "file_size": 41654,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:32.210+00:00",
                    "height": 458,
                    "width": 626,
                    "storage_key": "d1ba26ae-4127-4abb-8dac-16cf19fd788d",
                    "context": "documentation"
                  },
                  "storage_key": "d1ba26ae-4127-4abb-8dac-16cf19fd788d",
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
                  "content": "Open the Blueprint by double-clicking it in the <strong>Content Browser.</strong> Then in the Blueprint editor window, go to the <strong>Components </strong>panel and click the <strong>Add Component</strong> button. Search for and select <strong>Static Mesh</strong>. This will add a Static Mesh component to the Blueprint.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740003,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740003,
                    "file_name": "StaticMesh.png",
                    "file_size": 10167,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:32.371+00:00",
                    "height": 157,
                    "width": 277,
                    "storage_key": "d5664862-df1e-4e31-8c97-0f7f1b3e2a53",
                    "context": "documentation"
                  },
                  "storage_key": "d5664862-df1e-4e31-8c97-0f7f1b3e2a53",
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
                  "content": "With the <strong>Static Mesh</strong> component selected, go to the <strong>Details </strong>panel and click the <strong>Static Mesh</strong> dropdown. Search for and select <strong>Shape_Cube</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740004,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740004,
                    "file_name": "StaticMeshDetails.png",
                    "file_size": 34419,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:32.477+00:00",
                    "height": 426,
                    "width": 563,
                    "storage_key": "440fd393-bfa5-483a-8411-d36605d0d2cc",
                    "context": "documentation"
                  },
                  "storage_key": "440fd393-bfa5-483a-8411-d36605d0d2cc",
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
                  "content": "Right-click in the <strong>Event Graph</strong> to open the context sensitive search window and search for and select <strong>AddActorLocalRotation </strong>to add this node to the graph.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740005,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740005,
                    "file_name": "AddActorLocalRotation.png",
                    "file_size": 27907,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:32.567+00:00",
                    "height": 494,
                    "width": 654,
                    "storage_key": "80db7f56-6838-4b3f-b6b1-804c49a54f88",
                    "context": "documentation"
                  },
                  "storage_key": "80db7f56-6838-4b3f-b6b1-804c49a54f88",
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
                  "content": "Connect the <strong>AddActorLocalRotation </strong>node to <strong>Event Tick</strong>. Set the <strong>Z value</strong> to <strong>2.0</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740006,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740006,
                    "file_name": "AddActorLocalRotationZ.png",
                    "file_size": 27862,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:32.636+00:00",
                    "height": 227,
                    "width": 451,
                    "storage_key": "8f548a13-261b-4f0c-a014-3cceba529193",
                    "context": "documentation"
                  },
                  "storage_key": "8f548a13-261b-4f0c-a014-3cceba529193",
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
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Drag the <strong>BP_RotateActor </strong>Actor into the Level and press <strong>Play</strong>. You should see the cube rotate continuously.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740007,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740007,
                    "file_name": "DragRotatingCube.png",
                    "file_size": 1508041,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:32.756+00:00",
                    "height": 1250,
                    "width": 1243,
                    "storage_key": "658996ac-7e4c-42d7-98fb-0259197c506c",
                    "context": "documentation"
                  },
                  "storage_key": "658996ac-7e4c-42d7-98fb-0259197c506c",
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
                  "content": "Now you will add a condition so the object spins only when the player is nearby. Right-click the <strong>Event Graph</strong> and add a <strong>Branch </strong>node.  Connect the node between the output pin of <strong>Event Tick</strong> and the input pin of <strong>AddActorLocalRotation </strong>nodes.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740008,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740008,
                    "file_name": "BranchNode.png",
                    "file_size": 37367,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:33.028+00:00",
                    "height": 231,
                    "width": 656,
                    "storage_key": "4b8b9ab6-e6f0-4b23-9198-09f3621d120d",
                    "context": "documentation"
                  },
                  "storage_key": "4b8b9ab6-e6f0-4b23-9198-09f3621d120d",
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
                  "content": "Create a variable of type Boolean called <strong>Can Rotate</strong><strong> </strong>and connect it to the<strong> Condition </strong>pin of the <strong>Branch </strong>node, as shown below.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740009,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740009,
                    "file_name": "BranchCanRotate.png",
                    "file_size": 42913,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:33.125+00:00",
                    "height": 231,
                    "width": 665,
                    "storage_key": "5d3ea075-6770-421e-a303-e751647151ac",
                    "context": "documentation"
                  },
                  "storage_key": "5d3ea075-6770-421e-a303-e751647151ac",
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
                  "content": "<strong>Compile </strong>the Blueprint and set the <strong>Default Value</strong> of <strong>CanRotate </strong>to <strong>False</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740010,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740010,
                    "file_name": "DefaultRotateFalse.png",
                    "file_size": 2388,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:33.196+00:00",
                    "height": 59,
                    "width": 258,
                    "storage_key": "cdffa5a0-9025-410d-8f37-ddd3735e0003",
                    "context": "documentation"
                  },
                  "storage_key": "cdffa5a0-9025-410d-8f37-ddd3735e0003",
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
                  "content": "Go to the <strong>My Bueprints</strong> tab and click the <strong>+ Function</strong> button to create a new function. Name the function <strong>OverlappedPlayer</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740011,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740011,
                    "file_name": "OverlappedPlayerFunction.png",
                    "file_size": 20264,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:33.274+00:00",
                    "height": 300,
                    "width": 296,
                    "storage_key": "0060832a-0494-43a2-9390-7227471629a7",
                    "context": "documentation"
                  },
                  "storage_key": "0060832a-0494-43a2-9390-7227471629a7",
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
                  "content": "With the function selected, go to the <strong>Details </strong>panel and click the <strong>+ New Parameter</strong> button. Name the new boolean parameter <strong>Begin Overlap</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740012,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740012,
                    "file_name": "BeginOverlapInput.png",
                    "file_size": 4162,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:33.360+00:00",
                    "height": 55,
                    "width": 410,
                    "storage_key": "6f32aa2f-0849-461e-983c-a7992dd298a7",
                    "context": "documentation"
                  },
                  "storage_key": "6f32aa2f-0849-461e-983c-a7992dd298a7",
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
                  "content": "Drag the <strong>CanRotate </strong>variable inside the function and select <strong>Set CanRotate</strong>. Connect the <strong>Overlapped Player</strong> node to the <strong>Set Can Rotate</strong> node. Connect the <strong>Begin Overlap</strong> pin of the <strong>Overlapped Player</strong> node to the <strong>Can Rotate</strong> pin of the <strong>Set Can Rotate </strong>node, as seen below.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740013,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740013,
                    "file_name": "ConnectCanRotate.png",
                    "file_size": 18789,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:33.435+00:00",
                    "height": 188,
                    "width": 438,
                    "storage_key": "5fcaaca8-4f9c-4c77-aa94-bb5f63d8b4c5",
                    "context": "documentation"
                  },
                  "storage_key": "5fcaaca8-4f9c-4c77-aa94-bb5f63d8b4c5",
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
            "content": "Modifying the Player Blueprint",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this section, you will modify the <strong>ThirdPersonCharacter </strong>Blueprint to cast to the <strong>BP_RotateActor </strong>Actor and set its <strong>Rotate </strong>variable to <strong>True </strong>when you are nearby.",
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
                  "content": "Open your <strong>ThirdPersonCharacter</strong> Blueprint.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "In the Blueprint editor window, go to the <strong>Components </strong>panel and click the <strong>Add Component</strong> button.  Search for and select <strong>Sphere Collision</strong>. This will add a Sphere Collision component to the Blueprint.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740014,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740014,
                    "file_name": "SphereCollision.png",
                    "file_size": 12419,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:33.549+00:00",
                    "height": 174,
                    "width": 267,
                    "storage_key": "59310b32-d791-4150-aec3-f95feb877610",
                    "context": "documentation"
                  },
                  "storage_key": "59310b32-d791-4150-aec3-f95feb877610",
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
                  "content": "With the <strong>Sphere Collision</strong> component selected, go to the <strong>Details </strong>panel and set the <strong>Radius </strong>to 200.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740015,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740015,
                    "file_name": "SphereRadius.png",
                    "file_size": 3209,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:33.648+00:00",
                    "height": 56,
                    "width": 398,
                    "storage_key": "6df61e72-204d-4239-9245-d2e3ece8584d",
                    "context": "documentation"
                  },
                  "storage_key": "6df61e72-204d-4239-9245-d2e3ece8584d",
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
                  "content": "Right-click the <strong>Sphere Collision</strong> component and select the <strong>OnComponentBeginOverlap </strong>and <strong>OnComponentEndOverlap </strong>events to add them to the <strong>Event Graph</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740016,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740016,
                    "file_name": "OverlapEvents.png",
                    "file_size": 17378,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:33.757+00:00",
                    "height": 135,
                    "width": 624,
                    "storage_key": "01be82a3-8c83-4ecc-8e4b-d58ab93b47e9",
                    "context": "documentation"
                  },
                  "storage_key": "01be82a3-8c83-4ecc-8e4b-d58ab93b47e9",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740017,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740017,
                    "file_name": "OverlapEventNodes.png",
                    "file_size": 44540,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:33.890+00:00",
                    "height": 446,
                    "width": 358,
                    "storage_key": "f9b45bfb-0b47-4e17-ba7b-7ae7cc956e32",
                    "context": "documentation"
                  },
                  "storage_key": "f9b45bfb-0b47-4e17-ba7b-7ae7cc956e32",
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
                  "content": "Drag from the <strong>On Component Begin Overlap</strong> node's <strong>Other Actor</strong> pin, then search for and select <strong>cast to BP Rotate Object</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740018,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740018,
                    "file_name": "CastToBpRotateActor.png",
                    "file_size": 39459,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:33.994+00:00",
                    "height": 264,
                    "width": 787,
                    "storage_key": "8d0ecd29-e867-4d32-8ff3-0b078a7094a8",
                    "context": "documentation"
                  },
                  "storage_key": "8d0ecd29-e867-4d32-8ff3-0b078a7094a8",
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
                  "content": "Drag from the <strong>As BP Rotate Object</strong> pin and search for and select <strong>Overlapped Player</strong>. Enable the <strong>Begin Overlap</strong> pin of the <strong>Overlapped Player</strong> node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740019,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740019,
                    "file_name": "OverlappedPlayer.png",
                    "file_size": 30824,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:34.100+00:00",
                    "height": 256,
                    "width": 702,
                    "storage_key": "3261da8d-d116-4fdf-a429-699f25c3523f",
                    "context": "documentation"
                  },
                  "storage_key": "3261da8d-d116-4fdf-a429-699f25c3523f",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740020,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740020,
                    "file_name": "OverlappedPlayerWhole.png",
                    "file_size": 60075,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:34.238+00:00",
                    "height": 257,
                    "width": 854,
                    "storage_key": "8a76f992-953f-473e-9ad1-d2def72ec82b",
                    "context": "documentation"
                  },
                  "storage_key": "8a76f992-953f-473e-9ad1-d2def72ec82b",
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
                  "content": "Repeat steps 5 and 6 to attach the same nodes to the <strong>On Component End Overlap</strong> node. Disable the <strong>Begin Overlap</strong> pin of the <strong>Overlapped Player</strong> node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740021,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740021,
                    "file_name": "CompleteFunction.png",
                    "file_size": 116093,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:34.301+00:00",
                    "height": 465,
                    "width": 869,
                    "storage_key": "5156fbd7-4cae-48f5-9fec-945aa8aac5c9",
                    "context": "documentation"
                  },
                  "storage_key": "5156fbd7-4cae-48f5-9fec-945aa8aac5c9",
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
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Press <strong>Play </strong>and approach the <strong>BP_RotateActor </strong>Actor to see it rotate only when the player is nearby.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740022,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740022,
                    "file_name": "RotateCube.GIF",
                    "file_size": 13182881,
                    "content_type": "image/gif",
                    "created_at": "2025-06-17T15:12:34.498+00:00",
                    "height": 360,
                    "width": 640,
                    "storage_key": "e29b3dfc-024e-4463-9f6a-93c0d89332eb",
                    "context": "documentation"
                  },
                  "storage_key": "e29b3dfc-024e-4463-9f6a-93c0d89332eb",
                  "context": "documentation",
                  "width": 600,
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
            "content": "Next Steps",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Now that you know how to use casting, take a look at the other types of communication referenced in the <a href=\"making-interactive-experiences/interactive-framework/actors/actor-communication\"></a> documentation page.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "qPl",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1694,
        "excerpt_assignment_id": 1404,
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
            "content": "Casting Blueprint classes is a common communication type, in which you use a reference to an Actor class Blueprint and convert it to a different class. If this conversion is successful, then you can use Direct Blueprint communication to access its information and functionality.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "This method requires a reference to the Actor class Blueprint in your Level so you can use the <strong>Cast </strong>node to try to convert it to a specific class. This communication type uses a one-to-one relationship between your working Actor class Blueprint to your target Actor class Blueprint.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this Quick Start guide, you will learn how to create an Actor in C++, that has the Blueprint casting functionality used to access information from a target Blueprint.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Setup",
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
                  "content": "Begin by creating a new <strong>Games</strong> &gt; <strong>Third Person</strong> &gt; <strong>C++</strong> project named <strong>BPCommunication</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740023,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740023,
                    "file_name": "ProjectSetupCpp.png",
                    "file_size": 472073,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:35.205+00:00",
                    "height": 719,
                    "width": 1099,
                    "storage_key": "e3dc2f8e-bb9a-45e9-bd24-5367e1cc86b2",
                    "context": "documentation"
                  },
                  "storage_key": "e3dc2f8e-bb9a-45e9-bd24-5367e1cc86b2",
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
            "content": "Creating a Rotating Actor",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "For this example, you will create an Actor class Blueprint that has the functionality to rotate its Static Mesh Component when the player is nearby.",
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
                  "content": "From the <a data-document-id=\"3228682\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-cplusplus-class-wizard-in-unreal-engine\">C++ Class Wizard</a>, create a new Actor class named <strong>RotatingActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740024,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740024,
                    "file_name": "AddCppClass.png",
                    "file_size": 37790,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:35.452+00:00",
                    "height": 580,
                    "width": 946,
                    "storage_key": "88b95221-9481-4c95-b386-3ad7aa12bd20",
                    "context": "documentation"
                  },
                  "storage_key": "88b95221-9481-4c95-b386-3ad7aa12bd20",
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
                  "content": "In the class defaults of your <strong>RotatingActor.h</strong> implement the following code.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "public:\n\t\t\n            void SetbCanRotate(bool value);\n\t\t\n        protected:\n\t\t\n            // Called when the game starts or when spawned\n            virtual void BeginPlay() override;\n            void RotateActor();\n            bool bCanRotate;\n",
                  "lines_of_code": 13,
                  "id": 60452,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDQ1MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjAyKzAwOjAwIn0=--1178bd69dbaa76ccdc72e5c3143a4cd8b85e67990f7b58352fe4dd4e9ee3cb20",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to your <strong>RotatingActor.cpp</strong> and declare the following code in the constructor <strong>ARotatingActor::ARotatingActor</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "ARotatingActor::ARotatingActor()\n     {\n         RootComponent = CreateDefaultSubobject&lt;USceneComponent&gt;(TEXT(&quot;SceneComponent&quot;));\n         MeshComp = CreateDefaultSubobject&lt;UStaticMeshComponent&gt;(TEXT(&quot;StaticMesh&quot;));\n         MeshComp-&gt;SetupAttachment(RootComponent, FAttachmentTransformRules::KeepRelativeTransform);\n         bCanRotate = false;\n     }",
                  "lines_of_code": 7,
                  "id": 60453,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDQ1MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjAyKzAwOjAwIn0=--192d5c665f33a8e95c08cc4b8ef82a355ddf327d3b60b039dedc24c4769a34ed",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Implement the following code for your <strong>ARotatingActor::RotateActor</strong> method.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void ARotatingActor::RotateActor()\n     {\n         AddActorLocalRotation(ActorRotation);\n     }",
                  "lines_of_code": 4,
                  "id": 60454,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDQ1NCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjAyKzAwOjAwIn0=--123aece2457c1a0df0a4402e66c71c3798a501a13084e5e0592e57395a838479",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to the <strong>ARotatingActor::Tick</strong> method and implement the following code.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void ARotatingActor::Tick(float DeltaTime)\n         {\n             Super::Tick(DeltaTime);\n\t\t\n             if (bCanRotate)\n             {\n                 RotateActor();\n             }\n         }",
                  "lines_of_code": 9,
                  "id": 60455,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDQ1NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjAyKzAwOjAwIn0=--42bf923c782accd58ab813c6c55864aa65829c9a1a3e4db7d6f4629c417dd466",
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
            "content": "RotatingActor.h",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "#pragma once\n\t#include &quot;CoreMinimal.h&quot;\n\t#include &quot;GameFramework/Actor.h&quot;\n\t#include &quot;RotatingActor.generated.h&quot;\n\n\tUCLASS()\n\tclass BPCOMMUNICATION_API ARotatingActor : public AActor\n\t{\n\tGENERATED_BODY()\n\n",
            "lines_of_code": 31,
            "id": 60456,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2MDQ1NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjAyKzAwOjAwIn0=--2ff52e1f144b4290be76f0a7614f152bf53d4b640718ad124b00a97414d2da50",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "RotatingActor.cpp",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "#include &quot;RotatingActor.h&quot;\n\n\t// Sets default values\n\tARotatingActor::ARotatingActor()\n\t{\n\t\t// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n\t\tPrimaryActorTick.bCanEverTick = true;\n\t\tRootComponent = CreateDefaultSubobject&lt;USceneComponent&gt;(TEXT(&quot;SceneComponent&quot;));\n\t\tMeshComp = CreateDefaultSubobject&lt;UStaticMeshComponent&gt;(TEXT(&quot;MeshComp&quot;));\n\t\tMeshComp-&gt;SetupAttachment(RootComponent, FAttachmentTransformRules::KeepRelativeTransform);\n",
            "lines_of_code": 39,
            "id": 60457,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2MDQ1NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjAyKzAwOjAwIn0=--19a463e8ba9a322549ea254ff3776425c249f4490bbd5d105f97dbf4696210f2",
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
                  "content": "<strong>Compile</strong> your code.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "In the editor, navigate to your <strong>C++ Classes folder</strong>, right-click your <strong>RotatingActor</strong> and from the <strong>C++ class actions</strong> dropdown menu, select <strong>Create Blueprint class based on RotatingActor</strong> named <strong>BP_RotatingActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740025,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740025,
                    "file_name": "BpRotateActor.png",
                    "file_size": 46494,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:35.589+00:00",
                    "height": 284,
                    "width": 1124,
                    "storage_key": "0cbcec2e-20cf-44f6-9036-96af6166c9ef",
                    "context": "documentation"
                  },
                  "storage_key": "0cbcec2e-20cf-44f6-9036-96af6166c9ef",
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
                  "content": "In the class defaults for your <strong>BP_RotatingActor</strong> Blueprint, navigate to the <strong>Components </strong>tab, select the <strong>MeshComp</strong> <strong>Static Mesh Component</strong>, then navigate to the <strong>Details panel </strong>and from the <strong>Static Mesh category</strong>,<strong> </strong>select the arrow next to the <strong>Static Mesh variable</strong>.  Lastly, from the dropdown menu, select the <strong>Shape_Cube </strong>static mesh.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740026,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740026,
                    "file_name": "StaticMeshDetails.png",
                    "file_size": 34419,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:35.691+00:00",
                    "height": 426,
                    "width": 563,
                    "storage_key": "58dd2019-689e-4b11-9408-ffd0c964ffc5",
                    "context": "documentation"
                  },
                  "storage_key": "58dd2019-689e-4b11-9408-ffd0c964ffc5",
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
                  "content": "<strong>Compile </strong>and <strong>save </strong>your Blueprint.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "From the <strong>Content Browser</strong>, drag an instance of your <strong>Bp_RotatingActor</strong> into the Level.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740027,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740027,
                    "file_name": "DragRotatingCube.png",
                    "file_size": 1508041,
                    "content_type": "image/png",
                    "created_at": "2025-06-17T15:12:35.789+00:00",
                    "height": 1250,
                    "width": 1243,
                    "storage_key": "3373d921-8280-4990-99e3-b59dc5a68238",
                    "context": "documentation"
                  },
                  "storage_key": "3373d921-8280-4990-99e3-b59dc5a68238",
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
            "content": "Modifying the Third Person Character Class",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this section, you will modify the <strong>BPCommunicationCharacter </strong>class<strong> </strong>to cast to the <strong>Rotating Actor </strong>class and set the <strong>bCanRotate </strong>variable to <strong>True</strong> when your player is nearby.",
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
                  "content": "Open your <strong>BPCommunicationCharacter.h</strong> and implement the following.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "protected:\n             virtual void NotifyActorBeginOverlap(AActor* OtherActor);\n             virtual void NotifyActorEndOverlap(AActor* OtherActor);\n             class USphereComponent* SphereComp;",
                  "lines_of_code": 4,
                  "id": 60458,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDQ1OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjAyKzAwOjAwIn0=--ead1e2d8da404203a89046075036367a4441b31249effd580bf37b8332383fe0",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "In your <strong>BPCommunicationCharacter.cpp</strong> include the following class libraries",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "#include &quot;RotatingActor.h&quot;\n         #include &quot;Components/SphereComponent.h&quot;",
                  "lines_of_code": 2,
                  "id": 60459,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDQ1OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjAyKzAwOjAwIn0=--6bae708e9e999739d6da1a9d2344f4efbc84cdfc087ba8b6a77946689280d774",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "From the constructor <strong>ABPCommunicaionCharacter::BPCommunicationCharacter</strong> declare the following code.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "SphereComp = CreateDefaultSubobject&lt;USphereComponent&gt;(TEXT(&quot;SphereComp&quot;));\n         SphereComp-&gt;AttachToComponent(GetMesh(), FAttachmentTransformRules::KeepRelativeTransform);\n         SphereComp-&gt;SetSphereRadius(200);",
                  "lines_of_code": 3,
                  "id": 60460,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDQ2MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjAyKzAwOjAwIn0=--ebbee1c69f6a37bccdb1e97fec82afce08a77ee99af12b1db64e4ca28d5400fc",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Next, implement the <strong>ABPCommunicationCharacter::NotifyActorBeginOverlap</strong>, and <strong>ABPCommunicationCharacter::NotifyActorEndOverlap</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void ABPCommunicationCharacter::NotifyActorBeginOverlap(AActor* OtherActor)\n         {\n             if (ARotatingActor* RotatingActorCheck =Cast&lt;ARotatingActor&gt;(OtherActor))\n             {\n                 ActorCheck-&gt;SetbCanRotate(true);\n             }\n         }\n\t\t\n         void ABPCommunicationCharacter::NotifyActorEndOverlap(AActor* OtherActor)\n         {\n",
                  "lines_of_code": 15,
                  "id": 60461,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDQ2MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjAyKzAwOjAwIn0=--13df06b11493385c3690483ef96eda8aa76bee5cac5242cfbb14b1920be59b3a",
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
            "content": "BpCommunicationCharacter.h",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\t#pragma once\n\t#include &quot;CoreMinimal.h&quot;\n\t#include &quot;GameFramework/Character.h&quot;\n\t#include &quot;BPCommunicationCharacter.generated.h&quot;\n\n\tUCLASS(config=Game)\n\tclass ABPCommunicationCharacter : public ACharacter\n\t{\n\t\tGENERATED_BODY()\n",
            "lines_of_code": 77,
            "id": 60462,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2MDQ2MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjAyKzAwOjAwIn0=--4d6814b0fa9c7511ef70c42601a4d9ac57b88f4a1a4fa219670f86dec25dbac2",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "BpCommunication.cpp",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\t#include &quot;BPCommunicationCharacter.h&quot;\n\t#include &quot;HeadMountedDisplayFunctionLibrary.h&quot;\n\t#include &quot;Camera/CameraComponent.h&quot;\n\t#include &quot;Components/CapsuleComponent.h&quot;\n\t#include &quot;Components/InputComponent.h&quot;\n\t#include &quot;GameFramework/CharacterMovementComponent.h&quot;\n\t#include &quot;GameFramework/Controller.h&quot;\n\t#include &quot;GameFramework/SpringArmComponent.h&quot;\n\t#include &quot;CeilingLight.h&quot;\n",
            "lines_of_code": 164,
            "id": 60463,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2MDQ2MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjAyKzAwOjAwIn0=--229ff38908870b26a455c39045f42d0b41326f86bc2bb52d30f1b6d288efa3ba",
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
                  "content": "Press Play and approach the <strong>BP_RotateActor </strong>Actor to see it rotate only when the player is nearby.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25740028,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25740028,
                    "file_name": "RotateCube.GIF",
                    "file_size": 13182881,
                    "content_type": "image/gif",
                    "created_at": "2025-06-17T15:12:35.966+00:00",
                    "height": 360,
                    "width": 640,
                    "storage_key": "89bc4752-1064-4dd8-9c98-19104ce66cd3",
                    "context": "documentation"
                  },
                  "storage_key": "89bc4752-1064-4dd8-9c98-19104ce66cd3",
                  "context": "documentation",
                  "width": 600,
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
            "content": "Next Steps",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Now that you know how to use Blueprint casting, take a look at the other communication types referenced in the <a href=\"making-interactive-experiences/interactive-framework/actors/actor-communication\"></a> documentation page.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "RV4",
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
