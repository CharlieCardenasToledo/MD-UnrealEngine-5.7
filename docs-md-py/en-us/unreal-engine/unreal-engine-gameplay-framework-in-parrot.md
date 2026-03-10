# Unreal Gameplay Framework in Parrot

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-gameplay-framework-in-parrot

> Application Version: 5.7

When learning the basics of Unreal Engine, you should learn how the [Unreal Gameplay Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine) works. In this document, we’ll cover how we’ll set up the game mode and game state classes for Parrot.

## Game Mode

The game mode is responsible for defining fundamental rules of play, such as the number of players, or how players join the game. It also provides a framework for setting up useful games classes, such as the game state, player controller, HUD, and default pawn class.

To set up the game mode for Parrot, follow these steps:

1. In the **Content Browser**, click **Content** > **Blueprints** > **Game**.
2. Right-click in the browser and click **Blueprint Class**.
3. Set the parent class to **AGameModeBase**.
4. Name the class "BP\_ParrotGameMode".
5. Double-click the newly created blueprint to see the core classes it defines. For Parrot, some of these classes should be changed: **Game State Class** should be set to **BP\_ParrotGameState** **Player Controller Class** should be set to **BP\_ParrotPlayerController** **HUD Class** should be set to **BP\_ParrotHUD** **Default Pawn Class** should be set to **BP\_ParrotPlayerCharacter** ![The classes list after the changes for Parrot.](https://dev.epicgames.com/community/api/documentation/image/8a3e5edb-f691-4f5d-8b69-909a7f62bcc5)
6. Go to **Edit** > **Project Settings** > **Maps & Modes** and set the **Default GameMode** to **BP\_ParrotGameMode.** ![The Default GameMode set to BP_ParrotGameMode](https://dev.epicgames.com/community/api/documentation/image/9165fd31-bb25-46ac-89eb-78fc567e6848)

Now that the game mode is set up, you can set up the game state.

## The Game State

The game state handles what is currently happening in the game. It manages information that clients need to know but is not tied to any specific player. For example, you might store team scores here.

To create a game state for Parrot, follow these steps:

1. In the main editor, select Tools > New C++ Class...
2. Set the parent class to **AGameStateBase**.
3. Name the class "AParrotGameState".
4. In the Content Browser, click **+ Add** > **Blueprint Class**.
5. Set the parent class to **AParrotGameState**.
6. Name the class "BP\_ParrotGameState".
7. In your game mode blueprint, assign **BP\_ParrotGameState** to the game state field.

## Game Mode and Game State Concept Review

For more information about game mode and game state, see [Game Mode and Game State](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-mode-and-game-state-in-unreal-engine). As new classes are created throughout development, remember to update your game mode and game state.

The game mode can also be set per map. The Main Menu in Parrot uses a different game mode than the one that is used by levels in the game.

## Game Instance

The game instance is a single persistent class instance in the engine that handles project specific functionality. It exists for the entire lifetime of your application. It contains the game’s viewport client and the local player.

Following the same pattern as the game mode and state, we create a base C++ class, UParrotGameInstance, and a blueprint class, BP\_ParrotGameInstance. You can set the game instance class for your project under Edit->Project Settings->Maps & Modes

To create a game instance for Parrot, follow these steps:

1. In the main editor, select Tools > New C++ Class...
2. Set the parent class to **UGameInstance**.
3. Name the class "UParrotGameInstance".
4. In the Content Browser, click **+ Add** > **Blueprint Class**.
5. Set the parent class to **UParrotGameInstance**.
6. Name the class "BP\_ParrotGameInstance".
7. Go to Edit > Project Settings > Maps & Modes and set the Game Instance Class to BP\_ParrotGameInstance. ![The Game Instance Class set to BP_ParrotGameInstance](https://dev.epicgames.com/community/api/documentation/image/90129fe4-1ed6-481c-98d1-22d22345137c)

## Level Streaming Example

In Parrot, different maps are specific to different game modes, and the game instance tells the game which map should be loaded using `UParrotMapDataAsset` files. These are [data assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-assets-in-unreal-engine?application_version=5.5) that contain a soft object pointer to a map file. These assets are organized on the game instance and can cycle through them as the player progresses through the game. Since this is on the game instance, you can always stream the next level in from anywhere. The player controller listens for game state changes and then call into the game instance as needed.

The following screenshot shows a Blueprint that uses the **Stream Level** node and **Async Load Asset** node to asynchronously load the soft object reference to a **ParrotMapDataAsset**. Then, the **Open Level** node is called without having to wait for a synchronous load, since the level has already been loaded. The **CommonLoadingScreen** plugin is also used here. The loading screen widget will be invoked during the preload of the next map and removed during the postload.

![The Blueprint that asynchronously loads the soft object reference.](https://dev.epicgames.com/community/api/documentation/image/892e45a9-0baf-4b64-a8cf-fbb6e628ff59)

For more details on the loading screen and why Parrot does an asynchronous load instead of a synchronous one here, see the [User Interface for Parrot](https://dev.epicgames.com/documentation/en-us/unreal-engine/user-interface-for-parrot-in-unreal-engine) documentation.
