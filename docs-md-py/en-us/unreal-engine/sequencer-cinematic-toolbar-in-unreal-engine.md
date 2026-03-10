# Sequencer Toolbar Reference

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine

> Application Version: 5.7

This page provides a reference for Sequencer's Toolbar.

![sequencer toolbar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2adaab77-90dc-4d2f-a1fb-63a97683ce88/toolbar.png)


| Name | Icon | Description |
| --- | --- | --- |
| [**World**](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#world) | sequencer world | Lists information on the current world context, Level Sequence Actor, and playback realm. It contains options for specifying whether you want your sequence to autobind to Play In Editor (PIE), Simulation, or other runtime sessions. |
| **Save** | sequencer save | Saves the current sequence and any subscenes or shots. |
| **Find in Content Browser** | sequencer find | Locates the current sequence's Level Sequence asset in the Content Browser. |
| [**Create Camera**](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#createcamera) | sequencer camera | Creates a new **[Cine Camera Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine)**. A new **[Camera Cut Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-camera-cut-track-in-unreal-engine)** will also be created and will reference this camera if one had not already been created. |
| [**Render**](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#render) | sequencer render | Opens the **[Render Movie](https://dev.epicgames.com/documentation/en-us/unreal-engine/old-render-movie-in-unreal-engine)** Settings dialog, or the **[Movie Render Queue](https://dev.epicgames.com/documentation/404)** if its plugin is enabled. |
| [**Director Blueprint**](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#directorblueprint) | sequencer director | Opens the Director Blueprint for this sequence, from which **[Event Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-event-track-in-unreal-engine)** logic can be accessed. |
| [**Actions**](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#actions) | sequencer actions | Lists various sequence editor actions such as saving, import/export, baking, and selection editing. |
| [**View Options**](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#viewoptions) | sequencer view options | Lists various sequence view options. |
| [**Playback Options**](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#playbackoptions) | sequencer playback options | Lists various playback options such as playrate, start/end times, and playhead behavior. |
| [**Keyframe Options**](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#keyframeoptions) | sequencer keyframe options | Lists settings for Auto Key transform keyframing behavior, and what default tangents are created. |
| [**Auto Key**](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#autokey) | sequencer autokey | Enables Autokey mode, where keyframes are automatically created whenever a property or transform changes. |
| [**Edit Options**](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#editoptions) | sequencer edit options | Lists settings for how edits from the Details panel are interpreted by Sequencer when using Auto Key. |
| [**Snapping**](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#snapping) | sequencer snapping | Enables snapping. The dropdown menu next to this lists options for setting snapping rules for keyframes, sections, and the timeline. |
| [**Frames Per Second**](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#framespersecond) | sequencer fps | Lists settings for various Frames Per Second (FPS) targets at runtime. Also contains options to enable the runtime to lock to the chosen frame rate. |
| [**Curve Editor**](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#curveeditor) | sequencer curve editor | Opens the **[Curve Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine)** which is used for fine tuning of animation keyframes and tangents. |
| [**Breadcrumbs**](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine#breadcrumbs) | sequencer breadcrumbs | Displays the current sequence name, and is used to navigate master sequences and shots. |
| **Lock** | sequencer lock | Locks the entire sequence to prevent editing. |

## World

Sequencer's World menu contains options relating to the current Level, session, and the level sequence name.

![world menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3cc7b25b-b009-49fd-bfba-9da9db8dfc25/world1.png)

The **Actors** options category lists the running sessions that Sequencer can bind to, and provides you the option to switch your binding between them.

In this example you can see there are now two sessions being run: **Editor** and **Simulate**. You have the option to switch between them which causes Sequencer to bind to that realm instead.

![world menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c88fab45-c6ab-4eb6-a42f-3d2ec00212ce/world2.png)

**Auto Bind to PIE** and **Simulate** enable the automatic binding of Sequencer to their respective realms when they begin to run.

## Create Camera

Clicking the **Create Camera** button will automatically create a **[Cine Camera Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine)** and a **[Camera Cut Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-camera-cut-track-in-unreal-engine)** with a binding to the new camera. Your viewport will also begin piloting the camera, which will prepare you to start framing your shot.

![sequencer create camera](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0102a220-d3d3-419f-9525-12774b088ede/createcamera.gif)

You can specify if this camera is spawnable or posessable by toggling **Create Spawnable Camera** in the **[Editor Preferences and Project Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-editor-and-project-settings-in-unreal-engine)** window.

## Render

Clicking the Render button will open the **[Render Movie](https://dev.epicgames.com/documentation/en-us/unreal-engine/old-render-movie-in-unreal-engine)** Settings dialog box, from which you can render your sequence as a series of images.

![sequencer render](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/744dbadd-88fc-42a0-b567-7f2f14117f7a/renderbutton1.png)

If you have enabled the **[Movie Render Queue](https://dev.epicgames.com/documentation/404)** (MRQ) plugin, then the button will have a dropdown menu from which you can choose between launching the new MRQ tool or the legacy rendering tool.

![sequencer mrq button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c2c90c3-954c-41a1-a77b-e8e9e1b17a9e/renderbutton2.png)

## Director Blueprint

Clicking the Director Blueprint button opens the Sequence Director window, from which you can see your sequence's **[Event Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-event-track-in-unreal-engine)** events.

![sequencer director](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3ac204cf-ecb7-4f4b-b6c4-9fdbdd473bcd/directorbutton.png)

## Actions

The Actions button displays a dropdown menu with the following tools, commands, and options:

![sequencer actions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b2f46974-ed65-48fc-88f7-3fa60cd9e6cf/actionsbutton.png)

| Name | Description |
| --- | --- |
| **Save As...** | Saves the current sequence and provides the option to select a different name. |
| **Import...** | Imports an FBX animation file to the selected Actor. If no Actor is selected then the importer will attempt to apply the animation to the entire sequence. Visit the **[Importing and Exporting FBX files](https://dev.epicgames.com/documentation/en-us/unreal-engine/import-and-export-cinematic-fbx-animations-in-unreal-engine)** page for more information. |
| **Export...** | Exports a selected Actor to an FBX file. If no Actor is selected then the entire sequence will be exported. Visit the **[Importing and Exporting FBX files](https://dev.epicgames.com/documentation/en-us/unreal-engine/import-and-export-cinematic-fbx-animations-in-unreal-engine)** page for more information. |
| **Open Director Blueprint** | Opens the Director Blueprint for this sequence, from which Event Track logic can be accessed. |
| **Open Binding Tag Manager** | Opens a tool from which you can create Tags. These tags are applied to Actors which allows them to be identified in a Blueprint to perform special functions. Visit the **[Sequencer Tags and Groups](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-tags-and-groups-in-unreal-engine)** page for more information. |
| **Open Sequencer Group Manager** | Opens a tool that displays custom groups and the tracks applied to them. Visit the **[Sequencer Tags and Groups](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-tags-and-groups-in-unreal-engine)** page for more information. |
| **Restore Pre-Animated State** | Snaps all Actors back to their default editor positions. Playing or scrubbing the sequence will snap them back to their Sequencer-determined positions. |
| Transform |  |
| **Transform Selection** | Opens a tool you can use to modify keyframes and sections relative to the playhead time. You can move keys in a positive and negative numerical direction, or multiply and divide their relative distance from the playhead. sequencer transform selection |
| **Stretch/Shrink** | Opens a tool used for adding and removing time in your sequence relative to the playhead time. sequencer stretch shrink |
| **Translate Left** | Moves a selected keyframe 1 frame to the left relative to the sequence's frame rate. |
| **Translate Right** | Moves a selected keyframe 1 frame to the right relative to the sequence's frame rate. |
| **Trim or Extend Section Left** | Trims or extends a selected track's section from its left/start point to the playhead location. If no track is selected, then all sections will be trimmed or extended. |
| **Trim or Extend Section Right** | Trims or extends a selected track's section from its right/ending margin to the playhead location. If no track is selected, then all sections will be trimmed or extended. |
| **Bake Transform** | Selecting this will bake a selected Actor's transform in world space. Any existing attachment or transform tracks will be disabled. This behavior can be changed by locating the **Disable Sections After Baking** preference in the **[Editor Preferences and Project Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-editor-and-project-settings-in-unreal-engine)** window. If you disable it, any existing tracks overwritten during the bake will be deleted. |
| **Sync Sections using Source Timecode** | Synchronizes sections with the first selected section using its source timecode. |
| Selection Range |  |
| **Set Selection Start** | Sets the start point of a custom timeline selection range to the playhead time. |
| **Set Selection End** | Sets the end point of a custom timeline selection range to the playhead time. |
| **Clear Selection Range** | Removes the selection range. |
| **Select Keys in Selection Range** | Selects all keyframes within the selection range. Does not select sections. |
| **Select Sections in Selection Range** | Selects all sections within the selection range. Does not select keyframes. |
| **Select All in Selection Range** | Selects all keyframes and sections within the selection range. |
| Advanced |  |
| **Fix Actor References** | Attempts to automatically fix broken Actor bindings by matching the object binding name with an Actor in the Level with the same name. |
| **Rebind Possesable References** | Rebinds all posessable Actors in the current sequence to ensure they're using the most robust referencing mechanism. |
| **Networking** | Lists options for emulating the current sequence in a Client or Server context. |
| **Volatile** | Signifies that this sequence can change dynamically at runtime or during the game. This property must be set if any procedural changes will be made to the source sequence data in game. |
| **Blocking Evaluation** | Enables the sequence to fully evaluate and apply its state every time it is updated. |

## View Options

The View Options button displays a dropdown menu with the following tools, commands, and options:

![sequencer view options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/491be97c-ffb7-4284-bc3a-ab15e123bd75/viewbutton.png)
