# Performance Guidelines for Mobile Devices

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/performance-guidelines-for-mobile-devices-in-unreal-engine

> Application Version: 5.7

When developing for Mobile platforms, there are some things you should keep in mind when targeting specific devices or that are general good practices depending on the
list of devices you want to release your title for. This includes developing with a specific lighting tier to get the most out of performance on a
device and why a particular lighting tier may work best for your target audience. You will also find some suggestions to keep in mind for any project you work on that will
be developed with Mobile in mind.

## Performance Tiers

**Unreal Engine 5 (UE)** supports a variety of lighting features on mobile devices. Using these features costs performance and may cause your game to perform poorly on slower mobile devices. While it is
possible to mix and match most of UE's mobile lighting features, it can be useful to categorize these features into the following tiers. When building a mobile game, you should decide which features to
use based on the quality of graphics your game requires and the types of devices you need to support. Check the development requirements for [iOS Development](https://dev.epicgames.com/documentation/404) and [Android Development](https://dev.epicgames.com/documentation/404)
for more information on what devices have been tested here at Epic and which tiers we think are most appropriate for that device.

### LDR (Low Dynamic Range)

**Low Dynamic Range** (LDR) mode is the lowest performance tier supported in UE and is recommended for games that do not require lighting or Post Processing features.

To use this mode, you must disable **Mobile HDR** for your project in the **Rendering** section of the [Project Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/project-settings-in-unreal-engine).

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cda5782c-be22-490d-815d-e103dfd45ec7/01-mdv-perfom-disable-mob-hdr.png)

| Advantages | Limitations | Recommendations |
| --- | --- | --- |
| * Provides the fastest and lowest overhead mode available for mobile devices, which enables your game to run well on slower mobile devices. * Still provides full access to the **Material Editor** for defining custom shaders and even performing simple shading that can be used to fake lighting. | * The scene's color is written out in gamma space with each color channel clamped to the range of [0,1]. * Translucent primitives are blended in gamma space. In most cases, this will require you to author your translucent textures and Materials differently than you would in HDR or for a normal PC title. * Post Processing features are unavailable in this mode. | * Make sure all of your Materials have their shading model set to **Unlit** for maximum performance. * Placed lighting should not be used in your scene when depending on maximum performance. * Consider performing as many operations in the Materials **Vertex Shader** as possible. You can do this by enabling **Customized UVs**, connecting nodes to them and then in the pixel shader using a **Texture Coordinate** node to target the Customized UV. |

### Basic Lighting

In this tier, you will leverage **Static Lighting** and fully rough Materials to create **Levels** with interesting lighting while maximizing performance to reach a broader range of mobile devices.

To use this mode, you must enable **Mobile HDR** for your project in the **Rendering** section of the [Project Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/project-settings-in-unreal-engine).

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e907ba5-08f5-4f1e-b04f-7f385125cead/02-mdv-perfom-enable-mob-hdr.png)

| Advantages | Limitations | Recommendations |
| --- | --- | --- |
| * Access to Static Lighting and Global Illumination features. * Full HDR pipeline with access to some Post Processing features, like **Tone Mapping**. * Translucency is blended in linear space, enabling you to author content as your normally would for Desktop. | * Since all Materials need to be marked as **Fully Rough**, your Materials will not have interesting specular reflection. * If you choose to disable **Lightmap Directionality**, **Normal Maps** will have no effect. | * Author all of your Materials with the **Fully Rough** flag set. * Consider disabling the flag for **Lightmap Directionality** in your Materials for additional performance. * Use only Static Lights in your maps. * Disable some Post Processing features completely, like **Bloom**. Also, stick to the basic set of film and color controls. |

### Full HDR (High Dynamic Range) Lighting

In this tier, you take advantage of most of the HDR lighting features available for mobile in UE, as well as some of the Post Processing features. Using these features requires quite a bit of performance
in exchange for high-quality lighting features.

To use this mode, you must enable **Mobile HDR** for your project in the **Rendering** section of the [Project Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/project-settings-in-unreal-engine).

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ce95a18b-3040-409d-9ca8-53e27e7a9fab/02-mdv-perfom-enable-mob-hdr.png)

| Advantages | Recommendations |
| --- | --- |
| * Access to Static Lighting and **Global Illumination** features. * Full HDR pipeline with access to some Post Processing features. * Translucent is blended in linear space, enabling you to author content as you normally would for Desktop. * Realistic specular reflections on surfaces with support for varying roughness. | * Consider enabling **Bloom** to take full advantage of the HDR lighting pipeline. * Realistic specular reflections in combination with HDR lighting can lead to specular aliasing. To reduce this effect, enable the Material property for **Normal Curvature to Roughness** to reduce specular aliasing due to high-frequency information in your normal map. You can also consider enabling anti-aliasing via the **Project Settings > Rendering** to help reduce the artifact. * Take time to consider the placement of **Reflection Capture Actors** to achieve the best results. See [Reflections: Placing Reflection Captures](https://dev.epicgames.com/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine#placingreflectioncaptures) for more information. * Use only Static Lights and Lightmaps in your scene for the best performance. |

### Full HDR Lighting with per-pixel lighting from the Sun

In this tier, you take advantage of all of the HDR lighting features available for mobile in UE. This tier is the same as [Full HDR Lighting](https://dev.epicgames.com/documentation/en-us/unreal-engine/performance-guidelines-for-mobile-devices-in-unreal-engine#fullhdr_highdynamicrange_lighting) and has the same advantages and
recommendations with the exception that here you can add a single **Directional Light** to your scene that automatically uses per-pixel lighting for higher quality.

To use this mode, you must enable **Mobile HDR** for your project in the **Rendering** section of the [Project Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/project-settings-in-unreal-engine).

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/426b3eee-9ef5-4531-805b-0fa5c47f125a/02-mdv-perfom-enable-mob-hdr.png)

| Advantages | Recommendations |
| --- | --- |
| * All of the features and advantages listed for the [Full HDR](https://dev.epicgames.com/documentation/en-us/unreal-engine/performance-guidelines-for-mobile-devices-in-unreal-engine#fullhdr_highdynamicrange_lighting) tier. * Per-pixel diffuse and specular lighting for a single Directional Light. * High-quality precomputed **Distance Field** shadows for a single Directional Light. | * All of the recommendations and advantages of the [Full HDR](https://dev.epicgames.com/documentation/en-us/unreal-engine/performance-guidelines-for-mobile-devices-in-unreal-engine#fullhdr_highdynamicrange_lighting) tier. * Use only Static Lights in your except for a single Directional Light, which should be set to **Stationary**. |

## Shader Complexity View Mode

The [Shader Complexity](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-modes-in-unreal-engine#shadercomplexity) view mode in the [Mobile Previewer](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-mobile-previewer-in-unreal-engine) to get a
sense of what your Material costs will be for specific devices you are targeting. The colors indicated on screen will tell you how expensive the Material is for the device you're targeting; green means good
performance, bright red means very expensive, and white or pink means that the Material is very expensive.

To use it, in the **Main Viewport** click the **View Modes** list and select **Optimization Viewmodes** and choose **Shader Complexity**, or you can use the keyboard shortcut **Alt + 8**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/66979977-9c87-47e6-a334-270f3f605d96/03-mdv-perfom-enable-shader-complexity.png)

These are some examples taken from **Mobile Sun Temple** to give you an idea of Material cost when viewed using Shader Complexity:

|  |  |  |
| --- | --- | --- |
|  |  |  |
| The pillar Materials are fairly expensive here, and the translucent volumetric sheets are **very** expensive. In this scene, I asked to have the translucent sheets should be removed, as they cost too much. | Here the pillars are quite expensive as they use all five texture lookups and do quite a bit of layering. Otherwise, this is just about efficient enough for 30fps. | Here, the tree is causing pixels to be **extremely** expensive. If the player could ever get up close or cover the screen with that Material, the cost would be enormous. |

## Mobile Content Scale Factor

**Mobile Content Scale Factor** is a way to scale the resolution of your project to best fit the screen resolution of the mobile device being used to view your project.
You can [create and store multiple device profiles](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-device-profiles-in-unreal-engine) by creating a new configuration (.ini) file called **DefaultDeviceProfiles.ini** in your project's
config folder.

Inside of this file, you can specify what will happen to the resolution of your project for specific devices by entering the following command followed by one of the values from the iOS and Android sections below:

```
	r.MobileContentScaleFactor
```

In the following image, you can see an example of the Mobile Content Scale Factor being set in a configuration file:

Click for full image.

This particular configuration file is from the **Tappy Chicken** project and shows what will happen to the resolution of Tappy Chicken when it is played on various mobile devices. The top section of
this file handles the resolution scaling for iOS devices and the bottom section handles resolution scaling for Android devices. Take note that each **r.MobileContentScaleFactor** has a number after it. The number
is used after the command to determine if the project's resolution should be scaled up or down.

### Mobile Content Scale Factor for iOS

For iOS devices, inputting the following numbers will produce the following results:

The iOS scale factor is directly related to Apple's scale factor system and the actual resolution for any scale factor other than 0.0 will be corrected to match the aspect ratio of the screen and clamped to
the native resolution of the device.

| Value | Result |
| --- | --- |
| **0.0** | This will use the native resolution of the device. |
| **1.0** | On a Retina device is the non-retina resolution. |
| **2.0** | Full native resolution on iPhone 5S, iPad Air, etc. |
| **3.0** | Full native resolution for iPhone 6+. |

### Mobile Content Scale Factor for Android

For Android devices, inputting the following numbers will produce the following results:

Please note that inputting values other than 0.0 will use this value as the scale factor for a standard 1280x720 or 720x1280 resolution depending on the orientation of the device.

| Value | Result |
| --- | --- |
| **0.0** | This will use the native resolution of the device. |
| **1.0** | This will try and give you a resolution of 1280 x 720 for Landscape and 720 x 1280 for portrait. |
| **2.0** | This will try and give you a resolution of 2560 x 1440 for Landscape and 1440 x 2560 for portrait. |

## Mobile Material Quality Settings

When building content for a UE project that will run on both low and high-end mobile devices, you will often run into issues where a feature or your artwork is working on one set of devices
but not another. While there are a lot of ways to address issues like this, many of these are both time and resource intensive which can be error prone at times. To address these types of issues
UE has the **Material Quality Level** system. This system enables you to build one single Material that can then be used on a wide range of devices, giving you full control over which devices
use which features.

In the following sections, we'll cover these systems and how you can use them in your own UE projects:

### Previewing Material Quality Level

You can view what the different Material Quality Level settings will look like inside the Editor by going to the **Main Toolbar** and then then selecting **Settings** > **Material Quality Level** to choose
the level you want to preview.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff87d657-0c64-4dd9-89bc-b51aba98a00e/08-mdv-perfom-material-preview.png)

The following images show what a Material will look like when the Material Quality Level has been set to Low, Medium, and High.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b6e86cd3-dbfb-439f-8429-1d78c46e0d90/23-mdv-perfom-mmq-1.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4ef7b074-3c5d-4529-91fa-019322703e21/24-mdv-perfom-mmq-2.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fbab93df-9fa3-4ed6-b29b-3fa3499735f6/25-mdv-perfom-mmq-3.png)

Dragging the slider will show what happens when changing the Material Quality Level from Low to Medium to High

### Setting Material Quality Level

To set the Material Quality Level for your devices, you can do so in the following ways:

##### From the Console

Bring up the console by hitting the **`** (backtick) key and entering **r.MaterialQualityLevel** followed by one of the following values:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/787cf327-ef48-43fb-bc63-435c19cb1d59/09-mdv-perfom-command-line.png)
