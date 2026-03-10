# Level Blueprints in Parrot

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-level-blueprints-in-parrot

> Application Version: 5.7

## Level Editor

The first thing you see after opening Parrot is the [level editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/BlueprintAPI/LevelEditor?application_version=5.6). By default, the project opens the Main Menu map. You can use the default editor layout or customize it. For more information about the level editor in Unreal Engine and how it compares to Unity, see [Unity to Unreal Engine Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/unity-to-unreal-engine-overview).

## Level Blueprints

In Unreal, each level or map you make has its own integrated blueprint. It acts as a level-wide event graph, where you can do level-specific setup, trigger level events, and trigger transitions to new levels. Logic implemented in the level blueprint won’t be portable and reusable in other places or levels. For more information, see [Level Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-blueprint-in-unreal-engine).

Parrot uses level blueprints to manage level sequences. For more information, see [Sequences in Parrot](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequences-in-parrot).

## Open A Level Blueprint

At the top of the editor viewport, click the **World Blueprint** button and then click **Open Level Blueprint**. This opens the level blueprint for the current level.

![Click the World Blueprint button and then click Open Level Blueprint](https://dev.epicgames.com/community/api/documentation/image/3bf1e3df-1d4a-409f-b0bc-75d9af5ed236)
