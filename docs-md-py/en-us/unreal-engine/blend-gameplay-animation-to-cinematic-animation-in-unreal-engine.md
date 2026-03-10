# Blending Gameplay and Sequencer Animation

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/blend-gameplay-animation-to-cinematic-animation-in-unreal-engine

> Application Version: 5.7

When creating your cinematic sequences, you may want to blend gameplay animation to or from animation inside your Level Sequence. Typically this is done to create seamless transitions into and out of a cinematic, which includes blending both the player animation and the player camera.

This document provides instructions on workflows and considerations you can use to blend player and camera animations between Sequencer and gameplay.

#### Prerequisites

* You have a controllable player character in your project. For this document, the [Third Person Template](https://dev.epicgames.com/documentation/404) is used as an example.
* You have created your cinematic sequence and you are ready to blend it to gameplay.
* You are familiar with [how to reference the player](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-reference-the-player-in-unreal-engine-cinematics) in Sequencer.

## Animation Blueprint Setup

Normally when animating characters in Sequencer, the Animation Mode property automatically changes to **Use Custom Mode**. Custom Mode is a special Sequencer-specific [Animation Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine), different from the one used to animate the player in gameplay. In order to blend characters between Sequencer to Gameplay, you *cannot* use **Custom Mode**, and must instead use the same Animation Blueprint the character uses in gameplay.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0d11ab6b-274f-4021-b940-18e81391240b/animbp1.png)

You can ensure this by [referencing the player Character Blueprint in your Sequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-reference-the-player-in-unreal-engine-cinematics), which should have Animation Mode set to the gameplay Animation Blueprint. If not, then you can manually set this property by selecting the character, navigating to the **Details** panel, and doing the following:

* Set **Animation Mode** to **Use Animation Blueprint**.
* Set **Anim Class** to the **Animation Blueprint** used in gameplay. In the case of the Third Person Template, it is **ABP\_Manny\_C**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0a21a277-7b79-4703-bb5a-96eb6ed5875a/animbp2.png)

When an Animation Blueprint is explicitly set, Sequencer will not override this property to Use Custom Mode.

### Slot Setup

When animating characters in Sequencer using their Animation Blueprint, you must ensure that Animation Blueprint contains [Slots](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-slots-in-unreal-engine), which provide a way to inject animation into the [Anim Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/graphing-in-animation-blueprints-in-unreal-engine). Although mainly used to play animations from [Montages](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-montage-in-unreal-engine), you can also use Slots to play animation from Sequencer.

To create a new Slot, open the Animation Blueprint for the character you want to blend, and do the following:

1. Click **Window** and enable **Anim Slot Manager**, if it is not already enabled.
2. In the Anim Slot Manager, click **Add Slot**.
3. Type the name of your new Slot and press **Enter**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4e2a94e7-f73e-470d-ae34-8c20d9e69263/animbp3.png)


Slots are stored on the [Skeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletons-in-unreal-engine), therefore, when you are creating or changing Slots, you are also editing the Skeleton. Clicking **Save** in the Anim Slot Manager will save the Skeleton when you make any Slot changes.

Next, reference the Slot in your Anim Graph.

1. Right-click in the graph and add a **Slot 'DefaultSlot'** node.
2. Select the node and in the **Details** panel, set **Slot Name** to the name of the Slot you created earlier.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e372b68b-896d-49b9-ad36-fb3d6dc8a9c1/animbp4.png)

In addition to making the slot, also consider *where* in the Anim Graph it should be inserted. For most simple blends, it is best to place it as the final node before **Output Pose**, however there may be cases where it would be better to place it earlier in the Anim Graph logic chain to take advantage of procedural effects.

For this example, connect the Slot node between the Animation Blueprint logic and Output Pose.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/860e2756-887d-4489-b20c-6056c2fcc729/animbp5.png)

## Blending to Idle

One of the most common seamless blends to create is blending a cinematic to gameplay with the player character ending in their default idle locomotion pose. As stated in the [prerequisites](https://dev.epicgames.com/documentation/en-us/unreal-engine/blend-gameplay-animation-to-cinematic-animation-in-unreal-engine#prerequisites), this guide assumes your animation and Sequencer content already exists. This includes:

* [Character animation](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-add-cinematic-animation-to-a-character-in-unreal-engine) where the character ends at the component root coordinates and matches the gameplay idle pose.

  ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/12676f3f-97fe-4a39-8bf1-c0a8e7908b0f/blendidle1.gif)
* [Camera animation](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-animate-cinematic-cameras-in-unreal-engine) which ends in the approximate location of the gameplay camera.

  ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8b5b61b3-e5a7-4f59-b7da-93591f62a9c1/blendidle2.gif)

### Character Setup in Sequencer

To make the player character blend correctly, do the following operations in Sequencer:

1. Right click the [animation](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-animation-track-in-unreal-engine) section, navigate to the **Properties** menu, and set **Slot Name** to the name of the Slot you created earlier.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad9ca3f2-c43a-407a-a431-ef7b20a14d29/blendidle3.png)
2. Drag on the upper-right corner of the animation section to create a blend out region at the end of the animation. Although the ending pose of this animation might match the gameplay pose, this can still help to ensure the character does not "pop" when the Sequencer animation finishes.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ba32d9d-4f24-4064-b11c-ccbf8422cea2/blendidle4.gif)
3. Right click on the character's transform section, navigate to the **Properties** menu, and set **When Finished** to **Keep State**. This is required to ensure the character remains at the same position when Sequencer finishes.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eba0b61b-2464-484d-b81f-68d882bf82f7/blendidle5.png)

### Camera Setup in Sequencer

To make the cinematic camera blend correctly to the gameplay camera, do the following operations in Sequencer:

1. Right-click on the [Camera Cut Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-camera-cut-track-in-unreal-engine) and enable **Can Blend**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1d5b4b16-d9d7-4c79-ae40-1c59ec958129/blendidle6.png)
2. Similar to blending the animation section, drag on the upper-right corner of the camera cut section to create a blend out region at the end of the camera animation.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3c6916a8-aa19-483d-9169-c410ac1cc0e2/blendidle7.gif)
3. Select the **Cine Camera Actor** and disable **Constrain Aspect Ratio** in the **Details** panel.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a094357a-862b-4784-892b-e48aea0862ec/blendidle7a.png)

You may also need to select the **Level Sequence Actor** and disable **Override Aspect Ratio Axis Constraint** to prevent abrupt field of view changes, if your gameplay camera uses a different axis constraint.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4c9778c-2053-4630-a4d4-e3cdae554f74/blendidle7b.png)

### Blending Idle Results

When playing this sequence at runtime, you should see your character blend from Sequencer to gameplay. Again, this guide assumes you are familiar with [how to reference the player](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-reference-the-player-in-unreal-engine-cinematics) in Sequencer.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9b79a297-f46b-453c-aae2-a49dc76aec63/blendidle8.gif)
