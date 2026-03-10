# Visualizing Play Area Bounds

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/visualizing-play-area-bounds-in-unreal-engine

> Application Version: 5.7

Users can specify the bounds of their play area, sometimes called the *stage*, on their device. You can access these bounds in Unreal Engine with the [OpenXR APIs](https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine).

![image alt text](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/88ae5d1c-9121-4845-9c9b-491b9d4a7155/play-area-boundary-oculus-guardian.gif)

On Oculus devices, the Guardian boundary appears when the user gets close.

This page shows how you can visualize the play area bounds in your project. For setting up play area bounds on your device, refer to your device's documentation.

## Get Play Area Bounds

The `Get Play Area Bounds` function returns the length of the largest rectangle that can be found inside your play area. Play area bounds are visualized by your OpenXR compatible runtime when the user gets close to the boundary. It can also be useful to inform the user when they are moving close to the boundary with custom visualizations in your application.

![image alt text](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9cf23f63-bf80-4b66-a366-202517484d3b/get-play-area-bounds-blueprint-node.png)
