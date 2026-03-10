# Animation Attributes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-attributes-in-unreal-engine

> Application Version: 5.7

Custom node attributes can be imported in your FBX [Animation Sequences](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine) for creating varied animation data-driven setups. Unlike other animation data, such as [Curves](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curves-in-unreal-engine), attributes are stored per-sequence and support various property types.

This document provides an overview of how to import and reference animation attributes in Unreal Engine.

#### Prerequisites

* You are familiar with [creating custom attributes](https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2019/ENU/Maya-Basics/files/GUID-C7385EC4-74E1-4F6E-8C9D-60F5CCDA7994-htm.html) on nodes in Autodesk Maya.
* Your project contains a [Skeletal Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine).
* You are familiar with importing [Animation Sequences](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine).

## Importing Attributes

To start importing animation attributes in your Animation Sequence, you must ensure that a Bone contains an attribute with animation. Typically, this is done in DCC software, such as Autodesk Maya. In this example, the **root Bone** has a custom float attribute.

![custom attribute in maya](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aacb5c8d-8c32-4420-83df-9b5623369b67/import1.png)


The currently supported attribute data types for importing are **Floats**, **Integers**, **Strings**, and **Transforms**.

### Project Settings Setup

In order for attributes to import correctly, you will need to ensure they are defined in your Project Settings. From the main menu in Unreal Engine, go to **Edit > Project Settings**, navigate to the **Engine > Animation** section, and locate the **Custom Attributes** settings. The following settings are available:

![project settings custom attributes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/57059a83-1190-4fce-9287-e7f863e6f86a/projectsettings.png)

| Name | Description |
| --- | --- |
| **Bone Timecode Custom Attribute Name Settings** | A list of timecode-related properties and their default mappings to custom attributes. You can change these settings to map to different timecode attributes if your project is using different attribute names.   * **Hour Attribute Name** is an **Integer** attribute and is set by default to **TCHour**. * **Minute Attribute Name** is an **Integer** attribute and is set by default to **TCMinute**. * **Second Attribute Name** is an **Integer** attribute and is set by default to **TCSecond**. * **Frame Attribute Name** is an **Integer** attribute and is set by default to **TCFrame** * **Subframe Attribute Name** is a **Float** attribute and is set by default to **TCSubframe** * **Rate Attribute Name** is an **Integer** attribute and is set by default to **TCRate**. * **Takename Attribute Name** is a **String** attribute and is set by default to **Takename**.  timecode custom attributes  These will be included in the list of attribute names to import and will act as if they were added to the Bone Custom Attributes Names array. |
| **Bone Custom Attributes Names** | An array where you define your custom attribute names to search for when importing animation. Defining an attribute name on this list will search all Bones in your skeleton for the attribute.  Click **Add (+)** to add an attribute to the list, then fill in the following properties:   * **Name**, which is the name matching your custom animation attribute. * **Meaning**, which is an optional field where you can define additional context for this attribute.  bone custom attribute names |
| **Bone Names with Custom Attributes** | An array where you can define a list of Bones to filter for custom attributes when importing animation. Defining a Bone on this list will cause all custom attributes to import from that Bone when importing animation.  Click **Add (+)** to add an item to the list, then define a Bone name. bones names with custom attributes |
| **Attribute Blend Modes** | An array where you define how certain attributes behave during blends. This overwrites the global **Default Attribute Blend Mode** per attribute.  Click **Add (+)** to add an item to the list, define an attribute name, then set the blend mode:   * **Override** will overwrite the custom attribute value based on the highest weight during the blend. * **Blend** will set the average value of the custom attribute between the animations according to their weight.  attribute blend modes |
| **Default Attribute Blend Mode** | The default blend mode to use for all custom attributes. Similar to **Attribute Blend Modes**, you can select from **Override** or **Blend**. |
| **Transform Attribute Names** | The transform node name to search for when importing [transform attributes](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-attributes-in-unreal-engine#transformattributes). |

Depending on how you want to import custom attributes, you may want to set values on either **Bone Custom Attribute Names** or **Bone Names with Custom Attributes**. For example, if you wanted to import two custom attributes created on the **root Bone**, you could either:

* Create two array entries under **Bone Custom Attributes Names**, and match the names to your attributes.

  ![bone custom attribute names example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/66749331-9b62-4f7b-8085-5b54781ffdb9/projectsettings7.png)
* Create an entry under **Bone Names with Custom Attributes**, and name it **root**.

  ![bone names with custom attributes example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0dc7827a-1cfa-495d-bc2d-812494c91ba7/projectsettings8.png)

After you set up your custom attribute project settings, you can [import your Animation Sequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine) containing the custom attributes. When importing the FBX, ensure that **Import Custom Attribute** is enabled.

![import custom attribute](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6f160421-105f-4e45-b002-aeb4749e75b9/import2.png)
