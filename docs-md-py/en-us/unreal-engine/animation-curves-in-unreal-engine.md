# Animation Curves

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curves-in-unreal-engine

> Application Version: 5.7

As you play [Animation Sequences](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine) on your **Skeletal Mesh**, you may find it necessary to animate additional properties and values synchronized to that animation. You can accomplish this using **Animation Curves** (also called **anim curves**, or **curves**), which are float-type values you can add and keyframe within an Animation Sequence. Curves can be useful for augmenting your animations with additional animatable properties, such as animating [Material Parameters](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine), [Morph Targets](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-morph-target-pipeline-in-unreal-engine), and other attributes.

This document provides an overview of Animation Curves, and the various ways you can use them.

#### Prerequisites

* Your project contains a [Skeletal Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine) and [Animation Sequences](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine).
* If you are using anim curves to affect **Material Parameters**, you need a basic understanding of [Material Instancing](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine).
* If you are using anim curves to affect **Morph Targets**, you need a basic understanding of setting up [Morph Targets](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-morph-target-pipeline-in-unreal-engine) on your Skeletal Mesh.

## Creating Animation Curves

Animation Curves can be created in the following ways:

1. When viewing an **Animation Sequence** in the [Animation Sequence Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequence-editor-in-unreal-engine), click the **Curves** track dropdown menu and select **Add Curve… > Create Curve**. Type in the name of the new curve and press **Enter** to create it.

   ![create curve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/22145f2c-9468-4f2d-af0b-5fa8607f5227/create1.png)
2. In the [Anim Curves panel](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curves-in-unreal-engine#animcurvespanel), right-click in the **curve list area** and select **Add Curve**. Type in the name of the new curve and press **Enter** to create it.

   ![anim curve panel add curve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6c3d4a90-4fe0-4448-8a9a-246a4ded0454/create2.png)
3. If your skeleton already has curves, you can select them from the **Curves > Add Curve…** dropdown menu.

   ![add existing curve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9cf09eaa-e65c-4af0-9b32-e39b0da2b148/create3.png)

Animation Curves are stored on the **Skeleton Asset**. Therefore, when you are creating curves, you are also editing the [Skeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletons-in-unreal-engine), which will require you to save it.

### Importing Animation Curves

Custom attributes can also be created externally in animation software like Autodesk Maya, and then imported as curves along with your Animation Sequence.

To do this, first [create a custom attribute](https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2019/ENU/Maya-Basics/files/GUID-C7385EC4-74E1-4F6E-8C9D-60F5CCDA7994-htm.html) on any bone in your skeleton and keyframe it. You must ensure that it is a float-type attribute, as that is the only compatible data type with curves. Once finished, export your animation.

![create bone attribute](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d0970406-86ac-4c49-9d74-8f530a2983dd/attribute1.png)
