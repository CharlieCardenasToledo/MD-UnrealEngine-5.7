# Animation In Lyra

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine

> Application Version: 5.7

**Lyra**'s character animations were created almost entirely in **Blueprints** using Unreal Engine 5's improvements to the [Animation Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) system. The system setup is inspired by both Paragon and Fortnite, which achieve similar results through the use of custom C++ functionality.

# Asset Overview

The **AnimBP\_Mannequin\_Base** Animation Blueprint contains the [AnimGraph](https://dev.epicgames.com/documentation/en-us/unreal-engine/graphing-in-animation-blueprints-in-unreal-engine) window, which you can use to observe the architecture of [Animation Nodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-nodes-in-unreal-engine) that contribute to the final output pose of the Character Mannequin.
You can navigate to this Animation Blueprint by clicking on the **Content Drawer** > **Characters** > **Heroes** > **Mannequin** > **Animations** > **AnimBP\_Mannequin\_Base**.

The Mannequin Base Animation Blueprint's AnimGraph and Blueprint Thread Safe Update Animation function.

The AnimBP\_Mannequin\_Base is set up to support common techniques that are used across the Lyra game's Sample Weapons and [Gameplay Abilities](https://dev.epicgames.com/documentation/en-us/unreal-engine/abilities-in-lyra-in-unreal-engine).

### Blueprint ThreadSafe Update Animation

When developing animations for your character classes, there are some practices to be aware of to ensure your animations are running at optimal performance. In Lyra, we use [Multi Threaded Animation](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-optimization-in-unreal-engine) to calculate animation values instead of the [Event Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-event-nodes-in-unreal-engine) .

The **Animation Fast Path** helps you keep processes that calculate values outside of the Game Thread. You can enable this from the editor by navigating to **Edit** > **Project Settings** > **Engine** > **General Settings** > **Anim Blueprints,** then enabling **Allow Multi Threaded Animation Update**.

You can view the function responsible for gathering the animation data and processing these calculations by opening the **Class Defaults** of the **AnimBP\_Mannequin\_Base**, then navigating to the **My Blueprint** > **Functions** category and clicking the **BlueprintThreadSafeUpdateAnimation** function.

When using Thread Safe functions you can not access data directly from game objects as you could in the Event Graph. For example, if you were attempting to copy the Gameplay float value for the Character's speed it would not be considered thread-safe, therefore we recommend the use of Property Access to accommodate these instances.

### Anim Node functions

In Lyra, the state-specific logic is created by using Anim Node Functions. This has the benefit of keeping the Animation logic organized. If you need to calculate a value while the character is in the Idle Animation, then you can put that logic into the Idle state. To see an example follow the steps below:

1. Navigate to the **AnimBP\_Mannequin\_Base** > **Anim Graph** and double-click the **LocomotionSM** State Machine to open a window that displays the Locomotion states.

   The Locomotion State Machine includes State Aliases to transition between different Animation states.
2. You can double-click the **Idle** state and select the **Output Animation Pose** node, then under **Functions** in the **Details** panel, you can see the Anim Node Functions that provide a setup for the initial values of our nodes.

   In our example image, we opened the Idle state machine to view the Anim Node functions used in its Output Animation Pose.

   | Function | Description |
   | --- | --- |
   | **On Initial Update** | Called before the node is updated for the first time. |
   | **On Become Relevant** | Called when the node becomes relevant. |
   | **On Update** | Called when the node is updated. |
3. Navigate to **My Blueprint > Functions > State Node Functions** and double-click the **UpdateIdleState** function to view the logic used to calculate the final output pose of the Idle State locomotion node.



   In previous Engine versions, Legacy state machine events are fired after the animation update.

### State Aliases

As your projects begin to grow in size, you may have multiple animation states that your characters need to transition to. This can result in a State Machine with multiple transitional lines that can make it difficult to view in the Graph. State Aliases are used to simplify the transition logic while providing control over each individual transition between states. In Lyra, you can view an example of a State Alias being used by navigating to the **AnimBP\_Mannequin\_Base** > **Anim Graph** > **LocomotionSM** graph, then select the **JumpSources** state node.

The Locomotion State Machine graph with the Jump Sources node highlighted to observe the State Aliases available.

In the Details panel, you can view the Locomotion States which can directly transition to the Jump state.

When a Lyra Character is Idle, and the Player uses the Jump action, then the Lyra Character will enter into a jumping state. Eventually, they will transition into a falling state and then will either enter back into a cycle or idle state.

### Upper/Lower Body Layering

[BlendNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-blend-nodes-in-unreal-engine) are used to blend animations together. Most of the locomotion animations used in Lyra are full body, meaning that the animation is playing on the entire skeleton (like the **jog\_fwd** animation), then they are combined with a variety of upper body actions that the player can use at any time (such as weapon fire or reload animations).

This is achieved through using the **Layered blend per bone** node, which you can view by opening the **AnimBP\_Mannequin\_Base** > **AnimGraph**, then navigating to the comment Upperbody/lowerbody split.

When you select the Layered blend per bone node, you can view the Details panel which includes Blend Masks that provide explicit control over the weight of individual bones involved with a blend.

## Linked Layer Animation Blueprint

The [Animation Blueprint Linking](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-animation-blueprint-linking-in-unreal-engine) system enables dynamic switching between different sub-sections on the Animation Graph. The main Animation Blueprint has multiple places where you can override the pose through Linked Layer Animation Blueprints.
In Lyra, this means that depending on which weapon the player is holding, you can have different locomotion behavior, animation assets, or pose corrections. You can keep their functionality separate and allow multiple users to work on the animation simultaneously, or reduce dependencies between assets while still sharing the same core functionality.

### Anim Layer Interface

**ALI\_ItemAnimLayers** is an Anim Layer Interface that specifies where you can override an animation in the Animation Blueprint. In Lyra, this is done for locomotion states in addition to layers for aiming and skeletal controls.

The FullBody\_Aiming animation layer, which is a part of the Item Anim Layers interface.

**ABP\_ItemAnimLayersBase** is the base Linked Layer Animation Blueprint that all of the weapons use. You can access this Blueprint from **Content** > **Characters** > **Heroes** > **Mannequin** > **Animations** > **LinkedLayers**.

### Accessing Data From the Main AnimBP

Inside of the **ABP\_ItemAnimLayersBase** Animation Blueprint there is a custom function **Get Main Anim BPThreadSafe**, that is used to get a reference to the main Animation Blueprint (**AnimBP\_Mannequin\_Base**).

The Get Main Anim BPThreadSafe function as it appears in the Item Anim Layers Base Animation Blueprint.

This provides the use of Property Access to access all of its data and avoids having to re-calculate any values the linked layer may use like **Acceleration** or **Velocity**.

### Using Anim Node Functions for animation selection

In Lyra, **Linked Anim Layers** use **Property Access** along with Anim Node Functions to run logic when an animation updates (On Update) or becomes relevant (On Become Relevant).

In the example below, we are choosing a directional start animation every time the animation becomes relevant.

### Linked Layer Child Animation Blueprint

In Lyra, every weapon has a Child Animation Blueprint that inherits from the **ABP\_ItemAnimLayersBase**. Animators can slot in animations and edit any variables per-weapon as seen in the image of the **ABP\_PistolAnimLayers** Animation Blueprint shown below.

## Distance Matching and Stride Warping

**Distance Matching** adjusts the playrate of an animation in instances where it is difficult to match the motion between Animation assets and Gameplay, for example locomotion animation assets like starts, stops, and landing animations.

Stride Warping is used to dynamically adjust the length of the character's stride in instances where the playrate adjustment will not, such as when the character enters into the Jog state.

|  |  |
| --- | --- |
|  | stride-warp-motion |

By combining both of these techniques, you can dynamically choose to favor one technique over the other. During start states, we begin with using Distance Matching to preserve the pose, then blend in by using Stride Warping as we approach the Jog state.

![update-start-anim](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a3db66ee-dc0d-4841-b87e-69021d5e2987/updatestartanim.png)
