# Keyframing

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine

> Application Version: 5.7

Tracks and content in Sequencer are animated by creating **Keyframes** (also referred to as **Keys**) with defined properties at specific points along the timeline. When the playhead reaches a key in the timeline, the properties are updated to the values defined at those points. Properties can either gradually change (interpolate) between keyframes, or change immediately to the specified value upon reaching the keyframe (no interpolation).

Keyframes and track states reside within grouped containers, called **Sections**. Sections are time ranges in which the track is being evaluated by Sequencer. They can either have an infinite or finite length, and also can be moved, trimmed, or blended.

This guide provides an overview of animation keyframing in Sequencer, and how sections enhance the animation feature set.

#### Prerequisites

* You have an understanding of [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine) and its [Interface](https://dev.epicgames.com/documentation/404).

## Keyframes

Similar to most animation software, objects are animated in Sequencer by creating keyframes within the timeline. Keyframes enable the animation of an object's position, color and other attributes. Most Actor properties can be animated in Sequencer, and therefore also be keyframed.

![keyframe example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6ac60f20-6668-4716-b85f-0ddf266cd5e8/keyframes.png)

### Creation

There are a variety of ways to create keyframes in Sequencer. In most cases when a keyframe is created, it will be created at the location of the [Playhead](https://dev.epicgames.com/documentation/404). If the playhead is at the same location as an existing keyframe when placing a new keyframe, it will be overwritten with the new keyframe.

| Keyframe Creation Method | Image |
| --- | --- |
| Clicking the **Add Key** button on a track. | add key |
| Clicking the **Add Key** button next to a property in the selected Actor's Details panel.  The Actor or track does not need to be added to Sequencer for this to work. If it isn't added, it will automatically be added to Sequencer and keyframed. | add key details |
| Pressing **Enter** on your keyboard will place keys on the selected tracks.  If you have an Actor track selected, pressing **Enter** will create keyframes on all keyable child tracks. | add key enter |
| Adjusting the property value displayed along the property track will add a new keyframe if the track already contains keyframes. You can either drag the property left and right to scrub its value, or click it and manually type a new value. | add key value change |
| Clicking the **middle mouse button** along the track's timeline will create a keyframe at the playhead's position. The keyframe value will match the value at the playhead's position. | add key mmb middle mouse |
| Pressing **S** with an Actor selected creates a **[Transform Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine)** (if one does not already exist) and creates a keyframe with its current **Location**, **Rotation** and **Scale** properties.  This command also works if your window focus is on the viewport, mirroring Maya's keyframing hotkeys. It also will automatically add any Actor to Sequencer, if they currently are not being referenced inside your sequence. | add key s |
| Pressing **Shift + W** with an Actor selected creates a Transform track (if one does not already exist) and keyframes the **Location** property only. | keyframe location only |
| Pressing **Shift + E** with an Actor selected creates a Transform track (if one does not already exist) and keyframes the **Rotation** property only. | keyframe rotation only |
| Pressing **Shift + R** with an Actor selected creates a Transform track (if one does not already exist) and keyframes the **Scale** property only. | keyframe rotation only |

#### Auto Key

Keyframes can also be set up to create automatically whenever you change an Actor's properties, which is known as **Auto Keying**. To use Auto Key, you must enable the [Auto Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#autokey) button in the [Sequencer Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine).

Once enabled, modifying Actor properties will cause new keyframes to be created.

![sequencer auto option](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bc012162-eb80-4955-ac86-8befc4fbf5f9/autokey.gif)


The track you are auto keying must already have keyframes present in order to automatically create new keyframes. An empty track will not be auto keyed.

You can also open the [Keyframe Options Menu](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#keyframeoptions) to change the number of keyframes that are automatically created when channel keyframes are being auto keyed. Channel keyframes are property types made up of several properties, such as [Vectors](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine#vectors) or [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine#transformtrack).

![auto key settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/47b50a74-0835-48f7-bdd5-f8fabc804b25/autokeyoptions.png)

| Auto Key Option | Description |
| --- | --- |
| **Key All** | All channels and groups will be keyframed when a value is changed. For example, in transform, if you only edit the X-Location property of an Actor, then keyframes will be set on the full XYZ **Location** channels as well as all channels in **Scale** and **Rotation**. |
| **Key Group** | All axes within a channel will be keyframed when a value is changed. For example, in transform, if you only edit just the X-Location property of an Actor, then keyframes will be set on the full XYZ **Location** channels. |
| **Key Changed** | Only the axis that changes will be keyed. For example, in transform, if you only edit the X-Location property of an Actor, then only the X-Location channel will be keyframed. |

#### Duplication and Copy Paste

Keyframes can be created by duplication and copy / paste methods. You can duplicate a keyframe by right-clicking it and selecting **Duplicate** or by pressing **Ctrl+D**. Doing this will create a duplicate keyframe at the same location as the original.

You can also duplicate a keyframe by holding **Alt** and dragging a key, or group of selected keys along the timeline.

![keyframe alt copy duplicate](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5c34c4ab-af76-4590-ae1a-3f4b3721ac6a/altduplicate.gif)

Keyframes can be copied and pasted using standard **Cut** / **Copy** / **Paste** commands. You can either right-click a keyframe and select one of these commands, or use the **Ctrl + X**, **Ctrl + C,** **Ctrl + V** hotkeys on a selected keyframe or group of keyframes. When keyframes are pasted, the left-most keyframe will paste at the same location as the playhead, and the keyframe group (if multiple keys were copied) will be placed relative to that location.

![keyframe copy paste](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b2d29279-05de-4382-b92c-51ddd4c00cd7/copypastekeys.gif)

### Selection and Movement

Keyframes are selected by clicking them individually or by dragging a marquee selection around a group of keyframes. Keyframes from other tracks can be included in your selection when using marquee selection, and are highlighted when included within the marquee selection box.

![keyframe selection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/06b341a7-00ce-4347-a2c3-218a1c33dd51/selectingkeys.gif)

You can change the time of a keyframe by dragging it left and right. Multiple selected keys can also be moved relative to each other.

![move keyframe](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8fac29fe-8d87-439f-9653-dd1de02b2d5c/movekeys.gif)


By default, the timeline [Playhead](https://dev.epicgames.com/documentation/404) will automatically snap to a selected keyframe, and will continuously snap to the keyframe while dragging it along the timeline. You can change this behavior by disabling both the **Snap to the Pressed Key** and **Snap to the Dragged Key** settings in the [Snapping](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#snapping) toolbar menu.

Use **Ctrl + ]** and **Ctrl + [** to select all keyframes to the left or right of the playhead's location.

![select keyframe forward backward](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d9671be0-dded-4a73-aabc-361123302df2/selectforwardback.gif)

### Layer Bars

To assist with movement and scaling of multiple keyframes at the same time, you can utilize **Layer Bars** to manipulate your keyframes. When multiple keyframes or sections exist on your Actor or Component, this bar will appear along the header track of the object which you can move and trim.

![sequencer layer bars](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ef2f772c-fa59-4938-97b3-bb291f815cce/layerbar1.png)

Dragging the center portion of the bar moves all child keyframes and sections in a grouped manner. Dragging the edges will scale the keyframes and sections relative to that edge.

![manipulate layer bar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a793ea0c-b3d9-44fd-8f3a-349a77f4668b/layerbar2.gif)


Layer Bars are hierarchical and will appear on lower Component Tracks, and also [Folder Tracks](https://dev.epicgames.com/documentation/en-us/unreal-engine/organize-cinematic-tracks-in-unreal-engine). Manipulating them at any of these points will appropriately manipulate keys, sections, and other Layer Bars of all Actors within. This makes it easier to manipulate keyframes on your Actors without needing to expand to the tracks to do so.

![layer bar hierarchy](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca4a0923-f001-4bad-a4c6-2f89ecb3f870/layerbar4.gif)

You can enable or disable this feature by navigating to the **View Options** menu in Sequencer and selecting **Layer Bars**.

![enable or disable layer bars](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/84a15efb-105d-4671-9b4b-9fa13c6a358e/layerbar3.png)

### Key Bars

If you want to retime neighboring pairs of keyframes, you can select and drag the line drawn between two keyframes. This will move both keyframes relative to each other. This method of manipulating keyframes can be useful to save time from multi-selecting each key individually, and preserving custom curves between these keys.

![maniplate key bars](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf18105d-c83a-434b-b5f4-a121579b133f/keybars1.gif)

You can enable or disable this feature by navigating to the **View Options** menu in Sequencer and selecting **Key Bars**.

![enable or disable key bars](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5dabd06d-65e6-48cc-a7db-c70b1e80296c/keybars2.png)

### Interpolation

Keyframes can either **Interpolate** or **not Interpolate**. Keys that interpolate will gradually change the values of the property they are animating over time, while keyframes that don't interpolate will retain their value until the next keyframe is reached. An example of non-interpolating keyframes would be when keyframes created on an [Event Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-event-track-in-unreal-engine), [Boolean Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine#boolean), or [Enum Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine#enum)

![keyframe interpolation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/20e20112-a477-4167-8a3f-dc8ac6a56252/interpolatecompare.png)

1. **Non-Interpolating Keyframes**: These keyframes are displayed using a **white diamond** shape.
2. **Interpolating Keyframes**: These keyframes are displayed using a **red circle**, or other colored shape if using different tangents.

Keyframes that interpolate can have their **tangents** adjusted. Tangents are properties on the keyframe that control the speed and easing angle of the interpolation between keyframes. Depending on the tangent type chosen, the keyframe icon will display differently to denote its tangent property

![keyframe tangent type display](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f959ec12-b7d1-4408-bd43-4e9f774f0804/tangentkeys.png)

There are five main types of tangents you can select:

| Tangent Name | Keyframe Icon | Description |
| --- | --- | --- |
| **Cubic (Auto)** | cubic auto | The Cubic (Auto) tangent type is the default tangent type. It attempts to maintain a smooth curve between keyframes and eases both the start and end keyframes. It will automatically adjust whenever keyframes are added or moved. |
| **Cubic (User)** | cubic user | Cubic (User) is similar to Cubic (Auto), but it will lock the tangent from any further automatic edits when keyframes are added or moved. Cubic (Auto) keyframes will convert to Cubic (User) when manual tangent edits occur within the [Curve Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine). |
| **Cubic (Break)** | cubic break | Cubic (User) is similar to Cubic (Auto), but its tangents are **broken**, allowing for different incoming and outgoing angles to be specified from the Curve Editor. |
| **Linear** | linear | Linear tangents cause keyframes to have no smoothing or easing between them, causing abrupt starts and stops when reaching each keyframe. |
| **Constant** | constant | Constant tangents function similarly to non-interpolating keyframes by maintaining their current value until the next keyframe is reached. |

You can convert an existing keyframe's tangent type by right-clicking it and selecting a tangent type from the **Key Interpolation** menu category.

![change tangent menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d223814e-326d-4c78-be06-ff6bc16f728e/tangenttype.png)


Hotkeys can also be used to change a selected keyframe's tangent. Pressing **1**, **2**, **3**, **4**, or **5** on your keyboard will change the tangent to **Cubic (Auto)**, **Cubic (User)**, **Cubic (Break)**, **Linear**, or **Constant**, respectively.

The default tangent for newly created keyframes can be changed by clicking the [Keyframe Options](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#keyframeoptions) button in the Sequencer toolbar and selecting a tangent type from the **Default Key Interpolation** menu category.

![default tangent](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/962ae093-aca6-4b60-bbde-c2bf22a99906/defaulttangent.png)

### Properties

Right-clicking a keyframe and navigating to the **Properties** menu will display the keyframe's current **Property Values** and **Time**. Depending on the [Property Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine) being animated, the **Properties** menu display will vary according to the property.

![keyframe properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8424ca2d-dd7c-4155-83f3-484ec1f35811/keyframeproperties.png)

There are also keyframe-specific commands you can use to edit your keyframe time.

| Name | Description |
| --- | --- |
| **Set Key Time** | Selecting this will cause a new window to appear from which you can specify a new time for the keyframe. set key time |
| **Rekey** | Snaps the keyframe to the [Playhead](https://dev.epicgames.com/documentation/404). rekey |
| **Snap to Frame** | Snaps all selected keyframes to their nearest frame, as defined in the [Frames Per Second](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#framespersecond) toolbar menu. snap to frame |
| **Delete** | Deletes the selected keyframe. |

## Sections

In the context of keyframes and keyframing actor properties, Sections are the groups that contain keyframes. They function similar to animation layers found in other animation tools, but with some differences. While layers usually do not consider time ranges for their keyframes, Sections do, which enable features such as offsetting whole chunks of keyframe data easily, without needing to select and move every keyframe individually. All keyframes reside within sections, either infinite or finite in length.

![sections example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6d22d88a-7944-4eef-af79-754180409dd9/sections.png)
