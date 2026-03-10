# Animation Optimization

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-optimization-in-unreal-engine

> Application Version: 5.7

When developing animation systems in **Unreal Engine** using [Animation Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) you can use several animation optimization techniques to increase your project's performance.

You can use the following document to learn more about a few best-practice techniques to optimize your animation system in Unreal Engine.

## Overview

Your project's Animation System performance, or how efficiently each frame is evaluated, is based on the amount of time your **Game Thread** and **Worker Threads** require to process your animation system each **Tick**.

Animations are added to an Animation Blueprint, where they will be evaluated and played back on the character at runtime. Additional processes, such as animation blends, IK evaluations, physics simulations, and more, will each subtract from your project's performance budget in order to be evaluated. Some processes are simple and don't require much performance budget to evaluate, other processes perform more advanced operations that result in better looking animations, but may require a lot of your performance budget. All animation system features have an associated performance cost.

Generally speaking, the most performance-expensive operation of an Animation Blueprint is the **Event Graph** logic. While **AnimGraph** logic can be optimized using systems like [Fast Path](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-optimization-in-unreal-engine#aniamtionfastpath), it is recommended that you reduce your Event Graph logic as much as possible to achieve the best performance. The Event Graph is evaluated each Tick, with each process occurring sequentially on the **Game Thread**.

The following diagram is a conceptual breakdown of a single frame of animation. Each frame of animation contains several Ticks, and with each Tick the Event Graph is evaluated. Event Graph evaluations are typically the largest operation performed each tick. Event Graph evaluations are sequential, meaning each Tick's evaluation takes longer to complete.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/90eddafc-41b8-4d21-9b8a-2697abd3136f/diagram1.png)

You can optimize this process by relocating Event Graph logic to **Thread Safe functions** that can be evaluated simultaneously on available **Worker Threads**.

The following diagram illustrates the drastic reduction in the time each Tick takes to complete. When relocating all Event Graph operations to Thread Safe functions, operations can be performed simultaneously, thus reducing the amount of time required to evaluate each Tick by a significant margin and improving your animation systems performance.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4c9dcd1f-cbd9-46dd-b2b0-ce111e3a7b3b/diagram2.png)

## Using Multi-Threaded Animation Updates

Animation Blueprint Event Graphs always run on the **Game Thread**. In order to optimize the logic within the Event Graph to take advantage of multi-threading, you can instead build logic using **Thread Safe functions**.

To ensure thread safety, all references to data derived from other blueprints and components within your project, such as variables, must be called by your Animation Blueprint, rather than pushed to it.

### Blueprint Thread Safe Update Animation

You can use the **Blueprint Thread Safe Update Animation** override function to evaluate logic in your Animation Blueprint in a Thread Safe manner. You can add the Blueprint Thread Safe Update Animation function to your Animation Blueprint in the My Blueprint panel by selecting it in the **Override** down-down menu adjacent to the **Function** section.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/11ea2b4f-ec01-4267-9bab-c4167cddfb13/bptso.png)

### Thread Safe Functions

Thread Safe functions are [Blueprint Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/functions-in-unreal-engine) you can use to perform logic to set variables and properties that can be used by your animation system, in addition to performing other operations typically performed in the Event Graph.

To create a Thread Safe function in your Animation Blueprint, create a new function in the **My Blueprint** panel using (**+**) **Add**.After creating a new function, open its **Details** panel and enable the **Thread Safe** property.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9a52d0cd-824b-43c1-a9f4-3ee5c18f7351/enablethreadsafe.png)

Thread Safe enabled functions can then be added to the Blueprint Thread Safe Update Animation override function to be evaluated simultaneously when worker threads become available each Tick.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/705941a7-5094-4dcf-b27a-49591c298995/addfunctions.gif)

### Property Access

Thread Safe functions are unable to directly access non-thread safe blueprints and components. In order to access non-thread safe blueprints and their properties safely, you can use the **Property Access** feature to read their data and call their functions. Property Access can be used as a standalone node within a thread safe function's graph, or within a pin's properties on AnimGraph nodes.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9118d540-f6d7-4d69-8444-235c4db8df31/panode.png)
![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ae1bf7e-e1ef-4c0c-b091-cf1c9dcfe757/aspin.png)

**Property Access Node | Property Access Pin**

To create a Property Access node, right-click in the graph of a Thread Safe function, and select the **Property Access** option in the context-menu.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df8d1f0d-33e2-4ab9-9d0a-78d260db4705/createpa.png)
