# Volumetric Fog

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-fog-in-unreal-engine

> Application Version: 5.7

**Volumetric Fog** is an optional part of the [Exponential Height Fog](https://dev.epicgames.com/documentation/en-us/unreal-engine/exponential-height-fog-in-unreal-engine) Component. Volumetric Fog computes participating media density and lighting at every point in the camera frustum to support varying densities and any number of lights that affect the fog.

![Image](https://dev.epicgames.com/community/api/documentation/image/23acb13a-c367-4bec-ba0f-c3b9068eaa79)

_In this scene, Volumetric Fog is coming from the directional light source off screen through the arch and surrounding area to create shadowed fog._

## Volumetric Fog Controls

When setting up and adjusting Volumetric Fog, you can control it globally or locally in your scene. The global controls enable you to use the Exponential Height Fog component to control fog for the the entire scene. The local controls enable you to control fog by way of a particle system in areas where the particles can spawn.

### Global Controls

To control Volumetric Fog, you can adjust the properties in your **Exponential Height Fog** and on each **Light** to control the Light's contribution amount.

#### Exponential Height Fog

Volumetric Fog controls can be found in the **Exponential Height Fog** component under the **Volumetric Fog** section. The exponential height distribution provides a global density for Volumetric Fog.

![Volumetric Fog controls in the Exponential Height Fog Details panel](https://dev.epicgames.com/community/api/documentation/image/873ad485-040d-41af-893b-985646d89299)

| Property | Description |
| --- | --- |
| **Scattering Distribution** | This determines how directional the volumetric scattering is; a value of 0, means light scatters equally in all directions, while a value close to 1 causes scattering, predominantly in the direction of the light (you have to be looking at the light to see its scattering). |
| **Albedo** | This is the overall reflectiveness of the participating media. Clouds, fog, and mist, which are based on water particles, have an albedo close to 1. |
| **Emissive** | This is a density of light emitted by height fog. |
| **Extinction Scale** | Controls how much the participating media blocks light. |
| **View Distance** | This is the distance from the camera over which Volumetric Fog will be computed. In the created volume texture for the fog there are a limited number of Z slices depending on this distance. Increasing the distance will result in under-sampling that can cause artifacts to appear. The number of Z slices can be adjusted by using r.VolumetricFog.GridSizeZ, where higher is better quality, but will be more expensive. |
| **Start Distance** | This is the distance (in world units) from the camera from which the volumetric fog will start. |
| **Near Fade In Distance** | This is the distance over which volumetric fog will fade in from the start distance. |
| **Static Lighting Scattering Intensity** | Scales the intensity of the volumetric fog static lighting scattering. |
| **Override Light Colors with Fog Inscattering Colors** | When enabled, uses the **Fog Inscattering Color**, **Directional Inscattering Color**, and **Inscattering Texture** properties to override the light color with Volumetric Fog. |

#### Lights

Each Light's contribution amount to the scene (and whether it shadows the fog) can be controlled by adjusting the following properties on each Light's Details panel under the **Light** section.

![Volumetric Fog light properties](https://dev.epicgames.com/community/api/documentation/image/60a276d4-0082-4ce1-ae23-f914780dcba3)

| Property | Description |
| --- | --- |
| **Volumetric Scattering Intensity** | Controls how much this light will contribute to the Volumetric Fog. When set to 0, there is no contribution. |
| **Cast Volumetric Shadow** | Toggles whether or not to cast a volumetric shadow for lights contributing to Volumetric Fog. When shadow casting is enabled, Point and Spot Lights are approximately three times more expensive because they contribute to the volume textures shadowing, where as non-shadow casting lights only contribute to the fog but do not shadow. |

```json
{
  "type": "comparison_slider",
  "image_left_id": 25711182,
  "caption_left": "Volumetric Scattering Intensity: 1 (Default)",
  "image_right_id": 25711183,
  "caption_right": "Volumetric Scattering Intensity: 0",
  "image_left": {
    "id": 25711182,
    "file_name": "VolumetricFogEnabled.png",
    "file_size": 1803324,
    "content_type": "image/png",
    "created_at": "2025-06-03T17:46:01.414+00:00",
    "height": 911,
    "width": 1512,
    "storage_key": "798a236c-26d2-4723-8f1a-e5117536a21d",
    "context": "documentation"
  },
  "image_right": {
    "id": 25711183,
    "file_name": "VolumetricFogDisabled.png",
    "file_size": 1811904,
    "content_type": "image/png",
    "created_at": "2025-06-03T17:46:01.623+00:00",
    "height": 911,
    "width": 1512,
    "storage_key": "ac2c4d29-131b-449b-b444-37e4373f1adc",
    "context": "documentation"
  },
  "image_left_storage_key": "798a236c-26d2-4723-8f1a-e5117536a21d",
  "image_right_storage_key": "ac2c4d29-131b-449b-b444-37e4373f1adc",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

In this example, the Spot Light's contribution to the Volumetric Fog has been disabled by setting the **Volumetric Scattering Intensity** to 0.

### Local Controls

Materials using the **Volume** domain describe Albedo, Emissive, and Extinction for a given point in space. Albedo is in the range [0-1], while Emissive and Extinction are world space densities with
any value greater than 0.

![Volume Material example](https://dev.epicgames.com/community/api/documentation/image/7466e02f-82eb-4e21-a5bb-d1472604ffcb)

_This is an example of the simplest Volume Material for a Particle System._

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Volume materials currently only work on particles and positions inside of the particle radius will be valid, which is usually handled by a SphereMask.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

Placing a single Particle System with the material causes a sphere of density to be added to the Volumetric Fog. The effect is fully three dimensional (3D) with no billboards involved.

![Image](https://dev.epicgames.com/community/api/documentation/image/c90db40f-b5a9-4adf-812c-d180a675e71e)

Taking this approach a step further, you could use multiple spherical fog particles with noise from textures to limit fog to a certain area of your scene.

![Image](https://dev.epicgames.com/community/api/documentation/image/3312dcba-d61f-45a4-a257-4b81764402b9)

In this scene, the fog particles have populated these low-lying areas to create a localized fog effect that is shadowed using Volumetric Fog.

## Temporal Reprojection

The volume textures (voxels) used by Volumetric Fog are relatively low-resolution and aligned to the camera frustum. Volumetric Fog uses a heavy temporal reprojection filter with a different sub-voxel jitter
per frame to smooth out the aliasing. As a side-effect, fast-changing lights, like flashlights and muzzle flashes, leave lighting trails. To disable the contribution of these lights, set **Volumetric Scattering Intensity** to 0.

## Precomputed Lighting on Volumetric Fog

```json
{
  "type": "include",
  "excerpt_id": 185,
  "excerpt_assignment_id": 1332,
  "blocks": [
    {
      "type": "paragraph",
      "content": "Volumetric Lightmaps support static lighting application for Volumetric fog by having each fog voxel interpolate precomputed lighting to its position in space.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "comparison_slider",
      "image_left_id": 24487614,
      "caption_left": "Spot Light with | No Indirect Light Bounce",
      "image_right_id": 24487615,
      "caption_right": "Spot Light with | Indirect Light Bounce",
      "image_left": {
        "id": 24487614,
        "file_name": "16-volumetric-lightmaps-sl-no-bounce.png",
        "file_size": 1152489,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:02:11.919+00:00",
        "height": 1093,
        "width": 1913,
        "storage_key": "32df3761-b84a-4af5-a2c1-9020a8fa8c86",
        "context": "documentation"
      },
      "image_right": {
        "id": 24487615,
        "file_name": "17-volumetric-lightmaps-sl-indirect-bounce.png",
        "file_size": 1118785,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:02:12.286+00:00",
        "height": 1093,
        "width": 1913,
        "storage_key": "636ffe6b-8cf5-4f57-ab33-eb31c18f054e",
        "context": "documentation"
      },
      "image_left_storage_key": "32df3761-b84a-4af5-a2c1-9020a8fa8c86",
      "image_right_storage_key": "636ffe6b-8cf5-4f57-ab33-eb31c18f054e",
      "context": "documentation",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Stationary Lights have their indirect lighting stored in lightmaps, which now affects fog.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "comparison_slider",
      "image_left_id": 24487616,
      "caption_left": "Sky Light with Emissive Color",
      "image_right_id": 24487617,
      "caption_right": "Sky Light Volumetric Lightmap",
      "image_left": {
        "id": 24487616,
        "file_name": "18-volumetric-lightmaps-skylight-emissive.png",
        "file_size": 2962702,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:02:12.788+00:00",
        "height": 1093,
        "width": 1913,
        "storage_key": "993eb1e8-9e0f-4f25-90c0-4e79efae35c2",
        "context": "documentation"
      },
      "image_right": {
        "id": 24487617,
        "file_name": "19-volumetric-lightmaps-skylight-vlm.png",
        "file_size": 3210470,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:02:13.160+00:00",
        "height": 1093,
        "width": 1913,
        "storage_key": "dd619e55-78bc-4038-b8ed-d62b2e136529",
        "context": "documentation"
      },
      "image_left_storage_key": "993eb1e8-9e0f-4f25-90c0-4e79efae35c2",
      "image_right_storage_key": "dd619e55-78bc-4038-b8ed-d62b2e136529",
      "context": "documentation",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Skylights are shadowed properly, preventing indoor areas from becoming over-fogged.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "comparison_slider",
      "image_left_id": 24487619,
      "caption_left": "Indirect Lighting Cache: | Static and Emissive for Static Lighting | (Old Method)",
      "image_right_id": 24487621,
      "caption_right": "Volumetric Lightmap: | Static and Emissive for Static Lighting | (New Method)",
      "image_left": {
        "id": 24487619,
        "file_name": "20-volumetric-lightmaps-static-ilc.png",
        "file_size": 1563378,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:02:13.532+00:00",
        "height": 923,
        "width": 1510,
        "storage_key": "c5977085-71a5-4188-a43c-919c71b607d0",
        "context": "documentation"
      },
      "image_right": {
        "id": 24487621,
        "file_name": "21-volumetric-lightmaps-static-vlm.png",
        "file_size": 1562024,
        "content_type": "image/png",
        "created_at": "2025-04-10T20:02:13.752+00:00",
        "height": 923,
        "width": 1510,
        "storage_key": "26cf8090-ba13-4f19-883a-be8b3038870b",
        "context": "documentation"
      },
      "image_left_storage_key": "c5977085-71a5-4188-a43c-919c71b607d0",
      "image_right_storage_key": "26cf8090-ba13-4f19-883a-be8b3038870b",
      "context": "documentation",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Static and Emissive for Static lights affect fog without costing anything since they're all merged into the Volumetric Lightmap.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "xzZ",
  "settings": {
    "is_hidden": false
  }
}
```

## Performance

The GPU cost of Volumetric Fog is primarily controlled by the volume texture resolution, which is set from the Shadow level of the Engine Scalability. Volumetric Fog costs 1 millisecond on PlayStation 4 at **High** settings,
and 3 milliseconds on an NVIDIA 970 GTX on **Epic** settings, which has eight times more voxels to operate on.

- Particles using **Volume** domain can add a significant GPU cost, depending on their 3D overdraw and instruction count. Use the console command `profilegpu` to inspect this cost.
- Point and Spot Lights that have **Cast Volumetric Shadow** enabled, cost approximately three times more than unshadowed Point and Spot Lights.

Cloud rendering will use the expensive path when `r.PostProcessing.PropagateAlpha` is enabled and when any features, such as Exponential Height Fog, Volumetric Cloud, and Sky Atmosphere, have alpha holdout enabled.

## Currently Supported Features

This list comprises the currently supported features of Volumetric Fog:

- A single Directional Light, with shadowing from Cascaded Shadow Maps or static shadowing, with a Light Function.
- Any number of Point and Spot Lights, with dynamic or static shadowing (if **Cast Volumetric Shadowing** is enabled).
- Shadowing of Stationary Sky Lights.
- Precomputed Lighting through Volumetric Lightmaps (Direct Lighting of Static Lights, Indirect Lighting of Stationary Lights).
- A single Skylight, with shadowing from Distance Field Ambient Occlusion (if enabled).
- Particle Lights (if **Volumetric Scattering Intensity** is greater than 0).

Also, translucency is properly affected by Volumetric Fog, depending on its position in the scene. By default, translucency computes fog at vertices, so water planes with low tessellation can
introduce artifacts. These materials can be set to compute fogging per-pixel to solve this with **Compute Fog Per-Pixel** enabled in the Material Details.

## Known Issues

The following features are **not yet supported** while using Volumetric Fog:

- IES profiles and Light Functions on Point and Spot Lights.
- Shadowing from Ray Traced Distance Field Shadows.
- Shadowing from Volumetric Fog (itself).
- Source Radius on Point and Spot Lights.
- Some settings in the Exponential Height Fog, like Fog Cutoff Distance, Start Distance, and Fog Max Opacity.

### Common Questions

Below are some common questions or issues that may arise when using Volumetric Fog.

- **How can one achieve stronger light shafts without heavy global fog?** When the global density of fog is increased, you get denser fog, so you only notice light shafts (shadows of light) if the fog is dense enough to have everything heavily fogged. There are two ways to go about having stronger light shafts without heavy fog: Keep the global fog density low, but use a higher **Volumetric Scattering Intensity** for the Directional Light. Also, adjust the **Scattering Distribution** to nearly **0.9** in your Exponential Height Fog Actor. Keep the global fog density low, but increase it in certain areas with Volume particles.
- **Can Exponential Height Fog and Volumetric Fog be used at the same time?** At this time, Volumetric Fog replaces **Fog Inscattering Color** within the Volumetric Fog **View Distance**. Because Volumetric Fog is physically-based and Exponential Fog is not, it's impossible to blend the two systems in the distance for them to precisely match. This also means that some settings in the Exponential Height Fog component will have no effect on Volumetric Fog.
- **Can the Volumetric Fog's center be decoupled from the camera? This would be ideal for top-down games...** Not currently, though, a standalone volume would be ideal for this. However, it's hard to integrate them with translucency efficiently.

## Training Stream

```json
{
  "type": "external_video",
  "url": "https://www.youtube-nocookie.com/embed/N4mkgbwLg7U?feature=oembed",
  "original_url": "https://www.youtube.com/watch?v=N4mkgbwLg7U",
  "caption": "Volumetric Fog | Feature Highlight | Unreal Engine",
  "autoplay": false,
  "settings": {
    "is_hidden": false
  }
}
```
