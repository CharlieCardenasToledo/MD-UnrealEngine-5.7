# Spawnables and Possessables

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/spawn-temporary-actors-in-unreal-engine-cinematics

> Application Version: 5.7

In Sequencer, you can choose to either reference an Actor that currently exists in the scene, referred to as a **Possessable**, or spawn a new Actor, referred to as a **Spawnable**. This document provides an overview of these concepts and how you can use them in your scenes.

#### Prerequisites

- You have an understanding of **[Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine)** and its **[Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine)**.
- You know how to create and use **[Tracks](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine)**.

## Possessable and Spawnables

### Possessable

You can possess Actors by adding existing Actors in a level to your sequence. The link is formed as a [soft object path](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject/FSoftObjectPath?application_version=5.5). In most cases this might be an acceptable or even preferable workflow. If your scene requires a high degree of interaction with currently existing Actors in a **Level Sequence**, then possessing is likely the best choice for referencing Actors.

You can add any Actor to the sequence by selecting it or picking an Actor from the **Add Actor to Sequencer** list. You can also drag an Actor from the **Outliner** to an open space in **Sequencer**.

![Actor to sequencer possessable](https://dev.epicgames.com/community/api/documentation/image/de2d8baf-d79a-41b9-876b-78a9a819d269)

### Spawnable

In cases where your scene requires Actors that might be temporary for the duration of a scene, you can use **Spawnables**. By default, when a sequence with a Spawnable Actor starts, the Actor will be spawned. When the sequence ends, the Actor will be destroyed and removed. You can also explicitly control the frames during which the Actor is spawned and destroyed with the Spawn Track.

#### Create Spawnable

There are two methods for spawning Actors: dragging actors and adding an Actor.

If you have an existing Actor that isn't in **Sequencer** and you want to turn it into a **Spawnable**, add it to **Sequencer** as a **Possessable** and then convert the Actor into a **Spawnable**.

You can create a **Spawnable** by dragging it into Sequencer. Drag an Actor from the **[Content Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-in-unreal-engine)**, **[Outliner](building-virtual-worlds/level-editor/world-outliner)**, or **[Place Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine)** panels into an open area in Sequencer Outliner.

![Drag actor from Content Browser to Sequencer](https://dev.epicgames.com/community/api/documentation/image/542c4b17-08c5-4479-8932-62c99f72181c)

_Drag actor from Content Browser to Sequencer_

![Drag actor from Place Actors to Sequencer](https://dev.epicgames.com/community/api/documentation/image/5d1dec7b-0c45-421b-9588-4eace139d910)

_Drag actor from Place Actors to Sequencer_

To convert a **Possessable** to a **Spawnable**, follow these steps:

1. Select the Actor that you want to spawn in the Viewport or from the Outliner.
2. In Sequencer, click **Track > Add Actor to Sequencer > Add '{name of selected actor}'**. This action adds the Actor to Sequencer but it is not a Spawnable yet.
3. Right-click the Actor in Sequencer and select **Convert to Spawnable**.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "A Spawnable Actor can be converted back to Possessable. When this happens, the Actor is re-created in your level and the track binds to it, removing the Spawnable Actor.",
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

#### Identify Spawnables in Sequencer

Once an Actor has been spawned, a **lightning bolt overlay** appears on the Actor in Sequencer and in the **Outliner**.

![Possessable and Spawnable](https://dev.epicgames.com/community/api/documentation/image/725fcb97-1ff9-4f06-8dea-582563cf48b3)

_Possessable Actor Spawnable Actor_

![Spawned actors in Outliner](https://dev.epicgames.com/community/api/documentation/image/2d69f2f6-3d84-468d-8729-e8b3b3fbaecf)

_Spawned actors in Outliner_

## Spawnable Properties

Spawnable Actors have various properties that control their behavior and interactions with Sequencer. These properties can be accessed by right-clicking the Spawnable bound track and locating the **Spawnable** category.

| Property Name | Description |
| --- | --- |
| **Spawned Object Owner** | Specifies which Level Sequence owns the Actor, which also determines the automatic spawn behavior. **This Sequence** is the default setting which causes the Actor to be spawned and destroyed for the duration of the current sequence only. **Root Sequence** causes the Actor to spawn and despawn for the duration of the master sequence, if one is being used. This causes the Actor to be spawned and destroyed outside the bounds of the current sequence. **External** causes the Actor to spawn at the start of the sequence, but it will not be destroyed at the end. You can instead destroy the Actor through Blueprints by using **[Sequencer Tags and Groups](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-tags-and-groups-in-unreal-engine)**. |
| **Spawnable Level** | Specifies which Level the Actor will spawn into. This list is determined by what Levels exist in your **[Levels](https://dev.epicgames.com/documentation/en-us/unreal-engine/levels-in-unreal-engine)** window. |
| **Change Class** | This option provides a way to change which class is being spawned, while preserving any Sequencer tracks already added to this Spawnable. This does not preserve any non-Sequencer data such as object properties. |
| **Continuously Respawn** | When enabled, the Actor is checked every tick to ensure that it still exists (based on the status of the Spawn track). The Actor respawns in the event that an external destroy event did destroy it. |
| **Evaluate Tracks When Not Spawned** | When enabled, all tracks from this Actor will still be evaluated even if the Actor is not spawned. This is useful if the Actor requires any preprocessing before being spawned. |
| **Net Addressable** | When enabled, this Spawnable Actor will be spawned using a unique name that allows it to be referenced by the server and client. |
| **Save Default State** | Saves the current state of this Spawnable Actor. Typically, you don't need to click this as Unreal Engine will attempt to automatically save any changes to the Spawnable Actor. |
| **Convert to Possessable** | Converts the Actor to a Possessable Actor. When this occurs, the Actor is re-created in your Level and the Actor track binds to it, removing the Spawnable Actor. |

## Workflows

Spawnable Actors helps you create more organized scenes in terms of content organization and management.

### Lighting Scenes

Instead of placing several lights in your Level that have to be manually enabled or disabled per shot, you can add the required lights to your shot as Spawnable Actors. They will exist only for that shot and don't clutter your Level with unnecessary lights.

![Lighting scenes](https://dev.epicgames.com/community/api/documentation/image/e1318929-d6ac-4e89-b64e-07ee8eaf07b8)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "This workflow can also be used for any temporary Actor, such as particles so that it can create an instance of it.",
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
