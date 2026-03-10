# Event Track

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-event-track-in-unreal-engine

> Application Version: 5.7

In Sequencer, you can define frames in your sequence where you want to execute [Blueprint Scripting](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine) functionality. This is accomplished using the **Event Track**.

This guide provides an overview of the Event Track, including how to create it, access the Director Blueprint, and the types of events you can create.

#### Prerequisites

* You have an understanding of [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine), and its [Interface](https://dev.epicgames.com/documentation/404).
* You have an understanding of [Blueprints Visual Scripting](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine).

## Creation

To create an Event Track, click **Add Track (+)** in Sequencer, navigate to **Event Track**, and select either the [Trigger](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-event-track-in-unreal-engine#triggerevents) or [Repeater](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-event-track-in-unreal-engine#repeaterevents) event type.

![create event track](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0258fa8a-56ed-43ad-9582-4f2c56407e33/createevent1.png)

Event Tracks can also be created under an [Object Binding Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-actor-tracks-in-unreal-engine), which will [bind the event to that object](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-event-track-in-unreal-engine#objectbinding).

![create event track actor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/36d73258-3f1e-4753-81fd-a93455a87b4c/createevent2.png)

Once an Event Track is created, you can create additional event [Sections](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine#sections) by clicking **Add Section (+)** on the Event Track and selecting an event type.

![add more event tracks](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/197fde22-e49a-4e88-b8ae-19e74859571b/createevent3.png)

When adding events, you can choose to add either **Trigger** or **Repeater** type events. Trigger Events cause an event to evaluate on the same frame as the keyframe, whereas Repeater Events will evaluate for each frame for the duration of the event section.

### Trigger Events

Trigger events are events that evaluate once per keyframe. When this track is created, you can then **[Keyframe](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine)** it to create event keyframes.

![trigger event](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/047574c9-34b0-404e-8b6b-104142405486/trigger1.png)

### Repeater Events

Repeater events are events that will fire or evaluate for each frame of the sequence continuously for the duration of the event section. Adjusting the [Frames Per Second](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#framespersecond) of the sequence will also adjust the evaluation rate of the repeater to match. When this track is created, it will contain a finite [Section](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine#sections) range, controlling its evaluation time.

![repeater event](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61552c43-1458-4d1a-b23b-06c0ffe1ae03/repeater.png)

You can [edit, move, and trim](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine#interactionanddisplay) this event section just like any other section in Sequencer.

## Director Blueprint

The Director Blueprint is the logic center for the Event Track from which you will perform [Blueprint Visual Scripting](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine) from your event endpoints. **Parameters** and **Object Bindings** can also be specified in the Blueprint in order to pass variable and object information throughout the script. Each **Level Sequence** has its own Director Blueprint, containing all the logic for the events in that sequence.

There are several ways you can open the Director Blueprint:

1. Double clicking an event keyframe or section. This method will also bind the event to a new [**endpoint**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-event-track-in-unreal-engine#eventendpoint) if it is currently unbound.

   ![double click event](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/39419881-7700-4366-bcf5-86ea88eaff61/directorbp1.gif)
2. Clicking the [Director Blueprint Toolbar button](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#directorblueprint).

   ![director blueprint toolbar button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5ed1af54-8eaf-4330-809a-5079b6e095b6/opendp2.png)
3. Clicking the [Actions Toolbar button](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#actions) and then selecting **Open Director Blueprint**.

   ![open director blueprint](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d2c66314-be22-45c9-8068-d3e7e06c2ce4/opendp.png)

### Event Endpoint

Regardless of whether a Trigger or Repeater event is created, you must bind it to an **Event Endpoint** in order to add logic to it. To do this, right-click the keyframe (if using trigger) or section (if using repeater) and select **Properties > Unbound > Create New Endpoint**. Doing this will bind the event keyframe or section to a new endpoint node and open the **Director Blueprint**.

![create new endpoint](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/abd8a5d9-e29d-45c1-a5be-a8a50bddb83b/bind1.png)
