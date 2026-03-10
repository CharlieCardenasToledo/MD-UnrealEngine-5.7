# Blueprint Editor Toolbar

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/toolbar-in-the-blueprints-visual-scripting-editor-for-unreal-engine

> Application Version: 5.7

The **Toolbar** is displayed at the top-left of the Blueprint Editor by default. The Blueprint Editor Toolbar buttons provide easy access to common commands needed when editing Blueprints. The Toolbar provides different buttons depending on which mode is active and which Blueprint type you are currently editing.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1eb2fd31-cd4e-490e-a505-f2841a144e32/toolbarbp.png)

The Toolbar contains two sections:

* **Toolbar options** - Tools for working with your Blueprint.
* **Mode buttons** - Buttons that you can use to switch which mode your Blueprint is in.

## Toolbar Buttons

  

| Button | Description |
| --- | --- |
| Compile Successful Button | Compilation was successful. Clicking the button compiles the Blueprint being edited. Output from the compiling process is displayed in the Blueprint Log of the Message Log. This button will be inactive during debugging. |
| Compile Needed Button | The *Blueprint* needs to be recompiled. Clicking the button compiles the Blueprint being edited. Output from the compiling process is displayed in the Blueprint Log of the Message Log. This button will be inactive during debugging. |
| Compile Warning Button | There was a warning during compilation. Clicking the button compiles the Blueprint being edited. Output from the compiling process is displayed in the Blueprint Log of the Message Log. This button will be inactive during debugging. |
| Compile Failed Button | Compilation failed. Clicking the button compiles the Blueprint being edited. Output from the compiling process is displayed in the Blueprint Log of the Message Log. This button will be inactive during debugging. |
| Save Button | Saves the current Blueprint. |
| Find in Content Browser Button | Summons the **Content Browser** and navigates to this asset. |
| Search Button | Finds references to functions, events, variables, and pins in the current Blueprint. |
| Blueprint Properties Button | Opens the Blueprint Properties in the **Details** pane. |
| Blueprint Properties Button | Shows the Class Defaults Panel in the Details Tab |
| Simulate Button | Starts the game in simulation mode. See the [Simulate In Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine#simulateineditor) section for more information. |
| Play In Editor Button | Starts the game in normal play mode. Clicking the arrow displays the **Play Options** menu. See the [Play In Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine#playineditor) section for more information. |
| Pause Button | Pauses simulation. When the simulation is paused, the **Resume** and **Frame Skip** buttons will appear on the toolbar. |
| Resume Button | Resumes execution after a breakpoint is hit or the Pause button is pressed. |
| Frame Skip Button | Advances a single frame, or tick. This button appears when simulation is paused, or when a breakpoint is hit. |
| Stop Button | Halts execution of the game and exits Simulate In Editor mode. |
| Possess Button | Switches from Simulate In Editor mode to Play In Editor mode. Attaches to the player controller, allowing normal gameplay controls. Toggles with **Eject**. |
| Eject Button | Switches from Play In Editor mode to Simulate In Editor mode. Detaches from the player controller, allowing regular editor controls. Toggles with **Possess**. |
| Step Button | Steps through execution of the graph one node at a time. This button appears during simulation after a breakpoint is hit. |
| Debug Dropdown | If you have one or more instances of a *Blueprint* in a level, this dropdown allows you to select which instance to debug. |
