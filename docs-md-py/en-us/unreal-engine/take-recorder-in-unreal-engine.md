# Take Recorder

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine

> Application Version: 5.7

**Take Recorder** records gameplay animation, live performances, and other sources into Unreal Engine directly. By recording and managing takes into Sequencer, you can achieve a highly iterative workflow in your virtual production.

## Common Uses

Some of the main use cases and features of **Take Recorder** are:

* **Animation Recording**: Record animations and motions of characters or objects in the game world. This provides you with a way to create custom animations by manipulating the characters directly in the level.
* **Camera Recording**: Capture camera movements, angles, and focal lengths. This is useful for creating dynamic camera shots for in-game and non-game cinematics.
* **Sequencer** Integration: Seamlessly integrates with Unreal Engine's **[Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview)**, which is the timeline-based cinematic editing tool. This integration can use recorded takes directly in Sequencer for further editing and compositing.
* **Multiple Takes**: Create multiple takes for the same scene or action. This gives you the flexibility to experiment with different variations or performances without having to re-record everything from scratch.
* **Non-Destructive Workflow**: Non-destructive workflow ensures that your original animations and gameplay data remain untouched, which gives you the capability to make changes and adjustments without losing previous recordings.
* **Metadata Support**: Store metadata alongside recorded takes. This metadata can include character names, shot descriptions, and other relevant information, which helps organize and manage your recordings.
* **Performance Capture Support**: For advanced setups, Take Recorder supports performance capture solutions like Motion Capture (MoCap) systems, which record high-quality character animations with external hardware.
* **Real-time Recording**: Depending on your hardware and setup, Take Recorder can operate in real-time, enabling immediate feedback on the recorded performance during gameplay.

## Prerequisites

* **Take Recorder** is a [Plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine) that must be enabled prior to use. From the main menu, go to **Edit > Plugins**, locate **Take Recorder**, and click the checkbox to enable it. This requires Unreal Engine to restart in order for the plugin to be enabled. This plugin is required for Take Recorder to work.
* To record animation from motion capture and other live performances, you can optionally enable **[Live Link](https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-in-unreal-engine)**. From the main menu, go to **Edit > Plugins**, locate **Live Link**, and click the checkbox to enable it. This requires Unreal Engine to restart in order for the plugin to be enabled.
* You also need a project with a playable character and actors to record. Alternatively, use a project created using the [Third Person Template](https://dev.epicgames.com/documentation/404) template.

## Opening Take Recorder

To start using **Take Recorder**, click **Window > Cinematics > Take Recorder** to open the Take Recorder panel. Take Recorder opens a new empty sequence if one is not open already.
The new sequence's time display is set to a timecode matching Take Recorder's time display.

## Interface Overview

There are four main sections of the **Take Recorder** user interface:

![Take Recorder UI](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f20dcb47-0048-48a4-8c2a-3021452491e2/take_recorder_ui.png)

1. **[Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#toolbar)**: The **Take Recorder** toolbar contains several buttons and toggles which control Sequencer integration, takes browsing, option displays, and **[user/project settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#user/projectsettings)**.
2. **[Slate](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#slate)**: The Slate section shows information on the pending take and timecode. Specify the take name, take number, set a marker frame, adjust frames per second (fps), add a description about the take, and set recording speed. The **Start Recording** button is located here and initiates the recording of the take.
3. **[Sources](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#sources)**: The Sources section contains options to specify the sources to record into your sequence. Sources can be captured from any actor in the Level as well as Live Link sessions, other sequences, a microphone, or World states.
4. **[Details](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#details)**: The Details section contains user and project settings for **Take Recorder**, as well as settings for your sources.

### Toolbar

The **Take Recorder** toolbar contains buttons and toggles for controlling Sequencer integration, takes browsing, and option displays.

| Name | Icon | Description |
| --- | --- | --- |
| **Clear Pending Take** | Clear Pending Take | Revert the currently opened sequence to an empty pending sequence. Removes any sequences specified in the **Record to Sequence** button. |
| **Review Last Recording** | Review Last Recording | Open the most recent sequence that was recorded. Does not become clickable until after a recording has been created. |
| **Record to Sequence** | Record to Sequence | Open a dropdown menu from which you can specify another sequence to record your take into. Clear it by clicking the Clear Pending Take button. Record to sequence |
| **Takes Browser** | Takes Browser | Open a Content Browser window for navigating to your saved takes. When using the columns view mode, take-related metadata information is displayed. Take Browser |
| **Show / Hide Sequence** | Show / Hide Sequence | Show or hide the Level Sequence that is used for setting up this take. |
| **Settings** | Settings | Show or hide project and user settings in the Take Recorder's details area. |
| **Return** | Return | Return to the pending take sequence, when reviewing a previous take. This feature is accessible while reviewing a previous recording. |
| **Slate Info Lock** | Slate Info Lock | Lock or unlock the ability to modify a slate, when reviewing a previous take.This feature is accessible while reviewing a previous recording. |
| **Start New Recording** | Start New Recording | Start a new recording using the current selected take as a base. This feature is accessible while reviewing the last recording. |

### Slate

The **Slate** area displays information on the current pending take, the current time, and recording functions. Set custom names and numerical entries for your slate and take number by clicking the **Slate** or **Take** text fields and modifying the text. The same can be done by clicking the **\** field in the slate body.

**Take Recorder** isn't running when the panel is initially loaded. The current timecode shows the current time from the running timecode provider, which defaults to UE's timecode provider. See **Recording Clock Source** in the [Take Recorder](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#takerecorder) section for timecode options.

To start a new recording, click the red **Record button** in either the Take Recorder window or in Sequencer playback controls. Sequencer's record button starts recording any selected actor into the current sequence, and does not require the Take Recorder window to be open. Click the button again or press the Esc key to stop the recording and save the current take.

![Take Recorder buttons](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d49ab518-bb91-452e-8da1-b0be64b68630/record_buttons.png)

1. **Take Recorder** window record button.
2. **Sequencer** record button.

During a recording session, click the **Add Marked Frame** button to add custom markers to the current time of the recording.

![Customer markers](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92d8e25b-f9fc-4a5f-b9be-820cc09557b0/custom_markers.png)

Click the **Frames Per Second** (fps) menu for a dropdown list of different frame rates to select for your pending take.

![Frames Per Second (fps)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/da22fd14-d7b8-421a-b663-f55d9e69a2b6/fps.png)

Change the recording speed and overall time dilation of the engine by editing the **Record Speed** number. This is useful when recording to a populated sequence by making the animation play at a slower speed, ensuring you can observe and match the animation at a more comfortable pace.

![Record Speed](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/65729b9b-5b3f-448f-906e-2df5071b8e90/record_speed.png)

#### Warnings

**Take Recorder** provides warning information if you don't have a valid source to record from or if you try to name a take the same as a previously recorded take.

If you do not have a valid source to record from, the Record button is replaced with an invalid source icon. Ensure you have selected a recordable source before attempting any recordings.

![Invalid source](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6749bbe6-be57-41c1-bf87-f8adc4a22c50/invalid_source_icon.png)

If you try to use the same take number from a previous take, the **Take Recorder** warns you that a take with the same number already exists and tells you where the previous take is. If you click that warning, it automatically changes the take number to the next available take number.

### Sources

The **Source** section is where you specify recording sources. Sources are listed here and can be enabled or disabled from the recording.
When a source is enabled, the toggle icon is orange. When it is disabled, the toggle icon is gray.

![Enabled and disabled sources](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/73e38df2-5c6a-4146-bd34-8ff5062c12b4/sources.png)

1. Enabled source
2. Disabled source

Each source also has a color bar at the far right end in the **Source** panel. The color of each source corresponds to the recorded subsequence.

**Take Recorder** only records a source **if** the source has both: The source has a recorder **and** a corresponding track that Sequencer can play back.

For example, any track that can be keyframed can be recorded. If a property of an actor cannot be keyframed, it cannot be recorded.

To add a source, click **+Source** and choose from a list of available sources. You can choose from:

* **[Any Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#anyactor)** in the level
* **[Camera Cuts](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#cameracuts)**
* **[Level Sequences](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#levelsequences)**
* **[Live Link](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#livelink)**
* One or more **[microphones](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#microphones)**
* **[Nearby Spawned Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#nearbyspawnedactors)**
* A **[Player](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#player)** actor
* **[World](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#world)** / **[Level assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#levelvisibility)**

![Add Source](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d2b5ad77-78d0-4825-a455-3921eaadcd04/add_source.png)


Add a source to **Take Recorder** by dragging an actor from the **[Outliner](https://dev.epicgames.com/documentation/en-us/unreal-engine/outliner-in-unreal-engine)** into the **Source panel**.

| Source | Description |
| --- | --- |
| **Any Actor** | The **Take Recorder Source** records an actor from the World's properties. Records the properties of the actor and the components on the actor and safely handles new components being spawned and the actor being destroyed. Selecting **Any Actor** as a source creates an actor source with the following details.   * **Source Actor**: The actor being referenced in the world.   Record Type: Specify to record the actor as a **[Spawnable or Possessable](https://dev.epicgames.com/documentation/404)**.   + **Project Default**: Sets the record type to either possessable or spawnable depending on your project's default settings (default setting). See the value (true or false) in the Record to Possessable field in [Take Recorder settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#userandprojectsettings).   + **Possessable**: Overrides the Take Recorder settings and records the take assets as a possessable.   + **Spawnable**: Overrides the Take Recorder settings and records the take assets as a spawnable. * **Record Parent Hierarchy**: Whether or not to also include the parent hierarchy if this actor is attached to a parent.   + If this is **disabled** and you are recording to a **posessable actor**, then the resulting transforms are in local space, since this actor is still attached to the parent.   + If this is **disabled** and you are recording to a **spawnable actor**, then the resulting transforms are in global space since the actor is a spawned copy and not attached to anything. * **Reduce Keys**: When enabled, this executes a [Simplify](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#simplify) operation on all keyframes after recording finishes. * **Recorded Properties**: A list of default properties for this actor and Components that can be enabled or disabled. Disabling a property does not include it as a track when recording finishes. * **Include Animation Names**: An array where you specify Bone or [Curve](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curves-in-unreal-engine) names to include in the recording. If you fill this array with any entries, only those Bones or Curves are included. For example, if you specify "root", then only the root bone is recorded. * **Exclude Animation Names**: An array where you specify Bone or Curve names to exclude from recording.  Source for Any Actor panel |
| **Camera Cuts** | If **Camera Cuts** is added as a source, **Take Recorder** records all active cameras during the session. Any time the active camera is changed, a new camera actor and camera cut section is created. |
| **Level Sequence** | Selecting a **Level Sequence** as a source provides other sequences to be played during your recording session. Specify any number of sequences to play from the details area of this source. Playback of sequences only is supported during recording within gameplay or simulation sessions.   * **Level Sequences to Trigger**: Option to select one or more Level Sequences.  Source for Level Sequence |
| **Level Visibility** | The **Level Visibility** source records the visibility states of all Levels at the start of the recording. It does not record any level change, only the visible states. It does not record any changes during the recording session. |
| **Live Link** | **Live Link** connects to any currently active Live Link sessions. The Live Link session must be specified in the **Subject Name** details field. Select a live link session directly by navigating to **Add Source (+) > From Live Link**.   * **Reduce Keys**: when enabled, this executes a [Simplify](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine#simplify) operation on all keyframes after recording finishes. * **Subject Name**: Name of subject to record. * **Save Subject Settings**: Toggle to Save subject settings while using Live Link. If you want to retain preprocessor, translations, and interpolations settings with your Live Link actor, enable this option. * **Use Source Timecode**: Toggle to use the subject's timecode or the system time while recording.   + If this option is enabled, the Live Link subject's timecode is used even if it doesn't match UE's timecode.   + If this option is disabled, data is keyed on the LiveLink thread and not the game thread. A key is stamped for every sample that arrives using the engine's time. No timecode track is created, so the relationship between the source's timecode and the recorded level sequence is lost. * **Discard Samples Before Start**: If enabled, UE discards Live Link samples with a timecode that occurs before recordings if **[Start at Current Timecode](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#startatcurrenttimecode)** is enabled.  Source for Live Link |
| **Microphone Audio** | **Microphone Audio** permits your device's microphone to be recorded during the recording session. Upon completion, **Take Recorder** creates a sound file is created upon completion containing your recorded audio. The details area contains settings for audio recording, track name, and the recording directory.   * **Audio Gain**: Gain in decibels to apply to recorded audio. * **Replace Recorded Audio**: Replace existing recorded audio with any newly recorded audio. Enabled by default. * **Audio Input Device**: Current selected channel from the Details panel for this source. * **Audio Source Name**: Name of the audio source * **Audio Track Name**: Name of the recorded audio track * **Audio Asset Name**: Name of the audio asset. Supports any of the following format specifiers that are substituted when at recording time:   + **{day}**: Day of the timestamp for the start of the recording.   + **{month}**: Month of the timestamp for the start of the recording.   + **{year}**: Year of the timestamp for the start of the recording.   + **{hour}**: Hour of the timestamp for the start of the recording.   + **{minute}**: Minute of the timestamp for the start of the recording.   + **{second}**: Second of the timestamp for the start of the recording.   + **{take}**: Take number.   + **{slate}**: Slate string. * **Audio Sub Directory**: Name of the subdirectory audio is saved in. Leave this field empty to place in the same directory as the sequence base path. Supports any of the following format specifiers that are substituted at recording time:   + **{day}**: Day of the timestamp for the start of the recording.   + **{month}**: Month of the timestamp for the start of the recording.   + **{year}**: Year of the timestamp for the start of the recording.   + **{hour}**: Hour of the timestamp for the start of the recording.   + **{minute}**: Minute of the timestamp for the start of the recording.   + **{second}**: Second of the timestamp for the start of the recording.   + **{take}**: Take number.   + **{slate}**: Slate string.  Source for microphone audio |
| **Nearby Spawned actors** | The **Nearby Spawned Actors** source records all spawned actors located within a specified radius from the camera's location. The details panel includes options for defining the range and specifying filters. If you are using filters, then only the filtered actors are added to the take. Only actors that spawn during a gameplay session are added. Actors that have already spawned are not affected.   * **Spawn Proximity**: Proximity to the current camera that an actor must be spawned in order to be recorded as a spawnable. If Proximity is set to 0cm, all spawned actors are recorded. * **Filtered Spawned Actors**: Only recorded actors that are listed in the Filter Type list. Defaults to disabled. * **Filter Types**: Type filter to apply to spawned actors.  Source for nearby spawned actors |
| **Player** | The **Player** source records the Player's controlled actor. Using this source might be useful if your player is dynamically spawned and does not exist as an actor in the Level until gameplay starts. |
| **World** | If **World** is added as a source, everything in the Level is recorded (defaults to true). Particles that are created using **Spawn Emitter** functions are only captured when using this source. |

You can save your source list as a preset and reuse it later. To save your source list:

1. Click the **Presets button** next in the Source panel.
2. Select **Save As Preset**.
3. The **Save Take Preset** window appears and prompts you for the **Path** location (folder where this preset is saved) and the **Name** of the preset.
4. Click the **Save button** to save your preset.

![Save Source presets](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5e344de3-8f13-4361-bb01-e32eba469ef4/source_presets.png)
