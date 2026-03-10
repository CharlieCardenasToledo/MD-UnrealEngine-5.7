# Mesh Distance Fields

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine

> Application Version: 5.7

**Unreal Engine** leverages the power of **Distance Fields** to have dynamic ambient occlusion and shadowing for Static Mesh Actors in your games. In addition to that, the Mesh Distance Field representation of an Actor can be used for other features like GPU particle collision or even with the Material Editor to create dynamic flow maps and much more.

Continue reading below to learn how Mesh Distance Fields work and some of the ways you can use it in your games.

## How does it work?

To represent a Static Mesh's surfaces, a **Signed Distance Field** (SDF) is used. It works by storing the distance to the nearest surface in a volume texture. For every point on the exterior of the mesh is considered positive distance and any point inside the mesh stores a negative distance. In the example below, the positive distances are being traced and stored to represent the tree later on.

![Example of the storing distance to the nearest surface](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8ef9f5cf-b9bf-4911-8bb3-62168e2448f2/01-distance-field-positive-distance-tracing.png)

The first property of SDF that make them useful is that when tracing a ray, you can safely skip through empty space as the distance to the nearest surface is already known (this is sometimes called Sphere Tracing). This allows the intersections to be determined with a small number steps. By ray tracing a distance field, a visibility result is produced, meaning that if the ray intersects the mesh, the light will then be shadowed.

![Example of the sphere tracing principle](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/36617eb9-2551-49ff-b0c8-ff2bd40f7828/02-distance-field-sphere-tracing.png)

The second property that makes SDF useful is that when you trace a ray, by tracking the closest distance a ray passed by an occluding object, an approximate cone intersection can be computed with no extra cost. This approximation makes it possible to do very soft area shadows and sky occlusion using distance fields. This property is key to features like [Distance Field Ambient Occlusion](https://dev.epicgames.com/documentation/en-us/unreal-engine/distance-field-ambient-occlusion-in-unreal-engine) as a small number of cones can compute a soft visibility for the entire hemisphere of a receiver point.

![Example of the tracking the closest distance a ray passed by an occluding object](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a00fed3b-d268-4fd8-a1af-37f51b80896e/03-distance-field-cone-tracing.png)


You can read further about [using Distance Fields for Lighting](http://iquilezles.org/www/articles/raymarchingdf/raymarchingdf.htm) here.



## Scene Representation

Each level that you create is made up of all these Mesh Distance Fields for your placed Actors. When Mesh Distance Fields are generate, they are done so "offline" using triangle raytracing that stores the results in a volume texture. Because of this, mesh distance field generation cannot be done at runtime. This method computes the Signed Distance Field rays in all directions to find the nearest surface and stores that information.

You can visualize the Mesh Distance Fields that represent your scene by using the viewport and selecting **Show > Visualize > Mesh Distance Fields**.

|  |  |
| --- | --- |
|  |  |
| Menu to Enable Visualization | Mesh Distance Field Visualization |

Click images for full size.

When you see areas that are more white than gray, it means that many steps were needed to find the intersection of the mesh surface. Rays at grazing angles to surfaces took many more steps to intersect than would have for a simpler mesh.

### Quality

The quality of a Mesh Distance Field representation is controlled by its volume texture resolution. This can be modified using **Distance Field Resolution Scale** in the [Build Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-properties-in-unreal-engine#buildsettings) of the **Static Mesh Editor**.

Click image for full size.

The Mesh Distance Field quality will be best for levels that are built out of meshes with similar size, as large meshes tend to create errors. For example, meshes in [Fortnite](https://www.epicgames.com/fortnite) either conform to a grid or are props placed around parts of the level, which gives the best results with few errors. Landscapes are handled separately by [heightfields](https://dev.epicgames.com/documentation/en-us/unreal-engine/distance-field-ambient-occlusion-in-unreal-engine#landscapes) and are not affected by Distance Field resolution.

|  |  |  |
| --- | --- | --- |
|  |  |  |
| Original Mesh | Resolution is too low, important features are lost | Resolution has been increased, important features represented |

Click images for full size.

The resolution of your Mesh Distance Field should be adjusted enough to capture the important features. As you increase the resolution of the mesh, the memory footprint of the Mesh Distance Field will increase as well. In the Static Mesh Editor, you can see the Mesh Distance Field size listed on the top left of the Viewport.

Click image for full size.

When the Mesh Distance Field is generated, corners are rounded off based on resolution. This can be offset by increasing its resolution, but in most cases, should not be an issue depending on the complexity of the mesh. The maximum size volume texture any single mesh can have is 8 megabytes with a resolution of 128x128x128.

|  |  |  |
| --- | --- | --- |
| Rounded corners based on the resolution 1 | Rounded corners based on the resolution 2 | Rounded corners based on the resolution 3 |

For thin surfaces, they can only be represented with a negative texel inside the mesh, which is necessary for finding its root. Increasing the resolution can capture the larger detail more accurately here, but in cases where you're only using [Distance Field Ambient Occlusion](https://dev.epicgames.com/documentation/en-us/unreal-engine/distance-field-ambient-occlusion-in-unreal-engine) and the surfaces aren't represented properly. Occlusion further from the surface will be accurate, so it's often not noticeable with sky occlusion.

![Thin serfaces representation with Mesh Distance Field visualization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8bbec761-8442-4347-aed2-093ee64cc279/14-distance-field-quality-corners-4.png)

### Global Distance Field

The Global Distance Field is a low-resolution Distance Field that uses Signed Distance Fields occlusion in your levels while following the camera. It creates a cache of the per-object Mesh Distance Fields and composites them into a few volume textures centered around the camera, called clipmaps. Only newly visible areas or those affected by the scene modification need to be updated, so composition doesn't cost much.



The lower resolution of the object Distance Field means that it can be used for everything, but when computing cone traces for sky occlusion, they are sampled near the point of being shaded while the Global Distance Field is sampled further away.

You can visualize the Global Distance Field in the viewport by clicking **Show > Visualize > Global Distance Field**.

Click image for full size.

Below is a comparison of the per-object Mesh Distance Field visualization in comparison to the Global Distance Field visualization that combines them into clipmaps based on the camera view and distance.

![Mesh Distance Fields Visualization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f6e2df4f-2a01-49e6-b574-d31dd17b7f73/16-distance-field-mdf-visualization.png)

![Global Distance Fields Visualization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ddd6a294-ed01-4029-bdb1-bc089b49ae9d/17-distance-field-gdf-visualization.png)



For more information, visit the [Distance Field Ambient Occlusion](https://dev.epicgames.com/documentation/en-us/unreal-engine/distance-field-ambient-occlusion-in-unreal-engine) page.

### Foliage

Foliage assets can also leverage the Distance Fields making it possible to have dynamic occlusion or even have distance shadowing beyond what Cascaded Shadow Maps can shadow.

Below are some options you should consider when using any foliage assets in your games to get the most out of performance and quality.

#### Two-Sided Distance Field

For high-density meshes (like trees) where you have surface that are usually made up of a masked material that represents many holes for leaves or branches, these cannot adequately be represented as a solid surface. For this reason, you can enable the [Build Setting](https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-properties-in-unreal-engine#buildsettings) for **Two-Sided Distance Field Generation** in the **Static Mesh Editor**. This option will work well for foliage but does come at a higher ray marching cost.

![Enabling the Two-Sided Distance Field](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd14ec9e-8dda-4df3-854f-3ed8c11e9237/18-distance-field-two-sided-distance-field.png)
