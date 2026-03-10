# PCG Biome Core Overview

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-overview-guide-in-unreal-engine

> Application Version: 5.7

The PCG Biome Core and Sample Plugins provide examples of how to use the  [PCG Framework](building-virtual-worlds/procedural-generation/procedural-content-generation-overview) with features like Attribute Set Tables, Feedback loops, Recursive Sub-graphs, and [Runtime Hierarchical Generation](building-virtual-worlds/procedural-generation/pcg-development-guides/using-pcg-generation-modes). This section contains the definition of the PCG Biome Core and Sample plugins and the tool features list.

For more information on the Procedural Content Generation (PCG) Framework, see [Procedural Content Generation Framework](building-virtual-worlds/procedural-generation/procedural-content-generation-overview).

## What is the PCG Biome Core

![Image](https://dev.epicgames.com/community/api/documentation/image/49b26df3-77a5-495e-afca-7cebb4c009f0)

_PCG Biome Overview_

The PCG Biome Core is a data-driven biome creation tool made of native PCG Framework nodes, graphs, and making use of data assets. The tool has been built with a systemic approach providing a fixed pipeline, organized in logical sections with customizable steps.

It serves as an example to learn about the PCG Framework and leverages features such as Attribute Set Tables, Feedback loops, Recursive Sub-graphs, and [Runtime Hierarchical Generation](building-virtual-worlds/procedural-generation/pcg-development-guides/using-pcg-generation-modes).

It can be used by productions to get started in their world creation tool set and copied, modified or extended for specific needs and requirements without any or with minimal programming support.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The plugin itself is labeled as experimental and will evolve through future updates while relying on the PCG Framework and standard UE functionality that is Beta or Ready for Production. If used in production, it is recommended to copy the plugin to prevent future releases from breaking existing content.",
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

The PCG Biome Core plugin is standalone, containing only what is required for the tool to work such as base data assets, structures, blueprint classes, and PCG graphs. For more information on enabling plugins, see [Working with Plugins](understanding-the-basics/customizing-unreal-engine/working-with-plugins).

## What is the PCG Biome Sample

![PCG Biome Overview](https://dev.epicgames.com/community/api/documentation/image/089987d1-06e0-48f4-a429-e60ee9a599e9)

_PCG Biome Overview_

The PCG Biome Sample is a content example showcasing the PCG Biome Core tool. It includes the following features:

- A world with a pre-configured Biome Core
- Multiple biomes, including assets like a biome volume, a biome spline, a biome texture, and other injected data
- A specific crop field generator

The Biome Sample plugin can be enabled in any project using the Plugin settings. It depends on the Biome Core plugin and its own content. The Biome Sample is a guide and a reference on how to set up the Biome Core without having to load a separate project.

## Feature List

The PCG Biome Core contains the following features:

- Data-driven. Can be copied, modified, or extended for any productions needs.
- PCG native nodes only. No custom code, no custom Blueprint element.
- Fixed pipeline organized in logical sections with customizable steps using PCG Graphs and Data Assets.
- Unlimited user defined biomes.
- Ready-to-use classes, structures, data assets, and graphs.
- Biomes can be spatially defined from volumes, splines, and textures.
- Local generation per Biome actor with live updates.
- Local attribute set table to hold biome asset properties built from all data assets references in the biome actor.
- Optional local assets and biome definition, embedded and unique per Biome actor.
- Local Biome Cache to define biome bounds in 3D space per biome actor and per biome actor type (volume, spline or texture).
- Multiple Biome layering and priority sorting.
- Per Biome local blending, with control over blending range, noise, and density.
- Local Preview mode when creating a new Biome.
- Support for exclusions volumes and splines.
- Meshes, PCG Data Assets, PCG Assemblies, and actors spawning.
- Points bounds from meshes with support for custom bounds scaling.
- Layering of generated points with overlap managed by generator priority and accurate bounds.
- Support for multiple generator subtypes, to better control asset distribution in a biome (such as using landscape layer weights painting).
- Global root and children point filtering from customizable compute and texture projection filter graphs (such as height, density, and flow).
- Per-asset recursive hierarchical transform and spawning with support for multiple children per recursion level.
- Recursion max depth and ratio controls.
- Static mesh property overrides per asset entry (such as cast shadow or collisions).
- Transforms offsets and scale per asset entry.
- GPU Hierarchical Generation details spawning on landscape and meshes.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The major changes introduced in Biome Core for Unreal Engine 5.6 release are backward-compatible with previously existing Biome assets and actors, but they require a global refresh that can be triggered by toggling enable state on Biome actors in a given world. The Biome Setup actor class has been deprecated and must be replaced with Biome Texture volumes as shown in the Biome Sample Level.",
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
