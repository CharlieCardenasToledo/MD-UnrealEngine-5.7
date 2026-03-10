# Game Animation Sample Project

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/game-animation-sample-project-in-unreal-engine

> Application Version: 5.7

The **Game Animation Sample Project** is a project you can use to observe and learn about a modern, high-fidelity animation system in Unreal Engine. The system uses a suite of motion captured animations driven by animation features such as [Motion Matching](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-matching-in-unreal-engine) to deliver a high quality and responsive animation system for a human character’s traversal system. The system features coverage for common animation needs such as locomotion, scaling ledges, and vaulting. The project is broken up into several obstacle courses that you can navigate as several included characters.

The animation sample project is also built to be extensible, allowing you to import your own character to see how the animation system works with different characters, and even migrate the animation assets and systems into your own project to be used and built off of.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ae800846-43a5-4202-b12f-c1e77ccbb6a0/image_0.gif)


The Game Animation Sample Project is designed to be built upon as Engine and feature development continues, so it is recommended that you continue to follow updates with upcoming releases.

### Installing the Project

To install the project, download the [Game Animation Sample Project](https://www.fab.com/listings/880e319a-a59e-4ed2-b268-b32dac7fa016) from [Fab](https://www.fab.com).

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7d4dac20-17b2-41ae-af37-7a502f8df42b/projectmarketpalce.png)

To open the project, locate the project in the **Vault** section of the **Library** panel in the **Unreal Engine Launcher** and select the **Create Project** button.

After creating and opening the project, you can use the **Play In Editor** (**PIE**) controls to run the project.

### Read Me

By stepping on the **Read Me** button in the `DefualtLevel` you can view an introduction dialogue to the project.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/34c71930-27fb-4724-a4b3-cfa6ef43a9b5/image_3.png)

Here you can read a transcript of the Read Me file.

| Read Me |
| --- |
| The goal of this project is to showcase a comprehensive set of various gameplay animation features and assets for users to use, deconstruct, and learn from. For now the focus is mainly on animation features, rather than gameplay systems, so any gameplay functionality you find within this project (such as the traversal system) will be simple, serving only as an example of how animation systems can interact with gameplay systems.  This first release is centered around our new Motion Matching toolset, showing how to set up basic third person character locomotion with best practices for using motion matching with a capsule driven movement model. We also demonstrate how Motion Matching can be used to select montages and entry frames for gameplay actions. We also are heavily relying on Choosers, a recently added feature which help us control motion matching by filtering down which databases can be selected from based on gameplay context.  This project will continue to be updated and improved upon with each major engine release. Think of this as a living project that will grow over time with more animations, more features, and more ideas explored for a multitude of game types. This is just the beginning, so stay tuned, and we hope you have fun exploring the many things this project has to offer! |

### Player Controls

By stepping on the View Controls button in the `DefaultLevel` you can reference a list of the player controls.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c9d4fcc6-d6c4-400b-b85b-4d1970e9f5f9/image_4.png)

Here you can reference a list of the player controls for both keyboard and mouse, and gamepad inputs.![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fbc18715-312f-4e0d-a38b-c1606d4e9cdc/image_5.png)

| Keyboard | Controller | Action |
| --- | --- | --- |
| **W**, **A**, **S**, and **D** | **Left Analog Stick** | Moves the player character. |
| **Mouse** (**X** and **Y**) | **Right Analog Stick** | Rotates the Camera. |
| **Left CTRL** | **Right Shoulder Button** | Toggles the player’s run and walk states. |
| **Space** | **Bottom Face Button** | Causes the Character to Jump and navigate ledges and vaults in the obstacle courses. |
| **Middle Mouse Button** | **Right Analog Stick Button** | Toggles the characters rotation mode between a free rotation and a strafe. |
| **Right Mouse Button** | **Left Trigger** | Focus the camera, similar to an aim function in an action game. |
| **Number Keys** |  | When using the `CPB_Sandbox_MetaHuman_Bodies` player character, you can swap the MetaHuman mesh with the different MetaHuman body types with the **1** - **9** keys. You can also toggle the mesh to be a masculine or feminine type, using the **0** key. alt text |

### Game Animation Widget

The **Game Animation Widget** is a panel of helpful tools and properties you can use to interface with the Animation Sample Project. You can open the Game Animation Widget by controlling the character in the viewport during a PIE and stepping on the Game Animation Widget button in the `DefaultLevel`.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/62cc2f64-bed2-4a24-b173-038832e5e1eb/image_6.png)
