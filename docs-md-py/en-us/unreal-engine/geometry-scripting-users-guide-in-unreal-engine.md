# Geometry Scripting User Guide

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/geometry-scripting-users-guide-in-unreal-engine

> Application Version: 5.7

## What is Geometry Scripting?

**Geometry Scripting** is an Unreal Engine plugin containing a set of function libraries that can generate and edit mesh geometry through Blueprints (BP) and Python. To view all available functions, see the [Geometry Scripting Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/geometry-scripting-reference-in-unreal-engine).

Geometry Scripting `UFunctions` and Blueprint nodes operate on `UDynamicMesh` objects, which are objects created using the `FDynamicMesh3` C++ triangle mesh data structure. This is the same data structure used by the **Geometry Processing** plugin and **Modeling** editor mode.

You can use Geometry Scripting in **Editor Utility Widgets** and **Asset Actions** to create custom mesh analysis, processing, and editing tools. You can also use it in **Actor Blueprints** to create procedural objects and implement complex geometric queries.

Geometry Scripting has a variety of potential uses:

- Testing and quality analysis of third-party mesh importers.
- Analyzing mesh UVs to identify assets with wasted texture space.
- Scripted merging of mesh assets for production workflows.
- Procedural mesh actors such as the level design tools used in the [Lyra Sample Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-geometry-tools-in-unreal-engine).

## Enabling Plugin

Using Geometry Scripting requires having the associated plugin enabled.

To enable the plugin or verify that it is already enabled:

1. In the **[Menu Bar](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-in-unreal-engine)**, select **Edit** > **Plugins**.
2. In the search bar, type "geometry script". ![Enable Geometry Scripting Plugin](https://dev.epicgames.com/community/api/documentation/image/5677daa3-3076-4774-bc3b-6547c71cb3bc)
3. Enable **Geometry Script** plugin, and select **Yes** in the dialog popup.
4. Restart the engine.

## Dynamic Mesh Objects

Geometry Scripting operates on several new object types:

- `UDynamicMesh`
- `UDynamicMeshComponent`
- `ADynamicMeshActor`

Similar to the static mesh, static mesh component, and static mesh actor architecture, these classes are not specifically part of the Geometry Scripting plugin. They are located in the **Geometry Framework** engine module and can be used separately from Geometry Scripting.

### Dynamic Mesh

The core component that enables Geometry Scripting is the `UDynamicMesh` object. This `UObject` is a container for a mesh data structure not tied to a specific component. This diverges from previous Unreal Engine approaches like `UProceduralMeshComponent` in that mesh geometry can be created and manipulated without an explicit scene representation.

For example, a `UDynamicMesh` can be initialized based on a `UStaticMesh`, edited, and then stored back in the asset. Combined with Editor Utility Widgets to provide the user interface, tech artists can create custom purpose-built mesh editing tools in Blueprint or script mesh asset query and editing operations via Python.

You can also convert various actor geometry types to and from `UDynamicMesh`, such as gameplay volumes.

### Dynamic Mesh Component

In addition to `UDynamicMesh`, `UDynamicMeshComponent` has been promoted into a "real" (non-transient, serializable) component. This component is similar to a `UProceduralMeshComponent`; however, it is backed by a `UDynamicMesh`, which you can manipulate through Geometry Scripting.

`UDynamicMeshComponent` has been developed over the past several years as part of the mesh modeling toolset, providing real-time previews of mesh editing. Similar to `UProceduralMeshComponent`, it supports updates to the mesh geometry updating — vertex attributes, and creating and modifying the entire mesh topology. You can perform these updates in-editor and at runtime.

Raytracing is supported; however, Nanite and Lumen are not.

### Dynamic Mesh Actor

`ADynamicMeshActor` is similar to `AStaticMeshActor` in that it is essentially a container for a `UDynamicMeshComponent`. However, dynamic mesh actors provide specific support for Actor Blueprints that want to implement procedural mesh generation based on a `UDynamicMesh`.

With dynamic mesh actors, Geometry Scripting and Modeling Mode tools can create and edit either type of mesh actor in addition to volumes.

### Generated Dynamic Mesh Actor

`AGeneratedDynamicMeshActor` is a subclass of `ADynamicMeshActor` that provides additional support for implementing Blueprint-based procedural mesh actors. Specifically, this class offers the function **On Rebuild Generated Mesh** that can be implemented in BP subclasses to generate a mesh instead of doing so in the **Construction Script**. The function provides better in-editor interactive performance and leaves the door open to more carefully managed large-scale procedural geometry generation in the future.

![On Rebuild Generated Mesh Event](https://dev.epicgames.com/community/api/documentation/image/b897fdaa-2974-43be-a6a8-7f71cee38241)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<em>Event On Rebuild Generated Mesh</em> only exists in Actor Blueprints derived from the GeneratedDynamicMeshActor class. Also, the <strong>Generated Dynamic Mesh Actor</strong> function is currently editor-only.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

### Key Differences between UStaticMesh and UDynamicMesh

Unlike `UStaticMesh`, `UDynamicMesh` is not an asset. A `UDynamicMeshComponent` owns its `UDynamicMesh`; instead of being shared between multiple components like a `UStaticMesh`.
This difference means, for example, instanced rendering is not available.

A dynamic mesh is stored in a level only instead of a separate asset file. Duplicating a `UDynamicMeshComponent` creates a copy of the mesh (creating a new mesh instead of an instance). Transferring between levels or projects must be done through copy and paste.

In many ways, `UDynamicMeshComponent` behaves more like mesh objects in a Digital Content Creation (DCC) tool, such as Autodesk 3ds Max, Autodesk Maya, or Blender. This handling does introduce potential problems with huge meshes dramatically increasing the size of the level file. However, with [One File Per Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/one-file-per-actor-in-unreal-engine), the mesh data is stored with the OFPA actor file rather than the level (so, still potentially huge, but in a separate file).

## Function Pattern

Most Geometry Scripting functions follow a standard pattern similar to the **Apply Mesh Plane Cut** node shown below.

![Geometry Script Node Pattern](https://dev.epicgames.com/community/api/documentation/image/bbeb754c-99f5-4c9c-b628-5d7bd1c2f86f)

The first argument, **Target Mesh**, is the `UDynamicMesh` edited by the operation. Generally, Geometry Scripting operations modify the input mesh rather than creating a new mesh to avoid making several temporary mesh objects. The input `UDynamicMesh` is always returned as an output, also called **Target Mesh** (`same name == same object`). This setup makes it easy to chain multiple operations in sequence.

Geometry Scripting nodes have many parameters and settings. We exposed the most frequently used options as arguments, but you can find additional options in an operation-specific **Options** structure. The most common way to create the proper Options structure is to drag off the empty **Options** pin. In addition, you can right-click the **Options** pin and use the **Split Struct Pin** context menu item to directly expand the Options structure in the node, as shown below.

![Blueprint Node Options](https://dev.epicgames.com/community/api/documentation/image/a4e22814-0601-4233-ac38-8fe93d7e0c5e)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Most nodes also have a <strong>Debug</strong> pin to provide geometric debugging support for mesh generators. This is not actively being used, but is a placeholder for future functionality.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

## Using UDynamicMesh Pools

It is common to create temporary meshes inside a mesh generator, such as using a primitive mesh to subtract from the main mesh. To do this, a temporary `UDynamicMesh` is needed. While you can create one using the **Construct Object From Class** function, you must garbage collect the mesh after usage. However, if you expect to run the generator frequently, re-using the mesh across runs is more efficient.

Dynamic mesh actor has built-in support for this using a `UDynamicMeshPool`. You can use this setup by calling **Request and Release Mesh** to get a temporary mesh and using it through the **With Mesh** execution pin. The temporary mesh is released automatically before the execution continues through the **After Release** pin. Each temporary mesh can be explicitly released using **Release Compute Mesh** or **Release All Compute Meshes**, which returns any temporary meshes currently allocated from the pool.

In an Editor Utility Widget, there is no default dynamic mesh pool instance to allocate meshes from. However, you can use **Create Dynamic Mesh Pool** to create one (for example, as a variable in the Editor Utility Widget or Utility Blueprint).

For examples of using dynamic mesh pools, see the [Geometry Scripting Through Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/geometry-scripting-through-blueprints-in-unreal-engine) and [Create Action Utilities With Geometry Scripting](https://dev.epicgames.com/documentation/en-us/unreal-engine/create-action-utilities-with-geometry-scripting--in-unreal-engine) tutorials.

## Creating a Procedural Mesh

As noted, one use case for Geometry Scripting is to create procedural meshes using Actor Blueprints. The example below uses a BP subclass of **Generated Dynamic Mesh Actor**. The **Event On Rebuild Generated Mesh** populates the `UDynamicMesh` of a `UDynamicMeshComponent`. The `UDynamicMesh` is passed to a Geometry Scripting function **Append Box**, which creates a mesh based on the input variables.

![Procedural Mesh Box Example](https://dev.epicgames.com/community/api/documentation/image/9bcb2452-a83b-4594-ac41-f8c8b70a2a20)

The script creates a parametric box primitive mesh with parameters arists can adjust in-editor with just a few BP nodes. By adding additional nodes, you can build increasingly complex mesh generators directly in Blueprints. To expand upon this script and continue learning about Geometry Scripting, see [Geometry Scripting Through Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/geometry-scripting-through-blueprints-in-unreal-engine).

![Procedural Mesh with Geometry Scripting](https://dev.epicgames.com/community/api/documentation/image/42e97a5b-3ddb-4b7a-9248-d5784001f433)

## Additional Notes

To check if a specific function exists, see the [Geometry Scripting Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/geometry-scripting-reference-in-unreal-engine) documentation.

Some functions (such as **Apply PolyGroup Catmull Clark SubD**) are editor-only. This setting means you can only use these functions in Editor Utility Actors/Actions/Widgets or Generated Dynamic Mesh Actor BP subclasses.

The majority of Geometry Scripting functions only work with `UDynmicMesh` objects. There are functions to convert the internal mesh representations from a static mesh, skeletal mesh, or volume actor into a `UDynamicMesh`, and functions to convert back. No functions exist for other geometry types, such as landscape, geometry caches or collections, grooms, and cloth.

Currently, `UDynamicMeshComponent` does not support the following features:

- Nanite
- Mesh Distance Field
- LODs
- Instanced Rendering

Actor Blueprints and Editor Utility Blueprints are always executed on the Game Thread, so Geometry Scripting functions that are called also run on the Game Thread. Some Geometry Scripting functions internally perform portions of their work on task threads, for example, C++ calls to ParallelFor, Async, or `UE::Tasks::Launch()`. However, this only occurs in the context of a single function, and the function will not return until all that parallel work is completed.
