# Equip Your Character

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools

> Application Version: 5.7

## Before You Begin

Ensure you’ve completed the following objectives in the previous sections of [Code a First-Person Adventure Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine):

- Built a C++ first-person player character in [Create a Player Character With Input Actions](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-02-create-a-player-character-with-input-actions-in-cplusplus).
- Set up data-driven gameplay elements to manage item data in [Manage Items and Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-05-manage-item-and-data-in-an-unreal-engine-game).
- Created a pickup item and added it to your level in [Create a Respawning Pickup Item](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine).

### Create Reference Items With a New CreateItemCopy Function

Before you start creating a new equippable pickup item, you’ll first need to modify your **ItemDefinition** and **PickupBase** classes to support capturing a reference item from a wider variety of item types.

In the `InitializePickup()` function in your `PickupBase` class, you set a `ReferenceItem` of type `UItemDefinition`. This is too restrictive; setting a reference item this way won’t include the additional properties you’ll add to any new, specialized item classes derived from `UItemDefinition`.

To solve this, you’ll create a new virtual function in `ItemDefinition` that creates and returns a copy of that item. Because it’s a virtual function, you can override it in any classes that inherit from `UItemDefinition`. When `PickupBase` calls the function, the compiler determines the correct function to call based on the class it was called from.

Adding this function to the parent `ItemDefinition` class ensures it’s available if you decide to continue extending your project to include more item types that inherit from `UItemDefinition`.

To define a new `CreateItemCopy()` function for creating reference items, follow these steps:

1. Open `ItemDefinition.h`. In the `public` section, declare a new virtual const function named `CreateItemCopy()` that returns a `UItemDefinition` pointer. The function should take a `UObject` pointer named `Outer` so you can tell Unreal Engine what object owns the copy.
2. In `ItemDefinition.cpp`, add a function signature for the `CreateItemCopy()` function.
3. Inside the function, create a new `UItemDefinition` object pointer named `ItemCopy`, passing `Outer` as the owner. Inside,
4. Assign each field of `ItemCopy` to this class’s fields and then return `ItemCopy`:

Next, refactor your `InitializePickup()` function by removing the code that manually sets up `ReferenceItem` and replace that code with a `CreateItemCopy()` call.

To update `InitializePickup()` with your new `CreateItemCopy()` function, follow these steps:

1. Open `PickupBase.cpp` and go to `InitializePickup()`.
2. Delete these five lines that define and set `ReferenceItem`:
3. Set `ReferenceItem` by calling `TempItemDefinition->CreateItemCopy()`:

Save `PickupBase.cpp`. Your `InitializePickup()` function should now look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Initializes the pickup with values retrieved from the associated data table.\nvoid APickupBase::InitializePickup()\n{\n\t// Only initialize if the pickup has valid inputs \n\tconst FSoftObjectPath TablePath = PickupDataTable.ToSoftObjectPath();\n\tif (!TablePath.IsNull() &amp;&amp; !PickupItemID.IsNone())\n\t{\n\t\t/* Resolve the table soft reference into a usable data table.\n\t\t   Use the loaded table if available; otherwise load it now. */\n\t\tUDataTable* LoadedDataTable = PickupDataTable.IsValid()\n",
  "lines_of_code": 63,
  "id": 163360,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMzNjAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--f1b60e09407c73b6ac3d15b5f86423ec102ec2b3feeaeda108b16220bc903e1c",
  "settings": {
    "is_hidden": false
  }
}
```

## Define Equippable Tool Data

In the previous section, you learned how to create interactable pickup objects in your level that are concrete representations of table data. In this section, you’ll learn how to build tools for your character to equip.

To set up a new equippable tool, you’ll create:

- `EquippableToolDefinition`: A Data Asset class derived from `ItemDefinition` that stores the tool’s data.
- `EquippableToolBase`: An Actor class to represent the tool in-game. It gives your character the animations, input mappings, and mesh so the character can hold and operate the tool.

To make your character able to pick up and equip tools, you’ll add:

- A place to store items.
- A way to know the type of each item in their inventory.
- A way to equip tools.

Remember, the `EquippableToolBase` actor represents the tool your character is holding and using, while the `PickupBase` actor represents the pickup item in your level. Your character has to collide with the pickup item before it can equip it, so you’ll also modify `PickupBase` to grant the item to the character after a successful collision.

Then, you’ll combine your new tool class with the pickups and Data Table you’ve already built to create a custom dart launcher and attach it to your character!

First, you’ll define your tool’s data in a new `ItemDefinition` class.

To create a new `EquippableToolDefinition` class, follow these steps:

1. In Unreal Editor, go to **Tools > New C++ Class**. Go to **All Classes**, search for and select **ItemDefinition** as the parent class, and click **Next**. ![Image](https://dev.epicgames.com/community/api/documentation/image/e9057eb5-03ce-440a-a632-e723a9900d6f)
2. Name the class `EquippableToolDefinition` and click **Create Class**.
3. In Visual Studio, at the top of `EquippableToolDefinition.h`, ensure there's an include for `”ItemDefinition.h”`, then add the following forward declarations: `class UInputMappingContext`: Each equippable tool should hold a reference to an Input Mapping Context that you’ll apply to the character wielding that tool. `class AEquippableToolBase`: The Actor representing your tools in-game. You’ll create this in the next step.
4. In the `public` section, add a `TSubclassOf` property of type `AEquippableToolBase` named `ToolAsset`. Give this a `UPROPERTY()` macro with `EditDefaultsOnly` and `BlueprintReadOnly`. `TSubclassOf<AEquippableToolBase>` is a template wrapper around `UClass` that enables you to reference Blueprint subclasses of `AEquippableToolBase` while ensuring type safety. It’s useful in gameplay scenarios where you want to spawn different types of actors dynamically. You’ll use `ToolAsset` to dynamically spawn a tool actor when it gets equipped to your character.
5. Declare an override for the `CreateItemCopy()` function you declared in `UItemDefinition`. This override creates and returns a copy of the `UEquippableToolDefinition` class. Your complete `EquippableToolDefinition.h` file should look like the following:
6. In `EquippableToolDefinition.cpp`, add a function definition header for `CreateItemCopy()`.
7. Add an `if` statement to check if the Outer is null. If it is null and a fallback Outer is needed, copy the item with `GetTransientPackage()` as the Outer. `GetTransientPackage()` returns an engine-owned UPackage that is never saved to disk and lives for the lifetime of the editor or game session, so it's a good backup Outer for temporary UObjects.
8. Return a `DuplicateObject<T>(ExistingObject, Outer)` call to clone the equippable item definition asset and return the copy.
9. Save both `EquippableToolDefinition` class files. The code won't compile until you create `EquippableToolBase`.

## Set Up an Equippable Tool Actor

Next, start building your equippable tool Actor. This is the in-game representation that adds the tool’s animations, controls, and mesh to the character.

To create and set up a new base equippable tool Actor, follow these steps:

1. In Unreal Editor, go to **Tools > New C++ Class**. Select **Actor** as the parent class and name the class **EquippableToolBase**.
2. Click **Create Class**. Unreal Engine automatically opens your new class’ files in VS.
3. At the top of `EquippableToolBase.h`, forward declare class `AAdventureCharacter`, `UInputAction`, and `UInputMappingContext`. The equippable tool needs to know what Character it's equipped to so it can bind tool-specific Input Actions to that Character.
4. In `EquippableToolBase.h`, add an `#include` for `EnhancedInputSubsystems.h`, `Animation/AnimBlueprint.h`, and `Components/SkeletalMeshComponent.h`.
5. In the class declaration’s `UCLASS` macro, add the `BlueprintType` and `Blueprintable` specifiers to expose this class to Blueprints.
6. In `EquippableToolBase.cpp`, add an `#include` for `AdventureCharacter.h`. and `InputMappingContext.h`.

### Declare Tool Animations

In `EquippableToolBase.h`, in the `public` section, add two `TObjectPtr` to `UAnimBlueprint` properties named `FirstPersonToolAnim` and `ThirdPersonToolAnim`. These are the first-person and third-person animations that the character uses when equipped with this tool.

Give these properties a `UPROPERTY()` macro with `EditAnywhere`and `BlueprintReadOnly`.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "public:\t\n\t// Sets default values for this actor&#39;s properties\n\tAEquippableToolBase();\n\n\t// --- New Code Start --- \n\t// First Person animations\n\tUPROPERTY(EditAnywhere, BlueprintReadOnly)\n\tTObjectPtr&lt;UAnimBlueprint&gt; FirstPersonToolAnim;\n\n\t// Third Person animations\n",
  "lines_of_code": 13,
  "id": 163369,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMzNjksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--232fc68a996da3baf33de770cc73d43b7fa5a9d1ff4e000368acfa2e577aab0d",
  "settings": {
    "is_hidden": false
  }
}
```

### Create the Tool’s Mesh

To declare and set up a mesh component for equippable tools, follow these steps:

1. In `EquippableToolBase.h`, in the `public` section, add a `TObjectPtr` to a `USkeletalMeshComponent` named `ToolMeshComponent`. This is the tool’s skeletal mesh that the character sees when equipped. Give it a `UPROPERTY()` macro with `EditAnywhere` and `BlueprintReadOnly`.
2. In `EquippableToolBase.cpp`, modify the `AEquippableToolBase()` constructor function to create a default `USkeletalMeshComponent` and assign it to `ToolMeshComponent`. Then check if the `ToolMeshComponent` is not null to make sure your tool has a model when it's loaded.

### Declaring the Tool’s Owner

In `EquippableToolBase.h`, in the `public` section, create a `TObjectPtr` to an instance of your Character class named `OwningCharacter`. Give it a `UPROPERTY()` macro with `EditAnywhere` and `BlueprintReadOnly`.

This is the character this tool is currently equipped to.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// The character holding this tool\nUPROPERTY(EditAnywhere, BlueprintReadOnly)\nTObjectPtr&lt;AAdventureCharacter&gt; OwningCharacter;",
  "lines_of_code": 3,
  "id": 163372,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMzNzIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--58b18c17859b016dcbb5d340db5cfd12d4a4e66193021801f091f08a5b3b07fa",
  "settings": {
    "is_hidden": false
  }
}
```

### Declare Input and a Use-Tool Function

Your tool comes with an Input Mapping Context and Input Action that it needs to give the character.

To set up the tool's controls, follow these steps:

1. To add the Input Mapping Context, in the `public` section, declare a `TObjectPtr` to a `UInputMappingContext` named `ToolMappingContext`. Give it a `UPROPERTY()` macro with `EditAnywhere` and `BlueprintReadOnly`.
2. Similar to when you implemented movement controls, you’ll add a function that implements a use-tool action and a new function that binds an input action to the function. In `EquippableToolBase.h`, in the `public` section, declare two virtual void functions named `Use()` and `BindInputAction()`. The `BindInputAction()` function takes a const `UInputAction` pointer and binds the given input action to the character’s `Use()` function. When you implemented character movement controls, you used the InputComponent’s `BindAction()` function that requires you to pass the exact name of the target function. You don’t know the full name of the function yet, so you need a custom `BindInputAction()` function that you can implement in each `EquippableToolBase` subclass to call `BindAction`, passing `[ToolChildClass]::Use`.
3. In `EquippableToolBase.cpp`, add function definition headers for the `Use()` and `BindInputAction()` functions. These won’t do anything in the parent class, so you can leave them blank for now. You’ll add logic to these when creating `EquippableToolBase` subclasses; for example, the `Use()` function should include tool-specific actions such as launching a projectile or opening a door.
4. Save your code and compile it from VS.

Your `EquippableToolBase.h` file should now look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;GameFramework/Actor.h&quot;\n#include &quot;EnhancedInputSubsystems.h&quot;     \n#include &quot;Animation/AnimBlueprint.h&quot;\n#include &quot;Components/SkeletalMeshComponent.h&quot;\n#include &quot;EquippableToolBase.generated.h&quot;\n",
  "lines_of_code": 61,
  "id": 163376,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMzNzYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--145735bddad5d1c8d787a4f47967364fcb17ccc9792210ede3cd6feed97bfa77",
  "settings": {
    "is_hidden": false
  }
}
```

`EquippableToolBase.cpp` should now look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#include &quot;EquippableToolBase.h&quot;\n#include &quot;InputMappingContext.h&quot;\n#include &quot;AdventureCharacter.h&quot;\n\n// Sets default values\nAEquippableToolBase::AEquippableToolBase()\n{\n \t// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n",
  "lines_of_code": 41,
  "id": 163377,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMzNzcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--084a9c34b55b2cc8ed76dcccc74e753a261efe4b183180017b77f18bf01ae623",
  "settings": {
    "is_hidden": false
  }
}
```

## Grant Items to a Character

You’ve defined tools your character can use, but they can't equip them yet. Next, you'll add an inventory system so the character can store and equip items when picking them up.

### Build an Inventory Component

Your character’s inventory should add functionality to the character but not exist in the game world, so you’ll use an **Actor Components** class to define an inventory that knows what items a character has, can swap tools, and can prevent the character from obtaining more than one of the same tool.

To create an inventory component for the character, follow these steps:

1. In Unreal Editor, go to **Tools > New C++ Class**. Select **Actor Component** as the parent class and name the class `InventoryComponent`. Click **Create Class**. ![Image](https://dev.epicgames.com/community/api/documentation/image/abfd6b28-4096-433a-b82c-1040ff25e0d6)
2. In VS, at the top of `InventoryComponent.h`, forward declare a `UEquippableToolDefinition`. This is the class you’ll be storing in your inventory.
3. In the `public` section, declare a new `TArray` of `UEquippableToolDefinition` pointers named `ToolInventory`. Give this the `UPROPERTY()` macro with `VisibleAnywhere`, `BlueprintReadOnly`, and `Category = "Tools"`. This inventory only stores tools, but you can expand this to include any type of item you want. A more generic implementation would store only `UItemDefinition` or `TSubclassOf<UItemDefinition>` values to build a more complex inventory with UI, icons, sound effects, cost, and other item properties.

Your complete `InventoryComponent.h` file should now look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;Components/ActorComponent.h&quot;\n#include &quot;InventoryComponent.generated.h&quot;\n\nclass UEquippableToolDefinition;\n\n",
  "lines_of_code": 33,
  "id": 163380,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMzODAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--9e62350251c514dd6fba9042752ade14c66cd0acf18939fddac0d546bddcc00b",
  "settings": {
    "is_hidden": false
  }
}
```

### Add Tool and Inventory Declarations to the Character

Now that you have a place to store your items, you’re ready to upgrade your character with logic that grants them items.

To add tool and inventory forward declarations and `#include` statements to your character class, follow these steps:

1. To start, at the top of your character’s `.h` file, forward declare the `UItemDefinition`, `AEquippableToolBase`, `UEquippableToolDefinition`, and `UInventoryComponent` classes.
2. At the top of your character's `.cpp` file, add an `#include` for `EquippableToolDefinition`, `InventoryComponent.h`, and `EquippableToolBase.h`.

### Create the Character’s Inventory Component

In the character’s `.h` file, in the `public` section, declare a `TObjectPtr` to a `UInventoryComponent` named `InventoryComponent`. Give it a `UPROPERTY()` macro with `VisibleAnywhere` and `Category = "Inventory"`.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Inventory Component\nUPROPERTY(VisibleAnywhere, Category = &quot;Inventory&quot;)\nTObjectPtr&lt;UInventoryComponent&gt; InventoryComponent;",
  "lines_of_code": 3,
  "id": 163383,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMzODMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--970d8ce8ea3905ea087e690af52649134cf01997448dfd990ee7122f06027f91",
  "settings": {
    "is_hidden": false
  }
}
```

In your character’s `.cpp` file, in the constructor function, after you create the Mesh Component subobject, create a default `UInventoryComponent` subobject named `InventoryComponent`. This ensures your inventory is set up properly when the Character spawns.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Sets default values\nAAdventureCharacter::AAdventureCharacter()\n{\n\t// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it\n\tPrimaryActorTick.bCanEverTick = true;\n\n\t// COMPONENT CREATION\n\t\t// Create a first-person camera component\n\t\tFirstPersonCameraComponent = CreateDefaultSubobject&lt;UCameraComponent&gt;(TEXT(&quot;FirstPersonCamera&quot;));\n\t\tcheck(FirstPersonCameraComponent != nullptr);\n",
  "lines_of_code": 19,
  "id": 163384,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMzODQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--1c41a8b9e994dccfa90e6779891c9309ccba24b074ea74f9d9cb547514260ccf",
  "settings": {
    "is_hidden": false
  }
}
```

### Check Existing Inventory

Before you attach the tool, check if the player already has the tool so you don’t equip it multiple times.

To check if the tool is already owned, follow these steps:

1. In the character’s `.h` file, in the `public` section, declare a function named `IsToolAlreadyOwned()` that takes a `UEquippableToolDefinition` pointer and returns true if that tool already exists in the player’s inventory.
2. In your character’s `.cpp` file `AdventureCharacter.cpp`, implement the `IsToolAlreadyOwned()` function. Inside, in a `for` loop, get each tool in the character’s inventory by accessing the `InventoryComponent->ToolInventory` array.
3. In an `if` statement, check if the `ToolDefinition->ID` from the tool passed to this function matches the `InventoryItem->ID`. If so, `return true` since the character already owns this tool. Otherwise, after the `for` loop, `return false` because `ToolDefinition` didn’t match any existing inventory items and is therefore a new item.

### Attach a Tool

To create and call `AttachTool()` to attach a new tool to the character, follow these steps:

1. In your character’s `.h` file, in the `public` section, declare a function named `AttachTool()` that takes a `UEquippableToolDefinition` pointer. This function attempts to equip the tool within the `ToolDefinition` to the player.
2. In the `protected` section, declare a `TObjectPtr` to an `AEquippableToolBase` named `EquippedTool`. Give it `VisibleAnywhere`, `BlueprintReadOnly`, and `Category = Tools UPROPERTY()` specifiers.
3. In your character’s `.cpp` file, implement `AttachTool()`. First, in an `if` statement, check if the Character already has the tool by calling `IsToolAlreadyOwned()`.

#### Spawn a Tool Actor

The `AEquippableToolBase` tool stored inside `ToolDefinition` is an Actor, so it may not be loaded when `AttachTool()` is called. To handle this, you’re going to spawn a new instance of the tool using the `SpawnActor()` function.

`SpawnActor()` is part of the **UWorld** object, which is the core object that represents the map and the actors in it. Access it by calling the `GetWorld()` function from any Actor.

In the `if` statement inside `AttachTool`, declare a new `AEquippableToolBase` pointer named **ToolToEquip**. Set this equal to the result of calling `GetWorld()->SpawnActor()`, passing the `ToolDefinition->ToolAsset` as the Actor to spawn and`this->GetActorTransform()` as the location to spawn it.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Only equip this tool if it isn&#39;t already owned\nif (!IsToolAlreadyOwned(ToolDefinition))\n{\n\t// Spawn a new instance of the tool to equip\n\tAEquippableToolBase* ToolToEquip = GetWorld()-&gt;SpawnActor&lt;AEquippableToolBase&gt;(ToolDefinition-&gt;ToolAsset, this-&gt;GetActorTransform());\n}",
  "lines_of_code": 6,
  "id": 163391,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMzOTEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--f46837146c2d63ae6c4cdce169cd1c4b8cab3960c8b88130db128c2ac8cd41e5",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "When you pass <code class=\"inline-code\">ToolDefinition-&gt;ToolAsset</code> to <code class=\"inline-code\">SpawnActor</code>, UE knows to look at <code class=\"inline-code\">ToolAsset</code>’s class type and spawn that type of Actor. (<code class=\"inline-code\">ToolAsset</code> is the <code class=\"inline-code\">EquippableToolBase</code> Actor associated with that <code class=\"inline-code\">ToolDefinition</code>.)",
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

#### Attach an Item to the Character

To attach the spawned tool actor to your character, follow these steps:

1. In `AttachTool`, after the `ToolToEquip` declaration, declare a new `FAttachementTransformRules` named `AttachementRules`. `FAttachementTransformRules` is a struct that defines how to handle location, rotation, and scale when attaching. It takes `EAttachmentRules` and a bool `InWeldSimulatedBodies` at the end to tell UE if physics is involved. When true, UE welds both bodies together so they can interact as one when moving around. Some popular attachment rules include `KeepRelative` (maintain relative transform to parent), `KeepWorld` (maintain world transform), and `SnapToTarget` (snap to parent's transform).
2. In your `AttachmentRules` definition, add `EAttachmentRule::SnapToTarget` and `true`.
3. Call `ToolToEquip->AttachToActor()` to attach the tool to the character, followed by `ToolToEquip->AttachToComponent()` to attach the tool to the right-hand socket of the first-person mesh component. `AttachToActor` attaches an Actor to a target parent Actor, and `AttachToComponent` attaches an Actor’s root component to the target component. They have the following syntax: `MyActor->AttachToActor(ParentActor, AttachmentRules, OptionalSocketName)`

#### Add the Item’s Animations to the Character

After attaching `ToolToEquip`, set the animations on the first and third-person meshes using `SetAnimInstanceClass()`, passing the tool’s first-person and third-person animations.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "\t\t// Attach the tool to this character, and then the right hand of their first-person mesh\n\t\tToolToEquip-&gt;AttachToActor(this, AttachmentRules);\n\t\tToolToEquip-&gt;AttachToComponent(FirstPersonMeshComponent, AttachmentRules, FName(TEXT(&quot;HandGrip_R&quot;)));\n\n\t\t// --- New Code Start ---\n\t\t// Set the animations on the character&#39;s meshes.\n\t\tFirstPersonMeshComponent-&gt;SetAnimInstanceClass(ToolToEquip-&gt;FirstPersonToolAnim-&gt;GeneratedClass);\n\t\tGetMesh()-&gt;SetAnimInstanceClass(ToolToEquip-&gt;ThirdPersonToolAnim-&gt;GeneratedClass);\n\t\t// --- New Code End ---",
  "lines_of_code": 9,
  "id": 163395,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMzOTUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--cafd969d7877c66ef42548c151e8d49b4aca43c48e3f04c9112cf2598cc73547",
  "settings": {
    "is_hidden": false
  }
}
```

`SetAnimInstanceClass` dynamically changes the animation Blueprint at runtime for a skeletal mesh and is commonly used when equipping items and weapons with different sets of animations. `GeneratedClass` gets the actual `AnimInstance` class generated from the Blueprint.

#### Add the Item to Inventory

To make the tool belong to the character, follow these steps:

1. After setting the new animations, add the tool to the character’s inventory using `ToolInventory.Add()`.
2. Now that the tool is attached, set the `ToolToEquip->OwningCharacter` to this character.
3. You’ve finished attaching the new tool to the character, so set the `EquippedTool` to `ToolToEquip`.

#### Add an Item’s Controls to the Character

To add the tool’s **Input Action** and **Input Mapping Context** to the character, follow these steps:

1. In your character's .h file, in the `protected` section, declare a `TObjectPtr` to a `UInputAction` named `UseAction`. This is the “use tool” input action that you’ll bind to the tool’s `Use()` function.
2. You’ll implement the input action similar to how you set up `AAdventureCharacter::BeginPlay()` in the **Bind the Input Mapping to the Character** section of [Configure Character Movement](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-03-configure-character-movement-with-cplusplus-in-unreal-engine): getting the `PlayerController`, then the enhanced input local subsystem, using `if` statements to check for null pointers as you go. Add this code after `EquippedTool = ToolToEquip;`: This time, when you add the tool’s Input Mapping Context to the player subsystem, set the priority to `1`. The priority of the player’s main mapping context (`FirstPersonContext`) is lower (`0`), so when both mapping contexts have the same key binding, the input binding in `ToolToEquip->ToolMappingContext` takes priority over `FirstPersonContext`.
3. After adding the mapping context and between the two new `if` statements, call `ToolToEquip->BindInputAction()`, passing the `UseAction` to bind the character’s input action to the tool’s `Use()` function.

Your complete `AttachTool()` function should look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "void AAdventureCharacter::AttachTool(UEquippableToolDefinition* ToolDefinition)\n{\n\t// Only equip this tool if it isn&#39;t already owned\n\tif (!IsToolAlreadyOwned(ToolDefinition))\n\t{\n\t\t// Spawn a new instance of the tool to equip\n\t\tAEquippableToolBase* ToolToEquip = GetWorld()-&gt;SpawnActor&lt;AEquippableToolBase&gt;(ToolDefinition-&gt;ToolAsset, this-&gt;GetActorTransform());\n\n\t\t// Attach the tool to the First Person Character\n\t\tFAttachmentTransformRules AttachmentRules(EAttachmentRule::SnapToTarget, true);\n",
  "lines_of_code": 37,
  "id": 163402,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM0MDIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--ce1743608fefd97224f20f8f126fcebc0dfa525b8b631c76c4702a147cf7ae54",
  "settings": {
    "is_hidden": false
  }
}
```

### Support Different Item Types with GiveItem()

You’ve got a way to attach tools, but because pickups and their item definitions can contain more than just tools, you need a way to know what kind of item your character is interacting with before calling `AttachTool()`.

You'll create a `GiveItem()` function to perform different actions based on the type of `ItemDefinition` passed in. You declared different types of items with the `EItemType enum` in `ItemData.h` and you can use that data now to differentiate between different item definitions.

To create a function that gives an item to the player based on its type, follow these steps:

1. In `AdventureCharacter.h`, in the `public` section, declare a function named `GiveItem()` that takes a `UItemDefinition()` pointer. Other classes call this function when attempting to give an item to the player.
2. In `AdventureCharacter.cpp`, add a function definition header for `GiveItem()`. In the function, start by declaring a `switch` statement that cases based on the `ItemType` of the item passed to this function.
3. Inside the switch statement, declare cases for `EItemType::Tool`, `EItemType::Consumable`, and a default case. In this tutorial, you’re only implementing the Tool-type item, so in the `Consumable` and `default` cases, log the type of item and break out of the switch case.
4. Inside the `Tool` case, cast the `ItemDefinition` to a `UEquippableToolDefinition` pointer named `ToolDefinition`.
5. Ensure the cast succeeded by checking if `ToolDefinition` is `null`. If it isn’t `null`, call `AttachTool()` to attach the tool to the character. Otherwise, `print` the error and `break`.

Your complete `GiveItem()` function should look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "void AAdventureCharacter::GiveItem(UItemDefinition* ItemDefinition)\n{\n\t// Case based on the type of the item\n\tswitch (ItemDefinition-&gt;ItemType)\n\t{\n\tcase EItemType::Tool:\n\t{\n\t\t// If the item is a tool, attempt to cast and attach it to the character\n\n\t\tUEquippableToolDefinition* ToolDefinition = Cast&lt;UEquippableToolDefinition&gt;(ItemDefinition);\n",
  "lines_of_code": 29,
  "id": 163407,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM0MDcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--fb75df3a52065d1b8cf72cbc7e2ff1e15b64aa277c7ccf5b61cae82d8256ae66",
  "settings": {
    "is_hidden": false
  }
}
```

Last, you need an in-game trigger to set your item-granting logic in motion. When a character collides with a pickup, the pickup should call the character’s `GiveItem()` function to grant the pickup’s `ReferenceItem` to the character.

To call `GiveItem()` after a collision with the tool pickup, follow these steps:

1. In `PickupBase.cpp`, in `OnSphereBeginOverlap()`, after checking if the Character is valid, call `Character->GiveItem(ReferenceItem)` to grant the item to your character.

Now that you’ve set up your tool data and actor, you can use these to build a real tool for your character to equip in-game!

## Implement a Dart Launcher

For your first equippable tool, you’ll create a dart launcher that can launch projectiles. In this section, you’ll start by creating the tool for your character to hold and use. In the next section of this tutorial, you’ll implement projectile logic.

### Set up a New DartLauncher Class

To derive a new dart launcher class from `EquippableToolBase`, follow these steps:

1. In the Unreal Editor, go to **Tools > New C++ Class**.
2. Go to All Classes, search for **EquippableToolBase**, and select it as the parent class.
3. Name the class `DartLauncher`. Create a new folder named `Tools` in your project's `Public` folder to store the code for your tools. Click **Create Class**. ![Image](https://dev.epicgames.com/community/api/documentation/image/84cba007-f2f4-4363-9b3e-dbd6322fb0aa)
4. In Visual Studio, at the top of `DartLauncher.h`: Add the `BlueprintType` and `Blueprintable` specifiers to the `UCLASS()` macro. Add a `public` section, and declare overrides for both the `Use()` and `BindInputAction()` functions from `AEquippableToolBase`. Your complete `DartLauncher.h` class should look like the following:
5. In `DartLauncher.cpp`, at the top of the file, add an include statement for `”AdventureCharacter.h”`. You’ll need this in the `BindInputAction()` function.

Next, you'll start adding new logic to the dart launcher.

### Implement Tool Controls

Now that you’re working in a specific tool and know what function you’re binding, you can implement `BindInputAction()`.

To bind the tool's Use function, follow these steps:

1. In `DartLauncher.cpp`, add a function definition header for the `Use()` function.
2. Inside `Use()`, add a debug message that notifies when the player triggers the function.
3. Add a function definition header for `BindInputAction()`. Inside the function, in an `if` statement, get the player controller for the `OwningCharacter` by using `GetController()`, and then cast it to `APlayerController`. This is similar to how you added a mapping context in the `AAdventureCharacter::BeginPlay()` function.
4. Bind the `Use` function similar to how you bound your movement actions in the **Binding Movement Actions** section of [Configure Character Movement](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-03-configure-character-movement-with-cplusplus-in-unreal-engine): In another `if` statement, declare a new `UEnhancedInputComponent` pointer named `EnhancedInputComponent`. Set this equal to the result of calling `Cast()` on the `PlayerInputComponent` passed to this function while casting it to `UEnhancedInputComponent`.
5. Use `BindAction` to bind the `ADartLauncher::Use` action to the `InputToBind` action that’s passed to this function using `BindAction()`. This binds the InputAction to `Use();` so that when the given action happens, `Use()` is called.
6. Save your code and compile it.

Your `BindInputAction()` function and your complete `DartLauncher.cpp` class should now look like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n\n#include &quot;Tools/DartLauncher.h&quot;\n#include &quot;AdventureCharacter.h&quot;\n\n\nvoid ADartLauncher::Use()\n{\n\tGEngine-&gt;AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT(&quot;Using the dart launcher!&quot;));\n",
  "lines_of_code": 25,
  "id": 163415,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM0MTUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--412ee4a44049919c74484dc14d6ca5f45dc15e789d902b9425d87e4491016a85",
  "settings": {
    "is_hidden": false
  }
}
```

### Adapt an Animation Blueprint For Your Character

The first-person template includes a sample Animation Blueprint for weapon-type items, but you’ll need to make a few changes to the Blueprint so it can work with your dart launcher.

To add a tool-holding Animation Blueprint to your character, take the following steps:

1. In the **Content Browser**, go to the **Content > Variant\_Shooter > Anim** folder, right-click the `ABP_FP_Pistol` Animation Blueprint, and select **Duplicate**.
2. Name this copy **ABP\_FP\_DartLauncher**, drag it into the **Content > FirstPerson > Anims** folder, and select **Move Here**. ![Image](https://dev.epicgames.com/community/api/documentation/image/9c3c55e6-1076-4539-b2e6-66fde6f84765)
3. Open the new Animation Blueprint.
4. Near the top of the Event Graph, zoom in to the group of nodes that begins with an **Event Blueprint Begin Play** node. ![Image](https://dev.epicgames.com/community/api/documentation/image/1c5d41b9-ab86-42a1-a1e5-54ee6e7eed42) This Blueprint gets **First Person Mesh** and **First Person Camera** variables from `BP_FPShooter`, so you’ll change this to use your Character Blueprint instead (this tutorial uses `BP_AdventureCharacter`).
5. Click each of these nodes and press **Delete**: **Cast To BP\_FPShooter** **First Person Mesh** variable getter **First Person Camera** variable getter
6. Right-click on the **Event Graph**, then search for and select a **Cast To BP\_AdventureCharacter** node. ![Image](https://dev.epicgames.com/community/api/documentation/image/19440113-fe9d-4f9c-85f0-ef670a32cbe1)
7. Connect the execution pins from **Event Blueprint Begin Play** to the new node, and then to the **Set First Person Mesh** node.
8. Connect the **Try Get Pawn Owner** node’s **Return Value** pin to the **Cast To** node’s **Object** pin. ![Image](https://dev.epicgames.com/community/api/documentation/image/cb607252-69c1-4527-86c4-1803d5ec974b)
9. To create a new node off of **Cast To BP\_AdventureCharacter**, click the **As BP My Adventure Character** pin and drag to an empty spot in the graph. ![Image](https://dev.epicgames.com/community/api/documentation/image/3a8e46b8-5ca0-44a1-ab1a-ff0adb06dcf8)
10. Search for and **Get Mesh** and select it under **Variables > Character**. Connect the new node’s **Mesh** pin to the **Set First Person Mesh** node.
11. For the camera, drag another node from the **As BP My First Person Character** pin, and search for and select **Get Component by Class**.
12. On the new node, set the **Component Class** to **Camera Component**. Then, connect the **Return Value** pin to the **Set First Person Camera** node. ![Image](https://dev.epicgames.com/community/api/documentation/image/dbe4e68c-cc5d-4c3e-be99-f1936e7ab307)
13. Save your `ABP_FP_DartLauncher` Blueprint and compile it.

### Define Dart Launcher Controls

Your dart launcher needs an input action and input mapping context so the character can shoot projectiles from the tool.

To create player controls for your dart launcher tool, follow these steps:

1. In the **Content Browser**, go to the **Input > Actions** folder.
2. Create and set up a “use tool” Input Action: Click **Add**, go to **Input**, and select **Input Action**. Name it **IA\_UseTool**. ![Image](https://dev.epicgames.com/community/api/documentation/image/275793eb-4060-4f95-9e8a-d3a8f0a6c55f) Double-click **IA\_UseTool** to open it. In its **Details** panel, ensure its **Value Type** is **Digital (bool)**. Next to **Triggers**, click the **plus** button (**+**), then select **Pressed** from the list of triggers. ![Image](https://dev.epicgames.com/community/api/documentation/image/23103bc1-f9f9-4ba3-b9ae-d3d76e149792) Save and close the Input Action.
3. Back in the **Content Browser**, go to the **Input** **folder**.
4. Create and set up a new Input Mapping Context that maps the left mouse button and gamepad right trigger to the dart launcher's Use action: Create a new **Input Mapping Context** named **IMC\_DartLauncher**. ![Image](https://dev.epicgames.com/community/api/documentation/image/f628c3f0-22ab-4e76-baab-0f7e1ee52bb3) Open **IMC\_DartLauncher**. Click the plus button next to **Mappings**. In the dropdown list, select `IA_UseTool`. Click the arrow to expand the mapping. Click the keyboard button, then press your left mouse button to bind that button to `IA_UseTool`. Next to **IA\_UseTool**, click **+** to add another binding. In the dropdown list, expand **Gamepad** and select **Gamepad Right Trigger Axis**. ![Image](https://dev.epicgames.com/community/api/documentation/image/b9baa77a-9643-4513-a1de-f8e1c62da995) Save and close the Input Mapping Context.

### Assign the Use Input Action

To assign `IA_UseTool` to the character's **Use Action** variable, follow these steps:

1. Open your character's Blueprint.
2. In the **Details** panel, in the **Input** section, set **Use Action** to `IA_UseTool`. ![Image](https://dev.epicgames.com/community/api/documentation/image/d35d6599-e2d7-4005-be92-0a45f29238c9)
3. Compile and save your Blueprint.

### Create the DartLauncher Blueprint

Now you can bring everything together in a new DartLauncher Blueprint.

To create the Dart Launcher Blueprint from the DartLauncher class, follow these steps:

1. In the Content Browser, go to your C++ Classes > *ProjectName*> Public > Tools folder, right-click your DartLauncher class, and create a new Blueprint class.
2. Name it `BP_DartLauncher`. Right-click your FirstPerson > Blueprints folder to create a new folder named Tools to store your equippable items, then finish creating the Blueprint.
3. In the Blueprint's **Details** panel, set the following default properties: Set **First Person Tool Anim** to `ABP_FP_DartLauncher`. Set **Third Person Tool Anim** to `ABP_TP_Pistol`. Set **Tool Mapping Context** to `IMC_DartLauncher`. Leave **Owning Character** empty. ![Image](https://dev.epicgames.com/community/api/documentation/image/e52eff20-5a1c-45d9-bbfd-d196bd466cc6)
4. In the **Components** tab, click the **Tool Mesh Component** and set the **Skeletal Mesh Asset** to `SKM_Pistol`. ![Image](https://dev.epicgames.com/community/api/documentation/image/24dc6e6d-0f1c-4139-9281-58b51b333b77)

### Create the Dart Launcher Data Asset

To create a Data Asset to store this Blueprint’s data, follow these steps:

1. In the **Content Browser**, in the **FirstPerson > Data** folder, create a new Data Asset and pick **Equippable Tool Definition** as the Data Asset instance. Name this asset `DA_DartLauncher`.
2. Inside `DA_DartLauncher`, in the **Details** panel, set the following properties: Set **Tool Asset** to `BP_DartLauncher`. Set **ID** to **tool\_001**. Set **Item Type** to **Tool**. Set **World Mesh** to `SM_Pistol`. ![Image](https://dev.epicgames.com/community/api/documentation/image/ae599263-87cd-4417-84ea-a81265b7dc4e)
3. Enter a **Name** and **Description**.
4. Save your Data Asset.

### Create a Data Table for Tools

Although this tool could go in your `DT_PickupData` table, it’s helpful to organize your tables to track specific things. For example, you could have different tables for items that specific classes can equip, or tables of items that different enemies drop when defeated. In this tutorial, you’ll have a table for consumables and a table for tools.

To create a new Data Table to track your tool items, follow these steps:

1. In the **Content Browser**, go to the **FirstPerson > Data** folder, and create a new **Data** **Table**.
2. Select **ItemData** as the row structure.
3. Name the table `DT_ToolData`, then open it. ![Image](https://dev.epicgames.com/community/api/documentation/image/60bf2e34-5c78-4207-b39a-fb0fa0716048)
4. Inside `DT_ToolData`, click **Add** to create a new row for your dart launcher.
5. With the new row selected, set the following fields: Change the **Row Name** and **ID** to `tool_001`. Set **Item Type** to **Tool**. Enter the same **Name** and **Description** you set in the Data Asset. Set **Item Base** to the `DA_DartLauncher`. ![Image](https://dev.epicgames.com/community/api/documentation/image/0b0d8057-0651-4033-b9c0-fb7b008b2a2b)
6. Save and close the Data Table.

## Test a Dart Launcher Pickup In Game

You’ve modified your pickup class to grant an item to the user, created an equippable item class that gives the player a new mesh, animations, and controls, and set up an equippable dart launcher tool.

It’s time to bring it all together and create the in-game pickup that triggers all the equippable item logic you’ve set up in this part of the tutorial. `PickupBase` handles picking up an object, and `EquippableToolBase` handles giving an item to the player.

In the **Content Browser**, go to **Content > FirstPerson > Blueprints** and drag a new `BP_PickupBase` into the level. Set the **Pickup Item ID** to `tool_001`and the **Pickup Data Table** to `DT_ToolData`.

![Image](https://dev.epicgames.com/community/api/documentation/image/c1fa4e33-9241-4dc2-8bc9-4de441520804)

Click **Play** to test out your game. When the game begins, your pickup should initialize to the dart launcher. When you run over your pickup, your character should start holding the tool!

## Next Up

In the final section, you’ll implement projectile physics in your dart launcher and make it launch foam darts!

- [Related Document](en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine.md)

## Complete Code

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "ItemDefinition.h",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;Engine/DataAsset.h&quot;\n#include &quot;Data/ItemData.h&quot;\n#include &quot;ItemDefinition.generated.h&quot;\n\n// Defines an item definition built from data table data.\n",
  "lines_of_code": 32,
  "id": 163416,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM0MTYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--73b69e89de45f163c83d9b01b3a70748d605dc82b129a006fcb808b3a503ad9a",
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
  "title": "EquippableToolDefinition.h",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;ItemDefinition.h&quot;\n#include &quot;EquippableToolDefinition.generated.h&quot;\n\nclass AEquippableToolBase;\nclass UInputMappingContext;\n",
  "lines_of_code": 25,
  "id": 163417,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM0MTcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--22e2a7edc0544048d2cbb24936ddf1086e96182d3ff81b739c91d9a225636553",
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
  "title": "EquippableToolDefinition.cpp",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#include &quot;EquippableToolDefinition.h&quot;\n\nUEquippableToolDefinition* UEquippableToolDefinition::CreateItemCopy(UObject* Outer) const\n{\n\t// If we need an Outer, use GetTransientPackage\n\tif (!Outer)\n\t{\n\t\tOuter = GetTransientPackage();\n",
  "lines_of_code": 15,
  "id": 163418,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM0MTgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--4dc44bb2d03583255d43df5949fc7ece8974382d773259a42c17975669d8f6c8",
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
  "title": "InventoryComponent.h",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;Components/ActorComponent.h&quot;\n#include &quot;InventoryComponent.generated.h&quot;\n\nclass UEquippableToolDefinition;\n\n",
  "lines_of_code": 33,
  "id": 163419,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM0MTksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--26a6d3b98ab5b55e3ad36755848f0ce128cce055ec266fe8b8ca06d7b637bcf7",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "code_snippet",
  "description": "N",
  "snippet_type": "cpp_programming",
  "title": "DartLauncher.h",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;EquippableToolBase.h&quot;\n#include &quot;DartLauncher.generated.h&quot;\n\n\nUCLASS()\n",
  "lines_of_code": 21,
  "id": 163420,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM0MjAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--2bbb0055bc20073b8e7014afdc90c2784e67329ddc131e6b40afb2381e9986a4",
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
  "title": "DartLauncher.cpp",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n\n#include &quot;Tools/DartLauncher.h&quot;\n#include &quot;AdventureCharacter.h&quot;\n\n\nvoid ADartLauncher::Use()\n{\n\tGEngine-&gt;AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT(&quot;Using the dart launcher!&quot;));\n",
  "lines_of_code": 25,
  "id": 163421,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM0MjEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--8aaa85266ebd000df8fbf022a515d217060194c94a200c74fa0b16992d91b674",
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
  "title": "EquippableToolBase.h",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;GameFramework/Actor.h&quot;\n#include &quot;EnhancedInputSubsystems.h&quot;      // CHAT GPT SAID NOT NEEDED?\n#include &quot;Animation/AnimBlueprint.h&quot;\n#include &quot;Components/SkeletalMeshComponent.h&quot;\n#include &quot;EquippableToolBase.generated.h&quot;\n",
  "lines_of_code": 61,
  "id": 163422,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM0MjIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--626885c26f0775ae7436cb146927d6f2ee1685b859b2ccd4b0de8b02ade0864b",
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
  "title": "EquippableToolBase.cpp",
  "code_preview": "\n// Copyright Epic Games, Inc. All Rights Reserved.\n\n\n#include &quot;EquippableToolBase.h&quot;\n#include &quot;InputMappingContext.h&quot;\n#include &quot;AdventureCharacter.h&quot;\n\n// Sets default values\nAEquippableToolBase::AEquippableToolBase()\n",
  "lines_of_code": 44,
  "id": 163423,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM0MjMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--ae3c9e09ade5a77a44d79eb68c57aab55783d9eeaa29b8b9b8c94781629b8692",
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
  "title": "AdventureCharacter.h",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;Camera/CameraComponent.h&quot;\n#include &quot;GameFramework/Character.h&quot;\n#include &quot;EnhancedInputComponent.h&quot;\n#include &quot;EnhancedInputSubsystems.h&quot; \n#include &quot;InputActionValue.h&quot;\n",
  "lines_of_code": 113,
  "id": 163424,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM0MjQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--904bfc34350440620c5e41da86028368d1d1468aafd45b4e851911f9c90c35a9",
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
  "title": "AdventureCharacter.cpp",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n\n#include &quot;AdventureCharacter.h&quot;\n#include &quot;InventoryComponent.h&quot;\n#include &quot;EquippableToolDefinition.h&quot;\n#include &quot;EquippableToolBase.h&quot;\n\n// Sets default values\nAAdventureCharacter::AAdventureCharacter()\n",
  "lines_of_code": 233,
  "id": 163425,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM0MjUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODoyNyswMDowMCJ9--f028cf07ea080621b861396f712ed04dbaf1a2aaad8b569eb09e55e33eda1d8d",
  "settings": {
    "is_hidden": false
  }
}
```
