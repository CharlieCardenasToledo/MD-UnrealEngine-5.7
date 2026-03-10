# Lyra Sample Game

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine

> Application Version: 5.7

**Lyra** is a learning resource designed as a sample game project to help you understand the frameworks of Unreal Engine 5 (UE5). Its architecture is designed to be modular, including a core system and plugins that are updated regularly along with the development of UE5.

- Cross-Platform compatibility and scalability.
- Online Multiplayer and cross-play support for Epic Online Services and Console Online Subsystems.
- Features a choice between three different Game modes: Elimination (Team Deathmatch), Control (Capture the Control point) and Exploder (a top down party game).
- A customized Gameplay Ability System.
- Niagara FX.
- Unreal Motion Graphics (UMG) widget classes and UI Icons for the project's gameplay concepts including menu settings, controller key sticks, and displays for health, mana, and ammo. These UI features are designed with modularity so you could use their systems in your own game independent of Lyra.
- Optimized, hand-crafted content including locomotion animation assets, sounds, and a weapon system compatible with any Pawn.
- New UE5 Mannequins, Manny, and Quinn. These Mannequins are playable characters that share the same core skeleton hierarchy as MetaHumans, with a compatible animation system.

## Downloading the Lyra Starter Game

To install the Lyra Starter Game sample project, follow these steps:

1. Access the [Lyra Starter Game sample](https://fab.com/s/3fe3f994dd6d) from **Fab** and click **Add to My Library** for the project file to show in the **Epic Games Launcher**. Alternatively, you can search for the sample project using Fab in Launcher, or the Fab plugin for UE.
2. From the **Epic Games Launcher** go to **Unreal Engine > Library > Fab Library** to access the project.
3. Click **Create Project** and follow the on-screen instructions to download the sample and start a new project.

To learn more about accessing sample content from Fab, see [Samples and Tutorials](https://dev.epicgames.com/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine).

## Downloading Lyra for Engine Source Builds

You can download your own source build of Unreal Engine, refer to [Downloading Unreal Engine SourceCode](programming-and-scripting/development-environment-setup/downloading-unreal-engine-source-code).

When you have finished downloading your Unreal Engine source build, you will want to download and install Lyra inside the top level directory of your custom-built engine. After selecting a top level directory, it will create a LyraStarterGame subdirectory, then create a LyraStarterGame.uproject file including the source code and content.

![lyra-uproject-directory](https://dev.epicgames.com/community/api/documentation/image/ac514aed-b4a0-41d8-8b45-8a2dab5d15e2)

To launch your installed copy of the sample, you can either double click the `.uproject` file or launch the sample directly from the Library tab of the launcher.

![lyra-sample-from-library-launcher](https://dev.epicgames.com/community/api/documentation/image/f705b0e8-98c7-4562-8ac2-953d97e83d38)

If you are using a custom-built version of the engine, you can recreate project files and launch Lyra as a project from inside your source code editor such as Visual Studio.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you right click the <code>LyraStarterGame.uproject</code> file you can associate it with a different installed version of the engine if you have multiple copies installed, or generate project files for compiling with a source code editor.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26060525,
      "caption": "",
      "alt_text": "uproject-options-list",
      "image": {
        "id": 26060525,
        "file_name": "UProjectOptions.png",
        "file_size": 3495,
        "content_type": "image/png",
        "created_at": "2025-09-12T16:54:11.829+00:00",
        "height": 69,
        "width": 293,
        "storage_key": "e8ebe2be-2b0d-4ccb-9e71-bc9f1b87bab1",
        "context": "documentation"
      },
      "storage_key": "e8ebe2be-2b0d-4ccb-9e71-bc9f1b87bab1",
      "context": "documentation",
      "width": null,
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

## Playing the Game Sample

When you launch Lyra, the **DefaultEditorOverview** level will be loaded as the **Default Map**. From the Editor, you can click on **Play In Editor**(**PIE**) to launch the default level.

![play-in-editor-arrow](https://dev.epicgames.com/community/api/documentation/image/e3808222-4097-40bf-a053-81f4a6d04d33)

When in PIE, Your Player Controller will take possession of the Lyra Pawn. In the level there are several portals that load into an **Experience**.

![main-game-select](https://dev.epicgames.com/community/api/documentation/image/7d578996-9ac9-4c2c-8174-67afd4a8b578)

The table below provides a brief description into each map:

| Game Mode Map | Description | Content File Path |
| --- | --- | --- |
| **Control** | Secure the control points along with your teammates to increase your score and win. | `/ShooterMaps/Maps/L_Convolution_Blockout` |
| **Elimination** | Find and eliminate enough enemies to win in this classic head-to-head team match. | `/ShooterMaps/Maps/L_Expanse` |
| **Front End** | Contains the Main Menu of the Lyra sample game. | `/Game/System/FrontEnd/Maps/L_LyraFrontEnd` |
| **Default Map** | The base example of the user facing map. | `/Game/System/DefaultEditorMap/L_DefaultEditorOverview` |
| **Shooter Gym** | A small test level to test the ShooterCore plugin functionality. | `/ShooterCore/Maps/L_ShooterGym` |
| **Exploder** | Destroy blocks, collect power-ups, and avoid getting exploded in this top-down party game. | `/TopDownArena/Maps/L_TopDownArenaGym` |

The maps for each game mode can be loaded directly in the editor by using **File > Open Level** and navigating to the content file paths listed above.

![using-the-open-level-window](https://dev.epicgames.com/community/api/documentation/image/2ce6972e-abbd-46ad-b826-1c44e57a99da)

Most of the maps are located inside game feature plugins. After loading a map like **Expanse** for the first time, the **Editor Viewport** will be empty because it is a **World Partition** map.

![expanse-world-partition](https://dev.epicgames.com/community/api/documentation/image/6cd8ed19-6080-439a-940e-f7290efe2b0a)

To see the level Actors, select the **world partition grid cells** by clicking and dragging in the bottom right **World Partition** details panel, then right click and select **Load Selected Cells** to load that part of the map.

![Image](https://dev.epicgames.com/community/api/documentation/image/47c7b07f-3336-4d2a-850d-edce9a211871)

Using PIE while one of the Game Mode levels is open will load the appropriate game mode as if you had walked into the appropriate portal on the default map.

For more information on Lyra's Game maps and menus, refer to the [A Tour of Lyra](https://dev.epicgames.com/documentation/en-us/unreal-engine/tour-of-lyra-in-unreal-engine) reference page.

## Lyra Framework Systems

Lyra makes use of the **Gameplay Feature Plugins**, this means that the Content folder only contains generic assets and the main lobby, however, the plugins folder contains the different core elements that create the Lyra Starter Game.

![plugins-content-folder](https://dev.epicgames.com/community/api/documentation/image/c2767406-b05e-4db8-950f-9053e3892775)

When a game experience is chosen inside the lobby, the game will load the plugins that are required. For example, choosing the **Expanse** Team Deathmatch\_ map will load **ShooterCore** for the pawn and mechanics, and **ShooterMaps** for the level.

| Plugin Folder Name | Description |
| --- | --- |
| **Lyra Example Content** | Contains shared materials, such as grids. |
| **Shooter Core Content** | The core elements of the LyraShooterGame experience. This includes gameplay logic for game modes, specific Gameplay Abilities like Dash, and Blueprints for Actors such as teleporters and grenades, Bots, Weapons and User Interface elements. |
| **ShooterMaps Content** | The maps used by the LyraShooterGame (Expanse and Convolution), with associated materials and content. |
| **TopDownArena Content** | The content for the TopDownArena experience, from the map generator to power ups. |

Experiences are defined using a **LyraExperienceDefinition** class. You can access the **Default Gameplay Experience** from the World Settings by navigating to the **Toolbar** > **Window** > **World Settings** > **Game Mode**.

![world-settings-experience-definition](https://dev.epicgames.com/community/api/documentation/image/ab467ec5-493f-42d3-9a4c-fb4339d5c6b3)

You can think of experiences as a much more advanced version of a GameMode. Multiple Experiences can exist inside a plugin, for example the experiences Team Death Match and Control Points both use the ShooterCore plugins and are derived from the same parent class(**B\_LyraShooterGameVase**, a child class of the LyraExperienceDefinition.)

These classes contain the information that are used in Lyra's input and gameplay mechanics. While other options contain information like the scoring system (based on Elimination for Team Deathmatch and Capture for Control Points)

## Topics

- [Related Document](en-us/unreal-engine/lyra-sample-game-in-unreal-engine.md)
