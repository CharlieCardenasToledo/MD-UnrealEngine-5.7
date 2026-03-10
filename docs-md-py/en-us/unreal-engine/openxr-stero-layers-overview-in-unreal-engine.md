# OpenXR Stereo Layers Overview

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/openxr-stero-layers-overview-in-unreal-engine

> Application Version: 5.7

OpenXR Stereo Layers send a separate texture to the head-mounted display (HMD) and re-project the texture in a separate rendering pass than the rest of the project. This can be useful for user interface (UI) elements that you want attached to the HMD without additional effects applied to them, such as post-processing or anti-aliasing.

Stereo Layers are rendered to the HMD, but they do not appear in the **VR Preview** window on your desktop.

This page is an overview of the OpenXR Stereo Layers feature. To learn how to add Stereo Layers to your OpenXR app, see the [OpenXR Stereo Layers Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/openxr-stereo-layers-quick-start-in-unreal-engine).

## Stereo Layer Types

You can set which space the Stereo Layer's position and rotation are relative to. The following are the available types:

* **Face-Locked**: The Stereo Layer stays in the same place in the HMD view, regardless of its position or rotation.

  ![Texture is relative to the HMD's view](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/173a2ad7-8449-45b5-a38e-03054b2bed15/image_1.gif)
* **Tracker-Locked**: The Stereo Layer position is relative to the real-world tracking space around the player.

  ![Texture is relative to the physical space around the user](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ebf659fd-230d-49cb-827e-fe9636dc14ce/image_2.gif)
* **World-Locked**: The Stereo Layer position is relative to the virtual world space and the object to which it's attached as a Component.

  ![Texture is relative to the virtual object in the scene](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a27e0c11-4cee-4abc-b5ee-2030219f10b5/image_3.gif)

Mixing Face-Locked layer priorities with World-Locked and Tracker-Locked layers by setting the `vr.StereoLayers.bMixLayerPriorities` console variable is not supported.

## Stereo Layer Shape

You can set the shape of the layer by selecting an option from the **Stereo Layer Shape** dropdown.
Stereo Layers support the following shapes:

* Cylinder
* Equirect
* Quad

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/35faedef-e109-41d6-b633-949a4c1b03cb/stereo_layer_shapes.png)
