# Constraints

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-constraint-tools-in-unreal-engine

> Application Version: 5.7

When animating, there may be cases where you need to attach elements together without causing a change in the Outliner or Control hierarchy. This kind of attachment is known as **constraining**. Constraints in Unreal Engine are broken up into different methods: **Position**, **Rotation**, **Scale**, **Parent**, and **LookAt**. With these methods, you can set options to control how these constraints operate, such as controlling the attachment offset and baking the constraint back to normal keyframes.

This document provides an overview of constraining in Sequencer, and the different workflows for each constraint method.

#### Prerequisites

* You have created a **Control Rig Asset**. Refer to the [Control Rig Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-create-control-rigs-in-unreal-engine) page for information on how to do this.
* Constraints when animating are accessed through the [Animation Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine) panel, therefore you need to enable **Animation Mode**.
* Constraining is mainly dependent on using Control Rig within **Sequencer**, therefore you need a [basic knowledge](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine) of Sequencer.

## Create a Constraint

Constraint information, as well as the workflow for adding constraints, is located in the Animation panel when [Animation Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine) is enabled.

![constraint section in animation panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2757924a-9bdc-4cfe-9ea6-208371fe1e52/create1.png)

Constraints are established by creating a **Parent - Child** relationship between two or more objects. To create a new constraint, first select your Controls you want to constrain (child), then click **Add Constraint (+)** and select a constraint type. Your cursor changes to an eyedropper tool you can use to select the object to constrain to (parent) in the Viewport.

![create constraint](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/31ab3b07-c793-4df7-b951-a8cbadf5c328/create2.gif)


Constraining is not limited to Control Rig elements, you can constrain any object or Actor. Additionally, Actors can be constrained without needing Sequencer to be open.

After creating your constraint, you can view its keyframe information in Sequencer for the constrained Control. Most constraints will also create compensating keyframes, which maintains the current visual position of the child when the constraint activates. These compensating keyframes are linked to the constraint keyframe, and follow it if you change the timing.

![constraint keyframe](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/82185aee-9837-4377-aa27-f848ef4606ec/create3.gif)

## Constraint Usage

Your constraints can also be viewed in the Animation Panel's **Constraints** section, when selecting the constrained Control. Here you can create new constraint keyframes, edit the properties of the constraint, and bake the constraint back to normal keyframes.

![constraint select](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f71dd667-35d7-4eed-b167-c69056550013/manage1.png)

If you have more than one constraint applied to an object, they also appear here too. When you play or scrub the sequence, each constraint indicates its status by highlighting when it becomes active or inactive.

![constraint switching](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf02d51b-3e73-4a51-aac9-2fc930c34c46/manage2.gif)

The buttons for a constraint entry provide the following functionality:

| Button | Description |
| --- | --- |
|  | Creates an active keyframe for the constraint at your current time in Sequencer. If the constraint is already active, then a deactivate keyframe is created instead. Compensating keyframes are also created to maintain the same world position on the constrained object |
|  | If you have multiple constraints on the same object, these buttons move the constraint up or down on the list. Constraints in Unreal Engine are hierarchical and override other constraints higher on the list (only if the constraints animate the same channels). New constraints always take priority over older ones and are placed lower on the list.   Because constraints can be overridden, it is not always necessary to deactivate other constraints. For example, since [Parent Constraints](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-constraint-tools-in-unreal-engine#parentconstraint) animate all transform channels of a control, simply activating one is enough to essentially deactivate all others, so long as the one activated is higher priority. In this example, although both constraints are active, only the **root** constraint is providing the constraint effect due to it being lower in the list and higher priority |
|  | Removes this constraint. |

Right-clicking on a constraint entry reveals a context menu where you can edit properties specific to that constraint type, [bake](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-constraint-tools-in-unreal-engine#bakeconstraint) the constraint, and set [compensating keyframes](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-constraint-tools-in-unreal-engine#compensatekeyframes).

![constraint properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4b8a5de6-2a66-464d-ab7b-d9185cd81d1e/manage3.png)
