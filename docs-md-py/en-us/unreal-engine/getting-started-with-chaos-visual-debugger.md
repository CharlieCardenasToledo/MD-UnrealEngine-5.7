# Getting Started with Chaos Visual Debugger

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger

> Application Version: 5.7

**[Chaos Visual Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine)** (**CVD**) is a tool that you can use to record physics simulations. With CVD, you can record games and applications running on your machine, as well as from a remote machine, or a platform that’s connected to your machine.

![Image](https://dev.epicgames.com/community/api/documentation/image/af6324d6-5713-470d-bd20-c64224b35cd6)

By playing back recordings in CVD, you can inspect data for debugging. These recordings are project independent, meaning they can be loaded even without access to Unreal Engine (UE) project files, enabling cross-team collaboration or remote debugging.

The data that CVD records includes:

- **Particles** (including velocities, accelerations, mass properties, and object states)
- **Collision geometry** (including collision channels)
- **Collision constraints** (contact pairs with their state)
- **Joint constraints** (state and joint settings)
- **Character ground constraints** (physics-based character movement)
- **Scene queries** (including line traces, sweeps, and overlaps)
- **Rigid body animation nodes** (RBAN)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "In the context of CVD, <b>particles </b>usually refer to rigid bodies.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

## Launch Chaos Visual Debugger

There are two ways to launch CVD; [from the Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#inside-the-unreal-editor) or [as a standalone program](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#as-a-standalone-program).

### Inside the Unreal Editor

To open the Chaos Visual Debugger from the Unreal Editor, in the menu bar, click **Tools > Debug > Chaos Visual Debugger**. After selecting CVD, the tool will open in a new window.

![Launch From The Editor](https://dev.epicgames.com/community/api/documentation/image/81ea3fed-2bd6-4f3b-b294-b1e7e10d4d52)

### As a Standalone Program

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "To run CVD as a standalone program, you must use a source-code build of Unreal Engine. You can download a source-code build from <a href=\"https://www.unrealengine.com/en-US/ue-on-github\">GitHub</a>. To learn more, see <a data-document-id=\"3228638\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source\">Building Unreal Engine from Source</a>.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

You can build and run the CVD as a standalone program from either an executable (not portable) or batch file (portable). The table below describes the file location and build steps for each option.

| Build Flow | Description |
| --- | --- |
| **CVD Executable** | The executable is located in the following file path: `Engine\Binaries\Win64\ChaosVisualDebugger.exe` To build and run CVD, follow these steps: From your IDE of choice (such as Visual Studio), open the CVD executable. Build and run the executable. |
| **CVD Batch File** | The batch file located at the following path: `Engine\Programs\ChaosVisualDebugger\BuildAndCook.bat` To build and run CVD, follow these steps: Build the Editor. Run the batch file to build, cook, and package CVD. Access the output build from `Engine\Programs\ChaosVisualDebugger\PackagedBuild` and run it. |

## Explore the CVD User Interface

This section describes the most common buttons, panels, and toolbars you will interact with in the Chaos Visual Debugger. While some of these elements are similar to the Unreal Editor interface, you should familiarize yourself with CVD due to visual differences between CVD and some Unreal Editor versions.

The sections below describe where to find each user interface (UI) element and offer simple use cases. For a deeper dive, follow the links provided throughout this page.

![CVD Interface](https://dev.epicgames.com/community/api/documentation/image/1ae159a8-20f8-4710-bcd9-43a2c79f5dda)

| Number | Name | Overview |
| --- | --- | --- |
| 1 | **Menu Bar** | Options to load recent recordings and modify the CVD layout. |
| 2 | **Main Toolbar** | Options to start or stop recordings, load recordings, and customize which data to record. |
| 3 | **Viewport Toolbar** | Options to modify which data is displayed in the viewport and how it's visually differentiated. |
| 4 | **Scene Outliner** | Displays a list of scene components within a recording. |
| 5 | **Viewport** | Displays a loaded or live recording, like the Unreal Editor viewport. This can include: A level open in the Unreal Editor. A Play-In-Editor (PIE) session. Packaged builds running on your machine. An application running on a platform connected to your machine, such as a console. |
| 6 | **Playback Controls** | Displays a collection of playback timelines and logs including: [The Game Frames Timeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#game-frames-timeline) [The Solver Timeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#solver-timeline) [The Solver Stage Timeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#solver-stage-timeline) [The Recorded Output Log](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#recorded-output-log) [The Output Log](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#output-log) |
| 7 | **Details Panel** | Displays information for a selection made in the viewport that doesn't have a dedicated Data Inspector, such as particles. |
| 8 | **Data Inspectors** | Provides additional details for: [Collision data](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger#collision-data-inspector) [Scene queries](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger#scene-query-inspector) [Joint constraint data](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger#joint-constraint-data-inspector) [Particle data](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger#particle-data-details-panel) |

### Menu Bar

| Name | Description | Image |
| --- | --- | --- |
| **File** | Quick access to open recent recordings. | ![Menu Bar File](https://dev.epicgames.com/community/api/documentation/image/05640caa-0c0f-499d-9d2f-a49dca24096b) |
| **Window** | Show or hide parts of the CVD UI. | ![Menu Bar Window](https://dev.epicgames.com/community/api/documentation/image/eddafbd0-0758-474f-b701-be80d7c5d85d) |

### Main Toolbar

![Main Toolbar](https://dev.epicgames.com/community/api/documentation/image/4842107f-d4c1-430e-ae6d-ffea856c4aec)

| Number | Name | Description |
| --- | --- | --- |
| 1 | **Open File** | Loads existing `.utrace` recordings. |
| 2 | **Connect to Session** | (Legacy) Connects to a remote machine for remote debugging. |
| 3 | **Combine** | Combines multiple recordings that are open in CVD into one `.cvdmulti` file. |
| 4 | **Scene Query Browser** | Inspects all scene queries made for a single frame. For more information on this, see [Data Inspectors](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger). |
| 5 | **Session Targets** | Selects the target(s) to record. |
| 6 | **Loading Mode** | Loads single or multiple recordings (which merges data). |
| 7 | **Record to File** | Begins a recording and saves to file. |
| 8 | **Record Live Session** | Begins a recording and renders the visualization in real time. |
| 9 | **Data Channels** | Customizes the data captured during recording, such as: [Data flags](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger) [Simulation stages](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#solver-stage-timeline) |
| 10 | **Settings** | Customizes CVD’s UI and performance. |

### Viewport Toolbar

![Viewport Toolbar](https://dev.epicgames.com/community/api/documentation/image/b9f5e930-9f35-4ba2-80de-bd2d347f74fe)

1. [Hamburger Menu](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#hamburger-menu)
2. [View Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#view-mode)
3. [Lighting Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#lighting-mode)
4. [Show Button](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#show-button)
5. [Transform and Snapping Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#transform-and-snapping-toolbar)

#### Hamburger Menu

| Name | Description | Image |
| --- | --- | --- |
| **Play at Recorded Framerate** | Overrides the recorded frame rate to a fixed one. | ![Play At Recorded Framerate](https://dev.epicgames.com/community/api/documentation/image/94710bbe-f892-42e7-9236-94d9810c5651) |
| **Object Tracking (F8)** | Locks the camera to an object in the viewport. | ![Object Tracking](https://dev.epicgames.com/community/api/documentation/image/332730c6-919c-4aef-8595-aaf769e3920d) |
| **FOV Options** | Adjusts the viewport’s FOV (field of view) and furthest render distance. | ![FOV Options](https://dev.epicgames.com/community/api/documentation/image/a37d5186-1379-4a07-a37d-b4d0a87feac4) |
| **Allow Translucent Selection (T)** | Toggles the ability to click through translucent objects. | ![Allow Translucent Selection](https://dev.epicgames.com/community/api/documentation/image/63d399ac-9881-4f02-9c35-dd8562b4a137) |
| **Go to Location** | Teleports the camera to a location entered into this field, using an XYZ format. | ![Go To Location](https://dev.epicgames.com/community/api/documentation/image/0b7dabf8-f29e-4f7f-bca7-fb1554c36b28) |

#### View Mode

View mode switches between **Perspective**, **Top**, **Bottom**, **Left**, **Right**, **Front**, and **Back** views in the viewport.

| Perspective | Top | Left |
| --- | --- | --- |
| ![Perspective](https://dev.epicgames.com/community/api/documentation/image/e20328e0-fdff-4d28-b93e-ea4aaf49369c) | ![Top](https://dev.epicgames.com/community/api/documentation/image/2ab85134-6a5f-4ed9-9987-010c751d4e96) | ![Left](https://dev.epicgames.com/community/api/documentation/image/c3c47c0b-c1e5-49f4-a089-b100046ab6a4) |

#### Lighting Mode

Lighting mode switches between **Lit**, **Unlit**, **Lit** **Wireframe**, and **Wireframe** view modes in the viewport.

```json
{
  "type": "sequence_slider",
  "caption": "Lighting Modes",
  "images": [
    {
      "image_id": 25947724,
      "storage_key": "389d07f6-8083-4dbd-82eb-baa8de412163",
      "context": "documentation",
      "image": {
        "id": 25947724,
        "file_name": "lit-wireframe.png",
        "file_size": 705423,
        "content_type": "image/png",
        "created_at": "2025-08-18T14:51:27.799+00:00",
        "height": 716,
        "width": 1600,
        "storage_key": "389d07f6-8083-4dbd-82eb-baa8de412163",
        "context": "documentation"
      }
    },
    {
      "image_id": 25947725,
      "storage_key": "78bb80f5-b4d7-4a26-99ac-2b6460a2cf00",
      "context": "documentation",
      "image": {
        "id": 25947725,
        "file_name": "unlit.png",
        "file_size": 518634,
        "content_type": "image/png",
        "created_at": "2025-08-18T14:51:28.009+00:00",
        "height": 715,
        "width": 1600,
        "storage_key": "78bb80f5-b4d7-4a26-99ac-2b6460a2cf00",
        "context": "documentation"
      }
    },
    {
      "image_id": 25947726,
      "storage_key": "db7d7894-0b97-4a0d-be51-0982078970f6",
      "context": "documentation",
      "image": {
        "id": 25947726,
        "file_name": "lit.png",
        "file_size": 994552,
        "content_type": "image/png",
        "created_at": "2025-08-18T14:51:28.207+00:00",
        "height": 716,
        "width": 1600,
        "storage_key": "db7d7894-0b97-4a0d-be51-0982078970f6",
        "context": "documentation"
      }
    },
    {
      "image_id": 25947727,
      "storage_key": "17bf8af8-b661-405c-87b4-927abc9fdb2d",
      "context": "documentation",
      "image": {
        "id": 25947727,
        "file_name": "wireframe.png",
        "file_size": 908971,
        "content_type": "image/png",
        "created_at": "2025-08-18T14:51:28.473+00:00",
        "height": 715,
        "width": 1600,
        "storage_key": "17bf8af8-b661-405c-87b4-927abc9fdb2d",
        "context": "documentation"
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For better visibility when using Unlit mode, enable <b>Mesh Edges</b>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25947701,
      "caption": "",
      "alt_text": "Mesh Edges",
      "image": {
        "id": 25947701,
        "file_name": "mesh-edges.png",
        "file_size": 86004,
        "content_type": "image/png",
        "created_at": "2025-08-18T14:51:25.955+00:00",
        "height": 465,
        "width": 1057,
        "storage_key": "209f074f-5a5c-4fda-be6f-8af100778536",
        "context": "documentation"
      },
      "storage_key": "209f074f-5a5c-4fda-be6f-8af100778536",
      "context": "documentation",
      "width": 600,
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

#### Show Button

The **Show** button modifies which visualization flags and debug text are visible in the viewport for an existing recording. For more information about data flags, see [Data Visualization Flags](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger).

![Show Button](https://dev.epicgames.com/community/api/documentation/image/576635ca-fe9e-4c28-92bc-50d2e2a2351a)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Settings in this menu persist between CVD sessions unless reset to default.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

#### Transform and Snapping Toolbar

The transform and snapping toolbar is similar to the legacy viewport toolbar in previous versions of the Unreal Editor. Most often, you’ll use these tools to manipulate light actors.

| Icon | Name | Description |
| --- | --- | --- |
| ![Icon Select](https://dev.epicgames.com/community/api/documentation/image/1a59c3c9-128c-45d6-ad60-cfb05f89086c) | **Select Objects** | Selects objects within the viewport. |
| ![Translate Object](https://dev.epicgames.com/community/api/documentation/image/ea14cd04-6cde-457f-b08a-2208433f7fcf) | **Select and Translate Objects** | Moves light actors around the world along individual axes, dual axes, or on all three axes. |
| ![Rotate Object](https://dev.epicgames.com/community/api/documentation/image/6f17c4d9-7eed-49ff-be60-95b29667ca27) | **Select and Rotate Objects** | Rotates light actors along individual axes. |
| ![Scale Object](https://dev.epicgames.com/community/api/documentation/image/1c688e3c-43f7-4ddc-9970-bb6562a1484f) | **Select and Scale Objects** | Scales light actors using the scale gizmo. Use the gizmo to scale objects along individual axes, dual axes, or uniformly on all three axes. |
| ![Coordinate System](https://dev.epicgames.com/community/api/documentation/image/9b78b1ec-6a8c-4257-88fe-e962b14395e4) | **Coordinate System** | Cycles the coordinate system between **World** and **Local**. |
| ![Snap To Surface](https://dev.epicgames.com/community/api/documentation/image/cc7cb5fc-842c-4aa7-af6d-cee17bb74930) | **Snap to Surface** | Sets the snapping behavior of light actors when you drag them along another object’s surface. |
| ![Snap To Grid](https://dev.epicgames.com/community/api/documentation/image/27ef1988-e41f-448d-80fd-c3676b21a767) | **Snap to Grid** | Toggles whether light actors snap to the grid and sets the increment. |
| ![Rotation Increments](https://dev.epicgames.com/community/api/documentation/image/1d4fda57-1f38-410b-81b8-57b80ea2e894) | **Rotation Increments** | Toggles whether light actors rotate in increments and sets the degree. |
| ![Scaling Increments](https://dev.epicgames.com/community/api/documentation/image/0cf8a82e-eb16-43e4-8199-5b4a4daa7f94) | **Scaling Increments** | Toggles whether light actors scale in increments and sets the increment. |
| ![Camera Speed](https://dev.epicgames.com/community/api/documentation/image/4f813627-bc75-4a1e-896e-79334fa70a5e) | **Camera Speed** | Affects the speed at which the camera can move around the world. |

### Scene Outliner

The **Scene Outliner** displays a list of scene components within a recording. Since each recording can contain multiple solvers, each solver's particles are put under a folder with the name and ID of the solver they belong to. Within that folder, each particle is labeled with its Chaos-side debug name.

![Scene Outliner](https://dev.epicgames.com/community/api/documentation/image/60b8a755-553a-4289-bc69-23850e1dd93a)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "In CVD, a <b>physics solver</b> is an instance of a physics simulation (usually from a game world), handled by the <a data-document-id=\"3229583\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-in-unreal-engine\">Chaos Physics Engine</a>.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

### Playback Controls

The Chaos Visual Debugger includes controls to play and rewind existing recordings based on [game-thread](https://dev.epicgames.com/documentation/en-us/unreal-engine/threaded-rendering-in-unreal-engine) frames, physics-solver frames, or stages of a simulation. This maximizes the degree to which you can inspect situations that use [networked physics](https://dev.epicgames.com/documentation/en-us/unreal-engine/networked-physics-overview), asynchronous physics, or multiple game worlds (such as multiplayer games).

#### Game Frames Timeline

The **Game Frames Timeline** represents each game-thread frame for a recording.

![Game Frames Timeline](https://dev.epicgames.com/community/api/documentation/image/ddee7ff6-5026-4413-85ba-92c8dd140cb5)

When you playback a recording using this timeline, you’ll notice that the Solver Timeline also plays. This is because for each **game-thread** frame that plays, CVD searches for the closest **physics-solver** frame available at that timestamp.

[Video: V_dVNdNq](https://dev.epicgames.com/community/api/cms/videos/V_dVNdNq/embed.html)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The frame numbers of the Game Frames Timeline may not always match the Solver Timeline. This is because game-thread frames can correspond to multiple physics-solver frames. Access to both timelines means you can inspect situations where this occurs, such as when using Async Physics. ",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25947715,
      "caption": "(1) Solver Timeline (2) Game Frames Timeline",
      "alt_text": "Game Frame and Solver Timelines",
      "image": {
        "id": 25947715,
        "file_name": "gameframe-callout.png",
        "file_size": 17055,
        "content_type": "image/png",
        "created_at": "2025-08-18T14:51:26.993+00:00",
        "height": 243,
        "width": 700,
        "storage_key": "341d2b5d-3e0b-47eb-820a-94b48108ce83",
        "context": "documentation"
      },
      "storage_key": "341d2b5d-3e0b-47eb-820a-94b48108ce83",
      "context": "documentation",
      "width": 600,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "For an in-depth explanation of how CVD visualizes Sync and Async Physics, data from multiple game worlds, and resimulated frames, see <a href=\"https://youtu.be/_DKKztvMd2o?t=1007\">Debugging Chaos Physics in Unreal Engine at the 16:05</a> minute mark.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

#### Solver Timeline

The **Solver Timeline** represents each physics-solver frame for a recording. Each solver gets a dedicated track. Using this timeline, you can playback data for any solver track and see which solver frame corresponds to a specific game-thread frame.

![Solver Timeline](https://dev.epicgames.com/community/api/documentation/image/4b04d15d-e462-4ab1-ae8e-fd49a63d8188)

| Setting | Description | Image |
| --- | --- | --- |
| **Timeline Sync Mode** | Controls how each solver track is synced. **Recorded Timestamp (Default):** Syncs all solver tracks based on which time they were recorded, regardless of networked physics time offsets. **Network Tick:** Visualizes each solver track as if the client-side prediction logic works correctly. This can help you pinpoint any divergences that indicate a client and server desync. **Manual:** Fully disables automatic track syncs. | ![Network Tick](https://dev.epicgames.com/community/api/documentation/image/4cb6503a-273b-4e5e-ae39-b3b02549738d) |
| **Re-Simulation Badge** | Appears on any solver track that includes frames that are part of a re-simulation done during the network desync correction process. | ![ReSim Badge](https://dev.epicgames.com/community/api/documentation/image/4ac59488-8b0a-427f-9a0c-3b3152129bf9) |
| **Visibility Control** | Shows or hides visualized data from a particular solver track. | ![Visibility Control](https://dev.epicgames.com/community/api/documentation/image/e0db75a7-0008-482d-9662-c741347bbd4d) |

#### Solver Stage Timeline

With the **Solver Stage Timeline**, you can jump to a specific **stage** of a physics simulation. **Stages** are snapshots of a simulation taken at different points within a single physics frame.

![Solver Stage Timeline](https://dev.epicgames.com/community/api/documentation/image/6618e055-0423-4c5f-a064-952fd4690d7b)

You can visualize the following stages, using a particle simulation as an example:

| Stage | Description |
| --- | --- |
| **Evolution Start** | Takes a snapshot of all particles at the beginning of the solver step. |
| **Post-Integrate** | Takes a snapshot of all particles after performing the `Integrate` calculation on them. |
| **Collision Detection Broad Phase** | Takes a snapshot of all mid phases (an object is created for every particle pair whose bounds overlap) after running the Broad Phase of the collision detection process. |
| **Collision Detection Narrow Phase** | Takes a snapshot of all mid phases after running the Narrow Phase of the collision detection process. |
| **Pre Constraint Solve** | Takes a snapshot of all particles before solving the available constraints. |
| **Post Constraint Solve** | Takes a snapshot of all particles after solving the constraints. |
| **Evolution End** | Takes a snapshot of all particles at the end of the solver step. |

The Solver Stage Timeline is useful for inspecting unusual behavior within singular frames, such as when an object appears in the correct location at the beginning of a frame but in an unexpected location at the end of a frame.

#### Recorded Output Log

Located next to the Solver Timeline Tracks tab, the **Recorded Output Log** tab is where CVD records the log stream of your application for retroactive inspection.

![Recorded Output Log](https://dev.epicgames.com/community/api/documentation/image/115f02ea-7c13-407d-a2c8-8f59f547a339)

#### Output Log

The **Output Log** is a real-time log to monitor activity. This tab shows the active log for the current CVD instance and displays errors or warnings for CVD itself.

![Output Log](https://dev.epicgames.com/community/api/documentation/image/bf1ab71b-21fc-4286-9a9c-9544a9743552)

## Details Panel

The **Details** panel displays information for a selection made in the viewport.

![Details Panel](https://dev.epicgames.com/community/api/documentation/image/20ccfa17-2c80-45c4-87b7-e2d20b113d34)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The Details panel also acts as the Data Inspector for particle data. For more information, see <a data-anchor-id=\"18633\" data-document-id=\"4509808\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger#particle-data-details-panel\">Particle Data (Details Panel)</a>.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

## Next Up

- [Related Document](en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger.md)

- [Related Document](en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger.md)

- [Related Document](en-us/unreal-engine/capturing-data-with-chaos-visual-debugger.md)
