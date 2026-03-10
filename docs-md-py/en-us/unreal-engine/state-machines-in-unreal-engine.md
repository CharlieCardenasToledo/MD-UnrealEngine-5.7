# State Machines

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/state-machines-in-unreal-engine

> Application Version: 5.7

**State Machines** are modular systems you can build in **Animation Blueprints** in order to define certain animations that can play, and when they are allowed to play. Primarily, this type of system is used to correlate animations to movement states on your characters, such as idling, walking, running, and jumping. With State Machines, you will be able to create **states**, define animations to play in those states, and create various types of **transitions** to control when to switch to other states. This makes it easier to create complex animation blending without having to use an overly complicated Anim Graph.

This document provides an overview of how to create and use State Machines, states, and transitions in Animation Blueprints.

#### Prerequisites

* State Machines are created within [Animation Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine), therefore you should have an understanding of how to use Animation Blueprints and their [interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-editor-in-unreal-engine).
* Your project contains a character with a movement component so that you can build states that react to input. The [Third Person Template](https://dev.epicgames.com/documentation/404) can be used if you do not have one.

## Creation and Setup

State Machines are created within the [Anim Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/graphing-in-animation-blueprints-in-unreal-engine#animgraph). To create one, right-click in the **Anim Graph** and select **State Machines > Add New State Machine.** Connect it to the **Output Pose**.

![add new state machine](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ddbd59bf-8e71-405b-8b5d-a7bbc3284178/create1.png)

State Machines are subgraphs within the Anim Graph, therefore you can see the State Machine graph within the **My Blueprint** panel. Double-click it to open the State Machine.

![new state machine](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9236cc22-6ff0-44af-9ab6-7b942c63a7a7/create2.png)


You can also double-click the State Machine node in the Anim Graph to open it.

### Entry Point

All State Machines begin with an **entry** point, which is typically used to define the **default state**. In most common locomotion setups, this would be the character idle state.

To create the default state, click and drag the **entry** output pin and release the mouse, which will expose the context menu. Select **Add State**. This will create the new state and connect it to the entry output, making this state active by default.

![state entry point](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6941aa29-6a13-492e-91c9-5fe1f4fea3aa/create3.png)

## States

States are organized sub-sections within a State Machine that can transition to and from each other regularly. States themselves contain their own Anim Graph layer, and can contain any kind of animation logic. For example, an idle state may just contain a character's idle animation, whereas a weapon state may contain additional logic for shooting and aiming. Whatever logic is used, the purpose of a state is to produce a final animation or pose unique to that state.

### Creating States

States can be created in the following ways:

* Right-click in the State Machine graph and select **Add State**.

  ![add state](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/806171ce-c486-4230-aea9-7e922030e4e1/state1.png)
* Click and drag off of the border of a state (or entry output), then release the mouse and select **Add State**. This will also connect it to the previous state with a [transition](https://dev.epicgames.com/documentation/en-us/unreal-engine/state-machines-in-unreal-engine#transitions).

  ![drag add state](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/85ec3324-7fcd-4767-8d6a-e075928e5301/state2.png)
* Drag an **Animation Asset** into the State Machine graph from the **Content Browser** or **Asset Browser**. This also adds the animation to the state and connects it to its **Output Pose**.

  ![drag and drop add state](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b0d40ed6-a6e0-4856-8c3e-c62e2bf52ad7/state3.png)

State Machines can have as many states as needed, and they also display as subgraphs under the State Machine.

![states in my blueprint panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cb6652e2-96d2-43ea-b06b-16e4fdedcb77/state4.png)
