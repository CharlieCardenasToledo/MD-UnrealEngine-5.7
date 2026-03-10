# Direct Actor Communication Quick Start Guide

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/direct-actor-communication-quick-start-guide-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1773,
        "excerpt_assignment_id": 1440,
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
            "content": "Direct Actor communication is a common method of sharing information between Actors in your Level.\nThis method requires a reference to the target Actor so you can access it from your working Actor. This communication method uses a one-to-one relationship between your working Actor and your target Actor.\nIn this Quick Start guide, you will learn how to use direct Actor communication to access information from a target Actor in order to use its functions.",
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
                  "image_id": 25748738,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748738,
                    "file_name": "image_0.png",
                    "file_size": 80765,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:17.598+00:00",
                    "height": 774,
                    "width": 1110,
                    "storage_key": "43c7e21d-3105-407a-b742-4d224d115b8f",
                    "context": "documentation"
                  },
                  "storage_key": "43c7e21d-3105-407a-b742-4d224d115b8f",
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
                  "image_id": 25748739,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748739,
                    "file_name": "image_1.png",
                    "file_size": 228409,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:17.886+00:00",
                    "height": 774,
                    "width": 1110,
                    "storage_key": "ffe81583-4703-4171-987d-d1238e6d29ef",
                    "context": "documentation"
                  },
                  "storage_key": "ffe81583-4703-4171-987d-d1238e6d29ef",
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
                  "image_id": 25748740,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748740,
                    "file_name": "image_2.png",
                    "file_size": 70174,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:18.084+00:00",
                    "height": 774,
                    "width": 1110,
                    "storage_key": "26945a1c-63eb-4f56-835c-db504e782c08",
                    "context": "documentation"
                  },
                  "storage_key": "26945a1c-63eb-4f56-835c-db504e782c08",
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
            "content": "You have created a new Third Person project and are now ready to learn about direct Actor communication.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "2 - Adding Direct Actor Communication",
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
                  "content": "Go to <strong>Starter Content &gt; Blueprints</strong> inside the <strong>Content Browser</strong> and drag the <strong>Blueprint_CeilingLight </strong>actor into the Level.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748741,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748741,
                    "file_name": "image_3.png",
                    "file_size": 980535,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:18.204+00:00",
                    "height": 1042,
                    "width": 1671,
                    "storage_key": "949afbf1-d18d-4737-94ef-493947cec8a1",
                    "context": "documentation"
                  },
                  "storage_key": "949afbf1-d18d-4737-94ef-493947cec8a1",
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
                  "content": "Select your <strong>ThirdPersonCharacter </strong>Actor in the Level and position it closer to the lamp.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748742,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748742,
                    "file_name": "image_4.png",
                    "file_size": 548979,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:18.399+00:00",
                    "height": 711,
                    "width": 997,
                    "storage_key": "2f49cd3a-d27b-407e-847f-c79ee5d648a3",
                    "context": "documentation"
                  },
                  "storage_key": "2f49cd3a-d27b-407e-847f-c79ee5d648a3",
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
                  "content": "With your <strong>ThirdPersonCharacter </strong>Actor selected, go to the <strong>World Outliner</strong> and click <strong>Edit ThirdPersonCharacter</strong> to open the Blueprint editor.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748743,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748743,
                    "file_name": "image_5.png",
                    "file_size": 38716,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:18.801+00:00",
                    "height": 362,
                    "width": 501,
                    "storage_key": "4c5506d8-240e-4a2c-a889-0da25033f90d",
                    "context": "documentation"
                  },
                  "storage_key": "4c5506d8-240e-4a2c-a889-0da25033f90d",
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
                  "content": "Go to the <strong>Variables </strong>section and click the <strong>+ Variable</strong> button to create a new variable.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748744,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748744,
                    "file_name": "image_6.png",
                    "file_size": 7518,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:18.862+00:00",
                    "height": 137,
                    "width": 390,
                    "storage_key": "d4460372-d648-49c8-accd-3cfa445f371b",
                    "context": "documentation"
                  },
                  "storage_key": "d4460372-d648-49c8-accd-3cfa445f371b",
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
                  "content": "Name the variable <strong>LampReference</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Go to the <strong>Details </strong>panel and click the <strong>Variable Type</strong> dropdown. Search for and select the <strong>Object Reference</strong> for the <strong>Blueprint Ceiling Light</strong> as shown below.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748745,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748745,
                    "file_name": "image_7.png",
                    "file_size": 21563,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:18.940+00:00",
                    "height": 273,
                    "width": 520,
                    "storage_key": "922ce76b-8bfe-40ce-a99a-976c483f6730",
                    "context": "documentation"
                  },
                  "storage_key": "922ce76b-8bfe-40ce-a99a-976c483f6730",
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
                  "content": "Finally, enable the <strong>Instance Editable</strong> checkbox and <strong>Compile </strong>and <strong>Save </strong>the Blueprint.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748746,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748746,
                    "file_name": "image_8.png",
                    "file_size": 7772,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:19.042+00:00",
                    "height": 119,
                    "width": 364,
                    "storage_key": "65b472a0-7f8b-4336-aa44-1b4e78adc1f5",
                    "context": "documentation"
                  },
                  "storage_key": "65b472a0-7f8b-4336-aa44-1b4e78adc1f5",
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
                  "content": "In the <strong>Event Graph</strong>, right-click and search for and select the <strong>F </strong>key to create the input node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748747,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748747,
                    "file_name": "image_9.png",
                    "file_size": 23299,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:19.130+00:00",
                    "height": 445,
                    "width": 449,
                    "storage_key": "2a018f9e-dea3-45f1-96e5-1aa5de7340b1",
                    "context": "documentation"
                  },
                  "storage_key": "2a018f9e-dea3-45f1-96e5-1aa5de7340b1",
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
                  "content": "Drag from the <strong>Pressed </strong>pin of the <strong>F Key </strong>node and search for and select <strong>Flip Flop</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748748,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748748,
                    "file_name": "image_10.png",
                    "file_size": 18498,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:19.286+00:00",
                    "height": 186,
                    "width": 567,
                    "storage_key": "bae479f0-ecc5-4331-82c1-b2f9ed4aaf4b",
                    "context": "documentation"
                  },
                  "storage_key": "bae479f0-ecc5-4331-82c1-b2f9ed4aaf4b",
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
                  "content": "Drag the <strong>Lamp Reference</strong> variable into the <strong>Event Graph</strong> and select <strong>Get LampReference</strong>. Drag from the pin and search for and select <strong>Get Point Light 1</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748749,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748749,
                    "file_name": "image_11.png",
                    "file_size": 58308,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:19.389+00:00",
                    "height": 464,
                    "width": 610,
                    "storage_key": "dd6680b5-2fe6-416f-91c0-d085fb3b3c62",
                    "context": "documentation"
                  },
                  "storage_key": "dd6680b5-2fe6-416f-91c0-d085fb3b3c62",
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
                  "content": "Drag from the <strong>Point Light 1</strong> pin and search for and select <strong>Set Visibility</strong>. Connect the <strong>A pin</strong> from the <strong>Flip Flop</strong> node to the <strong>Set Visibility</strong> node as shown below.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748750,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748750,
                    "file_name": "image_12.png",
                    "file_size": 59348,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:19.471+00:00",
                    "height": 204,
                    "width": 969,
                    "storage_key": "ad8121e5-31bd-4567-9296-bc5e8c4abbf9",
                    "context": "documentation"
                  },
                  "storage_key": "ad8121e5-31bd-4567-9296-bc5e8c4abbf9",
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
                  "content": "Copy the <strong>Lamp Reference</strong>, <strong>Point Lamp 1</strong>, and <strong>Set Visibility</strong> nodes and connect them to the <strong>B</strong> Pin of the <strong>Flip Flop</strong> Node. Enable the<strong> New Visibility</strong> checkbox as shown below.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748751,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748751,
                    "file_name": "image_13.png",
                    "file_size": 110273,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:19.576+00:00",
                    "height": 387,
                    "width": 969,
                    "storage_key": "bdb3fd1f-af76-4123-9e61-ae2c41a4580b",
                    "context": "documentation"
                  },
                  "storage_key": "bdb3fd1f-af76-4123-9e61-ae2c41a4580b",
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
            "content": "In this section you modified your <strong>ThirdPersonCharacter </strong>Blueprint Actor to use a reference to the lamp Actor and turn the lamp on and off by pressing the F key.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "3 - Interacting with the Lamp Actor",
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
                  "content": "Select the <strong>ThirdPersonCharacter </strong>Actor in your Level and from the <strong>Details </strong>panel click the <strong>Lamp Reference</strong> dropdown. Search for and select the <strong>Blueprint_CeilingLight </strong>Blueprint.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748752,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748752,
                    "file_name": "image_14.png",
                    "file_size": 505933,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:19.690+00:00",
                    "height": 754,
                    "width": 1165,
                    "storage_key": "4a1b5a48-f0a8-4565-acb8-4ddcb76d186b",
                    "context": "documentation"
                  },
                  "storage_key": "4a1b5a48-f0a8-4565-acb8-4ddcb76d186b",
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
                  "content": "Press Play to go into Play Mode and press the <strong>F key</strong> to turn the lamp on and off.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748753,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748753,
                    "file_name": "image_15.gif",
                    "file_size": 5026898,
                    "content_type": "image/gif",
                    "created_at": "2025-06-19T15:30:19.948+00:00",
                    "height": 799,
                    "width": 1600,
                    "storage_key": "a14e2b74-ce94-4927-89b1-f1050afae602",
                    "context": "documentation"
                  },
                  "storage_key": "a14e2b74-ce94-4927-89b1-f1050afae602",
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
            "content": "Section Results",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this section you added the Ceiling Lamp Actor reference to the <strong>ThirdPersonCharacter </strong>Blueprint Actor and you turned the light on and off by pressing the F key.",
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
            "content": "Now that you know how to use direct Actor communication, take a look at the other types of communication referenced in the <a href=\"making-interactive-experiences/interactive-framework/actors/actor-communication\"></a> documentation page.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "0oz",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1774,
        "excerpt_assignment_id": 1441,
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
            "content": "Direct Actor communication is a common method of sharing information between Actors in your Level.\nThis method requires a reference to the target Actor so you can access it from your working Actor. This communication method uses a one-to-one relationship between your working Actor and your target Actor.\nIn this Quick Start guide, you will learn how to use direct Actor communication to access information from a target Actor in order to use its functions.",
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
                  "image_id": 25748754,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748754,
                    "file_name": "image_0.png",
                    "file_size": 80765,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:20.584+00:00",
                    "height": 774,
                    "width": 1110,
                    "storage_key": "a0abdaa5-bd2f-4a04-8f08-d6f6a10ac627",
                    "context": "documentation"
                  },
                  "storage_key": "a0abdaa5-bd2f-4a04-8f08-d6f6a10ac627",
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
                  "image_id": 25748755,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748755,
                    "file_name": "image_1.png",
                    "file_size": 228409,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:20.813+00:00",
                    "height": 774,
                    "width": 1110,
                    "storage_key": "5a8a8cdb-0121-4f67-8d77-3996ec1d8093",
                    "context": "documentation"
                  },
                  "storage_key": "5a8a8cdb-0121-4f67-8d77-3996ec1d8093",
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
                  "content": "Select <strong>C++ </strong>and <strong>With Starter Content</strong> options and click <strong>Create Project</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748756,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748756,
                    "file_name": "image_2.png",
                    "file_size": 233661,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:21.027+00:00",
                    "height": 1428,
                    "width": 2048,
                    "storage_key": "160635fb-3849-4f14-962f-84cd614634e4",
                    "context": "documentation"
                  },
                  "storage_key": "160635fb-3849-4f14-962f-84cd614634e4",
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
            "content": "You have created a new Third Person project and are now ready to learn about direct Blueprint communication.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "2 - Creating the Ceiling Light Actor",
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
                  "content": "From the <a data-document-id=\"3228682\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-cplusplus-class-wizard-in-unreal-engine\">C++ Class Wizard</a>, create a new Actor class named <strong>CeilingLight</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748757,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748757,
                    "file_name": "image_3.png",
                    "file_size": 271113,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:21.260+00:00",
                    "height": 1237,
                    "width": 2048,
                    "storage_key": "9b5dd294-fca5-4e7c-9429-b3140969d80a",
                    "context": "documentation"
                  },
                  "storage_key": "9b5dd294-fca5-4e7c-9429-b3140969d80a",
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
                  "content": "In the class defaults of <strong>CeilingLight.h</strong> implement the following code.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "protected:\n            UPROPERTY(EditInstanceOnly, BlueprintReadWrite)\n            USceneComponent* SceneComp;\n\t\t\n            UPROPERTY(EditInstanceOnly, BlueprintReadWrite)\n            class UPointLightComponent* PointLightComp;\n\t\t\n            UPROPERTY(EditInstanceOnly, BlueprintReadWrite)\n            UStaticMeshComponent* StaticMeshComp;\n\t\t\n",
                  "lines_of_code": 21,
                  "id": 64350,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2NDM1MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ5KzAwOjAwIn0=--1745f337759db3d581c76c06c4d7b1b1054a01b346eb6bd0e6ccea5a943cc974",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Next navigate to <strong>CeilingLight.Cpp</strong> and declare the following Include library.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "#include &quot;Components/PointLightComponent.h&quot;",
                  "lines_of_code": 1,
                  "id": 64351,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2NDM1MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ5KzAwOjAwIn0=--3f27bb41de56780eb47aa9fccd6ce3a8aec5b11fd7da502e0beecfd6a13b9d0e",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "From the constructor <strong>ACeilingLight::CeilingLight</strong> declare the following.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "ACeilingLight::ACeilingLight()\n         {\n             // Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n             PrimaryActorTick.bCanEverTick = true;\n             SceneComp = CreateDefaultSubobject&lt;USceneComponent&gt;(TEXT(&quot;SceneComp&quot;));\n             PointLightComp = CreateDefaultSubobject&lt;UPointLightComponent&gt;(TEXT(&quot;PointLightComp&quot;));\n             StaticMeshComp = CreateDefaultSubobject&lt;UStaticMeshComponent&gt;(TEXT(&quot;StaticMeshComp&quot;));\n             SceneComp = RootComponent;\n             PointLightComp-&gt;AttachToComponent(SceneComp,FAttachmentTransformRules::KeepRelativeTransform);\n             StaticMeshComp-&gt;AttachToComponent(SceneComp, FAttachmentTransformRules::KeepRelativeTransform);\n",
                  "lines_of_code": 19,
                  "id": 64352,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2NDM1MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ5KzAwOjAwIn0=--8d857b235e3c7c23b86e68079804bd258797f2ec2ec3b533aee65d938f7d0c4a",
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
            "content": "CeilingLight.h",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "// Fill out your copyright notice in the Description page of Project Settings.\n\t#pragma once\n\n\t#include &quot;CoreMinimal.h&quot;\n\t#include &quot;GameFramework/Actor.h&quot;\n\t#include &quot;CeilingLight.generated.h&quot;\n\n\tUCLASS()\n\tclass BPCOMMUNICATION_API ACeilingLight : public AActor\n\t{\n",
            "lines_of_code": 47,
            "id": 64353,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2NDM1MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ5KzAwOjAwIn0=--df7e1ddacfe5297482d9cf1336059da47c773a8de0dee36ab34282c3784abca0",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "CeilingLight.cpp",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "//Copyright Epic Games, Inc. All Rights Reserved.\n\t#include &quot;CeilingLight.h&quot;\n\t#include &quot;Components/PointLightComponent.h&quot;\n\n\t// Sets default values\n\tACeilingLight::ACeilingLight()\n\t{\n\t\t// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n\t\tPrimaryActorTick.bCanEverTick = true;\n\t\tSceneComp = CreateDefaultSubobject&lt;USceneComponent&gt;(TEXT(&quot;SceneComp&quot;));\n",
            "lines_of_code": 51,
            "id": 64354,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2NDM1NCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ5KzAwOjAwIn0=--f9e9ef4740375fc7f7e2b1951db0b28e93331241c4d15d2e7572be7963f11a44",
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
                  "content": "From the <strong>C++ Classes folder</strong>, right-click your <strong>CeilingLight</strong> Actor, then from the <strong>C++ Class Actions</strong> dropdown menu, select <strong>Create Blueprint class based on CeilingLight</strong>. Name your Blueprint <strong>BP_CeilingLight</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748758,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748758,
                    "file_name": "image_4.png",
                    "file_size": 307390,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:21.491+00:00",
                    "height": 1051,
                    "width": 2048,
                    "storage_key": "0d60e7cb-7b84-460c-96ac-f23399bb40fb",
                    "context": "documentation"
                  },
                  "storage_key": "0d60e7cb-7b84-460c-96ac-f23399bb40fb",
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
                  "content": "From the <strong>BP_CeilingLight</strong> class defaults, navigate to the <strong>Components</strong> panel, then select the <strong>StaticMeshComp</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748759,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748759,
                    "file_name": "image_5.png",
                    "file_size": 59315,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:21.782+00:00",
                    "height": 530,
                    "width": 833,
                    "storage_key": "48362a6c-d8f6-46cb-8857-7cfd381589b3",
                    "context": "documentation"
                  },
                  "storage_key": "48362a6c-d8f6-46cb-8857-7cfd381589b3",
                  "context": "documentation",
                  "width": 400,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "From the <strong>Details </strong>panel, navigate to the <strong>Static Mesh category</strong>, select the dropdown arrow next to the <strong>Static Mesh</strong> variable, then search and select for <strong>SM_Lamp_Ceiling</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748760,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748760,
                    "file_name": "image_6.png",
                    "file_size": 80666,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:21.857+00:00",
                    "height": 646,
                    "width": 1102,
                    "storage_key": "604ff94f-3a76-45b6-b26d-8c005611cac9",
                    "context": "documentation"
                  },
                  "storage_key": "604ff94f-3a76-45b6-b26d-8c005611cac9",
                  "context": "documentation",
                  "width": 400,
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
              ],
              [
                {
                  "type": "paragraph",
                  "content": "From the <strong>Content Browser</strong>, drag an instance of your <strong>BP_CeilingLight Actor</strong> into your Level.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748761,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748761,
                    "file_name": "image_7.png",
                    "file_size": 989285,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:22.058+00:00",
                    "height": 1099,
                    "width": 2048,
                    "storage_key": "6f52846e-70d8-418f-84a9-b1dd922bc398",
                    "context": "documentation"
                  },
                  "storage_key": "6f52846e-70d8-418f-84a9-b1dd922bc398",
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
            "content": "Modifying the ThirdPersonCharacter Class",
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
                  "content": "Navigate to your C++ Classes folder, and double-click the <strong>BPCommunicationCharacter</strong> class to open its <strong>BPCommunicationCharacter.h</strong>, then declare the following code in the class defaults.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "protected:\n             UPROPERTY(EditInstanceOnly, BlueprintReadWrite)\n             class ACeilingLight* CeilingLightToToggle;\n             void ToggleCeilingLight();",
                  "lines_of_code": 4,
                  "id": 64355,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2NDM1NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ5KzAwOjAwIn0=--7d21b8e748eba8452534c6a6de7ca2f931fa4da47928b1c01ea7075f271a775f",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to your <strong>BPCommunicationCharacter.cpp</strong>, and declare the following include.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "#include &quot;CeilingLight.h&quot;",
                  "lines_of_code": 1,
                  "id": 64356,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2NDM1NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ5KzAwOjAwIn0=--72c626a2d10acc25be5f87c7125064cf8077fb73910d23c59ed8184211e20d13",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Implement your <strong>ABPCommunicationCharacter::ToggleCeilingLight</strong> method.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void ABPCommunicationCharacter::ToggleCeilingLight()\n         {\n             if (CeilingLightToToggle)\n                 {\n                   CeilingLightToToggle-&gt;TurnOffLight();\n                 }\n         }",
                  "lines_of_code": 7,
                  "id": 64357,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2NDM1NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ5KzAwOjAwIn0=--d8474f2978deeb42b24f081c4dfeea3be8b696d374be3425cfe80ef7c58df029",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to the <strong>ABPCommunicationCharacter::SetupPlayerInputComponent</strong> method and declare the following.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "PlayerInputComponent-&gt;BindAction(&quot;Use&quot;, IE_Pressed, this, &amp;ABPCommunicationCharacter::ToggleCeilingLight);",
                  "lines_of_code": 1,
                  "id": 64358,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2NDM1OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ5KzAwOjAwIn0=--651e221e8752894556b1d4fb5f741f38312711b58c50ca29688875c8b19a8310",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "In the <strong>Editor</strong>, navigate to <strong>Edit &gt; Project Settings &gt; Input</strong>.  From the <strong>Bindings </strong>category, navigate to the <strong>Action Mappings</strong> then click the <strong>Add (+)</strong> button to create a new <strong>Action mapping</strong> named <strong>Use</strong>, and select the <strong>E</strong> key for the <strong>key value</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748762,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748762,
                    "file_name": "image_8.png",
                    "file_size": 316717,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:22.282+00:00",
                    "height": 1282,
                    "width": 2048,
                    "storage_key": "85db4feb-1b4e-453a-ac6d-ec6c862b35de",
                    "context": "documentation"
                  },
                  "storage_key": "85db4feb-1b4e-453a-ac6d-ec6c862b35de",
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
            "content": "BPCommunicationCharacter.h",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\t#pragma once\n\n\t#include &quot;CoreMinimal.h&quot;\n\t#include &quot;GameFramework/Character.h&quot;\n\t#include &quot;BPCommunicationCharacter.generated.h&quot;\n\n\tUCLASS(config=Game)\n\tclass ABPCommunicationCharacter : public ACharacter\n\t{\n",
            "lines_of_code": 77,
            "id": 64359,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2NDM1OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ5KzAwOjAwIn0=--c5fceec60a2e5ed9fdbc86115f1eb681930e56c4ceb8c5894d2229ca03d5f9e7",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "BPCommunicationCharacter.cpp",
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
            "lines_of_code": 142,
            "id": 64360,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2NDM2MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjQ5KzAwOjAwIn0=--1741befe18dc335404d92f4c96a1225e57bfbab9544eb2e2a2bf752f94186dbd",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "3 - Interacting with the Lamp Blueprint",
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
                  "content": "Select your <strong>ThirdPersonCharacter </strong>Blueprint in the Level and position it closer to the lamp.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748763,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748763,
                    "file_name": "image_9.png",
                    "file_size": 548979,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:22.462+00:00",
                    "height": 711,
                    "width": 997,
                    "storage_key": "cde79130-9806-42ad-94f2-c5582114f301",
                    "context": "documentation"
                  },
                  "storage_key": "cde79130-9806-42ad-94f2-c5582114f301",
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
                  "content": "With your <strong>ThirdPersonCharacter </strong>selected, navigate to the <strong>Details </strong>panel, then from the BPCommunication Character category, find the <strong>Ceiling Light To Toggle </strong>variable, and select the arrow adjacent to it. From the dropdown menu, search for and select the <strong>BP_CeilingLight </strong>Actor.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748764,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748764,
                    "file_name": "image_10.png",
                    "file_size": 107904,
                    "content_type": "image/png",
                    "created_at": "2025-06-19T15:30:22.727+00:00",
                    "height": 786,
                    "width": 872,
                    "storage_key": "98edd89a-cac2-4909-9495-a63de341f65f",
                    "context": "documentation"
                  },
                  "storage_key": "98edd89a-cac2-4909-9495-a63de341f65f",
                  "context": "documentation",
                  "width": 400,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Press <strong>Play</strong> to go into <strong>PlE </strong>(Play-in Editor) mode and press the <strong>E key</strong> to turn the lamp on and off.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25748765,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25748765,
                    "file_name": "image_11.gif",
                    "file_size": 5026898,
                    "content_type": "image/gif",
                    "created_at": "2025-06-19T15:30:22.891+00:00",
                    "height": 799,
                    "width": 1600,
                    "storage_key": "52aedfc2-c0dd-4fd4-a511-f46f575345cc",
                    "context": "documentation"
                  },
                  "storage_key": "52aedfc2-c0dd-4fd4-a511-f46f575345cc",
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
            "content": "Section Results",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this section you added the Ceiling Light Actor reference to the <strong>ThirdPersonCharacter </strong>Blueprint and you turned the light on and off by pressing the E key.",
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
            "content": "Now that you know how to use direct Blueprint communication type, take a look at the other communication types referenced in the <a href=\"making-interactive-experiences/interactive-framework/actors/actor-communication\"></a> documentation page.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "oY0",
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
