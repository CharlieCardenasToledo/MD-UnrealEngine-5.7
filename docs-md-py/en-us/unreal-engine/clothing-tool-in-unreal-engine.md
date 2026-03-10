# Clothing Tool

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/clothing-tool-in-unreal-engine

> Application Version: 5.7

Unreal Engine uses Chaos Cloth solver which is a low-level clothing solver responsible for the particle simulation that runs clothing. This clothing solver allows integrations to be lightweight and very extensible because we now have direct access to the simulation data.

![Unreal Engine uses Chaos Cloth solver which is a low-level clothing solver responsible for the particle simulation that runs clothing](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/88be3135-2772-4946-bbd0-c7cc989a645b/clothing-overview-banner.png)

With the Clothing Tools available within the Editor, the workflow enables developers to work directly with Unreal Engine to author their content without the need for external dependencies.

Unreal Engine Cloth Workflow. Click the image for full-size view.

This workflow enables you to create your content once and then do all the creation editing of the clothing directly inside of Unreal. It makes the creation and iteration of testing content that much quicker, and you also avoid any disconnects between where the content was created versus where it's being used by being able to see all of your edits for your clothing simulation happening in real-time and as they will appear in your game.

## Cloth Painting Workflow

Using the workflow of creating cloth in-Editor, the Cloth Paint Tool enables you to quickly create clothing for your characters using any existing material element of a Skeletal Mesh.

Click for the full image.

1. **Section Selection -** Use this to select the Material IDs that will be used for painting cloth onto.
2. **Cloth Paint Panel -** This section includes all the necessary tools and properties you can use when painting clothing.

Follow the steps below to learn the process to create your clothing assets, assign them to your character, and along with the basics of painting on your render mesh.

### Create and Assign a Cloth Asset

To start working with clothing, you will first need to create a clothing asset from your Level of Detail (LOD) section and assign it to your render mesh so that you can paint on it.

Follow the steps below to get started:

1. In the Skeletal Mesh Editor, click the **Section Selection** button from the main toolbar. It will enable you to select the different parts of your Skeletal Mesh that have their Material Element assigned.

   Click for full image.
2. Use the left-click to select a part of your mesh that you want to use as cloth. Then right-click to open the context menu to create your Cloth Asset.

   Click image for full size.
3. From the context menu, select **Create Cloth Asset from Selection** and then fill in the following areas of the menu:

   ![The parameters to be filled in when creating a cloth asset from a selection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f4901ec-820c-4bb7-9770-a32d2cb2756d/create-cloth-context-menu.png)
   * **Asset Name** - Give your asset a name so that you can easily find locate it later.
   * **Remove from Mesh** - If you've got a separate mesh piece of geometry you want to be associated as cloth, you can enable this option. If not, you can leave this unchecked.
   * **Physics Asset** - If this cloth asset is for a character, use its Physics Asset here to get proper collision for the cloth simulation.

   Once you're happy with the settings, click the **Create** button.

   ![Clicking create after setting the parameters](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1f878138-9697-4e67-b66d-961d2713a164/create-cloth-button.png)
4. Right-click on the section again to bring up the context menu and hover over the **Apply Clothing Asset** and select from the available clothing assets to apply. It will associate any clothing assets created with the section you've selected.

   ![Appying a clothing asset using the context menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5ae77098-a87b-4672-b252-19f594141c3d/cloth-asset-context-menu-apply.png)

### Painting On Your Cloth

Once you're ready to paint on your cloth, you can use the following controls to Paint on your selected cloth asset.

* Paint - **Left Mouse Button**
* Erase - **Shift + Left Mouse Button**
* Cloth Preview - **H**

  If you've used the NVIDIA's PhysX DCC Plugin to create Clothing for 3DS Max or Maya, or similar painting tools in other programs, the controls should feel familiar for this operation.

1. In the Skeletal Mesh Editor, go to the File menu and select **Window**, then select **Clothing** from the list.

   ![Selecting clothing in the main window's menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6dd844f6-5948-4147-a67a-fe36893fabcb/painting-step-1-1.png)

   This will open the **Clothing** panel.

   ![The clothing panel with main parameter categories expanded](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9bce5bcc-6d4b-48a3-85fb-27fe152fcd56/clothing-panel.png)
2. Click the **Activate Cloth Paint** button from the toolbar to enable properties you can use to paint for your selected Cloth Asset.

   ![Highlighting the activate cloth paint button in the toolbar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/485f00b1-fc72-4e40-ade5-9e55441894cf/activate-cloth-paint.png)
3. In the **Clothing** panel, select your assigned **Cloth Asset** from the **Clothing Data** list.

   ![Selecting a cloth asset from the clothing data list](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/043d3239-aeb8-4a1d-9c3c-8789fcae604c/painting-step-2.png)
4. In the **Cloth Painting** section, you can select a [Paint Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/clothing-tool-in-unreal-engine#painttools) type to use and then set a **Paint Value** (by default, the Brush paint tool will be used). Then left-click and drag across the surface of your mesh to start painting.



   Hold the **H** keyboard shortcut to preview your painted cloth.

## Paint Tools

![The paint tool selection dropdown menu highlighted](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c6ba837-6a31-47ab-9897-72769ea94513/paint-tool-selection.png)

The **Tool** selection enables you to choose from the brushes available to cloth paint.

* [Brush](https://dev.epicgames.com/documentation/en-us/unreal-engine/clothing-tool-in-unreal-engine#brush)
* [Gradient](https://dev.epicgames.com/documentation/en-us/unreal-engine/clothing-tool-in-unreal-engine#gradient)
* [Smooth](https://dev.epicgames.com/documentation/en-us/unreal-engine/clothing-tool-in-unreal-engine#smooth)
* [Fill](https://dev.epicgames.com/documentation/en-us/unreal-engine/clothing-tool-in-unreal-engine#fill)

### Brush

The **Brush** tool enables you to paint a radius and strength value on your cloth as you drag across cloth assets.

![The lower part of the clothing panel with a brush selected in the cloth painting section](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8d2bb0f4-1e00-4c6e-9fbc-97e208f2e9e4/cloth-painting-brush.png)

Use the **Paint Value** to control the strength of the brush when you are painting the cloth. This value controls how much the painted area will react like cloth based on this value. A value of 0 would mean that the skinned vertex could not move and a value of 100 would allow the skinned vertex to move one meter from its original position.

![Painting cloth with the brush](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7c2e5064-1e73-4659-b977-3183b7d5df21/paint-brush.png)


For additional information about this tool and its properties, see the [Brush Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/clothing-tool-in-unreal-engine---properties-reference#brush) reference here.

### Gradient

The **Gradient** tool enables you to paint a gradual blend between a set of cloth values that are selected.

![The lower part of the clothing panel with gradient selected in the cloth painting section](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/21a791a0-4156-44bb-a401-7ed1fdb6502a/cloth-painting-gradient.png)

To paint a gradient, perform the following steps:

1. Use the **Left-Mouse Button** to paint your **Gradient Start Value**. This is indicated by a **Green** dot over the painted vertice.
2. Hold the **Ctrl + Left-Mouse Button** to paint your **Gradient End Value**. This is indicated by a **Red** dot over the painted vertice.
3. When you are finished painting, press the **Enter** key to paint your gradient.

![An example of a cloth gradient](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7d5bd370-68c7-4525-8567-74d9ec3df3b9/gradient-example.png)


For additional information about this tool and its properties, see the [Gradient Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/clothing-tool-in-unreal-engine---properties-reference#gradient) reference here.

### Smooth

The **Smooth** tool enables you to blur or soften the contrast between painted cloth values.

![The lower part of the clothing panel with smooth selected in the cloth painting section](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d1f8dd76-5a75-42b9-a178-220459912fb1/cloth-painting-smooth.png)

Use the **Strength** value to adjust how strong or soft the blurring effect is to create a soft gradient between painted areas.

![Using the smooth tool to create a soft gradient between painted areas](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cd3e28f5-9c5d-436a-8bf2-211f61183331/paint-smooth.png)


For additional information about this tool and its properties, see the [Smooth Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/clothing-tool-in-unreal-engine---properties-reference#smooth) reference here.

### Fill

The **Fill** tool enables you to replace areas with similar values with another value.

![The lower part of the clothing panel with fill selected in the cloth painting section](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf71e328-8721-4944-8ce3-fb96bac08fd1/cloth-painting-fill.png)

Use the **Fill Value** to set a value to fill the vertices in the area with. Use **Threshold** to set a value that the fill operation should use when sampling the vertices to replace.

![Painted Area (White)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7d061150-44db-47e0-bd1f-554569accb3d/paint-fill-1.png)

![Painted area using | Fill value of 1.0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/986be5fe-17b7-48e6-ab5e-9984c1ff2567/paint-fill-2.png)



For additional information about this tool and its properties, see the [Fill Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/clothing-tool-in-unreal-engine---properties-reference#fill) reference here.

## Cloth Properties

The **Cloth Config** properties enable you to adjust your cloth to simulate different materials, such as burlap, rubber, or many other types of cloth materials.

![Clothing config properties on the clothing panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/013f4203-a045-47ef-845f-93450c54f6da/cloth-config.png)
