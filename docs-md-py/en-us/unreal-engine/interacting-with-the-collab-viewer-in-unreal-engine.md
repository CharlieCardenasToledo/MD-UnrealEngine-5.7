# Interacting with the Collab Viewer

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/interacting-with-the-collab-viewer-in-unreal-engine

> Application Version: 5.7

This page describes the different ways you can control the camera and interact with content at runtime in the Collab Viewer Templates, in both [desktop](https://dev.epicgames.com/documentation/en-us/unreal-engine/interacting-with-the-collab-viewer-in-unreal-engine#desktopcontrols) and [VR](https://dev.epicgames.com/documentation/en-us/unreal-engine/interacting-with-the-collab-viewer-in-unreal-engine#vrcontrols) modes.

## Desktop Controls

### Toolbar

You can use the toolbars at the top of the window to teleport, switch navigation modes, and save the current session.

| Icon | Description |
| --- | --- |
| Voice Over IP | Voice Over IP is enabled by default in the project. Toggle it on or off by clicking this icon. |
| Activate Fly mode | Activates Fly mode. In Fly mode, you can fly freely around the scene in all directions. In this mode, you pass through all geometry regardless of collision settings on the Actors. See [Fly Mode Controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/interacting-with-the-collab-viewer-in-unreal-engine#flymodecontrols).  Returning to Walk mode after being in Fly mode re-enables gravity. Depending on your location, you will either free-fall until you reach the ground, or you will snap to the closest ground surface. |
| Activate Walk mode | Activates Walk mode. In Walk mode, you're held down to the ground by gravity. As you walk around the scene, you collide with any objects in the Level that are set up with collision volumes. See [Walk Mode Controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/interacting-with-the-collab-viewer-in-unreal-engine#walkmodecontrols). |
| Activate Orbit mode | Activates Orbit mode. In Orbit mode, you select a point of interest in the Level. Then, as you rotate the camera, you move around that point of interest, keeping it in the center of the screen. See [Orbit Mode Controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/interacting-with-the-collab-viewer-in-unreal-engine#orbitmodecontrols). |
| Activate VR mode | Activates VR mode, if you have a supported VR headset installed and working. See [VR controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/interacting-with-the-collab-viewer-in-unreal-engine#vrcontrols). |
| Save | Saves the current state of the viewer, including annotations and measurements. See [Saving and Loading a Session](https://dev.epicgames.com/documentation/en-us/unreal-engine/saving-and-loading-a-session-in-unreal-engine) |

Switch between modes quickly with the following hotkeys:

* Activate Fly mode by pressing **U** on your keyboard.
* Activate Walk mode by pressing **I** on your keyboard.
* Activate Orbit mode by pressing **O** on your keyboard.
* Activate VR mode by pressing **P** on your keyboard.

### Common Desktop Controls

The following controls work the same way in all desktop movement modes: Fly mode, Walk mode, and Orbit mode.

| To... | Do... |
| --- | --- |
| Activate the laser pointer | Move the mouse cursor to the object you want to highlight, then left-click. |
| Open the Interaction Menu | Press **Spacebar**. For details on using the items in this menu, see [The Interaction Menu](https://dev.epicgames.com/documentation/en-us/unreal-engine/interacting-with-the-collab-viewer-in-unreal-engine#theinteractionmenu). |
| Move to a preset bookmark location | Press any number key from 0-9 that has been mapped to a specific bookmark location. See [Working with Bookmarks in the Collab Viewer Template](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-bookmark-in-the-collab-viewer-template-in-unreal-engine). |
| Exit the application | Press **Esc**. |

### Fly Mode Controls

In addition to the [Common Desktop Controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/interacting-with-the-collab-viewer-in-unreal-engine#commondesktopcontrols), the following controls work in Fly mode.

| To... | Do... |
| --- | --- |
| Look around the world from your current position | Right-click and drag. |
| Move forward, to the left, backward, or to the right from your current position | Hold the right mouse button and press **W**, **A**, **S** and **D**. |
| Move straight up or down (along the world's global Z axis) | Hold the right mouse button and press **Q** and **E**. |

### Walk Mode Controls

In addition to the [Common Desktop Controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/interacting-with-the-collab-viewer-in-unreal-engine#commondesktopcontrols), the following controls work in Walk mode.

| To... | Do... |
| --- | --- |
| Look around the world from your current position | Right-click and drag. |
| Move forward, to the left, backward, or to the right from your current position | Hold the right mouse button and press **W**, **A**, **S** and **D**. |

### Orbit Mode Controls

In addition to the [Common Desktop Controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/interacting-with-the-collab-viewer-in-unreal-engine#commondesktopcontrols), the following controls work in Orbit mode.

| To... | Do... |
| --- | --- |
| Orbit the camera around the point of interest | Right-click and drag. |
| Change the camera's point of interest to a new location, remaining at the current zoom level | Middle-click. |
| Choose a new point of interest, and zoom to fit the selected object in the viewport | Double middle-click. |
| Zoom in or out on the current point of interest | Turn the mouse wheel. |
| Pan the camera left, right, up, or down | Middle-click and drag. |

## VR Controls

| To... | Do... |
| --- | --- |
| Teleport to a new location | * **Oculus Touch:** Press and hold the B button on the right controller or the Y button on the left. * **Valve Index Controller:** Press and hold the B button on either controller. * **HTC Vive Controller:** Press and hold the Grip button on either controller.   You'll see an arc emitted from your controller, and a target marker superimposed on the ground. The target marker represents your Teleport location. Move your controller in real world space to place the marker as close as possible to the place you want to move.  The pointer of the marker represents your facing direction after the teleport. You can control this facing direction by rotating your wrist. Release the button you're holding to complete the teleport. |
| Activate the laser pointer | Press the main trigger button on either controller, and move the controller around in real world space. |
| Open the Interaction Menu | Push the right-hand controller thumbstick forward or back. Use the thumbstick to highlight the option you want to activate, then press the thumbstick button to confirm your choice. For details on using the items in this menu, see [The Interaction Menu](https://dev.epicgames.com/documentation/en-us/unreal-engine/interacting-with-the-collab-viewer-in-unreal-engine#theinteractionmenu). |
| Exit the application | Press **Esc** on your computer keyboard. |

## The Interaction Menu

The Interaction Menu offers you several commands and modes for interacting with the content in your scene at runtime.

![The Interaction Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d3c766c6-cc70-4123-839f-7074425fbe96/collabviewer-server-interactionmenu.png "The Interaction Menu")
