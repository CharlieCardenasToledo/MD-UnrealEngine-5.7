# Selecting Actors

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/selecting-actors-in-unreal-engine

> Application Version: 5.7

Selecting Actors, while simple in nature, is an important part of the level-editing process. The ability to quickly and easily select the Actors that you want to work with enhances productivity and speeds up the design process.

This page details the different ways to select Actors in Unreal Engine.

## Simple Selection

The most basic method of selecting Actors is to **left-click** them in the Viewport. Clicking an Actor will deselect any currently selected Actors and select the new one instead. If you hold down the **Ctrl** key while you click a new (unselected) Actor, the new Actor is added to the selection. If you hold down the **Ctrl** key while clicking a selected Actor, the Actor is removed from the selection.

This method is good for selecting small numbers of Actors or several isolated Actors spread out across a Level, but it can be slow and tedious for selecting large numbers of Actors.

![A selected Static Mesh Actor in the Viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d7b37c18-de76-4cae-99d2-1133040feaf3/selected-actor.png)

Selected Actors are highlighted in the Viewport. In this example, the table is selected, as shown by the yellow highlight and the presence of the Transform widget.

When you select multiple Actors, you can transform them as a group, and you can modify their properties simultaneously in the **Details** panel.

When you have two or more Actors selected, you can add them to a group to make it easier to re-select them or change their properties at the same time. For more information, refer to the [Grouping Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/grouping-actors-in-unreal-engine) page.

## Selecting Actors in the World Outliner

The **World Outliner** is a panel in the Unreal Editor that contains a hierarchical tree view of all Actors in the level. By default, it is located at the right-hand side of the Unreal Editor window.

You can select and deselect individual Actors in the list the same way you would in the Viewport.

In addition, you can select multiple Actors in the following ways:

* Click an Actor, then hold down the **Shift** key and click another Actor to select all the Actors between them in the list.

  ![Selecting a range of Actors in the World Outliner](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2b8296f1-47c2-4a25-97a3-9ee1479e16bd/select-actors-shift.gif)
* Hold down the **Ctrl** key and click multiple Actors to select all of them. The Actors don't have to be in sequence.

  ![Selecting multiple Actors in the World Outliner](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4d0cfcb1-9dd7-4cca-aba0-a06b9e67d9a2/select-actors-ctrl.gif)

Selecting any Actor in the **World Outliner** also selects it in the viewport, and vice versa.

## Marquee Selection (Click-And-Drag)

Marquee selection is a quick way to select or deselect a group of Actors within a certain area in the viewport. This type of selection is performed by clicking and dragging the mouse, while optionally holding down a key or key combination. All the Actors within the box will be selected or deselected depending on the combination of keys and mouse button you hold down while dragging the mouse.

![Marquee selection in Unreal Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/86b31a0c-4a94-432a-ba11-efe7f4c613c0/select-marquee.png)
