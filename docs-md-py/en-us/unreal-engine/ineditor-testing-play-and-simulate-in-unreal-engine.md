# In-Editor Testing (Play and Simulate)

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "include",
  "excerpt_id": 2708,
  "excerpt_assignment_id": 2590,
  "blocks": [
    {
      "type": "paragraph",
      "content": "Unreal Editor allows you to spawn a player anywhere and instantly preview your game from within the editor without waiting for files to save. There are two preview types available: <strong>Play In Editor</strong> (PIE) which is directly accessed via the <strong>Play</strong> button located on the Main Toolbar\nand <strong>Simulate In Editor</strong> (SIE) which is accessed via the <strong>Play</strong> dropdown menu (<strong>Alt+S</strong>). The in-editor preview system supports toggling between Play In Editor and Simulate In Editor sessions, so that you can quickly iterate on gameplay and asset tweaks\nand see how your game changes as a result.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "QMmj",
  "settings": {
    "is_hidden": false
  }
}
```

When you launch a game preview session, the editor quickly creates a duplicate copy of your level. Changes can be saved back to the editor copy of the level using Keep Simulation Changes.
This duplication of the level keeps the editor's copy of the world safely immutable.

Game previewing includes level streaming, and the **Outliner** will update accordingly so that you can select and edit Actors that are streamed in as a result of gameplay.
Any Actors you have selected when you begin testing your game with a Play In Editor or Simulate In Editor session will remain selected. The reverse is also true, so any Actors selected
during in-editor testing will remain selected after you end the testing session. This means that the **Details** panel will show the properties for an Actor you select because you want to change its
appearance or behavior, even if you begin gameplay in a distant section of the level.

## Toolbar

You can begin a Simulate In Editor or Play In Editor session from either the **Level Editor** or the **Blueprint Editor**, using the appropriate Toolbar buttons or dropdown menus.

From the **Level Editor**, you can click the **Play** button.

![Toolbar Buttons](https://dev.epicgames.com/community/api/documentation/image/4ca96da1-99eb-405a-a3f8-65dae5181685)

_Click image for full size._

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "This will start a Play In Editor (PIE) session, so that gameplay can be tested directly from the editor.  Different modes and options for Play In Editor sessions can be selected in the dropdown menu, and the Play In button will use the same settings that were selected for the previous session.",
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

Click the **Play** dropdown button to display the **Play Options** dropdown menu.

![Play Menu](https://dev.epicgames.com/community/api/documentation/image/1e2df8c6-3d9b-4d91-a90b-875d99f98f3d)

_Click image for full size._

You can change your [Play In Editor mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine#modes), set basic [networked Play In Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/play-in-editor-multiplayer-options-in-unreal-engine) options, or open the [full Play In Editor settings window](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-settings-in-unreal-engine). Clicking on **Simulate** begins Simulate In Editor mode, which changes the testing section of the Toolbar. While simulating, you can pause or stop gameplay, as well as swap to a Play In Editor session with the **Possess** button.

![Simulate In Editor Toolbar](https://dev.epicgames.com/community/api/documentation/image/7b2beacf-a541-4592-824c-e7d600686d35)

_Click image for full size._

## Play In Editor

Clicking on the **Play** button in the toolbar (**Alt + P**) or selecting **Play From Here** in the **Viewport** context menu begins a Play In Editor session.
Play In Editor allows you to play the current level directly from the editor, so that you can test gameplay functionality, including player controls and level events triggered by players' actions.

### Modes

Launching a game preview with a different mode will change the default Play mode that is activated by the **Play** button.

#### Display Types

$ Viewport : Gameplay will be shown in the active Level Editor viewport.

**Click to see full-size image:**

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "image",
        "image_id": 26335650,
        "caption": "",
        "alt_text": "",
        "image": {
          "id": 26335650,
          "file_name": "PIEViewport_Windows.png",
          "file_size": 1419042,
          "content_type": "image/png",
          "created_at": "2025-12-09T19:32:23.090+00:00",
          "height": 1080,
          "width": 1920,
          "storage_key": "80b76fd5-2296-494f-8602-e1b6a8b70c1c",
          "context": "documentation"
        },
        "storage_key": "80b76fd5-2296-494f-8602-e1b6a8b70c1c",
        "context": "documentation",
        "width": 500,
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "image",
        "image_id": 26335651,
        "caption": "",
        "alt_text": "",
        "image": {
          "id": 26335651,
          "file_name": "PIEViewport_Mac.png",
          "file_size": 1608169,
          "content_type": "image/png",
          "created_at": "2025-12-09T19:32:23.281+00:00",
          "height": 1080,
          "width": 1920,
          "storage_key": "b0d806ca-3bec-4792-b76a-4810423070a7",
          "context": "documentation"
        },
        "storage_key": "b0d806ca-3bec-4792-b76a-4810423070a7",
        "context": "documentation",
        "width": 500,
        "settings": {
          "is_hidden": false
        }
      }
    ]
  },
  "settings": {
    "is_hidden": false
  }
}
```

This is the only display type that allows toggling between *Play In Editor* and *Simulate in Editor* by using the Possess and Eject buttons. In the **Viewport** modes, you can also use the Pause and Stop buttons to interrupt gameplay.

![Image](https://dev.epicgames.com/community/api/documentation/image/c42bf45b-2225-411b-b42b-b74cef8827aa)

By default, the preview window does not automatically get control of the mouse cursor. You can click in the preview window to turn control of the mouse cursor over to the game.

![Image](https://dev.epicgames.com/community/api/documentation/image/1bee3fbb-c2b9-4356-aca3-cf43b22cc2a7)

To regain control of the mouse cursor, press **Shift+F1**.

![Image](https://dev.epicgames.com/community/api/documentation/image/40d1a788-4262-42de-b83a-801aa02090e9)

Small labels will appear in the preview window when you toggle mouse control. To change the options for mouse control or how the mouse control label displays, use the [Play In Editor settings window](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-settings-in-unreal-engine).

$ New Window : Gameplay will be shown in a new window. To change the default size of new windows, use the [Play In Editor settings window](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-settings-in-unreal-engine).

**Click to see full-size image:**

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "image",
        "image_id": 26335655,
        "caption": "",
        "alt_text": "",
        "image": {
          "id": 26335655,
          "file_name": "NewWindow_Windows.png",
          "file_size": 773077,
          "content_type": "image/png",
          "created_at": "2025-12-09T19:32:23.884+00:00",
          "height": 754,
          "width": 1290,
          "storage_key": "034c80b4-454e-4254-8a4d-b24d5f88d145",
          "context": "documentation"
        },
        "storage_key": "034c80b4-454e-4254-8a4d-b24d5f88d145",
        "context": "documentation",
        "width": 500,
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "image",
        "image_id": 26335656,
        "caption": "",
        "alt_text": "",
        "image": {
          "id": 26335656,
          "file_name": "NewWindows_Mac.png",
          "file_size": 1244052,
          "content_type": "image/png",
          "created_at": "2025-12-09T19:32:24.129+00:00",
          "height": 754,
          "width": 1290,
          "storage_key": "2e9543ac-2f57-4fbd-b0b8-9d2dfbf3200e",
          "context": "documentation"
        },
        "storage_key": "2e9543ac-2f57-4fbd-b0b8-9d2dfbf3200e",
        "context": "documentation",
        "width": 500,
        "settings": {
          "is_hidden": false
        }
      }
    ]
  },
  "settings": {
    "is_hidden": false
  }
}
```

When playing a game preview in a new window, you cannot switch to a *Simulate In Editor* session. However, you can still pause and stop gameplay with the toolbar buttons that appear.

![Image](https://dev.epicgames.com/community/api/documentation/image/8fa783b1-63e5-4266-ba32-12ab38db54ff)

By default, playing in a new window will give mouse control to the game automatically. You can press **Shift+F1** to regain control of your mouse cursor.

$ Standalone Game : Gameplay will be shown in a new window that runs in its own process. To change the default standalone window size, use the [Play In Editor settings window](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-settings-in-unreal-engine).

**Click to see full-size image:**

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "image",
        "image_id": 26335658,
        "caption": "",
        "alt_text": "",
        "image": {
          "id": 26335658,
          "file_name": "Standalone_Windows.png",
          "file_size": 1246719,
          "content_type": "image/png",
          "created_at": "2025-12-09T19:32:24.439+00:00",
          "height": 758,
          "width": 1296,
          "storage_key": "c01f1811-cfe7-4f42-89c3-c2d593d2a88a",
          "context": "documentation"
        },
        "storage_key": "c01f1811-cfe7-4f42-89c3-c2d593d2a88a",
        "context": "documentation",
        "width": 500,
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "image",
        "image_id": 26335659,
        "caption": "",
        "alt_text": "",
        "image": {
          "id": 26335659,
          "file_name": "Standalone_Mac.png",
          "file_size": 840932,
          "content_type": "image/png",
          "created_at": "2025-12-09T19:32:24.757+00:00",
          "height": 758,
          "width": 1296,
          "storage_key": "db9900d3-b58b-4005-bca2-308e148d142e",
          "context": "documentation"
        },
        "storage_key": "db9900d3-b58b-4005-bca2-308e148d142e",
        "context": "documentation",
        "width": 500,
        "settings": {
          "is_hidden": false
        }
      }
    ]
  },
  "settings": {
    "is_hidden": false
  }
}
```

Because this display type lets you play the game in its own process, you cannot pause or stop the game. You also cannot switch to *Simulate In Editor*. As a result, the toolbar buttons do not change when playing a standalone game preview.

By default, playing in a standalone window will give mouse control to the game automatically. You can press **Shift+F1** to regain control of your mouse cursor.

#### Start Locations

$ Camera Location : Gameplay begins at the current camera location.

$ Default Player Start : Gameplay begins at the Player Start location.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If your game uses a NavMesh for either player-controlled or AI-controlled movement, using Camera Location for your Play In Editor starting location could cause you to spawn\nin a location that breaks pathing.  In this case, starting a Play In Editor session from the Default Player Start is recommended.",
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

### Play From Here

You can access an additional Play In Editor mode by right-clicking in the **Viewport** and selecting **Play From Here**.

![Play from here](https://dev.epicgames.com/community/api/documentation/image/e59cdbee-eec8-4ed2-9de4-f214943e62aa)

_Click image for full size._

**Play From Here** begins gameplay at the location that you have clicked, and acts as if your **Display Type** is set to **Level Viewport**.

### Switching to Simulate In Editor

While in a Play In Editor session in a viewport, press **Shift+F1** to regain your mouse control. Then, click on **Eject** in the **Toolbar** to switch to a Simulate In Editor session.
You will detach from the player controller, and begin a Simulate In Editor session at your current location.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can also press the <strong>Eject</strong> keyboard shortcut (<strong>F10</strong>) to switch to Simulate In Editor from Play In Editor.",
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

If you have set up more than one client for your Play In Editor testing with [Networked Play In Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/play-in-editor-multiplayer-options-in-unreal-engine), only the first session (the one in the **Viewport**) will support
switching to Simulate In Editor mode. Even for single-player gameplay testing, *Play In Editor* sessions where the game is in a new window or in a standalone game process do not support switching to Simulate In Editor.

## Simulate In Editor

Using the **Simulate** button begins a **Simulate In Editor** session in the currently active viewport. While simulating, gameplay begins, including the execution of Blueprints and C++ code that do not rely on a player's interaction with the game. While simulating, you have full access to the Editor's tools, so you can modify the scene and its contents, or even place new Actors. You can also select and inspect Pawns controlled by AI right as they are performing actions, and quickly debug and tweak gameplay behaviors. However, because you are not using a PlayerController while simulating, you cannot enter game controls. You can save certain changes made in a Simulate In Editor session using **Keep Simulation Changes**.

### Switching to Play In Editor

While in a Simulate In Editor session, you can click on **Possess** in the **Toolbar** to switch to a Play In Editor session.
You will attach to the player controller, and begin a Play In Editor session in the active level viewport.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can also press the <strong>Possess</strong> keyboard shortcut (<strong>F10</strong>) to switch to Play In Editor from Simulate In Editor.",
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

If you began in-editor testing with a Simulate In Editor session, and then used Possess to attach to the player controller, you will begin
your Play In Editor session at the default player start. This is equivalent to selecting **Play** > **Selected Viewport** > **Default Player Start** from the **Play** dropdown menu.
However, if you had previously swapped from a Play In Editor session to a Simulate In Editor session, without leaving in-editor testing mode, when you click **Possess**,
you will re-attach to the player controller and resume gameplay at the location in the level where you previously clicked on **Eject**.

## Testing Gameplay

### Blueprints

When you enter Play In Editor or Simulate In Editor mode, all your Blueprint are compiled, although they are not saved. While playing or simulating, all Blueprint graphs are read-only, so you cannot add additional nodes or connect wires differently.

![Simulating readonly](https://dev.epicgames.com/community/api/documentation/image/c0694ce2-627e-4e1f-983d-3f9f7d00c956)

However, you can change Blueprint defaults while a preview session is active, and the changes will be applied to all instances of that Blueprint in the level you are testing.

### C++

For projects that contain C++ code, there is a **Compile** button on the **Level Editor Toolbar**. This button recompiles and reloads game code on the fly. If you change a property or a function in
a C++ file in your project, clicking the **Compile** button will recompile and reload your game module, so that your code changes are reflected in the editor. In some cases, you can even compile
while using Play In Editor or Simulate In Editor, and your code changes will update without you needing to stop gameplay or simulation.
