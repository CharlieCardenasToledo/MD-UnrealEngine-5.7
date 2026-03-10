# Solvers

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-solvers-in-unreal-engine

> Application Version: 5.7

IK Rig supports a variety of IK Solvers to affect a wide range of Bone hierarchies. They are used to create the Inverse Kinematic solution to rotating and positioning Bones in a chain. Multiple Solvers can also be used at the same time to further customize the IK effect.

This page provides an overview of the different Solvers you can add within the IK Rig editor, and their properties.

#### Prerequisites

* You have created and opened an IK Rig Asset. See the [IK Rig Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-in-unreal-engine) page for how to do this.
* You are familiar with how to create [IK Goals](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-in-unreal-engine#ikgoals).

## Creating Solvers

The primary way to create Solvers is by clicking **Add New Solver** in the **Solver Stack** panel, then selecting a **Solver**.

![add new solver](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c33dc3ea-77c9-4994-beb5-812c15b0b897/create1.png)

If a Solver does not already exist in your IK Rig, then creating an **IK Goal** will also prompt you to create a Solver, which automatically binds to that goal. Click the **Solver Type** dropdown menu to select a Solver.

![add default solver](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92e701e3-679f-441e-a55c-20526c76db58/create2.png)

## Solver Usage

All IK Solvers require either a **root Bone**, **IK Goal**, or both to be specified. These two starting and ending Bones will complete the IK chain for that Solver.

![root bone goal bone](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/618d4aa8-c30f-48d7-92c4-aea932331efc/example.png)

1. The root Bone at the start of the hierarchy chain.
2. The goal, or effector Bone at the end of the hierarchy chain. This is driven by an [IK Goal](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-in-unreal-engine#ikgoal).

### Connecting to Bones and Goals

To set the root Bone to a Solver, select the **Bone** in the **Hierarchy** and the **Solver** from the **Solver Stack**, then right-click on the **Bone** and select **Set Root bone on Selected Solver**.

![set root bone on selected solver](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1dfd7e9-c925-429c-8d04-119a5f9400c8/connect2.gif)

If your Solver requires an IK Goal, connect it by selecting the **goal** from the **Hierarchy** and the **Solver** from the **Solver Stack**, then right-click on the **goal** and select **Connect Goal to Selected Solver**.

![connect goal to selected solver](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0672a19b-68de-428e-bc34-51262429432d/connect1.gif)


Once Bones and goals are connected to a Solver, selecting the Solver will highlight those objects within the Hierarchy, as well as in the Viewport.

![bone highlight](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e35fe38-c83a-4801-b68d-b51c776094b9/create3.png)

### Multiple Solvers

Multiple Solvers can also be added to the Solver Stack, which provides extra functionality for your IK Rigs. The order of multiple Solvers will matter, as they evaluate in sequence, denoted by the number next to their name.

![multiple solvers](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/abf0bda7-821a-4eb4-90a2-77c22c25aa69/multiple1.png)

For example, in most leg IK setups, you may want to ensure that the **Set Transform Solver** on the hips evaluates first, before the Limb IK leg chains. This is so the legs can properly compensate for the movement of the hips beforehand.

![solver order of execution](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/35270a5e-c9b8-467e-b2d9-04d820388db5/multiple2.png)

Solvers can be rearranged by dragging them up and down in the Solver Stack.

![rearrange solvers](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/86c91014-a072-42df-9694-6ecc44da98eb/multiple3.gif)

### Excluding Bones

Bones within an IK chain can be excluded from the hierarchy, causing them to be ignored by all Solvers. This can be useful to correct bad poses, or to simplify a complex chain.

To exclude Bones, select all the **Bones** to be excluded, then right-click on them and select **Exclude Selected Bone From Solve**. Excluded Bones are denoted with a different icon.

![exclude selected bone from solve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9c6855e1-40dc-426f-99ed-50d5eeaa7912/excluded1.png)


You can re-include excluded Bones by right-clicking them and selecting **Include Selected Bone In Solve**.

## Solver Types

The following is a list of the different Solvers you can use in IK Rig.

### Body Mover

The **Body Mover Solver** will translate and rotate the root Bone based on the location of other connected IK Goals, which are typically the feet. Using Body Mover allows IK Rig to generate large-scale, gross movement of the body resulting in a more natural final pose

#### Setup

Body Mover requires a root Bone and at least two IK Goals to be connected. However, it can support several goals if the character is quadrupedal or multi-legged.

#### Usage

Body Mover is mainly intended for ground alignment, and should be used as the first Solver paired with other Solvers, such as [Limb IK](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-solvers-in-unreal-engine#limbik) or [Full Body IK](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-solvers-in-unreal-engine#fullbodyik).

For example, on its own, Body Mover does not produce correct looking results as an IK Solver.

![body mover solver](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9ddea3dd-fc77-4ef7-a7e0-891381819261/bodymover1.gif)

However, once other IK Solvers are set up to evaluate after it, and with appropriate settings applied, then Body Mover will function more naturally.

![body mover solver](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bbc70f46-9d81-4deb-8375-91c16b2f431f/bodymover2.gif)

#### Settings

Selecting the Body Mover Solver will reveal additional settings in the Details panel.

![body mover settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b93bcf66-d0d0-490f-8a3f-df44a3df34f1/bodymover3.png)

These settings are used to control the degree of movement exerted on both position and rotation axes, including their channels. In certain cases it may be necessary to adjust these properties to provide a more natural looking pose.

For example, on humanoid characters, setting **Rotation Alpha** to **0** will resolve the character leaning unnaturally towards the offset goal.

![body mover fix rotation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea4e4fd8-d591-4172-b4c9-8fc6e6afba43/bodymover4.gif)

However, on quadrupedal or multi-legged creatures, it may be more natural to keep this root rotation and not change any settings.

![body mover spider](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/89800902-717b-4e1d-b5a1-8d6bb4630ad0/bodymover5.gif)

#### Goal Settings

Selecting a **Goal Setting** located underneath a goal assigned to the Body mover solver will reveal additional properties in the **Details** panel.

![body mover goal settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/77852fdf-ca5a-40f7-9baa-384c9790453a/bodymover6.png)

**Influence Multiplier** is used to increase or decrease the amount of influence this goal exerts on the Body Mover solver, and can be useful if you want a goal to have more influence compared to others.

### Limb IK

Limb IK provides a cheaper-performance single-chain IK Solver. Typically you will want to use this for individual limbs, such as arms and legs.

#### Setup

Limb IK requires a root Bone and a single IK Goal to function. It follows typical IK rules in that you specify the starting bone (root), and an ending bone (goal). This Solver requires at least three Bones in the chain, in order to work correctly.

In most cases, you should specify the **shoulder** or **arm** as the root, and the **hand** as the goal. For legs, you should specify the **upper leg** or **thigh** as the root, and the **foot** as the goal.

![limb ik](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b8160fe6-bd9d-46a6-b142-7befb9b86e4a/limbik1.png)

#### Settings

Selecting **Limb IK** from the Solver Stack panel will reveal additional properties in the **Details** panel. These properties are only valid if your Limb IK chain is made up of more than 3 Bones. So if you are using Limb IK for a normal humanoid **Thigh > Leg > Foot** solve, then these properties will not affect its behavior.

![limb ik settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2797d42a-5b46-4470-b58c-9d76b4165624/limbik2.png)

| Name | Description |
| --- | --- |
| **Root Bone** | The root Bone assigned to this Limb IK solver. |
| **Reach Precision** | This value controls the accuracy threshold of the effector reaching the goal's position. Lower numbers are more accurate and higher numbers are less accurate. |
| **Hinge Rotation Axis** | The normal plane for the solver chain. |
| **Max Iterations** | Increasing this value will cause the joint chain to better converge on the goal location, but increases the CPU cost of the Limb IK chain. |
| **Enable Limit** | Enables rotational limits on the joint chain between the root and effector. |
| **Min Rotation Angle** | If **Enable Limit** is enabled, this forces at least this input angle between the parent and child bone. |
| **Average Pull** | Enables an average pull distribution along the joint chain. |
| **Pull Distribution** | Manual control of the weight of the pull distribution along the chain if **Average Pull** is disabled. Lower numbers favor the effector, and higher numbers favor the root. |
| **Reach Step Alpha** | Moves the end effector towards the target and limits displacement. |
| **Enable Twist Correction** | Enables twist correction along the solver chain by comparing the orientations of bones along the chain. |
| **End Bone Forward Axis** | Which axis to favor if **Enable Twist Correction** is enabled. |

### Full Body IK

Full Body IK (FBIK) is a fully-featured multi-goal IK solver that supports Bone limits, stiffness, and preferred angles. This Solver is useful if you want to create a large-scale IK system for multiple goals, with each of them exerting natural influence upon the whole body.

#### Setup

A root Bone and at least one IK Goal must be connected for Full Body IK to function. However, unlike Limb IK, multiple goals may be added to allow the skeleton to reach for multiple locations simultaneously.

![full body ik multiple goals](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/49c51de1-2208-4fe3-a46a-1691e01d11b2/fbik1.gif)

#### Usage

FBIK differs from other solvers in that you can create settings for any of the Bones affected by the Solver. This is so you can further refine the movement of a specific Bone within the FBIK chain.

To create a Bone setting, select the **Full Body IK Solver**, then right-click a **Bone** you want to create settings for and select **Add Settings to Selected Bone**.

![full body ik bone settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e3aed254-ac71-4dc6-97fb-4fdb273bd4f4/fbik2.png)

Selecting the Bone setting in the Hierarchy will reveal the following Bone settings in the Details panel:

![full body ik bone settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b88c4b94-582e-421b-b05a-990264fa5674/fbik3.png)

| Bone Setting | Description |
| --- | --- |
| **Stiffness** | **Rotation** and **Position Stiffness** properties are used to control how much a bone in the IK chain can be affected by goals and effectors. Use these properties to change the degree to which the pelvis bone will be affected by the movement of the controls. A value of **0** results in completely free movement, whereas a value of **1** completely locks the bone from movement.  In this humanoid example, the pelvis bone is specified as the root Bone for the FBIK chain, however in its base state it is rotating too aggressively. Increasing the **Stiffness** properties resolves this. fbik stiffness |
| **Limits** | **Limits** can be used to limit the range of, or completely lock, the rotation of bone axes along the IK chain. Each axis can be set to the following:   * **Free**, which allows for the bone to move freely. * **Limited**, which only allows movement within a specified range. If this is chosen, then the **Min/Max** properties are used to define the range of movement. * **Locked**, which disables movement along that axis.   Using limits can help with correcting unnatural joint movement. For example, these limits can be used to correct the unnatural ankle rotation issue. A value of **-50** is set for **Min Z** and **40** for **Max Z**, and the **Z** axis is set to **Limited**. fbik limits |
| **Preferred Angles** | **Preferred Angles** can be used to prioritize joints rotating along a specific axis to reach the effector. In some cases they can be used to resolve rigid issues in joint rotation. Enabling **Use Preferred Angles** will cause the rotation to reference the **Preferred Angles**.  The Preferred Angle properties you specify depend on the type of character, and its joint structure. For this example, the mannequin's knee should be bending more along the **Z axis**, therefore the **Z** property is increased. preferred angles |

#### Settings

Selecting the Full Body IK Solver reveals the following properties in the Details panel:

![fbik settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/453615a9-8dce-4458-8812-be63c0011915/fbik7.png)
