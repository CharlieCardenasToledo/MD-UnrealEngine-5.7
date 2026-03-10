# Manage Items and Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-05-manage-item-and-data-in-an-unreal-engine-game

> Application Version: 5.7

## Before You Begin

To start this tutorial, you need an Unreal Engine Project with C++ classes.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "This page continues from <a data-document-id=\"3948432\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation\">Add a First-Person Camera, Mesh, and Animation</a>; however, you can complete this independently of the rest of the <a data-document-id=\"3947837\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine\">Code a First-Person Adventure Game</a> tutorial series if you'd just like to learn about data-driven gameplay.  ",
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

## Data Organization in Games

How you organize and represent data is an important part of game design. Interactable items could have very different qualities and can exist in game or just as a piece of data. You could represent this data by creating separate classes and Blueprints for each item type, distributing and communicating data across different Actors. However, this gets inefficient as your game and the amount of stored data grows.

A better approach is **data-driven gameplay**. Instead of hardcoding values, you'll organize data in a centralized location managed by systems in your game. Data-driven gameplay lets you load what you need when you need it. For example, many games use spreadsheet documents to organize dialogue as it's easier for a system to pull a specific line of dialogue instead of storing potentially hundreds of lines in each character.

In this section, you’ll learn how use this methodology to start creating custom items.

### Data-Driven Gameplay Elements

Before you start building basic items, it’s important to consider what defines an “item”. Since an item can be anything a player interacts with, it should have a minimal set of properties that are valid for any type of item. You’ll set this up in an **Item Data Struct**. You should also have a centralized place to organize and display this item data. For that, you’ll use a **Data Table** asset.

Your Item Data Struct acts as a template that defines the type of data your item has, then your Data Table and **Data Assets** store the actual data entries based on your struct. Data Assets also make it easier to inspect individual items and provide a natural extension point as item behavior becomes more complex.

The diagram below shows the four data-driven gameplay elements you’ll create in this part of the tutorial. Once you’ve finished setting up all four elements, you’ll revisit this diagram in more detail to help summarize what you’ve built.

![Image](https://dev.epicgames.com/community/api/documentation/image/a49fe57e-0a2b-4c42-815f-eb9fc9606d1d)

First, you’ll create two files to define your item data:

- `ItemData.h`: A container for the Item Data Struct (`FItemData`) declaration.
- `ItemDefinition.h`: A class that inherits from `UDataAsset` so your item data can be used in Unreal Editor.

The Item Data Struct doesn’t inherit from `UObject` and can’t be instantiated in a level, so you also need the Data Asset class to use and reference in the editor.

Then, in Unreal Editor, you’ll create a Data Table and a Data Asset Instance based on `ItemDefinition`.

## Define Your Item Data

Your Item Data Struct defines the data or properties each item in the Data Table should have, acting like the table's columns.

Your Item Data Struct will have the following properties:

- **ID**: A unique name for the item, useful when referencing table rows later.
- **Item Type**: The type of this item (in this case, you’ll define Tool and Consumable types).
- **Item Text**: Textual data about the item, including a name and description.
- **Item Base**: The ItemDefinition Data Asset associated with this item.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you want to create your own table fields (columns), keep in mind that Data Table fields can be any types that are compatible with <code class=\"inline-code\">UPROPERTY()</code>.",
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

### Create a Header File Container for the Struct

First, set up a new folder and new header (`.h`) file to store your Item Data Struct definition.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You could create the <code class=\"inline-code\">FItemData</code> struct within <code class=\"inline-code\">ItemDefinition.h</code>, but putting the struct in a separate file helps organize your data elements and allows for reuse.",
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

To set up a header file as a container for your Item Data Struct, follow these steps:

1. In Unreal Editor, go to **Tools** > **New C++ Class**.
2. In the **Choose Parent Class** window, select **None** as the parent class, then click **Next**.
3. Next to **Path**, click the folder icon. In your `Source/[ProjectName]` folder, go into the `Public` folder, and create a new folder named `Data` to store this class. ![Image](https://dev.epicgames.com/community/api/documentation/image/42270355-d59a-4498-b9ae-caf6d72a9101)
4. Name the class `ItemData` and click **Create Class**.
5. If Unreal Engine doesn't open your new class files automatically, open your project and `ItemData.h` in Visual Studio.
6. Delete all text in `ItemData.cpp`, then save and close the file. You won't be using it.
7. In `ItemData.h`, delete everything under the `#include “CoreMinimal.h”` line.
8. In `ItemData.h`, add the following include statements: `#include “Engine/DataTable.h”`: Required to have your struct inherit from `FTableRowBase`. `#include “ItemData.generated.h”`: Required by Unreal Header Tool. Make sure this include statement comes last for your code to compile properly.
9. Add a forward declaration for a class named `UItemDefinition`. This will be the Data Asset that you can work with in the editor.

### Define Item Properties

There's no existing variable types for an item type and text data, so you'll need to define these.

You'll create two properties:

- An enum that lists all possible item types. In this tutorial, you’ll create Tool and Consumable-type items.
- A struct that lists item properties (a name and a description).

To define an Item Type enum, follow these steps:

1. In `ItemData.h`, after the `#include` statements, define an `enum class` named `EItemType` and give it type `uint8`. Add the `UENUM()` macro above it with a `BlueprintType` specifier to declare this enum to Unreal Header Tool and expose it as data inside Blueprints, allowing it to appear in Data Tables.
2. Add two custom values to this enum: `Tool`, adding a `UMETA()` macro with `DisplayName = “Tool”` `Consumable`, adding a `UMETA()` macro with `DisplayName = “Consumable”`

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "These item types are custom and not built into Unreal Engine; so once you’ve learned the basics, you can make anything you like! (Perhaps a <code class=\"inline-code\">QuestItem</code>, <code class=\"inline-code\">Currency</code>, or <code class=\"inline-code\">Disguise</code>?)  ",
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

To define an Item Text struct, follow these steps:

1. After `EItemType`, create a new struct named `FItemText` with a `USTRUCT()` macro containing `BlueprintType`. This struct holds textual data about your item.
2. Inside `FItemText`, add the `GENERATED_BODY()` macro.
3. Then, add two `FText` properties named `Name` and `Description` to store the name and description for this item. Add the `UPROPERTY()` macro to each with `EditAnywhere` and `BlueprintReadOnly` as the arguments.

### Create the Item Data Struct

Now that you’ve added those prerequisite declarations, create the Item Data Struct with your item’s properties inside. These properties become the fields in your Data Table.

To define your data table's structure, follow these steps:

1. Below `FItemText`'s definition, define a struct named `FItemData` that inherits from `FTableRowBase`. Add the `public` specifier to make it visible anywhere and add `GENERATED_BODY()` for Unreal Header Tool.
2. In the `FItemData` struct, add the following declarations: An `FName` named `ID`. Each row in a Data Table needs an associated `FName` to reference. An `EItemType enum` named `ItemType`. This is the enum of item types you declared earlier. An `FItemText` struct named `ItemText`. This is the struct of text data you declared earlier.
3. Add the `UPROPERTY()` macro to each declaration with `EditAnywhere` , `BlueprintReadOnly`, and `Category = “Item Data”` arguments.
4. Declare a `TSoftObjectPtr` to a `UItemDefinition` named `ItemBase`. Give it the same `UPROPERTY` macro as the other properties in the struct. In the next step, you’ll create a `UDataAsset` class named `ItemDefinition`. In your Data Table, you’ll use the `ItemBase` field to reference `ItemDefinition Data Asset` instances.
5. Save your code. Don't compile yet, your code won't build until you've created `ItemDefinition`.

`ItemData.h` should now look like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;Engine/DataTable.h&quot;\n#include &quot;ItemData.generated.h&quot;\n\nclass UItemDefinition;    // NEW put this back\n\n",
  "lines_of_code": 58,
  "id": 162570,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjI1NzAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyOCswMDowMCJ9--08e1cd7d90bbe0c31a7799e45f76d974d5d23f3af94ae1280970cb1d1eb6257c",
  "settings": {
    "is_hidden": false
  }
}
```

## Build an Item Definition DataAsset

So far, you’ve defined your item data, or the type of data that appears in your Data Table. Next, you’ll implement the `UItemDefinition` class that you'll use to make Data Assets in Unreal Editor.

This class inherits from `UDataAsset` and therefore is a `UObject`, meaning you can create and use instances of it directly in the editor without going through code.

To create your `ItemDefinition` DataAsset class (`ItemDefinition.h`), follow these steps:

1. In Unreal Editor, go to **Tools** > **New C++ Class**.
2. In the **Choose Parent Class** window, click **All Classes**.
3. Search for and select **DataAsset** as the parent class, then click **Next**. ![Image](https://dev.epicgames.com/community/api/documentation/image/1ea4a5f0-07d6-483f-bc33-eef612f9f369)
4. Name the class `ItemDefinition` and click **Create Class**.

VS should automatically open your new class’ `.h` and `.cpp` files. If not, refresh VS and open the files manually. You’ll just be working in the `.h` file, so you can close the `.cpp` file.

To set up `ItemDefinition.h`, follow these steps:

1. In `ItemDefinition.h`, add an include for `ItemData.h` because you’ll want to re-use the `ItemType` and `ItemText` properties you declared in that file.
2. In the `UCLASS()` macro above the class definition, add `BlueprintType` and `Blueprintable` specifiers to expose this as a base class for creating Blueprints.
3. In the class definition, add a `public` section if one doesn't exist already.
4. In the `public` section, copy the `FName ID`, `EItemType ItemType`, and `FItemText ItemText` declarations from `ItemData.h`. Your item definition gets the same data as the `FItemData` struct so you don’t need to reference the original table when you want to get information about the item.
5. After `ItemText`, declare a `TSoftObjectPtr` of type `UStaticMesh` named `WorldMesh`. You’ll use this static mesh to display this item in the world. Add the same `UPROPERTY(EditAnywhere, Category = “Item Data”)` macro to this property.
6. Save your code and compile it from Visual Studio.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Data Table rows are similar to CSV rows, meant for holding textual data and not storing full assets. To optimize data management, we recommend bundling information like an item’s mesh, material, and animations in a DataAsset as this is the central place where all data about one particular item lives. So, the item’s static mesh property is here in <code class=\"inline-code\">UItemDefinition</code> instead of in the <code class=\"inline-code\">FItemData</code> struct. ",
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

Your complete `ItemDefinition.h` should now look like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;Engine/DataAsset.h&quot;\n#include &quot;Data/ItemData.h&quot;\n#include &quot;ItemDefinition.generated.h&quot;\n\n// Defines an item definition built from data table data.\n",
  "lines_of_code": 29,
  "id": 162575,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjI1NzUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyOCswMDowMCJ9--59f2bfef9d10d78950ae0184650df4288a3a13c9c5f25cc27c17cf54e7b22e47",
  "settings": {
    "is_hidden": false
  }
}
```

## Create a Data Asset Instance

With your item data (`FItemData` struct from `ItemData.h`) and item definition (`UItemDefinition` class) defined, you’ve got all the pieces you need to build your item instances and Data Table.

First create a Data Asset for a new projectile pickup item, then create a Data Table and populate it with your Data Asset’s information.

To create a Data Asset item from your `ItemDefinition` class, follow these steps:

1. In the **Content Browser**, go to the **Content** > **FirstPerson** folder, click **Add** or right-click a blank area in the **Asset View**, select **New Folder**, and name it `Data`. ![Image](https://dev.epicgames.com/community/api/documentation/image/51f47856-7bd1-4dfc-a48e-3cd0bc33890a) This is where you’ll store and organize data assets in your game.
2. In the `Data` folder, click **Add** or right-click a blank area in the Asset View and select **Miscellaneous** > **Data Asset**. ![Image](https://dev.epicgames.com/community/api/documentation/image/db810f37-57d5-4ec0-8281-2cc173c48999)
3. In the **Pick Class For Data Asset Instance** window, select **Item Definition** (the C++ class you defined earlier), then click **Select**. Name the new Data Asset `DA_Pickup_001`. ![Image](https://dev.epicgames.com/community/api/documentation/image/b70ba099-ceab-4fcd-98d8-5f53267f01e9)
4. Double-click `DA_Pickup_001` to open it. In its **Details** panel, you’ll see all the properties you defined in `ItemDefinition.h`.
5. Enter `pickup_001` as the **ID**. ![Image](https://dev.epicgames.com/community/api/documentation/image/870c5636-1d2b-4797-9665-97438240e46c)
6. Set the **Item Type** to **Consumable**.
7. Expand **Item Text** and enter a **Name**and **Description**.
8. Set the **World Mesh** to `SM_FoamBullet`.
9. Click **Save** near the top-left corner of the window to save your Data Asset.

## Define A Data Table

Now that you have at least one Data Asset to populate a Data Table with, you can create the table!

Each row in the Data Table is one filled-in instance of your ItemData struct.

To create a Data Table, follow these steps:

1. In the **Content Browser**, in your `Data` folder, right-click a blank area and select **Miscellaneous** > **Data Table**.
2. In the **Pick Row Structure** window, select **ItemData** (the `FItemData` struct you defined in `ItemData.h`), then click **OK**. ![Image](https://dev.epicgames.com/community/api/documentation/image/e0bd866e-4f2b-4472-97b4-6fe2f7f08f07)
3. Name the new table `DT_PickupData`, then double-click it to open it.

Your Data Table is empty initially. However, you’ll see the properties you defined in `FItemData` as headings at the top of the table, and an additional column named **Row Name**.

To add your pickup item Data Asset as a row in the table, follow these steps:

1. In the toolbar near the top of the window, click **Add** to add a new row to your table. The Data Table editor lists row entries in the top-left panel in the Data Table tab.
2. Double-click the `NewRow` row name and change it to `pickup_001` (the ID of your Data Asset). ![Image](https://dev.epicgames.com/community/api/documentation/image/6aa53fd6-027f-4b5e-83d4-32910f860116)
3. In the **Row Editor** panel, enter the same values you set in the `DA_Pickup_001` Data Asset into the **ID**, **Item Type**, and **Item Text** fields. ![Image](https://dev.epicgames.com/community/api/documentation/image/09413174-7e62-4c83-b49d-535259bcea83)
4. Set the **Item Base** to your `DA_Pickup_001` Data Asset.
5. Save your Data Table.

And that’s it! Take a look at the diagram of Data-Driven Gameplay elements you’ve created in this step again and see how they’re all connected:

![Image](https://dev.epicgames.com/community/api/documentation/image/bbdf679a-71b0-45c1-a22e-8b9d5ea85373)

You’ve created a Data Table that gets its columns from your `FItemData` struct. You populated the table with a row that contains the data from the Consumable-type `ItemDefinition` Data Asset instance you’ve created and used the `ItemBase` pointer to reference the Data Asset itself. Last, your Data Asset instance got its properties from the parent `UItemDefinition` Data Asset class you created.

## Next Up

In the next section, you’ll learn how to extend this item definition to create a custom pickup class and instantiate it in your level.

- [Related Document](en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine.md)

## Complete Code

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "ItemData.h",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;Engine/DataTable.h&quot;\n#include &quot;ItemData.generated.h&quot;\n\nclass UItemDefinition;   \n\n",
  "lines_of_code": 54,
  "id": 162576,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjI1NzYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyOCswMDowMCJ9--e629107b3d8b6e61291fe9a6cfe25d8827b554a119a48d8d03490c1e2fe8b7dc",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "ItemDefinition.h",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;Engine/DataAsset.h&quot;\n#include &quot;Data/ItemData.h&quot;\n#include &quot;ItemDefinition.generated.h&quot;\n\n// Defines an item definition built from data table data.\n",
  "lines_of_code": 29,
  "id": 162577,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjI1NzcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyOCswMDowMCJ9--bb15624aa071a3fc85d94f3d2bba80a0876341313831e05c482bade9bf6fed1c",
  "settings": {
    "is_hidden": false
  }
}
```
