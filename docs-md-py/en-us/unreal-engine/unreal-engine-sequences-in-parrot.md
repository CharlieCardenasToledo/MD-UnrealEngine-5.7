# Sequences in Parrot

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequences-in-parrot

> Application Version: 5.7

Sequencer is a tool in Unreal Engine for creating cinematic sequences. Parrot uses Sequencer to create moving obstacles in the levels, such as a shark. For more information about using Sequencer in Unreal Engine, see [Cinematics and Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine).

## Shark Obstacle

The **MainMenu** level of Parrot uses level sequences to create a swimming shark. You can view how these basic sequences are set up by opening `Content/Maps/MainMenu/SwimmingShark`.

With the sequence open in Sequencer, you can see how the tracks are set up. There is a path track under the shark actor in the level, which makes the shark swim around a spline actor placed in the level. There is also an event track that triggers events to manipulate the shark’s animator to switch between its animations.
