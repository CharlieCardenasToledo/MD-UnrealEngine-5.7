# Modeling Mode Quick Start

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/modeling-mode-quick-start-in-unreal-engine

> Application Version: 5.7

The **Modeling Mode** toolset in Unreal Engine is used to create meshes, rapidly prototype new level geometry, and edit existing meshes all without leaving the Editor.

![Pine Wood Crate Created Using Modeling Mode](https://dev.epicgames.com/community/api/documentation/image/718850eb-fad2-4778-a84e-e0cbbfb69c44)

_In this quick start, you will create this pine crate using Modeling Mode._

This quick start guide walks you through the creation of a wood crate using several of the tools in Modeling Mode. You start by creating a new primitive shape and add detail using several of the **PolyEdit** tools. Next, you prepare your model for texturing using the [UV](working-with-content/modeling-and-geometry-scripting/modeling-tools/uvs-category) tools. Finally, you add a **Material** and drop it into your **Level** with full collision and physics simulation.

### Prerequisite Topics

Before starting this quick start guide, we recommend you familiarize yourself with Modeling Mode and [how Unreal Engine handles 3D models](https://dev.epicgames.com/documentation/en-us/unreal-engine/static-meshes).

Although many tools in Modeling Mode are similar to their counterparts in other modeling software, there are a few key differences in how the Modeling Mode editor structures mesh editing that you should know before you begin working with it.

For more information, see the [Modeling Mode Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine).

## 1 - Creating a Box Primitive

Before you start, create a new project based on the First Person Game template. For more information on creating new projects in Unreal Engine, see [Creating a New Project](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-a-new-project-in-unreal-engine).

1. Open **Modeling Mode** by clicking the **Select Mode** drop down menu and select **Modeling**. This will open the **Mode Toolbar** and **Modeling** panel. ![Opening Modeling Mode using the Modes drop down](https://dev.epicgames.com/community/api/documentation/image/76c12e86-58b6-46df-8470-f9e61ba213c8)
2. In the **Shapes** category at the top of the **Mode Toolbar**, click **Box** and adjust the settings in the **Modeling** panel to your desired size. For this guide, the default settings are fine. This creates a 100 centimeter box that is about half the height of the default character. ![Create a box primitive with the Box tool](https://dev.epicgames.com/community/api/documentation/image/b7d44f70-f69f-4aac-9256-e034df000c29)
3. Click in the **Viewport** to create your box, then click **Complete** at the bottom of the screen or press **Enter**.

## 2 - Creating the Outer Frame

Turning your primitive shape into a detailed 3D model begins with defining its **PolyGroups**.

![A box displays Modeling Mode PolyGroups](https://dev.epicgames.com/community/api/documentation/image/4b5facb9-8473-4e78-83b6-d3e2516d0299)

_A box primitive with six defined PolyGroups._

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "It can be helpful to collapse the sections you are not using in the <strong>Mode Toolbar</strong>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24484389,
      "caption": "",
      "alt_text": "Collapsing Tool Catagories in the Modeling Tools Pallette",
      "image": {
        "id": 24484389,
        "file_name": "modeling-mode-collapse-tools.png",
        "file_size": 32479,
        "content_type": "image/png",
        "created_at": "2025-04-10T18:10:53.505+00:00",
        "height": 854,
        "width": 159,
        "storage_key": "7bafae45-1898-4ece-bccf-169e63ef53c2",
        "context": "documentation"
      },
      "storage_key": "7bafae45-1898-4ece-bccf-169e63ef53c2",
      "context": "documentation",
      "width": null,
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

1. Select the box in the viewport. In the **Mode Toolbar**, find the **Attributes** section and click **GrpGen**. This will generate PolyGroups for the box. ![Select the GrpGen tool in the Modeling Tools palette](https://dev.epicgames.com/community/api/documentation/image/3912356d-0f94-4a90-b4b6-85752aeb8dae)
2. The default **Conversion Mode** and settings are fine for this Quick Start, so click the **Accept** button at the bottom of the viewport or press **Enter**. ![Create your PolyGroups using the default settings](https://dev.epicgames.com/community/api/documentation/image/0f0fbd1f-ca15-4378-a038-9a4ee923829d)
3. In the **Mode Toolbar**, locate the **PolyModel** tools section and click **PolyEd**. This will open the **PolyEdit** tools in the **Modeling** panel. ![Click on PolyEd to open the PolyModel tools in the Tools Details panel](https://dev.epicgames.com/community/api/documentation/image/8c19d5b4-ec24-4b0b-af13-95470a9eaa7b)
4. Select one of the faces in the **Viewport** and click **Inset**. Move the mouse in the viewport until the face is inset the amount shown in the image below. ![Inset the face to create the outer frame](https://dev.epicgames.com/community/api/documentation/image/e084c2cb-2335-4631-89ff-475a7d992be1) Click the mouse again to inset the face.
5. Select the inner face you created and click **Extrude**. Extrude the face inward to create the outer frame of the crate. ![Extrude the inner face inward to finish creating the outer frame](https://dev.epicgames.com/community/api/documentation/image/cbacc04e-9606-4579-b2b3-20d3c8fe7967)
6. Repeat this process for each side of the crate. Don't forget the bottom face.

## 3 - Adding Additional Detail

Next, you will add a cross brace to the outer frame of the crate.

1. In the **PolyEd** tools, select the inner face you just extruded and click the **Decompose** button. This will split the face into its component triangles and create an edge from corner to corner. ![Decompose the inner face of the crate](https://dev.epicgames.com/community/api/documentation/image/567ddfad-3674-402b-8c23-94e76775f629)
2. Select the new edge you created. Then hold **Shift** and select the additional edges in the corners connected to the new edge as shown in the image below. ![Select the new edge and the two connected corner edges and Bevel](https://dev.epicgames.com/community/api/documentation/image/4770fdfe-9f37-4303-89fc-ca0f5ac673d2) With the edges selected, navigate to the **Edge Edits** section and click **Bevel**. Leave the settings at the defaults and click the **Apply** button at the top of the menu. This splits the edge and creates a new face.
3. Select the new face and extrude it until it is level with the outer frame. ![Extrude the new face to create the cross brace](https://dev.epicgames.com/community/api/documentation/image/317a8758-1077-4067-8f0d-f86a3bbc6efa)
4. This creates two inner faces, one at the end of the extruded cross brace and one in the inner corner. Move your camera view inside the crate and select the inside faces as shown below. ![Move the camera inside the crate and select the inner face at the end of the cross brace](https://dev.epicgames.com/community/api/documentation/image/5a056826-f7ca-46d8-be17-bee1d479517d) ![Move the camera down and to the left to select the inner face in the corner](https://dev.epicgames.com/community/api/documentation/image/9c1b8c5c-b406-487e-b74f-63c30cab2af4) Click Delete or press the Delete key to remove the faces.
5. The **Weld** tool joins two edges at the location of the last one selected. Select the two edges shown below. ![Move the camera back outside the crate to select the two edges where the cross beam meets the corner](https://dev.epicgames.com/community/api/documentation/image/04aff87b-690d-4777-bed0-29e29521413b) Click **Weld**.
6. Repeat this process for the other end of the inner frame.
7. Repeat the process for each side of the crate.

## 4 - Unwrapping UVs

To display the wood texture correctly, the crate will need to be UV unwrapped.

1. Since you have made significant changes to the original box shape, click **GrpGen** and generate new PolyGroups for the crate. Change the **Min Group Size** to `3` to generate six new PolyGroups (one per side) similar to the image below. ![Generate six new PolyGroups](https://dev.epicgames.com/community/api/documentation/image/a0ca2901-0f70-46b2-b672-a9118279619e) Click **Accept** or press **Enter** to continue.
2. Next, go to the **UVs** section of the menu and select the **Unwrap** tool. At the top of the **Modeling** panel, open the **Island Generation** dropdown menu and select **PolyGroups**. ![Use the Unwrap tool to create a UV map](https://dev.epicgames.com/community/api/documentation/image/4605a8a7-7326-4d73-9c1e-8c48dc4ec17e)
3. Change the value of the **Texture Resolution** to 2048. This changes the offset between the UV islands to make sure there are enough pixels between them. ![Change the Texture Resolution to 2048](https://dev.epicgames.com/community/api/documentation/image/32db251d-841d-406d-ba7a-d8d4e115d275)
4. To see the generated UV map, click the checkbox for the **Enabled** option in the **Preview UV Layout** section of the menu. Your UV map will look similar to the image below. Click **Accept** or press **Enter** to finalize the UV map. ![Enable the UV map preview window](https://dev.epicgames.com/community/api/documentation/image/0358dddf-ffbb-481e-a41b-f6ad7043b6bc)
5. Finally, check the quality of the generated UV map by adding a wood material to the crate. In the **Details** panel, open the **Materials** section and click the dropdown menu for **Element 0**. Search for the **M\_Wood\_Pine** Material and apply it to the crate. ![Add the M_Wood_Pine Material in the Details panel](https://dev.epicgames.com/community/api/documentation/image/06b6e518-bd23-4d6a-bdc8-c449883c6f0c)

## 5 - Bring the Crate into the Level

Make the crate ready for your Level by adding **Simplified Box Collision** in the **Static Mesh Editor** and enabling **Physics Simulation**.

1. Locate your crate asset in the **Content Browser** and open it in the **Static Mesh Editor**. This can be done by navigating to the `FirstPerson/Maps/_GENERATED/User` folder and double clicking your box asset. ![Return to Select mode and open the crate in the Static Mesh Editor](https://dev.epicgames.com/community/api/documentation/image/08ebfd03-e43a-4ffb-8be6-32f47ff859b4)
2. Click on the **Collision** menu and select **Add Box Simplified Collision** to add a basic collision box to the crate. ![Add a collision box to the crate using the Add Box Simplified Collision option](https://dev.epicgames.com/community/api/documentation/image/01df0196-a2c3-4a34-b860-3cb99f77dc10)
3. Locate the **Collision Complexity** section in the **Details** panel. Open the drop down menu and select **Project Default**. ![Change the Collision Complexity property to Project Default](https://dev.epicgames.com/community/api/documentation/image/e9143268-eb39-4736-89b0-40a23ca01080)
4. Back in the **Editor** window, enable **Simulate Physics** in the **Details** panel. ![Enable Simulate Physics in the Details panel](https://dev.epicgames.com/community/api/documentation/image/ea2dd436-b9ca-4400-934e-e626717ae60b)

## Result

Over the course of this quick start, you created a wood crate Asset using the Modeling Mode toolset, entirely inside the Unreal Editor. You added detail to your model, added a UV map, and a wood Material.

Finally, you added appropriate collision settings and enabled physics to make your crate a game ready Asset.

![The final version of the pine crate inside the level](https://dev.epicgames.com/community/api/documentation/image/8681e949-eb9c-4260-9d84-f223547eef69)

_The final version of the pine crate inside the Level._
