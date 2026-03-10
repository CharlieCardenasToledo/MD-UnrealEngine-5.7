# Landscape Material Expressions

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-material-expressions-in-unreal-engine

> Application Version: 5.7

## LandscapeLayerBlend

```json
{
  "type": "include",
  "excerpt_id": 186,
  "excerpt_assignment_id": 403,
  "blocks": [
    {
      "type": "paragraph",
      "content": "The <strong>Landscape Layer Blend</strong> node blends together multiple per-layer values, such as texture samples or materials. Layers with higher blend weights have more influence on the blended result.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "To add a new layer, click the plus (<b>+</b>) icon.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24487885,
      "caption": "Click image for full size.",
      "alt_text": "Layer Blend Array Elements",
      "image": {
        "id": 24487885,
        "file_name": "02-layer-blend-array-elements.png",
        "file_size": 18764,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:12:02.193+00:00",
        "height": 265,
        "width": 617,
        "storage_key": "7c900f29-ca7f-4df3-b1fd-4150fdac90b8",
        "context": "documentation"
      },
      "storage_key": "7c900f29-ca7f-4df3-b1fd-4150fdac90b8",
      "context": "documentation",
      "width": 450,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "After you’ve added layers to the node, the Layer Names appear in the LandscapeLayerBlend node. The node has the following inputs:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24487886,
      "caption": "Click image for full size.",
      "alt_text": "Landscape Layer Blend Mode",
      "image": {
        "id": 24487886,
        "file_name": "03-landscape-layer-blend-mode.png",
        "file_size": 85357,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:12:02.322+00:00",
        "height": 653,
        "width": 1020,
        "storage_key": "b632b57f-f61b-4cda-a171-e47f8e98a995",
        "context": "documentation"
      },
      "storage_key": "b632b57f-f61b-4cda-a171-e47f8e98a995",
      "context": "documentation",
      "width": 550,
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
              "content": "Number",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "Property",
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
              "content": "<strong>1</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Layers</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Lists layers contained in the array. Add new layers by clicking the plus icon ().",
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
              "content": "<strong>2</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Additional Layers</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Shows any additional collapsed layers.",
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
              "content": "<strong>3</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Layer Name</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Displays the unique name of the layer. The <strong>Layer Name</strong> corresponds to the layer name used in <a data-document-id=\"3224514\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine\">Paint mode</a> in the Landscape tool window.",
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
              "content": "<strong>4</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Blend Type</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Defines the blend mode used by this layer. It contains the following options: <strong>LB Alpha Blend</strong>, <strong>LB Height Blend</strong>, or <strong>LB Weight Blend.</strong> For more information, see <a data-document-id=\"3224657\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine\">Landscape Layer Blend Types</a>.",
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
              "content": "<strong>5</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Preview Weight</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Displays the weight value to use when previewing the blending in the Material Editor.",
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
              "content": "<strong>6</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Const Layer Input</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Defines an RGB value to use when you do not want to use a texture. This is used for debugging a layer.",
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
              "content": "<strong>7</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Const Height Input</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Defines a height value to use when you do not want to use a texture.",
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
      "content": "The <strong>Landscape Layer Blend</strong> node has the following inputs and outputs:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24487887,
      "caption": "Click image for full size.",
      "alt_text": "Layer Blend Node",
      "image": {
        "id": 24487887,
        "file_name": "05-layer-blend-node.png",
        "file_size": 31590,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:12:02.537+00:00",
        "height": 342,
        "width": 367,
        "storage_key": "202f23be-ca5b-466c-964f-20bde280e751",
        "context": "documentation"
      },
      "storage_key": "202f23be-ca5b-466c-964f-20bde280e751",
      "context": "documentation",
      "width": 250,
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
              "content": "Number",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "Item",
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
              "content": "<strong>1</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Layer <em>Layer Name</em></strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Displays the unique name of the layer. This input is only available after you have added and names layers in the <strong>Details</strong> panel.",
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
              "content": "<strong>2</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Height <em>Layer Name</em></strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Defines a height map to blend with the named layer. This input is only visible on layers where the <strong>Blend Type</strong> property is set to <strong>LB Height Blend</strong>.",
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
              "content": "<strong>3</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Output</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the blended result.",
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
      "type": "callout",
      "callout_type": "note",
      "blocks": [
        {
          "type": "paragraph",
          "content": "All layer names must be unique. It is recommended to name your layers with a descriptive name that indicates the layer’s contents.",
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
  "excerpt_hash_id": "Be3",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "include",
  "excerpt_id": 191,
  "excerpt_assignment_id": 404,
  "blocks": [
    {
      "type": "paragraph",
      "content": "When you use the LB Height Blend mode for multiple Landscape layers, you may find black spots on your Landscape where different layers meet. LB Height Blend works by managing the blend factor, or weight, for the layer, using the specified height value. When multiple layers are painted on an area and are set to LB Height Blend, the layers painted in a particular area can simultaneously have a <code class=\"inline-code\">0</code> height value, so the desired blend factor for each layer becomes <code>0</code>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Because there is no specific ordering, black spots can appear because no layers have any contributions in that area. When you blend a Normal map, even more black spots can appear, because this blending results in a Normal value of (<code class=\"inline-code\">0,0,0</code>), which is invalid and causes lighting issues. If this happens, paint the area with a material with a non-zero weight.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "In the left image, all layers are LB Height Blend, causing some areas to be black. On the right, the red \"1\" layer has been changed to use LB Alpha Blend.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24487893,
      "caption": "Click image for full size.",
      "alt_text": "LB Height Blend Problem",
      "image": {
        "id": 24487893,
        "file_name": "06-lb-height-blend-problem.png",
        "file_size": 363188,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:12:03.922+00:00",
        "height": 238,
        "width": 800,
        "storage_key": "e4f2b94a-1c22-49f2-971a-b398833bb166",
        "context": "documentation"
      },
      "storage_key": "e4f2b94a-1c22-49f2-971a-b398833bb166",
      "context": "documentation",
      "width": 600,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Below is an example of the properties of the <strong>Landscape Layer Blend</strong> node for all the layers being blended together. The <strong>Soil</strong> layer has its blend mode set to LB Alpha Blend, while the other layers have theirs set to LB Height Blend. This is to stop the issue mentioned above from happening.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24487894,
      "caption": "Click image for full size.",
      "alt_text": "Layer Blend Properties",
      "image": {
        "id": 24487894,
        "file_name": "07-layer-blend-properties.png",
        "file_size": 78463,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:12:04.176+00:00",
        "height": 1092,
        "width": 682,
        "storage_key": "ec4d7ab9-a269-431e-b705-45ad4a6b28df",
        "context": "documentation"
      },
      "storage_key": "ec4d7ab9-a269-431e-b705-45ad4a6b28df",
      "context": "documentation",
      "width": 450,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "To delete a layer, click the dropdown arrow to the right of the layer's element number, and select <strong>Delete</strong>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24487895,
      "caption": "Click image for full size.",
      "alt_text": "Delete Layer",
      "image": {
        "id": 24487895,
        "file_name": "08-delete-layer.png",
        "file_size": 22197,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:12:04.371+00:00",
        "height": 277,
        "width": 657,
        "storage_key": "f638880b-3dc4-44c7-b2fa-b462629fe914",
        "context": "documentation"
      },
      "storage_key": "f638880b-3dc4-44c7-b2fa-b462629fe914",
      "context": "documentation",
      "width": 450,
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "5aV",
  "settings": {
    "is_hidden": false
  }
}
```

## LandscapeLayerCoords

```json
{
  "type": "include",
  "excerpt_id": 187,
  "excerpt_assignment_id": 405,
  "blocks": [
    {
      "type": "paragraph",
      "content": "The <strong>Landscape Layer Coords</strong> node generates UV coordinates used for mapping the Landscape material onto Landscapes.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24487888,
      "caption": "Click image for full size.",
      "alt_text": "Landscape Layer Coords Node",
      "image": {
        "id": 24487888,
        "file_name": "09-landscape-layer-coords-node.png",
        "file_size": 66129,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:12:02.947+00:00",
        "height": 510,
        "width": 1047,
        "storage_key": "a237623c-ffdf-4378-ba52-66d9474893fa",
        "context": "documentation"
      },
      "storage_key": "a237623c-ffdf-4378-ba52-66d9474893fa",
      "context": "documentation",
      "width": 550,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "This node has the following options:",
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
              "content": "Number",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "Property",
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
              "content": "1",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Mapping Type</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the orientation to use when mapping the material or network to the Landscape. It contains the following options:",
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
                    "content": "<strong>TCMT Auto</strong>: Uses landscape vertex coordinates, in the range [0, OverallLandscapeResolution]",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<strong>TCMT XY</strong>: Uses object space XY mapping. This is equivalent to TCMT Auto.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<strong>TCMT XZ</strong>: Uses object space XZ mapping. Recommended for side-projected textures.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<strong>TCMT YZ</strong>: Uses object space YZ mapping. Recommended for side-projected textures.",
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
              "content": "2",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Custom UVType</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the UV coordinates to map the material to the Landscape based on the type. It contains the following options:",
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
                    "content": "<strong>LCCT None</strong>: Do not use custom UVs.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<strong>LCCT Custom UV0</strong>: Use custom UVs in channel 0.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<strong>LCCT Custom UV1</strong>: Use custom UVs in channel 1.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<strong>LCCT Custom UV2</strong>: Use custom UVs in channel 2.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<strong>LCCT Weight Map UV</strong>: Use original Weightmap UVs.",
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
              "content": "3",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Mapping Scale</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Applies uniform scaling to the UV coordinates.",
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
              "content": "4",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Mapping Rotation</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Applies the rotation, in degrees, to the UV coordinates.",
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
              "content": "5",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Mapping Pan [U]</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Applies the offset in the [U] direction to the UV coordinates.",
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
              "content": "6",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Mapping Pan [V]</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Applies the offset in the [V] direction to the UV coordinates.",
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
              "content": "7",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Unlabeled Output</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the UV coordinates to map the material to the Landscape based on the given property values.",
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
  "excerpt_hash_id": "ve0",
  "settings": {
    "is_hidden": false
  }
}
```

## LandscapeLayerSwitch

```json
{
  "type": "include",
  "excerpt_id": 188,
  "excerpt_assignment_id": 406,
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can use the <strong>Landscape Layer Switch</strong> node to exclude some material operations when a specific layer is not contributing to a region of the Landscape. You can use this to optimize your material by removing calculations that are not necessary when a layer's weight is zero.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24487889,
      "caption": "Click image for full size.",
      "alt_text": "Landscape Layer Switch Node",
      "image": {
        "id": 24487889,
        "file_name": "10-landscape-layer-switch-node.png",
        "file_size": 64032,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:12:03.207+00:00",
        "height": 372,
        "width": 1152,
        "storage_key": "d0d94b25-1733-4738-a0b8-3bbf5be80f7d",
        "context": "documentation"
      },
      "storage_key": "d0d94b25-1733-4738-a0b8-3bbf5be80f7d",
      "context": "documentation",
      "width": 550,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "This node has the following options:",
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
              "content": "Number",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "Property",
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
              "content": "1",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Parameter Name</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Displays the unique name of the parameter.",
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
              "content": "2",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Preview Used</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "If checked, uses a preview.",
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
              "content": "3",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Layer Used</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Indicates the material network to use if the specific layer is in use by the current region of the Landscape.",
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
              "content": "4",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Layer Not Used</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Indicates the material network to use if the specific layer is not used by the current region of the Landscape.",
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
              "content": "5",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Output</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Either the <strong>Layer Used</strong> or <strong>Layer Not Used</strong> inputs, depending on whether the layer contributes to the particular region of the Landscape.",
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
  "excerpt_hash_id": "e8R",
  "settings": {
    "is_hidden": false
  }
}
```

## LandscapeLayerWeight

```json
{
  "type": "include",
  "excerpt_id": 189,
  "excerpt_assignment_id": 407,
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can use the <strong>Landscape Layer Weight</strong> node to access layer weights and implement your own custom blending solution in the material graph. The output returns (Base + Layer * LayerWeight). By chaining multiple Landscape Layer Weight nodes together, you can produce a weighted sum that blends between the specified layers.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "You can directly access the <code class=\"inline-code\">LayerWeight</code> value without modification by setting the <b>Base</b> value to <code class=\"inline-code\">0</code> and the <b>Layer</b> value to <code>1.0</code>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24487890,
      "caption": "Click image for full size.",
      "alt_text": "Landscape Layer Weight Node",
      "image": {
        "id": 24487890,
        "file_name": "11-landscape-layer-weight-node.png",
        "file_size": 52605,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:12:03.350+00:00",
        "height": 378,
        "width": 994,
        "storage_key": "1cfa415f-6781-4e97-9155-476772833f95",
        "context": "documentation"
      },
      "storage_key": "1cfa415f-6781-4e97-9155-476772833f95",
      "context": "documentation",
      "width": 550,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "This node has the following options:",
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
              "content": "Number",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "Property",
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
              "content": "1",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Parameter Name</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Displays the name of the layer whose weight you want to read.",
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
              "content": "2",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Preview Weight</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Defines the weight to use for preview purposes in the Material Editor.",
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
              "content": "3",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Const Base</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Defines a specific RGB constant value to use when Base is not connected.",
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
              "content": "4",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Base</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The node network to blend with this layer. This includes the value of the previous layers and any other underlying data. This gives the layer value multiplied by the painted layer weight.",
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
              "content": "5",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Layer</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The value for the specified layer.  This input value is multiplied by the layer weight and accumulated onto Base to produce the Output value.",
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
              "content": "6",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Output</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the result of the blending between the Base and Layer inputs, based on the layer weights of the inputs.",
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
  "excerpt_hash_id": "bB6",
  "settings": {
    "is_hidden": false
  }
}
```

## LandscapeVisibilityMask

```json
{
  "type": "include",
  "excerpt_id": 190,
  "excerpt_assignment_id": 408,
  "blocks": [
    {
      "type": "paragraph",
      "content": "The <strong>Landscape Visibility Mask</strong> node outputs the visibility value of the landscape.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24487891,
      "caption": "Click image for full size.",
      "alt_text": "Landscape Visibility Mask Node",
      "image": {
        "id": 24487891,
        "file_name": "12-landscape-visibility-mask-node.png",
        "file_size": 36208,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:12:03.479+00:00",
        "height": 220,
        "width": 1125,
        "storage_key": "1ee8b585-5c84-4421-a0cc-dbc07f86f965",
        "context": "documentation"
      },
      "storage_key": "1ee8b585-5c84-4421-a0cc-dbc07f86f965",
      "context": "documentation",
      "width": 550,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "This node has the following options:",
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
              "content": "Number",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "Property",
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
              "content": "1",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Output</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the visibility mask value. The value is <code>0.0</code> where the landscape is transparent and <code>1.0</code> where the landscape is visible.",
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
      "type": "image",
      "image_id": 24487892,
      "caption": "Click image for full size.",
      "alt_text": "Layer Visibility Mask Opacity Mask",
      "image": {
        "id": 24487892,
        "file_name": "13-layer-visibility-mask-opacity-mask.png",
        "file_size": 141735,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:12:03.597+00:00",
        "height": 692,
        "width": 1335,
        "storage_key": "05e8047d-fadc-4290-9a01-56d2c20dcf2f",
        "context": "documentation"
      },
      "storage_key": "05e8047d-fadc-4290-9a01-56d2c20dcf2f",
      "context": "documentation",
      "width": 800,
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "zJZ",
  "settings": {
    "is_hidden": false
  }
}
```
