# Screen Percentage with Temporal Upscale

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/screen-percentage-with-temporal-upscale-in-unreal-engine

> Application Version: 5.7

**Screen Percentage**is a resolution scaling technique used to render a lower or higher resolution image than what is actually being presented. Being able to adjust the screen percentage enables your games to maintain a balance between performance and image resolution quality.

Prior to Unreal Engine 4 (UE4) version 4.19, you only had to change the screen percentage, but it has now been split into two types of scaling during the rendering pipeline: Primary and Secondary Spatial Upscaling.

* **Primary Spatial Upscaling** is the same screen percentage that has been used previously. It is based on the idea of rendering a frame at a lower resolution and then upscaling it before the user interface (UI) is drawn.
* **Secondary Spatial Upscaling**does a second and final spatial upscale pass, independently of the Primary upscaling pass.

## Primary Screen Percentage

The **Primary Spatial Upscale** (or primary screen percentage) works by rendering the screen resolution at a percentage of the screen and then scaling it to fit your current screen resolution. Using a lower screen percentage (or lower resolution) and then upscaling it is called upsampling. Or, when the screen percentage is increased (rendering at a higher resolution), it is scaled down to your current screen's resolution, which is called **super sampling**. All of this takes place before the user interface (UI) is drawn and can have an impact on performance.

The conceptual idea of how screen percentage works for all the buffer render targets that make up the image rendered on screen for a single GPU frame can be shown as follows:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/233bc996-cfb7-499f-9bc9-cd872d47f6c7/noupscaling.png "NoUpscaling.png")

For each GPU frame, all the render targets use their full resolution throughout the pipeline.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/44adf2e9-3221-43ae-822c-493255da3017/spatialupscale.png "SpatialUpscale.png")

With Spatial Upscaling, anything drawn before the UI is at a lower or higher resolution based on the Screen Percentage used. The screen percentage has been lowered (indicated by the narrower render targets before UI), creating a lower resolution image for the render targets. Spatial Scaling happens before the UI, scaling the image to the screen resolution it will be output to. For example, if the current resolution is set to 1920x1080 and a screen percentage of 83% is used, the render targets will be resized to an approximate resolution of 1600x900 before being upscaled back to 1920x1080.

### Spatial Upscale Quality

When upscaling the render targets, the quality of the upscale can be defined by using the following console variable:

```
	r.Upscale.Quality
```

It controls the quality in which screen percentage and Windowed Fullscreen mode scales the 3D rendering.

| Upsample Quality Value | Upsample Result |
| --- | --- |
| **0** | Nearest Filtering |
| **1** | Simple Bilinear |
| **2** | Directional blur with unsharp mask upsample |
| **3** | 5-tap Catmull-Rom bicubic, approximating Lanczos 2 (default) |
| **4** | 13-tap Lanczos 3 |
| **5** | 36-tap Gaussian-filtered unsharp mask (very expensive, but good for extreme upsampling) |

Alternatively, you can control how the tonemapper pass is handled by using the following console variable:

```
	r.Tonemapper.MergeWithUpscale.Mode
```

The tonemapper integrates a simple bilinear color space spatial upscale that can be used for performance reasons when enabled using a value of **1**. However, if a Post Process Material is inserted after the tonemapper, the tonemapper won't do the upscale. It will fall back to using the primary spatial upscale as if it were disabled.

## Temporal Anti-Aliasing Upsample

In addition to Primary Spatial Upscale, a second upscaling technique is also supported for the primary screen percentage: Temporal Upsample. Instead of performing temporal integration with the Temporal Anti-Aliasing (TAA) and then doing a primary spatial upscale, both happen at the same time in the Temporal Anti-Aliasing Upsample (TAAU) shader. It also allows them to converge to sharper images than what a spatial-only upscale could provide but comes at a higher cost since a larger number of post processes run at a higher resolution. It also allows for primary screen percentage changes to be hidden by dynamic resolution allowing it change more often to match the GPU budget as closely as possible.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aedcf059-93b1-4b5c-ba2e-127a4fa403ee/spatialandtemporalupsample.png "SpatialAndTemporalUpsample.png")

TAAU happens earlier in the pipeline causing the passes that follow to render at a higher resolution, leading to higher costs with sharper images.

It should be noted that with the temporal upsample, the ordering of the different post processes has not changed with the addition of TAAU, it simply replaced TAA. The difference now is that any process before TAAU will use a lower resolution before being upsampled to the resolution after the TAAU pass. Before 4.19, the resolution was assumed to be the same everywhere in the post processing.

As the primary screen percentage decreases, the convergence to a clean full-resolution output changes. Therefore, some existing TAA artifacts would be more noticeable. For example, aliasing can become an issue for very thin geometry increasing the probability to miss this geometric detail as the primary screen percentage is lowering.

### Enabling Temporal Upsample

To use Temporal Anti-Aliasing Upsample, you'll need to opt into the Project Setting for **Temporal Upsampling** or more simply by using the following console variable:

```
	r.TemporalAA.Upsampling 1
```

A lower primary screen percentage with spatial upscale can lose significant detail when using lower resolutions. For example, for something like a chain-link fence or the grill on the front of a car, the detail can become harder to see at farther distances when Temporal Anti-Aliasing is used. Enabling TAAU, this can be reduced while still using a lower screen percentage.

![Screen Percentage: 70 | Temporal Upsample: Disabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fc60ed14-edbd-4d0b-8ef0-a0d51aab245a/temporalupsample_before1-1.jpg)

![Screen Percentage: 70 | Temporal Upsample: Enabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/77f975d4-e2f0-401c-b4e6-d869b242737b/temporalupsample_after1-1.jpg)

In the comparison, the primary screen percentage has been set to **70** and the camera has been moved to a far enough distance to effectively see how TAA affects high-frequency geometry and materials. The temporal upsample enables this detail to be seen, even when lower resolutions are used to maintain this detail as much as possible.

### Additional Examples

In this first set of comparisons, a default scene that has only lowered the screen percentage is compared to one using the same screen percentage except it has the temporal upsample enabled. The difference may seem minute for these screenshots but on larger screens the areas with dense geometry or high-frequency textures can regain some lost detail, like with the fencing on the top of the house, or the tree fronds on the trees (close and far ones).

![Screen Percentage: 70 | Temporal Upsample: Disabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/87cb8135-df52-4665-ba4e-6f92e230ade8/shot3a-1.jpg)

![Screen Percentage: 70 | Temporal Upsample: Enabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/640155d3-6242-4b75-8fac-451a588d3d8b/shot2a-2.jpg)

In this one, the default screen percentage of 100 without any temporal upsample can be compared to the lower screen percentage that is using temporal upsample. While some specular highlights and some material detail is lost, the temporal upsample does a really good job of maintaining geometry detail even though the screen percentage has been lowered.

![Screen Percentage: 70 | Temporal Upsample: Enabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2d518691-ae3f-48aa-9568-f791189791b0/shot2a-5.jpg)

![Screen Percentage: 100 | Temporal Upsample: Disabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/185a9702-96f7-4cd0-9dbf-d40ffbc78443/shot1a-1.jpg)

### Automatic View Texture Mip Bias

Because screen percentage causes geometry to render at a lower pixel density, temporal upsample requires more texture information from the **Surface** and **Deferred Decal** Material Domains to maintain the same output sharpness. For this purpose, the Texture Sample expression can use, by default, **Automatic View Mip Bias**.

The Texture Sample expression can use **Automatic View Mip Bias** to toggle whether the texture should be sampled with per-view Mip biasing for sharper output with Temporal Anti-Aliasing.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/874c3b49-e4a9-468f-82f5-3e1ec5940494/automaticviewmipbias.png "AutomaticViewMipBias.png")
