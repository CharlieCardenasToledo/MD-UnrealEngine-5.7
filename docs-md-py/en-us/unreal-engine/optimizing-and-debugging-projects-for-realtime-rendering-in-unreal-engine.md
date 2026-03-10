# Optimizing and Debugging Projects for Real-Time Rendering

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/optimizing-and-debugging-projects-for-realtime-rendering-in-unreal-engine

> Application Version: 5.7

Optimizing a project is not always a straightforward task and getting the maximum performance can be challenging because it can, at times, be where milliseconds matter most.

## Getting Started Optimizing Your Project

There are multiple places you can start looking to improve performance by optimizing your project. This can start with improving content creation workflows, performing profiling captures to know where time is being spent to render each frame, and using built-in editor tools.

Unreal Engine already does a lot of heavy-lifting to optimize your project for performance without needing to set up anything. But, that doesn't mean that these built-in systems can't be adjusted to fit your project's needs more closely.

The guide below will help you get started in identifying common performance issues and where to look for them. You'll also learn about some of the tools available in the editor that you can use to optimize and improve performance.

- [Related Document](en-us/unreal-engine/guidelines-for-optimizing-rendering-for-real-time-in-unreal-engine.md)

## Rendering Pipeline Optimization

The choice of some optimizations can directly affect the rendering pipeline that Unreal Engine uses. They can improve performance for the project in general or may be well-suited for a specific platform you want to develop for.

For example, Unreal Engine offers multiple rendering paths with a Deferred path (default) and a Forward renderer. For platforms like VR and Mobile, the Forward Renderer can improve performance but it does not support all rendering features of the engine.

In other cases, changes to the rendering pipeline can improve performance by rendering at a lower resolution and upscaling rather than rendering at native resolution, all while maintaining the same visual fidelity as the native resolution.

- [Related Document](en-us/unreal-engine/forward-shading-renderer-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/screen-percentage-with-temporal-upscale-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/dynamic-resolution-in-unreal-engine.md)

## Configuration Files and Scalability Optimizations

Through console commands and configuration files, you can set properties that scales your project for the type of experience or platform your application is developed for.

Console commands are used to call and set specific properties. These can be used in configuration files and scalability settings to improve quality and performance of the rendered image for development of the project or for the final shipped product. Configuration files can store these callable scalability settings to automatically set them for the project, and they can even be platform-specific.

For example, a configuration file can be set up which has multiple scalability options for a user to select from to make the application run better on lower end hardware, or the configuration file can store presets that are designed for specific platforms to use that best optimize the application to run on it.

- [Related Document](en-us/unreal-engine/configuration-files-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/unreal-engine-command-line-arguments-reference.md)

- [Related Document](en-us/unreal-engine/anti-aliasing-and-upscaling-in-unreal-engine.md)

- Related Document

- [Related Document](en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/hardware-ray-tracing-tips-and-tricks-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/scalability-and-the-developer-for-unreal-engine.md)

- [Related Document](en-us/unreal-engine/scalability-reference-for-unreal-engine.md)

- [Related Document](en-us/unreal-engine/stat-commands-in-unreal-engine.md)

## Asset Optimization

Optimization of assets in your project starts with the workflows you choose when developing the project. Sometimes this can mean creating those assets in ways that work best with Unreal Engine's tools. Other times, the built-in editor tools can do this work for you.

For example, manually creating level of detail (LOD) meshes for every object can be a time-consuming process. Unreal Engine provides its own automatic tool to generate LODs for your meshes. You can even configure the properties for how LODs are generated manually or let it perform the task automatically.

The built-in tools and systems below can help you to improve performance during development of your project.

- Related Document

- [Related Document](en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/visibility-and-occlusion-culling-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/texture-streaming-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/creating-and-using-lods-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/setting-up-per-platform-lods.md)

- [Related Document](en-us/unreal-engine/static-mesh-automatic-lod-generation-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/proxy-geometry-tool-in-unreal-engine.md)

## Debugging and Profiling Tools

Unreal Engine provides its own debugging and profiling tools and offers plugins for some external applications. These tools are useful for inspecting and identifying areas to improve performance.

For example, using the visualization modes of the Level Editor can visually identify costs of materials currently being rendered on screen. Profiling tools for the CPU and GPU can capture individual frames and breakdown millisecond cost of what is being rendered. With this type of information, you can see what is taking the longest to render in a single frame. By investigating high-cost line items, it may be possible to optimize those elements further.

The tools below will help you debug and profile elements of your project to look for performance optimization opportunities.

- [Related Document](en-us/unreal-engine/using-renderdoc-with-unreal-engine.md)

- [Related Document](en-us/unreal-engine/unreal-insights-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/gpudump-viewer-tool-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/render-resource-viewer-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/primitive-debugger-in-unreal-engine.md)

## Other Topics

- Related Document

- [Related Document](en-us/unreal-engine/dealing-with-a-gpu-crash-when-using-unreal-engine.md)

### Additional Epic-Created Resources

- [Unreal Performance Optimization Learning Path](https://dev.epicgames.com/community/learning/paths/Rkk/unreal-engine-unreal-performance-optimization-learning-path)
