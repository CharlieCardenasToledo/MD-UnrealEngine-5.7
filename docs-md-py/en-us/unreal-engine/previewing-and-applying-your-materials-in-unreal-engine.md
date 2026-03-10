# Previewing and Applying your Materials

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/previewing-and-applying-your-materials-in-unreal-engine

> Application Version: 5.7

Previewing and applying your Materials is of critical importance to the Material creation process because it allows you see the results of the changes you make in the Material Graph. This is something you should do quite often to make sure that you are getting the exact results you want. This guide explains how to preview your Materials in the Material Editor viewport, and then shows how to apply a Material to meshes in Unreal Engine.

## Previewing in the Material Editor Viewport

The easiest way to preview a Material is in the Material Editor **viewport** window. The viewport window has a number of different options to customize the look and feel of the preview environment. The image below shows a breakdown of the viewport and its various options.

![Material Editor Viewport breakdown](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e96a9313-ee86-47cd-894b-43fb45dcaec6/material-editor-viewport-ue5.png)

| Number | Property | Description |
| --- | --- | --- |
| 1 | Viewport Options | This menu contains a toggle to turn the Realtime preview on and off. Also contains viewport statistics, layout options, and field of view (FOV) settings. |
| 2 | Viewport Types | Switch between perspective and orthographic viewports. |
| 3 | View Modes | Choose from available View Modes and change exposure settings. |
| 4 | Viewport Show Flags | Show or hide the background, grid, and viewport stats. |
| 5 | Preview Mesh | This is a preview mesh that you can use to examine how your Material will look on different objects. |
| 6 | Preview Mesh Options | Select from five different preview mesh options: cylinder, sphere, plane, cube, or a custom mesh. |

While inside the Material Editor, hover your mouse cursor over any icon to display a tooltip description explaining what each of the properties does. Some of these tooltips contain links to relevant documentation.

While you are creating your Materials in the Material Editor, the viewport window will show your changes immediately if you have the **Realtime** option enabled. Realtime is enabled by default. You can toggle this option on and off from the **Viewport Options** menu.

![Realtime Preview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92a541a0-ebde-4dfd-9ebb-2bc960d9b96a/toggle-realtime.png)

Adjust the values in any Material Expression currently hooked up to the [Main Material Node](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-main-material-node-in-unreal-engine) to preview changes in the viewport.



When making changes to your Material Network, it can take some time for the changes to render correctly in the viewport. The more complex a Material becomes, the longer it can take for the preview window to update. If you find that you need a quicker update, consider making your Material into a [Material Instance](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine).

### Preview Scene Settings

The **Preview Scene Settings** panel enables you to quickly preview your Materials in a variety of different environments and lighting conditions. This gives you a better understanding of how your Material will interact with light as the conditions change.

Go to **Window > Preview Scene Settings** in the menu bar enable the panel.

![Enable the Preview Scene Settings panel.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fbca3b39-edbd-4bdb-88ba-28eaffe132bd/open-preview-scene-settings.png)

The **Preview Scene Settings** panel opens in the bottom left corner of the Material Editor next to the Details tab.

![Preview Scene Settings interface options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2e193922-a1ea-41b4-943f-cd06808dea3d/preview-scene-settings-tab.png)

Preview Scene Settings contains options to alter the color, direction, and intensity of the viewport lighting. You can also change the background, and add basic post-processing effects.

This lets you view a Material under very different lighting conditions without changing anything in the Level.

![Default viewport settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e61e98d6-ac82-41e4-b315-c41dda2d93fd/preview-scene-settings-compare-01.png)

![Modified preview scene settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/721752df-6690-41b6-ba9f-cc50ca83d6ce/preview-scene-settings-compare-02.png)

### Previewing a Specific Node in the Material Graph

There are times when you may want to see the results of a single node in your Material graph. For example, if you are creating a Material that uses the [Fresnel Material expression](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-fresnel-in-your-unreal-engine-materials), you might want to preview the node so you can accurately fine-tune the falloff of the Fresnel effect.

**Right-click** a Material Expression and choose **Start Previewing Node** from the menu to preview that node in the viewport.

![Start previewing a Material Expression node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8a72fea9-d7d7-45f2-a8c5-a2aafe2c3210/start-previewing-node.png)
