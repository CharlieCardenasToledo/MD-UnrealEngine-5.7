# RigidBody

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-rigid-body-in-unreal-engine

> Application Version: 5.7

With the **RigidBody** [Animation Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) node, you can use a character's [physics asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine), to perform light-weight simulated physics motion of a character's auxiliary objects. This document will provide an overview of the RigidBody node and explain how you can get started using the RigidBody node, with an example workflow.

![rigidbody node animation blueprint node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0d43c043-2bd2-4345-9078-0b2e9e5be942/rigidbody.png)

#### Prerequisites

* Your project contains a [Skeletal Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine) character, with an [Animation Sequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine) or [Montage](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-montage-in-unreal-engine).

## Overview

The RigidBody node performs a similar function to the [Anim Dynamics](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-animdynamics-in-unreal-engine) node, but offers a more feature-rich physics simulation solution by enabling you to integrate a character's physics asset to have better control over the simulation. By using the RigidBody node, in conjunction with a physics asset, you can also simulate collisions with the rest of the character and any other objects in the level.

A typical use case for the RigidBody node is to simulate motion for secondary structures on the character's [Skeletal Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine), such as ponytails, chains, or other bones that are hanging or extended from the character's main body that require collision interaction with the rest of the [Skeletal Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine) and the level. The RigidBody node can be used to simulate dynamic and reactive motion to these structures in real time, in a more efficient process than more performance demanding techniques, such as true physics simulation.

|  |  |
| --- | --- |
| copy bone demo disabled | copy bone demo enabled |
| RigidBody Disabled | RigidBody Enabled |

## Set-Up

The example workflow will demonstrate how you can set-up and implement a RigidBody node in the character's [animation blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) using a physics asset to simulate dynamic and reactive motion for secondary structures on your character's [Skeletal Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine).

### Creating a Physics Asset

To begin using the RigidBody node, you must first set up a physics asset for your character. A full set up guide can be found in the [Creating a New Physics Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-a-new-physics-asset-in-unreal-engine) documentation.

If your character already has an associated physics asset, you can optionally choose to make a specialized physics asset to isolate the secondary structures you are simulating motion and collision with the RigidBody node. Using a specialized physics asset with the RigidBody node can be a more optimal method to better control the behaviors of the structures during the simulation.

![physics asset in the content browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f469d5e2-9a9e-417e-b140-da660492171a/physicsasset.png)

If your character does not have a physics asset, or you are choosing to create a specialized physics asset for use with the RigidBody node, you can create a new physics asset for your character by **right-clicking** the character's [Skeletal Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine) asset in the **Content Browser** and selecting **Create > Physics Asset > Create**.

![create a new physics asset by right clicking a skeletal mesh in the content browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fdb1826d-2136-4482-a4bf-03f35248bcbc/createnew.png)

From the **New Physics Asset** window, select **Create Asset** to create a new physics asset for your character.

For more information about creating a physics asset please see the [Creating a New Physics Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-a-new-physics-asset-in-unreal-engine) guide.

### Editing the Physics Asset

Open your character's physics asset in the [Physics Asset Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine) and ensure your character's physics Asset has [physics bodies](https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-bodies-in-unreal-engine) for the structure or structures you wish to use with the RigidBody node. In the example, physics bodies have been generated for the character's head hoses, as well as the objects the head hoses will interact with, such as the characters head, back, arms and weapon.

![physics asset physics bodies represent collision and components](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/33398e78-abf1-4ce1-9767-7cf2641494b2/physicsbodies.png)

With default settings, collision will be disabled on all [physics bodies](https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-bodies-in-unreal-engine). Enable collision on the bodies that comprise the parts of the [Skeletal Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine) you wish to simulate physics motion in the **Skeleton Tree** by **right-clicking** and selecting **Collision > Enable Collision All**.

![enable collision on all](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ca5319e-c1d3-493b-bff5-2d201351239f/enableall.png)

With all of the bodies that comprise the parts of the [Skeletal Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine) you wish to simulate physics and collision selected, set their **Physics Mode** to **Simulated** in the **Details** panel.

![select the physics type as simulated for the hoses](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/03f8c9c0-e13b-4cfd-9c06-2357b0593837/physicstype.png)

Select the remaining physics bodies, and set their **Physics Mode** to **Kinematic**.

![set remainging physics bodies to kinematic](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3eea2926-3fc0-40ac-afcc-36480423de22/kinematic.png)

You can test the basic functionality of the physics asset with the **Simulate** button in the [Physics Asset Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine)'s **Toolbar**.

![demo of siumulaiton](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3ab87e06-f3f5-41a7-b804-e8424841a35c/simulate.gif)

Jittering or shaking of the simulated objects will be common at this stage, you can fix this issue by enabling and tapering the **Mass (kg)** property on each of the physics bodies. Start by setting the closest body to the parent structure, as the heaviest physics body, and halving the mass for each subsequent body in the chain.

In the example, the first head hose physics body was set to a mass of **2kg**, and the second head hose physics body was set to a mass of **1kg**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7d9a42e2-db64-4aca-9c1c-545220bc5515/mass1.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a358acf3-71dc-42c4-878e-b55428cfcb51/mass2.png)

**Mass (kg) properties for Physics Bodies**

Finally, on all of the bodies you are simulating motion and collision with, set a value for the **Linear Damping** and **Angular Damping** properties. Higher values will reduce motion, controlling flailing and shaking of the simulated bodies. In the example, a value of **5.0** was set for each property, but fine tuning this value, for each unique implementation, is essential to achieving ideal results.

![damping settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d049fe37-be8c-47ad-a561-13c50dec499e/damping.png)
