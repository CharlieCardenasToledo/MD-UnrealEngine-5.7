# Distance Field Soft Shadows

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/distance-field-soft-shadows-in-unreal-engine

> Application Version: 5.7

Shadowing from movable light sources is provided using object Distance Fields for each rigid mesh to compute efficient area shadowing from dynamic light sources.
In Unreal Engine, this is called **Distance Field Shadows** (DFS). To calculate shadowing, a ray is traced from the point being shaded through the scene's Signed Distance Fields (SDF) toward each light.
The closest distance to an occluding object is used to approximate a cone trace for about the same cost as the ray trace. It allows for high-quality area shadowing from spherical light source shapes.

## Scene Setup

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "This feature requires that <strong>Generate Mesh Distance Fields</strong> be enabled in your <strong>Project Settings</strong> in the <strong>Rendering</strong> section.\nSee the <a data-document-id=\"3225038\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine\">Mesh Distance Fields</a> page for more information.",
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

To enable Distance Field Shadowing, start by dragging a **Light** into the scene and set its Mobility to **Movable** and then from the Light **Details** panel, enable **Distance Field Shadows**.

![Enable Distance Field Shadowing](https://dev.epicgames.com/community/api/documentation/image/4d4ce914-4a94-48fe-bba2-f6a21aa29a59)

### Area Shadowing Settings

Each Light type can use Distance Fields shadows to create soft area shadows. These shadows simulate real-world shadows by retaining sharp contact shadows closer to the base and softening the farther the shadow stretches away.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26433914,
  "caption_left": "Traditional Shadow Map",
  "image_right_id": 26433915,
  "caption_right": "Distance Field Shadow",
  "image_left": {
    "id": 26433914,
    "file_name": "02-dfss-default-shadow-map.png",
    "file_size": 337735,
    "content_type": "image/png",
    "created_at": "2026-02-05T17:47:59.376+00:00",
    "height": 720,
    "width": 720,
    "storage_key": "da15b552-e136-451e-9e73-72964732c8d9",
    "context": "documentation"
  },
  "image_right": {
    "id": 26433915,
    "file_name": "03-dfss-df-shadow-map.png",
    "file_size": 332883,
    "content_type": "image/png",
    "created_at": "2026-02-05T17:47:59.557+00:00",
    "height": 720,
    "width": 720,
    "storage_key": "3988b58f-5a88-4f95-9b6e-99a7937881dc",
    "context": "documentation"
  },
  "image_left_storage_key": "da15b552-e136-451e-9e73-72964732c8d9",
  "image_right_storage_key": "3988b58f-5a88-4f95-9b6e-99a7937881dc",
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
      "content": "For additional information about Light source settings and additional examples, see the <a data-document-id=\"3225083\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-properties-in-unreal-engine\">Mesh Distance Fields Reference</a> page.",
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

### Point and Spot Light Source Radius

For Point and Spot Lights, the **Source Radius** is used to determine how large shadow penumbras are on a light. Area shadows are computed with sharp contacts that get softer over long distances.
On a Point and Spot Light, it is represented by a yellow sphere.

![Source Radius representation of the Point and Spot Light in the Viewport](https://dev.epicgames.com/community/api/documentation/image/82f4f081-5520-4360-87ce-b41d5c694f89)

_The Editor draws the source shape of the light with yellow lines._

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The Light's source radius sphere should not be intersecting the scene, or it will cause lighting artifacts.",
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
  "type": "comparison_slider",
  "image_left_id": 26433916,
  "caption_left": "Source Radius: 0",
  "image_right_id": 26433917,
  "caption_right": "Source Radius: 50",
  "image_left": {
    "id": 26433916,
    "file_name": "05-dfss-source-radius-0.png",
    "file_size": 951807,
    "content_type": "image/png",
    "created_at": "2026-02-05T17:47:59.743+00:00",
    "height": 848,
    "width": 1272,
    "storage_key": "27739733-95ad-4c93-b355-e6eddc06af23",
    "context": "documentation"
  },
  "image_right": {
    "id": 26433917,
    "file_name": "06-dfss-source-radius-50.png",
    "file_size": 929717,
    "content_type": "image/png",
    "created_at": "2026-02-05T17:47:59.988+00:00",
    "height": 848,
    "width": 1272,
    "storage_key": "4f8f7255-7703-4bf2-8232-583ccd9bf37d",
    "context": "documentation"
  },
  "image_left_storage_key": "27739733-95ad-4c93-b355-e6eddc06af23",
  "image_right_storage_key": "4f8f7255-7703-4bf2-8232-583ccd9bf37d",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

The Distance Field shadows are from a Point Light using a Source Radius to soften the shadows cast by the doorway, bench, and piano on the surrounding geometry.

🚩 Conversion Failed 🚩
External video block: xai0iBffUc: Youtube video fetching error

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For additional information about Point and Spot Light settings, see the <a data-document-id=\"3225083\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-properties-in-unreal-engine\">Mesh Distance Fields Reference</a> page.",
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

### Directional Light Source Angle

For Directional Lights, the **Light Source Angle** is used to determine how large shadow penumbras are on a light.
Distance Field Shadows have very few self-intersection problems and therefore avoid the leaking and over-biasing problems in the distance that traditional shadow mapping would have.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26433918,
  "caption_left": "Source Angle: 1",
  "image_right_id": 26433920,
  "caption_right": "Source Angle: 3",
  "image_left": {
    "id": 26433918,
    "file_name": "07-dfss-shadow-source-angle-1.png",
    "file_size": 1593414,
    "content_type": "image/png",
    "created_at": "2026-02-05T17:48:00.238+00:00",
    "height": 857,
    "width": 1194,
    "storage_key": "52436ac7-ef90-49cc-b19d-4edc6f61bcc3",
    "context": "documentation"
  },
  "image_right": {
    "id": 26433920,
    "file_name": "08-dfss-source-angle-3.png",
    "file_size": 1591923,
    "content_type": "image/png",
    "created_at": "2026-02-05T17:48:00.461+00:00",
    "height": 857,
    "width": 1194,
    "storage_key": "cba478aa-d05e-4b78-8188-8bf0198f1734",
    "context": "documentation"
  },
  "image_left_storage_key": "52436ac7-ef90-49cc-b19d-4edc6f61bcc3",
  "image_right_storage_key": "cba478aa-d05e-4b78-8188-8bf0198f1734",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

*Distance Field Shadows from a Directional Light with a Light Source Angle adjusted for softer shadowing.*

In most cases, Cascaded Shadow Maps (CSM) are used to provide dynamic shadowing of a Directional Light. These require rendering the meshes in
the scene into several cascade shadow maps (levels of detail for shadowing). The cost of shadowing increases at large shadow distances because of
how many meshes and triangles are being rendered into the shadow maps.

Distance Field Shadows work much more gracefully in the distance, doing shadowing work only for visible pixels. Cascaded Shadow Maps can be used to shadow an area near
the camera while RTDF shadows will shadow farther regions up to the **Distance Field Shadow Distance** that is set.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26433921,
  "caption_left": "Cascaded Shadow Maps Only",
  "image_right_id": 26433922,
  "caption_right": "Cascaded Shadow Maps & Distance Field Shadows",
  "image_left": {
    "id": 26433921,
    "file_name": "09-dfss-cascaded-shadow-maps.png",
    "file_size": 3060938,
    "content_type": "image/png",
    "created_at": "2026-02-05T17:48:00.721+00:00",
    "height": 1013,
    "width": 1854,
    "storage_key": "27f2c73d-7241-4c96-bfb5-d774cdcd908f",
    "context": "documentation"
  },
  "image_right": {
    "id": 26433922,
    "file_name": "10-dfss-cascaded-and-df-shadows.png",
    "file_size": 2859319,
    "content_type": "image/png",
    "created_at": "2026-02-05T17:48:01.208+00:00",
    "height": 1013,
    "width": 1854,
    "storage_key": "57fac7de-95a2-408d-b6ca-15794eeaa87e",
    "context": "documentation"
  },
  "image_left_storage_key": "27f2c73d-7241-4c96-bfb5-d774cdcd908f",
  "image_right_storage_key": "57fac7de-95a2-408d-b6ca-15794eeaa87e",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

When Distance Field Shadows are enabled, anything beyond the set value for **Cascaded Shadow Map Distance** will be shadowed using
Distance Fields. In the comparison using both CSM and RTDF shadowing, the CSM shadow is set to 1,000 CM (centimeters), which allows for sharp
shadowing near the camera with lots of added detail. In the shadowing distance beyond 1,000 CM, RTDF shadowing is used, which shadows objects
up to 1.2 KM (kilometers) away. This enables the trees in the far distance to cast shadows when this would be too costly for Cascaded Shadow Maps.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For additional information about Directional Light settings, see the <a data-document-id=\"3225083\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-properties-in-unreal-engine\">Mesh Distance Fields Reference</a> page.",
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
  "excerpt_id": 1298,
  "excerpt_assignment_id": 2683,
  "blocks": [
    {
      "type": "header",
      "content": "Scene Representation",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Each level that you create is made up of all these Mesh Distance Fields for your placed Actors. When Mesh Distance Fields are generate, they are done so \"offline\" using triangle raytracing that stores the results in a volume texture. Because of this, mesh distance field generation cannot be done at runtime. This method computes the Signed Distance Field rays in all directions to find the nearest surface and stores that information.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "You can visualize the Mesh Distance Fields that represent your scene by using the viewport and selecting <strong>Show &gt; Visualize &gt; Mesh Distance Fields</strong>.",
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
              "image_id": 24649188,
              "caption": "",
              "alt_text": "Enabling of the Mesh Distance Field Visualization",
              "image": {
                "id": 24649188,
                "file_name": "04-distance-field-enable-mdf-view-mode.png",
                "file_size": 223645,
                "content_type": "image/png",
                "created_at": "2025-05-30T16:59:21.067+00:00",
                "height": 590,
                "width": 700,
                "storage_key": "4aca17ce-2d8b-4ed0-9aa6-7988604965dc",
                "context": "documentation"
              },
              "storage_key": "4aca17ce-2d8b-4ed0-9aa6-7988604965dc",
              "context": "documentation",
              "width": 400,
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "image",
              "image_id": 24649189,
              "caption": "",
              "alt_text": "Example of the scene using Mesh Distance Field Visualization",
              "image": {
                "id": 24649189,
                "file_name": "05-distance-field-visualize-mdf.png",
                "file_size": 2220785,
                "content_type": "image/png",
                "created_at": "2025-05-30T16:59:21.343+00:00",
                "height": 902,
                "width": 1907,
                "storage_key": "294ee649-7227-4829-aa27-44df6770f3e5",
                "context": "documentation"
              },
              "storage_key": "294ee649-7227-4829-aa27-44df6770f3e5",
              "context": "documentation",
              "width": 800,
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
              "content": "Menu to Enable Visualization",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Mesh Distance Field Visualization",
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
      "content": "<em>Click images for full size.</em>",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "When you see areas that are more white than gray, it means that many steps were needed to find the intersection of the mesh surface. Rays at grazing angles to surfaces took many more steps to intersect than would have for a simpler mesh.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "Z15",
  "settings": {
    "is_hidden": false
  }
}
```

### Mesh Distance Field Quality

Distance Field shadow fidelity has a significant impact on shadow accuracy, more so than [Distance Field Ambient Occlusion](https://dev.epicgames.com/documentation/en-us/unreal-engine/distance-field-ambient-occlusion-in-unreal-engine).
Increased Mesh Distance Field resolution will improve the shadows cast by Static Meshes. Use the Mesh Distance Field Visualization to inspect the quality.

The following example shows scene with Distance Field Shadowing with different Distance Field Resolution.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26433923,
  "caption_left": "Distance Field Resolution: 1",
  "image_right_id": 26433924,
  "caption_right": "Distance Field Resolution: 5",
  "image_left": {
    "id": 26433923,
    "file_name": "11-dfss-resolution-1a.png",
    "file_size": 722689,
    "content_type": "image/png",
    "created_at": "2026-02-05T17:48:01.471+00:00",
    "height": 720,
    "width": 1023,
    "storage_key": "04d669cf-fff9-4980-ac7e-6d9bb485005a",
    "context": "documentation"
  },
  "image_right": {
    "id": 26433924,
    "file_name": "12-dfss-resolution-1b.png",
    "file_size": 719232,
    "content_type": "image/png",
    "created_at": "2026-02-05T17:48:01.713+00:00",
    "height": 720,
    "width": 1023,
    "storage_key": "f2aa381e-50fc-41ea-94a2-ba29dbd72484",
    "context": "documentation"
  },
  "image_left_storage_key": "04d669cf-fff9-4980-ac7e-6d9bb485005a",
  "image_right_storage_key": "f2aa381e-50fc-41ea-94a2-ba29dbd72484",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

The following example shows scene with Mesh Distance Field visualization with different Distance Field Resolution.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26433926,
  "caption_left": "Distance Field Resolution: 1",
  "image_right_id": 26433927,
  "caption_right": "Distance Field Resolution: 5",
  "image_left": {
    "id": 26433926,
    "file_name": "13-dfss-resolution-2a.png",
    "file_size": 110336,
    "content_type": "image/png",
    "created_at": "2026-02-05T17:48:01.901+00:00",
    "height": 720,
    "width": 720,
    "storage_key": "8de60a8b-3652-4196-a46b-82f3c9b550d8",
    "context": "documentation"
  },
  "image_right": {
    "id": 26433927,
    "file_name": "14-dfss-resolution-2b.png",
    "file_size": 124205,
    "content_type": "image/png",
    "created_at": "2026-02-05T17:48:02.087+00:00",
    "height": 720,
    "width": 720,
    "storage_key": "24dcec40-bd07-4435-a5e8-962a19800f61",
    "context": "documentation"
  },
  "image_left_storage_key": "8de60a8b-3652-4196-a46b-82f3c9b550d8",
  "image_right_storage_key": "24dcec40-bd07-4435-a5e8-962a19800f61",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

Shadows for Mesh Distance Fields are computed at half-resolution with a depth-aware upsample. **Temporal Anti-Aliasing** (TAA) does a good job of helping reduce the flickering that can happen with half-resolution but jagged edges can still appear sometimes.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For additional information about Mesh Distance Field quality, see the <a data-document-id=\"3225038\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine\">Mesh Distance Fields</a> page.",
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

## Performance

The following GPU times were done on a Radeon 7870 at a resolution of 1920x1080 in a full game scene:

| Test | Cascaded/Cuebmap Shadow Maps Cost (ms) | Distance Field Shadows Cost (ms) | Percentage (%) Faster |
| --- | --- | --- | --- |
| Directional Light with distance of 10k units, 3 Cascaded Shadow Maps | 3.1 | 2.3 | 25% |
| Directional Light with distance of 30k units, 6 Cascaded Shadow Maps | 4.9 | 2.8 | 43% |
| One Point Light with a large radius | 1.8 | 1.3 | 30% |
| Five Point Lights with a small radius | 3.2 | 1.8 | 45% |

### Optimizations

Below are some things you can do or should consider to optimize Distance Fields shadowing:

- On a Directional Light, a larger **Source Angle** increases cost as more objects have to be considered for each point being shadowed.
- Larger values for **Distance Field Shadow Distance** reduce the culling efficiency.
- Shadows from meshes with **Two-Sided Distance Field Generation** (enabled in the **Build Settings**) will cost more as the resulting shadows are never fully opaque.

## Limitations

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Distance Field Shadowing shares the general limitations of the Mesh Distance Fields technique. For more information about these limitations,\nsee the <a data-document-id=\"3225038\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine\">Mesh Distance Fields</a> page.",
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
