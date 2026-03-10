# Outliner

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/outliner-in-unreal-engine

> Application Version: 5.7

The **Outliner** panel displays all the Actors within the scene in a hierarchical tree view. Using the Outliner, you can:

- Select and modify Actors.
- Search and filter Actors by name, type, and other characteristics.
- Use advanced search operators to further refine Actor searches.
- Customize which Actor information to display.

![Outliner panel in context](https://dev.epicgames.com/community/api/documentation/image/2c9a6d59-17ec-425d-9b67-d96ee338550c)

_By default, the Outliner panel docks to the right side of the Unreal Editor window. Click the image for full size._

You can have up to four instances of the Outliner and customize the settings for each instance separately. Switch between Outliner instances by right-clicking the Outliner tab and selecting a different Outliner, or go to **Window > Outliner** from Unreal Engine's main menu.

![Multiple Outliners](https://dev.epicgames.com/community/api/documentation/image/863b379f-a3f6-461d-9bdf-1842e90f396d)

_Switching between different Outliner instances._

## Outliner Actions

You can perform the following actions on an Actor in the Outliner:

| Action | Description |
| --- | --- |
| **Left-click** | Selects that Actor. |
| **Right-click** | Displays the same context menu brought up by right-clicking an Actor in the Viewport. Use this to quickly modify an Actor without having to navigate to that Actor in the Viewport. |
| **Left-click and drag** | Attaches the Actor being Dragged to another Actor. |
| **F** keyboard shortcut | With an Actor selected in the Outliner: Focuses that Actor in the Viewport. With an Actor selected in the Viewport: Scrolls the list of Actors in the Outliner to the selected Actor. |

## Searching and Filtering in the Outliner

Use the **Search** box in the Outliner to search and quickly filter the list of Actors in the scene. By default, searching displays all Actors with a partial match to the search term. If you use more than one search term, only Actors that match all the terms will appear.

You can use all of the [advanced search syntax](https://dev.epicgames.com/documentation/en-us/unreal-engine/advanced-search-syntax-in-unreal-engine) operators when searching in the Outliner.

Some of the most common operators are:

| Operator | Action | Example |
| --- | --- | --- |
| `-` | Excludes Actors that match a specific term. | `-Sky` |
| `+` | Forces a term to match exactly, as opposed to a partial match. | `+Sky` will match `Sky` but exclude `Skylight` |

You can save your search as a **custom filter** and access custom filters from the **Custom Filters** category of the **Filter** drop-down. Custom filters are saved globally for each user, which means they are available across all of the streams and projects of the user who created them.

![Filters in the Outliner](https://dev.epicgames.com/community/api/documentation/image/08786b23-972a-46c4-91c7-669b8e0b8731)

_Filters menu in the Outliner._

**Filtering** Actors in the Outliner works in the same way as [Asset filtering](https://dev.epicgames.com/documentation/en-us/unreal-engine/filters-and-collections-in-unreal-engine) in the Content Browser.

## Customizing the Outliner

**Right-click** any column header to bring up a context menu where you can select which columns to show or hide in the Outliner by enabling or disabling the checkbox next to the column name.

![Show and hide Outliner columns](https://dev.epicgames.com/community/api/documentation/image/62fac773-fec9-4d5f-a444-481e6078265e)

_Showing and hiding Outliner columns._

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Searching matches terms in all columns in the Outliner, whether or not they are visible.",
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

**Left-click and drag** the edge of a column header to resize that column.

The Outliner will always scroll to an Actor when you select that Actor in the Viewport. You can disable this behavior by toggling **Always Frame Selection** from the Outliner's **Settings** menu.

[Video: V_NYPhtF](https://dev.epicgames.com/community/api/cms/videos/V_NYPhtF/embed.html)
