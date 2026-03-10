# Landscape Noise Tool

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-noise-tool-in-unreal-engine

> Application Version: 5.7

The **Noise** tool applies a noise filter to produce variations in the surface of the Landscape heightmap.

## Using the Noise Tool

[Video: 1_4hs7l76k](https://dev.epicgames.com/community/api/cms/videos/1_4hs7l76k/embed.html)

In this example, the Noise tool is used to paint on the Landscape, similarly to how Sculpt would be used. Variations are painted around the area that raise and lower the heightmap based
on the tool settings. This enables you to paint grand or subtle variations into your Landscape.

Use the left mouse button control to sculpt with Noise for your Landscape heightmap:

| Controls | Operation |
| --- | --- |
| **Left Mouse Button** | Heightens or increases the heightmap or selected layer's weight. |

```json
{
  "type": "comparison_slider",
  "image_left_id": 26363829,
  "caption_left": "Before",
  "image_right_id": 26363830,
  "caption_right": "After",
  "image_left": {
    "id": 26363829,
    "file_name": "01-before-noise.png",
    "file_size": 1121034,
    "content_type": "image/png",
    "created_at": "2026-01-06T20:26:03.146+00:00",
    "height": 634,
    "width": 1040,
    "storage_key": "d3f76316-9cbd-41c3-9575-938adb6316d5",
    "context": "documentation"
  },
  "image_right": {
    "id": 26363830,
    "file_name": "02-after-noise.png",
    "file_size": 1188654,
    "content_type": "image/png",
    "created_at": "2026-01-06T20:26:03.358+00:00",
    "height": 634,
    "width": 1040,
    "storage_key": "e5947f11-3c9c-48a6-93cd-7a28c099744f",
    "context": "documentation"
  },
  "image_left_storage_key": "d3f76316-9cbd-41c3-9575-938adb6316d5",
  "image_right_storage_key": "e5947f11-3c9c-48a6-93cd-7a28c099744f",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

In this example, Noise has been painted onto the smooth Landscape surface giving it variations in different heights based on the strength and property values used.

## Tool Settings

| ![Noise Tool](https://dev.epicgames.com/community/api/documentation/image/f38b83e4-9bac-43db-996d-c620b0ddad2b) | ![Noise Tool Properties](https://dev.epicgames.com/community/api/documentation/image/81739b0a-0e95-46b3-b0ae-876511db1f20) |
| --- | --- |

| Property | Description |
| --- | --- |
| **Tool Strength** | Controls how much effect each brush stroke has. |
| **Noise Mode** | Determines whether to apply: all noise effects, only the noise effects that result in raising the heightmap, or only the noise effects that result in lowering the heightmap. **Both**: Raises and lowers values (for painted values of Noise) to the heightmap when the mouse click is activated. **Add**: Raises values (when painting Noise to the heightmap) when the mouse click is activated. **Sub**: Lowers values (when painting Noise to the heightmap) when the mouse click is activated. |
| **Noise Scale** | The size of the perlin noise filter used. The noise filter is related to position and scale, which means if you do not change **Noise Scale**, the same filter is applied to the same position many times. |

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The brush strength determines the amount of raising or lowering that can happen when using the Noise tool.",
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
