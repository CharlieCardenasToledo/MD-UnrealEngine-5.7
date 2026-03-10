# Animation Mode

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine

> Application Version: 5.7

**Animation Mode** is a [Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-modes-in-unreal-engine) in Unreal Engine that exposes new tools, panels, and editor behaviors that assist your animation workflows. Using this Mode when animating with Control Rig offers a more animation-focused editor experience, with tabs to aid in selecting Controls, transform displays, and launching tools.

This document provides an overview of Animation Mode, including its user interface, tools, and settings.

#### Prerequisites

* You have created a **Control Rig Asset**. See the [Control Rig Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-create-control-rigs-in-unreal-engine) page for information on how to do this.
* Animation Mode is mainly dependent on using Control Rig within Sequencer, therefore a [basic knowledge](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine) of Sequencer is required.

## Enabling Animation Mode

Animation Mode can be enabled in the following ways:

1. Dragging a Control Rig Asset from the [Content Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-in-unreal-engine) into a Level. This will create a new [Level Sequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine), add the character with a **Control Rig Track**, and enable Animation Mode.

   ![enable animation mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/841ca2b8-399d-4e89-92f7-756ab30dcd49/enable1.gif)
2. Selecting a Control Rig Track in Sequencer.

   ![enable animation mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a6d1615c-839d-48dd-baa9-f42c67a862c8/enable2.gif)
3. Manually enabling Animation Mode by clicking the **Mode** dropdown menu and selecting **Animation**. Alternatively, you can also press **Shift + 7**.

   ![enable animation mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ccbbd586-6388-4f63-bae8-24e49dcc9de6/enable3.png)

Animation Mode can be disabled and normal level editing mode restored either by selecting the **Mode** dropdown menu and clicking **Select**, or by pressing **Shift + 1**.

![disable animation mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/89a58254-93ff-4ee2-a0dc-4b5ec8041a73/disable.png)

## Animation Mode Overview

Animation Mode is a level editor [Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-modes-in-unreal-engine) which contains specialized editing interfaces and workflows. Activating it will add the following panels to the Unreal Editor interface:

![animation mode user interface](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/309509a8-557c-4734-9e80-c54c715fc5e0/modeoverview.png)
