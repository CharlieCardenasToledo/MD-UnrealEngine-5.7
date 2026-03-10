# Tracks

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine

> Application Version: 5.7

In Sequencer, Actor properties and other elements are accessed by the adding of tracks to your timeline. Depending on the track's type, they can be used to organize your tracks, create keyframes, or enable other auxiliary functions.

#### Prerequisites

- You have an understanding of [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine) and its [Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine).

## Track List

Below is a list of the main tracks you can add in Sequencer.

- [Related Document](en-us/unreal-engine/sequencer-track-list-in-unreal-engine.md)

## Adding Tracks

Sequencer provides a variety of ways to add tracks to your timeline.

Clicking **Add Track (+)** in Sequencer's Outliner reveals the list of tracks to add to your sequence. Select any track here to add it to Sequencer.

![sequencer track list](https://dev.epicgames.com/community/api/documentation/image/f0f48154-87f8-4ee7-bac6-7ef226240b5c)

Right-clicking in the empty region of the outliner will also bring up the track list.

![sequencer track list](https://dev.epicgames.com/community/api/documentation/image/b797c6f1-6f30-4080-827f-7b1857245ae3)

### Adding Actors

One of the most common track Sequencer uses is the [Object Binding Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-actor-tracks-in-unreal-engine). These are tracks that bind to **Skeletal Meshes**, **Static Meshes**, **Effects**, **Blueprints**, **Components** and other objects in a Level.

You can add Actors to your sequence by navigating in the **Add Track (+)** menu to the **Actor To Sequencer** submenu. Here you can choose any Actor currently in your Level to add to your sequence, or you can also search for a specific Actor using the search bar.

![actor to sequencer](https://dev.epicgames.com/community/api/documentation/image/ed04fb8a-a83f-49f7-a15c-418e26d685eb)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If an Actor is already selected in your Level, then it will be listed at the top of the <strong>Actor To Sequencer</strong> list for convenience.",
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

You can also drag Actors from other windows, like the  and add them into Sequencer.

![actor to sequencer drag drop](https://dev.epicgames.com/community/api/documentation/image/a92f420a-7b9b-436f-92be-359df18eabdd)

Actors can also be added as [Spawnables](animating-characters-and-objects/Sequencer/Overview/SpawnablesPossessables) by dragging them from the [Content Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-in-unreal-engine) or [Place Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine) panels.

![actor to sequencer content browser place actor](https://dev.epicgames.com/community/api/documentation/image/4bcc611a-3753-4598-b544-7858ad82c655)

### Adding Components

Some tracks allow for components and other track types to be added under their main header track. This is done to access specific track functionality, such as transform, components, properties, and other similar features.

To add a component track, hover over the track and click **Add Track (+)** to view a list of tracks available for the selected track. Typically, this list will be filtered based on the types of tracks and components that track or Actor can support.

![add child track](https://dev.epicgames.com/community/api/documentation/image/285ba8d0-3a95-4047-8c7a-48781d8edb8e)

As you can with most menus in Unreal Engine, you can type to filter the results in the **Add Track (+)** menu, making it easier to locate a specific property, component, or other track to add.

![type to filter tracks](https://dev.epicgames.com/community/api/documentation/image/b6cf26aa-0703-4705-94e8-505de6e9c0b3)

## Organization

Most tracks have properties that allow for them to be edited and displayed in different ways. These properties are saved in Sequencer and can be shared with others working on your project.

### Renaming

To assist in organization, all top-level tracks and components can be renamed in Sequencer. You can rename a track by triple-clicking on the track text, or right-clicking and selecting **Rename**, or by pressing **F2**.

![rename track](https://dev.epicgames.com/community/api/documentation/image/cb6c642a-3b66-45e3-bd03-e64f6acb18b6)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "When renaming a track bound to an Actor in the Level, the Actor in the level also renames.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26445414,
      "caption": "",
      "alt_text": "rename track renames actor",
      "image": {
        "id": 26445414,
        "file_name": "Rename3.gif",
        "file_size": 56192,
        "content_type": "image/gif",
        "created_at": "2026-02-13T16:28:27.726+00:00",
        "height": 240,
        "width": 599,
        "storage_key": "0dbf7797-b207-4323-a480-8dc59d8eeae0",
        "context": "documentation"
      },
      "storage_key": "0dbf7797-b207-4323-a480-8dc59d8eeae0",
      "context": "documentation",
      "width": null,
      "autoplay": true,
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

Most, but not all tracks can be renamed. Typically, you cannot rename a track if it is a property. However, some property tracks can be renamed, such as Transform.

![rename track restrict](https://dev.epicgames.com/community/api/documentation/image/a9680aac-0b89-4eb3-bf83-dc85681a4349)

*Tracks in Green can be renamed, tracks in Red cannot.*

### Lock

Tracks can be locked to prevent keyframes on them and their subtracks from being edited. Right-click a track and select **Locked** to lock that track. When a track is locked, all keyable tracks under it will display with a red border denoting the lock state.

![lock track](https://dev.epicgames.com/community/api/documentation/image/1c890c8a-11ff-4bb0-9e70-3443e2944297)

### Pin

You can **Pin** tracks so that they will appear in a separate outliner section at the top of your Sequencer outliner. Right-click a track and select **Pinned** to pin that track.

![pin track](https://dev.epicgames.com/community/api/documentation/image/fc4018c2-90e3-4d4b-8a18-c10b4c576efb)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Only one track can be pinned within each sequence.",
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

### Mute

Muting tracks causes them to become inactive and to not display any of their properties or keyframe results from Sequencer. Right-click a track and select **Mute** to mute that track.

![mute track](https://dev.epicgames.com/community/api/documentation/image/1efbc802-9df5-4859-af3d-ed4cffe966f7)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If the <strong><a data-document-id=\"3231543\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-actor-tracks-in-unreal-engine\">Object Binding Track</a></strong> is muted, it will also hide the Actor in the viewport.",
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

### Solo

When you **Solo** a track, all other tracks will be muted, allowing for the soloed track to be viewed in isolation. Right-click a track and select **Solo** to solo that track.

![solo track](https://dev.epicgames.com/community/api/documentation/image/b3d55f7c-f931-4884-ab5c-15aec4426039)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Soloing and muting are editor-only operations and do not impact the Level at runtime, unless you are previewing through <strong><a href=\"building-virtual-worlds/level-editor/in-editor-testing\">Play In Editor</a></strong>.",
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

### Reordering

Tracks can be reordered in the outliner by dragging them above or below each other. Visual cues appear when dragging to indicate where the track will be placed.

![reorder tracks](https://dev.epicgames.com/community/api/documentation/image/dc7fdcc7-dbf4-4bb8-896c-6e8e0c8e0b4d)

## Search and Filter

You can search and filter for specific track names using Sequencer's search field. Typing the full or partial name of a track will filter out tracks that do not match that name and will include child tracks as part of its search.

![search track](https://dev.epicgames.com/community/api/documentation/image/92593b2a-17bb-4fc4-aa6d-7c66e4b7b744)

Clicking the **Filters** button will also reveal a list of common track types that you can filter for.

![filter track](https://dev.epicgames.com/community/api/documentation/image/14af237b-a12a-4c6a-8a09-33c7bdc14a1b)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "When a filter is applied, the <strong>Filter</strong> button will indicate with a red dot.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26445424,
      "caption": "",
      "alt_text": "filter indication",
      "image": {
        "id": 26445424,
        "file_name": "Filter2.png",
        "file_size": 8237,
        "content_type": "image/png",
        "created_at": "2026-02-13T16:28:28.935+00:00",
        "height": 108,
        "width": 339,
        "storage_key": "63a4e511-9b32-41d5-a6fc-77bf0e106f4f",
        "context": "documentation"
      },
      "storage_key": "63a4e511-9b32-41d5-a6fc-77bf0e106f4f",
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
