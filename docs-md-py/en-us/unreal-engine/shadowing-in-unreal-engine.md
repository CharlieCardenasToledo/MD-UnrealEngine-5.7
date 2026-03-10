# Shadowing

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/shadowing-in-unreal-engine

> Application Version: 5.7

Shadows make objects feel grounded in the world. They give the viewer a sense of depth and space. Shadowing is supported by all available [types of lights](https://dev.epicgames.com/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine) and determined by a light's mobility.

## Supported Shadowing Methods

The type of shadowing used by a light is determined by what its Mobility is set to: **Static**, **Stationary**, or **Movable**. Mobility is the primary guiding factor in whether a light should cast a precomputed shadow baked into a texture called a lightmap, a dynamic shadow generated in real-time, or one that uses a combination of precomputed and dynamic shadowing.

A Light's Mobility can be set independently of other lights in the Level, meaning that you can use any combination of mobilities to light the scene.

The following shadowing methods are available to use:

Some require Project Settings to be enabled, or additional properties to be enabled on the Light to work.

* Shadow Mapping
  + The default shadowing method that renders geometry into shadow depth maps. This shadowing method works for all platforms that support dynamic shadowing, but it requires manual setup of shadowing distances and only culls per-component, causing poor performance with high polygon scenes. Also, it does not support [Nanite](https://dev.epicgames.com/documentation/404) geometry.
* [Virtual Shadow Maps](https://dev.epicgames.com/documentation/404)
  + This shadowing method renders geometry into virtualized shadow depth maps. It provides high quality shadows for next-gen projects with simplified setup. It has high efficiency culling when used with [Nanite](https://dev.epicgames.com/documentation/404) geometry.
* [Ray-traced Shadows](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-ray-tracing-in-unreal-engine)
  + This method traces a set number of samples per pixel using [Hardware Ray Tracing](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-ray-tracing-in-unreal-engine) with denoising algorithms to render high quality ray-traced shadows in real-time.
* [Distance Field Shadows](https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine)
  + This method uses signed distance fields per Static Mesh and is used by [Lumen Software Ray Tracing](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-global-illumination-and-reflections-in-unreal-engine) for dynamic soft area shadows.
* [Precomputed Shadows with Lightmass](https://dev.epicgames.com/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine)
  + This method uses lighting data from the scene to generate lightmap textures that are applied to Static geometry in the Level. Geometry requires additional setup with proper lightmap UVs. Precomputing lighting for the scene can vary depending on machine specifications, scene complexity, and other factors when determining how long a light build will take.

## Static and Stationary Light Preview Shadowing

When editing a Light with its Mobility set to **Stationary** or **Static** the light is considered *un-built*. **Preview Shadowing** is enabled to give you an idea of what the shadows will look like when lighting is rebuilt, but they are not representative of the final, baked result.

To indicate what are actually preview shadows, shadows from these lights are shown in the Level Editor with the text **Preview**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dbdfaa3b-5ea1-48a0-a043-7c4d4f680ea1/unbuiltshadows.png)


Preview text over shadows is visible only while working in the Level Editor. If you launch your project in Play-In-Editor (PIE) or Standalone Game modes, no text will appear over unbuilt shadows.

To resolve any preview shadows, you will need to build lighting. Use the Main Menu to select **Build > Build All Levels** to kick off a lighting build.

|  |  |
| --- | --- |
| built scene shadows | preview shadows |
| Built Scene Shadows | Preview Shadows |

Preview shadows can be disabled while working in the Editor by unchecking the **Preview Shadows Indicator** under the Level Viewport **Show > Visualize** menu.

## Configuring Shadowing Properties of Lights

The following properties can be found on the available [Types of Lights](https://dev.epicgames.com/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine).

The properties are accessible through the Level's **Details** panel when a Light is selected.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| directional light properties | sky light properties | point light properties | spot light properties | rect light properties |
| Directional Light | Sky Light | Point Light | Spot Light | Rect Light |

Click images for full size.

### Source Angle, Radius, Height and Width

Each type of light has an option to set the angle, radius, or height and width of its light source to control the size and shape of the shadows it casts. Larger angles, radii, heights, and widths soften shadows for objects the light affects.

In the examples below, the left Spot Light has no source radius specified and produces sharp shadows. The right Spot Light has a moderate source radius specified, which softens the shadows of that light depending on the distance of the objects from it.

![source radius example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c33814fa-f722-4633-8610-df4226f64bb7/source-radius-example.png)
