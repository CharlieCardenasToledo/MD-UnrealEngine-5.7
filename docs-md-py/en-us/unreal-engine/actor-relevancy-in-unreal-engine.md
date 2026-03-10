# Actor Relevancy

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/actor-relevancy-in-unreal-engine

> Application Version: 5.7

Unreal Engine levels can be very large. At any time, a player might only see a small fraction of the total number of actors in a level. Most of the actors are not visible or audible, nor do they have a significant effect on the current player. The set of actors the server determines are capable of affecting a client in any significant way are considered **relevant** for this client. The set of relevant actors is determined on a per-client, or, in networking terms, a per-connection basis. Unreal Engine only replicates actors to a client if they are relevant for that client.

The following image comparison showcase a contrived example that uses *distance-based* relevancy. The primary actor (in the middle of the frame) is set to have replicated actors remain relevant if they are within 300 centimeters (3 meters). In the before image, the secondary actor is within 300 cm, and is relevant. This means that the secondary actor is replicated to the primary actor’s connection and is visible. In the after image, the secondary actor has traveled beyond 300 cm from the primary actor; therefore, the actor is no longer relevant to the primary actor, is not replicated to the primary actor’s connection, and is not visible.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26338744,
  "caption_left": "Actor relevant",
  "image_right_id": 26338745,
  "caption_right": "Actor not relevant",
  "image_left": {
    "id": 26338744,
    "file_name": "actor-relevant.png",
    "file_size": 859446,
    "content_type": "image/png",
    "created_at": "2025-12-10T16:56:39.531+00:00",
    "height": 630,
    "width": 1200,
    "storage_key": "f8226a97-92d4-48f0-a3d4-c28254f266cc",
    "context": "documentation"
  },
  "image_right": {
    "id": 26338745,
    "file_name": "actor-not-relevant.png",
    "file_size": 853035,
    "content_type": "image/png",
    "created_at": "2025-12-10T16:56:39.738+00:00",
    "height": 630,
    "width": 1200,
    "storage_key": "395c9fa9-f98a-4bd7-8a76-61be5a142333",
    "context": "documentation"
  },
  "image_left_storage_key": "f8226a97-92d4-48f0-a3d4-c28254f266cc",
  "image_right_storage_key": "395c9fa9-f98a-4bd7-8a76-61be5a142333",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Dynamically spawned, replicated actors are destroyed on the client when they are no longer relevant. This is why the secondary actor is no longer visible to the primary actor in this case.",
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

## Obtain an Actor’s Relevancy

The network driver determines whether an actor is relevant for a particular connection with a call to [AActor::IsNetRelevantFor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/IsNetRelevantFor?application_version=5.5). This is handled automatically by the network driver.

### Make an Actor Relevant

You can force any actor to be relevant by calling [AActor::ForceNetRelevant](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/ForceNetRelevant?application_version=5.5) in your `AActor`-derived class.

### Override Actor Relevancy

You can customize actor relevancy by overriding the virtual function `AActor::IsNetRelevantFor` in your `AActor`-derived class.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Use caution when overriding <code>AActor::IsNetRelevantFor</code>. This may have unintended consequences if you are not familiar with Unreal Engine's replication system.",
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

## How Relevancy is Determined

The virtual function `AActor::IsNetRelevantFor` implements several tests to determine the set of actors that are relevant to a connection.

### Parameters

`AActor::IsNetRelevantFor` uses three parameters to determine whether the calling actor object is relevant:

| Parameter | Description |
| --- | --- |
| `RealViewer` | Client network object controlling the current actor for which relevancy is being checked. This is usually a Player Controller. |
| `ViewTarget` | Actor currently viewed or controlled by `RealViewer`. This is usually a Pawn. |
| `SrcLocation` | Source location of the controlling network object. This is used when distance-based relevancy is enabled. |

### Relevancy Logic

For a given actor and connection, the following tests are performed:

- If at least one of the following conditions hold, then the current actor is relevant for this connection: The current actor is always relevant. The current actor is owned by the current connection’s Pawn. The current actor is owned by the current connection’s Player Controller. The current actor is the current connection’s Pawn. The current connection’s Pawn is the instigator of some action, such as noise or damage.
- If the following conditions hold, then the replication system uses the current actor’s owner’s relevancy to determine whether it is relevant for this connection: The current actor has an owner. The current actor is set to use its owner’s net relevancy.
- If the following conditions hold, then the current actor is not relevant for this connection: The current actor is only relevant to its owner. The current actor does not have an owner. The current actor’s owner is not relevant.
- If the following condition holds, then the system uses the current actor’s base relevancy to determine whether it is relevant for this connection: The current actor is attached to the skeleton of another actor.
- If the following conditions hold, then the current actor is not relevant for this connection: The current actor is hidden. The current actor does not have a root component or the root component does not have collision enabled.
- If the following conditions hold, then the current actor is relevant for this connection: The Game Network Manager ([AGameNetworkManager](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AGameNetworkManager?application_version=5.5)) is set to use distance-based relevancy. The current actor is within the relevancy distance.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "This relevancy logic is for the base <code>AActor</code> class. Other <code>AActor</code>-derived classes may contain different network relevancy logic. For example, the <code>APawn</code> and <code>APlayerController</code> classes override <code>AActor::IsNetRelevantFor</code>. Therefore, they have different conditions for relevancy. See <code>Pawn.cpp</code> and <code>PlayerController.cpp</code> for more information.",
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

## Customize Relevancy Settings

You can customize network relevancy settings for your `AActor`-derived class in the Replication section of the Unreal Editor Details Panel or in C++.

![Edit relevancy settings in the Details Panel](https://dev.epicgames.com/community/api/documentation/image/10cc179d-d4fe-4157-8a7b-d3ba6bf31800)

## Relevancy Reference

The following tables provide functions and properties pertaining to actor relevancy that can be found in the `AActor` class:

### Functions

| Name | Description |
| --- | --- |
| [ForceNetRelevant](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/ForceNetRelevant?application_version=5.5) | Force this actor to be network relevant if it is not already relevant by default. |
| [IsNetRelevantFor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/IsNetRelevantFor?application_version=5.5) | Check if this actor is relevant for a specific network connection. |
| [IsRelevancyOwnerFor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/IsRelevancyOwnerFor?application_version=5.5) | Check if this actor is the owner when performing network relevancy checks for actors marked `bOnlyRelevantToOwner`. |
| [IsReplayRelevantFor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/IsRelevancyOwnerFor?application_version=5.5) | Check if this actor is relevant for recorded replay. |
| [IsWithinNetRelevancyDistance](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/IsWithinNetRelevancyDistance?application_version=5.5) | Check if the square of the distance between the given source location and this actor’s location is within `NetCullDistanceSquared`. |

### Properties

| Name | Description |
| --- | --- |
| [bAlwaysRelevant](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor?application_version=5.5) | Always relevant for network replication. Overrides `bOnlyRelevantToOwner`. |
| [bNetUseOwnerRelevancy](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor?application_version=5.5) | If this actor has a valid owner, call the owner's `IsNetRelevantFor` and `GetNetPriority`. |
| [bOnlyRelevantToOwner](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/bOnlyRelevantToOwner?application_version=5.5) | If true, this actor is only relevant to its owner. |
| [bRelevantForNetworkReplays](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor?application_version=5.5) | If true, this actor is replicated to network replays. Default true. |
| [NetCullDistanceSquared](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor?application_version=5.5) | Square of the maximum distance from the client’s viewport that this actor is relevant and replicates. |
| [Owner](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor?application_version=5.5) | Owner of this actor. Used for replication with `bNetUseOwnerRelevancy` and `bOnlyRelevantToOwner`. |
