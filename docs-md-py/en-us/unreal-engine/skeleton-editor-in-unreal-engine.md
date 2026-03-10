# Skeleton Editor

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine

> Application Version: 5.7

In Unreal Engine, [Skeleton Assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletons-in-unreal-engine) are the foundation for all animation work with **Skeletal Meshes**. The **Skeleton Editor Mode** is the visual editor where you can find the tools and properties to make changes to **Skeleton Assets**.

In this editor you can manipulate individual bones and bone structures, attach [Skeletal Mesh Sockets](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-sockets-in-unreal-engine), and preview any **Animation Curves** and **Animation Notifies** associated with your skeleton. The Skeleton Editor is also where you can find the **Retargeting Manager**, a tool for managing meshes associated with the current Skeleton Asset.

Below is the Skeleton Editor window with the following tools and Panels:

![skeleton editor overview window](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3d788844-ca7c-4399-b1de-22baa4ed8705/skeletoneditoroverview.png)

1. [Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine#toolbar)
2. [Skeleton Tree / Retarget Sources](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine#skeletontree/retargetsources)
3. [Viewport](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine#viewport)
4. [Preview Scene Settings / Details](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine#previewscenesettings/details)
5. [Anim Curves / Animation Notifies](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine#animcurves/animationnotifies)

## Toolbar

The Toolbar found in the Skeletal Mesh Editor is similar to the **Toolbar** found across Unreal Engine's many editors and windows. For general Animation Editor functions refer to the [Animation Editors Overview's Toolbar Section](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-editors-in-unreal-engine#toolbar) for more information. The following are features unique to the Skeletal Mesh Editor Mode.

![skeleton editor toolbar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/36918827-f69f-4929-89ca-96c96f52cf50/toolbar.png)

| Name | Icon | Description |
| --- | --- | --- |
| **Anim Notifies** | animation notifies animnotifies icon button | Opens the [Animation Notifies](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine#animation notifies) panel where you can manage the animation notifies associated with the skeleton. |
| **Retarget Sources** | retarget sources icon button | Will open the [Retarget Sources](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine#retargetsources) panel where you can manage retarget sources and setups with the current skeleton asset. |
| **Import Mesh** | import mesh icon button | Imports a new mesh for this skeleton. |
| **Make Static Mesh** | make static mesh icon button | Makes a new static mesh out of the preview's current pose. |

## Skeleton Tree / Retarget Sources

This panel features the Skeleton Tree tab by default. After clicking Retarget Sources in the Toolbar, the [Retarget Sources](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine#retargetsources) tab will also appear here.

### Skeleton Tree

Skeleton Tree tab displays the **Skeletal Hierarchy** of the current Skeleton Asset, which allows you to create and edit [Skeleton Sockets](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-sockets-in-unreal-engine) and define settings related to [Animation Retargeting](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine#retargetsource).

![skeleton tree window](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8867c4a-95fc-40fa-8655-f9c2a4b6fc78/skeletontree.png)

1. Using the green **Plus** (**+**) button, assets and profiles can be added to your skeleton. Below you will find a list of the assets the Plus (+) button can create.

   | Name | Description |
   | --- | --- |
   | **Socket** | Sockets are offsets from bones that allow you to attach game objects to skeletons. |
   | **Virtual Bone** | Virtual Bones are auxiliary bones that are children of a bone but constrained to another. |
   | **Add Time Blend Profile** | A Time Blend Profile is a set of per-bone scales that can be used in transitions to tweak the weights of specific bones, relative to the transitions' blend time. |
   | **Add Weight Blend Profile** | A Weight Blend Profile is a set of per-bone scales that can be used in transitions to tweak the weights of specific bones, relative to the transitions' blend weight. |
   | **Add Blend Mask** | A Blend Mask is used to specify the alpha of individual bones when layering poses. (It is used by the Layered Blend Per Bone node and the Pose Watch.) |
2. The **Gear** icon to the right of the Search Bar will open a menu providing settings and toggle filters you can use to alter Skeleton preview and skeleton tree behavior. Below you will find a description of each property and a description of its function.

   | Setting | Description |
   | --- | --- |
   | **Blend Profiles** | Select the Blend Profile you want to preview and edit with the current Skeleton Asset. The profile from the base Skeleton Asset will appear as a column in the Skeleton Tree tab displaying each bone's weight in the form of a slider. The Clear option at the bottom of the Blend Profiles header will clear the currently selected Blend Profile. blend profiles window |
   | **Add Time Blend Profiles** | Add a new Time Blend Profile for this skeleton. |
   | **Add Weight Blend Profiles** | Add a new Weight Blend Profile for this skeleton. |
   | **Add Blend Mask** | Add a new Blend Mask to this skeleton. |
   | **Show Retargeting Options** | Opens a new column in the Skeleton Tree showing each bone's **Bone Translation Retargeting** mode. The selectable options are:  * **Animation**: Displays translation data from the associated animation. * **Skeleton**: Shows translations from the associated Skeleton. * **Animation Scaled**: Shows translations from the associated animation, but scales the length by the current skeleton's proportions. * **Animation Relative**: Uses relative translations from the associated animation similar to an additive animation. * **Orient and Scale**: Orients and scales a uniform translation. |
   | **Filtering Flattens Hierarchy** | A visual filter that determines whether to display the above hierarchy or flatten it when searching for tree items. |
   | **Hide Parents When Filtering** | A visual filter that determines whether to show the parent items as grayed out, or hide them entirely. |
   | **Show all Bones** | Shows all bones in the current skeleton. |
   | **Show Mesh Bones** | Shows all bones used in the current mesh. |
   | **Show LOD Bones** | Shows all bones that are used in the current LOD. |
   | **Show Weighted Bones** | Shows all bones that have vertices weighted to them. |
   | **Hide Bones** | Hides all bones, but will still list any sockets and attached assets. |
   | **Show Active Sockets** | Shows mesh and skeleton sockets, hiding the skeleton sockets that have a customized mesh socket. |
   | **Show Mesh Sockets** | Shows any sockets that are in the mesh only. |
   | **Show Skeleton Sockets** | Show any sockets that are in the skeleton only. |
   | **Show All Sockets** | Shows all sockets that are in the mesh and skeleton. |
   | **Hide Sockets** | Hides all sockets. |

### Bone Manipulation

The **Bone Manipulation** tool is useful for previewing animations with altered bone positions. Using Bone Manipulation, you can preview how skeletons interact with other assets and even create new animations by assigning altered bone positions using the Timeline Record.

To use the Bone Manipulation Mode, select the desired Bone in the Skeletal Tree Window. You can now see the highlighted bone has a **Manipulator** in the Viewport and you can now manipulate the Bone through **Transform** (**W**), **Rotation** (**E**) and **Scale** (**R**).

![bone manipulation window](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a5f6cefb-ebdd-4535-b693-a47321cbf9c0/bonemanipulationmode.png)
