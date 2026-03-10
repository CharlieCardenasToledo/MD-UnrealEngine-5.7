# Skeletal Mesh LODs

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-lods-in-unreal-engine

> Application Version: 5.7

In **Unreal Engine**, you can generate Skeletal Mesh [LOD (Level of Detail)](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-and-using-lods-in-unreal-engine) model variants to optimize gameplay. In the following document you can read about using the LOD generation tool and the **Skeletal Mesh Reduction Tool** features to tweak the LOD generation to retain details and more precisely optimize **Skeletal Meshes**.

#### Prerequisites

* Your project contains a [Skeletal Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine).
* Your project has the Skeletal Mesh Reduction Plugin enabled.

First open in the **Project Settings** window by clicking **Edit > Project Settings** in the **Menu Bar**. In the Project Settings window, navigate to the **Skeletal Mesh Reduction Simplification** category and ensure the **Skeletal Mesh Reduction Plugin** property is set to **SkeletalMeshReduction**.

![skeletal mesh simplification plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5cd1d1c0-3d10-4928-9a0b-aceeec5a2675/plugin.png)

## Creating LODs

With your Skeletal Mesh, you can use the LOD Generation tool to create LOD variants of the model for use in your project.

In some cases, LODs for a Skeletal Mesh are created in an external DCC (digital content creation) software. The Skeletal Mesh Reduction Tool can be used in cases where externally created LODs are present, but any regenerated LOD will overwrite any existing LOD, even LODs imported from an external source.

### Generate LODs

First, open the Skeletal Mesh you wish to generate LODs for. In the **Asset Details** panel of the [Skeletal Mesh Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-editor-in-unreal-engine), navigate to the **LOD Settings** section.

With the **Number of LODs**  property you can define how many LODs you wish to generate.

Generating 4 LODs, would result in a total of 4 LODs for the Character. LOD 0 being the highest quality Mesh imported into Unreal Engine. Beginning with LOD 1, each increasing LOD is a step down in quality for the Skeletal Mesh, with LOD 3 being the lowest quality mesh.

Click **Apply Changes** to generate the new LODs for your Skeletal Mesh.

![define the number of lods and select apply changes to generate lods](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/46c0a18a-b1cf-4822-a180-3fd805750060/createlods.png)

You will be prompted to select a location to save a LODSettings file, this can be saved in the same location as your Skeletal Mesh and any related files.

The generated LODs will now be visible in the LOD menu option within the Viewport.

![lod 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/358ad7b0-45b7-4002-9d49-3e332cec6319/lod0.png)
![lod 1](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3fa5ea1e-0c53-45c7-a1fa-13afcf580e5c/lod1.png)
![lod 2](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8a6f470-deb2-4af9-8969-a9850c12864f/lod2.png)
![lod 3](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/266b9996-f927-4677-b256-b284205fb499/lod3.png)

*Skeletal Mesh LODs*



Depending on the complexity of your Skeletal Mesh and the power of your hardware, the LOD generation process may take some time to complete.

LODs can be individually modified and regenerated at any time by selecting **Regenerate LOD** from within an Individual LODs **Reduction Settings**, or the entire set can be modified and regenerated with **Apply Changes** from the base LOD's (LOD 0) **LOD Settings**.

LODs that have been generated using Unreal Engine, will have a note next to their property section in the Asset Details panel, indicating that it has been **[generated]**.

![generating tag on generate lods in the asset details](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fb668b4f-667a-4caf-9a83-defa7e55d1ce/generatedtag.png)

## Skeletal Mesh Reduction Tool

When generating LODs in Unreal Engine, there may be some cases where the Mesh reduction can eliminate key or important details of the Mesh. Using the **Skeletal Mesh Reduction Tool**, you can more precisely define how LODs are generated, and control the reduction effect.

### Bones to Prioritize

Within an individual LOD's set of properties in the **Asset Details** panel, you can use the **Bones to Prioritize** property to preserve the associated skinned geometry quality.

![LOD 3 Hand](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2a3e5d3e-51ce-4f68-a7e2-121621b2c28c/handlod3.png)

![LOD 6 Hand](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/be94f4dd-8e1f-4fcd-9aaf-f562786abef0/handlod6.png)

First, in the **Asset Details** panel locate the **LOD Picker** section and enable the **Custom** property. This will allow you to see each LOD's set of properties in the **Asset Details** panel.

![lod picker properties in the asset details panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3c6326b6-9019-40c1-99ac-8b11b3b8700d/lodpicker.png)
