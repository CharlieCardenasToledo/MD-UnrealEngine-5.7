# Material Blend Modes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/material-blend-modes-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "include",
  "excerpt_id": 697,
  "excerpt_assignment_id": 410,
  "blocks": [
    {
      "type": "paragraph",
      "content": "Blend Modes describe how the output of the current Material will blend over what is already being drawn in the background. Put more technically, it allows you to control how the engine will combine this Material (<strong>Source color</strong>) with what is already in the frame buffer (<strong>Destination color</strong>) when this Material is rendered in front of other pixels.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Blend Mode options are found in the Details panel with the rest of the base <a data-document-id=\"3226265\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-properties\">Material Properties</a>:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24523805,
      "caption": "",
      "alt_text": "Blend Modes dropdown menu",
      "image": {
        "id": 24523805,
        "file_name": "blend-mode-dropdown.png",
        "file_size": 24933,
        "content_type": "image/png",
        "created_at": "2025-04-21T22:46:09.496+00:00",
        "height": 350,
        "width": 556,
        "storage_key": "80c04109-dfc7-492d-a02b-83cf587b1dd9",
        "context": "documentation"
      },
      "storage_key": "80c04109-dfc7-492d-a02b-83cf587b1dd9",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "This document uses a sphere placed between the camera and a wall to demonstrate the various Blend Modes.  By changing the Blend Mode on the sphere Material you can see how the object blends with the pixels behind it.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24523806,
      "caption": "",
      "alt_text": "Blend Modes demo setup",
      "image": {
        "id": 24523806,
        "file_name": "camera-setup-sm.png",
        "file_size": 376960,
        "content_type": "image/png",
        "created_at": "2025-04-21T22:46:09.702+00:00",
        "height": 370,
        "width": 800,
        "storage_key": "464a22e9-9dab-4d3f-8107-e68d7c7b7b06",
        "context": "documentation"
      },
      "storage_key": "464a22e9-9dab-4d3f-8107-e68d7c7b7b06",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Opaque",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The Opaque Blend Mode is the most straightforward, and probably the one you will use most often. It defines a surface through which light neither passes nor penetrates. This is perfect for most plastics, metals, stone, and the larger percentage of other surface types.  From the perspective of the camera, the golden sphere completely occludes the wall behind it.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24523807,
      "caption": "",
      "alt_text": "Opaque Blend Mode",
      "image": {
        "id": 24523807,
        "file_name": "opaque-example.png",
        "file_size": 668217,
        "content_type": "image/png",
        "created_at": "2025-04-21T22:46:09.877+00:00",
        "height": 445,
        "width": 800,
        "storage_key": "5c85b439-6e1e-4d1e-8558-86c5216307e3",
        "context": "documentation"
      },
      "storage_key": "5c85b439-6e1e-4d1e-8558-86c5216307e3",
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
              "content": " ",
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
              "type": "image",
              "image_id": 24523808,
              "caption": "",
              "alt_text": "",
              "image": {
                "id": 24523808,
                "file_name": "CameraObjectSetup.png",
                "file_size": 280792,
                "content_type": "image/png",
                "created_at": "2025-04-21T22:46:10.077+00:00",
                "height": 394,
                "width": 1053,
                "storage_key": "4085402d-b79d-41a6-b646-2dd10bda729a",
                "context": "documentation"
              },
              "storage_key": "4085402d-b79d-41a6-b646-2dd10bda729a",
              "context": "documentation",
              "width": 500,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 24523809,
              "caption": "",
              "alt_text": "",
              "image": {
                "id": 24523809,
                "file_name": "CamerasView.png",
                "file_size": 113059,
                "content_type": "image/png",
                "created_at": "2025-04-21T22:46:10.326+00:00",
                "height": 284,
                "width": 508,
                "storage_key": "1d3d6309-2e9c-43d1-a5bd-e2b6b8bbfc89",
                "context": "documentation"
              },
              "storage_key": "1d3d6309-2e9c-43d1-a5bd-e2b6b8bbfc89",
              "context": "documentation",
              "width": 189,
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
              "content": "Scene Setup",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Camera's View",
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
      "type": "header",
      "content": "Masked",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The Masked Blend Mode is used when you need to selectively control visibility in a binary (on/off) fashion. For example, consider a Material that simulates a chain link fence or grate. You will have some areas that look solid while others are invisible. Such Materials are perfect for the Masked Blend Mode.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "A Masked Material graph is shown below, with a black and white striped texture plugged into the <strong>Opacity Mask</strong> input. White parts of the mask are rendered, while black parts are invisible. There are no intermediate levels of opacity when using a Masked Material.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24523810,
      "caption": "",
      "alt_text": "Masked Material Graph",
      "image": {
        "id": 24523810,
        "file_name": "masked-graph.png",
        "file_size": 288360,
        "content_type": "image/png",
        "created_at": "2025-04-21T22:46:10.470+00:00",
        "height": 414,
        "width": 916,
        "storage_key": "7b69179a-3e32-4f01-9849-2563a1c1fd77",
        "context": "documentation"
      },
      "storage_key": "7b69179a-3e32-4f01-9849-2563a1c1fd77",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Here is that Material from the camera's perspective:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24523811,
      "caption": "",
      "alt_text": "Masked Material",
      "image": {
        "id": 24523811,
        "file_name": "masked-example.png",
        "file_size": 508493,
        "content_type": "image/png",
        "created_at": "2025-04-21T22:46:10.675+00:00",
        "height": 444,
        "width": 800,
        "storage_key": "44a1ee3b-ed0a-48d8-b997-63f6477ac6cd",
        "context": "documentation"
      },
      "storage_key": "44a1ee3b-ed0a-48d8-b997-63f6477ac6cd",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "It is important to keep in mind the difference between <strong>transparent</strong> and <strong>not rendered</strong>. A transparent surface, such as glass, still interacts with light in the form of reflections (specularity). Pixels that are culled in Masked mode simply do not draw; you will not see any reflections in those areas. If you want to retain reflections or specular aspects, you would do well to use the Translucent Blend Mode, or consider making a <a data-document-id=\"3226511\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/layering-materials-in-unreal-engine\">Layered Material</a>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Further, since these features don't render in the masked area, they aren't calculated at all, leading to performance savings on the GPU.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Opacity Clip Mask",
      "level": 3,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "When using Masked Blend Mode, you need to pay special attention to the <strong>Opacity Mask Clip Value</strong> property. This property holds a 0-1 scalar value which controls what value of the opacity mask texture will be used as a cutoff point, beyond which all <strong>darker</strong> pixels will not render.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "sequence_slider",
      "caption": "Opacity Mask Clip Value (Drag the slider to preview.)",
      "images": [
        {
          "image_id": 24523823,
          "storage_key": "846604ab-7682-472f-b009-b42c1a7abce0",
          "context": "documentation",
          "image": {
            "id": 24523823,
            "file_name": "opacity-clip-mask-005.png",
            "file_size": 172907,
            "content_type": "image/png",
            "created_at": "2025-04-21T22:46:13.060+00:00",
            "height": 522,
            "width": 805,
            "storage_key": "846604ab-7682-472f-b009-b42c1a7abce0",
            "context": "documentation"
          }
        },
        {
          "image_id": 24523824,
          "storage_key": "3d8ffc6c-bfc3-415b-95e1-9445b0d744f9",
          "context": "documentation",
          "image": {
            "id": 24523824,
            "file_name": "opacity-clip-mask-01.png",
            "file_size": 173358,
            "content_type": "image/png",
            "created_at": "2025-04-21T22:46:13.254+00:00",
            "height": 522,
            "width": 805,
            "storage_key": "3d8ffc6c-bfc3-415b-95e1-9445b0d744f9",
            "context": "documentation"
          }
        },
        {
          "image_id": 24523825,
          "storage_key": "a8aada1e-5546-4eca-8136-2bd6aac1c4da",
          "context": "documentation",
          "image": {
            "id": 24523825,
            "file_name": "opacity-clip-mask-015.png",
            "file_size": 176878,
            "content_type": "image/png",
            "created_at": "2025-04-21T22:46:13.538+00:00",
            "height": 522,
            "width": 805,
            "storage_key": "a8aada1e-5546-4eca-8136-2bd6aac1c4da",
            "context": "documentation"
          }
        },
        {
          "image_id": 24523826,
          "storage_key": "7dd3acfe-394f-48fa-8fd6-059df22fdb74",
          "context": "documentation",
          "image": {
            "id": 24523826,
            "file_name": "opacity-clip-mask-02.png",
            "file_size": 174096,
            "content_type": "image/png",
            "created_at": "2025-04-21T22:46:13.791+00:00",
            "height": 522,
            "width": 805,
            "storage_key": "7dd3acfe-394f-48fa-8fd6-059df22fdb74",
            "context": "documentation"
          }
        },
        {
          "image_id": 24523827,
          "storage_key": "c57058f5-9dd0-431c-9959-920caea7fa5b",
          "context": "documentation",
          "image": {
            "id": 24523827,
            "file_name": "opacity-clip-mask-025.png",
            "file_size": 179700,
            "content_type": "image/png",
            "created_at": "2025-04-21T22:46:13.946+00:00",
            "height": 522,
            "width": 805,
            "storage_key": "c57058f5-9dd0-431c-9959-920caea7fa5b",
            "context": "documentation"
          }
        },
        {
          "image_id": 24523828,
          "storage_key": "5ba7513c-dcf1-486b-af61-64c6d5817795",
          "context": "documentation",
          "image": {
            "id": 24523828,
            "file_name": "opacity-clip-mask-03.png",
            "file_size": 175883,
            "content_type": "image/png",
            "created_at": "2025-04-21T22:46:14.254+00:00",
            "height": 522,
            "width": 805,
            "storage_key": "5ba7513c-dcf1-486b-af61-64c6d5817795",
            "context": "documentation"
          }
        },
        {
          "image_id": 24523829,
          "storage_key": "2221784e-eb85-4cd1-aebc-6ae4608a2756",
          "context": "documentation",
          "image": {
            "id": 24523829,
            "file_name": "opacity-clip-mask-04.png",
            "file_size": 180610,
            "content_type": "image/png",
            "created_at": "2025-04-21T22:46:14.393+00:00",
            "height": 522,
            "width": 805,
            "storage_key": "2221784e-eb85-4cd1-aebc-6ae4608a2756",
            "context": "documentation"
          }
        },
        {
          "image_id": 24523830,
          "storage_key": "f5e53311-4ab1-4e5f-b7fa-cdef8e1af037",
          "context": "documentation",
          "image": {
            "id": 24523830,
            "file_name": "opacity-clip-mask-05.png",
            "file_size": 178593,
            "content_type": "image/png",
            "created_at": "2025-04-21T22:46:14.753+00:00",
            "height": 522,
            "width": 805,
            "storage_key": "f5e53311-4ab1-4e5f-b7fa-cdef8e1af037",
            "context": "documentation"
          }
        },
        {
          "image_id": 24523831,
          "storage_key": "4fa85369-54a4-4cdf-a095-ea7289411de9",
          "context": "documentation",
          "image": {
            "id": 24523831,
            "file_name": "opacity-clip-mask-06.png",
            "file_size": 178301,
            "content_type": "image/png",
            "created_at": "2025-04-21T22:46:14.947+00:00",
            "height": 522,
            "width": 805,
            "storage_key": "4fa85369-54a4-4cdf-a095-ea7289411de9",
            "context": "documentation"
          }
        }
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
          "content": "In the example above, the Material has its <strong>Two Sided</strong> property set to <strong>True</strong> (checked), which is why you can see the inside of the box.",
          "settings": {
            "is_hidden": false
          }
        },
        {
          "type": "paragraph",
          "content": "Also, despite the interactive example shown here, the <strong>Opacity Mask Clip Value</strong> property is not designed to be changed at runtime.",
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
      "content": "Translucent",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The Translucent Blend Mode is used for objects that require some form of transparency.  This differs from the Masked Blend Mode in that it allows varying levels of translucency.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24523812,
      "caption": "",
      "alt_text": "Translucent Material Graph",
      "image": {
        "id": 24523812,
        "file_name": "translucent-graph.png",
        "file_size": 266110,
        "content_type": "image/png",
        "created_at": "2025-04-21T22:46:10.934+00:00",
        "height": 398,
        "width": 755,
        "storage_key": "d1c99238-fe13-4b65-a256-f49db8ab4da0",
        "context": "documentation"
      },
      "storage_key": "d1c99238-fe13-4b65-a256-f49db8ab4da0",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "This Blend Mode works by taking in an <strong>Opacity</strong> value or texture and applying it to the surface such that black areas are completely transparent, white areas are completely opaque, and the varying shades of gradation between result in corresponding transparency levels.  In the example, a black to white gradient is plugged into the Opacity input, resulting in a sphere that is fully transparent at the top of the mesh and gradually reaches full opacity at the bottom.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24523813,
      "caption": "",
      "alt_text": "Translucent gradient on a sphere",
      "image": {
        "id": 24523813,
        "file_name": "translucent-example.png",
        "file_size": 668120,
        "content_type": "image/png",
        "created_at": "2025-04-21T22:46:11.161+00:00",
        "height": 444,
        "width": 800,
        "storage_key": "ca50ec87-48d6-4187-916f-0bd30d040c24",
        "context": "documentation"
      },
      "storage_key": "ca50ec87-48d6-4187-916f-0bd30d040c24",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "An important consideration when using Translucent Materials is that they do not currently support specularity. This means that you will see no reflections along the surface. However, such reflections can be faked using a Cubemap in a node network similar to this. The Cubemap texture is simply added on top of the Base Color.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24523814,
      "caption": "",
      "alt_text": "Fake specularity on sphere",
      "image": {
        "id": 24523814,
        "file_name": "translucent-specularity.png",
        "file_size": 332666,
        "content_type": "image/png",
        "created_at": "2025-04-21T22:46:11.362+00:00",
        "height": 416,
        "width": 1276,
        "storage_key": "8c75d900-c0c0-4623-a953-1fc543d2f0c4",
        "context": "documentation"
      },
      "storage_key": "8c75d900-c0c0-4623-a953-1fc543d2f0c4",
      "context": "documentation",
      "width": 800,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Additive",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The Additive Blend Mode simply takes the pixels of the Material and adds them to the pixels of the background. This is very similar to the <em>Linear Dodge (Add)</em> Blend Mode in Photoshop. This means that there is no darkening; since all pixel values are added together, blacks will just render as transparent. This Blend Mode is useful for various special effects such as fire, steam, or holograms.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24523815,
      "caption": "",
      "alt_text": "Additive Material Graph",
      "image": {
        "id": 24523815,
        "file_name": "additive-graph.png",
        "file_size": 255286,
        "content_type": "image/png",
        "created_at": "2025-04-21T22:46:11.581+00:00",
        "height": 397,
        "width": 800,
        "storage_key": "2bfbb274-4b31-498e-9b19-4933bce0e1a3",
        "context": "documentation"
      },
      "storage_key": "2bfbb274-4b31-498e-9b19-4933bce0e1a3",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "As with the Translucent Blend Mode, this Blend Mode does not respect specularity (i.e. reflections). The additive nature of the blending probably means you will not use it anyway, but it is possible to simulate a reflection-like effect using the Cubemap method shown above in the Translucent section.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "In the image below a second sphere was added to the scene. Note that where the two spheres overlap, the pixels are added together and therefore brightened.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24523816,
      "caption": "",
      "alt_text": "Additive Material Example",
      "image": {
        "id": 24523816,
        "file_name": "additive-example.png",
        "file_size": 589809,
        "content_type": "image/png",
        "created_at": "2025-04-21T22:46:11.766+00:00",
        "height": 444,
        "width": 800,
        "storage_key": "9a0a4454-ab5b-4acc-8a7b-4044bb5f4aea",
        "context": "documentation"
      },
      "storage_key": "9a0a4454-ab5b-4acc-8a7b-4044bb5f4aea",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "One drawback of Additive Materials is that they are often difficult to see against light colored backgrounds.  A side view of the spheres demonstrates this.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24523817,
      "caption": "",
      "alt_text": "Additive Material side view",
      "image": {
        "id": 24523817,
        "file_name": "additive-side-view.png",
        "file_size": 552275,
        "content_type": "image/png",
        "created_at": "2025-04-21T22:46:11.988+00:00",
        "height": 507,
        "width": 800,
        "storage_key": "d04441ac-8ceb-4f58-ae13-803e224394b8",
        "context": "documentation"
      },
      "storage_key": "d04441ac-8ceb-4f58-ae13-803e224394b8",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "A solution is to use the <a data-document-id=\"3226262\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/material-blend-modes-in-unreal-engine\">AlphaComposite</a> Blend Mode instead, which can improve saturation and visibility in bright scenes.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Modulate",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The Modulate Blend Mode multiplies the value of the Material against the pixels of the background. The behavior is very similar to the Multiply Blend Mode in Photoshop, and produces a darkening effect.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24523818,
      "caption": "",
      "alt_text": "Modulate Material Graph",
      "image": {
        "id": 24523818,
        "file_name": "modulate-graph.png",
        "file_size": 18874,
        "content_type": "image/png",
        "created_at": "2025-04-21T22:46:12.146+00:00",
        "height": 251,
        "width": 335,
        "storage_key": "0a787355-a006-455f-a2ac-4c79b6f3747c",
        "context": "documentation"
      },
      "storage_key": "0a787355-a006-455f-a2ac-4c79b6f3747c",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "In the graph above, the Material Shading Model is set to <strong>Unlit</strong> and the Blend Mode to <strong>Modulate</strong>.  A Constant3 Vector is plugged into the Emissive input to define the surface color.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24523819,
      "caption": "",
      "alt_text": "Modulate Material Example",
      "image": {
        "id": 24523819,
        "file_name": "modulated-example.png",
        "file_size": 538521,
        "content_type": "image/png",
        "created_at": "2025-04-21T22:46:12.255+00:00",
        "height": 438,
        "width": 800,
        "storage_key": "ed8f0e03-3224-4a98-88cd-00eb417716ee",
        "context": "documentation"
      },
      "storage_key": "ed8f0e03-3224-4a98-88cd-00eb417716ee",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Notice again that with multiple spheres, the pixels that overlap are multiplied together and become darker.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "callout",
      "callout_type": "warning",
      "blocks": [
        {
          "type": "paragraph",
          "content": "The Modulate blend mode is best suited for certain particle effects, but care must be taken as it does not support lighting or Separate Translucency.",
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
      "content": "Alpha Composite",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <strong>AlphaComposite</strong> blend mode enables you to control how parts of the material are blended. With some material setup and logic, you can control what parts are blended additively and what parts are blended translucently using the opacity input of the material. AlphaComposite works by multiplying the underlying scene color by the inverse of the material’s opacity so that when the material is added to the scene color, areas of high opacity appear more saturated and full than those that are more opaque.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24523820,
      "caption": "Example of a material set up to use AlphaComposite with a partical effect.",
      "alt_text": "Alpha Composite graph",
      "image": {
        "id": 24523820,
        "file_name": "alpha-composite-graph.png",
        "file_size": 190573,
        "content_type": "image/png",
        "created_at": "2025-04-21T22:46:12.440+00:00",
        "height": 848,
        "width": 1340,
        "storage_key": "8bacb524-4d1a-4348-8463-dc5a6fdc41f6",
        "context": "documentation"
      },
      "storage_key": "8bacb524-4d1a-4348-8463-dc5a6fdc41f6",
      "context": "documentation",
      "width": 700,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Alpha Holdout",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <strong>AlphaHoldout</strong> blend mode lets you \"hold out\" the alpha of a Material, punching a hole through the objects directly behind it in view space.  The following image shows the camera and scene layout for an AlphaHoldout implementation.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24523821,
      "caption": "",
      "alt_text": "",
      "image": {
        "id": 24523821,
        "file_name": "alpha-holdout-scene.png",
        "file_size": 830292,
        "content_type": "image/png",
        "created_at": "2025-04-21T22:46:12.609+00:00",
        "height": 792,
        "width": 1305,
        "storage_key": "cd4cfe14-b443-4080-a7a1-a9edc77f3298",
        "context": "documentation"
      },
      "storage_key": "cd4cfe14-b443-4080-a7a1-a9edc77f3298",
      "context": "documentation",
      "width": 800,
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
            "content": "The camera.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "A Static Mesh in the foreground acts as the \"hole-punching\" object.  The <strong>AlphaHoldout Material</strong> is applied to this mesh. This Material must use the <strong>Unlit</strong> Shading Model.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "A receiving surface (which you intend to punch a hole through) is placed behind the AlphaHoldout object; in this case, a brick wall. The Material on the receiving surface <strong>MUST</strong> use either the Translucent, Additive, Modulate, or AlphaComposite Blend Modes.  An AlphaHoldout Material cannot act upon an Opaque Material.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "The background of the scene, which will be visible through the hole.",
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
      "content": "From the camera's perspective, you will see a transparent hole through the receiving surface, making the objects behind it visible.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24523822,
      "caption": "",
      "alt_text": "AlphaHoldout Example",
      "image": {
        "id": 24523822,
        "file_name": "alpha-holdout-cameraview.png",
        "file_size": 577392,
        "content_type": "image/png",
        "created_at": "2025-04-21T22:46:12.844+00:00",
        "height": 428,
        "width": 800,
        "storage_key": "ae849d98-8bbe-4741-b762-8ea9eef5c73f",
        "context": "documentation"
      },
      "storage_key": "ae849d98-8bbe-4741-b762-8ea9eef5c73f",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Because the AlphaHoldOut material is on a separate Static Mesh Asset, you can easily move it around in-editor or animate it in game.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "video",
      "video_id": "1_vsfhylhm",
      "provider": "kaltura",
      "caption": "",
      "autoplay": false,
      "loop": false,
      "width": null,
      "video": {
        "height": 900,
        "width": 1600,
        "identifier": "1_vsfhylhm"
      },
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Blend Mode Formulas",
      "level": 2,
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
              "content": "Mode",
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
              "content": "<strong>Opaque</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Final color = Source color.  This means that the Material will draw on top of the background. This blend mode is compatible with lighting.",
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
              "content": "<strong>Masked</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Final color = Source color if OpacityMask &gt; OpacityMaskClipValue, otherwise the pixel is discarded.  This blend mode is compatible with lighting.",
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
              "content": "<strong>Translucent</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Final color = Source color * Opacity + Dest color * (1 - Opacity).  This blend mode is <strong>NOT</strong> compatible with dynamic lighting.",
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
              "content": "<strong>Additive</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Final color = Source color + Dest color.  This blend mode is <strong>NOT</strong> compatible with dynamic lighting.",
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
              "content": "<strong>Modulate</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Final color = Source color x Dest color.  This blend mode is <strong>NOT</strong> compatible with dynamic lighting, or fog, unless this is a decal material.",
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
              "content": "<strong>AlphaComposite (Premultiplied Alpha)</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Final Color = Source Color + Dest Color * (1 - Source Opacity).",
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
              "content": "<strong>AlphaHoldout</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Final Color = Dest Color * (1 - Source Opacity).  This blend mode is <strong>NOT</strong> compatible with dynamic lighting.",
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
  "excerpt_hash_id": "G0B",
  "settings": {
    "is_hidden": false
  }
}
```
