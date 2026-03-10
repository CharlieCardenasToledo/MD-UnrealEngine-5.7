# Controls, Bones, and Nulls

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/controls-bones-and-nulls-in-control-rig-in-unreal-engine

> Application Version: 5.7

The primary rig elements used when creating robust rigs in Control Rig are **Controls**, **Bones**, and **Nulls**. Each of these elements have wide-ranging applications and can be used together to create complete rigs.

This document provides an overview of Controls, Bones, and Nulls, and provides simple workflow examples for using them.

#### Prerequisites

* You have created and opened a [Control Rig](https://dev.epicgames.com/documentation/en-us/unreal-engine/rigging-with-control-rig-in-unreal-engine#createcontrolrigasset) for a skeletal mesh.

## Elements Overview

Controls, Bones, and Nulls are created by right-clicking in the **Rig Hierarchy** panel and selecting one of the options from the **New** menu.

![new bone new control new null](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/efaf1664-96bd-4215-b2ba-0ce498a08718/creation1.png)

By default, creating one of these elements will locate it at the origin (0,0,0) of the viewport. If you have an element selected in the Rig Hierarchy panel, it will instead create it at the location of, and parented to, that selected element. This makes it easy to align your elements with each other, using this selection context.

![create control](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9d870ffd-b418-4123-a3a3-3ebf91cfbf95/creation2.gif)

### Organization

Elements can be renamed by right-clicking them in the **Rig Hierarchy** and selecting **Rename** or by pressing **F2**.

![rename control](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/618cd69a-4965-4c0c-8fef-0a8475f3420f/rename.png)

Elements can be re-organized by dragging them in the **Rig Hierarchy**.

* Dragging an element onto another element parents it to that element.
* Dragging an element to an empty region unparents it.
* Pressing **Shift+P** also unparents selected elements.

![control drag drop reparent](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0197a825-8f7a-49b9-a96c-cf0a81a61997/reparenting.gif)

## Controls

**Controls** are the main elements used for your Control Rig interaction. They are used to drive your Bone chains, animate in **Sequencer**, and provide additional custom attributes. You can also customize your Controls to have different [shapes and colors](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-shapes-and-control-shape-library-in-unreal-engine), property types, and transform limits.

### Creation Context

When creating Controls relative to a Bone, the Control will automatically inherit the same name as that Bone and apply `_ctrl` as a suffix.

![create control](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/91cb3791-c2e4-45df-9a18-2f8ada44e625/controlcreation1.gif)

#### Creating Multiple Controls

In addition to the normal creation method, you can also create Controls when multiple Bones are selected using a provided [Python script](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-python-scripting-in-unreal-engine#editorstartup). In the [Rig Hierarchy](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-editor-in-unreal-engine#righierarchy), select multiple Bones, then right-click on them and select **New > Add Controls For Selected**. This will create Controls for all selected Bones, matching their names with the suffix `_ctrl`, and matching the hierarchy structure.

![add controls for selected](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/da17696a-edeb-4014-bcb3-f988f3ca3281/addcontrolsselected.gif)

You can customize this creation method by holding **Alt** and clicking **New > Add Controls For Selected**. This will open a dialog window where you can customize the following settings:

![add controls for selected options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f96c1b8-0c53-4406-aa32-0c234e2e0db4/addcontrols2.png)

| Name | Description |
| --- | --- |
| **Output Format** | How to organize the controls once created. You can select the following options:   * **Hierarchy**: Copies the same hierarchy as the selected Bones, with the top-most control unparented from the Bone hierarchy. * **List**: Unparents all created Controls so they appear at the root of the Rig Hierarchy as a flat list. * **Child**: Parents all created Controls underneath the associated Bone. |
| **Suffix** | The text to apply after the Control name, which is copied from the Bone name. |
| **Prefix** | The text to apply before the Control name, which is copied from the Bone name. |

### Control and Value Types

There are a variety of Control types that you can specify for Controls which provide alternative or more limited properties for it. This can be useful if you are wanting to create attribute-based Controls, Proxy Controls, or feedback Controls.

You can specify the type of the Control by clicking the **Animation Type** drop-down menu for a selected Control in the Details panel. The following Control types can be chosen:

![control type](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/206eb505-05a3-423d-8f7f-6762ce961ccf/controltype1.png)

| Control Type | Description |
| --- | --- |
| **Animation Control** | The default Control type, which provides a normal visible animatable Control. |
| **Animation Channel** | A type of Control that is used to provide an animation channel or custom attribute. If **Group Channels** is enabled, this attribute will be accessible on the parent Control, where it can be animated together with other attributes. |
| **Proxy Control** | Proxy Controls are a type of Control which can be linked to other Controls in a **Driver / Driven** relationship. This is done by adding the Controls you want to drive in the **Driven Controls** array. Proxy Controls cannot be animated directly, however you can use them to drive other Controls in a consolidated manner using **Get Driven** and **Set Driven** nodes. |
| **Visual Cue** |  |

In addition to the Animation Type, you can also adjust the **Value Type**, which sets the output data of a Control. From the **Value Type** dropdown menu, you can set the following types:

| Name | Description |
| --- | --- |
| **Bool** | Makes the Control become a **bool-type**, where you can set **True / False** states in animation. Bool-type Controls are not visible in the **Viewport**. control type bool |
| **Float** | Makes the Control become a **float-type**, where you can animate the Control along a single position axis. If **Animation Type** is set to **Animation Control**, then you can specify which axis by selecting an axis from the **Primary Axis** property. The range you can move the Control when using this type is [limited by default](https://dev.epicgames.com/documentation/en-us/unreal-engine/controls-bones-and-nulls-in-control-rig-in-unreal-engine#transformlimits) between **0 - 100**. Floats can be useful if you are wanting to create a slider Control. control type float |
| **Integer** | Makes the Control become an **integer-type**, where you can animate the Control along a single position axis, incrementing by one. If **Animation Type** is set to **Animation Control**, then you can specify which axis by selecting an axis from the **Primary Axis** property. The range you can move the Control when using this type is [limited by default](https://dev.epicgames.com/documentation/en-us/unreal-engine/controls-bones-and-nulls-in-control-rig-in-unreal-engine#transformlimits) between **0 - 100**. You can also convert this Control Type to an Enum by referencing an **Enumeration** in the **Control Enum** property. control type integer enum |
| **Vector 2D** | Makes the Control become a **vector 2d-type**, where you can animate the Control along two position axes. If **Animation Type** is set to **Animation Control**, then the axis specified in **Primary Axis** will not be used, with the remaining axes being the ones providing the 2D plane. The range you can move the Control on both axes when using this type are [limited by default](https://dev.epicgames.com/documentation/en-us/unreal-engine/controls-bones-and-nulls-in-control-rig-in-unreal-engine#transformlimits) to between **0 - 100**. control type vector 2d |
| **Position** | Makes the Control become a **position-type**, where you can only animate the Control's location. control type position |
| **Scale** | Makes the Control become a **scale-type**, where you can only animate the Control's scale. control type scale |
| **Rotator** | Makes the Control become a **rotator-type**, where you can only animate the Control's rotation. control type rotator |
| **Euler Transform** | Makes the Control become a **transform-type**, where you can freely manipulate the Control on all translation, rotation, and scale axes. This is the default type. control type euler transform |

For spatial Controls, such as **Euler Transform**, **Rotator**, **Scale**, and **Position**, there are additional transform-related features available to you in the details panel when viewing the **Transform** properties:

![control transform buttons](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/53f26e36-4a2b-45a8-8eb7-1c33634fa5e5/spatialbuttons.png)
