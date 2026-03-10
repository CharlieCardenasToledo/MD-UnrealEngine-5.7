# Using the OnHit Event

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-onhit-event

> Application Version: 5.7

Imagine you are creating a game that involves any kind of damage to a player, enemy, or object. In that case, chances are you will encounter a situation where you need to determine if those objects were hit by something and if so, what hit them, where the impact point was, or other information regarding the hit detected.
The **OnHit Event** provides this information when the collision occurs, then you can use the data to drive changes in your game. Whether it affects health, destroys an object, or causes other gameplay-related actions.

In this tutorial, you will use the **OnComponentHit** and **Function** [Events](https://dev.epicgames.com/documentation/en-us/unreal-engine/events-in-unreal-engine) to apply damage to an Actor that will be represented by changing the Actor's mesh material. The Events will also apply an impulse at the hit location to push the Actor, simulating the effects of being hit by a projectile and applying force at the hit location.

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1546,
        "excerpt_assignment_id": 1337,
        "blocks": [
          {
            "type": "header",
            "content": "Project Setup",
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
                  "content": "Begin by creating a new <strong>Games</strong> &gt; <strong>First Person</strong> &gt; <strong>Blueprint</strong> Project named <strong>OnHit</strong>.",
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
            "image_id": 25711615,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25711615,
              "file_name": "image_0.png",
              "file_size": 599457,
              "content_type": "image/png",
              "created_at": "2025-06-03T19:37:20.020+00:00",
              "height": 740,
              "width": 1132,
              "storage_key": "0a95fb99-0d91-423b-b563-c62545e28006",
              "context": "documentation"
            },
            "storage_key": "0a95fb99-0d91-423b-b563-c62545e28006",
            "context": "documentation",
            "width": 600,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Creating the Mesh Material",
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
                  "content": "Navigate to the <strong>Content Browser</strong>, and find the <strong>LevelPrototyping/Materials </strong>folder.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Select <strong>MI_SolidBlue</strong>, then duplicate (<strong>CTRL+ D</strong>) and rename the newly duplicated asset <strong>MI_Solid_Red</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711616,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711616,
                    "file_name": "image_1.png",
                    "file_size": 147917,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:20.243+00:00",
                    "height": 318,
                    "width": 1394,
                    "storage_key": "dd18b887-d748-4edd-a334-afcc9d109653",
                    "context": "documentation"
                  },
                  "storage_key": "dd18b887-d748-4edd-a334-afcc9d109653",
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
                  "content": "Double-click to open the asset, then select and edit the <strong>Base Color</strong> to the color red.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711617,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711617,
                    "file_name": "image_2.png",
                    "file_size": 1016072,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:20.401+00:00",
                    "height": 888,
                    "width": 1236,
                    "storage_key": "6b405e3e-f324-49dc-b161-e3e1153497ff",
                    "context": "documentation"
                  },
                  "storage_key": "6b405e3e-f324-49dc-b161-e3e1153497ff",
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
                  "content": "<strong>Save </strong>the asset.",
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
            "content": "Creating the Cube Actor",
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
                  "content": "Navigate to the <strong>Content Browser</strong>, and find the <strong>LevelPrototyping/Meshes </strong>folder.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "<strong>Right-click</strong> on <strong>SM_ChamferCube</strong> Static Mesh and select <strong>Asset Actions &gt;</strong> <strong>Create Blueprint Using This..</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711618,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711618,
                    "file_name": "image_3.png",
                    "file_size": 118647,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:20.604+00:00",
                    "height": 795,
                    "width": 1127,
                    "storage_key": "04c126c0-9bc1-45be-be12-1b8bf8ee8b62",
                    "context": "documentation"
                  },
                  "storage_key": "04c126c0-9bc1-45be-be12-1b8bf8ee8b62",
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
                  "content": "Name your Blueprint <strong>BP_Cube</strong>.",
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
                      "content": "Be sure to choose a folder save location for the new Blueprint.",
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
                  "content": "In the <strong>Details</strong> panel, set <strong>Physics</strong> &gt; <strong>Simulate Physics </strong>to <strong>True</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711619,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711619,
                    "file_name": "image_4.png",
                    "file_size": 26205,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:20.729+00:00",
                    "height": 496,
                    "width": 418,
                    "storage_key": "fbd267f4-e4b0-41d9-a50e-55867e5426fe",
                    "context": "documentation"
                  },
                  "storage_key": "fbd267f4-e4b0-41d9-a50e-55867e5426fe",
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
                  "content": "In the <strong>Details</strong> panel, click <strong>Events</strong> &gt; <strong>On Component Hit</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711620,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711620,
                    "file_name": "image_5.png",
                    "file_size": 10288,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:20.789+00:00",
                    "height": 210,
                    "width": 474,
                    "storage_key": "c718aab5-3c0a-4083-ac65-2be2470a1afb",
                    "context": "documentation"
                  },
                  "storage_key": "c718aab5-3c0a-4083-ac65-2be2470a1afb",
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
                  "content": "This adds a new node to and opens the <strong>Event Graph</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711621,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711621,
                    "file_name": "image_6.png",
                    "file_size": 51150,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:20.847+00:00",
                    "height": 524,
                    "width": 630,
                    "storage_key": "acd89ca4-467b-43c5-bc60-6ddab30ba409",
                    "context": "documentation"
                  },
                  "storage_key": "acd89ca4-467b-43c5-bc60-6ddab30ba409",
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
                  "content": "<strong>Left-click</strong> and drag off of the <strong>Other Actor</strong> pin, then search for and add the <strong>Cast To FirstPersonProjectile</strong> node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711622,
                  "caption": "Here you are casting to another Blueprint called the FirstPersonProjectile Blueprint and making sure that when you hit the BP_Cube, it is the FirstPersonProjectile Blueprint that hits it. If it is, you can apply an additional script to change the mesh's material, signifying that it has taken damage. If it isn't, you won't do anything.",
                  "alt_text": "",
                  "image": {
                    "id": 25711622,
                    "file_name": "image_7.png",
                    "file_size": 63570,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:20.943+00:00",
                    "height": 610,
                    "width": 1008,
                    "storage_key": "7a343b26-7090-42b4-92ed-21575342e0d2",
                    "context": "documentation"
                  },
                  "storage_key": "7a343b26-7090-42b4-92ed-21575342e0d2",
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
                  "content": "Drag off the <strong>Hit</strong> pin and add a <strong>Break Hit Result</strong> node.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711684,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711684,
                    "file_name": "image_8.png.png",
                    "file_size": 240011,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:40:28.447+00:00",
                    "height": 1080,
                    "width": 970,
                    "storage_key": "7d5a8f3c-8bfc-431b-bd41-cfcc7b11c1d2",
                    "context": "documentation"
                  },
                  "storage_key": "7d5a8f3c-8bfc-431b-bd41-cfcc7b11c1d2",
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
                  "content": "\nDrag off the <strong>Hit Actor</strong> pin from the <strong>Break Hit Result</strong> and add the <strong>Apply Point Damage</strong> node.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711685,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711685,
                    "file_name": "image_9.png.png",
                    "file_size": 359638,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:41:31.462+00:00",
                    "height": 1080,
                    "width": 1563,
                    "storage_key": "8c2095ef-ff90-43b9-a40d-aacd9ce9c4bf",
                    "context": "documentation"
                  },
                  "storage_key": "8c2095ef-ff90-43b9-a40d-aacd9ce9c4bf",
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
                  "content": "\nOn the <strong>Apply Point Damage</strong> node, set the <strong>Base Damage</strong> to <strong>100</strong> and set the <strong>Damage Type Class</strong> to <strong>Damage Type</strong>.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711686,
                  "caption": "The Apply Point Damage node specifies the amount of damage, and the location where the damage is inflicted.",
                  "alt_text": "",
                  "image": {
                    "id": 25711686,
                    "file_name": "image_10.png.png",
                    "file_size": 259806,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:42:38.626+00:00",
                    "height": 1080,
                    "width": 951,
                    "storage_key": "b838f07a-e214-4038-86d5-89ecf31efd67",
                    "context": "documentation"
                  },
                  "storage_key": "b838f07a-e214-4038-86d5-89ecf31efd67",
                  "context": "documentation",
                  "width": 300,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "\nOn the <strong>Apply Point Damage</strong> node, connect the remaining wires.\n\n",
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
                        "content": "\nConnect the <strong>As BP First Person Projectile</strong> pin to the <strong>Damage Causer</strong> pin.\n\n",
                        "settings": {
                          "is_hidden": false
                        }
                      }
                    ],
                    [
                      {
                        "type": "paragraph",
                        "content": "\nConnect the <strong>Impact point </strong>to the <strong>Hit from Direction</strong> pin.\n\n",
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
                  "image_id": 25711687,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711687,
                    "file_name": "image_11.png.png",
                    "file_size": 336754,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:43:48.056+00:00",
                    "height": 1080,
                    "width": 1433,
                    "storage_key": "c7ca66be-7cd6-4d07-b80e-9050601b1c62",
                    "context": "documentation"
                  },
                  "storage_key": "c7ca66be-7cd6-4d07-b80e-9050601b1c62",
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
                  "content": "\n<strong>Compile</strong> and <strong>Save</strong>.\n\n",
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
            "content": "Implementing the Damage functionality",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Now that you created functionality to inflict damage on a cube when a projectile collides with it, you need to implement a function that sets the cube mesh's material when it receives damage, then after a delay resets the mesh back to its original material.",
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
                  "content": "\nNavigate to <strong>My Blueprint</strong> &gt; <strong>Functions </strong>and click <strong>Add</strong> (<strong>+</strong>) to create a new function named <strong>OnTakeDamage</strong>.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711688,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711688,
                    "file_name": "image_12.png.png",
                    "file_size": 199786,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:46:25.339+00:00",
                    "height": 1080,
                    "width": 1022,
                    "storage_key": "6fdcab51-1fe0-4104-985e-f6164215fc00",
                    "context": "documentation"
                  },
                  "storage_key": "6fdcab51-1fe0-4104-985e-f6164215fc00",
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
                  "content": "From the <strong>Components</strong> tab, Click and drag the <strong>StaticMesh Component</strong> onto the event graph.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711628,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711628,
                    "file_name": "image_13.png",
                    "file_size": 106617,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:21.536+00:00",
                    "height": 887,
                    "width": 986,
                    "storage_key": "62031831-4b20-41e6-b7b2-ec9ff6d92c15",
                    "context": "documentation"
                  },
                  "storage_key": "62031831-4b20-41e6-b7b2-ec9ff6d92c15",
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
                  "content": "Click and drag off of the Static Mesh pin and from the actions menu select <strong>Set Material</strong>, then change the <strong>Material</strong> parameter to the<strong> MI_Solid_Red</strong> material asset that you created earlier.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711689,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711689,
                    "file_name": "image_14.png.png",
                    "file_size": 263498,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:47:03.071+00:00",
                    "height": 1080,
                    "width": 1916,
                    "storage_key": "184f43b1-d6d9-4f5a-87f1-c4b23f97f99e",
                    "context": "documentation"
                  },
                  "storage_key": "184f43b1-d6d9-4f5a-87f1-c4b23f97f99e",
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
                  "content": "\n<strong>Compile</strong> and <strong>Save</strong>.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "\nNavigate to <strong>My Blueprint</strong> &gt; <strong>Functions</strong> and click <strong>Add</strong>(<strong>+</strong>) to create a new function named <strong>Damage Reset</strong>.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711690,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711690,
                    "file_name": "image_15.png.png",
                    "file_size": 172688,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:47:48.288+00:00",
                    "height": 1080,
                    "width": 919,
                    "storage_key": "2b06429a-9fd1-41d8-803e-6fed62bed9f1",
                    "context": "documentation"
                  },
                  "storage_key": "2b06429a-9fd1-41d8-803e-6fed62bed9f1",
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
                  "content": "\nFrom the <strong>Components</strong> tab, click and drag the <strong>StaticMesh Component</strong> onto the event graph.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "\nClick and drag off of the <strong>Static Mesh</strong> pin and from the actions menu select <strong>Set Material</strong>, then change the <strong>Material</strong> parameter to the <strong>MI_Solid_Blue</strong> material asset.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711691,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711691,
                    "file_name": "image_16.png.png",
                    "file_size": 285414,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:48:28.904+00:00",
                    "height": 1080,
                    "width": 1867,
                    "storage_key": "3e7de425-7fdc-4173-b0f8-501575037aa7",
                    "context": "documentation"
                  },
                  "storage_key": "3e7de425-7fdc-4173-b0f8-501575037aa7",
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
                  "content": "\nClick and drag off the execution pin of the <strong>Apply Point Damage</strong> node, then search for and select the <strong>On Take Damage</strong> function.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711692,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711692,
                    "file_name": "image_17.png.png",
                    "file_size": 314619,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:49:01.767+00:00",
                    "height": 1080,
                    "width": 1658,
                    "storage_key": "aecfef38-0023-42b8-a4b5-56970a87127c",
                    "context": "documentation"
                  },
                  "storage_key": "aecfef38-0023-42b8-a4b5-56970a87127c",
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
                  "content": "\nClick and drag off the execution pin of the <strong>On Take Damage</strong> function, then search for and select <strong>Delay</strong>.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711693,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711693,
                    "file_name": "image_18.png.png",
                    "file_size": 263164,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:49:38.243+00:00",
                    "height": 714,
                    "width": 1920,
                    "storage_key": "136d4ba9-1dde-405e-b0ba-ed30fb3264bc",
                    "context": "documentation"
                  },
                  "storage_key": "136d4ba9-1dde-405e-b0ba-ed30fb3264bc",
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
                  "content": "\nClick and drag off the <strong>Completed</strong> execution pin from the <strong>Delay</strong> node, then search for and select <strong>Damage Reset</strong>.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711694,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711694,
                    "file_name": "image_19.png.png",
                    "file_size": 244714,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:50:19.029+00:00",
                    "height": 651,
                    "width": 1920,
                    "storage_key": "fb684344-cd97-4ab4-972d-4daf66af58fa",
                    "context": "documentation"
                  },
                  "storage_key": "fb684344-cd97-4ab4-972d-4daf66af58fa",
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
                  "content": "\n<strong>Compile</strong> and <strong>Save</strong>.\n\n",
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
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25711635,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25711635,
              "file_name": "image_20.png",
              "file_size": 230687,
              "content_type": "image/png",
              "created_at": "2025-06-03T19:37:22.203+00:00",
              "height": 964,
              "width": 1726,
              "storage_key": "4acc5700-74f9-4b82-b541-7bc1742df174",
              "context": "documentation"
            },
            "storage_key": "4acc5700-74f9-4b82-b541-7bc1742df174",
            "context": "documentation",
            "width": 600,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Setting up the Level",
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
                  "content": "Drag the<strong> BP_Cube</strong> into the level from the <strong>Content Browser</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711696,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711696,
                    "file_name": "image_21.png.png",
                    "file_size": 1242177,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:56:30.491+00:00",
                    "height": 1080,
                    "width": 1215,
                    "storage_key": "1585ad66-50a9-4d95-94c9-52495eb4d1c5",
                    "context": "documentation"
                  },
                  "storage_key": "1585ad66-50a9-4d95-94c9-52495eb4d1c5",
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
                  "content": "\nNavigate to the <strong>Outliner</strong> &gt; <strong>Simulated Cubes</strong>, select all <strong>SM_ChauferCubes</strong> then right-click and select <strong>Replace Selected Actors with</strong> &gt; <strong>BP_Cube</strong>.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711697,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711697,
                    "file_name": "image_22.png.png",
                    "file_size": 258817,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:57:09.253+00:00",
                    "height": 1080,
                    "width": 833,
                    "storage_key": "cd1d6cf6-4a92-4b8e-920b-476b2aef7d0a",
                    "context": "documentation"
                  },
                  "storage_key": "cd1d6cf6-4a92-4b8e-920b-476b2aef7d0a",
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
                  "content": "\nClick <strong>Play</strong> to play in the editor and use the left-mouse button to fire a projectile at the cube.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711699,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711699,
                    "file_name": "image_23.GIF",
                    "file_size": 13182881,
                    "content_type": "image/gif",
                    "created_at": "2025-06-03T20:00:15.628+00:00",
                    "height": 360,
                    "width": 640,
                    "storage_key": "4e60d066-6bea-4bcc-9b4a-afd73693c0f3",
                    "context": "documentation"
                  },
                  "storage_key": "4e60d066-6bea-4bcc-9b4a-afd73693c0f3",
                  "context": "documentation",
                  "width": null,
                  "autoplay": false,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "When you play in the editor, you will see that when you hit the cube with the projectile you fire It causes the cube to take damage and change its mesh material, and applies an impulse at the location where the cube was hit causing it to move opposite the direction of the projectile.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "\nThe amount of force applied is defined inside the <strong>FirstPersonProjectile</strong> Blueprint which uses the <strong>Event Hit</strong> node to determine when the projectile actually hits something.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "\nIn the <strong>Content/FirstPersonBP/Blueprints</strong> folder, open the <strong>FirstPersonProjectile</strong> Blueprint.\n\n",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711710,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711710,
                    "file_name": "image_24.png.png",
                    "file_size": 360421,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T20:02:27.600+00:00",
                    "height": 964,
                    "width": 1920,
                    "storage_key": "405f7057-b949-4bc2-be73-35a30a4a0808",
                    "context": "documentation"
                  },
                  "storage_key": "405f7057-b949-4bc2-be73-35a30a4a0808",
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
            "type": "paragraph",
            "content": "The script in this Blueprint checks to see if the object hit is simulating physics (which you set to true on your cube Blueprint). If it is, it then applies an Impulse at the location it hits (the amount is defined inside the green box). You can adjust this value to increase or decrease the amount of impulse applied when a hit occurs.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "z5E",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1547,
        "excerpt_assignment_id": 1338,
        "blocks": [
          {
            "type": "header",
            "content": "Project Setup",
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
                  "content": "Begin by creating a new <strong>Games</strong> &gt; <strong>First Person</strong> &gt; <strong>C++</strong> Project named <strong>OnHit</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711639,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711639,
                    "file_name": "image_25.png",
                    "file_size": 597466,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:23.200+00:00",
                    "height": 740,
                    "width": 1132,
                    "storage_key": "7c805698-097e-4788-90d6-76379192efb3",
                    "context": "documentation"
                  },
                  "storage_key": "7c805698-097e-4788-90d6-76379192efb3",
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
            "content": "Creating the Mesh Material",
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
                  "content": "Navigate to the <strong>Content Browser</strong>, and find the <strong>LevelPrototyping/Materials </strong>folder.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Select <strong>MI_SolidBlue</strong>, then duplicate (<strong>CTRL+ D</strong>) and rename the newly duplicated asset <strong>MI_Solid_Red</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711640,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711640,
                    "file_name": "image_26.png",
                    "file_size": 147917,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:23.349+00:00",
                    "height": 318,
                    "width": 1394,
                    "storage_key": "6108d51a-563f-42f3-a250-5f7127e9251d",
                    "context": "documentation"
                  },
                  "storage_key": "6108d51a-563f-42f3-a250-5f7127e9251d",
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
                  "content": "Double-click to open the asset, then select and edit the <strong>Base Color</strong> to the color red.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711641,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711641,
                    "file_name": "image_27.png",
                    "file_size": 1016072,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:23.523+00:00",
                    "height": 888,
                    "width": 1236,
                    "storage_key": "bdbc8637-a17e-47cd-8d76-2a7e194aadf7",
                    "context": "documentation"
                  },
                  "storage_key": "bdbc8637-a17e-47cd-8d76-2a7e194aadf7",
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
                  "content": "<strong>Save </strong>the Asset.",
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
            "content": "Creating the Cube Actor",
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
                  "content": "In the <strong>Editor</strong>, click <strong>Add(+)</strong> &gt; <strong>New C++ Class</strong>, then choose<strong> Actor</strong> as your parent class and name your class <strong>Cube</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711642,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711642,
                    "file_name": "image_28.png",
                    "file_size": 30441,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:23.688+00:00",
                    "height": 359,
                    "width": 721,
                    "storage_key": "f13ec163-adbc-4059-878d-a9b31c62643e",
                    "context": "documentation"
                  },
                  "storage_key": "f13ec163-adbc-4059-878d-a9b31c62643e",
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
                  "content": "Declare the following class defaults in your <code>cube.h</code> file",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "UPROPERTY(EditDefaultsOnly, BlueprintReadWrite)\n         class UStaticMeshComponent* CubeMesh;\n\t\t\n         UPROPERTY(EditDefaultsOnly, BlueprintReadWrite)\n         UMaterialInstance* CubeMaterial;\n\t\t\n         UPROPERTY(EditDefaultsOnly, BlueprintReadWrite)\n         UMaterialInstance* DamagedCubeMaterial;\n\t\t\n         FTimerHandle DamageTimer;\n",
                  "lines_of_code": 14,
                  "id": 51951,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk1MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjIxKzAwOjAwIn0=--710aade424eba783afc58dfb0f760cd1709f7db41963570140b18aa9a78afbd6",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Next, in your <code>cube.cpp</code> file, declare the following class libraries.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "#include &quot;Kismet/GameplayStatics.h&quot;\n     #include &quot;OnHitProjectile.h&quot;",
                  "lines_of_code": 2,
                  "id": 51952,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk1MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjIxKzAwOjAwIn0=--0650a643105970c201fc3bbe8e714908990f8323a62b820a4f3a52bf4272730b",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to the cube constructor and implement the following functionality.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "ACube::ACube()\n     {\n         CubeMesh = CreateDefaultSubobject&lt;UStaticMeshComponent&gt;(TEXT(&quot;CubeMesh&quot;));\n         DamagedCubeMaterial = CreateDefaultSubobject&lt;UMaterialInstance&gt;(TEXT(&quot;DamageMaterial&quot;));\n         CubeMaterial = CreateDefaultSubobject&lt;UMaterialInstance&gt;(TEXT(&quot;CubeMaterial&quot;));\n\t\t\n         CubeMesh-&gt;SetSimulatePhysics(true);\n     }",
                  "lines_of_code": 8,
                  "id": 51953,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk1MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjIxKzAwOjAwIn0=--5f4f9f3bdb0d0dfc0c13504966f5964ef230356774844ec6e61c9ac21e305539",
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
            "content": "Implementing the Damage functionality",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Now that you created a cube, you need to implement a function that sets the mesh's material when it receives damage, then after a delay resets the mesh back to its original material.",
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
                  "content": "Declare the following code in your <code>cube.h</code> file.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void OnTakeDamage();\n\t\t\n         void ResetDamage();",
                  "lines_of_code": 3,
                  "id": 51954,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk1NCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjIxKzAwOjAwIn0=--667904ceb2321fe057733963af47f0ba20d6648f9c7e58bbd73c59ad7c2a218c",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to the <code>cube.cpp</code> file and implement the following for the <code>ACube::BeginPlay</code> function.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void ACube::BeginPlay()\n     {\n        CubeMesh-&gt;OnComponentHit.AddDynamic(this, &amp;ACube::OnComponentHit);\n     }",
                  "lines_of_code": 4,
                  "id": 51955,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk1NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjIxKzAwOjAwIn0=--a285c9558b760eb821e6df18077a1836ada964840f7ae8e861f5afde5e3ebf76",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Implement the <code>ACube::OnTakeDamage</code> function.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void ACube::OnTakeDamage()\n     {\n\t\t\n         CubeMesh-&gt;SetMaterial(0, DamagedCubeMaterial);\n         GetWorld()-&gt;GetTimerManager().SetTimer(DamageTimer, this, &amp;ACube::ResetDamage, 1.5f, false);\n     }",
                  "lines_of_code": 6,
                  "id": 51956,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk1NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjIxKzAwOjAwIn0=--de19a2607cac2f2275ec14687c25754f4554ce7041d7932aea49785ece559455",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Next, implement the <code>ACube::ResetDamage</code> function.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void ACube::ResetDamage()\n     {\n         CubeMesh-&gt;SetMaterial(0,CubeMaterial);\n     }",
                  "lines_of_code": 4,
                  "id": 51957,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk1NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjIxKzAwOjAwIn0=--4fb4fd48d65fd04342be73581a63da06087caf4110860ce991b9369198ae38c5",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Finally, navigate to the <code>ACube::OnComponentHit</code> function and implement the following code.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void ACube::OnComponentHit(UPrimitiveComponent* HitComp, AActor* OtherActor, UPrimitiveComponent* OtherComp, FVector NormalImpulse, const FHitResult&amp; Hit)\n     {\n     if (AOnHitProjectile* HitActor = Cast&lt;AOnHitProjectile&gt;(OtherActor))\n     {\n\t\t\n         UGameplayStatics::ApplyDamage(this, 20.0f, nullptr, OtherActor, UDamageType::StaticClass());\n         OnTakeDamage();\n\t\t\n     }\n     }",
                  "lines_of_code": 10,
                  "id": 51958,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk1OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjIxKzAwOjAwIn0=--39b4bdc6d6d1e1b07c79b3b3dc40f38111f4e9566f2fec7f053c697ff54e1aed",
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
                  "content": "In the editor, navigate to <strong>C++ Classes </strong>&gt; <strong>Cube</strong> then right-click on the <strong>Cube Actor</strong> and select <strong>Create Blueprint class based on Cube</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711643,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711643,
                    "file_name": "image_29.png",
                    "file_size": 34974,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:23.795+00:00",
                    "height": 287,
                    "width": 890,
                    "storage_key": "f0fc33e0-0e5e-44b0-b741-89ca6e3c5967",
                    "context": "documentation"
                  },
                  "storage_key": "f0fc33e0-0e5e-44b0-b741-89ca6e3c5967",
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
                  "content": "From the Components tab, select the <strong>Cube Mesh</strong>, then navigate to <strong>Details</strong> &gt; <strong>Static Mesh</strong> and select the <strong>SM_ChamferCube</strong> asset.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711644,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711644,
                    "file_name": "image_30.png",
                    "file_size": 27315,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:23.887+00:00",
                    "height": 407,
                    "width": 476,
                    "storage_key": "2b2431eb-7189-4b0a-aede-d368a95e6bd0",
                    "context": "documentation"
                  },
                  "storage_key": "2b2431eb-7189-4b0a-aede-d368a95e6bd0",
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
                  "content": "In the class defaults of the <strong>BP_Cube</strong>, set the <strong>Cube Material</strong> to the <strong>MI_Solid_Blue</strong> asset, and the <strong>Damaged Cube Material</strong> to the <strong>MI_Solid_Red</strong> asset.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711645,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711645,
                    "file_name": "image_31.png",
                    "file_size": 21622,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:23.966+00:00",
                    "height": 209,
                    "width": 439,
                    "storage_key": "4fe8516e-6f76-4da7-ad1a-a9fc51cf804b",
                    "context": "documentation"
                  },
                  "storage_key": "4fe8516e-6f76-4da7-ad1a-a9fc51cf804b",
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
                  "content": "<strong>Compile</strong> and <strong>Save</strong>.",
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
            "content": "CubeActor.h",
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
            "code_preview": "#pragma once\n\n\t\t#include &quot;CoreMinimal.h&quot;\n\t\t#include &quot;GameFramework/Actor.h&quot;\n\t\t#include &quot;Cube.generated.h&quot;\n\n\t\tUCLASS()\n\t\tclass ONHIT_API ACube : public AActor\n\t\t{\n\t\t\tGENERATED_BODY()\n",
            "lines_of_code": 42,
            "id": 51959,
            "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk1OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjIxKzAwOjAwIn0=--74d31f0211d37ec80aad37d76f824aad2af2fe48f0bb6bd60490792cad66e3c3",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "CubeActor.cpp",
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
            "code_preview": "#include &quot;Cube.h&quot;\n\t\t#include &quot;Kismet/GameplayStatics.h&quot;\n\t\t#include &quot;OnHitProjectile.h&quot;\n\n\t\t// Sets default values\n\t\tACube::ACube()\n\t\t{\n\t\t\t// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n\t\t\tPrimaryActorTick.bCanEverTick = true;\n\n",
            "lines_of_code": 52,
            "id": 51960,
            "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk2MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjIxKzAwOjAwIn0=--42b07ae3aa29d458f45e67558049325198a7f7ec96edd75ff04f7e704c243592",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Setting up the Level",
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
                  "content": "Drag the<strong> BP_Cube</strong> into the level from the <strong>Content Browser</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711646,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711646,
                    "file_name": "image_32.png",
                    "file_size": 1099108,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:24.033+00:00",
                    "height": 961,
                    "width": 1081,
                    "storage_key": "2b7197ef-8b44-4537-a03f-6a18a18bd3a1",
                    "context": "documentation"
                  },
                  "storage_key": "2b7197ef-8b44-4537-a03f-6a18a18bd3a1",
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
                  "content": "Navigate to the <strong>Outliner</strong> &gt; <strong>Simulated Cubes</strong>, select all <strong>SM_ChauferCubes</strong> then right-click and select <strong>Replace Selected Actors with</strong> &gt; <strong>BP_Cube</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711647,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711647,
                    "file_name": "image_33.png",
                    "file_size": 105846,
                    "content_type": "image/png",
                    "created_at": "2025-06-03T19:37:24.208+00:00",
                    "height": 880,
                    "width": 679,
                    "storage_key": "386f981d-6b3b-43f8-b8a3-fab1539cfed1",
                    "context": "documentation"
                  },
                  "storage_key": "386f981d-6b3b-43f8-b8a3-fab1539cfed1",
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
                  "content": "Click <strong>Play</strong> to play in the editor and use the left-mouse button to fire a projectile at the cube.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "When you play in the editor, you will see that when you hit the cube with the projectile fired it causes the cube to take damage and change its mesh material, and applies an impulse at the location where it was hit causing it to move opposite the direction of the projectile.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25711714,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 25711714,
                    "file_name": "image_34.GIF",
                    "file_size": 13182881,
                    "content_type": "image/gif",
                    "created_at": "2025-06-03T20:06:34.717+00:00",
                    "height": 360,
                    "width": 640,
                    "storage_key": "8bb51b60-081a-4245-a5bd-dfb1ab1a325c",
                    "context": "documentation"
                  },
                  "storage_key": "8bb51b60-081a-4245-a5bd-dfb1ab1a325c",
                  "context": "documentation",
                  "width": null,
                  "autoplay": false,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "The amount of force applied is defined inside the <code>OnHitProjectile.cpp</code> file which uses the <strong>OnHit</strong> function to determine when the projectile actually hits something.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void AOnHitCPPProjectile::OnHit(UPrimitiveComponent* HitComp, AActor* OtherActor, UPrimitiveComponent* OtherComp, FVector NormalImpulse, const FHitResult&amp; Hit)\n     {\n\t\t\n         // Only add impulse and destroy projectile if we hit a physics\n         if ((OtherActor != nullptr) &amp;&amp; (OtherActor != this) &amp;&amp; (OtherComp != nullptr) &amp;&amp; OtherComp-&gt;IsSimulatingPhysics())\n         {\n             OtherComp-&gt;AddImpulseAtLocation(GetVelocity() * 100.0f, GetActorLocation());\n\t\t\n             Destroy();\n         }\n",
                  "lines_of_code": 12,
                  "id": 51961,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo1MTk2MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjIxKzAwOjAwIn0=--0179cdf44bad61052904dad82f3d298ad477e707a9d758e6f2e33e232cd98314",
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
        "excerpt_hash_id": "5JN",
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
