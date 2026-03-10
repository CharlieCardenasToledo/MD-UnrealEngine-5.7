# Nanite Technical Details

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-technical-details

> Application Version: 5.7

This page provides deeper understanding and usage examples of Nanite's geometry system.

## Nanite Fallback Mesh and Precision Settings

Static and skeletal meshes include additional properties that control the precision of the Nanite representation and its fallback mesh generated from the originally imported source mesh.

These settings are located in the mesh asset’s editor in the **Details** panel under the **Nanite Settings** section.

![Image](https://dev.epicgames.com/community/api/documentation/image/6a2b8060-2583-4f8a-8c83-b001a435b3b3)

_Nanite Mesh Editor Settings_

| Property | Description |
| --- | --- |
| Enable Nanite Support | Enables this mesh to be used with Nanite and to generate a fallback mesh in situations where Nanite cannot be used. |
| Preserve Area | Enables Nanite meshes that would lose surface area due to simplification to redistribute that lost area to the remaining triangles by dilating out the open boundary edges. This is most useful for foliage where leaves tend to become disjoint triangles and quads through simplification. The effect of this setting is to scale each leaf up. For geometry ribbons, like blades of grass, it has the effect of thickening them. This setting should be enabled on all foliage meshes and nothing else. |
| Explicit Tangents | When true, the original model tangents are stored and used per asset. This setting means tangents are stored explicitly on disk instead of being derived implicitly at runtime. The Tangent Precision setting becomes available for additional control of vertex tangents. Enabling the setting increases storage by roughly 10% but can be preferable when implicit tangents are not precise enough. |
| Lerp UVs | Whether to interpolate UVs when simplifying. This should be enabled whenever possible. For real UV coordinates, this enables calculating the lowest-error optimal UVs for new vertices when simplifying, assuming the UVs are used as normal texture coordinates and will interpolate across the face of the triangles. This should be disabled if data stored in the UVs isn't valid to interpolate. For example, if indexes are stored in UVs, lerping an index doesn't make sense and will break the shader trying to use it. If disabled, error from UVs is no longer accounted for when Nanite selects the LOD to render because error due to arbitrary vertex attributes that aren't interpolatable can't be generally reasoned about. |
| Position Precision | Choose the precision this mesh should use when generating the vertex positions of a Nanite mesh. Automatically determines the appropriate precision based on the size of the mesh. The precision can be overridden to improve precision or optimize disk footprint. |
| Normal Precision | Choose the precision this mesh should use when generating the vertex normals of a Nanite mesh. Automatically determines the appropriate precision based on the size of the mesh. The precision can be overridden to improve precision or optimize disk footprint. |
| Minimum Residency (Root Geometry) | Sets the memory byte size this mesh should always keep in memory and has the rest streamed in. Higher values require more memory, but for some meshes, this can mitigate streaming pop-in issues from occurring. |
| Keep Triangle Percent | The percentage of triangles to keep from the source mesh. Reduce this percentage to optimize disk size. |
| Trim Relative Error | Sets the maximum amount of relative error that can be removed for the Nanite mesh. All detail in the source mesh with less visual impact than this relative error amount is removed. The relative error does not have a unit size and is relative to the size of the mesh. By default, Nanite stores all of the original source mesh's triangles. |
| Fallback Target | Determine which targeting system to use when generating a fallback mesh. Auto: Automatically create a fallback mesh based on project settings. Fallback Triangle Percent: Sets the percentage of triangles that remain when reducing the source mesh for Nanite. Fallback Relative Error: Reduce until the specified error is reached relative to the mesh size. All detail in the generated fallback mesh with less visual impact than this relative error amount is removed. |
| Source Import Filename | The file path used to import a high-resolution mesh for use with Nanite. The high-resolution version of the mesh is used in place of LOD0 by systems that can benefit from more detailed geometry, such as Nanite and Geometry Modeling in Unreal Engine. |
| Displacement UV Channel | UV channel to use when sampling displacement maps. |
| Displacement Maps | Add and edit displacement maps. |
| Max Edge Length Factor | Controls the maximum distance allowed between each vertex of the mesh on screen. This can be used to prevent over-simplification of meshes that are intended to be deformed, such as animation using world position offset, and spline meshes. This should be left at 0 by default unless explicitly needed to fix issues caused by over-simplification. |

### Vertex Precision

Nanite quantizes mesh vertex positions to maximize memory density and minimize disk footprint. The quantization step size is a power of two that can be selected to match the requirements of individual meshes using the Position Precision property. By default, Auto picks the appropriate precision based on the size of the mesh and its triangle density. You can manually override by selecting a precision size to improve precision or optimize disk footprint.

![Image](https://dev.epicgames.com/community/api/documentation/image/df9b78ec-a0ed-4cc4-b919-1b9d07f77225)

_Vertex Position Precision Options_

Quantization is a form of lossy compression. Lossy compression is particularly challenging when working with modular mesh pieces or other meshes that have shared boundaries, especially when those boundaries need to align perfectly to not introduce holes or cracks in the geometry.

To ensure consistency, quantization happens in unnormalized object coordinates centered around the mesh origin. This ensures that the quantization never causes cracks when the mesh uses the same precision setting, and the translation between the mesh center is a multiple of that precision.

### Trimming Mesh Data

There are times when you’ll need to reduce the amount of data that Nanite stores in order to optimize for disk size. Nanite includes settings which provide a way for you to trim the detail data from a stored Nanite mesh at any point during production. This means you can safely overshoot quality up front and adjust accordingly later on to fit the size budget of the project and its platform targets.

Trimming Nanite’s detail data is like having a pre-decimate option before being stored as a Nanite mesh. In Nanite’s case, detail doesn’t need to be uniform across the mesh, as it removes the least significant data first and is more akin to lossy compression.

To trim detail data, you can adjust the following settings:

- Keep Triangle Percent sets the percentage of triangles to keep from the original source (full detail) mesh.
- Trim Relative Error sets the maximum amount of relative error that is allowed when trimming the data from the source mesh. Any triangle that, if removed, would incur a relative error less than this amount is removed.

The defaults for both of these properties are that nothing is trimmed by default, having Nanite store all of the original source mesh’s triangles. This is why it’s important to trim data to reduce disk size (in other words, download size), not specifically for improving performance.

For more detailed information on this aspect, see [Data Size](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-technical-details) below.

### Fallback Mesh

Many parts of Unreal Engine need access to the vertex buffer provided by traditionally-rendered meshes. When you enable Nanite for a static mesh, it generates a coarse representation, the fallback mesh, of the highly detailed mesh. The fallback mesh is used when Nanite rendering is not supported. It is also used when it wouldn't be ideal to use the full-detail mesh, like when a complex collision is needed, using lightmaps for baked lighting, and for hardware ray tracing reflections with Lumen.

The **Fallback Triangle Percent** property represents the percentage of triangles from the original source mesh that are used to generate the Fallback Mesh. You can specify the percentage of triangles to keep between 0 and 100 percent, where large percentages keep more of the original mesh's detail.

The **Fallback Relative Error** property sets the maximum amount of relative error that is acceptable when removing details from the source mesh. Any triangles whose removal incurs less relative error than this amount are removed, with detail of less visual impact removed first. The relative error does not have a unit size and is relative to the size of the mesh.

For example, if you wanted your mesh without any decimation (removal of triangles), you would use a Fallback Triangle Percentage of 100 and a Fallback Relative Error of 0.

The comparison below shows the highly-detailed Nanite mesh based on the original source mesh versus the generated Fallback Mesh using default settings.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26376695,
  "caption_left": "High Poly Nanite Mesh",
  "image_right_id": 26376696,
  "caption_right": "Nanite-generated Fallback mesh with Default Settings",
  "image_left": {
    "id": 26376695,
    "file_name": "unnamed (5).png",
    "file_size": 1917192,
    "content_type": "image/png",
    "created_at": "2026-01-11T19:00:17.363+00:00",
    "height": 1055,
    "width": 1600,
    "storage_key": "d4876de2-beb3-4664-a8a2-3398d47c14e5",
    "context": "documentation"
  },
  "image_right": {
    "id": 26376696,
    "file_name": "unnamed (6).png",
    "file_size": 1819009,
    "content_type": "image/png",
    "created_at": "2026-01-11T19:00:20.388+00:00",
    "height": 1055,
    "width": 1600,
    "storage_key": "bb97055f-6045-4bc0-9df1-85b71c1aeced",
    "context": "documentation"
  },
  "image_left_storage_key": "d4876de2-beb3-4664-a8a2-3398d47c14e5",
  "image_right_storage_key": "bb97055f-6045-4bc0-9df1-85b71c1aeced",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

Use the Fallback Relative Error value to specify how much of the original detail is retained from the source mesh, and the Fallback Percentage value to set how much of that detail is used.

The comparison below shows the fallback mesh with properties reflecting changes to the Fallback Triangle Percent and Fallback Relative Error properties to retain more of the original source mesh’s triangles. When adjusting these values, use the Nanite details for **Nanite Triangles** in the viewport as an indicator of how many triangles the fallback mesh has.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26376697,
  "caption_left": "Nanite-generated Fallback Mesh with Default Settings",
  "image_right_id": 26376698,
  "caption_right": "",
  "image_left": {
    "id": 26376697,
    "file_name": "unnamed (6).png",
    "file_size": 1819009,
    "content_type": "image/png",
    "created_at": "2026-01-11T19:02:53.400+00:00",
    "height": 1055,
    "width": 1600,
    "storage_key": "8541e722-7b76-4be2-b56f-c33223832c9a",
    "context": "documentation"
  },
  "image_right": {
    "id": 26376698,
    "file_name": "unnamed (7).png",
    "file_size": 1904393,
    "content_type": "image/png",
    "created_at": "2026-01-11T19:03:35.454+00:00",
    "height": 1055,
    "width": 1600,
    "storage_key": "efc30caa-11ba-475d-a3c5-f2e2f5d01a31",
    "context": "documentation"
  },
  "image_left_storage_key": "8541e722-7b76-4be2-b56f-c33223832c9a",
  "image_right_storage_key": "efc30caa-11ba-475d-a3c5-f2e2f5d01a31",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

#### Fallback Mesh Visualization

In the Static Mesh editor, you can toggle between the fully detailed Nanite mesh and the Nanite fallback mesh using the viewports Nanite Fallback option in the Show dropdown menu. Alternatively, you can use the hotkey Ctrl + N to quickly toggle between the two visualization options.

![Image](https://dev.epicgames.com/community/api/documentation/image/10642ce5-55b6-4957-86df-dcb183b62dd8)

#### Using Custom Fallback Mesh LODs for Nanite-enabled Meshes

The fallback mesh is used for engine features, such as complex per-poly collision, ray tracing, light baking, and so on. It is also used for platforms that do not support Nanite. When generating the fallback mesh, a Nanite-enabled mesh always uses the LOD0 slot of the source mesh for auto-generating the fallback mesh. However, there are times when it is desirable to use a manually specified fallback mesh, or a series of traditional LODs, rather than an auto-generated one.

This level of control would allow you to use Nanite in a project but also directly control the geometry seen in ray-traced reflections, or on platforms that do not support Nanite.

Follow the steps below to specify your own custom fallback mesh, or to use a series of LODs:

1. Set the Fallback Triangle Percent to 0 so that the fallback mesh is as small as possible since it will be ignored when using this approach.
2. Add one or more LODs to the mesh using this traditional LOD setup procedure.
3. Use the LOD Import dropdown to Import LOD Level 1 from the LOD Settings section.
4. Set the Minimum LOD to 1 under the LOD Settings section. This causes the Nanite-generated fallback mesh to be ignored.

Complex collision presents a special case. Use the LOD for the Collision property under General Settings to specify which LOD should be used for collision. Any LOD can be used for collision, including LOD0.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "This particular approach may not be feasible to make Nanite projects automatically compatible with non-Nanite-supporting platforms and should be tested and evaluated for your project specifically.",
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

Nanite efficiently handles very large numbers of instances, but if Nanite is disabled, there could be an overwhelming number of draw calls for the traditional render pipeline. You can feasibly test this in your own project using r.Nanite 0 to toggle Nanite off and on.

See the Console Variables and Commands section of this page for more information.

## Data Size

One could assume that because Nanite has the ability to achieve micro detail, it means a large increase in geometry data, ultimately resulting in larger game packages and download sizes for players. Nanite’s mesh format is significantly smaller than the standard static mesh format because of its specialized encoding.

For example, using the Unreal Engine 5 sample Valley of the Ancients, Nanite meshes average 14.4 bytes per input triangle. This means an average one million triangle Nanite mesh will be ~13.8 megabytes (MB) on disk.

When comparing a traditional low poly mesh plus its Normal map to a high poly Nanite mesh, you would see something like:

```json
{
  "type": "comparison_slider",
  "image_left_id": 26376700,
  "caption_left": "Low Polygon Static Mesh with a 4k Normal Map",
  "image_right_id": 26376701,
  "caption_right": "High Polygon Static Mesh with 4k Normal Map",
  "image_left": {
    "id": 26376700,
    "file_name": "unnamed (8).png",
    "file_size": 1913853,
    "content_type": "image/png",
    "created_at": "2026-01-11T19:09:17.492+00:00",
    "height": 742,
    "width": 1600,
    "storage_key": "af7e9cdf-71a4-4b84-8a39-936b42868acf",
    "context": "documentation"
  },
  "image_right": {
    "id": 26376701,
    "file_name": "unnamed (9).png",
    "file_size": 1905954,
    "content_type": "image/png",
    "created_at": "2026-01-11T19:09:20.150+00:00",
    "height": 742,
    "width": 1600,
    "storage_key": "3080cf6e-4189-4cbf-99d8-eef4995d4d45",
    "context": "documentation"
  },
  "image_left_storage_key": "af7e9cdf-71a4-4b84-8a39-936b42868acf",
  "image_right_storage_key": "3080cf6e-4189-4cbf-99d8-eef4995d4d45",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

| Low Polygon mesh | High Polygon Mesh |
| --- | --- |
| Triangles: 19,066 Vertices: 10,930 Num LODs: 4 Nanite: Disabled Static mesh compressed package size: 1.34MB | Triangles: 1,545,338 Vertices: 793,330 Num LODs: n/a Nanite: Enabled Static mesh compressed package size: 19.64MB |

However, the compressed package size isn't the entire size of the asset. There are also unique textures only used by this mesh that have to be accounted for. Many of the materials used by meshes have their own unique textures made up of different Normal, BaseColor, Metallic, Specular, Roughness, and Mask textures.

This particular asset only uses two textures (BaseColor and Normal) and thus is not as costly on disk space as one with many other unique textures. For example, note the size of the Nanite mesh with ~1.5 million triangles is smaller in size (at 19.64MB) than a 4k normal map texture.

| Texture Type | Texture Size | Size on Disk |
| --- | --- | --- |
| BaseColor | 4k x 4k | 8.2MB |
| Normal | 4k x 4k | 21.85MB |

The total compressed package size for this mesh and its textures is:

- Low-polygon mesh: 31.04MB
- High-polygon mesh: 49.69MB

Because the Nanite mesh is very detailed already, replacing the unique normal map with a tiling detail map that is shared with other assets is a good approach to reduce texture sizes. This can result in some visual loss in quality, but it’s smaller than the difference in quality between the low poly and high poly meshes. A 1.5 million triangle Nanite mesh can both look better and be smaller than a low poly mesh with a 4k normal map texture when taking this into consideration.

Total compressed package size for the Nanite-enabled mesh and textures: 27.83 MB

```json
{
  "type": "comparison_slider",
  "image_left_id": 26376702,
  "caption_left": "High Polygon Static Mesh with 4K Normal Map",
  "image_right_id": 26376703,
  "caption_right": "Nanite Mesh with 4K \"Detail\" Normal Map",
  "image_left": {
    "id": 26376702,
    "file_name": "unnamed (10).png",
    "file_size": 1905954,
    "content_type": "image/png",
    "created_at": "2026-01-11T19:46:12.929+00:00",
    "height": 742,
    "width": 1600,
    "storage_key": "0d5a7575-7e2c-4835-ad84-b2a922104c1b",
    "context": "documentation"
  },
  "image_right": {
    "id": 26376703,
    "file_name": "unnamed (11).png",
    "file_size": 1897524,
    "content_type": "image/png",
    "created_at": "2026-01-11T19:46:39.748+00:00",
    "height": 742,
    "width": 1600,
    "storage_key": "8bd549c7-87e6-434a-9413-89dace61eb42",
    "context": "documentation"
  },
  "image_left_storage_key": "0d5a7575-7e2c-4835-ad84-b2a922104c1b",
  "image_right_storage_key": "8bd549c7-87e6-434a-9413-89dace61eb42",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can try plenty of experiments with texture resolution and \"detail\" normal maps, and this particular comparison demonstrates that the data sizes of Nanite meshes are not too dissimilar from data that artists are already familiar with. ",
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

Lastly, we can compare the Nanite compression to the standard static mesh format using the high poly, where both are identical at LOD0.

| High Polygon Static Mesh | Nanite Static Mesh |
| --- | --- |
| Triangles: 1,545,338 Vertices: 793,330 Num LODs: 4 Nanite: Disabled Static mesh compressed package size: 148.95MB | Triangles: 1,545,338 Vertices: 793,330 Num LODs: n/a Nanite: Enabled Static mesh compressed package size: 19.64MB |

Comparing the Nanite compression from earlier with a size of 19.64MB is 7.6x smaller than the standard static mesh compression with 4 LODs.

### General Advice on Data Size

Nanite and [Virtual Texturing](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-texturing-in-unreal-engine) systems, coupled with fast SSDs, have lessened concern over runtime budgets of geometry and textures. The biggest bottleneck now is how to deliver this data to the user.

Data size on disk is an important factor when considering how content is delivered — on physical media or downloaded over the internet — and compression technology can only do so much. The average end user's internet bandwidth, optical media sizes, and hard drive sizes have not scaled at the same rate as hard drive bandwidth and access latency, GPU compute power, and software technology like Nanite. Pushing that data to users is proving challenging.

Rendering highly detailed meshes efficiently is less of a concern with Nanite, but storage of its data on disk is what must be kept in check.

## Visualization Modes

Nanite includes a number of visualization modes to inspect its data in the current scene.

In the Level viewport under the View Modes dropdown, hover over Nanite Visualization and choose from the selection.

![Image](https://dev.epicgames.com/community/api/documentation/image/e9f980b7-e665-4645-aba4-1010ca3d7cf7)

The Overview visualization displays the rendered scene in the center of the image with select Nanite visualizations around the screen for reference.

![Image](https://dev.epicgames.com/community/api/documentation/image/228d863d-f3b5-4e38-9f87-46a3c77dce3a)

The following Nanite visualization modes are available to choose from:

| Nanite Vir |   |
| --- | --- |
| Mask | Visualization that marks Nanite (green) and Non-Nanite (red) geometry. |
| Triangles | Display all triangles of the Nanite meshes in the current scene. |
| Patches | Display all patches of the Nanite meshes in the current scene. |
| Clusters | Display colored representations of all grouping of triangles rendered in the current scene view. |
| Primitives | Visualization that colors components all the same color for all instances in an instance static mesh (ISM). |
| Instances | Visualization that applies a different color for each instance in the scene. |
| Overdraw | Displays the amount of overdraw happening for scene geometry. All evaluated pixels, including masked-out pixels, are added to the overdraw view. Smaller objects that are closely stacked together create more overdraw than larger ones. |
| Lightmap UV | Visualization that displays the UV coordinates of Nanite mesh surfaces.Visualization that displays the UV coordinates of Nanite mesh surfaces. |
| Evaluate WPO | Colors Nanite-enabled geometry that are using world position offset (green) versus ones that are not (red). |
| Pixel Programmable |   |
| Tessellation | Visualization for Nanite mesh using tessellation and amount of tessellation happening on only tessellated meshes. |
| Raster Bins | Displays groups that represent batches of geometry. |
| Shading Bins |   |

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Nanite includes an Advanced visualizations mode that enables additional visualization options in the Nanite Visualization menu. These visualizations are useful for programmers who are debugging or profiling various low-level aspects of Nanite.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Enable this advanced visualization mode with the console variable <code class=\"inline-code\">r.Nanite.Visualize.Advanced 1</code>.\n\n",
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

## Console Variables and Commands

The following stats and console variables are available for use in debugging and configuring Nanite.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "  Nanite rendering can be enabled and disabled globally at runtime using the console variable<code class=\"inline-code\"> r.Nanite 0</code>. Disabling Nanite is a good way to emulate platforms where it is not supported.",
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

### Nanite Fallback Rendering Modes

Nanite provides fallback mesh rendering modes when Nanite is either disabled or unsupported by a platform. You can control which mode is used with the console variable r.Nanite.ProxyRenderMode.

- **0** is the default mode and falls back to rendering fallback meshes, or screen space-driven LODs if set. This includes the recognition of Min LOD in the Static Mesh Editor properties (described in the Fallback Mesh section above).
- **1** disables all rendering of Nanite-enabled meshes.
- **2** works similarly to mode 1 but allows the Show > Nanite Fallback visualization in the Static Mesh Editor to render a Nanite fallback.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The fallback render modes 1 and 2 are useful for scenes that have far more instances than could possibly be supported without Nanite. They provide a way to open the scene in the editor on non-Nanite-supporting platforms.",
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

For example, in the Unreal Engine 5 Valley of the Ancients sample project, disabling Nanite would cause there to be tens of thousands of regular draw calls to happen, making it difficult to open the map on a non-supporting platform.

### Nanite Stats Command

The command `NaniteStats` adds an overlay of Nanite culling statistics to the top-right of the viewport.

![Image](https://dev.epicgames.com/community/api/documentation/image/15f01c55-5616-4fcc-9b3b-615994e29476)

_NaniteStats display on screen._

Command arguments are used to specify what stats Nanite displays on the screen. When no argument is provided, the primary view is used.

Use NaniteStats List to show all available views in the debug output:

- Primary
- VirtualShadowMaps
- ShadowAtlas (only when available)
- CubemapShadows (only when available)

Select a view by entering the command followed by the stat list name you want to view. For example, enter `NaniteStats VirtualShadowMaps`.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For views that use two-pass occlusion culling, the statistics are split into separate buckets for Main and Post pass.",
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

### Resizing the Nanite Streaming Pool Size

Control the amount of memory dedicated to holding Nanite streaming data with the console variable `r.Nanite.Streaming.StreamingPoolSize`. Using larger pools reduces IO and decompression work when moving around the scene but at the cost of a larger memory footprint.

If the pool is not large enough to fit all the data needed for a view, cache thrashing can occur where streaming never settles even for a static view.

To visualize Nanite streaming data, you can use the **Streaming Geometry** show flag, **Show > Nanite > Streaming Geometry**. When disabled, Nanite meshes are only rendered at the quality level that is always resident in memory.

### Setting Maximum Clusters in a Single Pass

You can specify the maximum number of candidate and visible clusters used in a single pass with the console variable `r.Nanite.MaxCandidateClusters` and `r.Nanite.MaxVisibleClusters`. Their values are used for sizing intermediate buffers and their default values have been chosen to work for common rendering scenarios.

There is no mechanism for dynamically resizing either of these buffers, or automatically scaling down quality on overflow, which can result in rendering artifacts from them being too small for scene complexity, and typically manifesting as missing or blinking geometry. When these types of artifacts occur, use NaniteStats to determine conservative bounds for candidates and visible clusters. More specifically, look at the stats for ClustersSW and ClustersHW. The memory cost of a candidate cluster is currently 12 bytes and a visible cluster is 16 bytes.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "  This console variable cannot be changed at runtime and must be specified in a configuration (.ini) file.",
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
