# Troubleshooting Mixed Reality Capture

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/troubleshooting-mixed-reality-capture-in-unreal-engine

> Application Version: 5.7

This page provides troubleshooting information for Mixed Reality Capture (MRC).

## Flickering During Captures

Depending on the resolution of the MR capture target (the default is 1080p), your app may be constrained by its render target pool size. By default, render targets are set to reallocate as needed, which can lead to ping-ponging and flickering as the MR capture targets fight with the stereo render targets. (shown in the video below)

If you see this kind of behavior, you can change the render target resize rule to 'Grow' (in your engine.ini file, set *r.SceneRenderTargetResizeMethod=2*). Making this change should resolve the issue.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/08dd5788-bbb6-4f99-96ef-74c753d0cc06/mr_captureflicker.gif)

## Capture Not Displaying on Spectator Screen

The MRC framework uses the [Virtual Reality Spectator Screen](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-reality-spectator-screen-in-unreal-engine) to display the composited scene. This means the Mixed Reality capture will only be displayed when running in Virtual Reality. If your project also uses the spectator screen, then you need to conditionally guard where you use them. There are MRC methods to help with this:

**Get Mixed Reality Capture Texture**  
Returns the Capture Texture, or a nullptr if there isn't one.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/25e0d3ac-a8d0-43a5-ab6f-bc8f0de5613e/01-get-mixed-reality_ue5.png "01-get-mixed-reality_ue5.png")
