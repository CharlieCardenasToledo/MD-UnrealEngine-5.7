# Cinematic Viewport

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-viewport-controls-in-unreal-engine

> Application Version: 5.7

In the Unreal Editor, you can change any **Level Viewport** to a specialized **Cinematic Viewport**. The Cinematic Viewport enables additional functionality, behavior, and display modes that can assist you with cinematic content creation. This guide gives an overview of how to enable the Cinematic Viewport and its features.

#### Prerequisites

* You have a project that is using Sequencer. You can use one of the provided [**Cinematic Samples**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine#cinematicsamples) if you don't already have one.
* **[Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine)** is currently open in your Level.

## Enabling the Cinematic Viewport

To enable the Cinematic Viewport mode, select the **Viewport Perspective** menu and enable **Cinematic Viewport**.

![enable cinematic viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3de0f659-1133-4074-bf0b-d0e845e1938a/enableviewport.png)

## Overview

Once the Cinematic Viewport is enabled and **Sequencer** is opened, your viewport should now be displaying new cinematic elements.

![cinematic viewport layout](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca8200f2-7d13-4910-8aca-344338be6cb5/overview.png)

1. [**Film Overlays**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-viewport-controls-in-unreal-engine#filmoverlays)
2. [**Playback Preview and Controls**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-viewport-controls-in-unreal-engine#playbackpreviewandcontrols)

### Film Overlays

The **Film Overlays** menu contains visual guides for the viewport that you can enable to assist with your framing and composition. There are two main categories of overlays, **Composition** and **Frame** overlays.

![film overlays menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/74f6fd98-9c57-480f-9d71-17da1214004d/overlaysmenu.png)

#### Composition Overlays

| Name | Description |
| --- | --- |
| **Disabled** | The default view mode, which does not display any overlay. |
| **Grid (3x3)** | Displays a 3x3 grid on the viewport, allowing for framing based on **[Rule of Thirds](https://en.wikipedia.org/wiki/Rule_of_thirds)**. 3x3 grid |
| **Grid (2x2)** | Displays a 2x2 grid on the viewport. 2x2 grid |
| **Crosshair** | Displays a central reticle, useful for emulating photography reticles. crosshair reticle |
| **Rabatment** | Displays a rabatment overlay on the viewport, allowing for framing based on **[Rabatment of the Rectangle](https://en.wikipedia.org/wiki/Rabatment_of_the_rectangle)**. rabatment |

Composition overlay lines can also be tinted to any color or alpha value you want. Clicking the color bar next to **Tint** will open the **Color Picker** where you can select the color and transparency of the lines.

![composition lines color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c9949b05-79d0-4eea-8392-69603e245193/comptinting.gif)
