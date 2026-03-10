# Feature Levels and Rendering Modes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mobile-feature-levels-and-rendering-modes-in-unreal-engine

> Application Version: 5.7

This page is **depricated** and will be removed in a future update. See the following pages:

* Information on the Mobile feature levels is available in the main landing page for [Mobile Rendering Features](https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-features-for-mobile-games-in-unreal-engine).
* Information about the Mobile Forward and Deferred shading modes is available in the [Mobile Shading Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/mobile-rendering-and-shading-modes-for-unreal-engine) page.
* Detailed information about the Mobile Deferred shading mode is available in the [Mobile Deferred Shading](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine) page.
* Information about the Desktop Renderer is available in the [Desktop Renderer on Mobile](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-desktop-renderer-on-mobile-in-unreal-engine) page.


Some features on this page are Experimental or Beta features. Use caution when using these in your projects, and avoid shipping projects using Experimental features.

The **Unreal Engine (UE)** Mobile renderer provides a separate rendering path from the desktop and console renderer, optimized for mobile devices such as mobile phones and tablets. This renderer can be configured in a variety of ways to suit specific devices and applications. This page provides a reference for where those options are and how to configure them.

## Feature Levels

The basic **Feature Levels** for Mobile are as follows:

| Feature Level | Description |
| --- | --- |
| OpenGL ES 3.2 | The default feature level for Android devices. You can configure the material settings for this feature level in **Project Settings** > **Platforms** > **Android Material Quality - ES32**. |
| Android Vulkan | A high-end renderer available for some specific Android devices. For more information on how to use Vulkan in your projects and what GPUs support it, see our guide on the [Android Vulkan Mobile Renderer](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-android-vulkan-mobile-renderer-in-unreal-engine). |
| Metal 2.0 | The feature level used for iOS devices. You can configure material settings for this feature level in **Project Settings** > **Platforms** > **iOS Material Quality**. |

Support for advanced Mobile rendering features varies depending on which Feature Level your application is using. Refer to each feature's documentation in the [Mobile Rendering Features](https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-features-for-mobile-games-in-unreal-engine) section for more information.

## Mobile HDR

The **Mobile High-Definition Rendering (HDR)** option is required to use a variety of high-end post-processes and rendering features.

## Using Deferred Shading

**Deferred shading** provides support for high-quality reflections, multiple dynamic lights, lit decals, and other advanced lighting features that are not normally available in the default forward rendering mode for Mobile.

![Reflections with mobile forward (old)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13290d19-bad6-4e9a-8bc0-b3e35368e976/mobilerenderingold.png)

![Reflections with mobile deferred (new)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/14c20dd9-e661-494e-a637-04fbe3f853cc/mobilerenderingnew.png)

To enable Deferred Shading, add the following CVar to your `DefaultEngine.ini`:

DefaultEngine.ini

```
	r.Mobile.ShadingPath=1
```

## Using the Desktop Renderer on Mobile (Experimental for Android, Beta for iOS)

Unreal now provides forward and deferred desktop renders for iOS devices and Android devices using Vulkan. This functionality is currently Experimental for Vulkan, and Beta for iOS.

* The iOS implementation is considered Beta in terms of feature readiness.
* The Android Vulkan implementation is considered Experimental.
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/99df6fef-0520-4ccf-92e9-a42acffbccd0/ipadusingdefferedrender.png)
