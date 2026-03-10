# Cinema 4D

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-datasmith-with-cinema-4d-in-unreal-engine

> Application Version: 5.7

This page describes how Datasmith imports scenes from Maxon Cinema 4D into Unreal Editor. It follows the basic process outlined in the [Datasmith Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-plugins-overview) and [About the Datasmith Import Process](https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-import-process-in-unreal-engine), but adds some special translation behavior that is specific to Cinema 4D. If you're planning to use Datasmith to import scenes from Cinema 4D into Unreal Editor, reading this page can help you understand how your scene is translated, and how you can work with the results in Unreal Editor.

![Cinema 4D](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b7afc169-875d-45c8-a4bd-bc333a86055a/c4d-ue4-comparison-c4d.png)

![Unreal Engine](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fa8aa030-1bb7-49b2-99d0-058eac010f10/c4d-ue4-comparison-ue4.png)

***Credit:** The classroom scene used on this page is courtesy of [Turbosquid](https://www.turbosquid.com/) user [scripter](https://www.turbosquid.com/Search/Artists/scripter).*

## Cinema 4D Workflow

Datasmith uses a **Direct** workflow for Cinema 4D. This means that to get your Cinema 4D content into Unreal using Datasmith, you need to do the following:

1. In Cinema 4D, save your scene to a `.c4d` file. From the main menu in Cinema 4D, do one of the following:
   * If you are using a more recent version of Cinema 4D, select **File > Save Project for Cineware** option.
   * If you are using an older version you might need to select **File > Save Project for Melange** instead.
2. In Unreal Engine, enable the **Datasmith C4D Importer** Plugin for your Project. To learn how to enable a plugin, see [Working wih Plugins](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine).
3. In Unreal Engine, use the Datasmith import options to import the `.c4d` file into your project. For instructions, see [Importing Datasmith Content into Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-datasmith-content-into-unreal-engine).

In Cinema 4D versions prior to R22, you can configure Cinema 4D to automatically include the information Datasmith needs when you save a `.c4d` file.

1. From the main menu, select **Edit > Preferences**.
2. On the **Files** tab of the **Preferences** dialog, enable the following options:

   * **Save Polygons for Melange**.
   * **Save Animations For Melange**.

Enabling these options increases the size of the files you save. If file size is a concern, or you frequently work with Cinema 4D scenes that you don't need to import into Unreal Engine, you may prefer to use the **File > Save Project for Melange** option only when you need it.

## Geometry

Datasmith creates a Static Mesh Asset for each visible geometric object in the Cinema 4D scene.

The object name that you see in the Cinema 4D Properties panel is the name Datasmith assigns to the corresponding Static Mesh Asset in Unreal Engine.

To influence the granularity of the Static Mesh Assets and Actors that Datasmith creates, you can merge objects in Cinema 4D before you export the scene.

For example you can do the following:

* Use the **Connect Objects** command in Cinema 4D to merge two objects into a single object. See [Connect Objects](https://help.maxon.net/c4d/en-us/#html/5666.html) in the Cinema 4D documentation.
* For more flexibility, use the **Connect Object** in Cinema 4D to combine objects that are closer than a given threshold value into a single mesh. In this case, the Datasmith importer produces a single Static Mesh Asset for the combined mesh, but the connected pieces remain separate objects in Cinema 4D. See [Connect Object](https://help.maxon.net/c4d/en-us/#html/OCONNECTOR.html) in the Cinema 4D documentation.

### Object Visibility

If you have objects that you don't want to import into Unreal Engine at all, hide them in Cinema 4D before you save your `.c4d` file. The Datasmith importer does not import geometry of hidden objects into Static Mesh Assets, and does not include them in the Datasmith Scene hierarchy.

You can use the **Objects** panel in Cinema 4D to hide the objects individually. Alternatively, you can put the objects you want to omit into their own layer, then use the **Layers** panel to hide all objects in that layer.

### Generators and Deformers

When you save your Cinema 4D scene for Melange, every generator in your scene is *baked* down to a single triangular mesh that represents the total procedurally generated geometry of the object. Similarly, every deformer is baked to a single triangular mesh based on the final state of the deformer. Datasmith imports each of these triangular meshes as a single Static Mesh Asset.

### Instances, Cloners, and Arrays

If you use instances, cloners, or arrays in your Cinema 4D scene to place copies of a single object at multiple different locations in your scene, Datasmith respects your intention by creating a single Static Mesh Asset in your Content Browser from that object's geometry. It then places multiple instances of this Static Mesh Asset into the Datasmith Scene.

### Normal Facing Directions

The Unreal Engine, like most real-time renderers, automatically culls triangles that face away from the camera in order to maximize performance. However, Cinema 4D can render geometry with or without this [backface culling](https://help.maxon.net/c4d/en-us/#html/45030.html). Depending on how you set up Cinema 4D, you may not be used to taking the facing direction of your surfaces into account. If your scene contains single-sided geometry for which the surface normals of the faces point away from the typical viewing direction, that geometry may seem to disappear when viewed from certain angles in the Unreal Engine.

For example, the image below shows a book that was modeled with one of its surface normals facing inward. After the scene is imported into Unreal, the front cover at first appears to be missing. In this case, flipping the normal direction of the surface makes the sides appear as they should.

![Book in Cinema 4D](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8f169928-fbd7-46ac-bb27-51241bb2ed20/backface-compare-c4d.png)

![Book in Unreal Engine](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/994ad06a-234c-45b6-80c6-8690ce285248/backface-compare-ue4.png)

You can avoid this problem by verifying in Cinema 4D that your surfaces are facing in the direction you expect. There are a few ways you can do this. For example:

* You can enable the **Options > Backface Culling** setting for your viewport. This hides all faces whose normals are pointing away from the camera, the same way they are hidden in Unreal Engine.
* When you are in Polygons mode, selected faces show up with a yellow highlight when they are facing toward you, but a blue highlight when facng away from you.

  ![Back faces are blue](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/091f9a90-3450-4f76-a842-76792ef5d0c6/backface-facingcolor.png "Back faces are blue")
* You can configure your viewport to show vertex normals as white lines that extend from the center of each face. Choose **Options > Configure** and go to the **Attributes** panel. Make sure the **Polygon Normals** setting is enabled, and disable its **Selected Only** option to visualize the normals for all faces in the model that you have selected while you're in Polygons mode.

  ![Show vertex normals on all surfaces](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/329c70a1-1791-446f-bfbf-c98ce9d65dce/viewport-attributes.png "Show vertex normals on all surfaces")

When you find faces with inversed normals in Cinema 4D, you can flip them around using the **Reverse Normals** command. See the [Cinema 4D documentation](https://help.maxon.net/c4d/en-us/#html/5670.html).

For a complete discussion and more possible solutions, see [Datasmith Import Process](https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-import-process-in-unreal-engine).

## Lights

Datasmith converts most types of lights from Cinema 4D into equivalent light types in Unreal Engine. This translation preserves the most important emissive properties of the light, including its placement in the scene, color, photometric intensity, cone angles, IES profile, and more.

The following table describes how Datasmith maps Cinema 4D light types into Unreal Engine light types:

| Cinema 4D | Unreal Engine |
| --- | --- |
| Point light, IES light | [Point Light](https://dev.epicgames.com/documentation/en-us/unreal-engine/point-lights-in-unreal-engine) |
| Spot light, Target light | [Spot Lights](https://dev.epicgames.com/documentation/en-us/unreal-engine/spot-lights-in-unreal-engine) |
| Area light, PBR light | [DatasmithAreaLight Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-import-process-in-unreal-engine#lights) |
| Sun light, Infinite light | [Directional Lights](https://dev.epicgames.com/documentation/en-us/unreal-engine/directional-lights-in-unreal-engine) |

## Cameras

For each camera in your Cinema 4D scene, Datasmith creates a CineCamera Actor in the Datasmith Scene. This camera is placed at the same position and rotation as its counterpart in Cinema 4D, and preserves some optional settings related to the camera's physical characteristics, including its focal length.

## Scene Hierarchy

When Datasmith imports a Cinema 4D scene into Unreal Engine, it creates a hierarchy of Actors that closely matches the hierarchy of objects in Cinema 4D. Datasmith preserves object names and hierarchical relationships as closely as possible, but might not be able to create an exact match.

Possible differences include:

* **Object ordering:** In Unreal Editor the **Outliner** orders Actors at each level of the hierarchy alphabetically. Actors might appear in a different order than their counterpart objects in Cinema 4D, but it does not affect their hierarchical relationships.
* **Object names:** The names of the Actors Datasmith creates can only contain alphanumeric characters, hyphens, and underscores. If the name of a Cinema 4D object contains any other characters, Datasmith converts them to underscores automatically.
* **Baking procedural elements:** During the import process, Datasmith bakes procedural features of the Cinema 4D scene, and replaces them with sets of static Actorsthat replicate their effects. This can affect the final hierarchy in Unreal Engine. See the next section for details.

### How Datasmith Bakes Cinema 4D Procedural Features

Datasmith imports each procedural object in the Cinema 4D scene (for example, a generator, cloner, or array) into Unreal Engine as a single parent Actor with the same name as the original Cinema 4D object.

Under each parent Actor, Datasmith creates Static Mesh Actors that simulate the effect of the procedural geometry. These Static Mesh Actors have the same name as their parent Actors, but with a numeric suffix.

If you use procedural features extensively in Cinema 4D, it can produce complex scene hierachies when Datasmith imports your scenes into Unreal Engine. However, you do have access to each individual Actor as a separate instance in Unreal Engine.

## Layers

When you import a Cinema 4D scene, Datasmith imports every named layer that has at least one object in it. It does not import empty layers, meaning layers in the Cinema 4D scene that have no objects in them. Datasmith assigns Level Actors it creates in Unreal Engine to the same Layer their counterpart objects are assigned to in the Cinema 4D scene.

To view imported layers, use the Layers panel (see [Layers Panel](https://dev.epicgames.com/documentation/en-us/unreal-engine/layers-panel-in-unreal-engine))

## Cinema 4D Materials

Datasmith creates a new Material Asset in the Unreal Engine Project for each Standard Material and Physical Material in your Cinema 4D scene.

The goal of these Material Assets is to respect the way you've set up the surfaces to look in Cinema 4D, while exposing properties that help you take advantage of Unreal's physically based renderer.

To modify a Material:

1. Double-click it in the **Content Browser**. Or, select an Actor in your Level that uses the Material you want to modify, and double-click the Material in the **Details** panel.
2. You'll open the Material Instance Editor shown below, where you can use the settings in the **Details** panel to modify the properties imported from Cinema 4D. You can also modify other built-in parameters exposed by the Unreal renderer.

For more information about how to use the Material Instance Editor, see [Material Instance Editor UI](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui).

### Working with Material Channels

When you edit a Material imported from Cinema 4D, the top of the **Details** panel lists the different types of Cinema 4D channels that Datasmith handles during the import process. If you're used to working with materials in Cinema 4D, the effect of these channels and their settings should be familiar to you already.

![Material channels](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d04d28da-6df7-4034-88db-416c98f5293a/material-channels.png "Material channels")
