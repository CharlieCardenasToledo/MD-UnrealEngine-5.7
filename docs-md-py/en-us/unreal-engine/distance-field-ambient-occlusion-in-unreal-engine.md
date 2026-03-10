# Distance Field Ambient Occlusion

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/distance-field-ambient-occlusion-in-unreal-engine

> Application Version: 5.7

Shadowing for Movable Sky Lights is provided by using Signed Distance Field Volumes precomputed around each rigid mesh to generate medium scale Ambient Occlusion. In **Unreal Engine**, this is called **Distance Field Ambient Occlusion** (DFAO). It supports dynamic scene changes; the rigid meshes can be moved or hidden, and it will affect the occlusion. Unlike [Screen Space Ambient Occlusion](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine) (SSAO), occlusion is computed from world-space occluders, so there are no artifacts from missing data off-screen.

This dynamic AO solution will not work for all projects, as it has some invasive limitations which enable it to support dynamic scene changes. In particular, only slight-non-uniform scaling (squishing) is supported. Also, large Static Meshes produce inferior quality results because a small volume texture is mapped to every object.

## Scene Setup

This feature requires that **Generate Mesh Distance Fields** be enabled in your **Project Settings** in the **Rendering** section. See the [Mesh Distance Fields](https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine#enablingdistancefields) page for more information.

To enable Distance Field Ambient Occlusion, drag a **Sky Light** into the scene and set its Mobility to **Movable**

For a step-by-step guide, follow the [Distance Field Ambient Occlusion](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-distance-field-ambient-occlusion-in-unreal-engine) How-To guide to learn more.

## Sky Light

The **Sky Light** component enables you to adjust the various settings that can be found listed under **Distance Field Ambient Occlusion**.

![Distance Field Ambient Occlusion Settings of the Sky Light](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/250e4b6e-8f8d-4418-8926-3f034e88f57c/01-dfao-sky-light-dfs-settings.png)

These are comparisons of some of the settings you can adjust:

### Occlusion Contrast

![Occlusion | Contrast: 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f9b96fd-fa31-4113-bef2-fcd8e1149aea/02-dfao-contrast-0.png)

![Occlusion | Contrast: 1](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/418eed97-31c0-4a2e-8dbb-0f01104aa221/03-dfao-contrast-1.png)

### Minimum Occlusion

![Min Occlusion: 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/66ba5d19-5063-40d5-93a1-03494a0f89f9/04-dfao-min-occlusion-0.png)

![Min Occlusion: 1](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b18ba19-6c4d-4347-837e-a686e24186ac/05-dfao-min-occlusion-1.png)

### Occlusion Tint

![Occlusion Tint: | Black](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed47bc29-72a9-45ac-b1dd-b5d22cf49763/06-dfao-min-occlusion-tint-0.png)

![Occlusion Tint: | Red](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c6648a1e-54ea-4fa1-bd9b-422977fe4938/07-dfao-min-occlusion-tint-1.png)



For additional information about Sky Light settings and additional examples, see the [Mesh Distance Fields Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-properties-in-unreal-engine#skylight) page.

## Scene Representation

The view mode for Distance Field AO enables you to see how DFAO looks in the level without regards to any other lighting that is happening.

You can visualize the Distance Fields that represent your scene ambient occlusion by using the Level Viewport view mode for **Distance Fields Ambient Occlusion** by selecting **Show** > **Visualize** > **Distance Fields Ambient Occlusion**.

Click image for full size.

While in this view mode, the only [Sky Light setting](https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-properties-in-unreal-engine#occlusionmaxdistance) that will have any effect is **Occlusion Max Distance**.

![Example of DFAO visualization mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ef3bda2d-2ade-4559-8c8e-fac526808ffb/09-dfao-example-dfao-visualization-mode.png)
