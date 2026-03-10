# Set Spectator Screen Mode Texture Plus Eye Layout

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/set-spectator-screen-mode-texture-plus-eye-layout-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "include",
  "excerpt_id": 752,
  "excerpt_assignment_id": 1346,
  "blocks": [
    {
      "type": "image",
      "image_id": 24544521,
      "caption": "",
      "alt_text": "",
      "image": {
        "id": 24544521,
        "file_name": "SetSpectatorScreenModeTexturePlusEyeLayoutNode.png",
        "file_size": 32383,
        "content_type": "image/png",
        "created_at": "2025-04-29T13:57:19.208+00:00",
        "height": 354,
        "width": 408,
        "storage_key": "f9613dbd-e740-454a-8207-16568e8247ce",
        "context": "documentation"
      },
      "storage_key": "f9613dbd-e740-454a-8207-16568e8247ce",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "This node sets up the layout for the <code>TexturePlusEye</code> function in <code>ESpectatorScreenMode</code>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "<strong>Inputs</strong>",
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
              "content": "Pin Location",
              "settings": {
                "is_hidden": false
              }
            }
          ],
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
              "type": "image",
              "image_id": 24544522,
              "caption": "",
              "alt_text": "",
              "image": {
                "id": 24544522,
                "file_name": "SetSpectatorScreenModeTexturePlusEyeLayoutNode_1.png",
                "file_size": 34139,
                "content_type": "image/png",
                "created_at": "2025-04-29T13:57:19.338+00:00",
                "height": 354,
                "width": 408,
                "storage_key": "6c7c9c85-5fef-474b-b29a-c2c71b872732",
                "context": "documentation"
              },
              "storage_key": "6c7c9c85-5fef-474b-b29a-c2c71b872732",
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
              "content": "(In) Exec",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Input execution pin.",
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
              "image_id": 24544523,
              "caption": "",
              "alt_text": "",
              "image": {
                "id": 24544523,
                "file_name": "SetSpectatorScreenModeTexturePlusEyeLayoutNode_2.png",
                "file_size": 34296,
                "content_type": "image/png",
                "created_at": "2025-04-29T13:57:19.525+00:00",
                "height": 354,
                "width": 408,
                "storage_key": "0dd93ce8-66e0-4f40-a79a-d359bf4ebcba",
                "context": "documentation"
              },
              "storage_key": "0dd93ce8-66e0-4f40-a79a-d359bf4ebcba",
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
              "content": "Eye Rect Min",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "A Vector 2D Structure, setting the minimum position of the screen rectangle that the Eye will be drawn in.",
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
                  "content": "Values are normalized between <code>0.0</code> and <code>1.0</code>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
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
              "type": "image",
              "image_id": 24544525,
              "caption": "",
              "alt_text": "",
              "image": {
                "id": 24544525,
                "file_name": "SetSpectatorScreenModeTexturePlusEyeLayoutNode_3.png",
                "file_size": 34280,
                "content_type": "image/png",
                "created_at": "2025-04-29T13:57:19.619+00:00",
                "height": 354,
                "width": 408,
                "storage_key": "bf69c778-1c19-4d85-81ac-87834b805f19",
                "context": "documentation"
              },
              "storage_key": "bf69c778-1c19-4d85-81ac-87834b805f19",
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
              "content": "Eye Rect Max",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "A Vector 2D Structure, setting the maximum position of the screen rectangle that the Eye will be drawn in.",
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
                  "content": "Values are normalized between <code>0.0</code> and <code>1.0</code>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
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
              "type": "image",
              "image_id": 24544527,
              "caption": "",
              "alt_text": "",
              "image": {
                "id": 24544527,
                "file_name": "SetSpectatorScreenModeTexturePlusEyeLayoutNode_4.png",
                "file_size": 34300,
                "content_type": "image/png",
                "created_at": "2025-04-29T13:57:19.713+00:00",
                "height": 354,
                "width": 408,
                "storage_key": "78c96e64-d93c-4cfc-b9ce-65b55621fa5e",
                "context": "documentation"
              },
              "storage_key": "78c96e64-d93c-4cfc-b9ce-65b55621fa5e",
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
              "content": "Texture Rect Min",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "A Vector 2D Structure, setting the minimum position of the screen rectangle that the Texture will be drawn in.",
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
                  "content": "Values are normalized between <code>0.0</code> and <code>1.0</code>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
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
              "type": "image",
              "image_id": 24544528,
              "caption": "",
              "alt_text": "",
              "image": {
                "id": 24544528,
                "file_name": "SetSpectatorScreenModeTexturePlusEyeLayoutNode_5.png",
                "file_size": 34255,
                "content_type": "image/png",
                "created_at": "2025-04-29T13:57:19.841+00:00",
                "height": 354,
                "width": 408,
                "storage_key": "602036bd-8d99-4c92-aa82-a06aa99d7174",
                "context": "documentation"
              },
              "storage_key": "602036bd-8d99-4c92-aa82-a06aa99d7174",
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
              "content": "Texture Rect Max",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "A Vector 2D Structure, setting the maximum position of the screen rectangle that the Texture will be drawn in.",
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
                  "content": "Values are normalized between <code>0.0</code> and <code>1.0</code>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
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
              "type": "image",
              "image_id": 24544529,
              "caption": "",
              "alt_text": "",
              "image": {
                "id": 24544529,
                "file_name": "SetSpectatorScreenModeTexturePlusEyeLayoutNode_6.png",
                "file_size": 34063,
                "content_type": "image/png",
                "created_at": "2025-04-29T13:57:19.906+00:00",
                "height": 354,
                "width": 408,
                "storage_key": "43566e83-18a0-43e5-81ab-28d06d9ccf01",
                "context": "documentation"
              },
              "storage_key": "43566e83-18a0-43e5-81ab-28d06d9ccf01",
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
              "content": "Draw Eye First",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "If this flag is set to <code>True</code>, the Eye is drawn before the Texture; however, if this flag is set to false, the Texture will be drawn before the Eye.",
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
              "image_id": 24544530,
              "caption": "",
              "alt_text": "",
              "image": {
                "id": 24544530,
                "file_name": "SetSpectatorScreenModeTexturePlusEyeLayoutNode_7.png",
                "file_size": 34103,
                "content_type": "image/png",
                "created_at": "2025-04-29T13:57:20.035+00:00",
                "height": 354,
                "width": 408,
                "storage_key": "8058fd85-bcce-433e-ae42-1b6a34c17452",
                "context": "documentation"
              },
              "storage_key": "8058fd85-bcce-433e-ae42-1b6a34c17452",
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
              "content": "Clear Black",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "If this flag is set to <code>True</code>, the Render Target will be drawn black before either rectangle is drawn.",
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
      "content": "<strong>Output</strong>",
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
              "content": "Pin Location",
              "settings": {
                "is_hidden": false
              }
            }
          ],
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
              "type": "image",
              "image_id": 24544531,
              "caption": "",
              "alt_text": "",
              "image": {
                "id": 24544531,
                "file_name": "SetSpectatorScreenModeTexturePlusEyeLayoutNode_8.png",
                "file_size": 34140,
                "content_type": "image/png",
                "created_at": "2025-04-29T13:57:20.130+00:00",
                "height": 354,
                "width": 408,
                "storage_key": "8e6f0e6d-c4fc-4c22-8fbb-330546d54a80",
                "context": "documentation"
              },
              "storage_key": "8e6f0e6d-c4fc-4c22-8fbb-330546d54a80",
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
              "content": "(Out) Exec",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Output execution pin.",
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
  "excerpt_hash_id": "Qm2",
  "settings": {
    "is_hidden": false
  }
}
```
