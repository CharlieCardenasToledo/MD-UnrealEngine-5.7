# Camera Rigs

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine

> Application Version: 5.7

One of the methods real-world filmmakers use to produce smooth, sweeping shots, is by utilizing **Camera Rigs**, which are apparatuses that the camera attaches to. In Unreal Engine, you can use **Rail** and **Crane** rigs to create realistic camera movements.

#### Prerequisites

* You have an understanding of the **[Cine Camera Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine)**, and have already added one into your Level.
* You know how to **[Create Camera Animation](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-animate-cinematic-cameras-in-unreal-engine)** within **[Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine)**.

## Camera Rig Rail

The Camera Rig Rail is used to emulate a **[Camera Dolly](https://en.wikipedia.org/wiki/Camera_dolly)** system, which is used to create **[Tracking Shots](https://en.wikipedia.org/wiki/Tracking_shot)**. The rail's track length and curvature can be modified to suit the needs of your shot.

![camera rig rail](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/45cc0745-bfcf-479b-9c38-c650f9b62295/railoverview.png)

### Creation

To add a rail rig to your Level, navigate to the **Cinematic** tab in the **[Place Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine)** panel and locate **Camera Rig Rail**. Drag it from the panel and into your viewport.

![create camera rig rail](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8f83d5c2-d20e-4bca-b2bb-5b3bbea3fd76/addrail.png)

Next, move the camera to your chosen position, relative to the dolly, and attach it to the rail by dragging the camera Actor onto the rig rail in the **[World Outliner](https://dev.epicgames.com/documentation/en-us/unreal-engine/outliner-in-unreal-engine)**.

![attach camera rig rail](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca7230a7-1b92-4c31-8afd-60e166b55a0d/attachcamrail.gif)


After a camera is attached to the dolly, it can still be moved to fine-tune its final position.

### Track Length and Shape

The Camera Rig Rail uses Unreal Engine's **[Blueprint Splines](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-splines-in-unreal-engine)** for determining its track's length and shape. By default, the rail uses linear spline points at the start and end of the track. These points can be selected and moved to adjust the length and direction of the track.

![camera rig rail length](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fa011cb6-04f5-48b9-b05c-09af64e2d852/railshape1.gif)

Selecting and moving the spline tangent points will add curvature to the track based on the tangent angle.

![camera rig rail curve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/152bc475-10b7-4408-bc78-a22a0c5efa09/railshape2.gif)

Additional points can be added to the track's spline to fine-tune the track's shape. Select the rig rail, right-click the spline, and select **Add Spline Point Here** to add a new point at your cursor's position.

![camera rail spline point](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2807870e-b72d-41e8-b1e5-03a58b4c5139/addsplinepoint.png)

### Rail Controls

When selecting the **Camera Rig Rail Actor**, it displays the following properties for controlling its behavior and movement.

![rail details](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9beb6c55-fd49-42c6-92fb-075566c72bde/railproperties.png)

| Name | Description |
| --- | --- |
| **Current Position on Rail** | This property controls the dolly movement along the track. The value range is clamped between **0** and **1**, where **0** is the **start point** of the track, and **1** is the **end point**. current position on rail |
| **Lock Orientation to Rail** | By default, the camera's orientation is set independently from the orientation of the dolly. Enabling **Lock Orientation to Rail** will cause the camera's rotation to be set relative to the dolly's rotation. lock orientation to rail |
| **Show Rail Visualization** | Disabling **Show Rail Visualization** will hide the dolly and track mesh, leaving only the spline visible. show rail visualization |
| **Preview Mesh Scale** | This property changes the size of the track and dolly preview geometry. preview mesh scale |

## Camera Rig Crane

The **Camera Rig Crane Actor** is used to emulate a boom arm or **[Camera Jib](https://en.wikipedia.org/wiki/Jib_%28camera%29)** system, which is used to create **[Crane Shots](https://en.wikipedia.org/wiki/Crane_shot)**. The crane can be pivoted along horizontal and vertical axes, and can be extended as needed.

![camera rig crane](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d5936e17-ae07-4db3-ae48-08612a12d0d2/craneoverview.png)
