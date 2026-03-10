# Keys and Curves

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/keys-and-curves-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 903,
        "excerpt_assignment_id": 603,
        "blocks": [
          {
            "type": "paragraph",
            "content": "A <strong>Curve</strong> defines a track of interpolated points to evaluate over a given range. Curves can be <strong>vectors</strong>, <strong>floats</strong>, and <strong>colors</strong>. Each track can have any number of <strong>keys</strong> that define a time and value. The data can be interpolated between these keys to calculate the value at any point during the Timeline.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Working with Keys and Curves",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this example, you will create a <strong>Curve Float</strong> that defines a curve of interpolated float points to evaluate over a given range.",
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
                  "content": "For creation the new <strong>Actor</strong> Blueprint Class, navigate to the <strong>Content Browser</strong>, select <strong>Add (+) &gt; Blueprint Class</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559846,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559846,
                    "file_name": "01_AddBPClass.png",
                    "file_size": 22798,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:52.768+00:00",
                    "height": 280,
                    "width": 400,
                    "storage_key": "b8a8455e-be25-45dd-800f-708816385d31",
                    "context": "documentation"
                  },
                  "storage_key": "b8a8455e-be25-45dd-800f-708816385d31",
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
                  "content": "Select <strong>Actor</strong> as a Parent Class and name created blueprint <strong>ExampleTimelineComponent</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559847,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559847,
                    "file_name": "02_SelectActor.png",
                    "file_size": 60422,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:52.949+00:00",
                    "height": 397,
                    "width": 600,
                    "storage_key": "57fa1fa9-3460-4c57-acd5-7236b6f2dc3c",
                    "context": "documentation"
                  },
                  "storage_key": "57fa1fa9-3460-4c57-acd5-7236b6f2dc3c",
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
                  "content": "Double-click your timeline component to open the <strong>Timeline Editor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to the <strong>Event Graph</strong> window, right click the <strong>Graph</strong> search for and select the <strong>Add Timeline</strong> node. Double-click created timeline node to open <strong>Timeline Editor</strong> window.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559848,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559848,
                    "file_name": "03_TimelineNode.png",
                    "file_size": 76033,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:53.034+00:00",
                    "height": 372,
                    "width": 600,
                    "storage_key": "afae556f-0a87-4c01-be06-70d5b74231f7",
                    "context": "documentation"
                  },
                  "storage_key": "afae556f-0a87-4c01-be06-70d5b74231f7",
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
                  "content": "Click the <strong>Track(+) &gt; Add Float Track</strong> to add a CurveFloat to your Timeline Component.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559849,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559849,
                    "file_name": "04_AddFloatTrack.png",
                    "file_size": 21176,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:53.245+00:00",
                    "height": 220,
                    "width": 715,
                    "storage_key": "b34f6f5c-348a-4d48-991e-0cb3402382b6",
                    "context": "documentation"
                  },
                  "storage_key": "b34f6f5c-348a-4d48-991e-0cb3402382b6",
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
                  "content": "<strong>Timeline Editor</strong> with created CurveFloat looks as following:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559850,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559850,
                    "file_name": "05_TimelineEditor.png",
                    "file_size": 102791,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:53.479+00:00",
                    "height": 645,
                    "width": 1338,
                    "storage_key": "9ed95c9e-b803-418d-83e5-d24f7a27cbc9",
                    "context": "documentation"
                  },
                  "storage_key": "9ed95c9e-b803-418d-83e5-d24f7a27cbc9",
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
            "content": "Adding Keys",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Keys are added by holding the <strong>Shift</strong> key and clicking on the gray bar, or by right clicking on the gray bar and selecting the action <strong>Add Key To CurveFloat</strong> from the drop down menu.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24559851,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24559851,
              "file_name": "06_AddCurveFloat.png",
              "file_size": 30107,
              "content_type": "image/png",
              "created_at": "2025-05-02T19:19:53.715+00:00",
              "height": 440,
              "width": 740,
              "storage_key": "bcc1b21f-ea0f-4fe3-b7e1-dee41a4fded9",
              "context": "documentation"
            },
            "storage_key": "bcc1b21f-ea0f-4fe3-b7e1-dee41a4fded9",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Editing Keys",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "The time and value of the key can be set by clicking the key and entering the values into the time and value fields near the top of the track.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24559852,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24559852,
              "file_name": "07_SetFloat.png",
              "file_size": 31049,
              "content_type": "image/png",
              "created_at": "2025-05-02T19:19:53.792+00:00",
              "height": 440,
              "width": 740,
              "storage_key": "7691b1e2-00f4-40b6-a585-c512324e8939",
              "context": "documentation"
            },
            "storage_key": "7691b1e2-00f4-40b6-a585-c512324e8939",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Deleting Keys",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Selected keys can be deleted by pressing the <strong>Delete</strong> key on the keyboard, or by right clicking on the key you want to delete and selecting the action <strong>Delete</strong> from the context menu.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Moving Keys",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "To move a key along the timeline, select the key, then drag it. Multiple keys can be selected using the <strong>Ctrl</strong> key. Dragging horizontally will update the <strong>Time</strong> value of the key, while dragging vertically will update the <strong>Value</strong>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "video",
            "video_id": "V_Dc3sdO",
            "provider": "kaltura",
            "caption": "",
            "autoplay": false,
            "loop": false,
            "width": null,
            "video": {
              "height": 440,
              "width": 740,
              "identifier": "V_Dc3sdO"
            },
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Key Interpolation",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "By right-clicking a key, a context menu menu appears to choose the interpolation type for selected key.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24559853,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24559853,
              "file_name": "08_InterpolationOptions.png",
              "file_size": 37933,
              "content_type": "image/png",
              "created_at": "2025-05-02T19:19:53.885+00:00",
              "height": 440,
              "width": 740,
              "storage_key": "bdb28e40-da38-4b69-89df-9b96edc34298",
              "context": "documentation"
            },
            "storage_key": "bdb28e40-da38-4b69-89df-9b96edc34298",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Key interpolation only affects the curve between the key you interpolate for and the next key after that. For example, with all other keys set to <strong>Linear</strong>, and the center key set to <strong>Auto</strong>, the track will look similar to the image below.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24559854,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24559854,
              "file_name": "09_InterpolationExample.png",
              "file_size": 29524,
              "content_type": "image/png",
              "created_at": "2025-05-02T19:19:53.989+00:00",
              "height": 440,
              "width": 740,
              "storage_key": "8c67a0ce-0696-4a70-8f5b-9a9738058794",
              "context": "documentation"
            },
            "storage_key": "8c67a0ce-0696-4a70-8f5b-9a9738058794",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Available interpolation types are:",
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
                  "content": "<strong>Auto</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559855,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559855,
                    "file_name": "10_AutoInterpolation.png",
                    "file_size": 29631,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:54.088+00:00",
                    "height": 440,
                    "width": 740,
                    "storage_key": "8c424555-d5ef-47a8-9ef3-2b4c8d069b7f",
                    "context": "documentation"
                  },
                  "storage_key": "8c424555-d5ef-47a8-9ef3-2b4c8d069b7f",
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
                  "content": "<strong>User</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559856,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559856,
                    "file_name": "11_UserInterpolation.png",
                    "file_size": 29594,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:54.205+00:00",
                    "height": 440,
                    "width": 740,
                    "storage_key": "abcb1ea1-ef44-4e83-941b-d2d29aef963b",
                    "context": "documentation"
                  },
                  "storage_key": "abcb1ea1-ef44-4e83-941b-d2d29aef963b",
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
                  "content": "<strong>Break</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559857,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559857,
                    "file_name": "12_BreakInterpolation.png",
                    "file_size": 29190,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:54.347+00:00",
                    "height": 440,
                    "width": 740,
                    "storage_key": "a1901223-2bde-486a-bddf-bdc8dc63568b",
                    "context": "documentation"
                  },
                  "storage_key": "a1901223-2bde-486a-bddf-bdc8dc63568b",
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
                  "content": "<strong>Linear</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559858,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559858,
                    "file_name": "13_LinearInterpolation.png",
                    "file_size": 29814,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:54.422+00:00",
                    "height": 440,
                    "width": 740,
                    "storage_key": "095d26e0-c188-4e20-a42a-1e3a510a0744",
                    "context": "documentation"
                  },
                  "storage_key": "095d26e0-c188-4e20-a42a-1e3a510a0744",
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
                  "content": "<strong>Constant</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559859,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559859,
                    "file_name": "14_ConstantInterpolation.png",
                    "file_size": 27673,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:54.535+00:00",
                    "height": 440,
                    "width": 740,
                    "storage_key": "cde7aaaa-3cf5-4a63-bb8d-c06b9e501e44",
                    "context": "documentation"
                  },
                  "storage_key": "cde7aaaa-3cf5-4a63-bb8d-c06b9e501e44",
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
            "content": "External Curves",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "To the left of the main key area is a field where you can add an external curve asset from the <strong>Content Browser</strong> to that track.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24559860,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24559860,
              "file_name": "15_ExternalCurve.png",
              "file_size": 25752,
              "content_type": "image/png",
              "created_at": "2025-05-02T19:19:54.622+00:00",
              "height": 440,
              "width": 740,
              "storage_key": "f1926ed3-e9dd-4885-9996-c30a535016ef",
              "context": "documentation"
            },
            "storage_key": "f1926ed3-e9dd-4885-9996-c30a535016ef",
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
                    "content": "External Curve Icon",
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
                    "type": "image",
                    "image_id": 24559861,
                    "caption": "",
                    "alt_text": "",
                    "image": {
                      "id": 24559861,
                      "file_name": "16_ExtCurveButton1.png",
                      "file_size": 721,
                      "content_type": "image/png",
                      "created_at": "2025-05-02T19:19:54.686+00:00",
                      "height": 24,
                      "width": 24,
                      "storage_key": "a315ab2d-77f8-4622-b4d7-17e10cc657e8",
                      "context": "documentation"
                    },
                    "storage_key": "a315ab2d-77f8-4622-b4d7-17e10cc657e8",
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
                    "content": "Use the curve selected in the <strong>Content Browser</strong> for this track.",
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
                    "image_id": 24559862,
                    "caption": "",
                    "alt_text": "",
                    "image": {
                      "id": 24559862,
                      "file_name": "17_ExtCurveButton2.png",
                      "file_size": 532,
                      "content_type": "image/png",
                      "created_at": "2025-05-02T19:19:54.806+00:00",
                      "height": 24,
                      "width": 24,
                      "storage_key": "656a5898-decd-4d4e-b3a5-68a1f259b2c9",
                      "context": "documentation"
                    },
                    "storage_key": "656a5898-decd-4d4e-b3a5-68a1f259b2c9",
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
                    "content": "Browse in the <strong>Content Browser</strong> to select a curve for this track.",
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
                    "image_id": 24559863,
                    "caption": "",
                    "alt_text": "",
                    "image": {
                      "id": 24559863,
                      "file_name": "18_ExtCurveButton3.png",
                      "file_size": 386,
                      "content_type": "image/png",
                      "created_at": "2025-05-02T19:19:54.863+00:00",
                      "height": 24,
                      "width": 24,
                      "storage_key": "b16cebdc-0058-4308-bdd3-bf9d40dae993",
                      "context": "documentation"
                    },
                    "storage_key": "b16cebdc-0058-4308-bdd3-bf9d40dae993",
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
                    "content": "Convert an imported external curve to an internal curve so that keys and curves can be edited.",
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
          },
          {
            "type": "paragraph",
            "content": "You can also right-click any curve (with at least one key selected) and choose <strong>Create External Curve</strong>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24559864,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24559864,
              "file_name": "19_CreateExtCurve.png",
              "file_size": 30446,
              "content_type": "image/png",
              "created_at": "2025-05-02T19:19:54.945+00:00",
              "height": 440,
              "width": 740,
              "storage_key": "c660bd4b-4b9d-4655-a307-9258e572a790",
              "context": "documentation"
            },
            "storage_key": "c660bd4b-4b9d-4655-a307-9258e572a790",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "This brings up a context window in which you can edit the path for where the curve asset will be saved. In doing this, you can then use this curve again on other timelines.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24559865,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24559865,
              "file_name": "20_CreateExtCerveWindow.png",
              "file_size": 15612,
              "content_type": "image/png",
              "created_at": "2025-05-02T19:19:55.056+00:00",
              "height": 301,
              "width": 456,
              "storage_key": "5916953c-ec57-494e-8866-ca62170a4b61",
              "context": "documentation"
            },
            "storage_key": "5916953c-ec57-494e-8866-ca62170a4b61",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "5A8",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 904,
        "excerpt_assignment_id": 604,
        "blocks": [
          {
            "type": "paragraph",
            "content": "A <strong>Curve</strong> (<strong><a data-document-id=\"3582631\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/Curves/UCurveBase?application_version=5.5\">UCurveBase</a></strong>) defines a track of interpolated points to evaluate over a given range. Curves can be <strong>vectors</strong>, <strong>floats</strong>, and <strong>colors</strong>. Each track can have any number of <strong>keys</strong> that define a time and value. The data can be interpolated between these keys to calculate the value at any point during the Timeline.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Working with Keys and Curves",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this example, you will create a <strong><a data-document-id=\"3582655\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/Curves/UCurveFloat?application_version=5.5\">UCurveFloat</a></strong> that defines a curve of interpolated float points to evaluate over a given range.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "To create and instantiate a <code>UCurveFloat</code> to a <strong>Timeline Component</strong>, follow the steps below:",
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
                  "content": "Navigate to the <strong>Content Browser</strong>, click <strong>C++ Classes</strong> folder, then click <strong>Add (+)</strong> button and select <strong>New C++ Class</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559866,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559866,
                    "file_name": "01_AddCppClass.png",
                    "file_size": 20887,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:55.471+00:00",
                    "height": 270,
                    "width": 400,
                    "storage_key": "44c98a2c-cb88-460a-86f6-10a2b8d6eae4",
                    "context": "documentation"
                  },
                  "storage_key": "44c98a2c-cb88-460a-86f6-10a2b8d6eae4",
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
                  "content": "Select <strong>Actor</strong> as a <strong>Parent Class</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559867,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559867,
                    "file_name": "02_ChooseParentCppClass.png",
                    "file_size": 38045,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:55.572+00:00",
                    "height": 580,
                    "width": 946,
                    "storage_key": "4d2664ad-0824-44ef-a79d-14f01721a659",
                    "context": "documentation"
                  },
                  "storage_key": "4d2664ad-0824-44ef-a79d-14f01721a659",
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
                  "content": "Name created Actor as <strong>ExampleTimelineComponent</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559868,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24559868,
                    "file_name": "03_NameCppActor.png",
                    "file_size": 33625,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:55.682+00:00",
                    "height": 580,
                    "width": 946,
                    "storage_key": "20ebda25-dc05-4e2c-b394-e114ce9af0e7",
                    "context": "documentation"
                  },
                  "storage_key": "20ebda25-dc05-4e2c-b394-e114ce9af0e7",
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
                  "content": "When new Actor is created, <strong>Visual Studio</strong> automatically  opens <code>ExampleTimelineComponent.h</code> and <code>ExampleTimelineComponent.cpp</code> files. Navigate to the <code>ExampleTimelineComponent.h</code> file and add the following to the <code>#include</code> section:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "ExampleTimelineComponent.h",
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
                  "id": 44456,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ1NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjQxOjQ4KzAwOjAwIn0=--f4e8a94d4ae59bd7765e20c880fc9caa2a1231c8734983d331a6fcd2340c7b16",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Next, in the <code>ExampleTimelineComponent</code> class definition, add the following code:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "ExampleTimelineComponent.h",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "protected:\n\n         UPROPERTY(EditAnywhere, BlueprintReadWrite)\n         UTimelineComponent* ExampleTimelineComp;\n\n     public:\n\n         UPROPERTY(EditAnywhere)\n         UCurveFloat* ExampleTimelineCurve;",
                  "lines_of_code": 9,
                  "id": 44457,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDQ1NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjQxOjQ4KzAwOjAwIn0=--83efc2fec0a47de8788663dba0978d84ce5b08655030e96a9beb5a26cefeb881",
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
                  "content": "Navigate to the <strong>Content Browser</strong>, select <strong>Add (+) &gt; Miscellaneous &gt; Curve</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559869,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559869,
                    "file_name": "04_AddCurveAsset.png",
                    "file_size": 60066,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:55.892+00:00",
                    "height": 451,
                    "width": 600,
                    "storage_key": "56ad9c6f-d047-431f-8ca8-b3d1ca5137cb",
                    "context": "documentation"
                  },
                  "storage_key": "56ad9c6f-d047-431f-8ca8-b3d1ca5137cb",
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
                  "content": "Select <strong>CurveFloat</strong> and name it <strong>ExampleFloatTrack</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559870,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559870,
                    "file_name": "05_ParentClassFloatCurve.png",
                    "file_size": 18627,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:56.008+00:00",
                    "height": 294,
                    "width": 600,
                    "storage_key": "7d793b11-63ac-4ab2-9b45-ad3551dd699d",
                    "context": "documentation"
                  },
                  "storage_key": "7d793b11-63ac-4ab2-9b45-ad3551dd699d",
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
                  "content": "In <strong>Content Browser</strong> navigate to the folder with your <strong>ExampleTimelineComponent</strong> class, right click it and select <strong>Create Blueprint Class based on ExampleTimelineComponent</strong>. Name it <strong>BP_ExampleTimelineComponent</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559871,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559871,
                    "file_name": "06_CreateBPBasedOnCpp.png",
                    "file_size": 31235,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:56.298+00:00",
                    "height": 260,
                    "width": 600,
                    "storage_key": "5d7972b5-b8d3-45e4-8e57-f2047139acaf",
                    "context": "documentation"
                  },
                  "storage_key": "5d7972b5-b8d3-45e4-8e57-f2047139acaf",
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
                  "content": "Open the <strong>BP_ExampleTimelineComponent</strong> class defaults, navigate to the <strong>Detail</strong> panel and assign your <strong>Example Timeline Curve</strong> with your <strong>ExampleFloatTrack</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559872,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559872,
                    "file_name": "07_SelectExampleFloatTrack.png",
                    "file_size": 34976,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:56.387+00:00",
                    "height": 440,
                    "width": 600,
                    "storage_key": "9e4b8db9-3b09-420a-b80f-4a3ce433c60a",
                    "context": "documentation"
                  },
                  "storage_key": "9e4b8db9-3b09-420a-b80f-4a3ce433c60a",
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
                  "content": "Double-click your <strong>Example Float Track</strong> from the Content Browser to open the <strong>Timeline Editor</strong>.",
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
            "content": "Adding Keys",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Keys are added by pressing the <strong>Enter</strong> key, or by right clicking on the gray bar and selecting the action <strong>Add Key</strong> from the context menu.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24559873,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24559873,
              "file_name": "08_AddKeytoCurve.png",
              "file_size": 36370,
              "content_type": "image/png",
              "created_at": "2025-05-02T19:19:56.566+00:00",
              "height": 400,
              "width": 760,
              "storage_key": "9970ea3a-9072-4893-a946-f294b6ce116f",
              "context": "documentation"
            },
            "storage_key": "9970ea3a-9072-4893-a946-f294b6ce116f",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Editing Keys",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "The time and value of the key can be set by clicking the key and entering the values into the time and value fields near the top of the track.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24559874,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24559874,
              "file_name": "09_SetFloat.png",
              "file_size": 32579,
              "content_type": "image/png",
              "created_at": "2025-05-02T19:19:56.646+00:00",
              "height": 400,
              "width": 760,
              "storage_key": "6d4e5b9f-5fb3-4467-9874-2d3ab3ee0ad0",
              "context": "documentation"
            },
            "storage_key": "6d4e5b9f-5fb3-4467-9874-2d3ab3ee0ad0",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Deleting Keys",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Selected keys can be deleted by pressing the <strong>Delete</strong> key on the keyboard, or by right clicking on the key you want to delete and selecting the action <strong>Delete</strong> from the context menu.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Moving Keys",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "To move a key along the timeline, select the key, then drag it. Multiple keys can be selected using the <strong>Ctrl</strong> key. Dragging horizontally will update the <strong>Time</strong> value of the key, while dragging vertically will update the <strong>Value</strong>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "video",
            "video_id": "V_SlfX0K",
            "provider": "kaltura",
            "caption": "",
            "autoplay": false,
            "loop": false,
            "width": null,
            "video": {
              "height": 400,
              "width": 760,
              "identifier": "V_SlfX0K"
            },
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Key Interpolation",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "By right-clicking a key, a context menu menu appears to choose the interpolation type for selected key.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24559875,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24559875,
              "file_name": "10_InterpolationOptions.png",
              "file_size": 45017,
              "content_type": "image/png",
              "created_at": "2025-05-02T19:19:56.759+00:00",
              "height": 400,
              "width": 760,
              "storage_key": "0e91265a-7f18-4eea-997a-5c5b36c0f2e7",
              "context": "documentation"
            },
            "storage_key": "0e91265a-7f18-4eea-997a-5c5b36c0f2e7",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Key interpolation only affects the curve between the key you interpolate for and the next key after that. For example, with all other keys set to <strong>Linear</strong>, and the center key set to <strong>Cubic-Auto</strong>, the track will look similar to the image below.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24559876,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24559876,
              "file_name": "11_InterpolationExample.png",
              "file_size": 31161,
              "content_type": "image/png",
              "created_at": "2025-05-02T19:19:56.859+00:00",
              "height": 400,
              "width": 760,
              "storage_key": "01de5f84-dd04-4ef1-bf03-361ed7126715",
              "context": "documentation"
            },
            "storage_key": "01de5f84-dd04-4ef1-bf03-361ed7126715",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Available interpolation types are:",
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
                  "content": "<strong>Auto</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559877,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559877,
                    "file_name": "12_AutoInterpolation.png",
                    "file_size": 31351,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:56.961+00:00",
                    "height": 400,
                    "width": 760,
                    "storage_key": "d39c25e0-9184-42fb-bf7b-9bebf08bc3c9",
                    "context": "documentation"
                  },
                  "storage_key": "d39c25e0-9184-42fb-bf7b-9bebf08bc3c9",
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
                  "content": "<strong>User</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559878,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559878,
                    "file_name": "13_UserInterpolation.png",
                    "file_size": 31935,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:57.030+00:00",
                    "height": 400,
                    "width": 760,
                    "storage_key": "501477e1-8e4b-4202-9cec-c1b01998b6d6",
                    "context": "documentation"
                  },
                  "storage_key": "501477e1-8e4b-4202-9cec-c1b01998b6d6",
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
                  "content": "<strong>Break</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559879,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559879,
                    "file_name": "14_BreakInterpolation.png",
                    "file_size": 31675,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:57.140+00:00",
                    "height": 400,
                    "width": 760,
                    "storage_key": "7aaec65a-025c-439e-8e03-5b1ae1178980",
                    "context": "documentation"
                  },
                  "storage_key": "7aaec65a-025c-439e-8e03-5b1ae1178980",
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
                  "content": "<strong>Linear</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559880,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559880,
                    "file_name": "15_LinearInterpolation.png",
                    "file_size": 30631,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:57.222+00:00",
                    "height": 400,
                    "width": 760,
                    "storage_key": "d3da9870-209f-40ff-9c55-407bf44a4132",
                    "context": "documentation"
                  },
                  "storage_key": "d3da9870-209f-40ff-9c55-407bf44a4132",
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
                  "content": "<strong>Constant</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24559881,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24559881,
                    "file_name": "16_ConstantInterpolation.png",
                    "file_size": 26741,
                    "content_type": "image/png",
                    "created_at": "2025-05-02T19:19:57.331+00:00",
                    "height": 400,
                    "width": 760,
                    "storage_key": "fb089950-8e79-4d69-aabf-f97033f47adf",
                    "context": "documentation"
                  },
                  "storage_key": "fb089950-8e79-4d69-aabf-f97033f47adf",
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
        "excerpt_hash_id": "yyB",
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
