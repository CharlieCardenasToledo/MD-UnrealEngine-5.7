# Serialization in Parrot

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/serialization-in-parrot-in-unreal-engine

> Application Version: 5.7

Setting up save and load functions for your game vary depending on the complexity of your game. Unreal Engine has [serialization support](https://dev.epicgames.com/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine) to handle saving and loading. Unreal Engine has a **SaveGame** object class that can be derived in Blueprint or C++ and works for saving simple variables. If your game requires more complicated saving and loading behavior, see this talk on [Serialization Best Practices and Techniques](https://dev.epicgames.com/community/learning/talks-and-demos/4ORW/unreal-engine-serialization-best-practices-and-techniques). If you want to write user configurable settings, use the `UGameUserSettings` utility class.

`UParrotGameUserSettings` in Parrot is derived from `UGameUserSettings`. This saves and loads the player configurable settings that Parrot needs.

## Audio Settings Example

In Parrot, the player can configure audio settings. Parrot saves the following float values:

- Main Volume
- Music Volume
- SFX Volume

Make sure that the project is using the correct game user settings class. This can be configured under **Edit** > **Project Settings** > **Engine - General Settings** by changing the **Game User Settings Class** field to point to **ParrotGameUserSettings**.

![The Game User Settings Class field pointing to ParrotGameUserSettings](https://dev.epicgames.com/community/api/documentation/image/79210b7e-a2a4-4987-b98c-d4bd928b6ff7)

Then, cast the user settings to the **UParrotGameSettings** type, and call the save function. This can be seen in `UParrotAudioSubsystem`, which is covered in [Audio Engine Implementation in Parrot](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-audio-implementation-in-parrot).

Another useful feature of using a `UGameUserSettings` derived class is that deserialization is not an issue. User settings are read and automatically applied when the game is started.
