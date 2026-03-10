# Mirroring Animation

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mirroring-animation-in-unreal-engine

> Application Version: 5.7

Animation mirroring copies animation from one side of a character to another so you can reuse the same animation in different situations. Using the **Mirror Data Table**, and other mirroring workflows, you can mirror not only your Animation Sequences, but also curves, sync markers, and Notifies. Additionally, mirroring within Unreal Engine provides a way to create mirrored animations without needing to manage a second copy.

This document provides an overview of how to mirror animation using the Mirror Data Table and Animation Blueprints.

#### Prerequisites

* Your project already contains a [Skeletal Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-actors-in-unreal-engine) and [animations](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine) to mirror.
* You have an understanding of how to create and use [Animation Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine).

## Mirror Data Table

To start mirroring animations, you must first create a **Mirror Data Table** Asset. Mirror Data Tables provide mirroring assignments and instructions for all the elements of a Skeleton you want to mirror.

To create it, click **Add (+)** in the Content Browser and select **Animation > Mirror Data Table**. A dialog window will appear where you must select the Skeleton you want to mirror. Select one and click **Accept**.

![create mirror data table](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c7c9c5b5-700f-4ce5-8d17-ea516019a690/table1.png)

Open the Mirror Data Table to view the editor with the following primary areas:

![mirror data table editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9746fe73-0b5a-4a38-bc7c-d14c9dd81a5a/table2.png)

1. **Data Table**, which contains the list of elements to mirror. This list auto-populates depending on the bone, notify, and other element names, which you can configure in the [Data Table Details](https://dev.epicgames.com/documentation/en-us/unreal-engine/mirroring-animation-in-unreal-engine#datatabledetails).
2. [**Data Table Details**](https://dev.epicgames.com/documentation/en-us/unreal-engine/mirroring-animation-in-unreal-engine#datatabledetails), which contains configuration settings for the mirroring behavior.
3. **Row Editor**, which provides settings for the selected entry where you can edit the element name, the mirrored name, and the element type.

### Adding and Editing Entries

To add a new table entry, click the **Add (+)** toolbar button and fill the four properties in the **Row Editor** panel.

* **Row Name**, which is the name of the entry.
* **Name**, which is the name of the first bone to mirror.
* **Mirrored Name**, which is the name of the second bone to mirror. Left or right bones can go in either of these properties, but these properties must contain the symmetrical bones.
* **Mirror Entry Type**, which is the element type to mirror. You can select the following types:
  + Bone
  + [Animation Notify](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-notifies-in-unreal-engine)
  + [Curve](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curves-in-unreal-engine)
  + [Sync Marker](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-notifies-in-unreal-engine#addsyncmarker...)
  + Custom, which provides a code foundation for extending the Mirror Data Table in C++ by adding additional types.

![add mirror entry](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/51649a42-730d-4f04-9285-0ed8456240ab/table3.png)


In order to have a fully mirrored character, it is necessary that the table contains most skinned bones, including central bones like **pelvis**, **spine**, **neck**, and **head**. This is so that the mirroring operation can appropriately flip the rotations of those bones along the mirror axis. For these entries, both the **Name** and **Mirrored Name** should match.

![mirror central bones](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/43f85064-4f2b-4a85-8afd-dded882c9512/table4.png)

### Data Table Details

The Data Table Details panel contains configurations and other settings for the mirror behavior:

![data table details](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0c60b30e-7ab2-4919-a6d0-844f1780cd5e/table5.png)

| Name | Descriptions |
| --- | --- |
| **Mirror Find Replace Expressions** | An array of expressions that are used to automatically populate the table with common mirror entries. Refer to the [Find and Replace Expressions](https://dev.epicgames.com/documentation/en-us/unreal-engine/mirroring-animation-in-unreal-engine#findandreplaceexpressions) section for more information. |
| **Mirror Axis** | The axis of mirroring, which is across the front of the character. In most cases this should be **X**. mirror axis |
| **Skeleton** | The Skeleton Asset to use for the mirror operation. |
| **Row Struct** | The structure to use for each row of the table. You must inherit from `FTableRowBase` if you want to extend this. |
| **Strip from Client Builds** | Enabling this will not cook this Data Table into client builds. Useful if you are making confidential tables that only servers should know about. |

### Find and Replace Expressions

**Find** and **Replace Expressions** are array entries you can add to the Data Table Details that automatically search and replace certain string text of elements in the skeleton. These expressions are then used to inform which elements are automatically populated when creating or reimporting the skeleton.

![find and replace expression properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c875758-dde6-4c58-affc-f24cb584fd9e/expression1.png)
