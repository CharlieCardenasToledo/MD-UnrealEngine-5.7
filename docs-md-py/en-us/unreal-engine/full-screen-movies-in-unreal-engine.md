# Image Plate

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/full-screen-movies-in-unreal-engine

> Application Version: 5.7

The **Image Plate Actor** supports the playback of movies and image sequences from a plate attached to the frustum of a **[Cine Camera Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine)**. Using these image plates, you can playback full-screen videos and image sequences, as well as including foreground elements within the camera's perspective.

#### Prerequisites

* The Image Plate plugin must be enabled prior to use. Navigate in the Unreal Engine menu to **Edit > Plugins**, locate **Image Plate** in the **Rendering** section, and enable it. You may need to restart the editor for this change to come into effect.

  ![image plate plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3d309ec-4ca2-417f-9f05-a62fcb7f53ca/plugin.png)
* You are familiar with **[how to set up a video asset for playback](https://dev.epicgames.com/documentation/en-us/unreal-engine/play-a-video-file-in-unreal-engine)**, or **[how to set up image sequences for playback](https://dev.epicgames.com/documentation/en-us/unreal-engine/play-an-image-sequence-in-unreal-engine)**.
* You are familiar with the usage of the **[Media Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-movie-media-track-in-unreal-engine)**.
* You are familiar with the basics of **[Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-materials)**.
* You have an understanding of **[Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine)** and its **[Interface](https://dev.epicgames.com/documentation/404)**.

## Creation

To fully set up the Image Plate Actor, you will need to add both a **[Cine Camera Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine)** and an **Image Plate Actor** to a Level, then attach the plate to the Cine Camera Actor.

First, add a Cine Camera Actor to your Level by navigating to the **Cinematic** tab in the **[Place Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine)** panel, and locate **Cine Camera Actor**. Drag it from the panel and into your viewport.

![create cine camera](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e7ccf323-5c7f-47e0-9f6e-1e2d0b68e165/createcam.png)
