# Environmental Light with Fog, Clouds, Sky and Atmosphere

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/environmental-light-with-fog-clouds-sky-and-atmosphere-in-unreal-engine

> Application Version: 5.7

Unreal Engine provides a set of components that allow for designers and artists to create immersive worlds with physically based lighting at large — or even small — scale while working efficiently to do so. These environment lighting components for atmosphere, clouds, fog, and lighting all work seamlessly together to create a unified experience that supports fully dynamically lit worlds.

The tools and features in this page will help you get started with creating your own worlds.

## Light Mixer

The **Light Mixer** is a dockable editor window where you can add, edit, and reference properties of Directional, Point, Spot, and Rect Lights in your Level.

For artists and designers, this window simplifies and can speed up your workflow by having them availabl and editable in one location. This includes lights that are components of scene Actors or of Blueprints. You can use Collections to organize them as well.

![Light Mixer Panel](https://dev.epicgames.com/community/api/documentation/image/c3259e7b-a916-4279-af46-c6fec7f0a48e)

For more information, see [Light Mixer](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-light-mixer-in-unreal-engine).

## Environment Light Mixer

The **Environment Light Mixer** is a dockable editor window where you can add, edit, and reference properties of environment lighting components for sky, clouds, atmosphere lights, and a sky light.

For artists and designers, this window simplifies and can speed up your workflow by having them all available in one location.

![Image](https://dev.epicgames.com/community/api/documentation/image/e73797b2-a717-49fd-bc21-8afbe14315bb)

For more information, see [Environment Light Mixer](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-light-mixer-in-unreal-engine).

## Fog Effects

Fog effects are useful for adding ambiance to the world and setting the mood for environments. This includes creating multi-layered fog for high and low-lying areas, and volumetric effects for light shafts.

![volumetric fog](https://dev.epicgames.com/community/api/documentation/image/f9a59c30-a722-455c-b7b0-bb91b2ef0665)

The [Sky Atmosphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/sky-atmosphere-component-in-unreal-engine) includes its own scattering and height fog simulation, but also works well with the Exponential Height Fog to support all types of lights in the scene.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26056452,
  "caption_left": "Sky Atmosphere's Height Fog",
  "image_right_id": 26056453,
  "caption_right": "Sky Atmosphere | with Exponential Height Fog",
  "image_left": {
    "id": 26056452,
    "file_name": "SkyAtmos_HeightFog.png",
    "file_size": 2924348,
    "content_type": "image/png",
    "created_at": "2025-09-11T19:41:26.400+00:00",
    "height": 1014,
    "width": 1916,
    "storage_key": "a338f91e-e932-4237-a251-e0980464083f",
    "context": "documentation"
  },
  "image_right": {
    "id": 26056453,
    "file_name": "ExpoHeightFog_2.png",
    "file_size": 2744450,
    "content_type": "image/png",
    "created_at": "2025-09-11T19:41:26.910+00:00",
    "height": 1014,
    "width": 1916,
    "storage_key": "3b7181ea-7a4e-4ddd-b76d-e7af6872fbd7",
    "context": "documentation"
  },
  "image_left_storage_key": "a338f91e-e932-4237-a251-e0980464083f",
  "image_right_storage_key": "3b7181ea-7a4e-4ddd-b76d-e7af6872fbd7",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

When the Project Setting **Support Sky Atmosphere Affecting Height Fog** is enabled, any contribution from Exponential Height Fog is additive. The Sky Atmosphere's height fog is applied on top of the Exponential Height Fog colors. However, should the **Fog Inscattering Color** and **Directional Inscattering Color** be set to black, the Sky Atmosphere will directly affect and influence the coloring of any Exponential Height Fog in the scene.

Additionally, you can used locally placed fog volumes to create fog effects in large or small areas of your scene. These local fog volumes support all platforms and volumetric fog effects when enabled.

![Placed Local Fog Volumes in a scene.](https://dev.epicgames.com/community/api/documentation/image/b3d45e87-3219-43da-9944-122cfed8a7df)

### Fog Effects Topics

- Related Document

- Related Document

- Related Document

## Atmosphere, Cloud, and World Lighting Effects

The lighting components for Sky Atmosphere, Volumetric Clouds, Directional Lights, and Sky Light make up the majority of your enviornment lighting. These components all work seamlessly together dynamically lit large worlds possible.

![enviornment lighting components](https://dev.epicgames.com/community/api/documentation/image/96aac395-0ff2-4910-98d5-54c128e1b86d)

In your Levels, you can use the following components:

- Up to two Directional Lights for the sun and moon, two suns, or any combination.
- A single Sky Light with optional real-time capturing.
- A Sky Atmosphere with its own height fog.
- Volumetric Clouds with or without a sky dome mesh.

With **Real Time Capture** enabled on the Sky Light, use the keyboard shortcut **Right Ctrl + L** (first Directional Light) or **Right Ctrl + Right Shift + L** (second Directional Light) in combination with moving the mouse to change lighting dynamically and see the results instantly.

[Video: 1_mranvqz3](https://dev.epicgames.com/community/api/cms/videos/1_mranvqz3/embed.html)

### Atmosphere, Clouds, and World Lighting Topics

- Related Document

- Related Document

- Related Document

- Related Document

- Related Document

### Atmosphere, Clouds, and World Lighting Properties Reference

- Related Document

- Related Document

## Material and Sparse Volume Texture Assets

- Related Document

- Related Document
