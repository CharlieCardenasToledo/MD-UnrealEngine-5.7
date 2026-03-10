# Per-Platform LODs

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/per-platform-lods

> Application Version: 5.7

In **Unreal Engine**, [Skeletal Mesh assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine) can be swapped out in real time, with different meshes of the same characters at different levels of detail, called [Level of Detail assets (LODs)](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-lods-in-unreal-engine). These lower resolution versions of a Skeletal Mesh are used to reduce the performance cost a character requires when they are far away from the camera, when higher detail would be hard to perceive by the player.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/88801149-f336-4bb0-9ddc-323d97076e97/lod0.png)
![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3b31229a-2d67-49fb-818b-32486cad5788/lod1.png)
![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/44c3a5e1-93b1-436f-9be9-7fe590ae892c/lod2.png)
![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7a22dbf1-dee5-4a20-b43e-b488295a64c8/lod3.png)

**Move the slider to observe the Mannequin Skeletal Mesh at LODs 0 through 3**

**LODs** usually come in ordered sets, starting with the full-resolution Skeletal Mesh being LOD 0, with each increasing LOD number being a reduction in the Meshes geometry count. Some higher number LODs can even reduce the number of bones the character's skeleton contains. The number of LODs a Character contains, and the severity of resolution steps, depends on your project's needs.

LODs can be hand authored in external **Digital Content Creation** (**DCC**) software, or generated within the engine using the [Skeletal Mesh Reduction Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-lods-in-unreal-engine#skeletalmeshreductiontool).

To read more about Skeletal Mesh LODs in Unreal Engine, refer to the following documentation:

## Per-Platform LODs

While having multiple Skeletal Mesh LODs of a character can help lessen the rendering cost, the extra memory required to store this information can be an issue on platforms that have limited resources like memory. It can be beneficial to your project's performance, across multiple platforms, to set a default LODs to be used on a per-platform basis.

The following document will provide an example workflow of how to set these default LODs to scale your project across multiple platforms.

#### Prerequisites

* Your project contains a Skeletal Mesh asset with a few LODs. If your Skeletal Mesh asset does not have any associated LODs, you can use the [Skeletal Mesh Reduction tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-lods-in-unreal-engine#skeletalmeshreductiontool) to generate a set.

### Setting Per-Platform LODs

Navigate in the **Content Browser** to your Skeletal Mesh asset that contains a set of LODs and open it in the [Skeletal Mesh Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-editor-in-unreal-engine).

You can hover your mouse over a Skeletal Mesh Asset in the **Content Browser**, to see some contextual information, including the number of LODs the Skeletal Mesh contains.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/88081ecb-d6c9-4704-8bff-a7d569e817dd/lodinfo.png)

To create a new minimum LOD default for a specified release platform, navigate in the Skeletal Mesh Editor's **Asset Details** panel under the **LOD Settings** section and add an array to the **Minimum LOD** property using (**+**) **Add** and select the platform or platform group to specify a new minimum LOD default.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a689a333-2100-4494-9a4e-658045484796/addminlod.png)
