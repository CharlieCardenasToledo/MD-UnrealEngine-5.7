# Depth of Field

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/depth-of-field-in-unreal-engine

> Application Version: 5.7

Similar to what happens with real-world cameras, **Depth of Field** (DOF) applies a blur to a scene based on the distance in front of, or behind, a focal point. The effect can be used to draw the viewer's attention to a specific subject of the shot based on depth and adds an aesthetic to make the rendering appear more like a photograph, or film.

## Depth of Field Types

There are several methods of performing depth of field effects in Unreal Engine that you can use. These have been broken into two categories:

* **Cinematic:** This method provides a cinematic and filmic look to a depth of field effects. Adjustments for this method align more with common camera options available in photography and cinematography. This option works for Desktop and Console platforms.
* **Mobile:** This method provides optimized and lower-cost DOF options that work for Mobile platforms.

Select from the methods below to learn more about their features:

## Implementation

Depth of Field is broken up into three layers (or region); Near, Far, and Focal Region. Each of these is processed separately and then later composited together to achieve the final image effect. Objects in the Near and Far layers are always fully blurred. They are blended with the non-blurred scene to achieve the final result.

![Depth Of Field Implementation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f2b042c1-353a-4220-88d2-91b8f6128302/ue5_1-depth-of-field-layer-implementation-1.png)

* Objects within the **Focal Region** (Black) use the non-blurred scene layer. This layer can be very narrow—like here, where it is only focused on the character— or very wide, encompassing more of the scene's foreground and background.
* Objects in the **Near** (Green) or **Far** (Blue) that are outside any transition areas between the Focal Region and the Near or Far regions are fully blended to the blurred layer meaning they are out-of-focus.
* Objects within the transition area—like the area to the left of the car—are blended linearly between the non-blurred scene layer (for Near and Far) and their blurred layer based on their position within the transition of the Focal Region.

### Visualizing Depth of Field

These layers, including transition regions, can be visualized using the **Depth of Field Layers** show flag in the Level Viewport under **Show** \> **Visualize**.

![Scene](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dcd844d8-b9e7-4a3d-8648-c2d895834f03/ue5_1-1-depth-of-field-visualization-scene-view.png)

![Layer Visualization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/446c6d48-fca3-4680-a98c-b5f33da9e212/ue5_1-1-depth-of-field-visualization.png)

Visualizing the **Depth of Field Layers** also includes useful information relevant to the DOF method being used, such as values that are currently set or when moving the mouse around the scene, the distance from the camera to the Actor is displayed next to the mouse cursor.

![Visualizing Depth Of Field](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e416314e-5ac2-4ed5-a3a6-e7206bfc257d/ue5_1-depth-of-field-visualization-stats.png)
