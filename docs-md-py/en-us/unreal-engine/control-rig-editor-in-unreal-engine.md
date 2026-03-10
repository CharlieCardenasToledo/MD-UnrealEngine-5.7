# Control Rig Editor

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-editor-in-unreal-engine

> Application Version: 5.7

This page outlines the user interface, tools, and features contained within the Control Rig Editor.

![control rig editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cfebc692-17b7-48f7-bde5-1fbabe91be9d/editoroverview.png)

1. [**Toolbar**](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-editor-in-unreal-engine#toolbar)
2. [**Viewport**](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-editor-in-unreal-engine#viewport)
3. [**Rig Hierarchy**](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-editor-in-unreal-engine#righierarchy)
4. [**Rig Graph**](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-editor-in-unreal-engine#riggraph)
5. [**Details**](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-editor-in-unreal-engine#details)

## Toolbar

![control rig toolbar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c01eb5a2-071f-4fbc-b2ab-aa433f0e859b/toolbar.png)

The **Control Rig** toolbar contains buttons and settings for previewing behavior and Control Rig construction. The buttons with specific Control Rig functionality are as follows:

| Name | Image | Description |
| --- | --- | --- |
| **Compile** | control rig compile | Similar to **[Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine)**, Control Rigs must be **compiled** in order to fully save and begin executing their logic. Clicking this button will compile your rig, as well as visually provide feedback on whether or not your rig needs to be compiled.  You are required to compile whenever changes are made within the Rig Hierarchy. This can include adding, removing, reparenting, or renaming Controls, Bones or spaces. Recompiling is also required when creating variables.  The Compile button also resets your controls after you manipulate them in the viewport. |
| **Solve Direction** | toolbar forwards solve | The Solve Direction button switches between different Solver event chains. Use this to preview different [Solve Directions](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-forwards-solve-and-backwards-solve-in-unreal-engine). Each option is associated with a Rig Graph solve direction event node. Selecting an option will begin previewing that solve chain. solve direction menu  Clicking the main button will swap the mode between the current mode and the previously selected mode. |
| **Auto Compile** | toolbar auto compile | Enable **Auto Compile** to set compiling to automatically occur when you make changes in the Rig Graph. This includes actions like creating and linking nodes. All other changes mentioned above will still require you to manually compile. |
| **Debug Object** | control rig editor preview | This drop-down menu links the Control Rig viewport to an active Control Rig in a simulating or playing session. This previews the current Control Rig animation from that session in the Control Rig viewport. |
| **Class Settings** | toolbar class settings | The Class Settings button toggles Blueprint class settings to be visible in the [Details](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-editor-in-unreal-engine#details) panel. The **Shape Libraries** property is located here, which can be used to change the control shapes available to you when rigging. Visit the [Control Shapes and Control Shape Library](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-shapes-and-control-shape-library-in-unreal-engine) page to learn more about this feature. shape library You can also access Control Rig Python commands such as [Python Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-python-scripting-in-unreal-engine#pythoncontext) and [Copy Python Script](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-python-scripting-in-unreal-engine#copypythonscript). |

## Viewport

From the Viewport, you can:

* Preview interaction with your Control Rig nodes.
* Set different display modes and debug displays.
* Select and manipulate controls.
* Change the preview mode using the top toolbar.

![control rig viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/405cf608-ca63-4e91-892f-9fba896030e5/viewport.png)
