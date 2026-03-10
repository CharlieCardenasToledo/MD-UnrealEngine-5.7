# Movable Light Mobility

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/movable-light-mobility-in-unreal-engine

> Application Version: 5.7

Lights that have their Mobility set to **Movable** are lights that can be or be changed dynamically in any way during runtime — these are sometimes called dynamic lights. Their performance cost is higher than those lights that are Static or Stationary and depend on the number of meshes affected by the light along with the triangle count of those meshes. For example, a shadow-casting dynamic light with a large radius has a higher performance cost than one with a smaller radius.

Movable light's support dynamic indirect lighting when used with [Lumen Global Illumination and Reflections](building-virtual-worlds\lighting-and-shadows\global-illumination\lumen).

Of the three light mobilities to choose from, Movable lights have varying quality (depending on the type of dynamic shadows being used), highest mutability, and highest performance cost.

## Supported Shadow Types

Movable lights support a lot more dynamic lighting and shadowing methods than Static and Stationary Lights do. The following types of shadowing are supported for lights that are Movable:

- **Shadow Maps** provide whole scene dynamic shadows. It is the standard shadowing method for all dynamic shadowing in the engine, and they work across most platforms for all light types. Shadow maps do not provide soft area shadowing, like many of the other shadowing methods in this list.
- [Virtual Shadow Maps](building-virtual-worlds\lighting-and-shadows\shadows\virtual-shadow-maps) provide consistent, high resolution shadow maps that works well with film-quality assets and large dynamically lit open worlds. They provide soft area shadowing and work well with [Nanite](designing-visuals-rendering-and-graphics\rendering-optimization\nanite), [Lumen Global Illumination and Reflections](building-virtual-worlds\lighting-and-shadows\global-illumination\lumen), and [World Partition](building-virtual-worlds\world-partition) to deliver the highest quality at a reasonable performance cost. Virtual Shadow Maps are supported on the latest console and PC platforms that support DirectX 11 or DirectX 12.
- [Ray Tracing Shadows](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-ray-tracing-in-unreal-engine) simulate soft area lighting effects for the highest shadowing quality at reasonable performance. They use the ray tracing architecture supported by NVIDIA GPU hardware running on Windows 10 (or later) with DirectX 12.
- Mesh Distance Field Shadows provide lighting effects and soft area shadowing from meshes based on a distance field representation of the mesh. This method requires the distance field meshes for the project, which is needed for software ray tracing in [Lumen Global Illumination and Reflections](building-virtual-worlds\lighting-and-shadows\global-illumination\lumen), and [Distance Field Ambient Occlusion](https://dev.epicgames.com/documentation/en-us/unreal-engine/distance-field-ambient-occlusion-in-unreal-engine).

## Shadow Biasing

The default shadow mapping techniques in Unreal Engine work across all platforms for Movable lights to provide dynamic shadowing. Shdaow mapping comes with some limitations that produce artifacts, such as faceted shadows on curved surfaces and shadow contact hardening at surface intersections that can make objects look like they are floating or not grounded in the scene.

Shadow biasing is a per-light set of properties that help reduce these types of artifacts while improving accuracy of self-shadowing and contact hardening from these light sources. These biasing settings work by finding a trade-off between balancing accuracy in one areas while reduing self-shadowing artifacts in another.

```json
{
  "type": "comparison_slider",
  "image_left_id": 25823510,
  "caption_left": "Shadow Bias (Constant and Slope): Default",
  "image_right_id": 25823511,
  "caption_right": "Shadow Bias (Constant and Slope): Adjusted",
  "image_left": {
    "id": 25823510,
    "file_name": "ShadowBias_Actor_0.png",
    "file_size": 238609,
    "content_type": "image/png",
    "created_at": "2025-07-21T13:47:46.869+00:00",
    "height": 489,
    "width": 500,
    "storage_key": "e4c8b5e5-76f0-4d9a-bb36-8ba1615fb358",
    "context": "documentation"
  },
  "image_right": {
    "id": 25823511,
    "file_name": "ShadowBias_Actor_1.png",
    "file_size": 235144,
    "content_type": "image/png",
    "created_at": "2025-07-21T13:47:46.951+00:00",
    "height": 489,
    "width": 500,
    "storage_key": "0b4ef717-0394-4c36-996b-1a496d104897",
    "context": "documentation"
  },
  "image_left_storage_key": "e4c8b5e5-76f0-4d9a-bb36-8ba1615fb358",
  "image_right_storage_key": "0b4ef717-0394-4c36-996b-1a496d104897",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Adjusting the <strong>Shadow Slope Bias</strong> reduces self-shadowing artifacts at the loss of shadow accuracy, which can cause a peter-panning (or floating) effect for grounded objects in the scene. Slope bias adjustments won't solve <em>all</em> your self-shadowing issues with dynamic lighting, but it can solve most of them. It's up to you to decide the <em>right</em> balance for your project.",
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

Directional Lights have an extra depth bias property that controls the bias strength across the Cascaded Shadow Maps (CSM). It reduces dicontinuities of shadow artifacts at cascade transition points.

```json
{
  "type": "comparison_slider",
  "image_left_id": 25823512,
  "caption_left": "Shadow Bias (Constant and Slope): Default",
  "image_right_id": 25823513,
  "caption_right": "Shadow Bias (Constant and Slope): Adjusted",
  "image_left": {
    "id": 25823512,
    "file_name": "ShadowBias_Landscape_0.png",
    "file_size": 649748,
    "content_type": "image/png",
    "created_at": "2025-07-21T13:47:47.031+00:00",
    "height": 620,
    "width": 1000,
    "storage_key": "1c9017e2-b0a7-4a89-844c-670ac92735d9",
    "context": "documentation"
  },
  "image_right": {
    "id": 25823513,
    "file_name": "ShadowBias_Landscape_1.png",
    "file_size": 650698,
    "content_type": "image/png",
    "created_at": "2025-07-21T13:47:47.136+00:00",
    "height": 620,
    "width": 1000,
    "storage_key": "f0b7cf12-eff8-434c-9eb5-33d887804240",
    "context": "documentation"
  },
  "image_left_storage_key": "1c9017e2-b0a7-4a89-844c-670ac92735d9",
  "image_right_storage_key": "f0b7cf12-eff8-434c-9eb5-33d887804240",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

The following properties are available on Lights to adjust shadow biasing:

| Property | Description |
| --- | --- |
| **Shadow Cascade Bias Distribution** | (Directional Lights Only) Controls the depth bias scaling across Cascaded Shadow Maps. It mitigates the difference in shadow artifacts between different cascade transitions. Values of 1 scales shadow bias based on each cascade's size. 0 scales shadow bias uniformly across all cascades. |
| **Shadow Bias** | Controls how accurate self shadowing of whole scene shadows are from this light source. At 0, shadows start at their shadow caster surface but there will be many artifacts. Larger values have shadows start farther from their caster and there won't be any self-shadowing artifacts, but the object may appear to float above a surface. Values around the mid-point of 0.5 is a good trade-off balance between accuracy and reduction in self-shadowing artifacts. |
| **Shadow Slope Bias** | This works in additions to Shadow Bias to control the accuracy of self-shadowing of whole scene shadows from the selected light. This property increases the amount of bias depending on the slope of a given surface. At 0, shadows start at their caster surface but will have many self-shadowing artifacts. Larger values will start shadows farther from their caster and there won't be any self-shadowing artifacts but objects might appear to float above a surface. |
| **Shadow Filter Sharpen** | Adjusts the sharpness of direct shadowing from Stationary or Movable lights. It can reduce the soft shadowing effect of shadow mapping. |

## Shadow Map Caching

Shadow map caching is a feature of Movable lights that makes shadow casting from Point and Spot Lights much more affordable in games. In Levels where you have assets that don't need to move, their shadow calculation is costing performance each frame. Shadow map caching looks at these assets that have their Mobility set to **Static** or **Stationary** and doesn't need to recalculate them each frame unless something changes with them or the light.

Shadow map caching has a significant impact on performance, especially in levels where there are a lot of assets affected by a lights.

For instance, in a moderately sized scene with three shadow-casting Movable Point lights, they could take upwards of 14 milliseconds to render shadow depths. With cached shadows enabled, those same three lights may take around 1 millisecond to render shadow depths.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Shadow map caching require memory to store the cached shadows, and for large enough scenes, you may need to adjust the amount of memory alloted to them with the console command <code>r.Shadow.WholeSceneShadowCacheMb</code>.",
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

### Shadow Map Caching Performance

You can check the performance of cached shadows by opening the stat window for shadow rendering with `Stat ShadowRendering`. Then enable/disable cached shadows with the console command `r.Shadow.WholeSceneShadows`.

|   |   |
| --- | --- |
| ![shadow map caching enabled](https://dev.epicgames.com/community/api/documentation/image/eadd7373-f5f6-42f4-a5e2-04bc9088ca96) | ![shadow map caching disabled](https://dev.epicgames.com/community/api/documentation/image/13456b88-c964-43f6-a582-21236eeb4341) |
| Shadow Map Cashing: Enabled | Shadow Map Caching: Disabled |

### Shadow Map Caching Limitations

Shadow map caching can significantly decrease the cost of using dynamic shadowing in your Levels, but there are some limitations that must be considered when using with unsupported features of the engine.

By default, caching can only happen when the following assets meets these criteria:

- Primitives in the Level must have their Mobility set to **Static** or **Stationary**.
- Materials that use **World Position Offset** will not be cached.
- **Point Lights** and **Spot Lights** are supported and must have their Mobility set to **Movable** while casting shadows.
- Lights that move around **will not** have their shadows cached.
- Materials that use animated **Tessellation** or **Pixel Depth Offset** can cause artifacts because their shadows will be cached but look incorrect with the asset.
