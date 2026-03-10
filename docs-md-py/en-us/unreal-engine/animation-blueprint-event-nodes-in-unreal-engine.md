# Animation Blueprint Event Nodes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-event-nodes-in-unreal-engine

> Application Version: 5.7

Within an Animation Blueprints **EventGraph**, event nodes are Animation Blueprint (AninBP) nodes that you can use to create starting or activation points for animation blueprint logic. This document will provide a reference for the AnimBP event node types that you can use when creating animation logic in Unreal Engine.

![event node in animbp eventgraph overview example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/503f9852-f32d-4915-ae8e-8b332e3e9b3d/overview.png)

In the EventGraph, event nodes are red, and are indicated by the **arrow icon** in the top right corner of the node.

![arrow icon](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/03ef5b97-10f9-4ba4-8971-9769a0b8533e/arrowicon.png)

You can add event nodes in the EventGraph by right-clicking in the graph and selecting a node from the **Add Event** section of the context menu.

![add event node in anim bp eventgraph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f563e74a-cd0b-4156-a729-edcf06fe41f7/addeventnode.png)


An AnimBP's EventGraph can only contain one of each type of event node. However multiple functions can be connected to a single event node simultaneously.

EventGraph event nodes do not contain input pins as they begin a string of animation logic. Event nodes have an Output Execute pin that will initialize the sequentially connected nodes when the event node is activated. Each event node type is activated by a set of parameters.

![output pin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3f046e3f-cc16-455e-ac50-b2401cf06620/outputpin.png)

You can begin a string of logic in the EventGraph by selecting one of the following Animation Event Node Types.

## Animation Event Node Types

You can use the following Event Nodes in your AnimBP's EventGraph to begin animation logic with specific parameters.

| Node Type | Image | Description |
| --- | --- | --- |
| **Blueprint Begin Play** | event blueprint begin play event node | The **Event Blueprint Begin Play** event node will activate any connected logic when the owning component is activated by the [Play](https://dev.epicgames.com/documentation/en-us/unreal-engine/playing-and-simulating-in-unreal-engine) function. With this node you can connect logic that will be run when the owning object is first activated, even before animation functions are initialized. When hovering over the node, you can reference the node's owning component, or Target. |
| **Blueprint Initialize Animation** | event blueprint initialize animation event node | The **Blueprint Initialize Animation** event node will activate seqeunctail nodes when the current Animation Blueprint is first built during runtime to perform initialization operations. With this node, you can build logic that will activate once at the beginning of the Animation Blueprint. |
| **Blueprint Linked Animation Layers Initialized** | event blueprint linked animation layers initialized event node | The **Blueprint Linked Animation Layers Initialized** event node will activate connected nodes when the all linked animation layers are initialized. You can use this node to run logic once, that will be activated as soon as all linked animation layers are initialized for the first time. |
| **Blueprint Post Evaluate Animation** | event blueprint post evaluate animation event node | The **Blueprint Post Evaluate Animation** event node will activate sequential nodes after the AnimBP has been evaluated. With this node, you can activate logic that will run after the AnimBP has been evaluated. |
| **Blueprint Update Animation** | event blueprint update animation event node loop update every frame | The **Blueprint Update Animation** event node is executed every frame allowing the Animation Blueprint to perform calculations and updates to any values it needs. This event node is the entry point into the **update loop** of the EventGraph. The amount of time elapsed since the last update is available from the **DeltaTimeX** output pin so time-dependent interpolations or incremental updates can be performed. |

## Advanced Animation Event Node Types

You can use the following Event Nodes in your AnimBP's EventGraph to begin animation logic using project specific parameters, player input, and custom parameters.

| Node Type | Image | Description |
| --- | --- | --- |
| **Input** | input keypress event node | **Input** event nodes will activate connected logic when the specified [player input](https://dev.epicgames.com/documentation/en-us/unreal-engine/input-in-unreal-engine) is received or released, depending on the output pin the logic is connected to. You can use this node to create animation logic that is dependent on user inputs, with specific input functions, such as keys, mouse movements, or touch controls. |
| **Input Action** | input action event node | With **Input Action** event nodes, sequential logic will be activated when the player initiates a defined [input action](https://dev.epicgames.com/documentation/en-us/unreal-engine/input-in-unreal-engine) during run time. You can use this node to create animation logic that is dependent on user interactions with specified mechanics and systems in your project. These systems are definable in the project settings. |
| **Anim Notify** | anim notify event node | You can use specific **Anim Notify** event nodes to activate animation logic when the connected [Anim Notify](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-notifies-in-unreal-engine) is activated in an animation. These nodes are dependent on the **Anim Noties** present in your project and will activate any connected logic when the notify is triggered in your animation sequence, composite or montage. You can use these event nodes to build animation logic that is connected to animation playback. |
| **Custom Event** | custom event node in animbp eventgraph | With the **Custom Event** node you can build and define the custom parameters in which you want to activate animation logic in your project. See the  documentation for more info on blueprints and blueprint nodes. |
