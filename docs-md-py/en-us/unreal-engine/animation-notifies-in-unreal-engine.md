# Animation Notifies

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-notifies-in-unreal-engine

> Application Version: 5.7

**Animation Notifications** (Animation Notifies or just Notifies) provide a way for you to create repeatable events synchronized to **Animation Sequences**. These events can be sounds (such as footsteps for walk or run animations), spawning particles, and other types. Animation Notifies have any number of different uses, and the system can be extended with custom types.

This document provides an overview of the different types of Animation Notifies, how to create them, and how to use them in a variety of ways.

#### Prerequisites

* Animation Notifies are created within [Animation Sequences](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine), therefore your project needs a **Skeletal Mesh** and an **Animation Sequence**.

## Getting Started

Animation Notifies are commonly accessed and created within Animation Sequences. To get started, open an **Animation Sequence Asset**, and locate the **Notifies** track in the timeline.

![notify track](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7ab47103-6082-4733-b574-b4ef50cc7d40/start1.png)

The Notifies track itself is a parent group for individual child tracks below, which contain the actual notify keyframes. By default, a single child track should exist (named **1**). If no child tracks exist, or if you want to add extra notify tracks, click **Add Track (+) > Add Notify Track** on the Notifies track.

![child notify tracks](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eeda4ef2-f99d-4228-8c8e-609b92b8815f/start2.png)


You can also insert or remove notify tracks by clicking the **Add Track (+) dropdown menu** on the child track itself and selecting either **Insert Notify Track** or **Remove Notify Track**.

![insert and remove notify tracks](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/00f1ca05-8a68-4474-9815-d2b4bcf0f46e/start3.png)

To rename a Notify track, triple-click on the track text to enable text editing.

![rename notify track](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48b059ad-05aa-462e-9dd9-fc989d05503d/start4.gif)

## Animation Notify Types

There are several types of Animation Notifies you can create, which are viewed when creating Notifies by right-clicking in the Notify track's timeline region.

![animation notify types](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/17678c1c-323d-4100-b15b-6145a717fec7/types.png)

### Notify

The most basic kind of Animation Notify you can create is simply called a **Notify**, which causes different pre-made events to be triggered at a specified time. The following Notifies can be found when viewing the **Add Notify…** menu. Selecting one will create the Notify keyframe at your cursor position.

![notify](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c3cead08-4907-4133-94c8-691331e5ca3a/typenotify1.png)

Notify keyframes can be edited by dragging them in the timeline. You can also hold **Shift**, which will move the **Playhead** in sync with the Notify, making it easier to align the Notify with a specific time in the animation.

![interact with notify](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/773cf240-72d8-46da-a01b-d5499a9d0225/typenotify2.gif)

#### Particle Effect

**Particle Effect** Notifies are used to spawn and play non-looping particle systems. You can select either:

* **Play Niagara Particle Effect**, which spawns [Niagara particles](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine).
* **Play Particle Effect**, which spawns [legacy Cascade particles](https://docs.unrealengine.com/4.27/RenderingAndGraphics/ParticleSystems).

This Notify is useful for creating repeatable particle effects, such as an effect when a character lands from jumping, shooting effects for a Skeletal Mesh weapon, or other similar effects.

![particle notify](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/216c8796-50fa-4b74-b022-3f89ad9338ab/particle1.gif)

When selecting the Particle Notify keyframe, the following relevant properties are located in the **Details** panel:

![particle notify properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df5d997d-ab5c-40eb-b4c5-32ee48630001/particle2.png)

| Name | Description |
| --- | --- |
| **Particle System / Niagara System** | The Cascade or Niagara system to spawn for this Notify. |
| **Location / Rotation / Scale Offset** | An array of location, rotation, and scale transform properties to offset the system from its spawn point. |
| **Attached** | When spawned on a [Socket](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-sockets-in-unreal-engine), enabling this causes the particle system to follow the Socket for its full duration. Disabling this still spawns the particle system at the Socket location, but the system does not continue to follow the Socket. |
| **Socket Name** | You can specify a bone or [Socket](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-sockets-in-unreal-engine) here, which spawns the particle system at its location. If nothing is specified here, then the system spawns at the root of the object. |

#### Sound

**Sound** Notifies are used to play sound effects from imported Sound Waves, [Sound Cues](https://dev.epicgames.com/documentation/en-us/unreal-engine/sound-cues-in-unreal-engine), and [MetaSounds](https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-in-unreal-engine). These Notifies are useful for synchronizing foley-type sounds to animations, such as footsteps, cloth movements, and similar repeatable sounds.

When selecting the Sound Notify keyframe, the following relevant properties are located in the **Details** panel:

![sound notify](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b58a33ee-c207-4931-8487-f7750a17e4d2/sound1.png)

| Name | Description |
| --- | --- |
| **Sound** | The sound asset to play for this Notify. You can select the following assets:   * Sound Wave * Sound Cue * MetaSound * Sound Bus |
| **Volume Multiplier** | A multiplier to increase or decrease the volume of the playing sound. |
| **Pitch Multiplier** | A multiplier to increase or decrease the pitch of the playing sound. |
| **Follow** | If enabled, the sound effect source follows the animated mesh as it moves. If disabled, the sound remains behind at the location it spawned. |
| **Preview Ignore Attenuation** | If enabled, [sound attenuation](https://dev.epicgames.com/documentation/en-us/unreal-engine/sound-attenuation-in-unreal-engine) is disabled when playing the sound. This setting is editor-only and does not impact normal sound attenuation operation when playing or simulating the game. |
| **Attach Name** | If **Follow** is enabled, you can specify a bone or Socket to attach to. If nothing is specified here, then the sound spawns at the root of the object. |

#### Clothing Simulation

**Clothing Simulation** Notifies are used to pause, resume, and reset cloth simulations on a character. These Notifies are useful if you are teleporting the character during the animation and need to pause or reset cloth evaluation. They can also be useful if your animations are causing the cloth simulation to overreact.

![cloth notify](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bc9bac01-9d49-4f60-a628-3bf648e3d6ab/cloth1.gif)

You can select the following Notifies:

* **Pause Clothing Simulation**, which pauses the simulation.
* **Resume Clothing Simulation**, which restores the simulation after having been paused.
* **Reset Clothing Simulation**, which initializes the simulation back to its default reference pose.

#### Reset Dynamics

The **Reset Dynamics** Notify can be used to restore any [AnimDynamics](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-animdynamics-in-unreal-engine) used on this Skeletal Mesh back to their original state. This Notify is useful if your animations are causing the AnimDynamic simulation to overreact or enter broken-looking states.

### Skeleton Notify

**Skeleton** Notifies are custom Notifies saved on the [Skeleton Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletons-in-unreal-engine), and then used as events within your [Animation Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine). These Notifies are useful for creating any arbitrary Blueprint logic you want a Notify to execute.

To create a Skeleton Notify, right-click on a Notify track, then select **Add Notify > New Notify…**

![skeleton notify](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a2c883d5-13e7-4afd-a598-e56bfccdfa5a/skelnot1.png)

You will be prompted to enter a name for the newly created Notify. Name it and press **Enter** to create the Skeleton Notify.

![skeleton notify creation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9abec0ed-37cb-40f7-823e-68adf2f46c37/skelnot2.png)


Skeleton Notifies are stored on the **Skeleton Asset**. Therefore, when creating them, you are also editing the [Skeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletons-in-unreal-engine), which requires you to save it.

You can also add currently-existing Skeleton Notifies to the timeline by right-clicking a Notify track, then selecting one from the **Add Notify > Skeleton Notifies** menu.

![add pre-exiting skeleton notify](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8d7f5ada-edf6-4fb2-9c6c-b1ce427af085/skelnot3.png)

Skeleton Notifies are used as **Notify Events** within Animation Blueprints, either in the [Event Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/graphing-in-animation-blueprints-in-unreal-engine#eventgraph) or [Transition Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/transition-rules-in-unreal-engine). To add a **Skeleton Notify Event**, right-click in the **Event** or **Transition Graph** of your **Animation Blueprint** and select the **Notify** from the **Add Anim Notify Event** menu. This adds the event node to the Graph which is executed when the Notify is called from the animation it resides in.

![skeleton notify animation blueprint event](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/37cb7236-0d4a-485d-94a9-5af7864a349e/skelnot4.png)

### Notify State

**Notify States** work similar to standard Notifies, however they operate over a duration, rather than a single event. Because of this, they provide three distinct events: a **start**, an **update**, and an **end**. These events can be accessed when creating [Notify State child classes](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-notifies-in-unreal-engine#customnotifyclasses).

Also like standard Notifies, they provide several different pre-made classes to choose from. You can find the following notifies when viewing the **Add Notify State…** menu. Selecting one creates the Notify keyframes at your cursor position.

![animation notify state](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eb21d25b-aba2-4c67-80ed-a1db72fac9bd/notifystate1.png)

Notify State keyframes are edited similar to normal Notifies by dragging them in the timeline. You can either drag the start or end to edit the range, or drag the whole Notify.

![interact with state keyframes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/37efb6e7-93a2-464a-a701-e23cc6aea9c2/notifystate2.gif)

#### Timed Particle Effect

Similar to [Particle Effect](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-notifies-in-unreal-engine#particleeffect) Notifies, **Timed Particle / Niagara Effects** Notifies are used to play particles during an animation. The main difference is that you can also define the duration of the particle, if the particle is set to loop. You can select the following types of Particle Notifies:

* **Timed Particle Effect**, which spawns [legacy Cascade particles](https://docs.unrealengine.com/4.27/RenderingAndGraphics/ParticleSystems).
* **Timed Niagara Effect**, which spawns [Niagara particles](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine).
* **Advanced Timed Niagara Effect**, which spawns Niagara particles with extra options for driving parameters within them.

Timed Particle Notifies share the same details with normal Particle Effect Notifies, however Advanced Timed Niagara Notifies contain the following additional properties:

![timed particle notify](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ce42c032-5187-4c5b-8634-5dbc19d00f10/timedparticle1.png)

| Name | Description |
| --- | --- |
| **Enable Normalized Notify Progress** | When enabled, causes the Notify state to output a normalized (0-1) value over the duration of the Notify to the Niagara [User Parameter](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-niagara-effects-for-unreal-engine#parametersandparametertypes) specified in **User Parameter**. The parameter starts at **0** and interpolates to **1** upon the notify finishing. This property is useful if you want to link certain particle parameters to the lifetime of the notify. |
| **User Parameter** | The name of the Niagara User Parameter to drive if **Enable Normalized Notify Progress** is enabled. |
| **Anim Curve Parameters** | An array where you can link [Animation Curve](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curves-in-unreal-engine) values to Niagara User Parameters. You can add items to the array by clicking **Add (+)**, then specify the following properties:   * **Anim Curve Name**, which is the Animation Curve that drives the Niagara parameter. * **Niagara User Float**, which is the Niagara User Parameter controlled by the Animation Curve. |

#### Trail

**Trail** Notifies are similar to Timed Particle Effects in that they spawn a particle system over the duration of the Notify. It differs because it is primarily used for [AnimTrail Cascade Particles](https://youtu.be/5HkghxEIXiU)**,** and contains additional properties for controlling trail attachment and properties.

![trail notify](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b3f27c0-f8d0-4500-b523-1dd8022b0694/trailnotify1.gif)

Selecting the Trail Notify reveals the following properties in the **Details** panel.

![trail notify details](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d348ab4e-cd30-4936-ad64-77bd122982b2/trailnotify2.png)

| Name | Description |
| --- | --- |
| **PSTemplate** | The AnimTrail Cascade Particle system to use. |
| **First / Second Socket Name** | You can specify a separate bone or Socket here for each property, which are used to define the attach points for the AnimTrail. This also defines the trail's default width, based on the distance between these two attach points. |
| **Width Scale Mode** | If **Width Scale Curve** is used, this defines the relative scale point of the trail's width. You can select the following options:   * From Centre, which scales the trail relative to the **center point** between the two sockets. * From First Socket, which scales the trail relative to the location of the **first Socket**. * From Second Socket, which scales the trail relative to the location of the **second Socket**. |
| **Width Scale Curve** | You can optionally specify an [Animation Curve](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curves-in-unreal-engine) here, which can be used to animate the scale width of the trail during the animation. A value of **1.0** maintains the default width, higher numbers increase the width, and lower numbers decrease the width. |
| **Render Geometry** | Enables rendering of the main trail geometry, leave this enabled. |
| **Render Spawn Points** | Enables debug rendering of the primary spawn points for the trail. |
| **Render Tangents** | Enables debug rendering of the curve tangents. |
| **Render Tessellation** | Enables debug rendering of all vertices on the curve, showing how the curve is tessellated between the spawn points. |

### Sync Marker

Sync Markers are Notifies used to inform [marker-based animation syncing](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sync-groups-in-unreal-engine#marker-basedsyncing), which is useful for blending animations together and keeping overall motion synchronized. Similar to [Skeleton Notifies](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-notifies-in-unreal-engine#skeletonnotifes), Sync Markers save to the Skeleton Asset, which requires you to save the Skeleton when adding them. You can then use the same Sync Markers repeatedly in any animation you want to synchronize while blending.

![sync marker notify](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fb9c2821-fabc-4aa1-a378-097eb759afea/markers1.png)
