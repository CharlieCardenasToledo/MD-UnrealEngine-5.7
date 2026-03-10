# Curve Editor

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine

> Application Version: 5.7

When you want more control over the way your objects are animated, the Curve Editor can be used to modify and fine-tune your keyframes. Using the Curve Editor's graph, you can create new keyframes, edit tangents, and use various built-in tools to adjust your animation curves.

The Curve Editor is used in other tools across the Unreal Editor, such as [Niagara](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine), Curve Assets, and [Animation Curves](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curves-in-unreal-engine). This guide provides an overview of how to use the Curve Editor within Sequencer, however, many of the features and functions shown will still be compatible within other areas of the editor as well.

#### Prerequisites

* You have an understanding of [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine) and its [Interface](https://dev.epicgames.com/documentation/404).
* You have an understanding of [Keyframing in Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine).

## Curve Editor Overview

The Curve Editor can be opened from Sequencer by clicking the **Curve Editor** button in the [Sequencer Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine).

![open curve editor sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/626a97a0-44f3-430d-9f77-0cd9e819f0ba/opence.png)

Once the Curve Editor is opened, you will see the following view:

![curve editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e559b3cc-c08c-49a3-8609-cfdfe0c70fab/ceoverview.png)

1. [Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#toolbar)
2. [Outliner](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#outliner)
3. [Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#graph)

### Toolbar

The Curve Editor Toolbar contains various commands, tools, and options. These can be found listed in the table below.

![curve editor toolbar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/73cb4e90-c230-4c96-bb70-ba80d9876d1e/toolbar.png)

| Name | Icon | Description |
| --- | --- | --- |
| **Save** | save | Saves the current sequence and any subscenes or shots. |
| **View Modes** | view mode | Opens a dropdown menu for the Curve Editor [View Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#viewmodes). |
| **Zoom to Fit** | zoom to fit | Frames and zooms in on the selected keyframes. If no keyframes are selected, then all viewable keyframes within the Graph view will be framed. You can also use the **F** hotkey for this command. |
| **Focus Playhead** | focus playhead | Focuses the graph view on the [Playhead](https://dev.epicgames.com/documentation/404) without changing zoom level. You can also use the **A** hotkey for this command. |
| **Zoom to Playback Range** | zoom to playback range | Focuses the graph view so that all keyframes are visible, including the start and end frames of the sequence. |
| **Curve Options** | curve options | Opens a menu where you can set the following commands:   * **Tangent Visibility**, which controls how [Tangents](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#editing tangents) are drawn in the graph. You can choose from:    + **All Tangents**, which causes all keyframes to display their tangents, regardless of whether they are selected or not.   + **Selected Keys**, which only displays tangents on selected keyframes.   + **No Tangents**, which disables all drawing of tangents. * **Auto Frame Curves**, which causes automatic framing and zooming of all visible keyframes on a curve when it is selected from the [Outliner](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#outliner). * **Snap Time to Selection**, which moves the Playhead to the selected keyframe's time. If multiple keyframes are selected, the Playhead moves to the left-most keyframe. * **Buffered Curves**, which enables or disables drawing [buffered curves](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#buffercurves) in the graph. * **Curve Tooltips**, which shows a tooltip for a curve's name, time, and value when hovering your cursor over it in the graph. curve tooltips |
| **Time and Value Fields** | time and value | These property fields display the **Time** and **Value** of the selected keyframe. You can edit these properties directly by typing in new values. |
| **Selection Mode** | select | Enables normal keyframe and tangent selection and editing. You can also use the **Q** hotkey for this command. |
| **Transform Mode** | transform | Enables the [Transform Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#transformtool) for editing keyframes. You can also use the **Ctrl + T** hotkey for this command. |
| **Retime Mode** | retime | Enables the [Retime Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#retimetool), which activates a lattice manipulation mode for adjusting keyframe times. You can also use the **Ctrl + E** hotkey to enable this command. |
| **Multi Select Mode** | multi select | Enables the [Multi Select Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#multiselecttool), which activates a scaling mode for selected groups of keyframes based on an adjustable pivot. You can also use the **Ctrl + M** hotkey to enable this command. |
| **Time Snapping** | time snap | Enables keyframe [snapping](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#snapping) on horizontal (time) increments in the graph.  The snap increments are based on Sequencer's [Frames Per Second](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#framespersecond) if you are using the Curve Editor from Sequencer. Otherwise, you can click the nearby dropdown menu to select a custom time-based snapping increment. curve editor time snapping |
| **Value Snapping** | value snap | Enables keyframe [snapping](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#snapping) on vertical (value) increments in the graph. You can select the nearby dropdown menu to select a custom value-based snapping increment, as well as adjust the display of the graph lines. curve editor value snapping |
| **Lock Axis** | lock axis | Opens a dropdown menu for selecting which axis to lock keyframe movements to.   * **Both** is the default value and allows keyframe movement in all directions in the graph. * **X Only** restricts keyframe movement along the horizontal (time) axis only. * **Y Only** restricts keyframe movement along the vertical (value) axis only. |
| **Cubic (Auto) Tangent** | auto tangent | Sets the selected keyframes to interpolate automatically, causing the curve's tangents to adjust based on the location of neighboring keyframes in the graph. curve editor cubic auto tangent |
| **Cubic (User) Tangent** | custom tangent | Sets the selected keyframes to use user-defined tangent angles. Whenever you adjust a tangent angle, the keyframe will automatically switch to this mode. curve editor cubic user tangent |
| **Cubic (Break) Tangent** | broken tangent | Sets the selected keyframes tangents to use broken tangent angles, allowing for keyframes that have different incoming and outgoing tangent angles. curve editor broken tangent |
| **Linear Tangent** | linear tangent | Sets the selected keyframes to use linear tangent angles. This causes the incoming and outgoing tangents to always face their respective neighbors, resulting in abrupt changes when reaching each keyframe. curve editor linear tangent |
| **Constant Tangent** | stepped tangent | Sets the selected keyframe to use stepped tangent angles, causing keyframes to maintain their value until reaching the next keyframe. curve editor constant tangent |
| **Weighted Tangents** | weighted tangent | Sets the selected keyframe to use weighted tangent angles, causing tangents to use user-defined lengths which determines the influence that tangent angle exerts over its neighboring keyframe tangents. curve editor weighted tangent |
| **Pre Infinity Settings** | pre infinity | Opens a dropdown menu for selecting the [Pre-Infinity](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#preandpostinfinity) behavior of the selected keyframe or curve. |
| **Post Infinity Settings** | post infinity | Opens a dropdown menu for selecting the [Post-Infinity](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#preandpostinfinity) behavior of the selected keyframe or curve. |
| **Flatten Tangent** | flatten tangent | Flattens the tangents of the selected keyframes horizontally. curve editor flatten tangent |
| **Straighten Tangent** | straighten tangent | When using **Broken Tangents** on a keyframe, selecting this will straighten the tangent angles, but not unbreak them. The angles will straighten along an average angle between the two broken tangents. |
| **Filter Tool** | filter | Opens the [Filter Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#filtertool) window, where you can **bake**, **simplify**, and perform other curve functions. |

### Outliner

The Curve Editor Outliner contains header information for all animatable tracks added to your sequence, as well as a track filter and playback controls.

![curve editor outliner](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8eec432-df76-47a0-8e35-415f409a4151/outliner.png)

Selecting entries from the list automatically filters and frames the [Graph View](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#graph) to only display curves from that selection and any children. You can disable the auto-framing behavior by disabling **Auto Frame Curves** from the **Curve Options** toolbar menu.

![outliner filter selection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6d1b1dd4-e6c5-4c75-a492-071deb861165/outlinerselectfilter.gif)

You can also use the search bar to search for entries to narrow down the list. Any returned results will also include children tracks.

![outliner search](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8cd029d-b6ae-4879-8320-9b87dfd17a28/searchfilter.png)

Contents displayed in the outliner are determined by what tracks you have selected from Sequencer. Selecting tracks in the Sequencer window will cause only the selected tracks to appear in the Curve Editor Outliner. Deselecting all tracks in Sequencer will cause all contents to appear in the Curve Editor.

![outliner sequencer select filter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/de6a7e70-29d5-408f-86ab-8e57dbacf310/outlinerselectfilter2.gif)


You can disable this selection matching and filtering behavior by disabling **Synchronize Curve Editor Selection** and **Isolate Curve Editor to Selection** in the [Sequencer Editor Preferences](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-editor-and-project-settings-in-unreal-engine) window.

### Graph

The Curve Editor Graph contains a two-dimensional display of your keyframes, and the interpolated curves generated. The graph plots both **Time** and **Value** on the **Horizontal** and **Vertical** axes, respectively, and keyframes are positioned in the graph according to those properties.

![curve editor graph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9c86c112-2174-4af3-9ba6-ec211dce5415/graph.png)

## Graph Navigation

There are several ways to navigate within the graph, as well as different [View Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#viewmodes) you can use for representing curve data.

### Panning

Use **RMB** to pan the graph view freely.

![graph pan](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ffc8317f-cfae-4407-b3e0-008b1ab14071/pan1.gif)

Holding **Shift + RMB** will pan along either the horizontal or vertical axis, depending on the initial direction of your cursor.

![graph pan single axis](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d239d9cf-b90e-4282-9827-1b66fcc22447/pan2.gif)

Holding **Alt + MMB** will pan only along the horizontal axis.

![graph pan horizontal](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6036bf67-2314-4fef-85bf-960a07f34c7e/pan3.gif)

### Zooming

Scrolling the mouse wheel will zoom the graph relative to the [Playhead](https://dev.epicgames.com/documentation/404).

![graph zoom scroll](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4674546-13c5-4bae-95f7-d4f380582ed4/zoom1.gif)

Holding **Alt + RMB** will smoothly zoom the graph according to your cursor movement. The zoom pivot is relative to your cursor position upon pressing **RMB**.

![graph zoom cursor smooth](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4893227-ca19-4a85-822e-0d4fca7777d2/zoom2.gif)

Holding **Alt + Shift + RMB** will freely zoom the graph according to your cursor movement, which enables scaling time and value axes separately. Moving your cursor up and down will scale the value axis, and moving it left and right will scale the time axis.

![graph zoom free](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/98e2bc8c-240a-4825-84b3-5c377d8fdc14/zoom3.gif)

### View Modes

The **View Modes** menu contains different options to visualize your curves.

![curve editor view mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f7d5ab10-b664-4175-8706-42c16c4325d3/viewmodes1.png)

**Absolute View Mode** is the default view mode, in which all curves and keyframes are displayed at their exact values in the graph. This mode functions similarly to most animation curve editors.

![absolute view mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/83391be3-2a33-41f5-b0a1-b7de4d2bfa2f/viewmodes2.png)

**Stacked View Mode** will separate each curve into its own group, and stack them in the graph. Each group's value range is normalized between **-1** and **1**.

![stacked view mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4987482-de9f-4675-92c6-3e8126f0e8d2/viewmodes3.gif)

**Normalized View Mode** will display all curve and keyframe values overlapping along a normalized value range of **-1** and **1**. This view can be useful if you are wanting to universally scale curve amounts proportionally.

![normalized view mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c3416d91-1978-4f78-865a-cbaeb8405b8a/viewmodes4.png)

## Curve Editing

The Curve Editor is primarily used for editing your **keyframes** and **tangents**. You can add, remove, or change keyframe locations which affect the curve. You can also edit a keyframe's tangent, and control the incoming and outgoing curve vectors of a keyframe, which also affects the curve. There are also a variety of features and behaviors to help with your editing.

### Editing Keyframes

Keyframes can be moved by using **LMB** and dragging them around the graph. Depending on your **Snap** settings, it should be possible to move a keyframe anywhere along the time and value axes. You can also use **MMB** to move selected keyframes relative to your cursor position. This provides an easier way for manipulating keyframes without needing selection accuracy.

![curve editor move keyframe](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c3661d48-9536-4bb1-aed5-ab40744e3e30/movekey1.gif)

Holding **Shift** and dragging a keyframe will cause it to lock on either the horizontal or vertical axes as it moves, depending on the initial direction of your cursor.

![move key axis](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e60feb3c-a16b-4f44-a296-0c4db7220294/movekey2.gif)

Clicking a curve segment will select all keyframes for that curve. With these selected, you can move entire curves by dragging a keyframe or by using **MMB** to move the curve relative to your cursor.

![curve editor move entire curve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/33d96ae7-349e-4bda-b47d-9617f3320880/movekey3.gif)

### Creating New keyframes

Keyframes can be added along a curve by clicking **MMB** when your cursor is hovered over a curve segment.

![add key to curve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3378e5f0-db66-4816-b65d-08fc69139ae9/addkey.gif)

You can also create keyframes without disturbing the curve structure by holding **Ctrl** and clicking **MMB** on any curve segment.

![add key to curve without disruption](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/91fec6ae-150d-4241-bd98-1960d3ef768b/create2.gif)

### Copy and Paste

Keyframes can be **cut** (Ctrl + X), **copied** (Ctrl + C), and **pasted** (Ctrl + V) on the same curve and across different curves. There are also certain rules and contexts that determine the paste behavior.

When copying and pasting keys, they will paste at their original value and relative to the [Playhead](https://dev.epicgames.com/documentation/404). Pasting multiple keys will cause the starting (left-most) keyframe to be placed at the **playhead**, and all other keys relative to that point.

![copy paste curve keys](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/734f6d56-5686-414b-bd56-d00e1c034204/copypaste1.gif)

Depending on which curve you have selected and filtered in the [Outliner](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#outliner), the paste operation will occur on all curves within the current view.

![copy paste all curves](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fdbd9fc8-432d-4337-985d-d2b25c629d7c/copypaste2.gif)

If multiple curves are within the current view and you want to paste on only one of them, you can click the curve segment, which will select all keyframes for that curve, and press **Ctrl + V**.

![copy paste single curve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e7315c8-1a75-4ede-aab0-24ae324eac31/copypaste3.gif)

### Editing Tangents

When selecting your keyframes, they will display their **tangent** information. Tangents are lines that control the incoming and outgoing direction of the curve as it reaches the keyframe. You can select either side of the tangent handle and edit them to control the curve trajectory from that keyframe.

![tangents](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e65287a9-44ad-4875-ac9a-de33ebdbf3c8/tangents.png)


Depending on your **Tangent Visibility** settings in the **Curve Options** menu, your tangents may be displayed differently. Ensure this is set to **Selected Keys** for the default behavior.

![tangent visibility](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bfab5d17-9af8-4ec1-a6be-6a78800a02e6/tangentsettings.png)

To edit a Tangent, first select a keyframe, then select the tangent handle and drag it around in the graph. Similar to moving keyframes, you can also use the **MMB** to move the tangent relative to your cursor position.

![edit tangent curve editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/de30026c-f215-40f7-9d31-1fe3948a2976/edittangent1.gif)

Multiple tangents can be adjusted at the same time by multi-selecting them and using **MMB** to edit them.

![edit multiple tangents](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/97fecaa5-13e0-43fd-8ff7-29861542ec8f/edittangent2.gif)

If multiple keyframes are selected, clicking a single tangent will select all tangent handles of the same side.

![select all tangent handles](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0945323f-d33a-4491-988c-61772904952c/edittangent5.gif)

Holding the **Shift** key while moving your tangents will snap them to the nearest 45 degree increment.

![snap tangent angle](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a2ef4373-2a30-49e7-a587-8fbc472e3f13/edittangent3.gif)

Various tangent modes are located in the **toolbar**, and can be used to change the tangent angle of the selected keyframe. Reference the [Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#toolbar) section in this document to view their behaviors.

![tangent mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/95323132-15b5-40fe-ab6a-e5b18f95b2c3/tangentmodes.png)

### Weighted Tangents

With a keyframe selected, clicking the **Weighted Tangents** toolbar button will enable weighted tangent angles. This causes tangents to have user-defined lengths which determines the influence that tangent angle exerts over its neighboring keyframe tangents.

Once **Weighted Tangents** is enabled, you can stretch the tangent to increase its influence on the curve, or shrink it to decrease its influence.

![weighted tangent](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/80ebf08e-ebb4-4c30-84cc-b3f3001da0fd/edittangent4.gif)

### Buffer Curves

Curves can be temporarily saved and stored (known as buffering), which is useful when making experimental changes to your curves as these curves can be reverted to their stored state. While a curve is buffered, it will display an after-image on the graph for your reference.

To store a curve, right-click a part of the curve segment and select **Buffer Curves**.

![store curves](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c113ebc-524a-4f79-96ed-dad6bd21e09e/storecurve2.png)

After a curve is stored, you can make any edits you want to the curve. Keyframes and tangents can be added, edited, or removed. To revert your curve back to the original stored version, right-click the curve segment and select **Apply 1 Buffered Curves**. Buffered curve data is locked to the curve it is stored on, so you cannot buffer for one curve and then apply that buffered data to a different curve.

![apply stored curve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b846fb20-45f7-4635-8de5-83934e34847f/storecurve3.gif)

You can also **Swap** your curves, which restores the curve but also stores the changes you just made. To do this, right-click the curve and select **Swap Buffered Curves onto Selected Curves**.

![swap buffered curve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/205ec306-acf4-459b-8e8a-a3ad836004a9/storecurve6.gif)


Stored curves are lost whenever you close the Sequencer window.

### Pre and Post Infinity

Curves also contain rules for how they should behave in the timeframes before and after their keyframe segments. This is known as **Pre** and **Post Infinity**, and can be useful in order to extend the animation on a curve without needing to create additional keyframes. **Pre-Infinity** affects the curve region before the first keyframe, and **Post-Infinity** affects the curve region after the last keyframe.

![pre post infinity](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b4fdf7ed-0a64-4219-b389-0c8dac51f516/infinity1.png)

You can access the Pre and Post Infinity settings for your curves by clicking the **Pre** or **Post Infinity** buttons in the [**Toolbar**](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#toolbar), or by right-clicking a curve segment and selecting **Pre-Infinity** and **Post-Infinity**. Both methods require you have a keyframe selected from the curve you want to adjust .

![pre post infinity menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9f9847d7-4422-4685-baf5-cd47af2b5461/infinity2.png)

You can choose from the following infinity types:

| Name | Description |
| --- | --- |
| **Constant** | This is the default value for all new curves, and will cause the curve to retain its value leading up to the first key, and after the final key. constant infinity |
| **Cycle** | The curve will repeat, using the absolute values of the keyframes for each loop segment. cycle infinity |
| **Cycle with Offset** | Similar to **Cycle**, the curve will repeat, however each loop segment's value will be set relative to the previous, causing the curve to compound for each loop. cycle with offset infinity |
| **Linear** | The curve will project the first and last keyframe's tangent angle outward. linear infinity |
| **Oscillate (Ping Pong)** | Similar to **Cycle**, the curve will repeat, however each loop segment will mirror the previous, going backward and forward for each loop. oscillate ping pong infinity |

For looping-based infinity modes, such as Cycle and Oscillate, the loop length is defined by the number of keyframes used. Therefore, it will adjust as you add or adjust the length of your keyframe segments.

![cycle length infinity](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4c455824-fd0d-452a-b436-781ad51eaeb2/infinity3.gif)
