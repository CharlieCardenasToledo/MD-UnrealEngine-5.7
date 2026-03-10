# Lumen Technical Details

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-technical-details-in-unreal-engine

> Application Version: 5.7

Lumen uses multiple ray-tracing methods to solve Global Illumination and Reflections. Screen Traces are done first, followed by a more reliable method. Lumen supports two different ray tracing methods: Hardware Ray Tracing and Software Ray Tracing through signed distance fields. Hardware ray tracing provides higher quality and is enabled by default, but it requires dedicated video card support and is more expensive.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Lumen's Global Illumination and Reflections primary shipping target is to support large, open worlds running at 60 frames per second (FPS) on next-generation consoles. The engine's <strong>High</strong> scalability level contains settings for Lumen targeting 60 FPS.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Lumen's secondary focus is on clean indoor lighting at 30 FPS on next-generation consoles. The engine's <strong>Epic</strong> scalability level produces around 8 milliseconds (ms) on next-generation consoles for global illumination and reflections at 1080p internal resolution, relying on <a data-document-id=\"3225866\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/temporal-super-resolution-in-unreal-engine\">Temporal Super Resolution</a> to output at quality approaching native 4K.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "You can read more about Lumen performance in the <a data-document-id=\"3224919\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine?application_version=5.5\">Lumen Performance Guide</a>.",
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

## Surface Cache

Lumen generates an automatic parameterization of the nearby scene's surface called the **Surface Cache**. It is used to quickly look up lighting at ray hit points in the scene. Lumen captures the material properties for each mesh from multiple angles. These capture positions (called **Cards**) are generated offline for each mesh.

Cards can be visualized with the console command `r.Lumen.Visualize.CardPlacement 1`.

![Lumen Card Placement Visualization](https://dev.epicgames.com/community/api/documentation/image/f5ba4226-7cf8-481a-9e90-df9fcb5b8b0e)

By default, Lumen only places 12 Cards on a mesh, but you can increase that amount by setting **Max Lumen Mesh Cards** in the **Build Settings** of the Static Mesh Editor. Adjusting the number of cards is useful for more complex interiors or single meshes with irregular shapes.

![Static Mesh Editor Build Setting Max Lumen Mesh Cards](https://dev.epicgames.com/community/api/documentation/image/33d6d4f5-1ae5-4b30-b040-b8324593f559)

Areas that don't have Surface Cache coverage are colored pink in the **Surface Cache** View Mode of the Level Editor.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "These areas will not bounce light and will appear black in reflections. Issues like this can be fixed by increasing the number of Cards used with Max Lumen Mesh Cards, but that may not solve all issues. Alternatively, breaking the mesh into less complex pieces can resolve these types of issues as well.",
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

| ![View Mode Lumen Surface Cache](https://dev.epicgames.com/community/api/documentation/image/74d0f658-4aa2-40df-8121-e5b4129db93e) | ![Lumen Surface Cache Visualization Example](https://dev.epicgames.com/community/api/documentation/image/2cbe3293-27b3-4c72-878a-797d837029f1) |
| --- | --- |
| View Mode > Lumen > Surface Cache | Lumen Surface Cache Visualization of Complex Mesh |

Materials with view-dependent logic, such as Pixel Depth, Camera Position, or Camera Vector may appear incorrectly in Lumen Surface Cache view mode. Materials that use these nodes can use the **Ray Tracing Quality Switch** node to provide a version of the Material that works with Lumen Surface Cache, or to optimize Surface Cache captures for complex materials.

![ray tracing quality switch material node](https://dev.epicgames.com/community/api/documentation/image/844652e8-3300-4c48-be94-90a93d0c5580)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For more information about using the Ray Tracing Quality Switch node, see <a data-document-id=\"3225131\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.5\">Ray Tracing Performance Guide</a>.",
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

Nanite accelerates the mesh captures used to keep Surface Cache in sync with the triangle scene. High polygon meshes in particular, need to be using [Nanite](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.5) to have efficient captures. Foliage and Instanced Static Mesh Components can only be supported if the mesh is using Nanite.

After the Surface Cache is populated with material properties, Lumen calculates direct and indirect lighting for these surface positions. These updates are amortized over multiple frames, providing efficient support for many dynamic lights and multiple bounce global illumination.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Unreal Engine provides visualization modes for Surface Cache and Cards representation. See the <a data-document-id=\"3224921\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-technical-details-in-unreal-engine\">Lumen Visualization Options</a> section of this page for more details.",
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

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Only meshes with simple interiors can be supported — walls, floors, and ceilings should all be separate meshes. Importing an entire room, which includes furniture, in a single mesh is not expected to work with Lumen.",
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

## Screen Tracing

Lumen features trace rays against the screen first (called **Screen Tracing** or Screen Space Tracing), before using a more reliable method if no hit is found, or the ray passes behind a surface. Screen tracing supports any geometry type and is useful for covering up mismatches between the Lumen Scene and triangle scene.

The disadvantage in using screen traces is that they greatly limit controls for art direction, which would only apply to indirect lighting, like lighting properties for Indirect Lighting Scale or Emissive Boost. Setting a large Indirect Lighting Scale on a light will cause view-dependent global illumination, as Screen Traces cannot support it correctly.

The example scene below uses Screen Traces first before falling back to other, more costly tracing options. When disabling Screen Traces for global illumination and reflections, it is possible to see only the Lumen Scene produced by Software Ray Tracing. Screen Traces help resolve the mismatch that can happen between the triangle scene and Lumen Scene.

You can perform this type of comparison by disabling Screen Traces from the Level Viewport's **Show > Lumen** menu and removing the check next to **Screen Traces**, or disable the setting for **Screen Traces** in the **Post Process Volume** under **Lumen Global Illumination** and **Lumen Reflections** categories.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26463356,
  "caption_left": "Screen Traces Enabled | (Default)",
  "image_right_id": 26463357,
  "caption_right": "Screen Traces Disabled | Using Surface Cache",
  "image_left": {
    "id": 26463356,
    "file_name": "screen-traces-enabled.jpg",
    "file_size": 446308,
    "content_type": "image/jpeg",
    "created_at": "2026-02-24T20:07:57.454+00:00",
    "height": 858,
    "width": 1526,
    "storage_key": "b05b57b7-ede1-4aef-9f74-5f3d38e543db",
    "context": "documentation"
  },
  "image_right": {
    "id": 26463357,
    "file_name": "screen-traces-disabled.jpg",
    "file_size": 444687,
    "content_type": "image/jpeg",
    "created_at": "2026-02-24T20:07:57.634+00:00",
    "height": 858,
    "width": 1526,
    "storage_key": "d5b756ad-73af-4562-8ae5-a0761c5a7a85",
    "context": "documentation"
  },
  "image_left_storage_key": "b05b57b7-ede1-4aef-9f74-5f3d38e543db",
  "image_right_storage_key": "d5b756ad-73af-4562-8ae5-a0761c5a7a85",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

## Lumen Ray Tracing

Lumen provides two methods of ray tracing the scene: Software Ray Tracing and Hardware Ray Tracing.

- **Software Ray Tracing** uses Mesh Distance Fields to operate on the widest range of hardware and platforms but is limited in the types of geometry, materials, and workflows it can effectively use.
- **Hardware Ray Tracing** supports a larger range of geometry types for high quality by tracing against triangles and to evaluate lighting at the ray hit instead of the lower quality Surface Cache. It requires supported video cards and systems to operate.

Software Ray Tracing is the only performant option in scenes with many overlapping instances, while Hardware Ray Tracing is the only way to achieve high quality mirror reflections on surfaces.

### Software Ray Tracing

Lumen uses Software Ray Tracing against Signed Distance Fields by default. This tracing representation is supported on any hardware supporting Shader Model 6 (SM6), and only requires that **Generate Mesh Distance Fields** be enabled in the Project Settings. The renderer merges Mesh Distance Fields into a Global Distance Field to accelerate tracing. By default, Lumen traces against each mesh's distance field for the first two meters for accuracy, and the merged Global Distance Field for the rest of each ray.

Projects with extreme overlapping instances can control the method Lumen uses with the project setting **Software Ray Tracing Mode**. Lumen provides two options to choose from:

- **Detail Tracing** is the default method and involves tracing against the individual mesh's signed distance field for the highest quality. The first two meters are used for accuracy and the Global Distance Field for the rest of each ray.
- **Global Tracing** only traces against the Global Distance Field for each ray for the fastest traces.

Mesh Distance Fields are streamed in and out based on distance as the camera moves through the world. They are packed into a single atlas to allow ray tracing.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Use the command <code>r.DistanceFields.LogAtlasStats 1</code> to output mesh distance field statistics to the log.",
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

The quality of Lumen's Software Ray Tracing depends on the quality of the mesh's distance field representation. There are two visualization options, one for **Mesh DistanceFields** and the other for **Global DistanceField**. These visualization modes are found under the viewport's **Show > Visualize** menu.

![Show Visualization menu selections for Mesh Distance Fields and Global Distance Field](https://dev.epicgames.com/community/api/documentation/image/d5c40212-0a9d-4169-b80c-8afba444c44d)

| ![Lumen Scene View](https://dev.epicgames.com/community/api/documentation/image/600998d7-9750-433e-831e-b6b63a86926b) | ![Mesh Distance Field Visualization](https://dev.epicgames.com/community/api/documentation/image/e3529c42-5469-4d9d-a321-6e30be3c5521) | ![Global Distance Field Visualization](https://dev.epicgames.com/community/api/documentation/image/87383792-5f14-40e7-af7a-66a27acb7baf) |
| --- | --- | --- |
| Scene View | Mesh Distance Fields Visualization | Global Distance Field Visualization |

For some meshes, thin surfaces may not have a good distance field representation and could cause issues with light leaking. The Mesh Distance Field visualization can help you spot these types of issues.

![Image](https://dev.epicgames.com/community/api/documentation/image/126e545d-89e5-43ac-9fad-3976ec7ceb8a)

*(Left to Right) Triangle Mesh, Distance Field Resolution Scales 1.0 (Default), 1.5, 2.0*

There are two ways to go about improving a meshes distance field representation:

| ![Click image for full size.](https://dev.epicgames.com/community/api/documentation/image/0a70410f-9913-49d1-b512-e5791f2e1732) | ![Click image for full size.](https://dev.epicgames.com/community/api/documentation/image/4b794b20-48ef-47ac-a17a-a51f47f0f1bc) |
| --- | --- |
| Project Settings: Distance Field Voxel Density | Static Mesh Editor: Distance Field Resolution Scale |

- Projects can globally increase mesh distance field quality using the **Distance Field Voxel Density** found in the Project Settings.
- Increase the **Distance Field Resolution Scale** of individual meshes that need more quality from the Static Mesh Editor **Build Settings**.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Increasing Distance Field resolution or density will increase the disk size of the project.",
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

#### Limitations of Software Ray Tracing

Software Ray Tracing has some limitations relating to how you should work with it in your projects and what types of geometry and materials it currently supports.

**Geometry Limitations:**

- Only Static Meshes, Instanced Static Meshes, Hierarchical Instanced Static Meshes, and Landscape terrain are represented in the Lumen Scene.
- Foliage must be enabled with the setting **Affect Distance Field Lighting** found in the Foliage Tool settings.

**Material Limitations:**

- World Position Offset (WPO) is not supported.
- Translucent materials are added as a lumen card so they can receive diffuse global illumination when using **Hit Lighting for Reflections** with Lumen.
- Distance fields are built off of properties of the material assigned to the Static Mesh Asset rather than the override component. Overriding with a material that has a different Blend Mode or that has Two-Sided property enabled will cause a mismatch between the triangle representation and the mesh's distance field representation.

**Workflow Limitations:**

- Software Ray Tracing requires that levels be composed of modular geometry. Things like walls, floors, and ceilings should be separate meshes. Large single meshes, such as a mountain or multi-story building, will have a poor distance field representation that can cause self-occlusion artifacts to appear.
- Walls should be no thinner than 10 centimeters (cm) to avoid light leaking.
- Distance Fields cannot represent extremely thin features, or one-sided meshes seen from behind. Avoid these types of artifacts by ensuring the viewer doesn't see the triangle back faces of one-sided meshes or only use closed geometry.
- Mesh Distance Field resolution is assigned based on the imported scale of the Static Mesh. A mesh that is imported very small and then scaled up on the component **will not** have sufficient distance field resolution. Instead, set the distance field resolution from the Static Mesh Editor's Build Settings if you use scaling on placed instances in a Level.

### Hardware Ray Tracing

Hardware Ray Tracing supports a larger range of geometry types than Software Ray Tracing, in particular it supports tracing against skinned meshes. Hardware Ray Tracing also scales up better to higher qualities — it intersects against the actual triangles and has the option to evaluate lighting at the ray hit instead of the lower quality Surface Cache.

To use high quality hit lighting, the following must be enabled in the Project Settings under the **Engine > Rendering** section:

![Lumen Project Settings for High Quality](https://dev.epicgames.com/community/api/documentation/image/82ff7777-50d9-49cc-a2f9-c6a73d679e72)

- Support Hardware Ray Tracing: **Enabled**
- Use Hardware Ray Tracing when available: **Enabled**
- Ray Lighting Mode: **Hit Lighting for Reflections**

While Hardware Ray Tracing provides the highest quality of the two ray tracing methods, it also has the highest setup cost in large scenes causing tracing to become expensive with many overlapping meshes. Dynamically deforming meshes, like skinned meshes, also incur a large cost to update the Ray Tracing acceleration structures each frame, proportional to the number of skinned triangles. You can learn more about the setup and cost of Hardware Ray Tracing in the [Ray Tracing Performance Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.5).

For static meshes that have Nanite enabled, Hardware Ray Tracing mode can use the Nanite geometry or the **Fallback Mesh**. This is the mesh that is generated by **Fallback Relative Error** property to be used when the full detail mesh cannot be. These fallback meshes can be visualized in the level viewport under the **Show > Advanced > Nanite Meshes**.

Screen Traces are used to cover the mismatch between the full triangle meshes rendered by Nanite and the Fallback Mesh being ray-traced by Lumen. However, there are some cases where the mismatch is too large to be hidden. In these cases, raising the Fallback Relative Error can reduce incorrect self-intersection artifacts.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26463358,
  "caption_left": "Full-detail Triangle Mesh",
  "image_right_id": 26463359,
  "caption_right": "Nanite Generated Fallback Mesh",
  "image_left": {
    "id": 26463358,
    "file_name": "sme-naniteproxymesh1.png",
    "file_size": 1629126,
    "content_type": "image/png",
    "created_at": "2026-02-24T20:07:57.774+00:00",
    "height": 908,
    "width": 1349,
    "storage_key": "1975d312-93ee-4d4a-8aac-e510dddb36cb",
    "context": "documentation"
  },
  "image_right": {
    "id": 26463359,
    "file_name": "sme-naniteproxymesh2.png",
    "file_size": 1669041,
    "content_type": "image/png",
    "created_at": "2026-02-24T20:07:58.021+00:00",
    "height": 908,
    "width": 1349,
    "storage_key": "9a8d479c-1afd-4dd4-a3aa-c32ef5b6826d",
    "context": "documentation"
  },
  "image_left_storage_key": "1975d312-93ee-4d4a-8aac-e510dddb36cb",
  "image_right_storage_key": "9a8d479c-1afd-4dd4-a3aa-c32ef5b6826d",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

Lumen will use Hardware Ray Tracing when:

- The project has **Support Hardware Ray Tracing** and **Use Hardware Ray Tracing when available** enabled. Changing the first setting requires restarting the engine.
- The project is running on a supported operating system, RHI, and video card. Currently only the following platforms support performant Hardware Ray Tracing: Windows 10 with DirectX 12 Video cards must be NVIDIA RTX-2000 series and higher, or AMD RX 6000 series and higher. PlayStation 5 Xbox Series S / X

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "A project using Hardware Ray Tracing for Lumen may also want to fallback to Software Ray Tracing when needed, but not pay the memory costs and scene update costs of both at the same time. In these cases, you should add the following console variable to your <code>DefaultEngine.ini</code> configuration file:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "code_snippet",
      "description": "",
      "snippet_type": "cpp_programming",
      "title": "",
      "code_preview": "r.DistanceFields.SupportEvenIfHardwareRayTracingSupported=0",
      "lines_of_code": 1,
      "id": 163549,
      "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM1NDksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1NjozOCswMDowMCJ9--3e23ba2909527051ab2d84cd04490e7731dfcd60cbf962a7b1e5c14f3dfe1f0c",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "With this setting disabled, it is no longer possible to toggle <strong>Use Hardware Ray Tracing when available</strong> at runtime.",
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

## Large Worlds

Lumen Scene operates on the world around the camera, enabling large worlds and streaming. Lumen relies on Nanite's Level of Detail (LOD) and Multi-View rasterization for fast scene captures to maintain the Surface Cache, with all operations throttled to prevent hitches from occurring. Lumen does not require Nanite to operate, but Lumen's scene capturing becomes very slow in scenes with lots of high polygon meshes that have not enabled Nanite. This is especially true in scenes if the assets do not have good LODs set up for them.

Fast camera movement will cause Lumen Scene updating to fall behind where the camera is looking, causing indirect lighting to pop in as it catches up.

When Lumen is using Software Ray Tracing, Lumen Scene only covers 200 meters (m) from the camera position, but can be increased up to 800 m with the **Lumen Scene View Distance** setting in the Post Process Volume. Past the highest Lumen Scene distance, only Screen Traces are active for global illumination.

### Far Field

Lumen Hardware Ray Tracing implements **Far Field** traces, which extend Lumen Global Illumination and Reflections to one kilometer distance from the camera by default.

[Far Field](https://dev.epicgames.com/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.5) traces are enabled by the console variable `r.LumenScene.FarField=1` in the `DefaultEngine.ini` configuration file, and requires the use of [World Partition's Hierarchical Level of Detail](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition---hierarchical-level-of-detail-in-unreal-engine) (HLOD). Far Field requires the use of HLOD1 to be built.

When Far Field is enabled, it is traced beginning at the **Max Trace Distance** (default is 200m) and continues to `r.LumenScene.FarField.MaxtraceDistance` (default is 1 kilometer). Since objects can be culled from ray tracing using `r.RayTracing.Culling.Radius`, your projects will likely want the culling radius and max trace distance to match. Otherwise, the near-field (objects from the camera to the Max Trace Distance) may be culled before the far-field traversal point, which will leave a gap in coverage.

![Lumen Far Field Global Illumination and Reflections](https://dev.epicgames.com/community/api/documentation/image/79dc1285-7063-4f44-b81d-38c169c0b0cd)

_The Unreal Engine 5 technical demo "The Matrix Awakens" demonstrates large-world global illumination using Far Field traces._

## General Limitations of Lumen Features

- Lumen Global Illumination cannot be used with [Static Lighting](https://dev.epicgames.com/documentation/en-us/unreal-engine/static-light-mobility-in-unreal-engine) in lightmaps. Lumen Reflections should be extended to work with global illumination in lightmaps in a future release of Unreal Engine 5, which will provide a way to further scale up render quality for projects using Static lighting techniques.
- Lumen is **not** compatible with [Forward Shading](https://dev.epicgames.com/documentation/en-us/unreal-engine/forward-shading-renderer-in-unreal-engine).

## Lumen Platform Support

- Lumen **does not** support previous-generation consoles, such as PlayStation 4 and Xbox One.
- Projects that rely on dynamic lighting can use a combination of [Distance Field Ambient Occlusion](https://dev.epicgames.com/documentation/en-us/unreal-engine/distance-field-ambient-occlusion-in-unreal-engine) and [Screen Space Global Illumination](https://dev.epicgames.com/documentation/en-us/unreal-engine/screen-space-global-illumination-in-unreal-engine) on those platforms and legacy PC hardware.
- Lumen is developed for next-generation consoles (PlayStation 5 and Xbox Series S / X) and high-end PCs. Lumen has two ray tracing modes, each with different requirements.
- Software Ray Tracing Requirements: Video cards using DirectX 12 with support for Shader Model 6 (SM6)
- Lumen is supported on **Android Vulkan** and can be used with the Mobile Renderer. Games using dynamic lighting on mobile platforms that are not supported need to use unshadowed [Sky Light](https://dev.epicgames.com/documentation/en-us/unreal-engine/sky-lights-in-unreal-engine).
- Lumen **does not** currently support Virtual Reality (VR) systems. While VR can be supported, the high frame rates and resolutions required by VR make dynamic global illumination a poor fit.
- Hardware Ray Tracing Requirements: Windows 10 with DirectX 12, or Linux with Vulkan. Video cards must be NVIDIA RTX-2000 series or higher, or AMD RX-6000 series or higher.

## Lumen Visualization Options

Lumen provides several ways of visualizing data in the Unreal Editor that can be helpful in inspecting and troubleshooting how Lumen is lighting the scene.

The primary Lumen view modes are found in the Level Viewport under the View Modes menu:

| ![lumen viewmodes menu](https://dev.epicgames.com/community/api/documentation/image/c3eb1f74-9436-42c8-a6a5-cccca00233c1) | ![lumen overview viewmode](https://dev.epicgames.com/community/api/documentation/image/8be704a8-cbf2-48df-a66c-d948586919a7) |
| --- | --- |
| Lumen View Modes Options | Lumen Overview Visualization |

- **Overview** shows three of Lumen's visualizations as small tiles over the rendered scene.
- **Lumen Scene** shows Lumen's version of the scene, in the highest quality available: Surface Cache or Hardware Ray Tracing.
- **Geometry Normals** shows the normals of geometry making it easier to spot issues with the global distance field (for software ray tracing) or Nanite fallback meshes (for hardware ray tracing).
- **Reflection View** shows the scene as Lumen Reflections see it, including limited tracing distances used by reflections.
- **Surface Cache** is the same as Lumen Scene except that areas of meshes that were too complex to be covered are color highlighted in pink.

Additional visualizations are found in the Level Viewport's **Show > Visualize** menu.

![Show Visualization menu selections for Mesh Distance Fields and Global Distance Field](https://dev.epicgames.com/community/api/documentation/image/b5df5cae-dd99-4e45-a669-34b35429c6ee)

| ![Lumen Scene View](https://dev.epicgames.com/community/api/documentation/image/66fbc633-14db-4e01-bf58-0a6f6f607964) | ![Mesh Distance Field Visualization](https://dev.epicgames.com/community/api/documentation/image/29b00815-ebc8-430a-bff5-2424558949b7) | ![Global Distance Field Visualization](https://dev.epicgames.com/community/api/documentation/image/c4732b14-8ed5-45dc-8eca-5e9729601a44) |
| --- | --- | --- |
| Scene View | Mesh Distance Fields Visualization | Global Distance Field Visualization |

- **Mesh Distance Fields** shows the individual mesh's Signed Distance Field representations that make up the scene.
- **Global Distance Field** shows the lower detail distance field that has been merged of individual mesh distance fields. There are also some console commands you can use to visualize other data used for Lumen:
- Lumen's **Card Placement** looks at how capture positions (called **Cards**) are used in the scene. These Cards are generated offline for each mesh, and are used to capture the material properties of each mesh from multiple angles. Enable this visualization mode using `r.Lumen.Visualize.CardPlacement 1`.
- Hardware Ray Tracing uses the **Nanite Fallback Mesh**, which is generated from the **Fallback Relative Error** property of the Static Mesh Asset. The fallback mesh is used to cover mismatches between Screen Traces and the Nanite ray-traced scene in Lumen Reflections. Use **Show > Advanced > Nanite Meshes** to disable Nanite rendering and see the fallback mesh used by Lumen.

## Troubleshooting Topics

When troubleshooting any Lumen-related issues in your scene, a good place to start is with the **Lumen Overview** view mode.

Lumen Scene should match the main scene view in ways that have noticeable impact on indirect lighting. Significant pink areas in Lumen Surface Cache view mode should be solved by raising the **Max Lumen Mesh Cards** in the Static Mesh settings, or splitting the mesh into multiple parts.

![Image](https://dev.epicgames.com/community/api/documentation/image/856c8a31-0884-499a-9844-ed381868c7ba)

### Problem-Causing Meshes

In cases where you have problem-causing meshes contributing to indirect lighting, they can be removed from Lumen Scene using by using the Level instance's **Details** panel to disable one of the following:

- For **Software Ray Tracing**, unchecking the box for **Affect Distance Field Lighting** removes them.
- For **Hardware Ray Tracing**, unchecking the box for **Visible in Ray Tracing** removes them.

#### Problem: Splotchy Artifacts seen in Mirror Reflections Indoors

Splotchy artifacts seen in mirror reflections happen because Lumen uses very low quality settings to calculate multi-bounce global illumination since there is not much budget for it. In the Post Process settings, increase the **Lumen Scene Quality** to reduce artifacts.

| ![Click image for full size.](https://dev.epicgames.com/community/api/documentation/image/7bdad95d-4a1c-49bc-bd1b-2d52c7e0b6a5) | ![Click image for full size.](https://dev.epicgames.com/community/api/documentation/image/6d92b590-2353-41e8-9969-5b577bf04ab3) |
| --- | --- |
| Lumen Scene View Mode | Improved Lumen Scene Lighting Quality to 4 |

#### Problem: Small Meshes are Black in Mirror Reflections

Small meshes appear black in mirror reflections because Lumen culls small objects from Lumen Scene for performance. In the Post Process Setting, Increase the **Lumen Scene Detail** will capture smaller meshes over farther distances.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26463360,
  "caption_left": "Lumen Scene View Mode",
  "image_right_id": 26463361,
  "caption_right": "Lumen Scene Detail Increased",
  "image_left": {
    "id": 26463360,
    "file_name": "troubleshooting-topic-black-meshes-1.png",
    "file_size": 1651326,
    "content_type": "image/png",
    "created_at": "2026-02-24T20:07:58.275+00:00",
    "height": 962,
    "width": 1600,
    "storage_key": "c024c15a-10a2-4e99-bef6-9794d793ef43",
    "context": "documentation"
  },
  "image_right": {
    "id": 26463361,
    "file_name": "troubleshooting-topic-black-meshes-2.png",
    "file_size": 1859537,
    "content_type": "image/png",
    "created_at": "2026-02-24T20:07:58.558+00:00",
    "height": 962,
    "width": 1600,
    "storage_key": "89a95a37-fcab-4f12-b2d0-21225e94eae5",
    "context": "documentation"
  },
  "image_left_storage_key": "c024c15a-10a2-4e99-bef6-9794d793ef43",
  "image_right_storage_key": "89a95a37-fcab-4f12-b2d0-21225e94eae5",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

#### Problem: Sky Occlusion and Global Illumination Disappears at 200 Meters

Sky occlusion and global illumination are only maintained in Lumen Scene for the first 200 meters. In the Post Process settings, increase the **Lumen Scene View Distance** to maintain Lumen Scene over farther distances.

#### Problem: Light Leaking in Large Cave-like Areas

In cave-like, or enclosed areas, if light leaking is happening, it is because Lumen limits how far rays are traced to improve performance, but missing an occluder causes light leaking.

In the Post Process Setting, raise the **Lumen Scene Detail** and the **Max Trace Distance**.

For example, the mesh below is an enclosed box with no holes viewed from the outside.

![Image](https://dev.epicgames.com/community/api/documentation/image/a24e4f01-e0b6-46f9-8044-88c3a8170020)

Inside the box, you can see that skylighting is leaking throughout the scene.

![Image](https://dev.epicgames.com/community/api/documentation/image/14232bb4-8ee8-48e4-b8a5-af8ad0b7986e)

Raise the following values:

- Lumen Scene View Distance
- Max Trace Distance

The light leaking should now be fixed.

![Image](https://dev.epicgames.com/community/api/documentation/image/a53dd509-a164-4748-9021-7662d6213846)

#### Problem: Lighting Changes Propagate too Slowly to Global Illumination

When changing or toggling Lumen Global Illumination off, the lighting in the scene changes too slowly causing it to fade rather than quickly turn on or off.

For example, toggling the Sky Light off in the following scene, you see the lighting slowly fade out.

![Image](https://dev.epicgames.com/community/api/documentation/image/26c5cb17-2715-431c-8a9d-9d6c5e54363b)

You can improve the speed at which Lumen Global Illumination changes by increasing the Post Process Volume setting for **Final Gather Lighting Update Speed**.

Notice how the skylighting turns off more quickly than before.

![Image](https://dev.epicgames.com/community/api/documentation/image/bc4399fe-1e42-4629-abd6-ec189868d7eb)

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Remember to turn these settings back to defaults after the change to get back to cheaper lighting.",
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

#### Problem: Small Emissive Meshes Do Not Light the Scene Consistently

Small objects are culled from Lumen Scene leaving only the Screen Traces to pick up small emissive meshes. This leads to inconsistency in their lighting in the scene. Set the Level instances **Emissive Light Source** from the **Details** panel.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26463362,
  "caption_left": "Lumen Scene View Mode",
  "image_right_id": 26463363,
  "caption_right": "Emissive Light Source Property Enabled",
  "image_left": {
    "id": 26463362,
    "file_name": "troubleshooting-topic-emissive-1.png",
    "file_size": 415147,
    "content_type": "image/png",
    "created_at": "2026-02-24T20:07:58.926+00:00",
    "height": 966,
    "width": 1076,
    "storage_key": "170eb996-7bb9-49b8-b5e3-5620cb6cbd78",
    "context": "documentation"
  },
  "image_right": {
    "id": 26463363,
    "file_name": "troubleshooting-topic-emissive-2.png",
    "file_size": 556912,
    "content_type": "image/png",
    "created_at": "2026-02-24T20:07:59.294+00:00",
    "height": 965,
    "width": 1083,
    "storage_key": "764ac451-ac40-4181-abd7-2ba00d462eeb",
    "context": "documentation"
  },
  "image_left_storage_key": "170eb996-7bb9-49b8-b5e3-5620cb6cbd78",
  "image_right_storage_key": "764ac451-ac40-4181-abd7-2ba00d462eeb",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

#### Problem: Wanting Highest Quality Mirror Reflections Even if Not Performant

Lumen uses its Surface Cache for lighting reflection rays by default since it is significantly faster to render. However, lighting can be configured to evaluate at the ray hit by setting one of the following:

- In the Project Settings, set **Ray Lighting Mode** to **Hit Lighting for Reflections**.
- This changes lighting for the entire project.
- In the Post Process Volume, set **Ray Lighting Mode** to **Hit Lighting for Reflections**. Ideal for individual changes where you only need it for a single shot or viewpoint.

In the example scene below, notice how the specular highlights on the wall and stairs are missing in the reflection.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26463364,
  "caption_left": "Lumen Surface Cache",
  "image_right_id": 26463365,
  "caption_right": "Lumen Hit Lighting for Reflections",
  "image_left": {
    "id": 26463364,
    "file_name": "troubleshooting-topic-reflection-quality-1.png",
    "file_size": 1687420,
    "content_type": "image/png",
    "created_at": "2026-02-24T20:07:59.581+00:00",
    "height": 955,
    "width": 1600,
    "storage_key": "b0694fa2-fcae-479a-b95a-8cfe086691f4",
    "context": "documentation"
  },
  "image_right": {
    "id": 26463365,
    "file_name": "troubleshooting-topic-reflection-quality-2.png",
    "file_size": 1688050,
    "content_type": "image/png",
    "created_at": "2026-02-24T20:08:00.090+00:00",
    "height": 952,
    "width": 1600,
    "storage_key": "a89846c3-f55d-42e9-bb31-06a6ef6aa58e",
    "context": "documentation"
  },
  "image_left_storage_key": "b0694fa2-fcae-479a-b95a-8cfe086691f4",
  "image_right_storage_key": "a89846c3-f55d-42e9-bb31-06a6ef6aa58e",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```
