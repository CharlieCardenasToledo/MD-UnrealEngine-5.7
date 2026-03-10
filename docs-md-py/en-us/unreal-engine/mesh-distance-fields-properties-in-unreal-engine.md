# Mesh Distance Fields Properties

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-properties-in-unreal-engine

> Application Version: 5.7

The [Mesh Distance Fields](https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine) system in Unreal Engine can be used with various different systems that can be enabled or disabled. You can use these settings and properties to obtain a specific style for your Project, or use them for optimization purposes.

Below you'll find the details about the available menu systems and settings you can use that are specific to Mesh Distance Fields.

## Project Settings

The **Project Settings** panel contains the settings to enable Mesh Distance Field generation for the assets in your Project, as well as some optimization options you can enable to make the use of them more efficient in some cases.

Click **Edit** on the **Main** menu and select **Project Settings** to open it.

![Open Project Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4c66d2a8-056a-4504-9494-e7a2942e3ffe/01-mdf-properties-open-project-settings.png)

Settings for adjusting of the Mesh Distance Fields you can find by clicking  **Rendering > Software Ray Tracing**. The table below details the settings available.

Click image for full size.

| Property | Description |
| --- | --- |
| **Generate Mesh Distance Fields** | This determines whether the system will build Static Mesh Distance Fields, which can be used with Distance Field Shadows and Distance Field Ambient Occlusion. Enabling this will increase mesh build times and memory usage, and also requires you to restart the Unreal Editor for it to take effect.  If you enable the **Generate Mesh Distance Fields** setting for your project, you will still have increased memory usage even if you are not using any Distance Field rendering features on any Actors. If you disable this setting and restart the Unreal Editor, Mesh Distance Fields will no longer be loaded, and memory usage will go down. |
| **Distance Field Voxel Density** | Determines how the default scale of a mesh convert into distance field voxel dimensions. Changing this will cause all distance fields to be rebuilt. Large values can consume memory very quickly! Changing this setting requires restarting the editor. |

## Light Components

Below are the available [Mesh Distance Field](https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine) settings and properties that can be set for each [Light Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine) available.

### Directional Light

Below are the **Directional Light** settings that affect [Distance Field Shadowing](https://dev.epicgames.com/documentation/en-us/unreal-engine/distance-field-soft-shadows-in-unreal-engine).

![Directional Light settings that affect DFS](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/04fd3f89-6432-4400-b4ef-cd24fc1b61dd/03-mdf-properties-direct-light-dfs-settings.png)

| Property | Description |
| --- | --- |
| Light |  |
| **Source Angle** | This is the light source's angle in degrees and is used to support soft area shadows for dynamic shadowing methods using Distance Fields or Capsule Shadows. |
| Distance Field Shadows |  |
| **Distance Field Shadow Distance** | This is the farthest distance that will have Distance Field Shadowing. Distance Field Shadows will also cover the distance between this value and the **Dynamic Shadow Distance Movable Light** for CSM shadows. |
| **Distance Field Shadows** | This will toggle Distance Field Shadows on for the light source. |
| Distance Field Shadows Advanced Properties |  |
| **Distance Field Trace Distance** | This sets a distance in world units for how far shadows can cast from their shadow caster. When using larger values, you will increase the shadowing cost for the scene. |
| **Ray Start Offset Depth Scale** | This controls how large an offset there is for tracing shadows are from the receiving surface as the camera gets further away. This can be used to hide self-shadowing artifacts from low-resolution distance fields on large Static Meshes. |

#### Light Source Angle

The **Light Source Angle** softens or sharpens shadows based on the rotational angle of the light and the value entered. This allows for very soft shadowing to happen for points of the mesh that are farther away from the shadow receiving surface. Shadows closer to the mesh and the receiving surface will be sharper.

![Light Source Angle: | 1 (Default)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/72c3a34a-5f31-4c27-a0f3-c2ff7c1c8aa6/04-mdf-properties-source-angle-1.png)

![Light Source Angle: | 2](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8cd71cdd-501f-40bf-b09e-9d1aa474d10c/05-mdf-properties-source-angle-2.png)

The further the shadows stretch away from the mesh, or the farther that they are from the shadow receiving surface, the softer the shadow will become.

#### Cascaded Shadow Maps VS Distance Field Shadows

**Cascaded Shadow Maps** provide very detailed shadowing, but don't work well across extended view distances. **Distance Field Shadows** can cast shadow over a much greater distance more efficiently, but its quality relies heavily on the resolution of the volume texture generated for the Mesh Distance Field. [Mesh Distance Field quality](https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine#quality) may require a higher resolution to capture important details that would normally show up with shadow mapping. For this reason, it is recommended to use a combination of Cascaded Shadow Maps for areas close to the camera, and Distance Field Shadowing for farther distances.

![Cascaded Shadow Maps](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c9ab2730-8012-4c15-b699-66698cf5c35f/06-mdf-properties-cascaded-shadow-maps.png)

![Distance Field Shadows](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/45cd30f2-704e-4515-9b31-9e5e1c860082/07-mdf-properties-distance-field-shadow.png)

Despite the distance of all points of the lift from the ground, the shadow remains crisp and detailed when using Cascaded Shadow Mapping. Distance Field Shadows allow for softening of the shadow, based on the **Light Source Radius** and the distance of the shadow being cast from the surface, which provides a natural look.

#### Distance Field Trace Distance

The **Distance Field Trace Distance** controls how far Distance Field Shadowing can extend for any mesh that is casting shadows. Because shadows can extend along receiving surfaces for very long distances, this can cause Distance Field Shadows to increase performance cost for densely populated scenes. Lowering the Distance Field Trace Distance limits how far any one point of the Distance Field Shadow can be cast from a particular mesh without using a shorter **Distance Field Shadow Distance**.

![Distance Field Trace Distance: | 10000 (Default)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fd2eb9cc-54a7-478d-a4f7-0921eeabab86/08-mdf-properties-distance-trace-10k.png)

![Distance Field Trace Distance: | 5000](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/10f18c12-62ba-41f7-8fa3-c4f15c96acfa/09-mdf-properties-distance-trace-1k.png)

In this example, a very tall tree is being lit by a Directional Light with a shallow angle (like at sunrise or sunset). Lowering the Distance Field Trace Distance limits the top of the tree from casting indefinitely.

### Point/Spot Light

Below are the **Point** and **Spot Light** settings that affect [Distance Field Shadowing](https://dev.epicgames.com/documentation/en-us/unreal-engine/distance-field-soft-shadows-in-unreal-engine).

![Point and Spot Light settings that affect DFS](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/847626d6-7564-424a-9af0-792145581997/10-mdf-properties-point-spot-light.png)
