# Rendering from Multiple Camera Angles

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-from-multiple-camera-angles-in-unreal-engine

> Application Version: 5.7

When rendering using [Movie Render Queue](https://dev.epicgames.com/documentation/404), there may be a requirement to render from multiple Cinematic cameras within a single sequence or [Shot](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequences-shots-and-takes-in-unreal-engine#shots). For example, you could be rendering a product demonstration video or training material, which may require multiple angles. Rendering from multiple angles within a single shot can be more ideal than using [Takes](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequences-shots-and-takes-in-unreal-engine#takes), as Takes cause new Level Sequence assets to be created, diverging your content.

This document provides an overview of how to render multiple camera angles from a single shot using Movie Render Queue.

#### Prerequisites

* You have a basic knowledge of how to create and open a [Level Sequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview)
* Movie Render Queue is a [Plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine) you must enable prior to use. From Unreal Engine's main menu, go to **Edit > Plugins**, locate **Movie Render Queue** in the **Rendering** section, and click the checkbox to enable it. Then, restart Unreal Engine.

  ![enable mrq plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1d729556-8f5b-4393-bdce-89d553559a7c/plugin.png)

## First Camera Setup

Assuming Sequencer is already open within the Level you want to render, the first step is to start creating your [Cinematic Cameras](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine).

1. Click **Camera** in the **Sequencer Toolbar.** This creates a [spawnable](https://dev.epicgames.com/documentation/404) Cine Camera Actor, [Camera Cuts Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-camera-cut-track-in-unreal-engine), and then binds the Cine Camera Actor to the Camera Cuts section.

   ![create first camera](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e1fe608-8f01-4faa-9eb8-d6f1760faeb4/firstcam1.png)
2. Next, [move and keyframe](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-animate-cinematic-cameras-in-unreal-engine) the camera to your desired framing and animation for this shot.

   1. Enable the **Camera icon** on the Cine Camera Actor track, which pilots the camera.
   2. You can also adjust camera-specific properties, such as **Aperture**, **Focal Length**, and **Focus Distance** to help with your shot composition.

![create camera shot](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df054805-49aa-4867-b8b6-02cbef9607a9/firstcam2.png)
