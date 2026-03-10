# Color Management in nDisplay

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/color-management-in-ndisplay-in-unreal-engine

> Application Version: 5.7

nDisplay includes color management tools so you can apply color grading and OpenColorIO (OCIO) configurations to your displays without modifying the overall look of the Unreal project itself. These color settings can be applied to the entire nDisplay cluster, or to individual viewports and cluster nodes.

Typically, you'll want to use these nDisplay-specific color management tools after you've achieved the desired look for the project. These tools are useful for tuning the look of the content as it appears on specific displays.

The settings are exposed in the nDisplay 3D Config Editor, and also in the nDisplay Root Actor for rapid iterations. Changes made to the nDisplay Root Actor can be tracked by [Level Snapshots](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-snapshots-in-unreal-engine).

Changes made to the nDisplay Config Asset are saved in the UAsset. Changes made to the nDisplay Root Actor are only on the instance of the config asset, and won't be saved in the UAsset.

The following sections describe how you can use color grading and OpenColorIO with your nDisplay setup.

## Color Grading

The overall behavior of the color grading settings is identical to [Post Process Volume](https://dev.epicgames.com/documentation/en-us/unreal-engine/color-grading-and-the-filmic-tonemapper-in-unreal-engine#colorcorrection), with additional options provided for more specific control between nDisplay viewports and cluster nodes. For more information on the settings exposed in nDisplay, see [nDisplay Root Actor Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-root-actor-reference-for-unreal-engine).

Color grading is additive: when multiple color grading settings are enabled, they are applied in order like a stack. For example, if one color grading setting applies red, and another applies blue, the resulting color will be purple, a mix of the two.

The following sections describe the behavior of color grading when it's applied to different parts of the nDisplay cluster.

### Viewports

Color grading is applied to a viewport in the following order if they're enabled:

1. Post Process Volume
2. nDisplay Root Actor's Entire Cluster Color Grading
3. nDisplay Root Actor's Per-Viewport Color Grading

When color grading is enabled for the entire cluster on the nDisplay Root Actor, the settings will be applied consistently to every viewport and inner frustum. The example below shows a before and after: the nDisplay cluster with color grading disabled, and the nDisplay cluster with a blue color applied.

![Enable color grading for the entire cluster](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4d710b46-44d9-4c70-8d0e-37a503edd0bf/01-entire-cluster.png)


![Enitire Cluster Color Grading Disabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e46cf4e-9015-44ec-8a50-e8091ac49794/image_1.png)

![Entire Cluster Color Grading Enabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48be3c3e-89cf-4f9d-b666-02f0a3a085a1/image_2.png)

You can also apply color grading to specific viewports in the nDisplay cluster. This is useful for when content appears to have different colors across different models and brands of displays.

In the example below, a separate color grading is only applied to the viewport rendered on the ceiling panel. The resulting color is purple because color grading is additive. The red color applied to the viewport is mixed with the blue color applied to the entire cluster.

![Enable color grading on a per-viewport basis](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7153f20c-09ff-4198-8946-642b4f5cf9de/02-viewport-color-grading.png)
