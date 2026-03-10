# Sky Lights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/sky-lights-in-unreal-engine

> Application Version: 5.7

The Sky Light captures the distant parts of your level and applies that to the scene as a light. That means the sky's appearance and its lighting/reflections will match, even if your sky is
coming from atmosphere, or layered clouds on top of a skybox, or distant mountains. You can also manually specify a cubemap to use.

## Scene Capture

The Sky Light will only capture the scene under certain circumstances:

* For **Static Sky Lights**, updates automatically happen when building lighting.
* For **Stationary** or **Movable Sky Lights**, updates happen once on load and only updates further when **Recapture** is called unless the [**Real Time Capture**](https://dev.epicgames.com/documentation/en-us/unreal-engine/sky-lights-in-unreal-engine#realtimecapture) feature is enabled. Both are accessible via the **Details** panel, and Recapture can also be called via Blueprint in-game.

  ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d37247b4-e157-4721-b2ae-540f68bbae7d/skylight_recapture.png)

  Details panel Sky Light Recapture button

If you change the texture that the skybox is using, it will not automatically know to update. You'll be required to use one of the methods above for it to update.

A Sky Light should be used instead of the Ambient Cubemap to represent the sky's light because Sky Lights support local shadowing, which prevents indoor areas from getting lit by the sky.

## Mobility

Similarly to other [Light Types](https://dev.epicgames.com/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine), the Sky Light can be set to one of the following **Mobilities**:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5e9c79ae-2334-4289-98d0-11dfc42b9934/skylighticon.png)

| Mobility | Description |
| --- | --- |
| **Static** | Lighting cannot be changed while in game. This is the fastest method for rendering and allows for baked lighting. |
| **Stationary** | When lighting is built, shadowing and light bounces will only be captured from static geometry. All other lighting will be dynamic. This setting also allows for the light to change color, intensity, and the cubemap in-game, but it does not move and allows for partially baked lighting. |
| **Movable** | Lighting can be moved and changed in-game as needed. |

## Static Sky Light

A Sky Light set to **Static** will be baked completely into the lightmap for static objects in the level and therefore costs nothing. When edits are made to the light's properties, the changes will not be visible
until lighting has been rebuilt for the level.

When using a Static Sky Light, only Actors and Lights in the level that have their mobility set to **Static** or **Stationary** will be captured and used for lighting. Furthermore, only the emissive contribution
of Materials can be captured with a Static Sky Light in order to avoid a feedback loop. For this reason, make sure any skybox has a Material that is set to **Unlit**.

### Stationary Skylight

A Sky Light with **Stationary Mobility** gets baked shadowing from **Lightmass**. Once you place a Stationary Sky Light in your level, you have to rebuild lighting once to get the baked shadowing. You can then change the sky light as much as you want without rebuilding. The Sky Light shadowing that **Lightmass** bakes stores directional occlusion information in what is called a [**Bent Normal**](https://dev.epicgames.com/documentation/en-us/unreal-engine/sky-lights-in-unreal-engine#bentnormalforstationaryskylights).

Only components and lights with **Static** or **Stationary Mobility** will be captured and used for lighting with a Stationary Sky Light.

Like all types of **Stationary Lights**, the color of the direct lighting can be changed at runtime through **Blueprint** or **Sequencer**. However the indirect lighting is baked into the lightmap and cannot be modified at runtime. The amount of indirect lighting can be controlled by `IndirectLightingIntensity`.

![Direct Lighting Only](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2bd5fffc-2406-49c7-9d43-be57eef67eb3/0original.jpg)

![Direct Lighting and Diffuse GI computed for a Stationary Sky Light](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8f4d39d9-0cdd-47cd-b9e5-7bc1eb7ad3e4/0skylightgi.jpg)

### Movable Sky Light

A Sky Light set to **Movable** does not use any form of precomputation. It captures components and lights of any mobility when setup to capture the scene.

#### Distance Field Ambient Occlusion

This property requires that [Mesh Distance Fields](https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine) be enabled in the project settings.

Shadowing for a Movable Sky Light is provided by [Distance Field Ambient Occlusion](https://dev.epicgames.com/documentation/en-us/unreal-engine/distance-field-ambient-occlusion-in-unreal-engine) from Signed Distance Field Volumes
that are generated around each rigid object. Distance Field Ambient Occlusion supports dynamic scene changes where the rigid meshes can be moved or hidden, and it will affect the occlusion.

Click image for full size.

Check out the [How to use Distance Field Ambient Occlusion](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-distance-field-ambient-occlusion-in-unreal-engine) page for more information and examples.

## Precomputed (Static or Stationary) Sky Light

When using baked lighting with a Static or Stationary Sky Light, the lighting and shadowing data will be stored in lightmaps. The sections below discuss some of these features supported by
[Lightmass](https://dev.epicgames.com/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine).

### Improved Static Sky Light Directionality

Prior to Unreal Engine 4.18, Static Sky Lights used to be represented by Lightmass with a 3rd Order Spherical Harmonic which didn't capture the detail that could be present in a sunrise or sunset.
A filtered cubemap is used now which results in a higher resolution by default. Lightmass will also select the appropriate mip of the cubemap texture based on the size of the Final Gather rays to avoid any aliasing.

To see an example of this type of interaction, go to **Engine Content** > **MapTemplates** > **Sky** and select **SunsetAmbientCubemap** as it will show a great example.



![Third Order Spherical Harmonic | (Before) ](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/75584aa9-eeff-4d6c-94f2-f8d462ce7e52/skylight_2.png)

![Filtered Cubemap | (After)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1ae17229-7918-4bce-bba8-8ffec7d8f7ea/skylight_1.png)

The biggest difference can be seen in heavily occluded scenes with a Sky Light cubemap that has a lot of brightness and color variations.

#### Camera Obscura

With the improved directionality of Static Sky Lights, it is now possible to recreate a pinhole camera effect ([Camera Obscura](https://en.wikipedia.org/wiki/Camera_obscura)) with a small enough opening.
The smaller the opening, the more directional sky lighting will become.

|  |  |
| --- | --- |
|  |  |
| Sky Light Source Cubemap | Resulting Light Build |
| *Click image for full size.* | *Click image for full size.* |

### Bent Normal for Stationary Sky Lights

For Stationary Sky Lights, static and stationary lighting is baked separately from movable using Lightmass to store directional information in what is called a **Bent Normal**. This is
the direction from the texel to the most un-occluded source of ambient light. Areas that are mostly occluded use this direction for sky lighting instead of the surface normal, which improves quality in cracks.

![Static Sky Light Ambient Occlusion Only](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0675f32a-2b84-41c0-9fce-9129d8df0666/1skylightaoonly.png)

![Stationary Sky Light with Bent Normal](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5662c253-678a-43fa-b72d-d605df6c7554/1skylightbentnormal.png)

The first image shows Sky Light with Ambient Occlusion only. The second image shows Sky Light with Bent Normal occlusion. Notice how surfaces in cracks 'agree' on where the lighting is coming from.

For additional information visit the [Bent Normal Map](https://dev.epicgames.com/documentation/en-us/unreal-engine/bent-normal-maps-in-unreal-engine) page.

### Multiple Light Bounces

Multiple bounces of indirect light from Sky Lights is supported by adjusting the **Num Sky Lighting Bounces** setting in **World Settings** > **Lightmass**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ef1c9911-d50b-4b5c-9e34-0941be34ce3a/lightmasssettings.png)
