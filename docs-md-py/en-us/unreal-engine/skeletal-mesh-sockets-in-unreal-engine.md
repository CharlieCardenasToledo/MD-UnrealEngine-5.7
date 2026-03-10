# Skeletal Mesh Sockets

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-sockets-in-unreal-engine

> Application Version: 5.7

When attaching objects to Bones on your Skeletal Mesh, it may be necessary to offset this attachment. Instead of using math operations to estimate the offset transform, you can create **Sockets**. Sockets are dedicated attach points within the hierarchy of your Skeleton, which can be transformed relative to the Bone it is parented to. Once set up, you can attach your objects, weapons, and other actors to the Socket.

This document provides an overview of how to create and use Sockets.

#### Prerequisites

* Your project has a [Skeletal Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine).

## Creating Sockets

Sockets are created from the **Skeleton Tree**, which can be accessed from any of the main [Animation Editors](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-editors-in-unreal-engine). Right-click on a Bone in the **Skeleton Tree** and select **Add Socket.**

![add socket](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3a39642c-cbfb-4202-91c3-e498446c6257/create1.png)

Your new Socket will now be displayed in the Skeleton Tree, parented to the Bone that you selected previously.

![new socket](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7602e3a1-6541-483f-9e15-cb3268647f7e/create2.png)

Sockets can be deleted by right-clicking on them and selecting **Delete** or by pressing **Delete** on your keyboard.

![delete socket](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a9bcfbcd-0fec-47b9-a064-6c3ea85b8731/create3.png)


By default, when creating and manipulating Sockets, this will edit the [Skeleton Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletons-in-unreal-engine) of your Skeletal Mesh. Therefore, you must save it when making Socket changes.

## Managing and Editing Sockets

Once you have created a Socket, you can interact with them in the following ways.

### Socket Visibility

By default, Sockets are not visible in the [Animation Editor Viewport](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-editors-in-unreal-engine#viewport), you can make them visible by navigating in the Viewport menu to **Character > Bones**, and enabling **Sockets**.

![show sockets in viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a617ad6f-a69a-462b-a99c-fd276546ae16/visibility.png)

### Selection and Movement

Sockets can be selected by either clicking them in the Skeleton Tree, or if made visible in the viewport, by clicking them in the Viewport. You can then move them by dragging on the transform manipulator in the Viewport. Sockets can be translated, rotated, and scaled.

![select and move socket](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/749b505d-c36a-4601-8b44-1a8f860b6753/selectionmove.gif)

### Copy and Paste

Sockets can be copied and pasted in different ways depending on your requirements.

To copy a Socket, right-click on it in the Skeleton Tree and select **Copy Selected Sockets**, or press **Ctrl+C**.

![copy selected sockets](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2bd39ae4-7729-4b3b-bacf-d9a62fd1b64b/copypaste1.png)

Next, you can choose to either:

1. Paste the Socket to the same bone, which is done by right-clicking on any Bone in the Skeleton Tree and selecting **Paste Sockets**. This will essentially duplicate the Socket.

   ![paste sockets](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fb1f219e-a2fd-4366-8a74-eefb2869ed8a/copypaste2.png)
2. Paste the Socket to a different Bone, which is done by right-clicking a different Bone in the Skeleton Tree and selecting **Paste Sockets To Selected Bone**. This will paste a copy of that Socket with the same offset information, but parented to the new Bone.

   ![paste sockets to selected bone](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7c4c2317-3362-4ad3-8040-1589d4170fb9/copypaste3.png)

### Mesh Sockets

When [sharing Skeletons](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletons-in-unreal-engine#sharingskeletons) between different Skeletal Meshes, it may be necessary to create Sockets that are exclusive for one of the Skeletal Meshes. This can be done by using **Mesh Sockets**, which will make a Socket exist on the **Skeletal Mesh**, instead of the **Skeleton**.

![mesh socket compare](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7d14dca9-9701-4dbf-900e-ba132caf68d7/meshsocket1.png)
