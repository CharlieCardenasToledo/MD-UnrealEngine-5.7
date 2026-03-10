# Guidelines for Optimizing Rendering for Real-Time

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/guidelines-for-optimizing-rendering-for-real-time-in-unreal-engine

> Application Version: 5.7

This page provides guidelines and best practices for how to identify and optimize performance while getting the best possible fidelity from real-time rendering features.

In this page, you'll learn:

* What factors contribute to your performance budget
* Best practices for packaging projects
* Walk through of available toolls to guage performance bottlenecks

## Knowing Your Performance Budget

When developing your project, the target platform for your application has a finite amount of resources available, both for keeping objects in memory and processing them. When building your project, you must decide what to spend those resources on. Being familiar with the platform's capabilities in terms of speed, threads, and bandwdith for your CPU and GPU, as well as potential memory, graphics memory, and available disk space are all important factors to consider.

It is also important that you *benchmark* your project against any platform you intend to ship on to understand how it will run and where it will encounter performance bottlenecks. You can benchmark a platform or device by running a demanding application or technical demo on it, then observcing its performance stats. It's important to test and benchmark your own projects on a regular basis in this same manner.

### Console Commands for Displaying Performance Stats

You can check performance statistics using a series of console commands while running your project. These can be entered through the console window when the project has been launched or has been packaged as a Development build.

![The console window displayed in a mobile application with the onscreen keyboard.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/047f59a8-373a-41dc-809c-d8d81b56a2cd/image_0.jpg)

The console window displayed in a mobile application.

The console and the four-finger tap command are only available in Development builds. It is not available in Shipping or Testing builds.

Within the console, you can enter commands to display debug information to the screen. The following table includes a list of commands that provide performance information:

| Command | Description |
| --- | --- |
| `Stat GPU` | Displays the amount of time in milliseconds used by the GPU for different processes. |
| `Stat Unit` | Displays the amount of time in milliseconds used by the CPU for different processes. Also displays the game thread, rendering thread, and GPU times. |
| `Stat UnitGraph` | Displays a graph showing CPU and GPU utilization over time. This can help identify spikes. |
| `Stat TextureGroup` | Displays the amount of memory used by different pools of textures. |

For more console commands you can use to analyze your application's performance on-device, refer to [Stat Commands](https://dev.epicgames.com/documentation/en-us/unreal-engine/stat-commands-in-unreal-engine).

## Common Performance Factors

Having identified where to look for performance data, this section will familiarize you with some common factors that most often affect performance. By understanding which of these elements is impacting your project and how, you can start to identify and address them using engine's built-in diagnostic tools.

### Best Practices for High-Resolution Normal Maps

Baking high-resolution vertices into a normal map for a low-poly model can be a complex process, and many factors can reduce the quality of a normal map texture by the time it is inside the engine. There are many tool sets for baking normal maps, but we recommend **XNormal**. The process we use for Xnormal is roughly as follows:

1. Bake the normal map in Xnormal as an 8k TIFF with 4xAA.
2. Import the TIFF into photoshop, then downres it to a 1k texture.
3. Apply a Guassian Blur with a value of .35px.
4. Convert the image from 16-bit to 8-bit.
5. Export the image to a 24-bit TGA.
6. Import the final normal map into Unreal.

To ensure the surface normals used in the baking process are the same as what is present in the engine, you should export the optimized normals from inside Unreal. Import the baking model into Unreal, choose to create its own normals, then export the baking model from Unreal to be baked in Xnormal. This is an important step when creating high quality normal maps, as Xnormal needs to be aware of the surface normals of the mesh to apply the offsets from the high resolution model.

Finally, there are two options that will reduce artifacts when rendering **static meshes**:

* Use Full Precision UVs
* Use High Precision Tangent Basis

Both of these settings are available in the Static Mesh Editor in the **Details** panel under the **LODs** section.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/34784cae-e49f-4ffa-825e-b7a7fd32eba5/image_2.png)

### Draw Calls

Draw calls are lookups for assets, which happen every frame. The number of draw calls your application uses depends on the number of unique meshes in your scene, as well as the number of unique material IDs each mesh is using. Currently, a high number of draw calls are the biggest contributor to low graphical performance, and you should reduce them as much as possible.

As an example, a highly optimized car model might only have five or six separate meshes, and each one of those components might only have a single material.

A good target for draw calls in an optimized scene is roughly 700 on a Galaxy Tab S6, and less than 500 on lower-end hardware. In projects for HMI, which tend to use highly unique or complex materials, 100 draw calls would be a good target on a Galaxy Tab S6, while less than 50 would be preferable.

You can output your draw call count with the console command `Stat RHI`.

Keep in mind that draw call count will change based on whether you are in PIE or on device. |

#### Reducing Mesh Count

The easiest way to reduce draw calls is to reduce the number of unique meshes being rendered in the world. This can be done in a couple of ways: using built-in tools in the engine to combine meshes, and using visibility culling.

* Combining Unique Meshes
* Meshes can be combined manually using an external DCC application, like a modeling program.
* Alternatively, in-editor world building tools like [Hierarchical Level of Detail](https://dev.epicgames.com/documentation/en-us/unreal-engine/hierarchical-level-of-detail-in-unreal-engine) meshes can be generated in the level automatically by combining meshes and textures to reduce draw calls.
* Visibility Culling
* The engine uses multiple methods of [Visibility and Occlusion culling](https://dev.epicgames.com/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-in-unreal-engine) to reduce the number of meshes being rendered. Cull Distance Volumes are placed volumes that can remove additional meshes specified by their size and distance from the player camera.

#### Reducing Material ID Count

There are several possible options for reducing the number of unique materials on a mesh.

The simplest method is to use a program like **Substance Painter**, which integrates multiple materials into the same texture. This enables you to take advantage of a vast number of material types in a very simple Unreal material, which you can then use as the basis for **Material Instances** with simple texture inputs. This can also reduce material instruction counts, which further improves performance.

![image alt text](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ac6da2ed-a16e-4665-b10d-c041e2ae1167/image_3.png)

The second method uses **masking** for a more procedural approach. Materials can denote certain characteristics of a surface, like color, roughness, or metallic qualities. Instead of using a separate material for different parts of a mesh, you can use masks to separate parts of a mesh's UVs and apply different settings to each section. You can create a basic mask using a black and white texture, but it is more efficient to use **Vertex Color**.

![Final Render](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2230531f-a5c2-4c4a-a46c-3910313c739f/image_4.png)

![Vertex Color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f464a04f-c515-4e5f-a23a-bc199f836906/image_5.png)

In the example below, vertex colors are used to define different material types, and the material defines parameters which can influence the look of those pieces individually. Vertex color masking is more efficient and creates a sharper separation, as it does not rely on texture resolution.

A material using vertex colors to separate different material types.

### Materials

The complexity of a material can increase the pixel cost of a rendered frame. The more material instructions there are for each pixel, the more time the render needs to spend calculating its final value. Opaque materials are the least expensive but can differ greatly based on the shading model or the base shader code.

You can find a readout on the instruction count of a material in the **Stats** window inside the **Material Editor**.

The Stats window displaying instruction count.

The instruction count will also increase depending on the number of math functions there are in a material. The more nodes there are, the more expensive the material will be to render. Some specific operations also have a higher cost. Try to limit the instruction count when building more complex materials.

**Translucent** materials are some of the most expensive material types. Individual layers of translucency have an expensive per-pixel cost, and when multiple layers of transparency are stacked and rendered, there is a much greater cost. This is known as **overdraw**.

Head lights and tail lights for vehicles are examples of problem areas with transparency. In many cases, hand-painted texture maps are used to reduce material complexity. Complex shapes and depth can be illustrated well, even with a flat texture.

![image alt text](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/09a39dd8-453b-4d27-bae7-2a443e5ec5df/image_8.png)
