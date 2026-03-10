# Material Parameter Expressions

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine

> Application Version: 5.7

## Collection Parameters

A **Collection Parameter Expression** is used to reference a **Material Parameter Collection** asset. These are groups of parameters that you can easily reuse in many different assets such as Materials, Blueprints, and more.

They enable you to modify a global value once in the Parameter Collection, and have it propagate to multiple Materials that reference the collection. For more information, read the [Material Parameter Collections](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-material-parameter-collections-in-unreal-engine) documentation.

![Material Parameter Collection Example](https://dev.epicgames.com/community/api/documentation/image/15f0e436-3420-4b57-affa-6653f60cc01d)

_Click to enlarge image._

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "A Material can reference, at most, two different MaterialParameterCollections. One is typically used for game-wide values\nwhile the other can be used for level specific parameters. A collection can have up to 1024 scalar parameters and 1024 vector\nparameters.",
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

## DynamicParameter

```json
{
  "type": "include",
  "excerpt_id": 349,
  "excerpt_assignment_id": 346,
  "blocks": [
    {
      "type": "paragraph",
      "content": "The <strong>DynamicParameter</strong> expression provides a conduit for particle emitters to pass up to four values to the Material to be used in any manner. These values are set in <strong>Niagara</strong> by means of a <strong>ParameterDynamic</strong> module placed on an emitter.",
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
              "content": "<strong>Param Names</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "An array of the names of the parameters. The values here will determine the text displayed on the outputs of the expression in the Material Editor and will be the names used to reference the parameters in the ParameterDynamic module in Niagara.",
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
              "content": "<strong>Default Value</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the initial values that the parameter outputs (Vector4).",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Outputs",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": " ",
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
              "content": "<strong>Param1</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the value of the first parameter in the Param names property. The name of this output can change based on the values in the Param Names property.",
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
              "content": "<strong>Param2</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the value of the second parameter in the Param names property. The name of this output can change based on the values in the Param Names property.",
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
              "content": "<strong>Param3</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the value of the third parameter in the Param names property. The name of this output can change based on the values in the Param Names property.",
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
              "content": "<strong>Param4</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the value of the fourth parameter in the Param names property. The name of this output can change based on the values in the Param Names property.",
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
  "excerpt_hash_id": "qMq",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "include",
  "excerpt_id": 350,
  "excerpt_assignment_id": 347,
  "blocks": [
    {
      "type": "header",
      "content": "FontSampleParameter",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <strong>FontSampleParameter</strong> expression provides a way to expose a font-based parameter in a Material Instance Constant, making it easy to use different fonts in different instances. The alpha channel of the font will contain the font outline value.  Only valid font pages can be specified.",
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
              "type": "enhanced_table_header",
              "content": "Properties",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": " ",
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
              "content": "<strong>Parameter Name</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the name used to identify the parameter in instances of the Material and through code.",
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
              "content": "<strong>Group</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Provides a way to organize parameter names into groups, or categories, within a MaterialInstanceConstant. All parameters within a Material that have the same Group property name will be listed underneath that category in the Instance Editor.",
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
              "content": "<strong>Font</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Holds the default font asset (from the <strong>Content Browser</strong>) to be held within the expression.",
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
              "content": "<strong>Font Texture Page</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The current font texture page to be used as a part of the texture.",
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
      "image_id": 24499635,
      "caption": "",
      "alt_text": "Font Sample Parameter",
      "image": {
        "id": 24499635,
        "file_name": "font-parameter-expression.png",
        "file_size": 248199,
        "content_type": "image/png",
        "created_at": "2025-04-11T17:40:00.406+00:00",
        "height": 440,
        "width": 924,
        "storage_key": "8a1d3e40-934c-4314-80a2-162e02137a57",
        "context": "documentation"
      },
      "storage_key": "8a1d3e40-934c-4314-80a2-162e02137a57",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "R91",
  "settings": {
    "is_hidden": false
  }
}
```

## ScalarParameter

The **ScalarParameter** expression outputs a single float value ([constant](https://dev.epicgames.com/documentation/en-us/unreal-engine/constant-material-expressions-in-unreal-engine)) that you can access and change in a Material Instance or on the fly by Blueprint or code.

| Property | Description |
| --- | --- |
| **Parameter Name** | Specifies the name used to identify the parameter in instances of the Material and through code. |
| **Group** | Provides a way to organize parameter names into groups, or categories, within a MaterialInstanceConstant. All parameters within a Material that have the same Group property name will be listed underneath that category in the Instance Editor. |
| **Default Value** | Specifies the initial value that the constant takes on. |

You can update the value in a Scalar Parameter, and immediately see the results without recompiling the Material.

```json
{
  "type": "sequence_slider",
  "caption": "Scalar parameter updated from 0 to 10.",
  "images": [
    {
      "image_id": 24499641,
      "storage_key": "06f78c5a-5195-4a46-a67e-c0eed04818c5",
      "context": "documentation",
      "image": {
        "id": 24499641,
        "file_name": "scalar-example-01.png",
        "file_size": 210848,
        "content_type": "image/png",
        "created_at": "2025-04-11T17:40:03.601+00:00",
        "height": 394,
        "width": 951,
        "storage_key": "06f78c5a-5195-4a46-a67e-c0eed04818c5",
        "context": "documentation"
      }
    },
    {
      "image_id": 24499642,
      "storage_key": "6030426c-ec06-46cd-a550-21d47294120e",
      "context": "documentation",
      "image": {
        "id": 24499642,
        "file_name": "scalar-example-02.png",
        "file_size": 185106,
        "content_type": "image/png",
        "created_at": "2025-04-11T17:40:03.798+00:00",
        "height": 394,
        "width": 951,
        "storage_key": "6030426c-ec06-46cd-a550-21d47294120e",
        "context": "documentation"
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

## StaticSwitchParameter

The **StaticSwitchParameter** expression takes in two inputs, and outputs the first if the value of the parameter is *true*, and the second otherwise.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "This parameter is named static because it cannot change at runtime; it can only be set in the Material Instance Editor. Static Switches are applied at compile time, not at runtime. This means that whatever branch of the Material was dropped is never executed, so static switches are effectively free at runtime. On the other hand, a new version of the Material must be compiled for every <strong>used</strong> combination of static parameters in a Material, which can lead to a massive increase in shader permutations if abused. Try to minimize the number of static parameters in the Material and the number of permutations of those static parameters that are actually used.",
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

| Property | Description |
| --- | --- |
| **Parameter Name** | Specifies the name used to identify the parameter in instances of the Material and through code. |
| **Group** | Provides a way to organize parameter names into groups, or categories, within a MaterialInstanceConstant. All parameters within a Material that have the same Group property name will be listed underneath that category in the Instance Editor. |
| **Default Value** | If *true*, the first input is output. Otherwise, the second input is output. |
| **Extended Caption Display** | If *true*, the title bar of the expressions displays the value of the expression. |
| Inputs |   |
| **A** | Takes in a value of any number of channels. |
| **B** | Takes in a value of any number of channels. |

**Example Usage:** You can use Static Switches to remove an entire branch of a Material with no runtime cost. Material Instances can have different values, making it possible to have a templated shader setup with no performance loss.

```json
{
  "type": "sequence_slider",
  "caption": "Static Switch updated from True to False.",
  "images": [
    {
      "image_id": 24499643,
      "storage_key": "498e688a-d3f8-4db6-ae95-6c4236a69646",
      "context": "documentation",
      "image": {
        "id": 24499643,
        "file_name": "static-switch-comparison-01.png",
        "file_size": 213075,
        "content_type": "image/png",
        "created_at": "2025-04-11T17:40:04.078+00:00",
        "height": 555,
        "width": 1053,
        "storage_key": "498e688a-d3f8-4db6-ae95-6c4236a69646",
        "context": "documentation"
      }
    },
    {
      "image_id": 24499644,
      "storage_key": "8020f5b9-d4ad-4a25-a0cc-e774ecb17d98",
      "context": "documentation",
      "image": {
        "id": 24499644,
        "file_name": "static-switch-comparison-02.png",
        "file_size": 221801,
        "content_type": "image/png",
        "created_at": "2025-04-11T17:40:04.260+00:00",
        "height": 555,
        "width": 1053,
        "storage_key": "8020f5b9-d4ad-4a25-a0cc-e774ecb17d98",
        "context": "documentation"
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

## StaticBoolParameter

The **StaticBoolParameter** works like a StaticSwitchParameter, except that it only creates a bool parameter and does not implement the switch. You can use a StaticBoolParameter to pass a default value into a boolean input on a Material Function.

![Static Bool Parameter](https://dev.epicgames.com/community/api/documentation/image/d20f59b5-6d94-4b5a-b05a-1f9daba3e4ff)

| Property | Description |
| --- | --- |
| **Parameter Name** | Specifies the name used to identify the parameter in instances of the Material and through code. |
| **Group** | Provides a way to organize parameter names into groups, or categories, within a MaterialInstanceConstant. All parameters within a Material that have the same Group property name will be listed underneath that category in the Instance Editor. |
| **Default Value** | The default bool value of the parameter, *True* (checked) or *False*. |

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Static Switches are applied at compile time (not at runtime), meaning you can override the parameter in the Material Instance Editor, but it cannot change during gameplay. Whatever branch of the Material was dropped is never executed, which means static switches are effectively free at runtime. On the other hand, a new version of the Material must be compiled for every <strong>used</strong> combination of static parameters in a Material, which can lead to a massive increase in shader permutations if abused. Try to minimize the number of static parameters in the Material and the number of permutations of those static parameters that are actually used.",
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

This node is used with [MaterialFunctions](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-functions-in-unreal-engine).

## StaticComponentMaskParameter

The **StaticComponentMaskParameter** expression behaves like an ordinary Component Mask, except that you can override the mask values in a Material Instance.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "This parameter is named static because it cannot change at runtime; it can only be set in the Material Instance Editor. Static Switches are applied at compile time, not at runtime. This means that whatever branch of the Material was dropped will never be executed, so static switches are effectively free at runtime. On the other hand, a new version of the Material must be compiled out for every <strong>used</strong> combination of static parameters in a Material, which can lead to a massive increase in shader permutations if abused. Try to minimize the number of static parameters in the Material and the number of permutations of those static parameters that are actually used.",
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

| Property | Description |
| --- | --- |
| **Parameter Name** | Specifies the name used to identify the parameter in instances of the Material and through code. |
| **Group** | Provides a way to organize parameter names into groups, or categories, within a MaterialInstanceConstant. All parameters within a Material that have the same Group property name will be listed underneath that category in the Instance Editor. |
| **Default R** | If checked, the red, or first, channel of the input value is passed through to the output. |
| **Default G** | If checked, the green, or second, channel of the input value is passed through to the output. |
| **Default B** | If checked, the blue, or third, channel of the input value is passed through to the output. |
| **Default A** | If checked, the alpha, or fourth, channel of the input value is passed through to the output. |

**Example Usage:** You can use Static Component Masks to let instances dictate which channel of a mask texture to use. If the mask is static (does not need to change at runtime) then this approach should always be used instead of multiplying a texture lookup by a Vector Parameter to mask out channels, since the latter wastes texture bandwidth and shader instructions.

```json
{
  "type": "sequence_slider",
  "caption": "Checked channels pass through to the output, while unchecked channels are discarded.",
  "images": [
    {
      "image_id": 24499645,
      "storage_key": "6064e4cb-71c2-4d13-8d94-8fd6fa78c94a",
      "context": "documentation",
      "image": {
        "id": 24499645,
        "file_name": "component-mask-example-01.png",
        "file_size": 225729,
        "content_type": "image/png",
        "created_at": "2025-04-11T17:40:04.429+00:00",
        "height": 418,
        "width": 1020,
        "storage_key": "6064e4cb-71c2-4d13-8d94-8fd6fa78c94a",
        "context": "documentation"
      }
    },
    {
      "image_id": 24499646,
      "storage_key": "8ea7bac2-4582-41d6-a608-6a1035a09526",
      "context": "documentation",
      "image": {
        "id": 24499646,
        "file_name": "component-mask-example-02.png",
        "file_size": 212900,
        "content_type": "image/png",
        "created_at": "2025-04-11T17:40:04.595+00:00",
        "height": 418,
        "width": 1020,
        "storage_key": "8ea7bac2-4582-41d6-a608-6a1035a09526",
        "context": "documentation"
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

## VectorParameter

The **VectorParameter** expression is identical to the [Constant4Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/constant-material-expressions-in-unreal-engine), except that it is a parameter you can modify in instances of the Material and through code. One nicety of the VectorParameter is that you can set its value using the Color Picker.

| Item | Description |
| --- | --- |
| Properties |   |
| **Parameter Name** | Specifies the name used to identify the parameter in instances of the Material and through code. |
| **Group** | Provides a way to organize parameter names into groups, or categories, within a MaterialInstanceConstant. All parameters within a Material that have the same Group property name will be listed underneath that category in the Instance Editor. |
| **Default Value** **R** **G** **B** **A** | The vector to output by default unless overridden by a Material Instance Constant. Specifies the float value of the red, or first, channel of the vector the expression outputs. Specifies the float value of the green, or second, channel of the vector the expression outputs. Specifies the float value of the blue, or third, channel of the vector the expression outputs. Specifies the float value of the alpha, or fourth, channel of the vector the expression outputs. |

![Vector Parameter example graph](https://dev.epicgames.com/community/api/documentation/image/c23c4548-fda7-47b3-a407-b5965c2d34f7)

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "VertexColor is mutually exclusive with the Transform node due to limited interpolators. If you use both a Transform node and VertexColor, then VertexColor will come out all white.",
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

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<strong>Programmers:</strong> For sprite particles, colors are communicated to the shader per vertex, whereas colors for mesh particles are set as shader constants.",
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

```json
{
  "type": "include",
  "excerpt_id": 351,
  "excerpt_assignment_id": 348,
  "blocks": [
    {
      "type": "header",
      "content": "TextureObjectParameter",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <strong>TextureObjectParameter</strong> expression defines a texture parameter and outputs the texture object. This expression is frequently used to pass texture parameters into a Material Function with texture inputs.  Texture inputs on a Material Function node are not compatible with Float3 data from a TextureSample 2D node, so the Texture Object (T2d) is required. This node does not actually sample the texture, so it must be used in conjunction with a <strong>TextureSample</strong> node.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24499636,
      "caption": "",
      "alt_text": "Texture Object Parameter",
      "image": {
        "id": 24499636,
        "file_name": "texture-object-parameter-example.png",
        "file_size": 75261,
        "content_type": "image/png",
        "created_at": "2025-04-11T17:40:01.729+00:00",
        "height": 280,
        "width": 783,
        "storage_key": "c798b13e-8a10-466a-84b4-b0dde09b021f",
        "context": "documentation"
      },
      "storage_key": "c798b13e-8a10-466a-84b4-b0dde09b021f",
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
              "content": "<strong>Parameter Name</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the name used to identify the parameter in instances of the Material and through code.",
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
              "content": "<strong>Group</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Provides a way to organize parameter names into groups, or categories, within a MaterialInstanceConstant. All parameters within a Material that have the same Group property name will be listed underneath that category in the Instance Editor.",
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
              "content": "<strong>Texture</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the texture sampled by the expression.",
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
              "content": "<strong>Sampler Type</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The type of data that will be sampled and output from the node.",
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
              "content": "<strong>MipValueMode</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Selects how to customize the sample's mip-level or derivatives from the default hardware computed. Affects the look and performance.",
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
      "content": "This node is used with <a data-document-id=\"3226393\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/material-functions-in-unreal-engine\">MaterialFunctions</a>.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "P9L",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "include",
  "excerpt_id": 352,
  "excerpt_assignment_id": 349,
  "blocks": [
    {
      "type": "header",
      "content": "TextureSampleParameter2D",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <strong>TextureSampleParameter2D</strong> expression is identical to the TextureSample except that it is a parameter that you can modify in Material Instances and through Blueprint or code.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24499637,
      "caption": "",
      "alt_text": "Texture Sample Parameter",
      "image": {
        "id": 24499637,
        "file_name": "texture-sample-parameter.png",
        "file_size": 41785,
        "content_type": "image/png",
        "created_at": "2025-04-11T17:40:02.030+00:00",
        "height": 241,
        "width": 464,
        "storage_key": "702e4d79-64bb-45b8-a4b9-0de5e5b57fc6",
        "context": "documentation"
      },
      "storage_key": "702e4d79-64bb-45b8-a4b9-0de5e5b57fc6",
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
              "content": "<strong>Parameter Name</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the name used to identify the parameter in instances of the Material and through code.",
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
              "content": "<strong>Group</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Provides a way to organize parameter names into groups, or categories, within a MaterialInstanceConstant. All parameters within a Material that have the same Group property name will be listed underneath that category in the Instance Editor.",
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
              "content": "<strong>Texture</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the texture sampled by the expression.",
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
              "content": "<strong>Sampler Type</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The type of data that will be sampled and output from the node.",
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
              "content": "<strong>MipValueMode</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Selects how to customize the sample's mip-level or derivatives from the default hardware computed. Affects the look and performance.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Inputs",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": " ",
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
              "content": "<strong>UVs</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Takes in UV texture coordinates to use for the texture. If no values are input to the UVs, the texture coordinates of the mesh the material is applied to are used.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Outputs",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": " ",
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
              "content": "<strong>RGB</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the three-channel RGB vector value of the color.",
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
              "content": "<strong>R</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the red channel of the color.",
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
              "content": "<strong>G</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the green channel of the color.",
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
              "content": "<strong>B</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the blue channel of the color.",
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
              "content": "<strong>A</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the alpha channel of the color. If a texture does not contain an alpha channel, connecting the 'alpha' channel to something, while not technically illegal, will always result in zero (black).",
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
  "excerpt_hash_id": "Qeb",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "include",
  "excerpt_id": 353,
  "excerpt_assignment_id": 350,
  "blocks": [
    {
      "type": "header",
      "content": "TextureSampleParameterSubUV",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <strong>TextureSampleParameterSubUV</strong> expression is identical to the <a data-document-id=\"3226655\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/particle-material-expressions-in-unreal-engine\">ParticleSubUV</a> except that it is a parameter that can be modified in instances of the material and through code.",
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
              "type": "enhanced_table_header",
              "content": "Properties",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": " ",
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
              "content": "<strong>Parameter Name</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the name used to identify the parameter in instances of the Material and through code.",
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
              "content": "<strong>Group</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Provides a way to organize parameter names into groups, or categories, within a MaterialInstanceConstant. All parameters within a Material that have the same Group property name will be listed underneath that category in the Instance Editor.",
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
              "content": "<strong>Blend</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Blends together each frame of the SubUV sprite layout, rather than instantly \"popping\" from one frame to the next.",
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
              "content": "<strong>Texture</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the texture sampled by the expression.",
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
              "content": "<strong>Sampler Type</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The type of data that will be sampled and output from the node.",
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
              "content": "<strong>MipValueMode</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Selects how to customize the sample's mip-level or derivatives from the default hardware computed. Affects the look and performance.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Inputs",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": " ",
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
              "content": "<strong>UVs</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The UV input is ignored and does nothing.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Outputs",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": " ",
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
              "content": "<strong>RGB</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the three-channel RGB vector value of the color.",
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
              "content": "<strong>R</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the red channel of the color.",
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
              "content": "<strong>G</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the green channel of the color.",
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
              "content": "<strong>B</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the blue channel of the color.",
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
              "content": "<strong>A</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the alpha channel of the color. If a texture does not contain an alpha channel, connecting the 'alpha' channel to something, while not technically illegal, will always result in zero (black).",
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
  "excerpt_hash_id": "Go6",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "include",
  "excerpt_id": 354,
  "excerpt_assignment_id": 351,
  "blocks": [
    {
      "type": "header",
      "content": "TextureSampleParameterCube",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <strong>TextureSampleParameterCube</strong> expression is identical to the TextureSample except that it only accepts cubemaps and it is a parameter that can be modified in instances of the material and through code.",
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
              "content": "<strong>Parameter Name</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the name used to identify the parameter in instances of the Material and through code.",
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
              "content": "<strong>Group</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Provides a way to organize parameter names into groups, or categories, within a MaterialInstanceConstant. All parameters within a Material that have the same Group property name will be listed underneath that category in the Instance Editor.",
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
              "content": "<strong>Texture</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the texture sampled by the expression.",
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
              "content": "<strong>Sampler Type</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The type of data that will be sampled and output from the node.",
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
              "content": "<strong>MipValueMode</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Selects how to customize the sample's mip-level or derivatives from the default hardware computed. Affects the look and performance.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Inputs",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": " ",
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
              "content": "<strong>UVs</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Takes in UV texture coordinates to use for the texture. If no values are input to the UVs, the texture coordinates of the mesh the Material is applied to are used. This input accepts a two-channel vector value.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Outputs",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": " ",
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
              "content": "<strong>RGB</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the three-channel RGB vector value of the color.",
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
              "content": "<strong>R</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the red channel of the color.",
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
              "content": "<strong>G</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the green channel of the color.",
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
              "content": "<strong>B</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the blue channel of the color.",
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
              "content": "<strong>A</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the alpha channel of the color. If a texture does not contain an alpha channel, connecting the 'alpha' channel to something, while not technically invalid, will always result in zero (black).",
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
  "excerpt_hash_id": "ZZ9",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "include",
  "excerpt_id": 355,
  "excerpt_assignment_id": 352,
  "blocks": [
    {
      "type": "header",
      "content": "TextureSampleParameterMovie",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <strong>TextureSampleParameterMovie</strong> expression is identical to the TextureSample except that it only accepts movie textures (Bink movies) and it is a parameter that you can modify in instances of the Material and through code.",
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
              "content": "<strong>Parameter Name</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the name used to identify the parameter in instances of the Material and through code.",
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
              "content": "<strong>Group</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Provides a way to organize parameter names into groups, or categories, within a MaterialInstanceConstant. All parameters within a Material that have the same Group property name will be listed underneath that category in the Instance Editor.",
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
              "content": "<strong>Texture</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the texture sampled by the expression.",
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
              "content": "<strong>Sampler Type</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The type of data that will be sampled and output from the node.",
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
              "content": "<strong>MipValueMode</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Selects how to customize the sample's mip-level or derivatives from the default hardware computed. Affects the look and performance.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Inputs",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": " ",
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
              "content": "<strong>UVs</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Takes in UV texture coordinates to use for the texture. If no values are input to the UVs, the texture coordinates of the mesh the Material is applied to are used.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Outputs",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": " ",
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
              "content": "<strong>RGB</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the three-channel RGB vector value of the color.",
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
              "content": "<strong>R</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the red channel of the color.",
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
              "content": "<strong>G</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the green channel of the color.",
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
              "content": "<strong>B</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the blue channel of the color.",
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
              "content": "<strong>A</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Outputs the alpha channel of the color. If a texture does not contain an alpha channel, connecting the 'alpha' channel to something, while not technically illegal, will always result in zero (black).",
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
  "excerpt_hash_id": "nvX",
  "settings": {
    "is_hidden": false
  }
}
```
