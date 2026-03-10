# Camera Cut Track

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-camera-cut-track-in-unreal-engine

> Application Version: 5.7

One of the key parts of creating a cinematic in **Sequencer** is selecting which camera to be active during a sequence. You can use the **Camera Cut Track** to control this behavior, as well as providing tools to blend cameras together, or to and from gameplay.

This document provides an overview of how to create and use the Camera Cut Track in Sequencer.

#### Prerequisites

* You have an understanding of [Sequencer](https://dev.epicgames.com/documentation/404).
* You are familiar with how to [add Cameras to Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-animate-cinematic-cameras-in-unreal-engine).

## Creation

There are a variety of ways to create a Camera Cut Track:

* Click **Add Track (+) > Camera Cut Track**.

  ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e26705aa-21c8-4279-8cac-74648ddf6f44/create1.png)
* Click the **Camera** button in the [Sequencer Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine), which creates a Camera Cut Track and a [spawnable](https://dev.epicgames.com/documentation/404) [Cine Camera Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine), then binds the camera to the track.

  ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/77c7c8b5-454a-4a3c-8a28-dd75fc558c6f/create2.png)
* Add a currently-existing Camera Actor to the sequence by clicking **Add Track (+) > Actor To Sequencer > Camera Actor**. When you do this, you create a Camera Cut Track automatically and bind it to this camera.

  ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6c7de21e-71fe-4738-b0de-b88235801c8b/create3.png)

### Binding Cameras

To make Sequencer use a specific camera to look through, you must bind it to the Camera Cut Track. In most creation methods detailed above, your camera is already bound. If not, then you can bind it by clicking **Add Camera (+)** and selecting the following:

1. If you already have Cameras added to the sequence, you can select one from the **Existing Bindings** category here.
2. If you want to add a new camera, you can select one from the level list under **New Binding**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/32af3a32-6709-4140-8c7d-b24c4b9a7bb3/create4.png)
