# Predefined Shapes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/predefined-shapes-in-unreal-engine

> Application Version: 5.7

You can create a new mesh using the **Create** category in **Modeling Mode**. The category provides a selection of predefined primitives to use as a starting base. To learn more about Modeling Mode and how to access it, see [Modeling Mode Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine).

## Using Predefined Shapes

You can choose between nine shapes, represented in the table below.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Box | Sphere | Cylinder | Cone | Torus |
|  |  |  |  |  |
| Arrow | Rectangle | Disc | Stairs |  |

You can select your desired shape and drag it into the scene for placement. After placing your mesh, you can still adjust the tool settings in the [Tool Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine#accessingmodelingmode) panel. Once you have your desired settings, click **Accept**.

## Tool Settings

You use the **Tool Properties** panel to control settings such as the output type, dimensions, and material.

As with other Modeling Mode tools, parameter values are remembered when reopening the tool.

### Output Type

The **Output Type** sets the type of mesh you create. You can choose between the following types:

* **Static mesh**
* **Dynamic mesh**
* **Volume**

You can update the mesh type at any stage of the modeling process by various tools, such as **Convert** and **Transfer**, found in the **Transform** category.

To learn more about these output types and asset management, refer to the [Working with Meshes](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-meshes-in-unreal-engine) documentation.

### Shape

You can adjust the dimensions and subdivisions of your mesh under the **Shape** setting. Each shape has specific options.

In addition, you can configure the PolyGroups of your new mesh using the **PolyGroup Mode** setting. The Polygroup Mode has the following grouping options:

|  |  |  |
| --- | --- | --- |
| Generate PolyGroups per Shape | Generate PolyGroups per Face | Generate PolyGroups per Quad |
| **Per Shape** | **Per Face** | **Per Quad** |
| Outputs the entire mesh as a single group. | Automatically divide the mesh into recognizable face groups. | Automatically divide the mesh into a group for each quad. |

To learn more about PolyGroups, refer to the [Understanding PolyGroups](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine) documentation.

### Positioning

You can position your mesh in your level based on your scene or the ground plane.

Choosing **On Scene** from **Target Surface** positions your mesh based on the surface normal of the geometry your cursor resides over.



If you set [Collision Presets](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-collisions-with-static-meshes-in-unreal-engine#simulatingphysicsandcollisionpresets) to **No Collision** for any object in your level, then **On Scene** will not detect the object.

Choosing **Ground Plane** positions your mesh in the level with the Z-axis set to 0.

You can adjust the pivot location to the base, top, or center. You can visualize the position of the pivot by the cursor placement, highlighted in the table below.

|  |  |  |
| --- | --- | --- |
|  |  |  |
| Base | Centered | Top |

### Material

You can select the appropriate **Material** for your mesh. You can also set the **UV Scale** and enable **Show Wireframe**.

![Applying a material to your mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc28cd8d-38f0-42ea-9903-16832b39b478/material-setting.png)
