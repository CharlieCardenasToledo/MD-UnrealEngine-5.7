# Static Mesh Actors

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/static-mesh-actors-in-unreal-engine

> Application Version: 5.7

The **Static Mesh Actor** is a simple type of Actor that displays a 3D mesh in the Level. Although the name implies that the Actor is static (or unable to move), the "static" refers to the type of mesh used rather than the Actor's ability to move. A mesh is **static** if its geometry does not change. Otherwise, the Actor itself can be moved or changed in other ways during play.

Static Mesh Actors are commonly used to create game worlds or other types of environments.

Unreal Engine includes the following default Static Mesh Actors:

* Cube
* Sphere
* Cylinder
* Cone
* Plane

In addition to these, you can import your own Static Mesh Actors that were created in other 3D applications.

To learn more about how to import content into Unreal Engine, refer to the [Importing Assets Directly](https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-assets-directly-into-unreal-engine) page.

## Placing a Static Mesh Actor

The quickest way to place a Static Mesh Actor is to drag it into the Level Viewport from the [Content Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-in-unreal-engine). You can then use its Transform properties to place it where it needs to be.

![Placing a Static Mesh Actor through drag-and-drop](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/50c292cf-9dca-412e-8bb4-e2243875dc79/placing-a-static-mesh-actor.gif)


To learn about other methods for placing Actors, refer to the [Placing Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine) page.

## Changing a Static Mesh Actor's Material

You can override the Materials applied to a Static Mesh individually for each Static Mesh Actor. This way, you can use a single Static Mesh Asset more than once in a Level while giving each a unique appearance.

The example below shows three Static Mesh Actors that use the same Static Mesh, which is a simple three-dimensional cube. Each Actor uses a different Material.

![Three Static Mesh Actors using different Materials](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca73186b-9c02-42a8-8207-c4d3e53b48ba/cubes.png)
