# Skeletal Mesh Actors

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-actors-in-unreal-engine

> Application Version: 5.7

The **Skeletal Mesh Actor** displays an animated mesh whose geometry can be deformed, typically through the use of control points during animation sequences. These can either be created and exported from external 3D animation applications, or programmed directly in Unreal Engine.

To learn more about how to import content into Unreal Engine, refer to the [Importing Assets Directly](https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-assets-directly-into-unreal-engine) page.

Like the name suggests, Skeletal Meshes have a **skeleton** that consists of a number of **bones**. These are used in the animation process.

Skeletal Mesh Actors are commonly used to represent player characters, NPCs, other animated creatures, and complex machinery. The Unreal Engine Mannequin that appears in the [Third Person template](https://dev.epicgames.com/documentation/404) is an example of a Skeletal Mesh Actor.

## Placing a Skeletal Mesh Actor

The quickest way to place a Skeletal Mesh Actor is to drag it into the Level Viewport from the [Content Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-in-unreal-engine). You can then use its Transform properties to place it where it needs to be.

![Placing a Skeletal Mesh Actor from the Content Browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc760f3e-3c9f-4f4e-b472-2421f9b64575/placing-skeletal-mesh.gif)


To learn about other methods for placing Actors, refer to the [Placing Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine) page.

## Animating a Skeletal Mesh Actor

There are two basic ways to animate a Skeletal Mesh Actor in Unreal Engine:

* Using an [Animation Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) to play and blend multiple animations together.
* Using an Animation Asset to play a single [Animation Sequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine) one time or in a loop.

To learn more about animating Skeletal Meshes, refer to the [Skeletal Mesh Animation System](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-animation-system-in-unreal-engine) page.

## Changing a Skeletal Mesh Actor's Material

You can override the material of a Skeletal Mesh Actor individually to change its appearance. This is useful if you want to use the same Static Mesh in the Level multiple times, but want to have some variation between them.

The example below shows three Skeletal Mesh Actors that use the Unreal Mannequin Skeletal Mesh. Each Actor uses a different Material.

![Unreal Mannequins using different Materials](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/822ff27d-06c3-4303-904b-39cb33207d1f/mannequins-different-materials.png)
