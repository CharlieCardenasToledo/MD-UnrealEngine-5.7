# Third Person Template

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/third-person-template-in-unreal-engine

> Application Version: 5.7

![Hero image of the Third Person arena with a mannequin running.](https://dev.epicgames.com/community/api/documentation/image/57d46f36-2800-4438-9ccc-c0df900114cd)

When you create a new project, **Unreal Engine** gives you a list of templates you can choose from. These templates contain some ready-to-use assets, such as level geometry, a character you can control, and simple character animations. Many tutorials use one of these templates as a starting point.

In a third-person game, by default, the player sees the game world from a camera that's located at a fixed distance behind and slightly above their character. In Unreal Engine, you can control camera distance and position, and adjust it as needed.

The **Third Person** template in Unreal Engine 5 contains the following elements:

- A playable third-person character that can move and jump.
- Additional meshes for the character.
- A level with basic geometry (ramps, platforms).
- Physics-enabled cubes that react when the player collides with them.

The template also comes with redesigned mannequins.

### Creating a Third Person Project

Launching Unreal Engine opens the **Project Browser** window, where you can choose to open an existing Unreal Engine project or create a new one.

To create a third-person project, select the **Games** category on the left, and then select the **Third Person**template.

![Image of landing page for launching a template option, third person is selected.](https://dev.epicgames.com/community/api/documentation/image/50767a3d-d34f-4716-b5d3-c347ca8fef3a)

### Variants

The next set of options in creating your project are located in the **Variants** dropdown menu. Variants give you a way to build select gameplay styles faster. The Third Person template offers three specialized variants: Combat, Platforming, and Side Scroller.

![Image of Variants dropdown menu options.](https://dev.epicgames.com/community/api/documentation/image/97c6167f-e613-410b-8d92-43395ab9f3a9)

_Choose the None option for the standard template._

For a deeper dive into the features of these variants, see [Variants in Games Templates](https://dev.epicgames.com/documentation/en-us/unreal-engine/variants-in-game-templates).

#### Combat Variant

The **Combat** variant delivers combat mechanics, enemy targeting, and a built-in health management system to efficiently build action-oriented games.

![Image of two characters in the combat arena.](https://dev.epicgames.com/community/api/documentation/image/493d749d-87bd-4a6c-91d6-faa1cc25d736)

#### Platforming Variant

The **Platforming**variant delivers advanced jumping, climbing, and dynamic movement mechanics with precise control.

![Image of the platforming variant gameplay terrain.](https://dev.epicgames.com/community/api/documentation/image/d1b94399-1a90-450c-a229-5eb08492da8c)

#### Side Scroller Variant

The **Side Scrolle**r variant adapts the third-person perspective to a side-scrolling format, with pre-configured camera and movement systems.

![Image of a character moving through a side-view oriented gameplay space.](https://dev.epicgames.com/community/api/documentation/image/0bb13702-05cd-4630-a602-6b57a2340166)

There are several additional settings you can configure for your Third Person project. For an overview of these, refer to the [Creating a New Project](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-a-new-project-in-unreal-engine?application_version=5.6) page.

After following these steps, you now have a basic level with a third-person character you can control.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Why don't you try out your new level? In the main toolbar at the top of the editor, click <b>Play</b>. Use the <b>WASD</b> keys to move your character, press the <b>Space</b> bar to jump, and look around by moving the mouse.",
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

## Template Contents

The Third Person template contains all of the basic elements of a simple third-person experience. You can use it as a starting point for a traditional role-playing game (RPG), third-person shooter, or any other kind of application. The following section details the main template elements and where to find them in the **Content Browser**.

### Third-Person Character

Assets for the player character are located in the `Content/Characters` folder. By default, the Third Person template starts with the feminine Unreal Engine 5 mannequin. This folder contains additional **Skeletal Meshes** for the player character, both in the style of Unreal Engine 5 and the legacy Unreal Engine mannequin.

| Female Mannequin: Quinn (default) | Male Mannequin: Manny |
| --- | --- |
| ![Image female mannequin.](https://dev.epicgames.com/community/api/documentation/image/289eb92c-88b7-4754-ba8a-4bd5fece0fa1) | ![Image male mannequin.](https://dev.epicgames.com/community/api/documentation/image/941dd369-d4f3-42cc-b513-927d4fd6bd55) |

Unreal Engine mannequins also come with configurable Level of Detail (LOD) settings. LODs help optimize your application for different platforms.

For example, applications targeting mobile platforms (Android, iOS) should use less detailed character models. This helps improve the application's performance on these platforms. The **Data Asset** that controls mannequin LODs is located in the `Content/Characters/Mannequins/Meshes` folder.

### Animations

Animations for Unreal Engine mannequins are located in the `Content/Characters/Mannequins/Animations` folder. There are two sets of animations specific to the two mannequins.

The **Animation Blueprints** make full use of the new [IK Rig](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-ik-rig?application_version=5.6) system in Unreal Engine. Unlike legacy animations, the IK Rig can be used to dynamically modify pose-based solver parameters. An example of this can be seen in the screenshots below: the position of Quinn's feet adjusts dynamically to match the kind of terrain she is standing on.

| ![Quinn in a step position.](https://dev.epicgames.com/community/api/documentation/image/abd9e25e-d264-4db6-b99c-2083800e9910) | ![Quinn on an angled incline.](https://dev.epicgames.com/community/api/documentation/image/fc169ef8-55b2-447e-9c3c-ebb4b4a20337) | ![Quinn facing front with feet flat on ground.](https://dev.epicgames.com/community/api/documentation/image/974cfe58-0731-478b-bf19-9bc0a85557ed) |
| --- | --- | --- |

To see how this was implemented, have a look at the **CR\_Mannequin\_BasicFootIK** rig in the `Content/Mannequins/Rigs` folder.

Also in the `Rigs` folder, the **CR\_Mannequin\_Body** Control Rig asset can be used to easily pose and animate the mannequin directly in the editor. To learn more about how to pose and animate with Control Rig, refer to the [Control Rig](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-in-unreal-engine?application_version=5.6) documentation.

### Level

The assets that make up level geometry (static meshes, materials, and textures) are located in the `Content/LevelPrototyping` folder.

## Improving Your Project

Now that you have a playable level, you can start to import content and adjust things to make your game more interesting and unique.

### Character

You can change your character's appearance by changing its **Static Mesh**. As an example, let's change the default mannequin mesh. To do this, follow these steps:

1. In the **Content Browser**, go to `Content/ThirdPerson/Blueprints`, then double-click the `BP_ThirdPersonCharacter` Blueprint to open it in the Blueprint Editor. ![Image file structure for content to third person to blueprints with key image.](https://dev.epicgames.com/community/api/documentation/image/e690f5f8-3480-4c34-8e58-5a4ae2a97b4e)
2. In the Blueprint Editor, in the Components panel, click the Mesh(CharacterMesh) Component to select it. ![image blueprints page with mesh selected in the components menu.](https://dev.epicgames.com/community/api/documentation/image/8d586b43-c1e5-4851-bcfb-8e49e4d009be)
3. With the Mesh(CharacterMesh) Component selected, find the Details panel on the right side of the Blueprint Editor. Then, in the Mesh section, click the drop-down next to the Skeletal Mesh parameter and select `SKM_Manny` from the list. ![In the Details menu, select mesh, then the Manny mesh.](https://dev.epicgames.com/community/api/documentation/image/5f34a062-c84e-4d19-9a88-719c018a8719)
4. Still in the **Details** panel, in the **Animation** section, set the following options: Animation Mode: **Use Animation Blueprint** Anim Class: **ABP\_Manny** ![Image of menus to change animation class.](https://dev.epicgames.com/community/api/documentation/image/6f9821c7-6db2-45d9-8881-d589ecadec5b) Compile and Save the Blueprint. ![Image of compile in menu and save icon.](https://dev.epicgames.com/community/api/documentation/image/23c13f4e-530d-4730-9366-0940aab9bf02) Click the Viewport tab to confirm that the mesh has updated. ![Image of viewport tab with mannequin.](https://dev.epicgames.com/community/api/documentation/image/9c716c8b-c110-4c55-91f0-cf83c01f69e8)

Your character can already run and jump, but you can also add other types of character movement, like walking or crouching. For a detailed tutorial, see [Setting Up Character Movement](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-character-movement?application_version=5.6).

### Level

Your level already has some simple geometry, like stairs and platforms. The easiest way to add more content inside is to drag-and-drop it from the **Content Browser**.

If you chose to include **starter content** when you created your project, you should already have some things you can drag-and-drop into your level.

For an introductory tutorial on level design, see [Level Design Tutorial](https://dev.epicgames.com/community/learning/tutorials/GjpX/unreal-engine-ue-5-6-preview-level-design-tutorial-for-beginners-p1-ue5-unrealengine-leveldesign).

## What's Next?

Now that you've gone through the basics of creating a third-person experience, here are some other things you can try:

- In-depth tutorials: [Retarget animations](https://dev.epicgames.com/documentation/en-us/metahuman/retargeting-animations-to-a-metahuman-at-runtime) to a MetaHuman [Import and configure](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-skeletal-mesh-pipeline-in-unreal-engine?application_version=5.6) a different FBX model for your player character
- Download premade characters from [Fab](https://www.fab.com/)
- Populate your level with free content and props from [Quixel Bridge](https://dev.epicgames.com/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.6). You can build a variety of indoor and outdoor environments, and new content is added regularly.
- Add some fancy visual effects to your game, like motion blur or vignette, by using [post-processing effects](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine?application_version=5.6).
- Refine how your [skeletal meshes](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-rendering-paths-in-unreal-engine) are rendered, or learn to update your 3D imported data through a [Datasmith tutorial](https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-tutorials-in-unreal-engine).
- Add AI characters using [Behavior Trees](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-trees-in-unreal-engine?application_version=5.6). You can set them up to chase, flee, help, or harm the player.
