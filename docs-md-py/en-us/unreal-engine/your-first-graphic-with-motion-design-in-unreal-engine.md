# Your First Graphic with Motion Design

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/your-first-graphic-with-motion-design-in-unreal-engine

> Application Version: 5.7

This tutorial provides a set of step-by-step instructions about how to use Unreal Engine's Motion Design tools to create an animated 2D graphic that you can control in real time, causing it to enter the screen, leave the screen, and transform on screen. This workflow is a foundation you can build on to create more advanced and complex animations in both 2D and 3D using Motion Design.

## Getting Started

This tutorial assumes you are familiar with the content of the [Motion Design Quickstart](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-quickstart-guide-in-unreal-engine). If you haven't read it already, start there. When you have enabled the required plugins, and reviewed the sections on creating a new level and the Motion Design UI, continue below.

There are two ways to continue with this tutorial, both equally valid.

1. Use Motion Design in an [existing level](https://dev.epicgames.com/documentation/en-us/unreal-engine/your-first-graphic-with-motion-design-in-unreal-engine).
2. Create a new level using the [Motion Design template](https://dev.epicgames.com/documentation/en-us/unreal-engine/your-first-graphic-with-motion-design-in-unreal-engine).

### Use Motion Design in an Existing Level

Your first option for this tutorial is to open the **Motion Design interface** on an existing level by clicking the **Motion Design** button in the toolbar.

![The Motion Design button in the toolbar](https://dev.epicgames.com/community/api/documentation/image/394eeac1-992a-4b60-a5a6-64ad2d33d0c2)

_The Motion Design button in the toolbar._

You can also use the Motion Design tools without changing the entire interface by switching to the **Motion Design Mode** in the Modes dropdown. This Mode can also be opened using SHIFT+9 on your keyboard.

![Motion Design in the Modes menu](https://dev.epicgames.com/community/api/documentation/image/e4c7f2f6-bedd-4252-9a60-f91e848358bb)

_Motion Design in the Modes menu._

#### Populating an Empty Level with Default Elements in a Motion Design Scene

If you choose the first option above, to start from an empty level, you’ll need to activate **Motion Design** mode by clicking on the button at the top-middle of your screen. By default, when you create an empty new level in Unreal Engine, there are no lights, post-process volumes, or cameras.

![The Motion Design button](https://dev.epicgames.com/community/api/documentation/image/1b2111a4-f8b1-47fc-bddb-c113a51cda43)

_The Motion Design button._

1. Select which recommended default actors you want to add to your empty level by clicking **Create Defaults**. This opens the **Configure Default Scene Actors** window with several options. ![The Create Defaults button](https://dev.epicgames.com/community/api/documentation/image/be02f321-ccc9-4ae6-bb53-ae6ff63fb0ed)
2. Select which **Motion Design Default Scene Actors** you want to add or replace in your scene and click **Spawn**. For this tutorial, use the default options. ![The Configure Default Scene Actors window](https://dev.epicgames.com/community/api/documentation/image/92215023-36ad-4c1f-a3c8-8d1ca1041d0c)

The Viewport and Motion Design Outliner then both update with the options you selected.

### Create a New Motion Design Level

For this tutorial, your second option is to create a new level using the Motion Design template.

Create a new level (File > New Level). In the prompt window, select what kind of level you want to create. The **Motion Design** template is used for 2D designs, while **3DMotion Graphics** is used for 3D designs. This tutorial covers 2D design.

- To follow the steps in this tutorial, select the **Motion Design** template, and click **Create**. ![image alt text](https://dev.epicgames.com/community/api/documentation/image/b46f8315-520d-4b52-9d7a-bfb14d48b229)

#### Spawn Default Scene Actors

After creating the new level from the Motion Design template, you must configure and spawn your default scene actors.

1. Click the **Create Defaults** button to open the **Configure Default Scene Actors** window.
2. For this tutorial, you have to use the default options, so click **Spawn** to create the default scene actors. ![The Configure Default Scene Actors window](https://dev.epicgames.com/community/api/documentation/image/75fa73aa-5bd1-4f8b-a1b8-e1042ba4e69e)

## Creating an Animated 2D Graphic Using Motion Design

### What You’ll Learn

This section of the tutorial has instructions for using the Motion Design interface features and tools you will use to create an animated 2D graphic. These include:

- Drawing and customizing 2D primitives.
- Customizing geometry using the **Material Designer.**
- Positioning content using Null Actors.
- Adding text.
- Constraining text to fit certain background sizes.
- Controlling text with Remote Control.
- Playing in a Sequencer animation, stopping it using the Sequencer mark system, then continuing from that mark to play the off-animation.

### Initial Template Edits

After creating your new level, your UE user interface resembles the following image:

![The Motion Design template initial state](https://dev.epicgames.com/community/api/documentation/image/0790018d-8878-48d4-bf91-e99826237207)

_The Motion Design template initial state._

In this tutorial, you are going to create something new, so begin by deleting the graphical elements that spawn automatically with the template.

1. In the **Motion Design Outliner**, click on the **Starter Content** group
2. Press **delete** on your keyboard, and confirm you want to delete the children of the selected object in the dialogue window.

You should now see an empty Viewport similar to the following image.

![The Motion Design template after deleting the Starter Content group](https://dev.epicgames.com/community/api/documentation/image/d65941f3-1cd3-4d06-b623-70d1c31969f8)

_The Motion Design template after deleting the Starter Content group._

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The Viewport might display as a black screen. You can switch it to the checkerboard pattern using the <strong>View</strong> options in the lower-right of the Viewport.",
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

You must set your canvas dimensions.

1. To do so, click the **Camera** button on the upper-left of your Viewport.
2. Select **Ruler Override**.
3. Use the **Resolution** settings to define the size of your canvas according to the requirements of your project. ![Use Ruler Override to set the size of your canvas](https://dev.epicgames.com/community/api/documentation/image/4cd21c13-ac33-4899-8538-a27f9e4509ce)

### Shape Creation and Groups

You can create shapes using the Motion Design toolbox. If this panel is not open, you can access it by clicking the **Mode** dropdown, and selecting **Motion Design**.

![Select Motion Design in the Mode dropdown](https://dev.epicgames.com/community/api/documentation/image/1113d638-0495-4a23-8b5b-e617ecd8e894)

_Select Motion Design in the Mode dropdown._

You can choose from several shape options. For this tutorial, begin with a **Rectangle**.

- Double-click the **Rectangle** to spawn one in the center of your canvas. ![Double-click the Rectangle button to add a rectangle to your canvas](https://dev.epicgames.com/community/api/documentation/image/cb7c7b6d-de0f-4593-b97a-74bf44b14214) ![Your newly-created rectangle should resemble this image](https://dev.epicgames.com/community/api/documentation/image/d7272194-efae-46a2-9528-1ee91cce6ef8)

You can customize the shape and properties of your new rectangle (such as slant and bevel) in the Details panel on the lower right side of the interface. You can also change the sizing by clicking and dragging the handles of the newly created shape.

Next, anchor your shape.

1. In the **Details** panel, select the **Shape** category.
2. Change the **Horizontal Alignment** to **Left**, and the **Vertical Alignment** to **Center**. ![Changing the horizontal and vertical alignment](https://dev.epicgames.com/community/api/documentation/image/f28390b6-d384-4e90-a7a3-cc31c98adac0)

You will eventually have other actors that will move around at the same time as a **Group**.

- To create a Group, select the rectangle and press CTRL+G on your keyboard, or click the **Group** button found in the Motion Design Outliner. ![The Group button](https://dev.epicgames.com/community/api/documentation/image/457326c0-bd39-4f99-8364-e89e7c03da03) This creates a null actor parent of the Rectangle actor. ![The null actor parent of your Rectangle actor](https://dev.epicgames.com/community/api/documentation/image/d7934810-3990-41fa-b212-898e98528a9a)

In the Details panel, you can experiment with changing the location of the null actor. Changing the null actor’s position does not affect the position of the rectangle actor.

1. Rename the rectangle to **BG\_Main** by right-clicking it in the **Motion Design Outliner**.
2. Move the rectangle over to the left side of the screen so it is flush with the edge of the canvas. You can do this using the rectangle geometry, or you can position the rectangle by using its null actor parent. To do so, select that **null actor**, and rename it to **L3\_BG**. Using the parent, move the **Location** of the **group** in the **Details** panel. ![Renaming the null actor](https://dev.epicgames.com/community/api/documentation/image/85cadc0a-42bc-46de-8452-10c0bbed86d8)

Your canvas should now resemble the image below.

![Moving the rectangle by moving the group](https://dev.epicgames.com/community/api/documentation/image/bbe04694-fb2f-43b1-960b-90d9066ecece)

_Moving the rectangle by moving the group._

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can hold down your middle mouse button to pan around the canvas. The shaded areas represent the _offscreen _region. In this tutorial, you are going to set up your graphic to slide offscreen, so keep the boundaries of your canvas in mind.",
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

Next, size your rectangle:

1. Click on the **BG\_Main** actor, and click the **Shape** button.
2. In the Motion Design Outlines, make sure that **Size Type** is set to **Pixels**. This is the first setting under **Shapes**.
3. Unlink your **Pixel Size** property by changing the Pixel Size from **XY** to **Free**.
4. Set the **Pixel Size** property to 1842 x 132. ![Setting your unlinked Pixel Size property](https://dev.epicgames.com/community/api/documentation/image/87366a09-f160-4636-b5bc-6730928e161f)

You are creating a lower-third graphic, so move the position of the entire group to where they typically live.

- Select the **null actor** that parents BG\_Main, and set the **Y** position to -160. ![Setting the position of the null actor](https://dev.epicgames.com/community/api/documentation/image/29ed18cc-c958-4b5e-b6da-7884ff8a530d)

When everything is positioned, your Viewport should resemble the following image:

![The results of your initial positioning](https://dev.epicgames.com/community/api/documentation/image/68939bbf-6c84-40e9-b935-fe7956fa2535)

_The results of your initial positioning._

### Customizing the Graphic Using the Material Designer

Next, you will customize the lower third graphic to make it look more interesting than a simple gray box, using the **Material Designer**.

To customize the graphic:

1. Select the shape, and click on the **Material** button in the **Details** panel.
2. Set the **Material Type** to **Material Designer**.
3. Click the **Edit with Material Designer** button.

The **Material Designer** tab should appear in your **Tool Parameters** section. Your Viewport should now resemble the following image:

![Setting up to use the Material Designer](https://dev.epicgames.com/community/api/documentation/image/1694d14d-ffbb-4b4e-8197-514140395458)

_Setting up to use the Material Designer._

The Material Designer is Motion Design’s layer-based material creation tool. Similar to other layer-based tools, such as graphic editing or photo editing software, each layer has a fill, a mask channel, and an independent opacity value, as well as a full suite of blend modes.

Below is an overview of the Material Designer interface:

![The Material Designer interface](https://dev.epicgames.com/community/api/documentation/image/ffa8e99e-792e-464b-aa44-7aa619c3ba2d)

_The Material Designer interface._

#### Interface Key

1. Switch between a surface or a post-process material.
2. Material type selector. The available options are: Opaque Masked Translucent Additive Modulate
3. Adjust the opacity of the entire layer stack.
4. Switch between adjusting the fill or the mask layer stack.
5. Adjust layer opacity, and change the layer’s blend mode.
6. Individual layer control for fill and mask. The chain icon determines whether to link the UVs of the fill and alpha texture. You can enable or disable either part by clicking on the white dot to the left of the layer thumbnail.
7. The Viewport Utility Toolbar contains the following tools: Layer FX, which you can use to apply a variety of material effects to a layer. Add a layer. Duplicate a layer. Delete a layer.
8. Layer settings, such as texture transforms and the ability to clamp a texture.

In the Material Designer interface image above, the fill of the layer (the checkerboard icon) is selected, and the image below displays some options to set the layer type. These include:

- Texture
- Solid Color
- Color Atlas
- Texture Edge Color
- Gradient
- Material Function

![Layer type options](https://dev.epicgames.com/community/api/documentation/image/ef4c8eea-5577-4ad7-b075-d565e0247edc)

_Layer type options._

1. For now you want a simple solid color, so select **Solid Color**.
2. Next, click the **Color** widget, and set the color in the popup menu. ![Setting your color using the Color Picker](https://dev.epicgames.com/community/api/documentation/image/60a79bed-8968-44a3-86d5-e6fc5c45e70d)
3. Set your color to green using the following RGB values: R: 0.0 G: 0.441406 B: 0.030081

### Adding a Pattern

Next, you will add a pattern by creating a new layer with the **Add New Layer** button found in the Viewport utility toolbar.

![The Add New Layer button in the Viewport utility toolbar](https://dev.epicgames.com/community/api/documentation/image/33de188d-2caa-4fd4-8dd6-6fcbb87ca298)

_The Add New Layer button in the Viewport utility toolbar._

By default, it creates a texture. When you click on the dropdown, several options appear.

- Select a standard linear gradient texture. In the example shown below, the texture is named 2. ![Selecting a standard linear gradient texture](https://dev.epicgames.com/community/api/documentation/image/23014a9a-d9a0-4475-a7a2-ad36565e6bdf)

Next, you need to do some rotation and scaling of the UVs to get the type of pattern you want for this walkthrough.

1. Disable the layer mask for this layer by toggling the mask off and unlinking the scale. ![Toggle off the mask and unlink the scale](https://dev.epicgames.com/community/api/documentation/image/c6c8aa73-3df2-4dee-9c71-d566c5e956fd)
2. Set the **Properties** for the texture to the following: Type: Texture Texture: 2 Offset: 0.0, 0.0 Rotation: 45.0 Scale: 0.035, 0.035 Pivot: 0.5, 0.5 Mirror on X: disabled Mirror on Y: disabled Clamp Texture: disabled ![Your new texture layer's properties](https://dev.epicgames.com/community/api/documentation/image/31a46089-1c26-4762-9376-0dd87ecc380a)
3. Set the **Blend** for the gradient layer to **Multiply** as shown in the image below. ![Blend layer set to Multiply](https://dev.epicgames.com/community/api/documentation/image/7919c84c-17c8-448a-8712-90ded10f3fdb)

Your graphic should now resemble the following image:

![The initial pattern has a harsh gradient](https://dev.epicgames.com/community/api/documentation/image/2b90c02b-b128-49dc-9bd6-4db22d7e2716)

_The initial pattern has a harsh gradient._

Next, you need to reduce how harsh the gradient is.

- Set the **Opacity** (list item 5 on the interface overview above) to 0.11. ![Reducing the opacity of the pattern softens the gradient](https://dev.epicgames.com/community/api/documentation/image/ffee6ae3-cb40-4723-ba09-299bf74eeda1)

To break up the pattern, fade it toward the left side of the bar.

1. Return to the layer settings and re-enable the layer mask, but keep the layer UV unlinked.
2. Add another linear gradient to the mask (you can use the same one).
3. Clamp it using the **clamp texture** button in the texture parameters. This prevents it from repeating the texture.
4. Set the following properties on the alpha texture: **Clamp Texture: True** **Offset: -0.566, 0.0** **Rotation: 220.0** **Scale: 3.0, 0.0**

Your result should resemble the following image:

![Your banner after adding a clamped linear gradient](https://dev.epicgames.com/community/api/documentation/image/3987ee49-7c7c-495e-8357-21127f952b86)

_Your banner after adding a clamped linear gradient._

Next, you’ll round the edges and skew the shape slightly.

1. With your shape selected, click the **Shape** button.
2. Select the **Right Slant** property, and set the value to 18.00.

**Beveling** works in two ways, independent for each corner or uniformly. For this design, you’ll bevel the top right and bottom right corners.

1. Expand the options for **Top Right** and **Bottom Right** at the bottom of the **Shape** settings.
2. Set their values as follows: **Type:** Curve In **Size:** 13.0 **Subdivisions:** 8 ![Your values should match those shown in this screenshot](https://dev.epicgames.com/community/api/documentation/image/c3b71495-807e-48b2-98ab-1c4597a9664c)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can change the Viewport background from a checkerboard to solid black in the <strong>Viewport Utility Bar &gt; RGB</strong>. This makes it easier to view your graphic.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26262913,
      "caption": "Set the Viewport to a black background using the RGB setting.",
      "alt_text": "Set the Viewport to a black background using the RGB setting",
      "image": {
        "id": 26262913,
        "file_name": "image_34.png",
        "file_size": 77640,
        "content_type": "image/png",
        "created_at": "2025-11-12T17:11:31.170+00:00",
        "height": 742,
        "width": 1212,
        "storage_key": "2377165b-c313-4cdd-aa71-0701aea2a1a4",
        "context": "documentation"
      },
      "storage_key": "2377165b-c313-4cdd-aa71-0701aea2a1a4",
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

1. To recreate the background bar, **right-click** on your **L3\_BG group** and select **duplicate**. The bar’s color will be white, and the bar itself will be offset slightly.
2. Rename the actor to **L3\_BG\_Bar\_Offset**.
3. Place it below your other bar in the Motion Design Outliner. You should see a bit of flickering, since there is nothing governing the priority of the two bars yet.
4. Select your L3\_BG and L3\_BG\_Bar\_Offset actors, and group them by pressing CTRL+G.
5. **Right-click** your new **null actor** at the root of your group and add a modifier called **Translucent Priority**. ![Adding the Translucent Priority modifier](https://dev.epicgames.com/community/api/documentation/image/7d972dae-6f28-4296-bb5b-85ac2e579554)

The **Translucent Priority** modifier automatically sorts the render priority of translucent objects. The first item on the list renders on top of the next item. You can use this on a large nested group of actors, or on individuals. In this tutorial, you are going to use a translucent object at the top of your Motion Design Outliner, and let the Translucent Priority modifier regulate everything.

Move your graphics so they are offset instead of directly on top of each other.

- Offset the L3\_BG\_Bar\_Offset so that the **Z value** is **-170.0**. The result should resemble the following images:

![Your graphic should look like this](https://dev.epicgames.com/community/api/documentation/image/b3356dde-2547-4fe5-bc6c-aa96c9f9a1e2)

![Your UI should look like this](https://dev.epicgames.com/community/api/documentation/image/05ce4d06-d528-452a-8dc8-65332534a059)

_Your graphic and UI should look like this._

## Adding Content in Motion Design

Next, you will add a logo and some text to the bar graphics you already created.

### Adding Text to the Layout

To create some text, return to the **Toolbox**.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "When working with text, remember that for a given text actor, all the characters will share the same settings. If you want individual characters to use different fonts, colors, sizing, and so on, you need to use separate text actors for each character that requires different settings.",
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

![The Motion Design user interface](https://dev.epicgames.com/community/api/documentation/image/5c06000f-40fd-4fa1-bc7e-f18049eb2b34)

_The Motion Design user interface._

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The Motion Design interface is fully described in the <a data-document-id=\"3232791\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-quickstart-guide-in-unreal-engine\">Motion Design Quick Start</a>.",
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

1. In the Toolbox (#2 in the image above, to the left of the Viewport), there is an **Actors** button. Click that button to show all of the different types of actors you can add to your design.
2. Double-click on the **Text Actor** to add it to the root level of your Motion Design Outliner.
3. Drag the new Text actor into the null actor group, so it appears in line with your background and your background bar offset.
4. Rename the actor by double-clicking it in your Motion Design Outliner, and call it **Text\_Line\_1**.
5. With your Text\_Line\_1 actor selected, press **CTRL+G** to group it.
6. Name the group **Text\_Lines** so it is identifiable.
7. You want to have two text lines, so right-click and **duplicate** Text\_Line\_1, then rename the duplicate to Text\_Line\_2.

### Changing the Font

You can set the font of the text by going into your Motion Design Outliner, selecting one of the text actors, and going into your Details panel. There are several buttons you can select; click on the one called **Text**.

In the Details panel at the bottom, with the Text button selected, you can update the content of the text line by changing the string in the text field. You can also change your font and typeface.

1. Change the font to Roboto.
2. Change the typeface to Italic.
3. Shift the position of Line 2 down so the lines do not overlap. ![Setting the font and typeface for your text actor](https://dev.epicgames.com/community/api/documentation/image/90bab6bc-8033-41ea-84e1-eaed8adaabcd)

Notice the text is covered by the green bar. You can correct this by using the Translucent Sort Priority modifier that you set up previously. However, to use that modifier your actor must use a translucent material type.

1. Select one of your text actors, then click on the **Style** button in the Details panel. You’ll see that the Translucency style is set to None, which means the Translucent Sort Priority modifier can't sort it as it is not translucent.
2. Change the style to **Translucent**.
3. Repeat this for the other text actor, and you will now see the text appearing on top of the bar.
4. Selecting the **Text\_Lines** null actor at the root.
5. Click the **General** button in the Details panel.
6. Move the entire group down by shifting the null actor **Location** down, until it overlaps with the bar.
7. Select each text line, and set the **scale** to 0.45 in the transform settings. ![General text actor settings](https://dev.epicgames.com/community/api/documentation/image/e375c9de-e309-4dc2-a63b-1cc7242197ab)

### Text Layout Tools

You now need to use the **Text Layout Tools.**

- With the text selected, click on the **Layout** button in the Details panel. ![Text layout settings](https://dev.epicgames.com/community/api/documentation/image/f407ca19-aa27-4f9a-b188-4fe4af9bebe6)

In this section, you can set a variety of common text properties. You are going to modify a few of them now. Begin with the **Alignment** options.

1. You want to keep the horizontal alignment of your text left-justified, so do not change that option.
2. Change the vertical alignment of each text line to be centered, so select the third option in the second row.

Kerning, Line Spacing, and Word Spacing are also all available here, but you aren’t going to use those now.

1. Manually position Text\_Line1 and Text\_Line2 apart, so that they aren’t right on top of each other.
2. Use the **Max Width** setting to ensure your text stays confined within the layout.
3. Set the value so the text is retained within the borders of your graphics. ![Setting the Max Width value for your text layout](https://dev.epicgames.com/community/api/documentation/image/3fdb846c-6860-49e0-9f71-13f522f5486e)

Here is a comparison of before and after setting the Max Width value to 1550 and adjusting the text position.

```json
{
  "type": "sequence_slider",
  "caption": "Before and after adjusting your text layout.",
  "images": [
    {
      "image_id": 26262997,
      "storage_key": "9d9aacbf-2848-459f-bc82-4ec608bcde47",
      "context": "documentation",
      "image": {
        "id": 26262997,
        "file_name": "image_43.png",
        "file_size": 77207,
        "content_type": "image/png",
        "created_at": "2025-11-12T17:11:41.976+00:00",
        "height": 220,
        "width": 1260,
        "storage_key": "9d9aacbf-2848-459f-bc82-4ec608bcde47",
        "context": "documentation"
      }
    },
    {
      "image_id": 26262998,
      "storage_key": "ca5f8499-a9eb-4fd7-babf-2c2260b223fa",
      "context": "documentation",
      "image": {
        "id": 26262998,
        "file_name": "image_44.png",
        "file_size": 106568,
        "content_type": "image/png",
        "created_at": "2025-11-12T17:11:42.094+00:00",
        "height": 220,
        "width": 1260,
        "storage_key": "ca5f8499-a9eb-4fd7-babf-2c2260b223fa",
        "context": "documentation"
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

Make sure to leave space to the left of your bar for when you add the logo and show name.

### Grid Arrange Modifier

As mentioned above, another way to space out these two lines of text is to use the **Grid Arrange** modifier. To test it out:

1. Select the Text\_Lines root actor and then right-click it.
2. Navigate to the modifiers and select **Grid Arrange.**
3. You will see the following interface: ![The Grid Arrange modifier settings for your text line actors](https://dev.epicgames.com/community/api/documentation/image/11f5d56b-fbe1-498a-8945-ec31b7403b6a)

The two settings that you need to learn to use here are the **Count** and **Spread.**

- Set the **Count** to **(1, 2)** and the **Spread** to **(0.0, 31.0)**.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "When you added the Grid Arrange modifier, the Motion Design Outliner changed. Both the eyeball icons for the editor and runtime visibility for the second actor were disabled. This is because the count for both width and height was set to 1, so these settings were no longer required to be visible.",
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

![Text line actor arrangement after changing the Count and Spread settings](https://dev.epicgames.com/community/api/documentation/image/69aa9959-f3b6-4215-b3f8-b6cb3188e6c7)

_Text line actor arrangement after changing the Count and Spread settings._

This change arranged the text actors, spaced them out, and enabled their visibility in the Details panel. For more dynamic layouts, this sort of logic is necessary, but even for a comparatively more static layout like this tutorial project, it’s an effective tool.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can disable a modifier by clicking the checkmark on either the entire modifier stack or on the individual modifier. This is useful for experimenting and debugging.",
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

### Adding a Logo to the Layout

You will revisit the **Material Designer** here, but before you do, you need to add a piece of geometry to work with.

1. From the **Toolbox**, add a **rectangle** from the 2D shapes.
2. Double-click the rectangle, select it in your Motion Design Outliner, and create a **group** by pressing CTRL+G on your keyboard.
3. Name the group **Show\_ID**, and name the newly-created rectangle **Logo**.
4. Add two text actors to the group, and name them **Banner\_Line1** and **Banner\_Line2**. You are going to use these for part of your banner.
5. Select the whole Show\_ID group, and drag it above the Text\_Lines group in your Motion Design Outliner.

Your Motion Design Outliner should now resemble the following image:

![The Motion Design Outliner after adding the logo actor and banner line text actors](https://dev.epicgames.com/community/api/documentation/image/75298eac-121d-4f11-a3dc-b5aea2edfbbc)

_The Motion Design Outliner after adding the logo actor and banner line text actors._

With those elements in place, you can start building your logo. Click on the logo actor you just added and open the **Material Designer**. As a refresher, this means:

1. Select the actor.
2. Click the **Material** button.
3. Set the **Material Type** to **Material Designer**. Your Material Designer tab now populates to the left of your Motion Design Outliner. This time, you don’t need to unlink the fill and mask. You will apply a texture here that has both channels, so it automatically uses them.
4. Click the dropdown in the properties, and browse to the **UE\_Logo\_icon-only** asset in the **EDC\_Content** folder. You can also drag and drop the texture onto your canvas. Your result should resemble this image: ![Adding the UE_Logo_icon-only asset to the canvas](https://dev.epicgames.com/community/api/documentation/image/83e91164-2e32-472a-90b9-233a66d15dba)
5. Clamp the texture in the Material Designer property list for that layer. ![Enable the Clamp Texture setting](https://dev.epicgames.com/community/api/documentation/image/919c218d-8629-4cf4-937f-bed0c840677b)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can always check the key and fill of your level by selecting <strong>Alpha</strong> using the <strong>Viewport Utility</strong> <strong>Toolbar</strong>:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26262927,
      "caption": "Changing the Viewport to display the Alpha channel.",
      "alt_text": "Changing the Viewport to display the Alpha channel",
      "image": {
        "id": 26262927,
        "file_name": "image_50.png",
        "file_size": 37098,
        "content_type": "image/png",
        "created_at": "2025-11-12T17:11:33.034+00:00",
        "height": 411,
        "width": 1479,
        "storage_key": "f26d08ea-421e-4b03-999f-45046698f0ad",
        "context": "documentation"
      },
      "storage_key": "f26d08ea-421e-4b03-999f-45046698f0ad",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The Viewport changes to show you a view that resembles this image:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26262928,
      "caption": "The Viewport displaying the Alpha channel",
      "alt_text": "The Viewport displaying the Alpha channel",
      "image": {
        "id": 26262928,
        "file_name": "image_51.png",
        "file_size": 25315,
        "content_type": "image/png",
        "created_at": "2025-11-12T17:11:33.125+00:00",
        "height": 765,
        "width": 1252,
        "storage_key": "36c5fda0-eb02-4484-892d-31220dc0bdb5",
        "context": "documentation"
      },
      "storage_key": "36c5fda0-eb02-4484-892d-31220dc0bdb5",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Remember to switch the Viewport back to RGB before continuing to work.",
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

Since the **Material Designer** defaults to translucent materials, you can move the logo into your layout, and it will be sorted correctly as long as it is near the top of the list.

1. Configure the **Banner\_Line1** and **Banner\_Line2** text actors to have the same settings as the two text line actors you created previously.
2. Select each banner line actor, and set them to **Translucent** with an **Opacity** of **1.0**: ![Banner line text actor style settings](https://dev.epicgames.com/community/api/documentation/image/8fd0a8fa-37a9-4070-be81-200faa20e256)
3. Move the whole **Show\_ID** group, using either the handles in the Viewport or by using Transform settings under General in the Details panel, so that the logo is on the left side of your graphic. Your interim result will need further adjustment, and should resemble the following image: ![Work in progress with the banner icon and text needing transforms](https://dev.epicgames.com/community/api/documentation/image/0ab073d6-25f1-434c-8fbc-cbfc5cfbcc1e)
4. Click on your logo to select it.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you find selecting a logo is difficult, you might not have<strong> Translucent Selection </strong>enabled. Enable it by pressing the <strong>T</strong> key on your keyboard, and try selecting it again.",
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

You can resize the logo in two ways:

- Scaling the actual size by using the actor Transform settings under General in the Details panel.
- Changing the scale value in the Material Designer with Clamp Texture enabled.

For now, resize it by using the actor Transform settings. You will use the Material Designer transforms method later to scale the UVs for animating.

- In the Details panel, set the **scale** for all three axes to **0.55**. ![Scaling the logo actor](https://dev.epicgames.com/community/api/documentation/image/a8b7c356-c504-4bec-9324-4b209bac4ff9)

Next, you will work on your banner title.

1. Select Banner\_Line1, and set the text to "The Daily".
2. Set the layout settings for both Banner\_Line1 and Banner\_Line2 to the following: Alignment Horizontal: Left Justified Vertical: Centered Kerning, Line Spacing, and Word Spacing: 0 Max Width, Max Height, Scale Proportionally: Disabled ![Banner line text actor layout settings](https://dev.epicgames.com/community/api/documentation/image/c9862f5f-c4fa-4606-8366-c8ffe6fd0afb)

You don't need the Max Width setting for the banner line text actors, because when you are working with the completed project you will not be able to edit them.

1. Scale and reposition your text until your result resembles the following image: ![Banner icon and text actor after transforms](https://dev.epicgames.com/community/api/documentation/image/2a97babc-79b9-40d1-8708-ff8dbb4e39ab)
2. Change the font of your text to something you like. The examples shown use Roboto Italic for both. Under the Typeface option you can choose between different font weights.

![Adjusting the font and typeface](https://dev.epicgames.com/community/api/documentation/image/58b80ac5-1141-44a3-ae6b-8d4a729148a2)

_Adjusting the font and typeface._

### Viewport Features

The bottom right of the Viewport has several features. For the purposes of this tutorial, only two are relevant: Viewport Snapping and Viewport Guides.

![The bottom right of the Viewport, showing the icons for the features you can access](https://dev.epicgames.com/community/api/documentation/image/c298e5e8-d038-472e-abc1-d2ffefe47806)

_The bottom right of the Viewport, showing the icons for the features you can access._

#### Viewport Snapping

![Viewport snapping options](https://dev.epicgames.com/community/api/documentation/image/5b79aed9-c699-45a9-bf46-14d85fef8fe2)

_Viewport snapping options._

To access Viewport snapping options, right-click on the magnet icon. Each of these is a toggle, and can be configured as you prefer.

- For this example, right-click on the magnet icon and select **Screen & Guide**.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Left-clicking on the magnet icon disables whichever options you’ve selected.",
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

The grid-and-magnet icon immediately to the right provides the option to snap to a grid of a specified size.

![Specifying a grid size for Viewport snapping](https://dev.epicgames.com/community/api/documentation/image/bbeda3ea-16e5-4ea6-b97d-3e0448a6fc7c)

_Specifying a grid size for Viewport snapping._

#### Viewport Guides

To ensure everything is lined up the way you want, you can use Unreal Engine’s built-in guides system. If you click and drag from the rulers at the top and left side of your viewport, you can draw out guides that are useful when you want extra precision.

Drag out two guides to line up with the Unreal Engine logo. To remove a guide, double-click it.

![Using guidelines to arrange actors](https://dev.epicgames.com/community/api/documentation/image/6e8d0395-47bc-4a7a-8f95-85531c8ba491)

_Using guidelines to arrange actors._

If you have a complex set of guides you want to save, click **Camera** in the Viewport, then select **Guide Presets > Save As**.

![Saving your guide preset](https://dev.epicgames.com/community/api/documentation/image/a526a26c-3373-433e-b454-773322af32a1)

_Saving your guide preset._

When you have a saved guide preset, additional options appear under Guide Presets. These are:

- Active: Identifies which saved preset you are currently using.
- Save: Save your current preset.
- Save As: Save your current preset under a new name.
- Reload: Reloads your current preset settings.
- You can select a saved guide preset to populate it to the Viewport.

![The additional options available after you have saved a guide preset](https://dev.epicgames.com/community/api/documentation/image/c2dcf255-cbb0-4884-a7ff-0b1b0b37e466)

_The additional options available after you have saved a guide preset._

At this point, your project should resemble this image:

![The banner, text actors, and logo at this point in the tutorial](https://dev.epicgames.com/community/api/documentation/image/3896fefa-9a51-4078-ba12-6b4a9492b7bc)

_The banner, text actors, and logo at this point in the tutorial._

Save your work before continuing.

### Background Bar Visual Details

Before continuing, try adding a new texture to the background bar on your own, so that it is not a simple white bar, but instead has some additional detail to make it more visually interesting.

After you are done, read through the steps below to see how you did in comparison. If you had trouble, follow the instructions to modify your background bar.

1. Select your white bar background, and click the **Material** button in the Details panel.
2. Set the **Material Type** to **Material Designer**.
3. Click **Edit with Material Designer.** ![The Edit with Material Designer button](https://dev.epicgames.com/community/api/documentation/image/e456a2e4-6307-440f-a288-745e4caad5d7)
4. Add a texture with no alpha channel. ![Using the Add Layer menu to add a texture with no alpha channel](https://dev.epicgames.com/community/api/documentation/image/38876f70-422f-4137-9353-f0a353458515)
5. Change the blend mode to **Multiply** and set your texture controls as follows: Select the texture dropdown, and choose the **linear gradient asset** labeled **2**. Enable **Clamp Texture**. Adjust your UV settings for **Offset**, **Rotation**, and **Scale**. Set Offset to -1.415. Set Rotation to -90. Set Scale so that the X value is 0.029, and the Y value is 1.0. Set the **opacity** to .87. ![The settings for the new texture with no alpha channel](https://dev.epicgames.com/community/api/documentation/image/20b019d3-9e94-470d-91a0-cbabcd829e1a)

Your result should resemble the following image:

![The drop shadow result](https://dev.epicgames.com/community/api/documentation/image/815163e8-7c9c-4c57-95ac-a1f58088c9a8)

_The drop shadow result._

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "A drop shadow like this doesn’t need to be texture gradient-based, and can use normal scene lighting with a real-time shadow. It involves using duplicate geometry for the green backplate, and setting it to be opaque rather than translucent (translucent materials are incapable of casting shadows). Feel free to experiment!",
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

## Animating your Design

Your objective is now to take what you’ve created, have it slide into view from offscreen, and stop in the center. You will also set up the off-animation, where the graphic will retract back off-screen to the left.

### Animate the Banner Graphic

First, select the entire graphic, and set a keyframe where you want it to land.

1. Click on the root null actor. In this example, UE automatically named it Null Actor1. ![The banner graphic null actor](https://dev.epicgames.com/community/api/documentation/image/560f75e7-4591-4e86-a22c-4f2699a61074)
2. In the **Sequencer** panel, advance the playhead to frame 30.
3. Set a keyframe by pressing the **S key** on your keyboard, or by clicking the diamond icon to the right of the **Location** in the **Details** panel **General** settings. ![The set keyframe diamond icon](https://dev.epicgames.com/community/api/documentation/image/6278d789-2aad-445d-914a-0fc6185249f4)
4. Click the keyframe to make a new selection section appear. ![Your new selection section after placing and clicking a keyframe](https://dev.epicgames.com/community/api/documentation/image/92f20b2e-3e06-424a-b1db-0f1a52716e5e)
5. In Sequencer, click the pen icon to the left of the Magnet icon to find and enable **Auto-key**. This feature automatically places a keyframe any time you change the value of the track. ![The Auto-key feature in the menu](https://dev.epicgames.com/community/api/documentation/image/4623d92e-3ed7-4eb8-b1e1-05560463f302)
6. Drag your playhead back to frame 0, and expand your Null Actor1 Transform Location settings in Sequencer: ![Null actor Transform Location settings](https://dev.epicgames.com/community/api/documentation/image/383257f7-81fd-4789-a7a2-f998612ce670)
7. Change your keyframe **Y value** for the root null actor to **-1500**. This takes the entire graphic off-screen, and creates a keyframe at that value, because you enabled Auto-key. You can also set that keyframe by changing the value in the Motion Design Outliner, and clicking the keyframe diamond icon.
8. To have your animation ease into frame, click on the keyframe at the beginning of the move (frame 0 in this case). You should see a graph view in your selection section on the right. ![Graph view of your selection](https://dev.epicgames.com/community/api/documentation/image/31cb859e-53b8-417e-935e-e3b1848d72aa)
9. Clicking the **Selection** drop down menu shows you several options that will save you time when animating. For this example, select **Cubic**. ![The Cubic option in the Selection menu options](https://dev.epicgames.com/community/api/documentation/image/4e4358e7-13b4-4b6a-bd8b-f7becc82d321) ![The Cubic option in the UI after selecting it](https://dev.epicgames.com/community/api/documentation/image/b7e933e9-6e68-4daa-8cd6-776503f1d35e)
10. Next, add a pause to this animation so that you can start working on animating the off-animation. Move the playhead to frame 30, then right-click on it and select **Add Mark**. This creates a mark labeled **A**. You can change the label by right-clicking the A and changing the **Label** property. For now, A is fine as the label. ![Add a mark](https://dev.epicgames.com/community/api/documentation/image/793e970e-e380-4890-accb-c3584f4450c6) ![Your new mark](https://dev.epicgames.com/community/api/documentation/image/150aac62-d2d1-41f0-ac65-4a1879f7010b)
11. Click the button to open the **Sequence** tab, on the right side of the Sequencer panel. ![The Sequence tab](https://dev.epicgames.com/community/api/documentation/image/c1111b29-c37a-40cd-86c2-45f6a9d77a27)
12. Click the **Role** dropdown, and select **Stop**. Marks can have several roles. These include: Mark (default, no function) Stop Pause Jump Reverse ![Mark role options](https://dev.epicgames.com/community/api/documentation/image/4e9bb502-eef3-422a-ae8e-c7fe1d6cb3b1) Choosing Stop means the animation will stop at that point, until you choose to continue and start the off-animation you're going to make.
13. Create another keyframe at the current Y location that you already have at frame 50. You can also press ENTER as a shortcut when the track is selected. You can also create the keyframe for your Sequence by clicking the add keyframe button associated with the Y setting in the null actor Transform Location settings, as shown below: ![The add keyframe button](https://dev.epicgames.com/community/api/documentation/image/63af10be-c2fd-4cc4-aaeb-2583e0bbf24c)
14. Click the first keyframe, press and hold the ALT key, then drag the keyframe to approximately frame 90. This duplicates the original (offscreen) keyframe, and creates a suitable off-animation.
15. Right-click the playhead at frame 70, then select **Set End Time** to remove the unnecessary sections of the timeline.

### Animate the Logo

With the bar now animated, your next step is to animate the Unreal Engine logo you created, using the **Material Designer.**

Animating properties using the **Material Designer** is no different than animating any other property; as long as you have a diamond icon next to the property, the workflow is almost identical.

1. Start by selecting the Logo actor from the Motion Design Outliner.You’re going to give it a scale-down in addition to a fade-in using the layer opacity. ![Using opacity and scale to create an animation](https://dev.epicgames.com/community/api/documentation/image/239c7d5d-5283-4298-b32c-a4df08b05448)
2. Keyframe the opacity. Move the **Sequencer playhead** to frame **8**. Set the **Opacity** value to **0**. Click the keyframe diamond icon and your sequencer will move to that point. Give yourself about 20 frames for the reveal animation. ![Keyframing the opacity](https://dev.epicgames.com/community/api/documentation/image/53e6857c-f184-405e-9418-6617c100ef90)

The images below show the beginning and end values for your move animation. The key changes from beginning to end are as follows:

- Opacity value 0.0 -> Opacity value 1.0
- Scale X value 2.786 -> X value 1.0 Y value 2.786 -> Y value 1.0

```json
{
  "type": "sequence_slider",
  "caption": "Beginning and end values for your move animation.",
  "images": [
    {
      "image_id": 26262999,
      "storage_key": "5cee594d-64ea-4635-a14c-f81947202e70",
      "context": "documentation",
      "image": {
        "id": 26262999,
        "file_name": "image_84.png",
        "file_size": 43764,
        "content_type": "image/png",
        "created_at": "2025-11-12T17:11:42.246+00:00",
        "height": 813,
        "width": 368,
        "storage_key": "5cee594d-64ea-4635-a14c-f81947202e70",
        "context": "documentation"
      }
    },
    {
      "image_id": 26263000,
      "storage_key": "3cb51ec9-008b-4cbd-be57-431b5c02c24e",
      "context": "documentation",
      "image": {
        "id": 26263000,
        "file_name": "image_85.png",
        "file_size": 36343,
        "content_type": "image/png",
        "created_at": "2025-11-12T17:11:42.324+00:00",
        "height": 813,
        "width": 368,
        "storage_key": "3cb51ec9-008b-4cbd-be57-431b5c02c24e",
        "context": "documentation"
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

Your next task is animating the logo mask using the opacity tab.

![Using the opacity tab again](https://dev.epicgames.com/community/api/documentation/image/1b62a95d-d42b-490d-9312-94d3184e9512)

_Using the opacity tab again._

- Assign a texture for masking at the level of the entire material (rather than masking only a layer) from this tab. ![Assign a tearing texture to the material](https://dev.epicgames.com/community/api/documentation/image/e9f52c72-a4d7-4ec7-be53-39424c9b1472)

By adding this tearing texture to the material, no matter what you do in the underlying RGB tab, the texture will mask it.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "What you can do here is limited only by your creativity, and we encourage experimenting with all of the ways you can use keyframes - there’s a huge variety!",
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

## Rigging your Layout and Content with Remote Control

Now that you have designed and animated your graphic, the next step is rigging it to take advantage of **Remote Control**. Remote Control provides a way for you to expose a variety of properties so you can customize them from a central location.

Remote Control also offers a powerful system called **Behaviors**. Behaviors provide for logic operations that offer you even more rigging power. Do you want to switch between different styles (comprising several properties) by controlling the value of a single integer? The combination of Remote Controland Behaviors can help you do so.

- Begin by selecting the **Remote Control** tab. You can find it right next to the Sequencer tab. ![Select the Remote Control tab](https://dev.epicgames.com/community/api/documentation/image/b9fe62cb-b8f8-4ad2-a9ec-982c0a39f19e)
- You can also open it from the main menu under **Window** > **Remote Control Panel**. ![Open the Remote Control tab from the main menu](https://dev.epicgames.com/community/api/documentation/image/00af4d56-08ea-4284-b3b6-dd05feb00b40)

Every Motion Design level comes equipped with a pre-linked remote control preset. When you open the panel, your interface will resemble the following image:

![The Remote Control panel in its initial state](https://dev.epicgames.com/community/api/documentation/image/7e1a5690-0882-4146-9330-00e4485d04d3)

_The Remote Control panel in its initial state._

The Remote Control panel provides a lot of powerful and potentially-complex functionality, but for this use case you only need to use the essential features. You are going to:

- Control your two text lines.
- Using a single control, change the text of the show’s branding, the show logo, and the color of the bar itself.

Begin with the two text lines.

- To **Expose a Property** to **Remote Control**, go into your Motion Design Outliner and select the **Text\_Line\_1** actor.
- When you look at the Details panel, you will see joystick icons. Navigate to the property settings buttons and click **Text**.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "These joystick icons are widespread - Remote Control can control many parts of your project.",
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

![Joystick icons indicate a setting you can control using the Remote Control feature](https://dev.epicgames.com/community/api/documentation/image/129d578d-844a-4e68-aa03-b05c6d793751)

_Joystick icons indicate a setting you can control using the Remote Control feature._

Your interface should now resemble the following image. Under the **Properties** column, your text string is exposed and you can edit it. Whatever change you make to the text string is immediately reflected in your viewport.

![Exposed text strings in the Properties column](https://dev.epicgames.com/community/api/documentation/image/537bbfb5-187b-4b1e-8a40-b2e9a3528fed)

_Exposed text strings in the Properties column._

The **Property ID** column on the left will be important once you control the branding on the left side. Property ID is a way to group up your controls that is useful when you have many exposed properties you want to organize. It is a part of the workflow when you want to set multiple properties from a single source, which this tutorial covers later.

The column to the right of **Properties** is where you can add **Controllers** to your setup. **Controllers** provide a simpler, operator-friendly interface.

- To create a controller for the property you exposed, click and drag the group into the **Controller** column. Your interface should resemble the following image: ![Create a controller for an exposed property](https://dev.epicgames.com/community/api/documentation/image/e9e0c32a-981a-4689-bba2-63cd18bca5e5)

Organizing your controllers is important for making your rigging accessible to an operator, and labeling your fields can help you do so. You can edit the Controller ID and Description fields by double-clicking them, then entering a new alphanumeric string as the value. By default, the Controller ID value is **Text**.

1. Change the Controller ID label to **B100**.
2. Set the Description to **Text - Line 1**.

Your interface should now resemble the following image:

![After changing the Controller ID and Description text fields](https://dev.epicgames.com/community/api/documentation/image/6e0e9e92-f000-4739-92b8-67544c10e49d)

_After changing the Controller ID and Description text fields._

- Repeat the process for your Line 2 text.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Alternatively, instead of repeating the entire process, you can achieve the same result by a more complex but also more efficient means.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "enhanced_list",
      "style": "unordered",
      "items": [
        [
          {
            "type": "paragraph",
            "content": "Delete the Text_Line_2 actor.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Copy and paste the Text_Line_1 actor.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Rename the duplicate actor to Text_Line_2.",
            "settings": {
              "is_hidden": false
            }
          }
        ]
      ],
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "By doing so, a <strong>Tracker Component</strong> is added to the duplicate actor. This process duplicated the actor, and exposed the same properties to Remote Control. The only additional steps to this workflow you need to do are:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "enhanced_list",
      "style": "unordered",
      "items": [
        [
          {
            "type": "paragraph",
            "content": "Check your grid modifier is still spacing out the lines appropriately.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Drag the new actor's exposed group from your <strong>Properties </strong>panel into your <strong>Controller </strong>column.",
            "settings": {
              "is_hidden": false
            }
          }
        ]
      ],
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

Your interface should resemble the following image:

![Your interface after creating a second Text_Line actor](https://dev.epicgames.com/community/api/documentation/image/71be397b-f487-4dfe-93f4-4b06375dd6db)

_Your interface after creating a second Text_Line actor._

- Test out your remote-controlled properties by changing their values in your Controller Column under the **Input** field.

If everything is configured correctly, the effects of your changes will show immediately. Notice that when you dragged your text from the **Properties** panel into the **Controller,** a **Bind Behavior** was added (you can see it in the above screenshot). There are several of these Behaviors - all of which we designed to offer additional automation and logic to simplify your workflow.

With that in mind, you will rig up the logic that will drive the items on the left side of the bar, using the **Conditional Behavior** in tandem with the **Property ID** system.

- Start by exposing the properties you will need to work with. Using the same process you just learned with the Text\_Line actors, expose the following properties:

#### The Logo

1. Click on the logo actor in your Motion Design Outliner and open the Material Designer. ![The button to open the Material Designer associated with your logo](https://dev.epicgames.com/community/api/documentation/image/6efb0071-643d-43a1-ac8a-133377c648d4)
2. Clicking the Remote Control button associated with the logo texture adds a texture controller to your Remote Control panel.
3. In your Remote Control Properties column, highlight the newly exposed texture. Set your property ID (currently listed as **None**) to **100.Logo**.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "100 is the most important part here, but you can use a period to further describe the property in case you have multiple images or colors that you want to label and control.",
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

#### The Show Title text

1. Expose the text fields that comprise **The Daily** and **Hotfix** separately.
2. Assign those to property IDs **100.ShowTitleLine1** and **100.ShowTitleLine2** respectively. Your interface should resemble the following image:

![Assigning property IDs to the text fields](https://dev.epicgames.com/community/api/documentation/image/63ab447e-2b2a-41d2-8317-1cb50511acf1)

_Assigning property IDs to the text fields._

#### The Background Bar Color

1. Click on your BG\_Main actor, or select it in the Motion Design Outliner. If it didn’t automatically open, go into the Material Designer that you already set up.
2. Click on the green bottom layer, and expand your expose options by clicking the **More (⋮)** menu. ![The More menu options](https://dev.epicgames.com/community/api/documentation/image/f8bf2512-2d44-406f-bc39-0fcb9c810e5e)
3. Expose the property, and assign it the property ID **100.Background**.

Your interface should now resemble this image:

![Your interface after exposing all the properties](https://dev.epicgames.com/community/api/documentation/image/dab7a121-24ab-4ee5-9d2f-a90f95ce4f8a)

_Your interface after exposing all the properties._

Now that your exposed properties are set up, the next part is to set up controlling several properties from one integer.

1. Under the **Controller** column, click on the **plus sign** on the left side, and select **Integer**. ![Controller value options](https://dev.epicgames.com/community/api/documentation/image/16c7ddcb-05c9-47af-9bed-f769aa999fc4)
2. Label the Controller ID **A100** for organization purposes.
3. Use the drag handle to the left of the controller ID field for each line to reorder your list manually.
4. Change the description for this property to read **0 = Show 1** | **1=Show 2**.
5. Select the controller, and click on the plus sign in the **Behavior** column to manually add a behavior.
6. Select **Conditional**, and click on the property. ![Add the Conditional Behavior](https://dev.epicgames.com/community/api/documentation/image/6a8f93a2-3ad0-44b7-ab60-963f8478ae30) With this selected, you can choose how to evaluate what you are going to add, but leave it set to **=**.
7. Click the **plus** button next to Actions. ![Click the plus button at the top of the Actions column to add a new action](https://dev.epicgames.com/community/api/documentation/image/4ec08626-f5ba-4c3f-854a-1c0dc540f6d1)
8. From the menu, select **Add specific ID action** > **ID: 100**, as shown in the following image: ![Select a specific ID action using ID: 100](https://dev.epicgames.com/community/api/documentation/image/b7ca431d-f0fa-49aa-858c-d2c4abd543ba)

This collects all the properties with the 100 prefix and adds them all to the Actions column at the same time.

![All the properties with the 100 prefix collected together in the Actions column](https://dev.epicgames.com/community/api/documentation/image/7deb8e85-3bd7-4697-aa7f-bf90fe82bf7c)

_All the properties with the 100 prefix collected together in the Actions column._

Now, when you set that value to **0** in the **Remote Control** controller, it sets all of those values to whichever values you’ve set up for the selected properties. In this case, make sure you set it so that 0 = the Unreal Logo and the green bar.

1. Right-click on the group of properties, and choose **Duplicate**.
2. Double-click the **Condition** field of the duplicate group, and set the value to 1.

Here’s an example of something you can make using this workflow.

![A completed example using the workflow described here](https://dev.epicgames.com/community/api/documentation/image/6fbe723b-152c-4664-a4c7-6b49edabab63)

_A completed example using the workflow described here._

Once this is properly set up, when you press 0, you will see the first banner theme, and when you press 1, you will see the other banner theme.

## Using Storm Sync to Package Your Content

### Exporting a .spak File

You can export your content into a lightweight `.spak` file. This is useful in situations where you’re backing up content without source control, or handing a colleague a full scene and all of its dependent files. Here is how to use this feature for your project.

1. Open the level that you’ve been working on. The example shown here is called `Demo_Working_Project`.
2. Right-click in the viewport and select **Export**: ![Exporting your project to a .spak file](https://dev.epicgames.com/community/api/documentation/image/f747da1b-7298-4749-bb2b-557e4e1ad84b) UE then auto-collects and displays a full list of required files. ![An auto-collected list of files for export](https://dev.epicgames.com/community/api/documentation/image/f3876f5c-f06f-46f0-b493-aff5067d1f84)
3. Click on **Next**. This sends you to an export option screen where you can name your `.spak` file. ![Name your exported file](https://dev.epicgames.com/community/api/documentation/image/8ea9ebbf-544d-4ebe-9e93-9b3fa4d782e1)
4. Name your file, and click **Finish**. You should see a message on the lower right that shows you where your file was saved.

### Importing a .spak File

To import your `.spak` file, drag the file from the directory where you exported it and drop it into your **Content Browser.** You will be presented with a screen to verify the contents of the file before importing it. If UE detects changes between the files in the `.spak` file and what you have in your project, it lets you know, and imports what has changed. If it’s a brand new set of assets, that change list shows everything.

Here is an example of what the list will look like if you don’t already have any of the files:

![The changelist you will see when importing a project from a .spak file](https://dev.epicgames.com/community/api/documentation/image/14a4a00d-981a-4583-9e27-bc8ef271e1d3)

_The changelist you will see when importing a project from a .spak file._

Click **Import** to populate your Content Browser with the necessary files.

## Rundown Tool UI Overview

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Before starting this section, we strongly recommend a two-monitor setup. This will mean you can use one monitor to operate as an output monitor, while the other functions as a place to operate your graphics. Without a two-monitor setup, you will have difficulty following this tutorial.",
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

With everything set up, all that remains is for you to play out your customized content using the **Rundown** tool.

To begin, create a new Rundown by right-clicking in your Content Browser, and selecting **Motion Design > Motion Design Rundown**.

![Create a new Motion Design Rundown](https://dev.epicgames.com/community/api/documentation/image/3cc98e63-308f-4c9e-b656-a8ad63707a7e)

_Create a new Motion Design Rundown._

You can use the **Rundown** tool to add your levels to a central location and create pages that provide a way for you to rapidly generate content to be played out live. The following workflow will serve as a surface-level, fully local overview of the tool for simple playback.

With the right setup, you can have multiple instances of UE running on a network, where a discoverable instance of UE hosting the project you want to play can be controlled by the UE instance running the Rundown and the Rundown’s preview capability.

![The Motion Design Rundown interface](https://dev.epicgames.com/community/api/documentation/image/adbb3742-87e3-4ea0-9770-024b5ca1c361)

_The Motion Design Rundown interface._

Here are some aspects of the Rundown tool interface that are key to this tutorial:

1. Template List: All imported levels are located here, and you can import them by dragging the level from the **Content Browser**.
2. Playback Controls: You can control selected pages from this panel. Taking in/out, continuing, and taking the next item on the Rundown can all be done here. These playback controls refer strictly to actually taking the graphic to air. You can preview before taking by using the Page Preview, which is addressed in item 6.
3. Page List: Dragging any item from the Template List results in creating a page. You can take pages to specific, designated channels. For the purpose of this tutorial, leave it on Channel\_0.
4. Page Details: You can set individual page properties here, such as a text line, integer value, and so on. You can also modify the Page ID and page name from here.
5. Toolbar: The toolbar contains several commonly-used controls, such as saving, adding/removing a new template or page, or setting broadcast settings. There is also a quick access button on the right to Start All Channels and effectively go "on air."
6. Page Preview: Similar to the Playback Controls referenced above, operators can preview the content of a selected page before taking the graphic to air. You can also use **Preview Next** to review the complete list of pages.

## Using the Rundown Tool

Begin by adding your level to the Rundown.

1. Click **Add Template** on the top row, or drag your level directly into the template list.
2. Double-click the **Preview In** button to see what you’re working with.

Your result should resemble the following image:

![Previewing your page in the Rundown tool](https://dev.epicgames.com/community/api/documentation/image/0ce0fea5-020a-4b29-b3e0-8ea0b990e020)

_Previewing your page in the Rundown tool._

Previewing doesn’t mean that you have played your graphic out live on air. You’ll notice that the Take In / Take Out buttons are still grayed out (list item 2 in the interface description).

That is because you now need to drag that template into your **Page List.**

1. Drag the template into your Page List, then click **Continue** on the page preview panel. If everything is functioning correctly, you should see the off-animation that you created animate the graphic away.
2. With your page selected in your Rundown, modify some of the page details. Change the B100 and B200 values to say something other than the default text. Click **Preview In** again.

Your result should resemble the following image:

![Modifying your page's text in the preview](https://dev.epicgames.com/community/api/documentation/image/c27b6222-8b70-42bf-8457-17a0413606b7)

_Modifying your page's text in the preview._

1. Right-click your 0001 page and select **Duplicate**. You are going to make a variation of that page to further experiment with the controls.
2. On the duplicate page, set the value of your A100 property in your page details to 1 instead of 0. With the logic you have in place, the result of using Preview In for your graphic should resemble the following image: ![Creating a duplicate page](https://dev.epicgames.com/community/api/documentation/image/8f54c60b-da63-480b-8683-c4ad9367a4ed)

Now that you have your pages set up and functioning, briefly explore the output of your graphic. For simplicity, this tutorial will focus on a single machine operation where operation and output occur on the same engine.

- Open your **Broadcast Editor** by clicking the Broadcast button: ![Open the Broadcast Editor](https://dev.epicgames.com/community/api/documentation/image/62265d14-2027-4f78-8ac3-7767cab71420)

The **Broadcast** window now appears:

![The Broadcast window](https://dev.epicgames.com/community/api/documentation/image/0144df65-922b-4a97-8eb2-0ebb7c3a648d)

_The Broadcast window._

Under the **Output Devices** list on the right side, you should see the displays that you have available

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "As mentioned previously, you need more than one display.",
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

1. Click the display that you want to output to, and drag it into the Channel\_0 viewport. Your result should resemble the following image: ![The Channel_0 viewport after you drag in your output display](https://dev.epicgames.com/community/api/documentation/image/9820d7d1-2bad-4f5b-b658-26a44c91f659)
2. With your output set up, click the **Start All Channels** button. ![The Start All Channels button](https://dev.epicgames.com/community/api/documentation/image/9fedd569-5db2-415e-a11e-336ad9e1f961)

The screen that you designated for that channel will turn black and show no further activity until you go back to your **Rundown.**

1. For the purposes of this tutorial, designate the monitor that just went black your **Program display**, and designate the other monitor your **Rundown display**.
2. You are currently **Live**. Look at your Rundown display, and click **Preview In** on one of your pages. It will play out on the preview viewport. Assuming the preview looks correct, click **Take In** on the Rundown display. Your previously dark Program display now shows your lower third graphic.

The following image is a composite showing what the display on your two monitors should resemble:

![Your Rundown display on the left, and your Program display on the right](https://dev.epicgames.com/community/api/documentation/image/0e8b873e-707a-4d00-8f37-d3e3c6a1de98)

_Your Rundown display on the left, and your Program display on the right._

- While you are actively outputting to your Program display, select your second page from your Rundown and **Preview In** that page. ![Preview In the Rundown display without changing the Program display](https://dev.epicgames.com/community/api/documentation/image/b8550f63-a50c-4244-8d8f-2f22a2d340dc)

You are now previewing the next page while the Live page is actively displaying.

- Click **Continue** here: ![The Continue button](https://dev.epicgames.com/community/api/documentation/image/0f6fcf60-032f-47f8-9fe8-c2f2682086b0)

The graphic on your Program display animates the off-animation, and leaves the display.

- With your 002 page selected, click **Take In** and your blue lower third graphic will animate to move on to the Program display.

Now that your graphics are set up, play around with the options here to learn how to operate your graphics.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can call up pages from your page list by using your number pad. CTRL+Enter activates Preview In for that page, and Shift+Enter activates Take In to send that page to your Program display. Hover over the other buttons to see their respective shortcuts.",
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
