# Animation Track

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-animation-track-in-unreal-engine

> Application Version: 5.7

The Animation track applies animation to your Skeletal Mesh Actors using Animation Sequence assets in Sequencer. This guide provides an overview of the usage of this track and its properties.

#### Prerequisites

* You have an understanding of [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine) and its [Interface](https://dev.epicgames.com/documentation/404).
* Your project has a [Skeletal Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine) actor and can play [Animation Sequences](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine) in it.

## Creation

By default, the Animation track is [automatically created](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-editor-and-project-settings-in-unreal-engine#projectsettings) under your Actor's track when a Skeletal Mesh Actor class is added to Sequencer. If you have added a different Actor class that supports animation, or have deleted the track, then you can add the track manually by clicking **Add Track (+) > Animation** on the Actor's track, and selecting an **Animation Sequence**.

![add animation track](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/69844670-3162-49d7-8619-1cc405ef4e05/add1.png)

Doing this creates the Animation track with an Animation Sequence section at the playhead.

![sequencer animation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bfadc78d-26c0-446c-8604-46c732df5e37/createseq.png)

### Adding Animations

Once an Animation track is created, you can add animations to it. You can do this in the following ways:

Click **Add Animation (+)** on the Animation track and select an Animation Sequence. The animations listed here are filtered to only display [compatible](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletons-in-unreal-engine#compatibleskeletons) animations for the Skeletal Mesh.

![add animation sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/860dacef-29f3-4dbd-acb1-69adde8d3569/addanim.png)

You can also drag Animation Sequences from the **[Content Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-in-unreal-engine)** into the timeline area of Sequencer. This operation will preview the clip's length and drop points as you drag along the Animation track.

![drag drop add animation sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e87b6df9-56c7-41db-94d9-123b4c315187/dragdropanimcb.gif)


Dragging onto another clip will create a separate track for the animation.

## Usage

### Animation Mode

When a Skeletal Mesh is animated in Sequencer, its **Animation Mode** property will switch to **Use Custom Mode**. This is done to ensure Sequencer drives the Actor's animation using a special [Animation Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine).

![animation custom mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1b20a6a4-1277-4351-9e73-70aa04dbaca0/custommode.png)


Animation Mode will not switch to **Use Custom Mode** if an Animation Blueprint is already assigned. In that case, you should ensure the Animation Blueprint contains a [Slot](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-slots-in-unreal-engine) to receive animation from Sequencer.

### Layers and Blending

The Animation track supports multiple track layers, animations, and allows animations to be blended together in various ways.

![sequencer animation layers blend](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1954ec63-1b39-4bf9-9577-6ff690783725/animlayers1.gif)

You can add a second animation by clicking **Add Animation (+)** and selecting another Animation Sequence. This will add the new sequence to your current playhead time. If your playhead is placed over an animation, then it will create a new track layer for the animation.

![sequencer animation layer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b5e0447f-c42c-41da-b8db-2eef53203253/animlayers2.png)

Expanding the Animation track reveals the Weight attribute for the section, which has a value range of 0-1. Weights can be keyframed to allow for dynamic weighting and blending of animation sections.

![sequencer animation weight](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1e94c0e3-21a9-4155-a84b-32d7bea0367c/weight.png)

Animations can be moved between tracks by dragging them up and down.

![sequencer animation layer stack move up down](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/15e7e028-d56f-49a5-a710-d1d8092560d3/animlayers3.gif)

Intersecting two animation sections creates an automatic blend curve between them, and the animations blend over the duration of the intersection.

![sequencer blend clips together](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8930f4ba-9a5e-4fdb-9ce6-372231b9ae73/animblending1.gif)

You can adjust the **Start** and **End** blend curves by selecting and moving the blend curve handle located on the upper portion of the animation section's edge. A curve symbol will appear above the cursor to aid your selection accuracy.

![sequencer start end blend curve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2f8882d8-3a33-4a34-9fc3-2ece68835780/animblending2.png)

Right-clicking a blend curve reveals blend-specific context menu commands.

![blend curve menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5e939a01-4ae3-4f8e-95c9-a54fc480332d/blendcurvemenu.png)


| Name | Description |
| --- | --- |
| **Easing Length** | The length of the blend curve. Enabling **Auto** causes the blend curve to return to the default behavior and support automatic length calculation when sections are intersecting. blend curve length |
| **Method** | **Method** controls the type of curves to apply to the blend, and enables custom external blends based on functions. |
| **Options** | The Options menu will display a list of curve shapes that you can apply to your blend curve. Selecting one of these will replace your current curve shape with the selected curve. blend curve shape |

### Trim, Loop, and Play Rate

There are various ways you can edit your clips by looping, trimming, and time-scaling them.

Selecting either edge of the section and dragging inward will trim the section.

![sequencer trim animation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/327ff64a-026d-48d7-b83e-8cdbcd98ae78/trim1.gif)
