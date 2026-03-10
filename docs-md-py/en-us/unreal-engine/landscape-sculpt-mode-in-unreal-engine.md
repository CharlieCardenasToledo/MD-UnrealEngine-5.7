# Landscape Sculpt Mode

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-sculpt-mode-in-unreal-engine

> Application Version: 5.7

The **Landscape Sculpt Mode** provides direct control over the shape of the landscape terrain. Using a variety of brush types and configurations, you can raise, lower, smooth, flatten, or otherwise modify the Landscape’s heightmap data in real time. This mode offers hands-on sculpting for shaping hills, valleys, cliffs, and other terrain features directly in the viewport.

Sculpt mode operates on the currently active **Edit Layer**, making every change non-destructive and reversible. Combined with procedural systems such as **Blueprint Brushes** and **Landscape Splines**, it allows for hybrid workflows that mix hand-sculpted terrain with procedural features.

![Tools available in Landscape Sculpt Mode](https://dev.epicgames.com/community/api/documentation/image/3761d75b-fb91-48ca-87c9-d1ce1e478d06)

## Tool Workflow

Once you've [created your Landscape](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-landscapes-in-unreal-engine), you will have access to the other features of the Landscape tool. To use sculpting, select the **Sculpt** mode tab.

Once selected, the Sculpt tool options will become available for choosing the type of sculpting tool along with the [brush style and falloff type](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-brushes-in-unreal-engine) you would like to use to apply their effects to your landscape heightmap using strokes.

![Brush-type-and-falloff-menu](https://dev.epicgames.com/community/api/documentation/image/f077e859-0605-4983-9cc9-75cc2b98cd89)

[Video: 1_wzgcvjko](https://dev.epicgames.com/community/api/cms/videos/1_wzgcvjko/embed.html)

With your Sculpting tool selected, you can now use the following controls to start sculpting your landscape:

| Common Controls | Operation |
| --- | --- |
| **Left Mouse Button** | Performs a stroke that applies an additive application of the selected tool's effects to the heightmap and raises the terrain. |
| **Left Mouse Button + Shift** | Performs a stroke that applies a subtractive application of the selected tool's effects to the heightmap and lowers the terrain. |
| **Ctrl + Z** | Undo last stroke. |
| **Ctrl + Y** | Redo last undone stroke. |

## Sculpting Tools

Use the **Sculpting Tools** to modify the shape of your Landscape in various ways. Explore the different sculpting selections available below:

- [Sculpt](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-sculpt-mode-in-unreal-engine)
- [Smooth](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-smooth-tool-in-unreal-engine)
- [Flatten](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-flatten-tool-in-unreal-engine)
- [Ramp](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-ramp-tool-in-unreal-engine)
- [Erosion](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-erosion-tool-in-unreal-engine)
- [Hydro](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-hydroerosion-tool-in-unreal-engine)
- [Noise](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-noise-tool-in-unreal-engine)
- [Visibility](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-visibility-tool-in-unreal-engine)
- [Mirror](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-mirror-tool-in-unreal-engine)
- [Region Select](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-region-selection-tool-in-unreal-engine)
- [Copy](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-copy-tool-in-unreal-engine)
