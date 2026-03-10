# Volumetric Lightmaps

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-lightmaps-in-unreal-engine

> Application Version: 5.7

Volumetric Lightmaps replace the [Indirect Lighting Cache](https://dev.epicgames.com/documentation/en-us/unreal-engine/indirect-lighting-cache-in-unreal-engine) and Volume Lighting Samples going forward.

The Indirect Lighting Cache can be re-enabled by opening the **World Settings > Lightmass Settings** and setting the **Volume Lighting Method** to **Sparse Volume Lighting Samples**.

Lightmass generates [surface lightmaps](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-lightmapping-in-unreal-engine) for indirect lighting on static objects. However, dynamic objects (like characters) need a method of receiving indirect lighting as well. This is done by storing precomputed lighting in all points in space called a **Volumetric Lightmap** at build-time and then used for interpolation at runtime for indirect lighting of dynamic objects.

![Sparse Volume Lighting Samples | (Old Method)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0e9807f0-3403-4ea1-88b8-16027f7ba5b8/01-volumetric-lightmaps-lit-movable-character-ilc.png)

![Volumetric Lightmaps | (New Method)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e05a249e-4d88-48bb-b852-40f9f3a77370/02-volumetric-lightmaps-lit-movable-character-vlm.png)

Sparse Volume Lighting Samples determined leaking amounts and lighting accuracy. Volumetric Lightmaps improve upon this.

## How It Works

From a high-level, the Volumetric Lightmaps system works in the following manner:

* Lightmass places lighting samples throughout the level and computes indirect lighting for them during the lighting build.
* When it comes time to render a dynamic object, the Volumetric Lightmap is interpolated to each pixel being shaded, providing precomputed indirect lighting.
* If no built lighting is available (meaning the object is new or has moved too much), lighting is interpolated to each pixel from the Volumetric Lightmap for **Static** objects until lighting is rebuilt.

When a Lightmass Importance Volume is placed, the Volumetric Lightmap builds bricks that are made up of 4x4x4 cells (lighting samples). When lightmass is run, the cells are placed over the whole Lightmass Importance Volume and then it uses more cells around static geometry in the scene to capture better indirect lighting results.

![Example of visualization the Volumetric Lightmap](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0960fe12-7dd6-4fc0-98ac-cd8367bb41f8/03-volumetric-lightmaps-cube-vlm.png)
