# Using Transparency in Materials

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-transparency-in-unreal-engine-materials

> Application Version: 5.7

When creating certain surface types such as water or glass, you need the ability to make the surface not only see through, but also give the surface a sense of depth and color.
In the real world, these properties are referred to as **Transparency** or **Opacity** and the two often used interchangeably to describe the same thing. In Unreal Engine, **Transparency** and **Opacity** have two distinct meanings.

* **Transparency** is used to define whether or not a surface can be seen through.
* **Opacity** is used to define degree to which a surface transmits light. In other words, the opacity value determines how transparent or opaque (how see-through / hon see-through ) a surface is.

In the following tutorial you will learn everything you need to know about how to use transparency in your Unreal Engine Materials.

## Transparency

**Transparency** is the term used to describe a surface's ability to block or allow the passage of light. For example, a brick is an object that has no transparency. Stained glass transmits some but not all light, and therefore it is a surface with transparency. You can use transparency to simulate a variety of different real world surface types, including those listed below.

* Hair
* Glass
* Water
* Smoke or Fire Visual Effects
* Clouds
* Impact Decals
* Foliage

## Transparency and Opacity

In Unreal Engine, transparency works by assigning each pixel an **Opacity** value between 0 and 1. When **Opacity** is 1, the surface is fully opaque, meaning it blocks 100% of the light that hits it. When **Opacity** is 0, the surface allows all light to pass through. Opacity values between 0 and 1 yield pixels that are partially see-through. The image below shows opacity values increasing from 0 to 1 on a Static Mesh.

![Opacity values scale](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f9a492a7-18b4-4e32-9fb0-047a65b0292a/trans_opacity_settings.png)

You can also define opacity with a greyscale texture. The image below demonstrates how a texture can help define which parts of a mesh should have transparency and how transparent they should be. The texture is a gradient that goes from black at the top (or fully transparent) to white at the bottom (or fully opaque). The areas in the middle have a varying degree of opacity based on how close to black or white the pixel in the texture is.

![Opacity ramp](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3fda9b33-afae-417b-8ed3-eeaa0935b8fa/trans_ramp_example.png)

## Using Transparency in Materials

You can set up transparent Materials using the following steps:

This tutorial uses assets from the Unreal Engine **Starter Content**. If you did not include the Starter Content in your project, read the [Migrating](https://dev.epicgames.com/documentation/en-us/unreal-engine/migrating-assets-in-unreal-engine)
content page for information about how to move content between projects. This way you can add the Starter Content to your current project and not have to make a new one.

1. First **Right-Click** in the **Content Browser** and then select **Material** from the **Create Basic Asset** section of the context menu.

   ![Create new Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/958c6a4f-778c-40bc-9220-ba732e826bac/create-material.png)
2. Name the Material **TransparentMaterial** and then open it by **Double-Clicking** the Material thumbnail in the **Content Browser**. The Material Editor opens.
3. Click in the background of the Material Graph to display the Material properties in the **Details** panel. Under the **Material** section change the **Blend Mode** from **Opaque** to **Translucent**.

   ![Set translucent blend mode in details properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0d8a8eb9-700f-4bf6-aabe-1103697be3c0/translucent-blend-mode.png)
4. Now that the **Blend Mode** has been correctly set, add the following Material expressions to your graph. You can find the nodes by typing their names into the search bar in the Material palette. Once found **Left-click** and drag them from the palette into the Material Graph.

   * **Vector Parameter** x 1
   * **Scalar Parameter** x 1![Add parameter expressions to graph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/889c16d5-bbfd-4316-9cf3-fd39367ab3e2/add-parameter-expressions.png)
5. Rename the Vector Parameter node to **BaseColor** and give it a color value. Connect the output of the Vector Parameter node into the **Base Color** input on the Main Material Node.
6. Rename the Scalar Parameter to **Opacity** and give it a default value of 0.5. Plug the Scalar Parameter into the **Opacity** input on the Main Shader Node.

   ![Completed transparent graph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1b508cf4-f982-453d-8e40-075dae215a0d/default-transparency-value.png)
7. Click **Apply** and then **Save** in the Material Editor toolbar to compile the Material and save the asset.

   ![Apply and Save Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f0a0a9b6-58ba-4375-9b6b-20f18b24e705/save-apply.png)
8. Find the **TransparentMaterial** asset in the **Content Browser**, right-click the thumbnail and select **Create Material Instance** in the context menu.

   ![Create Material Instance](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/154f2f55-e3fa-494a-aca9-7e2c0bb64b85/create-material-instance.png)
9. Inside the **Content Browser**, navigate to the **Shapes** folder in the Starter Content. Left-click and drag the **Shape\_Sphere** Static Mesh into the viewport and release the left mouse button to spawn it in the level.

   ![Add sphere to level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/81e161bb-42af-462e-8ac1-b47cfafa6c23/place-sphere-in-level.png)
10. Find the **TransparentMaterial\_Instance** asset in the Content Browser. Left-click and drag the Material instance onto the sphere and release the left mouse button to apply it to the mesh.

    ![Apply Material to object](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a91edbab-4d1a-4573-a173-137c9e91bfff/apply-transparent-material.png)
11. Open the Material Instance by **Double-Clicking** on it in the **Content Browser**. In the Material Instance Editor, override the **OpacityAmount** parameter by checking the box next to the parameter name. Once enabled you can adjust the value of **OpacityAmount** to change how transparent the object will be.

## Transparency & Reflections

Objects that make use of transparency can display scene reflections if the following options are set. However keep in mind that having a lot of translucent Materials that have reflections enabled could cause performance issues.

1. Open the **TransparentMaterial** that was created above by **double-clicking** it in the **Content Browser**. In the **Details** panel under the **Translucency** category, change the **Lighting Mode** from **Volumetric NonDirectional** to **Surface TranslucencyVolume**.

   ![Surface translucency volume settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/414aa772-2cc1-451a-85e9-5572d5a90890/surface-translucency-volume.png)
2. Inside the Material Graph, select the **OpacityAmount** parameter and duplicate it twice by pressing **CTRL + D** on the keyboard. When completed, your Material Graph should look something like this.

   ![Duplicate Material expressions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3e6a90fc-414e-4868-a76b-8204aea27b42/duplicate-expression.png)
3. Rename the new Material Expression nodes to **Metallic** and **Roughness**. Set the default value of the **Metallic** Material Expression to 1.0 and set the default value of **Roughness** to 0. Then connect each Material Expression node to the corresponding input on the Main Material Node.

   ![Translucent reflective Material graph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ab47be85-8d32-4b90-8878-5a2df49227ea/metallic-roughness-defaults.png)
4. Click **Apply** and **Save** the Material Editor toolbar and then close the Material Editor.

   ![Apply and Save Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5d266d25-c8e5-4641-9d2b-60362fcd0d3e/save-apply.png)
5. You should now be able to see reflections on the spheres in your level.

   ![Transparent Material with reflections in level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/36daeb5d-d4a5-4ecb-bc98-5af02a3323a7/transparent-reflective-example.png)

By adjusting the parameters of the Material Instance, you can make the Transparency have extremely different looking results.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/00cac85a-d785-4581-8c7d-f90372f56c47/trans_reflection_different_results.png)

## Tinted or Colored Transparency

With the **Thin Transparent** Shading Model and Material expression, you can accurately represent tinted and colored transparent Materials, such colored glass and plastics. This Shading Model enables white specular highlights with correctly tinted background color for transparent surfaces.

![Standard Translucent Shading Model](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fadaeef6-3578-4d2d-a29d-5d6539fbfe37/transparency.png)

![Thin Translucent Shading Model](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c870a340-d14b-43a8-9ce5-7a5f3fd449d8/thintransparency.png)

An example of a Thin Translucent Material Graph is shown below.

Click to enlarge image.

Configure the Material with the following properties in the **Details** panel:

* Change the **Blend Mode** to **Translucent.**
* Change the **Shading Model** to **Thin Translucent.**
* In the Translucency category, change the **Lighting Mode** to **Surface ForwardShading.**

Add a **Thin Translucent Material** expression to the graph and connect a Constant3Vector or a Vector Parameter to the input. This node controls color tint of the transparent surface.

## Translucent Colored Shadows

Translucent Materials are able to cast colored shadows with light transmission in some cases. The amount of light that passes through the Material is determined by its opacity values and how much light is being cast onto the Material.

![Translucent colored shadows](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e5ee3474-7c91-461e-82fa-65083e84b500/colored-translucent-shadows.png)
