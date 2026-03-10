# Vehicle Template

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/vehicle-template-in-unreal-engine

> Application Version: 5.7

When you create a new project, Unreal Engine gives you a list of templates you can choose from. These templates contain some ready-to-use assets, such as level geometry, a character you can control, and simple character animations. Many tutorials use one of these templates as a starting point.

In the **Vehicle** game template, the player sees the game from a camera behind or inside a vehicle. The vehicle can be driven around the play area.

## Creating a Vehicle Project

Launching Unreal Engine opens the Project Browser window, where you can choose to open an existing project or create a new one.

To create a vehicle game project, select the **Games** category on the left, and then select the **Vehicle** template.

![Image](https://dev.epicgames.com/community/api/documentation/image/56a62152-c4ba-4f30-b899-3b30c0aa3091)

_Creating a new Vehicle project in Unreal Engine._

When the **Vehicle** template is selected, there are several additional settings you can configure in the panel on the right side of the project browser window to set up the Vehicle project. You can configure the following settings:

| Target Platform | Select the kind of platform your project is intended for: **Desktop** **Mobile** |
| --- | --- |
| Quality Preset | Select the maximum quality level, based on which platform your project targets: **Maximum**, if you are developing your project for a computer or game console. **Scalable**, if you are developing your project for mobile devices. |
| Variant | The variant of the template you want to open. Variants add additional assets to the project. For more about variants, see the Template Variants section of this page. |

After following these steps, the project includes a basic level with a vehicle you can control.

To try out the level, click Play in the Main Toolbar. You’ll use the WASD keys to control the vehicle using a keyboard. However, the template also supports controller, touchscreen, and VR controls.

- Press the **W** and **S** keys to accelerate and brake the vehicle.
- Press **A** and **D** to steer the vehicle left or right.
- Use the **mouse** to move the camera.
- Press **Space** to use the handbrake.
- Press **L** to toggle the headlights on and off.
- Press **Backspace** to reset the vehicle.

## Template Variants

The Vehicle template includes a set of variants to choose from located in the **Variants** dropdown menu. Variants give you a way to build different gameplay styles. The Vehicle template includes variants for **Timetrial** and **Offroad** gameplay.

![The variants for the Vehicle template.](https://dev.epicgames.com/community/api/documentation/image/54c08c88-0e1b-49d2-b354-087c366df349)

| Variant Name | Description |
| --- | --- |
| **None** | A basic template with the following contents: A vehicle that the player can move. A level with basic geometry such as roads and obstacles. |
| **Timetrial** | A template of a time trial racing game with the following contents: A vehicle that the player can move. A level with a racetrack with ramps and a tunnel. Checkpoints that the player can drive through that record the lap time. A user interface shows lap times and the current gear and speed of the vehicle. |
| **Offroad** | A template of an offroad driving game with the following contents: A vehicle that the player can move. A level with procedurally-generated geometry. |

For a deeper dive into the features of these variants, see [Game Template Variants](https://dev.epicgames.com/documentation/en-us/unreal-engine/variants-in-game-templates).

### Timetrial Variant

The **Timetrial** variant features a racetrack with track gates that the player can drive through. When the vehicle passes through all of the track gates in order, the player's lap time is recorded. There is a user interface (UI) that shows the time of the current lap, the player's best recorded lap time, as well as the gear and speed (in kilometers per hour) of the vehicle.

![The Timetrial variant of the Vehicle template.](https://dev.epicgames.com/community/api/documentation/image/ccec3813-9fbd-4388-b211-bbc1cac1ff7e)

#### Vehicle

The Timetrial variant features a sports car. The assets for the sports car are located in the `Content/Vehicles/SportsCar` folder.

#### Track Gates

When the vehicle drives through all of the track checkpoints in order, the lap count goes up by one, and the lap time is recorded. The track game blueprint is located in the `Content/Variant_Timetrial/Blueprints` folder.

#### User Interface

The UI for the Timetrial variant shows a starting countdown, as well as the current lap time, the player's best lap time, and the vehicle's current gear and speed. The UI assets are in the `Content/Variant_Timetrial/UI` folder and the `Content/VehicleTemplate/UI` folder.

### Offroad Variant

The **Offroad** variant features an offroad-style buggy vehicle and a landscape with uneven terrain and hills. This vehicle showcases vehicle setups using looser suspension.

![The Offroad variant of the Vehicle template.](https://dev.epicgames.com/community/api/documentation/image/4f7b1fe5-e89e-44b0-ad28-852153a5f21c)

#### Vehicle

The Offroad variant features an offroad car. The assets for the offroad car are located in the `Content/Vehicles/OffroadCar` folder.

#### Landscape Terrain

The offroad terrain is set up using the [Landscape](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-overview) tool and [Runtime Virtual Texturing](https://dev.epicgames.com/documentation/en-us/unreal-engine/runtime-virtual-texturing-in-unreal-engine). The assets for the terrain are located in the `Content/VehicleTemplate/Maps/LandscapeInfo` folder. To improve memory cost when rendering the level, the Landscape also uses an [HLOD layer](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition---hierarchical-level-of-detail-in-unreal-engine) located in the `Content/Variant_Offroad/Maps` folder.

#### User Interface

The UI for the Offroad variant shows the vehicle's current gear and speed. The UI Blueprint is in the `Content/VehicleTemplate/UI` folder.

## Template Contents

The following section details these contents and where to find them in the **Content Browser**.

### Blueprints

The None variant of the Vehicle template include Blueprints for the following assets:

- Vehicle
- Game mode
- Player controller

These Blueprints are located in the Content/VehicleTemplate/Blueprints folder.

The **Event Graph** in each Blueprint includes comments and annotations about what the different node groups do and the logic behind their implementation.

The Timetrial variant uses the player controller and game mode in the `Content/Variant_Timetrial/Blueprints` folder.

The Offroad variant uses the player controller and game mode in the `Content/Variant_Offroad/Blueprints` folder.

### Level

In the None variant of the Vehicle template, the level, **Lvl\_VehicleBasic**, is located in the `Content/VehicleTemplate/Maps` folder.

In the Timetrial variant, the level, **Lvl\_Timetrial**, is located in the `Content/Variant_Timetrial/Maps` folder. This level includes a racetrack with track gates.

In the Offroad variant, the level, **Lvl\_Offroad**, is located in the `Content/Variant_Offroad/Maps` folder. This level includes roads and offroad terrain.

## Improving your Project

Now that you have a playable level, you can import your own content and make changes to the game. Or, you can use the assets provided in the Content Browser with this project to build it out by dragging and dropping these assets into the level and placing them where you want.

For more instructions on how to populate your level, see [Level Designer Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine).

## What's Next?

Now that you've gone through the basics of creating a vehicle-based game, here are some other things you can try:

- Populate your level with content and props from [Fab](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3). You can build a variety of indoor and outdoor environments.
- Create or modify the in-game heads-up display (HUD) with [Unreal Motion Graphics (UMG)](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-editor-reference-for-unreal-engine).
- Use [Niagara](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine) to add or change visual effects in your game.
- Add AI vehicles for the player to race against using [StateTrees](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-state-tree-in-unreal-engine) or [Behavior Trees](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---overview).
- Try building and adding a [modular vehicle](https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-modular-vehicles-overview) to your game.
