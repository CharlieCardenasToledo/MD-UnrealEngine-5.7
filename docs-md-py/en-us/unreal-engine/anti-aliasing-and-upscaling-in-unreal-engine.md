# Anti-Aliasing and Upscaling

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/anti-aliasing-and-upscaling-in-unreal-engine

> Application Version: 5.7

**Anti-Aliasing** is the process of removing jagged, or stair-stepped, lines on edges and objects that should otherwise be smooth. There are different methods of anti-aliasing used to reduce these types of visual artifacts. Some are developed for use with specific renderers and platforms, while others are ideal for improving performance and fidelity.

![No anti-aliasing applied to the scene.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0ad00fcd-f7c3-45e9-ae48-a0b73f164508/1-no-aa.png)

![With anti-aliasing applied to the scene.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f20cbb48-4966-49c4-9676-d9110e0ff005/2-with-aa.png)

## Anti-Aliasing Methods

Many different methods of anti-aliasing have been developed. Unreal Engine provides several methods to choose from depending on the needs and requirements of your project. You can choose between anti-aliasing methods for desktop / console and mobile platforms.

Unreal Engine provides the following methods of anti-aliasing for your projects.

| Anti-Aliasing Method | Desktop / Console: Deferred Renderer | Desktop / Console: Forward Renderer | Mobile: Deferred Renderer | Mobile: Forward Renderer |
| --- | --- | --- | --- | --- |
| [Temporal Super Resolution (TSR)](https://dev.epicgames.com/documentation/en-us/unreal-engine/anti-aliasing-and-upscaling-in-unreal-engine#temporalsuperresolution) | Y | Y | N | N |
| [Temporal Anti-Aliasing Upsampling (TAAU)](https://dev.epicgames.com/documentation/en-us/unreal-engine/anti-aliasing-and-upscaling-in-unreal-engine#temporalantialiasingupsampling) | Y | Y | Y | N |
| [Fast Approximate Anti-Aliasing (FXAA)](https://dev.epicgames.com/documentation/en-us/unreal-engine/anti-aliasing-and-upscaling-in-unreal-engine#fastapproximateantialiasing) | Y | Y | Y | N |
| [Multi-Sample Anti-Aliasing (MSAA)](https://dev.epicgames.com/documentation/en-us/unreal-engine/anti-aliasing-and-upscaling-in-unreal-engine#multisampleantialiasing) | N | Y | N | Y |

Use the image slider below to switch between no anti-aliasing and the available anti-aliasing methods to compare their result. These are single frame captures that show a static scene. To see the clearest results of anti-aliasing, you should test in a scene where you have different types of assets and materials and where you can freely move around.

IMAGE SEQUENCE
NO AA, TSR, TAA, FAA, MSAA

![Without any Anti-Aliasing](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b0ca1b23-d9b1-43ad-aa77-2fe3441d980b/3-no-aa.png)
![Temporal Super Resolution | Deferred Renderer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/adec40c5-df65-46c0-9d5c-f787a75b9381/3-tsr.png)
![Temporal Anti-Aliasing Upsampling | Deferred Renderer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1841ab8a-a791-43ad-8240-331c454dfa48/3-taau.png)
![Fast Approximate Anti-Aliasing | Deferred Renderer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/141f1d78-0a08-4119-affe-a2da9bde682d/3-fxaa.png)
![Multi-Sample Anti-Aliasing | Forward Renderer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5df64c5d-614d-46bb-8145-741fe64f18c6/3-msaa.png)

**Drag the slider to see the scene when using no anti-aliasing, TSR, TAA, FAA, or MSAA (Forward Renderer).**

## Anti-Aliasing Scalability Settings

Anti-aliasing settings have their own scalability group in the **Engine Scalability Settings** to scale GPU costs directly related to the anti-aliasing quality for each of the methods. The scalability group controls the console variables for each of the respective anti-aliasing methods.

You can access the **Anti-Aliasing** scalability settings from the **Settings** dropdown menu under **Engine Scalability Settings**.

![Opening the Engine Scalability Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3d098b4b-0327-45af-9e13-664aa9dd1f4f/4-engine-scalability-settings.png)
