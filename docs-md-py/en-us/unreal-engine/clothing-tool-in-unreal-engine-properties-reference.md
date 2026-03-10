# Clothing Tool Properties Reference

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/clothing-tool-in-unreal-engine---properties-reference

> Application Version: 5.7

The **Cloth Paint Tools** have many options and properties that you can use to make very specific clothing simulations. Below you'll find the details about the menu options you can use when creating your clothing assets and details about the Cloth Paint panel that you will use when selecting different painting tools to paint cloth values for your render mesh.

## Clothing Asset Creation Menus

In this section, you'll find the details about the properties and settings you can use when creating and applying your clothing assets to your render mesh.

### Section Selection

The **Section Selection** menu is available by right-clicking a selected section. It enables you to select the different material elements of your render mesh to create and apply a clothing asset. In this menu, you can identify the LOD and a material section of your mesh that you've selected, create a cloth asset for your render mesh and its LODs, apply the clothing asset to the selected section, and remove it later if needed.

![The context menu which opens when right-clicking a selected section](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f050943e-8b56-4e9e-889c-0180b46da86c/section-selection-context-menu-properties.png)

| Property | Description |
| --- | --- |
| **LOD Section Selection** | The name of the LOD level used and the Section to create a Cloth Asset for. |
| **Apply Clothing Asset** | Select a clothing asset to apply to the selected section. |
| **Remove Clothing Asset** | Remove the currently assigned clothing asset. |
| **Create Clothing Asset from Section** | Create a new clothing asset using the selected section as a simulation mesh. Create a new clothing asset using the selected section  * Basics   + **Asset Name**: The name entered for the cloth section asset.   + **Remove from Mesh**: Whether or not to leave this section behind (if driving a mesh with itself). Enable this is driving a high-poly mesh with a low-poly mesh. * Collision   + **Physics Asset**: Physics Asset to extract collisions from. Note that this will export Sphere and Sphylls, but does support up to 32 convex faces (or 5 boxes). |
| **Create Clothing Asset from LOD Section** | Create a clothing simulation mesh from the selected section and add its LOD to an existing clothing asset. Create a clothing simulation mesh from the selected section and add its LOD to an existing clothing asset  * Target   + **Remap Parameters**: If reimporting, this will map the old LOD parameters to the new LOD mesh. If adding a new LOD, this will map the parameters from the preceding LOD.   + **Target Asset**: This is the target asset when importing LODs.   + **LOD Index**     - **Replace LOD**: Replace the simulation mesh in LOD0 of your selected clothing asset with this section.     - **Add LOD**: Use the selected section to add a new LOD. * Basic   + **Remove from Mesh**: Whether or not to leave this section behind (if driving a mesh with itself). Enable this if driving a high-poly mesh with a low-poly one. |
| **Generate section # up to LOD #** | Generated LODs will use section # up to LOD #, and ignore it for lower quality LODs |

## Clothing Panel

The **Clothing** panel houses all the clothing data, masks, configuration parameters for how your cloth reacts, and the tools you'll use when painting your cloth values.

![The clothing panel with main parameter categories expanded](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a0acdafe-fcd7-4a72-8bd2-078bab0cfb57/clothing-panel-properties.png)
