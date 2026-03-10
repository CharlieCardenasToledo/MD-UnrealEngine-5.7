# Draw Spline

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/draw-spline-tool-in-unreal-engine

> Application Version: 5.7

The **Draw Spline** tool creates splines in the Level Editor. You can use your created splines with the **Revolve Spline** and **Mesh Splines** modeling tools to create meshes, or with custom blueprint actors to create a variety of objects such as rails or vines.

To learn more about other spline workflows, see the following:

* [Blueprint Splines](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-splines-in-unreal-engine)
* [Camera Rig](https://dev.epicgames.com/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine)

You can edit splines outside of the tool by selecting and manipulating points on the spline, right-clicking the spline, or using the **Details** panel.

## Accessing the Tool

You can access the Draw Splines tool from the **Create** category in **Modeling Mode**. To learn more about Modeling Mode and how to access it, see [Modeling Mode Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine).

## Using Draw Spline

To create a spline, follow these steps:

1. Choose an output type for the spline from the **Output Mode** dropdown.
2. Choose how to draw your spline from the **Draw Mode** dropdown.
3. Click or drag in the level to draw your spline.
4. Accept or cancel the changes in the [Tool Confirmation](https://dev.epicgames.com/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine#tools,undohistory,andacceptingchanges) panel.

### Output Mode

**Output Mode** determines how a spline component is created.

| **Output Mode** | **Description** |
| --- | --- |
| **Empty Actor** | Creates an empty actor with a spline component. |
| **Existing Actor** | Attaches the spline component to an existing actor or replaces a spline inside that actor if **Existing Spline Index To Replace** is valid. To choose an existing actor, click the actor before switching the mode or use the eyedropper to choose. |
| **Create Blueprint** | Creates the Blueprint specified by **Blueprint To Create** and attaches the spline to that, or replaces an existing spline in the created object if **Existing Spline Index To Replace** is valid. |

If you are working with a blueprint actor that has an expensive construction script, it can be helpful to turn off **Rerun Construction Script on Drag** under advanced options.

### Draw Mode

To adjust how the spline is drawn in the scene, use the properties in the **Draw Mode** section. You can switch between the modes while creating a spline in the level.

| **Draw Mode** | **Description** | **Example** |
| --- | --- | --- |
| **Tangent Drag** | Draws a spline point by point with manual control over curvature (via tangents). Click to place a point and drag to set its tangent. Clicking without dragging creates sharp corners. | Tangent Drag Draw Mode |
| **Click Auto Tangent** | Draws a spline point by point with curvature automatically set. Click and drag to place new points, with the tangent set automatically. | Click Auto Tangent Draw Mode |
| **Free Draw** | Draws a spline with a freehand motion. Click and drag to place multiple points, with spacing controlled by **Min Point Spacing**. | Free Draw Draw Mode |

To have an open or closed path you can toggle **Loop**. When true, points continue to append to the loop as you draw onto it. To help visualize the path and rotation, increase the **Frame Visualization Width** value.

### Raycast Targets

The **Raycast Targets** section determines how the mouse location interacts with the scene while drawing a spline. You can toggle multiple options at the same time.

You must have at least one option enabled to draw a spline.

| **Raycast Targets** | **Description** | **Example** |
| --- | --- | --- |
| **World** | Splines are drawn on mesh surfaces in the level, except the target mesh when **Existing Actor** is enabled. | World Raycast Target |
| **Custom Plane** | Splines are drawn on a plane that you can reposition with the gizmo or with **Ctrl + Click.** | Custom Plane Raycast Target |
| **Ground Planes** | Splines are drawn on the XY ground plane in the perspective viewport, or on the viewed plane in orthographic viewports. | Ground Plane Raycast Target |

### Hotkeys

| **Hotkey** | **Description** |
| --- | --- |
| **C** | Zooms into the location of the mouse. |
| **Enter** | Accepts tool changes. |
| **ESC** | Cancels the changes and exit the tool. |
