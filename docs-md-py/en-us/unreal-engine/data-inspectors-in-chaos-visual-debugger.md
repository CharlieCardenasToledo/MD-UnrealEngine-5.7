# Data Inspectors

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger

> Application Version: 5.7

The **[Chaos Visual Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine)** (**CVD**) displays data in both the **Details** panel and **Data Inspector** tabs located in the bottom-right corner of CVD’s interface.

Each data category has a dedicated Data Inspector:

- [Particle Data (Details Panel)](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger#particle-data-details-panel)
- [Collision Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger#collision-data-inspector)
- [Scene Queries](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger#scene-query-inspector)
- [Joint Constraint Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger#joint-constraint-data-inspector)

![Data Inspectors](https://dev.epicgames.com/community/api/documentation/image/027a30d4-ccf5-46f9-b211-7ceef779d9e5)

## Particle Data (Details Panel)

The **Details** panel acts as a data inspector for particle data. In the context of CVD, particles usually refer to rigid bodies.

When you select a particle in the viewport or in the **Outliner**, this panel populates with all data recorded for that particle. Unlike collision contacts or scene queries, data for selected particles persists in the inspector when you use CVD’s playback controls.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If a selected particle contains collision data, a <b>Show Collision Data Inspector</b> contextual button appears at the bottom of the Details panel. This populates the Collision Data Inspector with the selected particle’s data.",
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

| ![Static Particle Data](https://dev.epicgames.com/community/api/documentation/image/3929c004-ed36-4d57-b4ec-13057d963c61) | ![Dynamic Particle Data](https://dev.epicgames.com/community/api/documentation/image/0c14c107-3902-4e35-a08d-b00553f5af1c) |
| --- | --- |
| *Details panel for a selected dynamic particle.* | *Details panel for a selected static particle.* |

## Collision Data Inspector

The **Collision Data Inspector** displays information for a selected **particle**, **contact** (a point where two collision shapes overlap), or **collision pair** (two particles that collide with one another).

![Collision Data Inspector](https://dev.epicgames.com/community/api/documentation/image/0d82ae69-c7be-43a8-8de4-8673c442e638)

Since contacts are generated per frame, when you use CVD’s playback controls, the collision data you inspect becomes out of date. Due to this, the Collision Data Inspector only displays data for the last-selected contact during playback.

To populate the Collision Data Inspector with collision pair information, follow these steps:

1. In the viewport, select a particle with collision data.
2. Click the **Show Collision Data Inspector** contextual button that appears in the **Details** panel. ![Show Collision Data](https://dev.epicgames.com/community/api/documentation/image/05898990-5fb0-4534-8679-95522ac18279) This populates the Collision Data Inspector with data from the particle, including a dropdown list of available collision pairs. ![Available Collision Pairs](https://dev.epicgames.com/community/api/documentation/image/0a258162-8d67-4ea3-a597-206c484aa893)
3. Select the collision pair you want to inspect.
4. To identify each particle in the Details panel, Outliner, and Viewport, click the **Select Particle 0** or **Select Particle 1** button. ![Select Particle Buttons](https://dev.epicgames.com/community/api/documentation/image/4b6cfb11-ac51-4467-bb9a-4ec0388798e2)

[Video: V_iYAbTs](https://dev.epicgames.com/community/api/cms/videos/V_iYAbTs/embed.html)

## Scene Query Inspector

The **Scene Query Inspector** displays information for a visualized query that is selected in the viewport. This inspector has its own timeline that steps through the objects that were evaluated as part of the query.

![Scene Query Inspector](https://dev.epicgames.com/community/api/documentation/image/08ab0b51-118a-4abb-9d6c-5308c8528d8e)

A contextual **Go to parent query** button becomes available if CVD detects that the selected query has performed (or is itself) a subquery. You can use this button to navigate to the parent query.

![Contextual Button](https://dev.epicgames.com/community/api/documentation/image/2ace746e-768d-453c-952e-6fbb694847c8)

### Scene Query Browser

The **Scene Query Browser** is an all-in-one browser for inspecting scene queries. To access the Scene Query Browser, click **Scene Query Browser** in CVD’s main toolbar.

![Scene Query Browser Button](https://dev.epicgames.com/community/api/documentation/image/e2fbe146-6fc9-44d5-b2af-8802468e4971)

![Scene Query Browser UI](https://dev.epicgames.com/community/api/documentation/image/46dc70e4-4f32-4fb0-a389-4502a507b67b)

| Number | Description |
| --- | --- |
| 1 | Enables scene query data flags (identical to those found in **Show > Scene Query Data Flags**). |
| 2 | Toggles viewport debug text (if any) on and off. Draws data in **worldspace** or in the **foreground** (always on top of any other scene components). Identical to the options found in **Show > Scene Query Visualization Settings**. |
| 3 | Filters queries by **Trace Tag**, **Trace Owner**, **Query** **Type**, or **Solver Name**. |
| 4 | **All Enabled Queries:** Visualizes all recorded queries. **Per Solver Recording Order:** Visualizes one query at the time and enables the Recorded Scene Queries timeline (see below). |
| 5 | Naviagates between recorded queries. This is useful if there are several scene queries on one frame that happen in the same location. |

## Joint Constraint Data Inspector

The Joint Constraint Data Inspector displays [joint state and joint setting](https://dev.epicgames.com/documentation/en-us/unreal-engine/constraints-user-guide-in-unreal-engine) data for joints that are selected in the viewport. Data in this inspector updates as you n through CVD’s playback controls.

![Joint Constraint Inspector](https://dev.epicgames.com/community/api/documentation/image/ad3a4e94-d186-4a20-9b51-67477fa530e0)

## Next Up

- [Related Document](en-us/unreal-engine/capturing-data-with-chaos-visual-debugger.md)
