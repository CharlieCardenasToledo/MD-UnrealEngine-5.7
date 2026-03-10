# Landscape Flatten Tool

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-flatten-tool-in-unreal-engine

> Application Version: 5.7

The **Flatten** tool pushes or pulls all other parts of the heightmap to the level that is currently under the mouse when activated. This can raise or lower the surrounding
heightmap values to be the same value.

## Using the Flatten Tool

[Video: 1_vph0p1ic](https://dev.epicgames.com/community/api/cms/videos/1_vph0p1ic/embed.html)

In this example, the Flatten tool is being used in the middle of the hillside to flatten out areas at the point where the mouse click was initiated. As long as the mouse is held down, the height value
that was detected is used along any surface to raise or lower (depending on your tool settings) to that height.

Use the following controls to sculpt your Landscape heightmap:

| Controls | Operation |
| --- | --- |
| **Left Mouse Button** | Flattens or levels by both raising and lowering or individually raising and lowering the heightmap. |

```json
{
  "type": "comparison_slider",
  "image_left_id": 24499259,
  "caption_left": "Before Flattening",
  "image_right_id": 24499261,
  "caption_right": "After Flattening",
  "image_left": {
    "id": 24499259,
    "file_name": "01-before-flattening.png",
    "file_size": 1266403,
    "content_type": "image/png",
    "created_at": "2025-04-11T16:59:04.552+00:00",
    "height": 664,
    "width": 1039,
    "storage_key": "253f09d8-01a7-4217-a22a-c9ef177d615d",
    "context": "documentation"
  },
  "image_right": {
    "id": 24499261,
    "file_name": "02-after-flattening.png",
    "file_size": 1268481,
    "content_type": "image/png",
    "created_at": "2025-04-11T16:59:04.771+00:00",
    "height": 664,
    "width": 1039,
    "storage_key": "25eb1273-3852-4942-98e1-af2a8686a11a",
    "context": "documentation"
  },
  "image_left_storage_key": "253f09d8-01a7-4217-a22a-c9ef177d615d",
  "image_right_storage_key": "25eb1273-3852-4942-98e1-af2a8686a11a",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

The brush strength determines the amount of Flattening that can happen when using the Flatten tool.

## Tool Settings

| ![Flatten Tool](https://dev.epicgames.com/community/api/documentation/image/09f48b82-f352-4c39-97d7-659d80f35efe) | ![Flatten Tool Properties](https://dev.epicgames.com/community/api/documentation/image/2b75ff61-d26d-4422-a90c-225dbc0bde84) |
| --- | --- |

| Property | Description |
| --- | --- |
| **Flatten Target** | Sets the target height toward which to flatten. |
| **Tool Strength** | Controls how much smoothing occurs with each brush stroke has. |
| **Flatten Mode** | Determines whether the tool will raise or lower the heightmap section under the brush. **Both**: Raises and lowers values to the current height value when the mouse click is activated. **Raise**: Raises values that are lower than the currently selected height when the mouse click is activated. Any values above this clicked point will be left unchanged. **Lower**: Lower values that are higher than the currently selected height when the mouse click is activated. Any values lower than this clicked point will be left unchanged. |
| **Use Slope Flatten** | If checked, flattens along the Landscape's existing slope instead of flattening toward a horizontal plane. |
| **Pick Value Per Apply** | If checked, constantly selects new values to flatten toward, instead of only using the first clicked point. |
| Advanced |   |
| **Show Preview Grid** | When Flatten Target is enabled, you can enable this option to show a preview grid for the flatten target height. |
| **Terrace Interval** | Sets the height of the Terrace interval for Terrace Flatten mode. |
| **Terrace Smoothing** | Sets the smoothing value for Terrace Flatten mode |
