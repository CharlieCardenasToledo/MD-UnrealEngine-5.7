# Property Matrix

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/property-matrix-in-unreal-engine

> Application Version: 5.7

While working in a level with multiple actors, updating individual properties at once can become time-consuming. You can use the **Property Matrix** to complete bulk edits and compare values for large numbers of objects or actors. It displays a configurable set of properties for a collection of objects as columns in a table view. The Property Matrix also provides a standard property editor that displays all properties for the current selection set.

![Propterty Matrix in Unreal Engine](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8734893a-452a-4522-8fbc-bdea22f16f05/ue-5-3-property-matrix-gif.gif)

## Features

| Feature | Benefits |
| --- | --- |
| **Bulk Object Editing** | * Easier workflow for setting a series of varying values to a bunch of objects, without sacrificing the ability to set the property on a bunch of objects to the same value. * Works with thousands of objects at the same time. * Can handle editing a wide variety of object types at the same time. |
| **Bulk Fine-Grain Object Comparison** | * Sort the values on thousands of objects at a time. * Quickly find assets and Actors with incorrect settings. |
| **Deep Property and Array Support** | * Do all of the above with the properties of arrays and struct types. * Can expose columns for any property. * Handles array indices. |

## Accessing the Property Matrix

You can access the Property Matrix by:

* Select the Property Matrix button in the **Details** panel adjacent to the **Search** bar.
* In the **Content Browser**, make a selection of assets, right-click, choose **Asset Actions**, then choose **Edit Selection in Property Matrix** from the context menu.
* In the **Outliner**, right-click your selection, then choose **Edit Selection in Property Matrix** from the context menu.
* In the **Outliner**, right-click your selection, then choose **Edit Components in the Property Matrix** to select any shared component types from the context menu.

## Using the Property Matrix

The Property Matrix is a table that handles data like other grid-based editors. All cells have two modes: Display and Edit. Depending on the current mode, the cells' feature set changes.

### Adding and Removing Columns

You can add and remove columns by pinning and unpinning properties in the **Pinned Columns** panel. The list of properties in the panel is referred to as the property tree.

![Adding Column](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8225b1d-aa46-40cc-a281-dbd5e2db951f/pinning-column.png)
