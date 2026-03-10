# Fracturing Geometry Collections User Guide

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/fracturing-geometry-collections-user-guide

> Application Version: 5.7

You can find similar information in video format in the Epic Developer Community site by watching the [Fracture and Clustering](https://dev.epicgames.com/community/learning/tutorials/k84m/chaos-destruction-fracture-and-clustering) tutorials.

The **Fracture Mode** is an editor mode that contains a wide variety of tools for creating, fracturing, and manipulating **Geometry Collections**. Geometry Collections are the asset type used by Chaos Destruction for simulating real-time fracturing in Unreal Engine.

The available fracturing tools provide users with a lot of control over how the Geometry Collection is fractured. This includes the number of fractured pieces and how they relate to each other (fracture hierarchy).

Each fracture tool uses a different method, or algorithm, to generate different fracture patterns. Each method comes with a variety of options to further customize the generated pattern, including adding randomization.

In this guide you will learn to use the various fracturing tools available in the Fracture Mode.

Before learning about the Fracture Mode, you should know how to create Geometry Collections from Actors in the Level. If you are not familiar with the process, refer to the [Geometry Collections User Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-destruction-key-concepts-in-unreal-engine).

## Fracture the Geometry Collection

Before using the fracturing tools, create a Geometry Collection from a Static Mesh Actor in your Level and select it.

![Create a Geometry Collection from a Static Mesh Actor in your Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c47ad94-0dbf-4f27-8721-3bfc74675f5d/destruction-fracture-6.png)

You can now access the available fracture tools under the **Fracture** section of the **Fracture Mode** panels. Each tool can be applied to the Geometry Collection as a whole, or to selected fractured pieces (individual bones) after fracturing.

Click the image for full size.

When applying a fracture method to the Geometry Collection, a new fracture level is created. This is reflected in the Geometry Collection's **Fracture Hierarchy** window.

Click the image for full size.

A Geometry Collection's fracture hierarchy resembles a tree structure. It contains a root bone with one or more child bones which make up the fractured pieces. Each child bone can, in turn, contain its own child bones.

The levels in the fracture hierarchy represent the structure of the tree, with four levels representing a tree-like structure with three branching levels of child bones.

![A 4 level fracture hierarchy](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c0b7ea53-99cf-47f4-aaec-85cbf7a5c84d/destruction-fracture-6c.png)

You can use different fracturing tools each time you fracture the Geometry Collection, creating different fracture patterns per level in the Fracture Hierarchy.

You can select multiple bones (fractured pieces) in the Geometry Collection by holding **CTRL** and selecting them directly in the viewport. You can also use the provided [selection tools](https://dev.epicgames.com/documentation/en-us/unreal-engine/fracture-mode-selection-tools-user-guide) to quickly select a set of bones directly.

### Reset the Geometry Collection

After fracturing the Geometry Collection, you can reset it to its original state by clicking the **Reset** button under the **Generate** section. This sets the Geometry Collection to its original state when it was created without any applied fracturing. This can be helpful when trying different fracture methods until you find the configuration that provides the desired results.

![Click the Rest button to reset the Geometry Collection to its initial state](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c9982bbf-9500-46bc-bbd7-925f184462cb/destruction-fracture-11.png)
![You can reset a Geometry Collection to its original state by clicking the Reset button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/94fdaea5-2367-495d-9d53-5c05536537b1/destruction-fracture-reset.gif)

### View Settings

The **View Settings** help you visualize what the Geometry Collection looks like after applying any fracture operation.

![Common view options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/340a925f-377a-4f08-8155-da2be656b4b1/destruction-fracture-8.png)

| Option | Description |
| --- | --- |
| **Explode Amount** | Displays what the Geometry Collection will look like when it fractures during gameplay. A value of 1 will separate all bones and will show what a completely fractured Geometry Collection looks like. |
| **Hide UnSelected** | Hides the bones that are not currently selected in the Geometry Collection. This helps you focus on specific bones while applying a fracture method. |
| **Fracture Level** | Defines which fracture level to visualize. Selecting All will display the bones for all fracture levels. |

Click the image for full size.

![Changing the Explode values from 0 to 1](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bfc9e7d3-8e73-42b7-a5c1-60207c87d500/destruction-fracture-explode.gif)

### Common options included with most fracture methods

All fracture tools have these **Common Fracture** options:

![Common Fracture options for all fracture methods](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/69d6b3d4-bd08-470c-9386-74fdbdc5e3c9/destruction-fracture-10.png)

| Option | Description |
| --- | --- |
| **Random Seed** | This value is used to generate the random fracturing pattern over the Geometry Collection. A -1 means a random seed value will be used every time a new fracture operation is applied. Specifying a value generates a fracture pattern tied to that seed number, which when entered will always generate that same fracture pattern. |
| **Chance to Fracture** | Sets the chance that a bone is likely to be fractured during the fracture operation where 1 is equal to 100%, meaning all bones will be fractured. 0 is equal to 0% chance of any bone being fractured. |
| **Group Fracture** | Generates a fracture pattern across all selected meshes. |
| **Draw Sites** | Draws points in the center of the bones to be cut out by the fracture pattern. |
| **Draw Diagram** | Draws the fracture pattern diagram on top of the Geometry Collection. |
| **Grout** | Defines the amount of space to leave between cut piece. |

![A fractured Geometry Collection with grout](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d6a39035-5bda-4906-a02a-19774fb57245/destruction-fracture-12.png)

Most fracture methods share these **Noise** options:

* **Amplitude**: Defines the size of the perlin noise displacement in centimeters. A value of 0 indicates that no noise will be used when generating the fracture pattern.

  ![Amplitude: 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/790ad5be-b738-4a7a-a183-438189399f2a/destruction-fracture-13a.png)

  ![Amplitude: 30](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4633eb2e-cda5-451e-9161-54738d888fd5/destruction-fracture-13b.png)
* **Frequency**: Defines the period of the perlin noise. Smaller values produce a smoother noise pattern, and larger ones produce a rougher noise pattern.

  ![Amplitude: 5, Frequency: 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8b67bbe-bbb1-4984-9e43-9fbeb482bd2c/destruction-fracture-14a.png)

  ![Amplitude: 5, Frequency: 200](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/82c0b673-e248-4684-93e7-45277f81e132/destruction-fracture-14b.png)
* **Persistence**: Defines the persistence of the perlin noise layers. For each layer (octave) after the first, the **amplitude** of the perlin noise will be scaled by this factor.

  ![Amplitude: 5, Persistence: 0.5](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4889222c-e019-44be-9ecf-4bf87751e6d9/destruction-fracture-15a.png)

  ![Amplitude: 5, Persistence: 1](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/661504bf-851b-4970-86ae-22320f0ce04d/destruction-fracture-15b.png)
* **Lacunarity**: Defines the lacunarity of the perlin noise layers. For each layer (octave) after the first, the **frequency** of the perlin noise will be scaled by this factor.

  ![Amplitude: 5, Lacunarity: 2](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/46fea472-9872-4e2a-be92-95ad95a85492/destruction-fracture-16a.png)

  ![Amplitude: 5, Lacunarity: 4](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/91bd75fb-095a-4423-bc84-f4e64b3d2f87/destruction-fracture-16b.png)
* **Octave Number**: Defines the number of fractal layers (octaves) of perlin noise that will be applied to the fracture pattern. Each layer is additive, with Amplitude and Frequency scaled by Persistence and Lacunarity, respectively. Smaller values (1-2) will generate smooth patterns, while larger values will generate more craggy patterns.

  ![Amplitude: 5, Octave Number: 1](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1c628374-1445-444f-bf5f-4bb0796249b7/destruction-fracture-17a.png)

  ![Amplitude: 5, Octave Number: 8](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f32469be-a6a1-4fad-8152-7af7200499e2/destruction-fracture-17b.png)
* **Point Spacing**: Distance (in centimeters) between vertices on cut surfaces where noise is added. Larger spacing between vertices results in more efficient meshes with fewer triangles. However, this also results in lower overall resolution to see the shape of the added noise.

## Use the Fracture Tools

Each Fracture tool has its own settings that provide relevant options to achieve the desired results.

### Uniform Fracture

The **Uniform** tool uses a Voronoi algorithm to generate the fracture pattern. Enter a minimum and maximum number of Voronoi sites (or number of fractured pieces) and the algorithm will choose a random value within the range.

![You can enter a minimum and maximum number of Voronoi sites](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48effc3a-1ba3-41c7-859f-628793108b07/destruction-fracture-18.png)
