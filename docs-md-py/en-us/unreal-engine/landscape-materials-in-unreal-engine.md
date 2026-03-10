# Landscape Materials

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine

> Application Version: 5.7

Unreal Engine (UE) provides several landscape-specific [Material](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-materials) Blueprint nodes that can help improve the textures for your Landscape. You can use the nodes alongside any other material in UE.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can create and modify <b>Landscape Materials</b> in the <a data-document-id=\"3226323\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-editor-user-guide\">Material Editor</a> in the same way as other materials.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

## Layer Weights and Ordering

Landscape materials operate as a blend between multiple layers, where painted blend weights control the influence of each layer.

Each layer is identified by a (case-insensitive) name that gets used in one of the landscape-specific material nodes (e.g. **Landscape Layer Sample**, **Landscape Layer Blend**, etc.). The nodes allow the material to access a specific weightmap of a specific target layer.

To be paintable, the layer needs to be created and associated with a **Landscape Layer Info** asset. For more information, see [Target Layers](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-and-using-custom-heightmaps-and-layers-in-unreal-engine). It is okay to create a target layer in the landscape and not use it in the landscape material. However, if a material looks for a layer name that has no target layer entry in the landscape, its weight will always be considered zero.

In the Blueprints editor, the material graph determines how the weights are interpreted to achieve the blended result. The blending method defines how the landscape uses those weights in the final result.

There are two possible blending modes: **W****eight Blending** and **Alpha Blending**. You can use these methods together to create different effects, such as snow on top of your grass and dirt layers.

| Blending Mode | Description |
| --- | --- |
| **Weight Blending** | Assigns a value between `0` and `1.0` to each layer of the material, which corresponds to a percentage value. Landscape Paint tools ensure that the weight value of all weight blended layers does not exceed `1.0`. The excess value is removed and the other layers scale down appropriately, so that a total of 100% remains. |
| **Alpha Blending** | Assigns each layer an alpha percentage value between 0 and 100%. If your material graph is set up for ordered blending, this method respects the order in which the layers are applied. The alpha layer exists separately from the other weighted layers, so when the alpha layer weight increases, other existing layer weights decrease. |

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The landscape material is responsible for interpreting weight values from the target layers in the landscape actor, then turning them into shading properties. However, the landscape system also comes with an edit-time layer weight blending system that can transform the weight values before they reach the material. For more information on weighted blending, see <a data-document-id=\"3224514\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine\">Landscape Paint Mode</a>.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

## Landscape-Specific Material Nodes

Inside the [Material Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-editor-user-guide), there are several specific nodes that you can use with the Landscape system. You can find these nodes by right-clicking and searching the context sensitive menu, or by searching in the **Palette** menu.

![Material Editor Context Menu](https://dev.epicgames.com/community/api/documentation/image/7dbda72d-a3ce-4d5b-a0a8-590457c93db4)

_Click image for full size._

### Landscape Layer Blend Node

```json
{
  "type": "include",
  "excerpt_id": 186,
  "excerpt_assignment_id": 2594,
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

#### Landscape Layer Blend Types

The **Landscape Layer Blend** node has three types of blend modes. Each different **Layer Blend** mode is used to achieve a different result.

| Blend Mode | Function |
| --- | --- |
| **LB Weight Blend** | Implements a weighted blend between all LB Weight Blend layers. This type is not order dependent. |
| **LB Alpha Blend** | Implements an alpha-blended overlay on top of the LB Weight Blend and LB Height Blend layers. Each LB Alpha Blend layer is applied in the order they appear in the list. For example, painting snow over rock and grass occludes both, but erasing snow reveals the rock and grass beneath it. |
| **LB Height Blend** | This is the same as LB Weight Blend, but also adds detail to the transition between layers based on a height map. For example, you can have dirt appear in the gaps between rocks at the layer transition point, instead of just smoothly blending between rock and dirt. ![LB-blend-image](https://dev.epicgames.com/community/api/documentation/image/d0f4dad7-a488-4971-814e-ec4221de118a) The dirt appears in the gaps between rocks at the layer transition point, creating a smooth transition where the layers meet. |

#### Adding a Landscape Layer Node

The `LandscapeLayerBlend` node automatically blends multiple layers together using either alpha blending or alpha blending with a height-based offset. The height-based offset lets a layer blend with other layers based on a heightmap input.

1. In the **Material Editor**, add a `LandscapeLayerBlend` node.
2. In the **Details** panel, next to **Layers**, click the plus icon (**+**) to add a layer. ![Landscape-layer-blend-add-new-layer](https://dev.epicgames.com/community/api/documentation/image/0e0a2020-8e8e-41a2-81ad-ea2790cd1244)
3. Expand the layer to view its properties.
4. Change the **Layer Name** to a descriptive name for the layer, for example, **Snow**.
5. Determine whether you want the layer to be alpha blended or height blended, and set the **Blend Type** accordingly. ![Landscape-layer-blend-change-name](https://dev.epicgames.com/community/api/documentation/image/7b8f5e9a-adef-49a8-91a0-5a60cbfb96e7)
6. **Add** as many additional layers as you want for your Landscape Material. Rename them, and set their Blend Types appropriately.
7. **Connect** the `LandscapeLayerBlend` node's output to the **Base Color** input of your material's base node.
8. Add **Texture Sample** nodes, and connect their main outputs to the **Layer** inputs of the `LandscapeLayerBlend` nodes. Alternatively, you can create a more complex material network and connect it to the **Landscape Layer Blend Layer** input. For any height-blended layers, connect the **Texture Sample**'s alpha output to the `LandscapeLayerBlend`'s **Height** input.

When you are done, your Landscape material network should look something like this:

![Landscape-layer-blend-in-Blueprints](https://dev.epicgames.com/community/api/documentation/image/36bb8349-d0cd-4401-8d2c-853619cbb704)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can preview the effects of different weights on the material by changing the <b>Preview Weight</b> properties of the <code class=\"inline-code\">LandscapeLayerBlend</code> nodes.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

For more information on the Landscape Layer Blend node, see [Landscape Layer Blend Technical Information](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine#landscape-layer-blend-technical-information).

### Landscape Layer Sample Node

The **Landscape Layer Sampl****e** node returns the weight value associated with a given target layer. Its result is a value between `0.0` (when the target layer is not used) and `1.0` (when the target layer is fully painted), that you can then use at will in its material computations.

![Landscape-layer-sample-node-menu](https://dev.epicgames.com/community/api/documentation/image/d45c91d1-cfe9-4325-9e2f-c04f74908c97)

| **Parameter Name** | Defines the name of the target layer to sample from. |
| --- | --- |
| **Preview Weight** | Defines the weight to use for preview purposes in the Material Editor. |

### Landscape Layer Coords Node

```json
{
  "type": "include",
  "excerpt_id": 187,
  "excerpt_assignment_id": 2595,
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

### Landscape Layer Switch Node

```json
{
  "type": "include",
  "excerpt_id": 188,
  "excerpt_assignment_id": 2596,
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

### Landscape Layer Weight Node

```json
{
  "type": "include",
  "excerpt_id": 189,
  "excerpt_assignment_id": 2597,
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

#### Adding a Landscape Layer Weight Node

1. In the **Material Editor**, add a `LandscapeLayerWeight` node. ![Landscape-layer-weight-node-in-Blueprints](https://dev.epicgames.com/community/api/documentation/image/2b204b6a-00c3-45ec-9ed8-7c231ac81ba0)
2. In the **Details** panel, change the **Parameter Name** to a descriptive name for the layer, for example, **Rock**. ![Landscape-layer-weight-menu-options](https://dev.epicgames.com/community/api/documentation/image/28232a67-7324-4cde-aa72-e97e7da8c412)
3. **Add** additional Landscape Layer Weight nodes, until you have one for each layer that you want your material to have. This example uses two `LandscapeLayerWeight` nodes.
4. Add and connect your **Texture Samples** or material network expressions to your **Landscape Layer Weight** nodes.
5. **Add** a `LandscapeLayerCoords` node and **set the UV** titling. Connect it to the **Texture Sample** nodes.
6. **Connect** each Layer node's output pin to the Base pin of the next layer node, while leaving the first layer node's Base pin unconnected.
7. Connect the last Layer node's output pin to the **Base Color** input of the `NewMaterial` node.

You should have something similar to the example below:

![Landscape-layer-weight-in-Blueprints](https://dev.epicgames.com/community/api/documentation/image/4a8439c5-e210-4a4d-8a35-bf24ca94d228)

### Landscape Visibility Mask Node

The **Landscape Visibility Mask** node outputs the visibility value of the landscape. The output is the visibility mask value. The value is `0.0` where the landscape is transparent and `1.0` where the landscape is visible.

![Landscape-visibility-mask-node](https://dev.epicgames.com/community/api/documentation/image/3861a4e4-8c25-4819-b217-2ac6edc6dde7)

On a standard landscape, landscape visibility requires the material to use a **Masked Opacity Blend Mode**, as the landscape shader needs to sample the visibility weightmap to discard pixels that are not visible enough. In order to do this, you have to connect the **Landscape Visibility Mask** material node to the **Opacity Mask**. This is more costly performance-wise, and should be avoided as much as possible on the global landscape material.

The landscape system is able to automatically detect the regions (landscape components) where visibility information is present. It can then override the material instance’s blend mode, only in those regions, in order to limit where a masked material is actually used. You need to leave the landscape material’s **Blend Mode** to **Opaque**, but connect the **Opacity Mask** (even if it appears greyed out), like this:

![Visibility-mask-in-blueprints-editor](https://dev.epicgames.com/community/api/documentation/image/4aa86c18-0817-450f-9613-3f9fc0cc434b)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "When generating a <a data-document-id=\"3224714\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/using-nanite-with-landscapes-in-unreal-engine\">Nanite landscapes</a> mesh, there’s no cost in the landscape material, as the Nanite renderer can keep on using the hardware rasterizer (the fast path), as it does with any other opaque materials. ",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

## Landscape Layer Blend Technical Information

Landscape layer nodes behave similar to a [Static Switch Parameter](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine#static-switch-parameter) node. This switches between using one branch of the material and another. Each component of the Landscape has its own **Material Instance Constant** created from the main Landscape material, which is applied to only that component.

If a Landscape component does not use a specific layer, the subtree of nodes connected to the layer is discarded. This reduces the complexity, letting the material applied to the Landscape contain any number of texture samples, as long as it is within the limits set by the shader model.

Using this method, you can create a main Landscape material that contains every texture or material you need, while keeping the final result within the parameters allowed by the hardware.

Please note that currently most RHIs support shared texture samplers, which means that there’s no hard constraint about how many layers can be used on a given landscape component. The exception being ES3.1 (mobile), which still has a hard limit in terms of sampler count (16), across all texture accesses in the material. Hence, if the game is planned to ship on such a platform, it’s important to make sure that the number of landscape layers remains low, since a new weightmap texture will be added every 4 target layers (1 target layer per channel of an RGB8 texture). This means another texture sampler will be added (on top of all the textures that might get sampled by the target layer’s shader code path).  For more information, see [Mobile Landscape Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine#mobile-landscape-materials).

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Any network of material expressions can be connected to the <strong>Layer</strong> inputs in place of a simple <strong>Texture Sample</strong>. This makes it possible to do more complex effects such as transitioning from detail textures to larger macro textures depending on the distance the layer is being viewed from.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

### Landscape Layer Blend Issues

```json
{
  "type": "include",
  "excerpt_id": 191,
  "excerpt_assignment_id": 2599,
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

## Mobile Landscape Materials

You can use any number of Landscape layers, as long as you have enough **Texture Sampler** nodes. The Landscape layer allocation uses the [Feature Level Switch material node](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine), letting a single PC or console Landscape material also have a mobile version. The following image shows how the Landscape in *Fortnite* Battle Royale looks when used for mobile devices.

![Mobile Landscape Feature Level](https://dev.epicgames.com/community/api/documentation/image/a2985158-b778-4d20-9c85-4341cf92ccd3)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "While you can use any number of nodes, we recommend that you only use three.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

## Assigning Materials to Landscapes

After creating a Landscape material, assign the material to a Landscape actor in your level.

1. In the **Content Browser**, locate the Landscape material that you want to use.
2. Either in the viewport or using the **World Outliner**, select the Landscape.
3. In the **Details** panel for the Landscape, locate the **Landscape Material** option, and click the dropdown to select a material. ![Assigned Material](https://dev.epicgames.com/community/api/documentation/image/9e3c0b65-fdbe-455b-ad47-2439cc2653d2)
