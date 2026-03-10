# Data Visualization Flags

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger

> Application Version: 5.7

To help you identify unusual physics behavior, **[Chaos Visual Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine)** (**CVD**) provides debug draw tools to visualize aspects of your application that are not normally visible during runtime.

You can control which debug draw tools are visualized in the viewport by toggling data flags. Data flags are organized into the following categories:

- [Collision Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger#collisions)
- [Scene Queries](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger#scene-queries)
- [Particle Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger#particle-data)
- [Joint Constraints](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger#joint-constraints)
- [Character Ground Constraints](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger#character-ground-constraints)
- [Generic Debug Draw Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger#generic-debug-draw-data)
- [Acceleration Structures](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger#acceleration-structures-data)
- [Common Show Flags](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger#common-show-flags)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Certain flags, such as <b>Center of Mass</b>, can have a performance impact on CVD. If the debug draw limit is reached, a warning appears in the viewport reading:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "<code class=\"inline-code\">Max Debug Draw lines limit reached! Try selecting fewer debug draw categories or focus the camera in a narrower area.</code>",
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

## Collision Data

Visualized collision data can help you identify areas where collisions are behaving unexpectedly. For example, when two objects intersect one another, instead of colliding as expected.  
  
To enable collision data, follow these steps:

1. In the Viewport Toolbar, click **Show > Collision Data Flags > Enable Draw**. This option opens a list of data flags. ![Collision Data Flags](https://dev.epicgames.com/community/api/documentation/image/9ea5a13b-382c-4b4e-af5b-7731444b1291)
2. Choose from the list of data flags to toggle on or off. ![Collision Data Flags](https://dev.epicgames.com/community/api/documentation/image/e2a0bb1c-c473-4241-b65a-40b08a7ed42a)
3. Click **Collision Data Visualization Settings** to customize how the data is drawn in the viewport. ![Collision Visualization Settings](https://dev.epicgames.com/community/api/documentation/image/db5da910-e6b2-46d0-955d-256c8976c93e)

The visualization settings include the following options:

- **Show Debug Text:** Toggles viewport debug text (if any) on and off.
- **Depth Priority:** Draws data in **worldspace** or in the **foreground** (always on top of any other scene components).
- **Options for Scale and Radius:** Control the size of debug draw elements, making them easier to see in the viewport.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Most data flags include visualization settings that contain similar toggleable features. ",
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

## Scene Queries

Visualized [scene queries](https://dev.epicgames.com/documentation/en-us/unreal-engine/traces-in-unreal-engine---overview) (line traces, sweeps, and overlaps) can help you debug cases where you performed a query during runtime but the query didn't find an expected object.

To enable scene query data, follow these steps:

1. In the Viewport Toolbar, click **Show > Scene Query Data Flags > Enable Draw**. This option opens a list of data flags. ![Scene Query Data Flags](https://dev.epicgames.com/community/api/documentation/image/79d126a2-4bce-442c-8a33-3817116c4e60)
2. Choose from the list of data flags to toggle on or off. ![Scene Query Flags](https://dev.epicgames.com/community/api/documentation/image/99c5e2ee-8b97-45e3-98bc-12d9fe59b999)
3. Click **Scene Query Visualization Settings** to customize how the data is drawn in the viewport. ![Scene Query Visualization Settings](https://dev.epicgames.com/community/api/documentation/image/51680a59-f24b-4cb5-9b9c-515ac3054ecd)

## Particle Data

Visualized particle data can help you identify irregular particle behavior, such as a particle moving faster than expected after applying a force.

To enable particle data, follow these steps:

1. In the Viewport Toolbar, click **Show > Particle Data Flags > Enable Draw**. This option opens a list of data flags. ![Particle Data Flags](https://dev.epicgames.com/community/api/documentation/image/0ada1c65-ed71-4e60-923c-408f6226caed)
2. Choose from the list of data flags to toggle on or off. ![Particle Data Flags](https://dev.epicgames.com/community/api/documentation/image/8d48d5b9-6dd0-47ed-958e-fb3db934b5c3)
3. Click **Particle Data Visualization Settings** to customize how the data is drawn in the viewport. ![Particle Visualization Settings](https://dev.epicgames.com/community/api/documentation/image/53b5db12-2911-44cc-98fd-6b483b13bf02)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "CVD only records and visualizes <b>physics thread</b> particle data, not <b>game thread</b> particle data. Game thread particle data is not visualized.",
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

### Geometry

Most particles have both [simple and complex collision geometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/simple-versus-complex-collision-in-unreal-engine), but only one is used for collision detection.

Options for toggling between simple and complex geometry, and other geometry visualization flags, are located in the Viewport Toolbar under **Show > Geometry Flags** menu.

![Geometry Visualization Flags](https://dev.epicgames.com/community/api/documentation/image/827f8506-06a4-4562-9ab1-15f250a3e89b)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<b>Query Only</b> geometry is visualized with translucent material. You can click through translucent materials by pressing <b>T </b>(or click <b>Allow Translucent Selection</b> in the Hamburger Menu) to enable or disable translucent selects. ",
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

### Particle Colorization

To increase draw visibility, you can choose to colorize particles using the following modes:

- **None:** Draws particles in default gray.
- **State:** Colorizes based on a [physics body’s state](https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-bodies-reference-for-unreal-engine) in a simulation (dynamic, sleeping, kinematic, or static).
- **Shape Type:** Colorizes based on [collision geometry type](https://dev.epicgames.com/documentation/en-us/unreal-engine/simple-versus-complex-collision-in-unreal-engine) (simple shapes, convex, heightfield, or trimesh).
- **Client Server:** Colorizes based on client or server-spawned particles.

```json
{
  "type": "sequence_slider",
  "caption": "State and Default Gray",
  "images": [
    {
      "image_id": 25947768,
      "storage_key": "e27a71d1-eff0-4a3f-9cd8-44e7e4152095",
      "context": "documentation",
      "image": {
        "id": 25947768,
        "file_name": "switcher-2.png",
        "file_size": 739333,
        "content_type": "image/png",
        "created_at": "2025-08-18T14:56:54.250+00:00",
        "height": 680,
        "width": 1600,
        "storage_key": "e27a71d1-eff0-4a3f-9cd8-44e7e4152095",
        "context": "documentation"
      }
    },
    {
      "image_id": 25947769,
      "storage_key": "d1e27353-843d-400a-bf20-3f6e08ab3cd0",
      "context": "documentation",
      "image": {
        "id": 25947769,
        "file_name": "switcher-1.png",
        "file_size": 723293,
        "content_type": "image/png",
        "created_at": "2025-08-18T14:56:54.462+00:00",
        "height": 680,
        "width": 1600,
        "storage_key": "d1e27353-843d-400a-bf20-3f6e08ab3cd0",
        "context": "documentation"
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

To change the mode and customize the colors, follow these steps:

1. In the Viewport Toolbar, click **Show > Particle Colorization**. ![Particle Colorization](https://dev.epicgames.com/community/api/documentation/image/f231e948-63ac-4011-a816-e6edac6e724e)
2. In the **Colors Mode** dropdown, click the **Particle Color Mode** dropdown, and select the mode to use. ![Particle Color Mode](https://dev.epicgames.com/community/api/documentation/image/89512faf-0314-463a-9918-2790c7792f37)
3. Click the **Colors by [mode]** dropdown menu to customize colors. Then, click a color tile to open a contextual color picker. ![Color Picker](https://dev.epicgames.com/community/api/documentation/image/48f45e74-eebb-49ea-994c-54dd66ccd0fe)

The table below describes the contextual color picker user interface (UI).

| Number | Description |
| --- | --- |
| 1 | Color wheel (or color spectrum if toggled). |
| 2 | Displays current and previously selected colors. |
| 3 | Toggles sRGB preview. |
| 4 | Toggles between the color wheel and color spectrum. |
| 5 | Toggles visibility of **Color Schemes**. |
| 6 | Eyedropper tool. |
| 7 | RBG/HSV sliders. |
| 8 | Alpha slider. |
| 9 | Displays the current color’s hex code. |
| 10 | **Color Schemes**: Functions similarly to swatches in Adobe Photoshop and other design programs. |

## Joint Constraints

Visualized joint constraints can help you debug unwanted ragdoll behavior, such as twisting joints. CVD records joint constraint data as an individual piece of data for every frame. Due to this, maintaining a selection across gameplay frames is not currently possible.

To enable joint constraint data, follow these steps:

1. In the Viewport Toolbar, click **Show > Joint Constraint Data Flags > Enable Draw**. This option opens a list of data flags. ![Enable Joint Constraint Flags](https://dev.epicgames.com/community/api/documentation/image/ac26e55b-0a10-4f63-9b6d-39e7f6cf757d)
2. Choose from the list of data flags to toggle on or off. ![Joint Constraint Flags](https://dev.epicgames.com/community/api/documentation/image/0ba4e021-5d82-48c7-ae94-795dfe8ba02e)
3. Click **Joint Constraint Visualization Settings** to customize how the data is drawn in the viewport. ![Joint Constraint Visualization Flags](https://dev.epicgames.com/community/api/documentation/image/415f01aa-cb92-4bcd-8d97-3ff38b6ee6b7)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "CVD doesn’t record joint constraints by default. To enable it, click the <b>Data Channel</b> dropdown menu in the main toolbar, and check <b>JointConstraints</b>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25947755,
      "caption": "",
      "alt_text": "Enable Join Constraints",
      "image": {
        "id": 25947755,
        "file_name": "enable-joint-constraints.png",
        "file_size": 421140,
        "content_type": "image/png",
        "created_at": "2025-08-18T14:56:51.905+00:00",
        "height": 615,
        "width": 1600,
        "storage_key": "386e084f-8088-449f-88d7-bc52f9d1cd8e",
        "context": "documentation"
      },
      "storage_key": "386e084f-8088-449f-88d7-bc52f9d1cd8e",
      "context": "documentation",
      "width": 1200,
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

## Character Ground Constraints

CVD can record the state of character ground constraints used by Unreal Engine’s Character Movement System, called [Mover 2.0](https://dev.epicgames.com/documentation/en-us/unreal-engine/mover-in-unreal-engine). Using this flag, you can identify and debug unusual behavior such as characters floating above or clipping through a ground plane.

To enable character ground constraint data, follow these steps:

1. In the Viewport Toolbar, click **Show > Character Ground Constraints Data Flags > Enable Draw**. This option opens a list of data flags. ![Enable Ground Constraints](https://dev.epicgames.com/community/api/documentation/image/1e369991-f8fd-4159-8f06-dad4a8659a46)
2. Choose from the list of data flags to toggle on or off. ![Ground Constraint Flags](https://dev.epicgames.com/community/api/documentation/image/5e2ba581-b962-4d0f-85fc-225c00161e1e)
3. Click **Character Ground Constraints Visualization Settings**, to customize how the data is drawn in the viewport. ![Ground Constraint Visualization Flags](https://dev.epicgames.com/community/api/documentation/image/ae67fadb-923f-4623-a516-a169629f5514)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "CVD doesn’t record character ground constraints by default. To enable it, click the <b>Data Channel</b> dropdown menu in the main toolbar, and check <b>Character Ground Constraints</b>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25947759,
      "caption": "",
      "alt_text": "Data Channels Ground Constraints",
      "image": {
        "id": 25947759,
        "file_name": "data-channels-not-default (1).png",
        "file_size": 818525,
        "content_type": "image/png",
        "created_at": "2025-08-18T14:56:52.538+00:00",
        "height": 1105,
        "width": 2876,
        "storage_key": "dde73ca5-6cf5-4e78-bda8-81bfa8031f82",
        "context": "documentation"
      },
      "storage_key": "dde73ca5-6cf5-4e78-bda8-81bfa8031f82",
      "context": "documentation",
      "width": 1200,
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

## Generic Debug Draw Data

The following C++ macros and Blueprint [nodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/nodes-in-unreal-engine) record debug draw shapes directly in CVD. Debug draw shapes can offer context when debugging physics calculations.

For example, if you use two points in space to calculate a force applied to a physics body, CVD only shows the body before and after the force is applied. If something looks off, you can use generic debug draw macros (or Blueprint nodes) to visualize the two points, and the force, frame-by-frame. This workflow can provide context on how the force was calculated and help you to correct it.

### C++ Macros

Depending on the shape you need to draw, each macro has its own set of parameters — except for the following optional parameters, which each macro uses:

| Macro | Parameter | Description |
| --- | --- | --- |
| **TraceDebugDrawBox** | **InBox** | The shape you want to record. |
| All macros | **Tag** | The FName that is used as a tag for filtering, search, and debug draw as a text tag in CVD’s viewport. |
| All macros | **Color** | The color to apply to this shape when it’s debug drawn in CVD. |
| All macros | **SolverID** | The ID of the solver this shape should be associated with. If no ID is provided, this shape is added as part of the current game from data bucket. |
| **TraceDebugDrawLine**, **TraceDebugDrawVector** | **InStartLocation** | The start point of the line. |
| **TraceDebugDrawLine** | **InEndLocation** | The end point of the line. |
| **TraceDebugDrawVector** | **InVector** | The vector you want to record. |
| **TraceDebugDrawSphere** | **Center** | The origin point of the sphere. |
| **TraceDebugDrawSphere** | **Radius** | The radius of the sphere. |
| All macros | **Owner** | Any UObject this debug draw shape is related to. This is used internally to know if a shape is recorded from a server solver or a client solver. |

### Blueprint Nodes

The following generic debug draw macros can also be implemented as function nodes in a Blueprint’s **Event Graph:**

- CVD Record Debug Draw Sphere
- CVD Record Debug Draw Box
- CVD Record Debug Draw Line

![Event Graph](https://dev.epicgames.com/community/api/documentation/image/62a34414-91df-4c83-8ff8-5961173e1297)

For more information about each node, see the Chaos Visual Debugger section of [Unreal Engine Blueprint API Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/BlueprintAPI?application_version=5.6).

#### Enable Generic Debug Draw Data

To enable generic debug draw data, follow these steps:

1. In the Viewport Toolbar, click **Show > Generic Debug Draw Data Flags > Enable Draw**. This option opens a list of data flags. ![Generic Debug Draw Data Flags](https://dev.epicgames.com/community/api/documentation/image/a6018ff5-47f1-4a97-a18c-624fc2fbeda8)
2. Choose from the list of data flags to toggle on or off. ![Generic Debug Draw Options](https://dev.epicgames.com/community/api/documentation/image/756db150-83e0-45c0-9977-92190fd2b199)
3. Click **Generic Debug Draw Data Visualization Settings** to customize how the data is drawn in the viewport. ![Generic Debug Draw Data Enabled](https://dev.epicgames.com/community/api/documentation/image/77786f4c-c0f3-4c2d-9b37-41862865dba5)

## Acceleration Structures

CVD can record and visualize acceleration structures used by the scene query system, which is currently an AABB (Axis-Aligned Bounding Box) Tree. An AABB Tree is a bounding volume hierarchy you can use to determine potential overlaps between objects.

In CVD, you can use AABB Tree visualization to see the composition of the tree and the bounds of each object as they were added to the tree.

This visualization is useful when an object that a scene query should have hit wasn’t hit, or wasn’t even evaluated by the physics engine. You can use AABB Tree visualization in CVD to inspect the bounds of the object and determine whether the error was caused by, for example, the bounds failing to encompass the object visually or incorrect bounds within the tree.

To customize which acceleration structure data flags are drawn, follow these steps:

1. In the **Viewport, click Show > Acceleration Structure Data Flags**, and select your desired data flags. ![Acceleration Structure Data Flags](https://dev.epicgames.com/community/api/documentation/image/9a13ca39-2994-4867-b21f-ae3065f639aa)
2. Click **Acceleration Structure Visualization Settings** to customize how the data is drawn in the viewport. ![Acceleration Structure Visualization Settings](https://dev.epicgames.com/community/api/documentation/image/5494ebf5-786f-4931-b178-5fbe4aa850a5)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "CVD doesn’t record acceleration structures by default. To enable it, click the <b>Data Channel</b> dropdown menu in the Main Toolbar, and check <b>Acceleration Structures Data</b>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25947766,
      "caption": "",
      "alt_text": "Enable Acceleration Structure Data Channel",
      "image": {
        "id": 25947766,
        "file_name": "data-channels-not-default (2).png",
        "file_size": 818811,
        "content_type": "image/png",
        "created_at": "2025-08-18T14:56:53.975+00:00",
        "height": 1105,
        "width": 2876,
        "storage_key": "6cc18ae6-9aa9-4c9f-87f0-ed81380d628c",
        "context": "documentation"
      },
      "storage_key": "6cc18ae6-9aa9-4c9f-87f0-ed81380d628c",
      "context": "documentation",
      "width": 1200,
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

## Common Show Flags

The **Common Show Flags** menu contains flags derived from the engine itself that can assist with visibility in CVD.

To customize which flags are enabled, in the Viewport Toolbar, click the **Show > Common Show Flags**.

![Common Show Flags](https://dev.epicgames.com/community/api/documentation/image/aed15348-2a74-4177-a503-f08b51f32c6a)

## Next Up

- [Related Document](en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger.md)

- [Related Document](en-us/unreal-engine/capturing-data-with-chaos-visual-debugger.md)
