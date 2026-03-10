# Landscape Erosion Tool

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-erosion-tool-in-unreal-engine

> Application Version: 5.7

The **Erosion** tool uses a thermal erosion simulation to adjust the height of the Landscape heightmap. This simulates the transfer of soil from higher elevations to lower elevations by natural forces. The
larger the difference in elevation, the more erosion will occur. This tool also applies a noise effect on top of the erosion, if desired, to provide a more natural random appearance.

## Using the Erosion Tool

[Video: 1_3bahh2cc](https://dev.epicgames.com/community/api/cms/videos/1_3bahh2cc/embed.html)

In the example above, the Erosion tool is being used on the front and back sides of the mountain face. On the front side, the incline is not as steep, so the surface is not eroded as quickly with the
settings being used. However, on the back side, the incline is much steeper and erodes much more quickly.

Use the following controls to sculpt with Erosion for your Landscape heightmap:

| Controls | Operation |
| --- | --- |
| **Left Mouse Button** | Applies erosion values that raises, lowers, or does both to the heightmap. |

```json
{
  "type": "comparison_slider",
  "image_left_id": 26444394,
  "caption_left": "Before",
  "image_right_id": 26444395,
  "caption_right": "After",
  "image_left": {
    "id": 26444394,
    "file_name": "erosion-before.png",
    "file_size": 3378866,
    "content_type": "image/png",
    "created_at": "2026-02-11T20:57:42.315+00:00",
    "height": 1324,
    "width": 1920,
    "storage_key": "658faee4-9676-4976-b02b-62b7c4738d22",
    "context": "documentation"
  },
  "image_right": {
    "id": 26444395,
    "file_name": "erosion-after.png",
    "file_size": 3613182,
    "content_type": "image/png",
    "created_at": "2026-02-11T20:57:47.553+00:00",
    "height": 1324,
    "width": 1920,
    "storage_key": "a71396dd-95f0-4b89-a117-b9e988a59720",
    "context": "documentation"
  },
  "image_left_storage_key": "658faee4-9676-4976-b02b-62b7c4738d22",
  "image_right_storage_key": "a71396dd-95f0-4b89-a117-b9e988a59720",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

In the example above, Erosion is used to smooth out the more jagged regions of a hill that is being sculpted using the Sculpt tool and an alpha brush. Erosion uses noise painted onto the hillside to raise or lower the surface giving it variations in different heights based on the strength and various property values that are used.

## Tool Settings

|   |   |
| --- | --- |
| ![Erosion Tool](https://dev.epicgames.com/community/api/documentation/image/f44af721-effa-4c78-b2df-228b085ee687) | ![Erosion Tool Properties](https://dev.epicgames.com/community/api/documentation/image/3f59aaa0-a82c-44b8-892e-6ef1a5f7a584) |

| Property | Description |
| --- | --- |
| **Tool Strength** | Controls how much effect each brush stroke has. |
| **Combined Layers Operation** | Uses the combined result of all underlying Edit Layers, when checked. |
| **Threshold** | The minimum height difference necessary for the erosion effects to be applied. Smaller values will result in more erosion being applied. |
| **Surface Thickness** | The thickness of the surface for the layer weight erosion effect. |
| **Iterations** | The number of iterations performed. Larger values result in more levels of erosion. |
| **Noise Mode** | Whether to apply noise to raise or lower the heightmap, or do both: **Both**: Raises and lowers values for all erosion effects applied to the heightmap. **Raise**: Applies erosion effects that result in raising the heightmap. **Lower**: Applies erosion effects that result in lowering the heightmap. |
| **Noise Scale** | The size of the noise filter used. The noise filter is related to position and scale, which means if you do not change **Noise Scale**, the same filter is applied to the same position many times. |
| **Use Layer Hardness** | Determines whether the tool should take into account the layer's hardness parameter. |
