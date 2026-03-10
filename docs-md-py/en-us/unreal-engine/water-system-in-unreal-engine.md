# Water System

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/water-system-in-unreal-engine

> Application Version: 5.7

The Water system enables you to create rivers, lakes, and oceans that all interact and work together with your Landscape terrains using a spline-based workflow. The Water system unifies the shading and mesh rendering pipeline, with surfaces that support physics interactions and fluid simulation with gameplay, such as ripples caused by footsteps or the wake behind a boat moving through the water.

## Enabling the Water System Plugin and Content

The Water system is a self-contained plugin that can be enabled/disabled depending on whether you need it for your project. The plugin enables the rendering and meshing system for water, and also provides example and default content for you to use.

To enable the Water system, use **Edit > Plugins** to open the **Plugins** browser. Search for the **Water** plugin and check its box to enable it.

![Water Plugin](https://dev.epicgames.com/community/api/documentation/image/c8e7d495-1f62-4993-b204-571a8ade28a7)

_Click image for full size._

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Restart the editor for changes to take effect.",
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

### Additional Water Plugin Content

The Water plugin also contains some default materials and content that can be used in your own projects or for exploration. You can find it in the Content Browser under the **Water Content** folder.

![Content Browser Settings](https://dev.epicgames.com/community/api/documentation/image/dbc0901a-a4c1-4b2a-8386-ee38f1b32581)

_Click image for full size._

![Water Content Folder](https://dev.epicgames.com/community/api/documentation/image/ec4cc7bc-1acb-43b3-a9b0-a4c1269d1bc9)

_Click image for full size._

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you do not see this folder in your Content Browser, select <strong>View Options</strong> (located in the bottom-right) and check the boxes next to <strong>Show Engine Content</strong> and <strong>Show Plugin Content</strong>.",
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

In this folder, there are example maps and content to try on your own, such as:

- Caustics generation
- Fluid simulation
- Physics simulation buoyancy Blueprints

## Getting Started

- [Related Document](en-us/unreal-engine/water-meshing-system-and-surface-rendering-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/water-body-actors-in-unreal-engine.md)

## Essentials

- [Related Document](en-us/unreal-engine/simulating-waves-using-the-water-waves-asset-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/water-buoyancy-component-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/single-layer-water-shading-model-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/water-debugging-and-scalability-options-in-unreal-engine.md)

## Additional Resources

[Video: V_Cbd9Qf](https://dev.epicgames.com/community/api/cms/videos/V_Cbd9Qf/embed.html)

[Video: V_cttCii](https://dev.epicgames.com/community/api/cms/videos/V_cttCii/embed.html)
