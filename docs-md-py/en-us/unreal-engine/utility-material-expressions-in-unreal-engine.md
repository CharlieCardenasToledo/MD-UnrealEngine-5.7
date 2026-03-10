# Utility Material Expressions

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine

> Application Version: 5.7

**Utility Material Expressions** are nodes that can affect Materials in a number of different ways than one might be used to. For example the **GIReplace** node will replace an object's indirect bounce color with a given value you input, while the Linear Interpolate node will help blend between two textures based on an Alpha input. On the following page you will find detailed descriptions for all of the Utility expressions are available in the Material Editor.

```json
{
  "type": "include",
  "excerpt_id": 687,
  "excerpt_assignment_id": 1517,
  "blocks": [
    {
      "type": "header",
      "content": "AntialiasedTextureMask",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <strong>AntialiasedTextureMask</strong> expression allows you to create a Material using a soft (anti-aliased) transition mask. The mask can be used to blend between two complex Material properties or to fade out an alpha blended Material (works well with SoftMasked). Specify a texture with the mask specified in one channel (red, green, blue, or alpha), set the used channel in the expression and specify the comparison value. Assuming the channel stores a grayscale value in the range 0 = black to 1 = white the comparison function defines if the resulting mask should be 0 or 1. This expression is a parameter, allowing the <strong>Texture</strong> property to be overridden by child MaterialInstances.",
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
              "content": "<strong>Threshold</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the value used as the cutoff point in pixel coverage. Pixel coverage values less than this become black; values greater become white.",
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
              "content": "<strong>Channel</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the channel of the Texture to use as the mask.",
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
              "content": "Specifies the mask texture to use.",
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
              "content": "Takes in texture coordinates to apply to the texture mask.",
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
      "content": "<strong>Pseudo code:</strong>",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "code_snippet",
      "description": null,
      "snippet_type": "cpp_programming",
      "title": null,
      "code_preview": "Result = 1\n    if TextureLookup &lt; Threshold then Result = 0",
      "lines_of_code": 2,
      "id": 39386,
      "url_signature": "eyJzbmlwcGV0X2lkIjozOTM4NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIwOjA1KzAwOjAwIn0=--a1b8fb3afae981271bb2728aae04f0ed6c57bfd02ec08f2d0a3f00100f7a05a2",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The actual implementation is quite a bit more complicated as it tries to return values between 0 and 1 depending on the actual pixel coverage to avoid aliasing.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Example (this tiny 128x128 texture, uncompressed for best quality):",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24514660,
      "caption": "",
      "alt_text": "ULogoLowBlurred.png",
      "image": {
        "id": 24514660,
        "file_name": "ULogoLowBlurred.png",
        "file_size": 6675,
        "content_type": "image/png",
        "created_at": "2025-04-16T22:02:23.232+00:00",
        "height": 128,
        "width": 128,
        "storage_key": "9ff5c452-c621-4c1d-b04c-27c111a7f94f",
        "context": "documentation"
      },
      "storage_key": "9ff5c452-c621-4c1d-b04c-27c111a7f94f",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Was used as a normal texture (left top) and used with the described material expression (bottom right):",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24514661,
      "caption": "",
      "alt_text": "AAMasked_Demo.png",
      "image": {
        "id": 24514661,
        "file_name": "AAMasked_Demo.png",
        "file_size": 24361,
        "content_type": "image/png",
        "created_at": "2025-04-16T22:02:23.490+00:00",
        "height": 256,
        "width": 256,
        "storage_key": "09c91591-a784-4be8-8651-4d2ab6ea06c5",
        "context": "documentation"
      },
      "storage_key": "09c91591-a784-4be8-8651-4d2ab6ea06c5",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The technique works best in magnification and with blurred input content. Compression hurts the quality a lot so try to use uncompressed low resolution textures.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "v2N",
  "settings": {
    "is_hidden": false
  }
}
```

## BlackBody

The **BlackBody** expression simulates the effects of [black body radiation](http://en.wikipedia.org/wiki/Black-body_radiation) within your Material. The user inputs a temperature (in Kelvin) and the resulting color and intensity can be used to drive Base Color and Emissive values to get a physically accurate result.

![Blackbody Expression](https://dev.epicgames.com/community/api/documentation/image/3c62b55c-e100-4dfa-9075-5fbcb91bc12a)

## BumpOffset

```json
{
  "type": "include",
  "excerpt_id": 688,
  "excerpt_assignment_id": 1518,
  "blocks": [
    {
      "type": "paragraph",
      "content": "<strong>BumpOffset</strong> is the Unreal Engine 4 term for what is commonly known as 'Parallax Mapping'.  The Bump Offset expression allows a material to give the illusion of depth without the need for additional geometry.  BumpOffset materials use a grayscale <em>heightmap</em> to give depth information.  The brighter the value in the heightmap, the more 'popped out' the material will be; these areas will parallax (shift) as a camera moves across the surface.  Darker areas in the heightmap are 'further away' and will shift the least.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "eMz",
  "settings": {
    "is_hidden": false
  }
}
```

| Item | Description |
| --- | --- |
| Properties |   |
| **HeightRatio** | Multiplier for the depth taken from the *heightmap*. The larger the value, the more extreme the depth will be. Typical values range from 0.02 to 0.1. |
| **ReferencePlane** | Specifies the approximate height in texture space to apply the effect. A value of 0 will appear to distort the texture completely off the surface, whereas a value of 0.5 (the default) means that some of the surface will pop off while some areas will be sunken in. |
| Inputs |   |
| **Coordinate** | Takes in base texture coordinates to be modified by the expression. |
| **Height** | Takes in the texture (or a value) to be used as the heightmap. |
| **HeightRatioInput** | Multiplier for the depth taken from the *heightmap*. The larger the value, the more extreme the depth will be. Typical values range from 0.02 to 0.1. If used, this input supersedes any value in the Height Ratio property. |

![Bump Offset Expression](https://dev.epicgames.com/community/api/documentation/image/03d562c1-dce8-4de2-9209-b8442af5ca7b)

## ConstantBiasScale

The **ConstantBiasScale** expression takes an input value, adds a bias value to it, and then multiplies it by a scaling factor outputting the result. So for example, to convert input data from [-1,1] to [0,1] you would use a bias of 1.0 and a scale of 0.5.

| Properties | Description |
| --- | --- |
| **Bias** | Specifies the value to be added to the input. |
| **Scale** | Specifies the multiplier for the biased result. |

![Constant Bias Scale Expression](https://dev.epicgames.com/community/api/documentation/image/284d91ec-51e5-4f2b-b03d-7f00ad8a928b)

## DDX

The **DDX** expression exposes DDX derivative calculation, a GPU hardware feature used in pixel shader calculation.

## DDY

The **DDY** expression exposes DDY derivative calculation, a GPU hardware feature used in pixel shader calculation.

## DepthFade

The **DepthFade** expression is used to hide unsightly seams that take place when translucent objects intersect with opaque ones.

| Item | Description |
| --- | --- |
| Properties |   |
| **Fade Distance** | World space distance over which the fade should take place. This is used if the FadeDistance input is unconnected. |
| Inputs |   |
| **Opacity** | Takes in the existing opacity for the object prior to the depth fade. |
| **FadeDistance** | World space distance over which the fade should take place. |

```json
{
  "type": "comparison_slider",
  "image_left_id": 25783825,
  "caption_left": "Without Depth Fade",
  "image_right_id": 25783826,
  "caption_right": "With Depth Fade",
  "image_left": {
    "id": 25783825,
    "file_name": "depth-fade-slider-01.png",
    "file_size": 777024,
    "content_type": "image/png",
    "created_at": "2025-07-07T20:35:58.748+00:00",
    "height": 664,
    "width": 1159,
    "storage_key": "7b79513e-1775-4af9-ab48-932767662fba",
    "context": "documentation"
  },
  "image_right": {
    "id": 25783826,
    "file_name": "depth-fade-slider-02.png",
    "file_size": 788734,
    "content_type": "image/png",
    "created_at": "2025-07-07T20:35:58.996+00:00",
    "height": 664,
    "width": 1159,
    "storage_key": "f8d41ac2-2dcc-44f8-b447-b7ead27e1756",
    "context": "documentation"
  },
  "image_left_storage_key": "7b79513e-1775-4af9-ab48-932767662fba",
  "image_right_storage_key": "f8d41ac2-2dcc-44f8-b447-b7ead27e1756",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

The Material network for this example is pictured below.

![Depth Fade Material Graph](https://dev.epicgames.com/community/api/documentation/image/bb817c60-f3f4-46f6-a260-a2799486d27c)

## DepthOfFieldFunction

The **Depth of Field Function** expression is designed to give artists control over what happens to a Material when it is being blurred by Depth of Field. It outputs a value between 0-1 such that 0 represents "in focus" and 1 represents "completely blurred." This is useful for interpolating between sharp and blurry versions of a texture, for instance. The Depth input allows for the existing results from the scene's Depth of Field calculations to be overridden by other calculations.

```json
{
  "type": "comparison_slider",
  "image_left_id": 25783827,
  "caption_left": "Blended Colors",
  "image_right_id": 25783828,
  "caption_right": "Blending regular and blurred textures",
  "image_left": {
    "id": 25783827,
    "file_name": "DepthOfFieldFunction_Color.png",
    "file_size": 1254081,
    "content_type": "image/png",
    "created_at": "2025-07-07T20:35:59.169+00:00",
    "height": 977,
    "width": 1618,
    "storage_key": "da8a336f-6e52-421b-b437-1e9ca93c2db5",
    "context": "documentation"
  },
  "image_right": {
    "id": 25783828,
    "file_name": "DepthOfFieldFunction_Texture.png",
    "file_size": 1434922,
    "content_type": "image/png",
    "created_at": "2025-07-07T20:35:59.306+00:00",
    "height": 977,
    "width": 1618,
    "storage_key": "ba28c308-6622-4044-9210-ea66fc114e51",
    "context": "documentation"
  },
  "image_left_storage_key": "da8a336f-6e52-421b-b437-1e9ca93c2db5",
  "image_right_storage_key": "ba28c308-6622-4044-9210-ea66fc114e51",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

![Depth of Field function](https://dev.epicgames.com/community/api/documentation/image/675736c7-f283-4e6c-827a-a9cd2e1acee3)

_Click image for full size view._

```json
{
  "type": "include",
  "excerpt_id": 689,
  "excerpt_assignment_id": 1519,
  "blocks": [
    {
      "type": "header",
      "content": "Desaturation",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <strong>Desaturation</strong> expression desaturates its input, or converts the colors of its input into shades of gray, based a certain percentage.",
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
              "content": "<strong>Luminance Factors</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the amount that each channel contributes to the desaturated color. This is what controls that green is brighter than red which is brighter than blue when desaturated.",
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
              "content": "<strong>Fraction</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the amount of desaturation to apply to the input. Percent can range from 0.0 (full original color, no desaturation) to 1.0 (fully desaturated).",
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
      "image_id": 24514662,
      "caption": "",
      "alt_text": "Desaturation Example",
      "image": {
        "id": 24514662,
        "file_name": "desaturation.png",
        "file_size": 310993,
        "content_type": "image/png",
        "created_at": "2025-04-16T22:02:24.082+00:00",
        "height": 436,
        "width": 1102,
        "storage_key": "1123c67c-3d78-429e-8a30-d917472004b4",
        "context": "documentation"
      },
      "storage_key": "1123c67c-3d78-429e-8a30-d917472004b4",
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
          "content": "<strong>Programmers:</strong> Define desaturated color <code>D</code>, input color <code>I</code> and luminance factor <code>L</code>.  The output will be <code>O = (1 - Percent)*( D.dot( I )) + Percent * I</code>",
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
  "excerpt_hash_id": "bMm",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "include",
  "excerpt_id": 690,
  "excerpt_assignment_id": 1520,
  "blocks": [
    {
      "type": "header",
      "content": "Distance",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <strong>Distance</strong> expression computes the (Euclidian) distance between two points/colors/positions/vectors and outputs the resulting value. This works on one, two, three and four component vectors, but both inputs to the expression must have the same number of channels.",
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
              "content": "<strong>A</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Takes in a value or vector of any length.",
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
              "content": "Takes in a value or vector of any length.",
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
      "type": "sequence_slider",
      "caption": "Note how the color changes as the camera distance increases.",
      "images": [
        {
          "image_id": 24514663,
          "storage_key": "c64edd57-f128-4f51-80ac-21d48bcb68a5",
          "context": "documentation",
          "image": {
            "id": 24514663,
            "file_name": "distance-01.png",
            "file_size": 354783,
            "content_type": "image/png",
            "created_at": "2025-04-16T22:02:24.505+00:00",
            "height": 602,
            "width": 1545,
            "storage_key": "c64edd57-f128-4f51-80ac-21d48bcb68a5",
            "context": "documentation"
          }
        },
        {
          "image_id": 24514664,
          "storage_key": "bee45474-c093-4977-8c80-798e7ab9bfe3",
          "context": "documentation",
          "image": {
            "id": 24514664,
            "file_name": "distance-02.png",
            "file_size": 311535,
            "content_type": "image/png",
            "created_at": "2025-04-16T22:02:24.702+00:00",
            "height": 602,
            "width": 1545,
            "storage_key": "bee45474-c093-4977-8c80-798e7ab9bfe3",
            "context": "documentation"
          }
        }
      ],
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "<strong>Pseudo code:</strong>",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "code_snippet",
      "description": null,
      "snippet_type": "cpp_programming",
      "title": null,
      "code_preview": "Result = length (A - B)",
      "lines_of_code": 1,
      "id": 39387,
      "url_signature": "eyJzbmlwcGV0X2lkIjozOTM4NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIwOjA1KzAwOjAwIn0=--7cfabed2b182835ad6d04a0e3ad65c9820fb6c84fb06dc74b8e3c3df2fc52760",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "<strong>Low level HLSL code:</strong>",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "code_snippet",
      "description": null,
      "snippet_type": "cpp_programming",
      "title": null,
      "code_preview": "float Result = sqrt (dot (A-B, A-B))",
      "lines_of_code": 1,
      "id": 39388,
      "url_signature": "eyJzbmlwcGV0X2lkIjozOTM4OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIwOjA1KzAwOjAwIn0=--62b36501214c796813066a8e802036b3648239ef64d306a780d8eabd3554d39a",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "z2G",
  "settings": {
    "is_hidden": false
  }
}
```

## DistanceFieldGradient

The **DistanceFieldGradient** Material Expression node, when normalized, outputs the X,Y,Z direction an object would move with in the distance field.
This makes the Distance Field Gradient Material Expression node well-suited for Materials that need to simulate the flow of liquids.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<strong>Generate Mesh Distance Fields</strong> must be enabled in <strong>Project Settings</strong> under <strong>Rendering</strong> for this expression to work correctly.",
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

| Item | Description |
| --- | --- |
| **Position** | Defaults to current World Position if nothing is input. |

Here is an example of how to use the **DistanceFieldGradient** Material Expression in your Materials.
In this example below make sure to note that the DistanceFieldGradient was first normalized and then input into a Mask Channel node.
The reason for this is because without normalizing the DistanceFieldGradient first you can not get directional data.
The Mask Channel Parameter was added to allow for easier RGB channel switching with in the Material Instance.

![Distance field gradient](https://dev.epicgames.com/community/api/documentation/image/9d8dbb2e-a294-4e53-87ce-8949ba310355)

_Click image for full size view._

Here is an example of the DistanceFieldGradient in action.
The image below shows what data the DistanceFieldGradient will use when the various RGB are enabled.

![Image](https://dev.epicgames.com/community/api/documentation/image/879e8a98-ff71-4c1d-8313-c583b4479678)

_Click image for full size view._

| Number | Description |
| --- | --- |
| **1** | Enabling the R channel and disabling all other channels. |
| **2** | Enabling the G channel and disabling all other channels. |
| **3** | Enabling the B channel and disabling all other channels. |

## DistanceToNearestSurface

The **Distance To Nearest Surface** Material Expression node allows Materials to sample any point in the levels Global Distance Field.
This Material Expression works by outputting the signed distance in world space units from the distance field to the nearest occluders in the scene.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<strong>Generate Mesh Distance Fields</strong> must be enabled in <strong>Project Settings</strong> under <strong>Rendering</strong> for this expression to work correctly.",
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

| Item | Description |
| --- | --- |
| **Position** | Defaults to current World Position if nothing is input. |

Here is an example of the **Distance To Nearest Surface** Material Expression in action.

![Distance to Surface](https://dev.epicgames.com/community/api/documentation/image/142734a7-c8c5-4886-b7d2-aa356c46b20c)

_Click image for full size view._

![Image](https://dev.epicgames.com/community/api/documentation/image/3af6c431-d170-4340-bece-46551044a036)

In this example the Distance To Nearest Surface was fed into the Opacity input on a Material and that Material was applied to a Static Mesh plane that was placed just above the levels floor.
What the Distance To Nearest Surface is doing is telling the Material to only color areas red were the Static Meshes plane will start to intersect other Static Meshes placed in the scene.

```json
{
  "type": "include",
  "excerpt_id": 691,
  "excerpt_assignment_id": 1521,
  "blocks": [
    {
      "type": "header",
      "content": "FeatureLevelSwitch",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <strong>Feature Level Switch</strong> node allows you to make simplified materials for lower powered devices.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "<strong>Example Usage</strong>: You might have a material with 10 textures overlapping and complex math, but just a single static texture for mobile (feature level ES2).",
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
              "content": "Inputs",
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
              "content": "<strong>Default</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The default Feature Level.",
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
              "content": "<strong>ES2</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Feature Level defined by the core capabilities of OpenGL ES2.",
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
              "content": "<strong>ES3.1</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Feature Level defined by the capabilities of Metal-level devices.",
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
              "content": "<strong>SM4</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Feature Level defined by the core capabilities of DX10 Shader Model 4.",
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
              "content": "<strong>SM5</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Feature Level defined by the core capabilities of DX11 Shader Model 5.",
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
  "excerpt_hash_id": "5VR",
  "settings": {
    "is_hidden": false
  }
}
```

## Fresnel

The **Fresnel** expression calculates a falloff based on the dot product of the surface normal and the direction to the camera. When the surface normal points directly at the camera, a value of 0 is output. When the surface normal is perpendicular to the camera, a value of 1 is output. The result is clamped to [0,1] so you do not have any negative color in the center.

| Item | Description |
| --- | --- |
| Properties |   |
| **Exponent** | Specifies the how quickly the output value falls off. Larger values mean tighter or quicker falloff. |
| **Base Reflect Fraction** | Specifies the fraction of specular reflection the surface is viewed from straight on. A value of 1 effectively disables the Fresnel effect. |
| Inputs |   |
| **ExponentIn** | Specifies the how quickly the output value falls off. Larger values mean tighter or quicker falloff. If used, value will always supersede the Exponent property value. |
| **Base Reflect Fraction** | Specifies the fraction of specular reflection the surface is viewed from straight on. A value of 1 effectively disables the Fresnel effect. If used, value will always supersede the Exponent property value. |
| **Normal** | Takes in a three-channel vector value representing the normal of the surface, in world space. To see the results of a normal map applied to the surface of the Fresnel object, connect the normal map to the Normal input of the material, then connect a [PixelNormalWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine) expression to this input on the Fresnel. If no normal is specified, the tangent normal of the mesh is used. |

![Fresnel Example](https://dev.epicgames.com/community/api/documentation/image/ae8313f1-d5b1-448f-af97-d224b651f6e3)

```json
{
  "type": "include",
  "excerpt_id": 692,
  "excerpt_assignment_id": 1522,
  "blocks": [
    {
      "type": "header",
      "content": "GIReplace",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "<strong>GIReplace</strong> allows artists to specify a different, usually simpler, expression chain when the material is being used for GI.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "<strong>Example Usage</strong>: Lightmass static GI and LPV dynamic GI use it.",
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
              "content": "Inputs",
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
              "content": "<strong>Default</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The default GI.",
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
              "content": "<strong>StaticIndirect</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used for baked indirect lighting.",
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
              "content": "<strong>DynamicIndirect</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used for dynamic indirect lighting.",
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
  "excerpt_hash_id": "y2x",
  "settings": {
    "is_hidden": false
  }
}
```

## LightmassReplace

The **LightmassReplace** expression simply passes through the Realtime input when compiling the material for normal rendering purposes, and passes through the Lightmass input when exporting the material to Lightmass for global illumination. This is useful to work around material expressions that the exported version cannot handle correctly, for example WorldPosition.

| Inputs | Description |
| --- | --- |
| **Realtime** | Takes in the value(s) to pass through for normal rendering. |
| **Lightmass** | Takes in the value(s) to pass through when exporting the material to Lightmass. |

```json
{
  "type": "include",
  "excerpt_id": 693,
  "excerpt_assignment_id": 1523,
  "blocks": [
    {
      "type": "header",
      "content": "LinearInterpolate",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <strong>LinearInterpolate</strong> expression blends between two input value(s) based on a third input value used as a mask. This can be thought of as a mask to define transitions between two textures, like a layer mask in Photoshop.  The intensity of the mask Alpha determines the ratio of color to take from the two input values.  If Alpha is 0.0, the first input is used.  If Alpha is 1.0, the second input is used.  If Alpha is between 0.0 and 1.0, the output is a blend between the two inputs. Keep in mind that the blend happens per channel.  So, if Alpha is an RGB color, Alpha's red channel value defines the blend between A and B's red channels <strong>independently</strong> of Alpha's green channel, which defines the blend between A and B's green channels.",
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
              "content": "<strong>Const A</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The value mapped to 0.0. Only used if the A input is unconnected.",
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
              "content": "<strong>Const B</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The value mapped to 1.0. Only used if the B input is unconnected.",
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
              "content": "<strong>Const Alpha</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Takes in the value to use as the mask alpha. Only used if the Alpha input is unconnected.",
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
              "content": "<strong>A</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Takes in the value(s) mapped to 0.0.",
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
              "content": "Takes in the value(s) mapped to 1.0.",
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
              "content": "<strong>Alpha</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Takes in the value to use as the mask alpha.",
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
      "content": "<strong>Programmers:</strong> LinearInterpolate does a per-channel lerp between A and B based on the parametric value Alpha.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24514665,
      "caption": "",
      "alt_text": "Lerp Example",
      "image": {
        "id": 24514665,
        "file_name": "lerp-expression.png",
        "file_size": 183436,
        "content_type": "image/png",
        "created_at": "2025-04-16T22:02:25.933+00:00",
        "height": 451,
        "width": 1136,
        "storage_key": "bb7d87b0-52d0-439f-95a5-c803230f69ce",
        "context": "documentation"
      },
      "storage_key": "bb7d87b0-52d0-439f-95a5-c803230f69ce",
      "context": "documentation",
      "width": 900,
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "q2v",
  "settings": {
    "is_hidden": false
  }
}
```

## Noise

The **Noise** expression creates a procedural noise field, giving you control over how it is generated.

| Item | Description |
| --- | --- |
| Properties |   |
| **Scale** | Changes the overall size of the noise cells. Lower numbers make the noise bigger. |
| **Quality** | A look/performance setting. Lower values are faster but may look worse, higher values are slower but may look better. |
| **Function** | **Simplex** (Texture Based): High quality for direct use and bumps about 77 instructions per level, 4 Texture lookups, can not tile. **Gradient** (Texture Based): High quality for direct use and bumps. Non-tiled: about 61 instructions per level, 8 Texture lookups. Tiling: about 74 instructions per level, 8 Texture lookups. Even "non tiled' mode has a repeat of 128. Useful repeat size range <= 128. Formerly labeled as Perlin Noise. **Fast Gradient** (3D Texture): High quality for direct use, **BAD** for bumps. about 16 instructions per level, 1 Texture lookup. Always tiles with a repeat of 16, "Tiling" mode is not an option for Fast Gradient noise. **Gradient** (Computational): High quality for direct use and bumps. Non-tiled: about 80 instructions per level, no Textures. Tiling: about 143 instructions per level, no Textures. **Value** (Computational): Low quality, but pure computation. Non-tiled: about 53 instructions per level, no Textures. Tiling: about 118 instructions per level, no Textures. Formerly mislabeled as Gradient noise. **Voronoi**: Also know as Worley or Cellular noise. Quality = 1 searches 8 cells, Quality = 2 searches 16 cells, Quality = 3 searches 27 cells, Quality = 4 searches 32 cells. All are about about 20 instructions per cell searched. |
| **Turbulence** | With Turbulence on, each noise octave will add only absolute values to the result. Changes the visual characteristics and can great shapes resembling sharp mountain ridges |
| **Levels** | How many different levels of noise at different scales to combine, multiplies the computational cost by the number of levels. |
| **Output Min** | The lowest value output by the noise calculation. |
| **Output Max** | The highest value output by the noise calculation. |
| **Level Scale** | Level scale is always active and determines how much the scale changes for each new octave. |
| **Tiling** | For noise functions that support it, allows noise to tile. This is more expensive, but useful when baking noise into a seamless wrapping texture. |
| **Repeat Size** | When tiling, how often should the noise repeat. |
| Inputs |   |
| **Position** | Allows the texture size to be adjusted via a 3D vector. |
| **FilterWidth** | In effect, controls how much blur will be applied to the noise texture. |

![Noise Example](https://dev.epicgames.com/community/api/documentation/image/93535665-9c8a-4342-80f3-4cae14583194)

## Previous Frame Switch

The **Previous Frame Switch** Material Expression assists with the implementation of complex [vertex animations](https://dev.epicgames.com/documentation/en-us/unreal-engine/vertex-animation-tool-in-unreal-engine) in Materials by providing a way to generate correct motion vectors which work correctly with Temporal AA and Motion Blur.

Materials that are only a function of time already work without modification, however, they cannot account for other variables, such as Material Parameters, that can affect the animation at runtime. The Previous Frame Switch Material Expression provides a means to solve these problems manually by tracking how these parameters change. For example, in Blueprints they could manually provide expressions for motion vector generation that is caused by changes in World Position Offset between frames.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Velocities from vertex deformation must be enabled in <strong>Project Settings</strong> under <strong>Rendering</strong> for this expression to work.",
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
            "content": "4.24 and later versions use <strong>Accurate velocities from Vertex Deformation</strong>",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "4.25 and future versions use <strong>Output velocities due to vertex deformation</strong>",
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
  "settings": {
    "is_hidden": false
  }
}
```

| Item | Description |
| --- | --- |
| Current Frame | Directional Vector used as the starting position reference. |
| Previous Frame | Directional Vector used as the XYZ reference for the amount of blur to add. |

Here is an example using **Previous Frame Switch** Material Expression in a Material.

![Previous Frame Switch](https://dev.epicgames.com/community/api/documentation/image/0f880f67-c8e3-480b-820b-3ce8d17fe7c3)

In this example, the Previous Frame Switch is using a constant value to control the directional blur through a Multiply node.

[Video: 0_bbk4eygc](https://dev.epicgames.com/community/api/cms/videos/0_bbk4eygc/embed.html)

In this example, you can see how this is being used in Epic's own games, like Fortnite, to control the motion blur with a Vertex Animation that assembles on screen.
The animation on the right is using Previous Frame Switch to add some motion blur, while the animation on the left is not.

#### Viewport Show Flag

There is a show flag in the Editor viewport under **Show** > **Visualize** > **Previous Frame's Reprojection** that you can use with the **Previous Frame Switch** to diagnose and correct discrepancies in the directional vectors of the current and previous frame.

![Previous Frame Reprojection Show Flag](https://dev.epicgames.com/community/api/documentation/image/1a84123a-2e26-4710-b075-ef5f897520d1)

When enabled, this visualizer compares the current frame color with the previous, and returns the difference between the two frames. When the difference is zero, the Material appears gray in the viewport (pictured left). When the directional vectors do not match, the Material displays a colored overlay (pictured right).

![Previous Frame Reprojection example](https://dev.epicgames.com/community/api/documentation/image/8862703d-ef13-4988-b29c-c64b5eb0f4d0)

## QualitySwitch

The **QualitySwitch** expression allows for the use of different expression networks based on the engine is switched between quality levels, such as using lower quality on lower-end devices.

| Inputs | Description |
| --- | --- |
| Default | This input is used for networks designed for default visual quality. |
| Low | This input is used for networks designed for lower visual quality. |
| High | This input is used for networks designed for higher visual quality. |

```json
{
  "type": "include",
  "excerpt_id": 694,
  "excerpt_assignment_id": 1524,
  "blocks": [
    {
      "type": "header",
      "content": "RotateAboutAxis",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <strong>RotateAboutAxis</strong> expression rotates a three-channel vector input given the rotation axis, a point on the axis, and the angle to rotate. This node outputs the Delta to the rotated position, not the fully rotated position itself. This makes it a useful and easy way to input the result into the World Position Offset input for simple rotations.",
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
              "content": "Inputs",
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
              "content": "<strong>NormalizedRotationAxis</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Takes in a normalized (0-1) vector which represents the axis about which the object will rotate.",
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
              "content": "<strong>RotationAngle</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The angle of rotation. A value of 1 equals a full 360-degree rotation.",
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
              "content": "<strong>PivotPoint</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Takes in the three-channel vector representing the pivot point about which the object will rotate.",
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
              "content": "<strong>Position</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Takes in the three-channel vector representing the position of the object.",
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
      "image_id": 24514666,
      "caption": "",
      "alt_text": "Rotate About Axis",
      "image": {
        "id": 24514666,
        "file_name": "rotate-about-axis.png",
        "file_size": 184497,
        "content_type": "image/png",
        "created_at": "2025-04-16T22:02:26.346+00:00",
        "height": 514,
        "width": 1116,
        "storage_key": "bbee1724-00c1-404e-82df-a7563aeb799d",
        "context": "documentation"
      },
      "storage_key": "bbee1724-00c1-404e-82df-a7563aeb799d",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "In the above example, the preview plane would appear to spin on its vertical axis.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "Rox",
  "settings": {
    "is_hidden": false
  }
}
```

## SphereMask

The **SphereMask** expression outputs a mask value based on a distance calculation. If one input is the position of a point and the other input is the center of a sphere with some radius, the mask value is 0 outside and 1 inside with some transition area. This works on one, two, three, and four component vectors

| Item | Description |
| --- | --- |
| Properties |   |
| **Attenuation Radius** | Specifies the radius to use for the distance calculation. |
| **Hardness Percent** | Specifies the transition area size. This works like the Photoshop brush hardness value. 0 means the transition is hard, 100 means the transition area is maximal(soft). |
| Inputs |   |
| **A** | Takes in the value representing the position of the point to check. |
| **B** | Takes in the value representing the center of the sphere. |

```json
{
  "type": "sequence_slider",
  "caption": "The node outputs a value of 1 until the camera passes beyond a certain distance, after which it outputs 0.",
  "images": [
    {
      "image_id": 25783831,
      "storage_key": "703180b0-042d-4bf8-b307-b927d73664c9",
      "context": "documentation",
      "image": {
        "id": 25783831,
        "file_name": "sphere-mask-01.png",
        "file_size": 173757,
        "content_type": "image/png",
        "created_at": "2025-07-07T20:35:59.845+00:00",
        "height": 418,
        "width": 853,
        "storage_key": "703180b0-042d-4bf8-b307-b927d73664c9",
        "context": "documentation"
      }
    },
    {
      "image_id": 25783832,
      "storage_key": "d1e88915-b17e-412f-a537-dcbc65486e3d",
      "context": "documentation",
      "image": {
        "id": 25783832,
        "file_name": "sphere-mask-02.png",
        "file_size": 157263,
        "content_type": "image/png",
        "created_at": "2025-07-07T20:36:00.080+00:00",
        "height": 418,
        "width": 853,
        "storage_key": "d1e88915-b17e-412f-a537-dcbc65486e3d",
        "context": "documentation"
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

## Thin Translucent

The **Thin Translucent Material Output** expression accurately represents physically based transparent materials in a single pass. This enables you to create *true* tinted or colored transparent materials that accurately respond to lighting and shading.

![Thin Translucent Graph](https://dev.epicgames.com/community/api/documentation/image/031445bd-f71a-48bc-8ee2-04ebcea9f0f7)

_Click image for full size._

When creating a tinted glass material, a white specular highlight and tinted background are needed. These are rendered in a single pass with a physically based shader that accounts for light bounces from the air into the glass and the glass into the air.

```json
{
  "type": "comparison_slider",
  "image_left_id": 25783829,
  "caption_left": "Standard Translucent Shading Model",
  "image_right_id": 25783830,
  "caption_right": "Thin Translucent Shading Model",
  "image_left": {
    "id": 25783829,
    "file_name": "Transparency.png",
    "file_size": 1006413,
    "content_type": "image/png",
    "created_at": "2025-07-07T20:35:59.461+00:00",
    "height": 575,
    "width": 1000,
    "storage_key": "8be61cb6-8b29-47c1-8f6c-a3c514b12cef",
    "context": "documentation"
  },
  "image_right": {
    "id": 25783830,
    "file_name": "ThinTransparency.png",
    "file_size": 1019242,
    "content_type": "image/png",
    "created_at": "2025-07-07T20:35:59.620+00:00",
    "height": 575,
    "width": 1000,
    "storage_key": "0992eb91-a065-49d0-afef-e9c7fc410023",
    "context": "documentation"
  },
  "image_left_storage_key": "8be61cb6-8b29-47c1-8f6c-a3c514b12cef",
  "image_right_storage_key": "0992eb91-a065-49d0-afef-e9c7fc410023",
  "context": "documentation",
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
      "content": "Enable Thin Translucent material output by setting the following in the Material Details panel:",
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
            "content": "<strong>Blend Mode:</strong> Translucent",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "<strong>Shading Model:</strong> Thin Translucent",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "<strong>Lighting Mode:</strong> Surface ForwardShading",
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
  "settings": {
    "is_hidden": false
  }
}
```

## Vector Noise

```json
{
  "type": "include",
  "excerpt_id": 695,
  "excerpt_assignment_id": 1525,
  "blocks": [
    {
      "type": "image",
      "image_id": 24514667,
      "caption": "",
      "alt_text": "",
      "image": {
        "id": 24514667,
        "file_name": "Vector_Noise_Example.png",
        "file_size": 521749,
        "content_type": "image/png",
        "created_at": "2025-04-16T22:02:26.892+00:00",
        "height": 356,
        "width": 1372,
        "storage_key": "faf9d63f-cd92-4fa5-ac47-6f5d60120dd2",
        "context": "documentation"
      },
      "storage_key": "faf9d63f-cd92-4fa5-ac47-6f5d60120dd2",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The Vector Noise Material expression adds several more 3D or 4D vector noise results to use in your Materials. Due to the run-time expense of these functions, it is recommended that once a look is developed with them, all or part of the computation be baked into a Texture using the Render Targets feature.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "These Material graph Expressions allow procedural looks to be developed in the engine on final assets, providing an alternative to creating procedurally generated Textures with an external tool. Inside the Vector Noise Material Expression, you will find the following Vector Noise types.",
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
              "content": "Image",
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
              "type": "image",
              "image_id": 24514668,
              "caption": "",
              "alt_text": "Cellnoise",
              "image": {
                "id": 24514668,
                "file_name": "Cellnoise.png",
                "file_size": 448198,
                "content_type": "image/png",
                "created_at": "2025-04-16T22:02:27.130+00:00",
                "height": 839,
                "width": 832,
                "storage_key": "6b4711eb-41cd-421c-8be7-3eba44813edb",
                "context": "documentation"
              },
              "storage_key": "6b4711eb-41cd-421c-8be7-3eba44813edb",
              "context": "documentation",
              "width": 128,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Cellnoise</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Returns a random color for each cell in a 3D grid (i.e. from the mathematical floor operation applied to the node input). The results are always consistent for a given position, so can provide a reliable way to add randomness to a Material. This Vector Noise function is extremely cheap to compute, so it is not necessary to bake it into a Texture for performance.",
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
              "image_id": 24514669,
              "caption": "",
              "alt_text": "Perlin 3D noise",
              "image": {
                "id": 24514669,
                "file_name": "VectorNoise.png",
                "file_size": 863118,
                "content_type": "image/png",
                "created_at": "2025-04-16T22:02:27.368+00:00",
                "height": 839,
                "width": 832,
                "storage_key": "c440bc87-d793-4dd8-b059-d148f9dd22a9",
                "context": "documentation"
              },
              "storage_key": "c440bc87-d793-4dd8-b059-d148f9dd22a9",
              "context": "documentation",
              "width": 128,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Perlin 3D Noise</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Returns a random color for each cell in a 3D grid (i.e. from the mathematical floor operation applied to the node input). The results are always consistent for a given position, so can provide a reliable way to add randomness to a Material. This Vector Noise function is extremely cheap to compute, so it is not necessary to bake it into a Texture for performance.",
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
              "image_id": 24514670,
              "caption": "",
              "alt_text": "Perlin Gradient",
              "image": {
                "id": 24514670,
                "file_name": "GradientNoise.png",
                "file_size": 1009060,
                "content_type": "image/png",
                "created_at": "2025-04-16T22:02:27.612+00:00",
                "height": 839,
                "width": 832,
                "storage_key": "8a6f6175-6e59-4b60-9577-4c9d9fcdcdfb",
                "context": "documentation"
              },
              "storage_key": "8a6f6175-6e59-4b60-9577-4c9d9fcdcdfb",
              "context": "documentation",
              "width": 128,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Perlin Gradient</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Computes the analytical 3D gradient of a scalar Perlin Simplex Noise. The output is four channels, where the first three (RGB) are the gradient, and the fourth (A) is the scalar noise. This noise type is useful for bumps on a surface or for flow maps.",
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
              "image_id": 24514671,
              "caption": "",
              "alt_text": "Perlin Curl",
              "image": {
                "id": 24514671,
                "file_name": "CurlNoise.png",
                "file_size": 1044598,
                "content_type": "image/png",
                "created_at": "2025-04-16T22:02:27.992+00:00",
                "height": 839,
                "width": 832,
                "storage_key": "7ffc20b6-b50d-4d83-9a50-c1e87d6b356b",
                "context": "documentation"
              },
              "storage_key": "7ffc20b6-b50d-4d83-9a50-c1e87d6b356b",
              "context": "documentation",
              "width": 128,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Perlin Curl</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Computes the analytical 3D curl of a vector Perlin Simplex Noise (aka Curl Noise). The output is a 3D signed curl vector and is useful for fluid or particle flow.",
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
              "image_id": 24514672,
              "caption": "",
              "alt_text": "Voronoi Noise",
              "image": {
                "id": 24514672,
                "file_name": "VoronoiNoise.png",
                "file_size": 629879,
                "content_type": "image/png",
                "created_at": "2025-04-16T22:02:28.252+00:00",
                "height": 839,
                "width": 832,
                "storage_key": "ae0c1ff3-1ccf-497f-8b94-64a520d6f045",
                "context": "documentation"
              },
              "storage_key": "ae0c1ff3-1ccf-497f-8b94-64a520d6f045",
              "context": "documentation",
              "width": 128,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "<strong>Voronoi</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Computes the same Voronoi noise as the scalar Noise material node. The scalar Voronoi noise scatters seed points in 3D space and returns the distance to the closest one. The Vector Noise version returns the location of the closest seed point in RGB, and the distance to it in A. Especially coupled with Cellnoise, this can allow some randomized behavior per Voronoi cell.",
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
      "content": "Below is a simple stone bed Material using the distance component of the Voronoi Vector Noise to modulate some surface bumps and blend moss into the cracks. The seed position together with Vector Noise &gt; Cellnoise is used to change the color and bump height per rock.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24514673,
      "caption": "",
      "alt_text": "Stone blend example",
      "image": {
        "id": 24514673,
        "file_name": "Stone_Example.png",
        "file_size": 1297227,
        "content_type": "image/png",
        "created_at": "2025-04-16T22:02:28.519+00:00",
        "height": 485,
        "width": 1000,
        "storage_key": "8c5f4711-87a7-41fc-a2bc-3a61581b6fd3",
        "context": "documentation"
      },
      "storage_key": "8c5f4711-87a7-41fc-a2bc-3a61581b6fd3",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The derivative-based operations <strong>Perlin Curl</strong> and <strong>Perlin Gradient</strong> can be added together in octaves, just as regular Perlin noise can. For derivatives of more complex expressions, it is necessary to compute the gradient of the result of the expression. To help with this, place the expression to compute into a Material Function and use it with the following helper nodes.",
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
              "type": "paragraph",
              "content": "<strong>Prepare3DDeriv</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Uses positions offset in a tetrahedral pattern to compute 3D derivatives. Evaluate the same 3D function at each offset position produced by this function, then feed the resulting values into Compute3DDeriv.",
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
              "content": "<strong>Compute3DDeriv</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Uses positions offset in a tetrahedral pattern to compute 3D derivatives. Use with Prepare3DDeriv.",
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
              "content": "<strong>GradFrom3DDeriv</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Computes 3D gradient vector from result of Prepare3DDeriv/Compute3DDeriv.",
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
              "content": "<strong>CurlFrom3DDeriv</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Computes curl of a 3D vector field from result of Prepare3DDeriv/Compute3DDeriv.",
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
          "content": "These helper Material Functions use four evaluations of the base expression spaced in a tetrahedral pattern to approximate these derivative-based operations.",
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
      "type": "paragraph",
      "content": "Below you will find descriptions of the various noise functions you will find in the Vector Noise Material Expression.",
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
              "content": "<strong>Function</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_list",
              "style": "unordered",
              "items": [
                [
                  {
                    "type": "paragraph",
                    "content": "<strong>Cellnoise</strong>: Random color for each integer grid cell in 3D space. About 10 instructions.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<strong>Perlin 3D Noise</strong>: Computational Perlin noise with 3D output, each channel output ranges from -1 to 1. About 83 instructions if only the red channel is used, 125 instructions if all three channels are used.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<strong>Perlin Gradient</strong>: Computes the gradient of a Perlin noise function. RGB output contains the gradient vector, A is the scalar noise. About 106 instructions.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<strong>Perlin Curl</strong>: Computes a 3D curl noise. The output is the mathematical curl of Perlin 3D Noise. About 162 instructions.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<strong>Voronoi</strong>: The same algorithm and instruction counts as the Voronoi function in the <em>Noise</em> expression, but RGB is the location of the closest seed point in each Voronoi cell, and A is the distance to that seed point.",
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
              "content": "<strong>Quality</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "A look/performance setting. Lower values are faster but may look worse, higher values are slower but may look better.",
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
              "content": "<strong>Tiling</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "For noise functions that support it this allows noise to tile. This is more expensive, but useful when baking noise into a seamless wrapping texture.",
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
              "content": "<strong>Tile Size</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "When tiling, how often should the noise repeat. For Perlin noise variants, the Tile Size must be a multiple of three.",
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
              "content": "",
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
              "content": "<strong>Position</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Allows the texture size to be adjusted via a 3D vector.",
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
      "type": "enhanced_list",
      "style": "unordered",
      "items": [
        [
          {
            "type": "paragraph",
            "content": "<strong>Cell Noise</strong> Material Example:",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24514674,
            "caption": "Click image for full size.",
            "alt_text": "Cell Noise",
            "image": {
              "id": 24514674,
              "file_name": "cell-noise.png",
              "file_size": 200792,
              "content_type": "image/png",
              "created_at": "2025-04-16T22:02:28.718+00:00",
              "height": 352,
              "width": 979,
              "storage_key": "1d03940e-2b89-42a3-85b6-7b96de633cb7",
              "context": "documentation"
            },
            "storage_key": "1d03940e-2b89-42a3-85b6-7b96de633cb7",
            "context": "documentation",
            "width": 800,
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "<strong>Perlin Gradient</strong>  Material Example:",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24514675,
            "caption": "Click image for full size.",
            "alt_text": "Perlin Gradient",
            "image": {
              "id": 24514675,
              "file_name": "perlin-gradient.png",
              "file_size": 363643,
              "content_type": "image/png",
              "created_at": "2025-04-16T22:02:28.910+00:00",
              "height": 519,
              "width": 1375,
              "storage_key": "6018011f-b419-49db-8e37-dae36dea81a8",
              "context": "documentation"
            },
            "storage_key": "6018011f-b419-49db-8e37-dae36dea81a8",
            "context": "documentation",
            "width": 800,
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "<strong>Voronoi</strong>  Material Example:",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24514676,
            "caption": "Click image for full size.",
            "alt_text": "Voronoi Noise",
            "image": {
              "id": 24514676,
              "file_name": "voronoi-material.png",
              "file_size": 531017,
              "content_type": "image/png",
              "created_at": "2025-04-16T22:02:29.092+00:00",
              "height": 571,
              "width": 1906,
              "storage_key": "8c46f32b-2269-4b25-ac78-1de7e8e81b6c",
              "context": "documentation"
            },
            "storage_key": "8c46f32b-2269-4b25-ac78-1de7e8e81b6c",
            "context": "documentation",
            "width": 800,
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
  "excerpt_hash_id": "P0J",
  "settings": {
    "is_hidden": false
  }
}
```
