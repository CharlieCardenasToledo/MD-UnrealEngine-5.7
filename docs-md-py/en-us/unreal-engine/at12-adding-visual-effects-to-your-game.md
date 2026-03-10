# Add Visual Effects to Your Game

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/at12-adding-visual-effects-to-your-game

> Application Version: 5.7

In this tutorial you’ll learn how to create a fire **Visual Effect (VFX)** and add it to the traps in your level.

## Before You Begin

Make sure you understand **how to create a material**, which is covered in the [Create Materials and Material Instances](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-03-create-materials-and-material-instances) module of this track.

You’ll work with the following assets:

- **BP\_FireTrap** Blueprint

## Niagara Overview

The **Niagara VFX System** is the primary tool to create visual effects (VFX) inside Unreal Engine. The system comes with a variety of premade visual effects that can be customized and placed directly inside your level. You can also create your own visual effects for full customization.

To learn more about Niagara, read the [Niagara Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-niagara-effects-for-unreal-engine) documentation.

## Create a Niagara System

Now, you’ll create your first **Niagara System** that uses a regular emitter. To create a new Niagara System, follow these steps:

1. Go to the **Content Browser** and navigate to the **Content > AdventureGame > Artist** folder. Right-click the Artist folder and select **New Folder**. Name it **VFX**.
2. In the new **VFX** folder, right-click anywhere in the asset area, go to **FX**, and select **Niagara System**. ![Image](https://dev.epicgames.com/community/api/documentation/image/bb19b2d9-4ca9-4506-8773-5957e4e5ab64)
3. The **Create Niagara System** window opens. Here, you can select an emitter or system as a base for your visual effect. If you select a system, it will create a Niagara System that uses one or more emitters. If you select an emitter, it will create a Niagara System that uses a single emitter. Select the **Hanging Particulates** emitter and click **Create**. ![Image](https://dev.epicgames.com/community/api/documentation/image/a19dca29-182f-4cbf-92cf-b6c3d92b84cc)
4. Name this asset **NS\_HangingParticles** and open it.

In the **NS\_HangingParticles** window, you’ll see two nodes: **NS\_HangingParticles** and **HangingParticulates**.

![Image](https://dev.epicgames.com/community/api/documentation/image/01589560-60c4-4e8a-a424-e8716eb2129c)

The **NS\_HangingParticles** node is the system node, listing options such as the **Properties** for the entire system, and two stages named **System Spawn** and **System Update** where you can add modules that execute when Unreal Engine creates the system (Spawn) and while the system is active (Update).

![Image](https://dev.epicgames.com/community/api/documentation/image/99ee959a-9abe-4ad4-b0dc-49afac35c207)

The **HangingParticulates** node is the emitter. This is the node that defines how the particles are generated and rendered.

![Image](https://dev.epicgames.com/community/api/documentation/image/98b58887-eda5-439f-bad6-0dcd61115727)

If you right-click anywhere in the **System Overview** graph, where the nodes are located, you can add new emitters to this system. Alternatively, you can use the **E** key as a shortcut to add a new emitter.

![Image](https://dev.epicgames.com/community/api/documentation/image/c83d212b-112f-4bc4-bd33-1f6b699b1028)

Adding a new emitter opens the **Add Emitter to your System** window. This is similar to the previous window where you created your system, but only displays the base emitters available (since you already created the system). For this example, close the window without adding another emitter.

The **HangingParticulates**emitter comes with pre-defined modules that generate the particles visual effect – similar to small dust particles. In the top-left corner of the window, you can see your effect in the **Preview** panel.

![Image](https://dev.epicgames.com/community/api/documentation/image/b2393986-ede5-4264-be02-f937135abffa)

Now, you’ll increase the **Spawn** **Rate** of this emitter to increase the number of particles that get spawned. Follow these steps:

1. Select the **HangingParticulates**node.
2. Using the **Details** panel, navigate to the **Spawn Rate** category.
3. Change the **SpawnRate** field to **250**. ![Image](https://dev.epicgames.com/community/api/documentation/image/d87cbd1a-9e47-45bc-b0b8-503738af5ebc)

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can also select the <b>Spawn Rate </b>module on the emitter to only see options related to that module in the Details panel.  ",
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

In the **Preview** panel, you’ll now see many more particles rendered.

![Image](https://dev.epicgames.com/community/api/documentation/image/8d9d28b0-2fa1-4da7-a55b-901379443287)

In the bottom part of the window, you can see a timeline used to animate the system. You can press the **Pause** or **Play** button to control the preview.

![Image](https://dev.epicgames.com/community/api/documentation/image/8302b77d-9ba3-430a-ac54-7685dd5db0b1)

Now, you’ll add this system to your level to see it in context. Follow these steps:

1. Go to the **Content Browser** and navigate to the **Adventure Game > Artist > VFX** folder where you created the **NS\_HangingParticles** asset.
2. Drag the **NS\_HangingParticles** asset into the world. You’ll now see your visual effect simulated in the level. [Video: V_Zfi9pu](https://dev.epicgames.com/community/api/cms/videos/V_Zfi9pu/embed.html)

## Create a Fire Effect

In this section, you’ll create a fire effect for your traps.

### Create the Material

To create an animated fire effect, you will use a texture that contains a series of still images that when displayed in a sequence appear to animate a flame. This type of texture is called a **SubUV texture** and it can be animated via the material or Niagara emitter.

First, you’ll create a material using the provided fire texture. Follow these steps:

1. Go to the **Content Browser** and navigate to the **AdventureGame > Artist > Materials** folder.
2. Right-click anywhere and create a **Material**.
3. Name this asset **M\_Fire\_SubUV\_Simple** and open it.

To set up the material, follow these steps:

1. In the **Details** panel, under the **Material** category: Change the **Blend Mode** to **Translucent**. Change the **Shading Model** to **Unlit**. ![Image](https://dev.epicgames.com/community/api/documentation/image/91e36c4b-fde4-40f6-87a1-a62755557125)
2. Right-click in the Material Editor and create a **ParticleSubUV** node. ![Image](https://dev.epicgames.com/community/api/documentation/image/2a020eab-49a1-46b9-9d0e-468a019c6620)
3. Select the **Particle SubUV** node, and in the **Details** panel, change the **Texture** to the **T\_Fire\_SubUV** file. ![Image](https://dev.epicgames.com/community/api/documentation/image/eeca0830-c2ba-41e2-9fdb-c3f94a992bda)
4. From the **Particle SubUV** node, drag the **RGB** pin and add a **Multiply** node (under the **Math** category).
5. From the **Multiply** node, drag the output pin and connect it to **M\_Fire\_SubUV\_Simple** node’s **Emissive Color** input. ![Image](https://dev.epicgames.com/community/api/documentation/image/f38a0f35-b7f8-4138-a1b7-e77f71639b4d)
6. Right-click an empty area below the **Particle SubUV** node and add a **Particle** **Color** node (under the **Particles** category).
7. Drag its **RGB** output pin and connect it to the **Multiply** node’s **B** input pin. ![Image](https://dev.epicgames.com/community/api/documentation/image/420d306a-e26e-4752-ab58-0fdd061fbf34)
8. From the **Particle SubUV** node, drag the **R** output pin and add a new **Multiply** node.
9. From the **Particle Color** node, drag the **A** output pin and connect it to the new **Multiply** node’s **B** input pin. ![Image](https://dev.epicgames.com/community/api/documentation/image/6d0a015c-a06f-4d3a-ba67-cc0b68bef7c5)
10. From the new **Multiply** node, drag the output pin and add a **Clamp** node.
11. From the **Clamp** node, drag the output pin and add a **Depth Fade** node.
12. On the **Depth Fade** node, change the **Fade Distance** field to **60**. ![Image](https://dev.epicgames.com/community/api/documentation/image/09558f34-dd40-4b62-b341-459a080f8e96)
13. From the **Depth** **Fade** node, connect the output pin to the **M\_Fire\_SubUV\_Test** node’s **Opacity** input pin. ![Image](https://dev.epicgames.com/community/api/documentation/image/83f77e11-57e3-46ed-b3ba-4a6da3d3ff48)

The preview of the material should now look similar to this:

![Image](https://dev.epicgames.com/community/api/documentation/image/37bf09f7-22df-4daf-8348-ee0efa62b296)

This material sets its emissive color to be the shape of the ParticleSubUV texture tinted (colorized) by the Particle Color, which comes from the Niagara System. The opacity is set by using the Particle Color's Alpha (transparency) value and normalized between 0 - 1. Finally, we use a DepthFade node to hide any particles that are overlapping (clipping) with nearby geometry in the level.

## Create the Niagara System

Next, you’ll create the Niagara System that generates the fire visual effect. For the fire effect, you will use a **Lightweight (stateless) emitter**. These emitters are optimized for better performance compared to traditional (stateful) emitters, but are limited to a specific set of modules.

To learn more about Lightweight emitters, read the [Niagara Lightweight Emitters Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-lightweight-emitters-overview) documentation.

Follow these steps to create a new Niagara system:

1. Go to the **Content Browser** and navigate to the **AdventureGame > Artist > VFX** folder.
2. Right-click anywhere and go to **FX** and select **Niagara System**.
3. In the list, select **Minimal Lightweight** and click **Create**. Note that you can also use the search field at the top of the window to find the system. ![Image](https://dev.epicgames.com/community/api/documentation/image/22b6c43d-61b0-4cfb-867e-a5d6f9d3141b)
4. Name this asset **NS\_LW\_Fire** and open it.

Next, you’ll set up the modules of the emitter. Follow these steps:

1. Select the **Minimal** emitter node. ![Image](https://dev.epicgames.com/community/api/documentation/image/41db4872-46e8-4109-ae53-c85f03939187)
2. In the **Details** panel, under the **Emitter** **State** category, change the **Loop Duration** to **5.0** **s**. ![Image](https://dev.epicgames.com/community/api/documentation/image/a344ee55-fc2d-4158-b9fd-819619f5ab29)
3. Under the **Spawn Burst Instantaneous** category: Next to the **Spawn Burst Instantaneous** headline, click the **Type** dropdown and change it to **Rate**. This will change the Spawn Burst Instantaneous module to a **Spawn Rate** module. ![Image](https://dev.epicgames.com/community/api/documentation/image/ba4365d0-414a-43c3-ae7e-46831fbafc7d) Change the **Spawn** **Rate** field type to **Binding**. ![Image](https://dev.epicgames.com/community/api/documentation/image/9d8e9343-651d-4ae4-b11e-23d52f2ce4c9) ![Image](https://dev.epicgames.com/community/api/documentation/image/de87df7e-d5df-4d24-81b2-e85a8b83cae2) Go to the **User Parameters** panel in the bottom-left corner of the window. Click the **Plus** button next to the User Parameters category, to add a new parameter. Select **Make New > Common > float**. ![Image](https://dev.epicgames.com/community/api/documentation/image/baf6f9dd-d37a-4bb2-a7ba-12ac4aff0d54) Name this parameter **FireSpawnRate**. Change the value of the **FireSpawnRate** parameter to **20**. ![Image](https://dev.epicgames.com/community/api/documentation/image/07a77501-e504-401c-bfd4-658db854c345) Select the **Minimal** emitter, and in the **Details** panel, change the **Spawn** **Rate** field’s value to **FireSpawnRate** using the dropdown. ![Image](https://dev.epicgames.com/community/api/documentation/image/358d5a50-fc97-4173-bd8e-64472fb9e6c3)
4. With the emitter still selected, in the **Details** panel, go to the **Initialize** **Particle** category and change the **Lifetime** field to **5.0 s**. ![Image](https://dev.epicgames.com/community/api/documentation/image/c888f61a-259c-4dee-9504-b9805996f49a)
5. On the emitter, press the **Plus** button next to the **Simulate** stage and add a **Shape Location** module. ![Image](https://dev.epicgames.com/community/api/documentation/image/e4fcdfe7-56c1-4a08-849d-5060036df0ea)
6. Select the new module and in the **Details** panel, set the **Shape Primitive** to **Plane**. This distributes the fire particles across a flat plane. You can reduce the **Plane Size** if you want, but for this tutorial, you can keep it at **100** by **100**. ![Image](https://dev.epicgames.com/community/api/documentation/image/3402c5ec-9384-4f21-92c2-bfdba58ec99b)
7. On the emitter, under the **Simulate** stage, add a **Add Velocity** module.
8. Select the module, and in the **Details** panel: Set **Velocity** to **Non-uniform Range**. ![Image](https://dev.epicgames.com/community/api/documentation/image/2b7c16f4-5e3d-4e4f-a145-a36bae1eb250) Set the **Velocity** field’s **Min Z** value to **5** and **Max Z** to **10**. This will move the particles upward slowly. ![Image](https://dev.epicgames.com/community/api/documentation/image/baa4052e-5a08-4b05-b5f3-952a52165c7d)
9. On the emitter, under **Simulate**, add a **Scale** **Color** module.
10. Select the module and in the **Details** panel, set the **Scale** type to **Color Range**. ![Image](https://dev.epicgames.com/community/api/documentation/image/8c0cac46-105d-40e7-82a5-6ce50544dde1) ![Image](https://dev.epicgames.com/community/api/documentation/image/e0ab7fd8-6d1f-4143-868d-1f26a3ea5298)
11. Click the **Min** color field and change the **Hex sRGB** to **FFA91300**.
12. Click the **Max** color field and change the **Hex sRGB** to **FF4747FF**. ![Image](https://dev.epicgames.com/community/api/documentation/image/37a846c9-d775-4880-8119-e4828c8b7699) This will set the color of each particle accordingly.
13. On the emitter, under **Simulate**, add a **Scale Sprite Size** module and set the range to **5** and **8**. This will resize the particles to make them significantly larger. ![Image](https://dev.epicgames.com/community/api/documentation/image/eaee8c81-0a34-47bd-8048-d49cb4e64e84)
14. On the emitter, under **Simulate**, add a **Sub UV Animation** module. ![Image](https://dev.epicgames.com/community/api/documentation/image/254d4f0e-e0d4-4946-8cd9-3f247502c08d)
15. On the emitter, under the **Render** category, select the **Sprite Renderer** module.
16. In the **Details** panel, update the following fields: Change the **Material** to the **M\_Fire\_SubUV\_Simple** material you created. Change the **Alignment** to **Velocity Aligned**. Change the **Facing** **Mode** to **Face Camera**. Under the **Sub UV** category, change the **Sub Image Size** to **6** and **6**. ![Image](https://dev.epicgames.com/community/api/documentation/image/f122fcd0-7da1-42f6-aaa2-8dd8b4af1357)

The reason you entered the Sub Image Size of 6 x 6 is because the T\_Fire\_SubUV texture has 6 rows and 6 columns.

![Image](https://dev.epicgames.com/community/api/documentation/image/9f914529-d2e2-4a3a-8f70-2b266391073f)

You can now see the preview of your new fire effect!

[Video: V_xf011L](https://dev.epicgames.com/community/api/cms/videos/V_xf011L/embed.html)

### Add the Fire Effect to the Fire Traps

Lastly, you’ll need to add the fire effect to the trap blueprint so that the fire effect plays on each trap while the trap is active. Follow these steps:

1. Go to the **Content Browser** and navigate to the **AdventureGame > Designer > Traps** folder.
2. Open the **BP\_TrapFire** blueprint.
3. In the **Components** panel, select the **Base** component, click **Add**, and add a **Niagara Particle System Component**. ![Image](https://dev.epicgames.com/community/api/documentation/image/3fc1bffa-6091-40db-b99f-a440017ce020) ![Image](https://dev.epicgames.com/community/api/documentation/image/d815f895-8826-4282-b6b9-18c06ac2ceae)
4. Select the **Niagara** component and in the **Details** panel, under the **Niagara** section, change the **Niagara System Asset** to the **NS\_LW\_Fire** you created. ![Image](https://dev.epicgames.com/community/api/documentation/image/4dd90978-0d48-4780-8e0b-08258755d9f0)
5. In the Blueprint Editor, open the **EventGraph** tab. This is what it looks like now: ![Image](https://dev.epicgames.com/community/api/documentation/image/cd342211-45d6-4619-bfa9-c124bc539a89)
6. Before the **Stop node** on the top row you’ll add two new nodes to deactivate the fire effect. Remove the connection between the **Stop** and **Set Material** nodes by holding **ALT** and left-clicking the connection between them. Make some space between the nodes. ![Image](https://dev.epicgames.com/community/api/documentation/image/ad3b4689-fce4-403b-85e4-465b2545f23e) Right-click in the middle and add a **Deactivate Niagara** node. Note that this node is named after the Niagara component you added earlier; for example, **Deactivate [Component]**, so the name may differ from what’s shown here. ![Image](https://dev.epicgames.com/community/api/documentation/image/82ea7b57-9448-4d50-9710-094dc023df4c) Connect the **Set Material** node to the **Deactivate Niagara** node. Connect the **Deactivate Niagara** node to the **Stop Audio** node. ![Image](https://dev.epicgames.com/community/api/documentation/image/7672fd5d-9c28-402c-91de-19d2943a5f81)
7. Now, you’ll repeat these steps for the row below this one, where **Set Material** and **Play Audio** take place.
8. Follow the same steps as before, and add an **Activate Niagara** node instead. ![Image](https://dev.epicgames.com/community/api/documentation/image/fa2a207a-522f-4ab5-b49d-8ae8a7a7283e)
9. **Compile** and **Save** your Blueprint.

Your **EventGraph** should now look like this:

![Image](https://dev.epicgames.com/community/api/documentation/image/4adaf849-f313-4efa-a693-6912104cfd36)

Next you'll add the ability to modify the **FireSpawnRate Niagara User Parameter** you created earlier from the trap blueprint. In this example, you are modifying the fire spawn rate, but this technique can be used to modify any number of user parameters in your Niagara System.

To modify the user parameter, follow these steps:

1. In the Blueprint Editor, go to the **Construction Script** tab.
2. Create a new float variable and name it **FireSpawnRate**.
3. Select the new variable and do the following: Change the **Category**to **Setup**. This will categorize FireSpawnRate with the other variables under the Setup category. Change the **Default Value** to **10**. This ensures that each new instance of the fire trap in the level will start with visible particles. Enable **Instance Editable** to turn this variable public.
4. In the graph, drag from the **Parent: Construction Script** node's exec pin and add a **Set Niagara Variable (Float)** node. On this node: Enter '**FireSpawnRate**' to the **In Variable Name** text field. This refers to the parameter you created in the Niagara system. Make sure you spell the name exactly as it appears inside your Niagara System. Drag the In Value pin and add a **Get FireSpawnRate** node. This refers to the variable you created in this blueprint. Drag the Target pin and add a **Get Niagara** node, which refers to the Niagara component you added to the blueprint.

**Save** and **Compile** the blueprint. Your **Construction Script** graph should now look like this:

![Image](https://dev.epicgames.com/community/api/documentation/image/27b12a6f-11c3-4a07-8267-3753548fef39)

It’s time to play your game and see the fire effect! Since you added the fire effect to the trap blueprint asset, you don’t have to add the visual effect to your level, or change any of the traps manually. The traps automatically gain the fire effects.

[Video: V_xyXuJv](https://dev.epicgames.com/community/api/cms/videos/V_xyXuJv/embed.html)

### Hide the Fire Trap Base Mesh

To hide the fire trap's square mesh so you only see the fire effect in game, follow these steps:

1. Return to the `BP_TrapFire` blueprint.
2. In the **Components** panel, select **TrapBase**.
3. In the **Details** panel, go to the **Rendering** category and enable **Hidden in Game**. ![Image](https://dev.epicgames.com/community/api/documentation/image/24ee620e-641b-4a54-937e-2d52f310239a)
4. **Compile** and **Save** the blueprint.

Now when you play the game, you'll only see the fire effect on the level floor.

![Image](https://dev.epicgames.com/community/api/documentation/image/f88fe24c-20e5-4d9c-a10b-3f134a3b954b)

### Modify the Fire Spawn Rate

You can use the **FireSpawnRate** variable you created earlier to change the number of fire particles each individual trap produces.

To modify the fire spawn rate, follow these steps:

1. In the **Outliner** panel, use the search field to search for **BP\_FireTrap**. Alternatively, you can unfold the **Room2** folder to see all of the fire traps in room 2. Select all **BP\_FireTrap** actors. In the **Details** panel, under the **Setup** category, change the **Fire Spawn Rate** field to **20**.

You'll notice how the number of fire particles spawned changes based on the number you input. You can keep trying different values until you find the right amount for your game!

[Video: V_9A3syu](https://dev.epicgames.com/community/api/cms/videos/V_9A3syu/embed.html)

Keep experimenting with your effect and see what you can create! To learn more, see [Creating Visual Effects](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine).

## Example Project

Below is a link to download the final sample project that you can build using this tutorial series. You can use this example project to see what your final project might look like, or as a reference to see how we built and designed the project.

```json
{
  "type": "attachment",
  "attachment_id": 44777,
  "caption": "Download the Artist Track Example Project here",
  "attachment": {
    "id": 44777,
    "file_name": "adventureartist.zip",
    "file_size": 78148382,
    "content_type": "application/zip",
    "created_at": "2026-02-04T20:01:13.583+00:00",
    "original_url": "https://d1iv7db44yhgxn.cloudfront.net/documentation/attachments/181fe7fd-4d04-4bac-a32f-f2f84f18350d/adventureartist.zip"
  },
  "settings": {
    "is_hidden": false
  }
}
```

## Next Up

Congratulations on finishing the Artist Track Tutorial Series! You learned to work with materials, post-process effects, lighting, audio, and Niagara visual effects to perform an art pass on your level.

If you are interested in packaging your project as a standalone program to test and share, see the following documentation:

- Related Document
