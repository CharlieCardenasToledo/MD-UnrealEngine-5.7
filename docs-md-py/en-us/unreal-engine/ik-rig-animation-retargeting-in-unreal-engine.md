# IK Rig Retargeting

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine

> Application Version: 5.7

You can use **IK Rigs** to create animation retargeting between different **Skeletal Meshes**. This differs from Unreal Engine's traditional [Animation Retargeting](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-retargeting-in-unreal-engine) feature in that you can transfer animation between skeletons with varying numbers of bones, bone names, and orientations, while optionally maintaining precise hand or foot contact points using IK.

Retargeting animations provides a way to share animation data between multiple different skeletons, without needing to create and manage new animations outside of Unreal Engine.

This page provides an overview of the **IK Retargeter**.

For information about using Unreal Engine’s automatic retargeting tools, see the [Auto Retargeting](https://dev.epicgames.com/documentation/en-us/unreal-engine/auto-retargeting-in-unreal-engine) documentation.

#### Prerequisites

* Your project has two different Skeletal Meshes to evaluate the retargeting process.
* IK Rig Assets have already been created and retargeting chains defined within them. Refer to the [Retargeting Bipeds with IK Rig](https://dev.epicgames.com/documentation/en-us/unreal-engine/retargeting-bipeds-with-ik-rig-in-unreal-engine) page for how to do this.

## Creation and Overview

To create an IK Retargeter, click **Add (+)** in the Content Browser, then select **Animation > IK Rig > IK Retargeter**. A dialog window appears where you must select the IK Rig that you want to retarget animation from. Once selected, name and open the **IK Retargeter Asset**.

![create ik retargeter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8572d5f3-40df-4340-b621-632ffbc67a70/create1.png)

The IK Retargeter contains the following tools and options:

![ik retargeter editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3d786479-3bdf-449e-adbc-acb80be05d2f/create2.png)

1. [Retarget Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine#poseediting), where you can edit, save, and import the base retarget poses on either the source or target character.
2. **Viewport**, where you preview and debug the source and target characters being retargeted.
3. The [Details panel](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine#headername), which displays properties for your selected item or when other modes are active.
4. [Hierarchy](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine#hierarchydisplay), which displays a filterable list of bones and their assigned chains on either character.
5. **Retarget Output Log**, which displays debug information, warnings, and errors indicating the current status of your IK Retargeter.
6. [Chain Mapping](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine#retarget chains), which is used to map target chains to source chains. The **Asset Browser** is used to [preview and export](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine#previewanimationandexport) retargeted animations.

## Retarget Chains

Limbs and other appendages you want to transfer in the retarget process must be defined on both the source and target IK Rigs. This is a process similar to "characterizing" your rig as seen in other applications like Autodesk MotionBuilder or Maya. The main difference is you define it by joint chains, rather than by individual **Bones**. This provides flexibility in retargeting characters with vastly different bone structures.

For example, if your target character contains more arm joints than your source, the retargeting behavior will still work correctly because you are defining the entire arm chain, no matter the number of bones.

![retarget chains example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3ee80c9b-8b79-4fd3-8a96-cc0ed7c44ff9/chains1.png)

1. Source arm chain.
2. Target arm chain.

### Chain Creation

Retargeting chains are created in the [IK Rig Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-in-unreal-engine). To create a chain, open the IK Rig Asset for both characters, navigate to the IK Retargeting panel, then do the following:

1. Click **Add New Chain (+)**.

   ![add new chain](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7a7c4f2f-4978-4490-9799-6e457a6d5877/chains2.png)
2. In the **Add New Retarget Chain** dialog window, ensure **Chain Name** is set correctly, then click **OK**. In most cases, IK Rig automatically assigns this value from its list of [common chain names](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine#chainpropertiesandnames).

   ![chain name](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d7f87af4-ca79-4b3d-b41b-e7b94be1df45/chains3.png)
3. In the **Add Goal to New Chain** dialog window, select **No Goal**. Typically you do not need to add [IK Goals](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-in-unreal-engine#ikgoals) unless your retargeting requires additional IK adjustments, such as [Speed Planting](https://dev.epicgames.com/documentation/en-us/unreal-engine/fix-foot-sliding-with-ik-retargeter-in-unreal-engine), [Stride Warping](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine#globalsettings), or **Blend to Source**.

   ![add goal to new chain](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a2d48fd5-cc50-4b96-9ecc-2d49bca72e20/chains4.png)

You can also create chains by selecting every **bone** in the intended chain, right-clicking on them in the **Hierarchy** panel, and selecting **New Retarget Chain from Selected Bones**.

![new retarget chain from selected bones](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ae87304-ef4e-458c-b696-db1dbb7efd8a/chain3.png)

### Chain Properties and Names

Chains require the following parameters to be set:

| Name | Description |
| --- | --- |
| **Chain Name** | The name of this chain. This name can be arbitrary, but it should match with the intended retarget chain in the other IK Rig.  The matching chain name process is determined by a [Fuzzy](https://en.wikipedia.org/wiki/Approximate_string_matching) string match. Therefore, while your **Chain Names** in each IK Rig do not have to match perfectly, you should still try to match them. For example, a Chain Name of `ArmLeft` can match to `left_arm` as long as there isn't a name that might be more accurate. |
| **Start Bone** | The starting Bone of the retarget chain. If you are retargeting an arm, then typically you would select the upper arm bone here. |
| **End Bone** | The ending Bone of the retarget chain. If you are retargeting an arm, then typically you would select the hand bone here. |
| **IK Goal** | You can optionally select an [IK Goal](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-in-unreal-engine#ikgoals) here in order to [stabilize limbs or chains](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine#retargetingwithikgoals) which may not be retargeting with good accuracy. This means you will also need to create [Solvers](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-solvers-in-unreal-engine) for those goals, which will execute their solve after the retargeting process. |

The **Chain Name** property automatically fills in itself depending on the name of the selected bones used when creating the chain. The system looks for common bone names used, and then picks a name that best matches the selected bones. This mapping list is as follows:

| Chain Name Mapping | Bone Names to Search For |
| --- | --- |
| **Head** | `head` |
| **Neck** | `neck` |
| **Leg** | `leg` `hip` `thigh` `calf` `knee` `foot` `ankle` `toe` |
| **Arm** | `arm` `clavicle` `shoulder` `elbow` `wrist` `hand` |
| **Spine** | `spine` |
| **Jaw** | `jaw` |
| **Tail** | `tail` `tentacle` |
| **Thumb** | `thumb` |
| **Index** | `index` |
| **Middle** | `middle` |
| **Ring** | `ring` |
| **Pinky** | `pinky` |
| **Root** | `root` |

For symmetrical chains, such as arms and legs, the auto-naming feature is determined by comparing the average location of the bones in the chain, and then assigning a prefix of **Left** or **Right**. If the selected bones are mostly located on the negative X side, they are "Left", positive X is "Right", and if they are relatively centered on the X axis, then they are considered "Center" and no prefix is applied.

If multiple chains are created for bones with similar names, a numerical suffix will apply for each subsequent chain. For example, if you were retargeting a creature with multiple heads, then the resulting chains would read as **Head\_1**, **Head\_2**, and **Head\_3**. You can manually name your chains however you like, but this convention is helpful to establish standard naming conventions and retarget quickly using other IK Rigs.

### Chain Display and Mapping

The **Chain Mapping** panel displays the source and target chains, and their mapping relationships. Using the dropdown menus under **Source Chain**, you can specify different chain mappings or correct mismatches.

![change source chain](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/109edfd2-dfda-4856-a556-d84eedfbf6b5/retargeter4.png)
