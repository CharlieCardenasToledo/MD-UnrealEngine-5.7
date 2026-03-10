# Subsystems in Parrot

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/subsystems-in-parrot-in-unreal-engine

> Application Version: 5.7

Parrot uses [subsystems](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-subsystems-in-unreal-engine) in Unreal Engine. Subsystems provide engine-managed lifetimes and add extension points for common functions. If you’ve used a [Singleton Pattern](https://en.wikipedia.org/wiki/Singleton_pattern) in Unity, subsystems fill a similar need. Subsystems are tied directly to the following scopes in the engine:

- Engine
- Editor
- Game Instance
- World
- Local Player

As these scopes enter different states, so do subsystems, and they can react accordingly.

A common reason to use subsystems is when you need to expose common C++ functionality to Blueprint and you know the expected lifetime.

## Audio Subsystem Example

Parrot uses an [audio subsystem](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-audio-implementation-in-parrot) for the following reasons:

- The subsystem is tied to the Game Instance’s lifetime without being on the Game Instance itself.
- The subsystem is accessible in C++ and Blueprint.
- Sound settings such as volume can be changed at any time from anywhere in the game.
- Manipulating audio settings through a subsystem provides a centralized debugging access point.
- Audio settings can be saved at any point by any external system.

To see this working in practice, look at `UParrotAudioSubsystem`. The audio subsystem interacts most with UI systems as that’s where the audio can be manipulated by the player. However, the flexibility is there if audio needs to be changed elsewhere. Whenever you’re adding a system to your game, consider whether a subsystem would be a useful abstraction.
