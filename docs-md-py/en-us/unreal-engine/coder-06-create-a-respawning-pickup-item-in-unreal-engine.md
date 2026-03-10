# Create a Respawning Pickup Item

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine

> Application Version: 5.7

## Before You Begin

Ensure you’ve completed the following objectives in the previous section, [Manage Items and Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-05-manage-item-and-data-in-an-unreal-engine-game):

- Set up an Item Data Struct, `UDataAsset` class, a Consumable-type Data Asset instance named `DA_Pickup_001`, and a Data Table.

## Create a New Pickup Class

So far, you've learned to define and store an item's structure and data. In this section, you'll learn how to turn this data into an in-game "pickup", a concrete representation of table data that the player can interact with and gain an effect. A pickup could be an equippable gadget, a box that gives them materials, or a powerup that gives them a temporary boost.

To start setting up a pickup class with initial declarations, follow these steps:

1. In the Unreal Editor, go to **Tools** > **New C++ Class**. Select **Actor** as the parent class and name the class `PickupBase`. Click **Create Class**.
2. In Visual Studio, in `PickupBase.h`, add the following statements to the top of the file: `#include ”Components/SphereComponent.h”`. You’ll add a sphere component to the pickup to detect collisions between player and pickup. `#include ”AdventureCharacter.h”`. Add a reference to your first-person character class so you can check for overlaps between the pickup and characters of this class. (This tutorial uses `AdventureCharacter`.) A forward declaration for `UItemDefinition`. This is the associated Data Asset item that each pickup references.
3. In the `UCLASS()` macro above the `APickupBase` class definition, add the `BlueprintType` and `Blueprintable` specifiers to expose it as a base class for creating Blueprints.
4. Switch to `PickupBase.cpp`.
5. In `PickupBase.cpp`, add an `#include` for `ItemDefinition.h` and `ItemData.h`.

## Initialize the Pickup with Table Data

Your pickup is just a blank Actor, so when the game begins, you need to give it the data it needs to operate properly. The pickup should pull a row of values from the Data Table and save those values in an ItemDefinition Data Asset (the “reference item”).

### Pull Data from a Data Table

To declare the function and properties you need to pull data from the data table, follow these steps:

1. In `PickupBase.h`, in the `public` section, declare a new void function `InitializePickup()`. You’ll use this function to initialize the pickup with values from the Data Table.
2. To pull data from the table, the pickup Blueprint needs two properties: the Data Table asset and the Row Name (which you’ve set up to be the same as the item ID). In the `protected` section, declare an `FName` property named `PickupItemID`. Give it the `EditInstanceOnly` and `Category = “Pickup | Item Table”` specifiers. This is the ID of this pickup in the associated Data Table.
3. Also in the `protected` section, declare a `TSoftObjectPtr` to a `UDataTable` named `PickupDataTable`. Give it the same specifiers as the `PickupItemID`. This is the Data Table the pickup uses to get its data. The Data Table may not be loaded at runtime, so use a `TSoftObjectPtr` here so you can load it asynchronously.
4. Save the header file and switch to `PickupBase.cpp` to implement `InitializePickup()`.

To initialize a pickup, you first need to retrieve a row of item data from the Data Table using the Pickup Item ID. This lookup should only happen if the ID is set and a valid Data Table asset is assigned. `PickupDataTable` is a soft reference and may not be loaded yet, so to validate the data table, you'll first convert that soft reference to an `FSoftObjectPath`

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "An <code>FSoftObjectPath</code> stores an asset’s path without loading it, making it useful for validating soft references before using them.  ",
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

To implement the `InitializePickup()` function, follow these steps:

1. In `PickupBase.cpp`, add the function definition for `InitializePickup()`.
2. Convert `PickupDataTable` to a `const FSoftObjectPath` named `TablePath` to verify that it points to a real asset before attempting to load and use it.
3. Inside the function, in an `if` statement, check if the `TablePath` is valid and that `PickupItemID` has a value.
4. In the `if` statement, declare a new pointer variable to a `UDataTable` named `LoadedDataTable` and use a ternary operator to test `PickupDataTable.IsValid()`, assigning `PickupDataTable.Get()` if it’s already loaded or `PickupDataTable.LoadSynchronous()` if it isn’t.
5. Use an `if` statement with a `return;` inside to exit the function if `LoadedDataTable` is null.
6. Retrieve the row of values from the Data Table. Declare a const `FItemData` pointer named `ItemDataRow` and set it to the result of calling `FindRow()` on your `LoadedDataTable`. Specify `FItemData` as the type of row to find.
7. Add the following two arguments to the `FindRow()` call: An `FName` row name you want to find. Pass the `PickupItemID` as the row name. An `FString`-type context string that you can use for debugging if the row isn’t found. You can use `Text(“My context here.”)` to add a context string, or use `ToString()` to convert the item ID into a context string.
8. Use an `if` statement with a `return;` inside to exit the function if `ItemDataRow` is null.
9. Check that the Data Asset referenced in the table row is valid so you can retrieve the item's mesh from the Data Asset later in this section of the tutorial. Declare a pointer to a `UItemDefinition` Data Asset named `TempItemDefinition` and use the same ternary operator syntax you used earlier.
10. Add an `if` statement to check that you have a loaded Data Asset before continuing.

### Create a Reference Item

Once you’ve retrieved the pickup’s row data, create and initialize a Data Asset-type `ReferenceItem` to hold that information.

By saving the data in a reference item like this, Unreal Engine can easily reference that data when it needs to know about the item instead of performing more table data lookups, which is less efficient.

To save a row of table data in a reference item, follow these steps:

1. In `PickupBase.h`, in the `protected` section, declare a `TObjectPtr` to a `UItemDefinition` named `ReferenceItem`. This is a Data Asset that stores the pickup’s data. Give it the `VisibleAnywhere` and `Category = “Pickup | Reference Item”` specifiers.
2. Save the header file and switch back to `PickupBase.cpp`.
3. In `InitializePickup()`, after the `if (!TempItemDefinition)` statement, set `ReferenceItem` to a `NewObject` of type `UItemDefinition`. Pass `this` as the outer class and the `UItemDefinition::StaticClass()` as the class type to create a base `UItemDefinition`.
4. To copy the pickup’s information into `ReferenceItem`, set each field in `ReferenceItem` to the associated field from `ItemDataRow`. For the `WorldMesh`, pull the `WorldMesh` property from `TempItemDefinition`.

### Call InitializePickup()

In `BeginPlay()`, call `InitializePickup()` to initialize the pickup when the game begins.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Called when the game starts or when spawned\nvoid APickupBase::BeginPlay()\n{\n\tSuper::BeginPlay();\n\n\t// Initialize this pickup with default values\n\tInitializePickup();\n}",
  "lines_of_code": 8,
  "id": 160737,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA3MzcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0ODoxNCswMDowMCJ9--263b1708eaaa25e7f22c51682344c8974704c4bae4a0d3c9581f18b3d0b7e930",
  "settings": {
    "is_hidden": false
  }
}
```

Save and build your code.

`PickupBase.cpp` should now look like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#include &quot;PickupBase.h&quot;\n#include &quot;ItemDefinition.h&quot;\n#include &quot;Data/ItemData.h&quot; \n\n// Sets default values\nAPickupBase::APickupBase()\n{\n\n",
  "lines_of_code": 82,
  "id": 160738,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA3MzgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0ODoxNCswMDowMCJ9--661df7b49218fb5d4605c508a42a7e8e450aa6ba02d1eb5292b9cd0ef90359c5",
  "settings": {
    "is_hidden": false
  }
}
```

## Create In-Game Functionality

Your pickup has the item data it needs, but it still needs to know how to appear and operate in the game world. It needs a mesh for the player to see, a collision volume to determine when the player touches it, and some logic to make the pickup disappear (as if the player picked it up) and respawn after a certain amount of time.

### Add a Mesh Component

Just like you did when setting up the player character in [Add a First-Person Camera, Mesh, and Animation](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation), you’ll use the `CreateDefaultSubobject` template function to create a static mesh object as a child component of your pickup class and then apply the item’s mesh to this component.

To give the base pickup class a static mesh component, follow these steps:

1. In `PickupBase.h`, in the `protected` section, declare a `TObjectPtr` to a `UStaticMeshComponent` named `PickupMeshComponent`. This is the mesh that will represent the pickup in the world. You’ll use code to assign the Data Asset’s mesh to this property, so give it the `VisibleDefaultsOnly` and `Category = “Pickup | Mesh”` specifiers so it’s visible, but not editable, in Unreal Editor.
2. Save the header file and return to to `PickupBase.cpp`.
3. In the `APickupBase` construction function, set the `PickupMeshComponent` pointer to the result of calling `CreateDefaultSubobject()` of type `UStaticMeshComponent`. In the `Text` argument, name the object `“PickupMesh”`.
4. On the next line, to ensure the mesh was properly instantiated, check that `PickupMeshComponent` isn’t null.
5. After creating the mesh component, call `SetRootComponent()` to ensure the mesh is the root component. If you don’t set a root component in C++, Unreal Engine may choose a different one during recompiles or editor restarts, which can break component attachment, transforms, and collision behavior.

Next, apply the item's mesh to the mesh component. You defined `WorldMesh` with a `TSoftObjectPtr`, so in `InitializePickup()`’s implementation, first check that the mesh is loaded before applying it.

To check the mesh is loaded and then apply it, follow these steps:

1. In `InitializePickup()`, after the `ReferenceItem` setup but inside the larger `if` statement, declare a `UStaticMesh` pointer named `LoadedMesh` and use the same ternary operator syntax to resolve `TempItemDefinition`'s `WorldMesh` soft pointer and ensure the mesh is ready to use.
2. In a new `if` statement, check if `LoadedMesh` is not null.
3. In the new `if` statement, set the `PickupMeshComponent` by calling `SetStaticMesh()`, passing `LoadedMesh`:
4. Save and build your code.

`PickupBase.cpp` should look like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#include &quot;PickupBase.h&quot;\n#include &quot;ItemDefinition.h&quot;\n#include &quot;Data/ItemData.h&quot; \n\n// Sets default values\nAPickupBase::APickupBase()\n{\n\t// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n",
  "lines_of_code": 101,
  "id": 161311,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjEzMTEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0ODoxNCswMDowMCJ9--1f220e1fd33e7b73819277a35667a95fb7540deb03d8d5e8ec8c283d361fb9a6",
  "settings": {
    "is_hidden": false
  }
}
```

### Add a Collision Shape

Add a sphere component to act as a collision volume, then enable collision queries on that component.

To set up collision on the pickup, follow these steps:

1. In `PickupBase.h`, in the `protected` section, declare a `TObjectPtr` to a `USphereComponent` named `SphereComponent`. This is the sphere component used for collision detection. Give it the `EditAnywhere`, `BlueprintReadOnly`, and `Category = “Pickup | Components”` specifiers.
2. Save the header file and return to `PickupBase.cpp`.
3. In the `APickupBase` construction function, after you set the `PickupMeshComponent`, set `SphereComponent` to the result of calling `CreateDefaultSubobject` with `USphereComponent` as the type and `“SphereComponent”` as the name. Add a null `check` afterwards.
4. Now that you have both components, use `SetupAttachment()` to attach the `PickupMeshComponent` to the `SphereComponent`:
5. After attaching the `SphereComponent`, set the sphere’s size using `SetSphereRadius()`. This value should be large enough for the player to intentionally interact with the pickup, but not so large that the player collects the pickup accidentally when passing nearby.
6. After setting the radius, make the sphere generate overlap events by calling `SetGenerateOverlapEvents(true)`.
7. Make the `SphereComponent` collidable by calling `SetCollisionEnabled()`. This function takes an enum (`ECollisionEnabled`) that tells the engine what type of collision to use. You want the character to be able to collide and trigger collision queries with the pickup, but the pickup shouldn’t have any physics that makes it bounce away when hit, so pass the `ECollisionEnabled::QueryOnly` option.
8. You've turned collision on for the sphere, and you also need to define what types of collisions can occur. Collision channels define what types of objects can interact with each other and collision responses define how those interactions are handled. Before setting up the sphere's collision responses, call `SetCollisionResponseToAllChannels()` to set the response to every collision channel to `ECR_Ignore` to ensure no engine defaults or presents affect your collision rules.
9. Now you can set the collision channel responses. The pickup needs query-only collision and overlap responses, but only with the Pawn channel.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For more information about Unreal Engine's collision system, see <a data-document-id=\"3229766\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/collision-response-reference-in-unreal-engine\">Collision Response Reference</a>.",
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

`PickupBase.cpp` should now look like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#include &quot;PickupBase.h&quot;\n#include &quot;ItemDefinition.h&quot;\n#include &quot;Data/ItemData.h&quot; \n\n// Sets default values\nAPickupBase::APickupBase()\n{\n\t// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n",
  "lines_of_code": 122,
  "id": 160751,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA3NTEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0ODoxNCswMDowMCJ9--3954db1afa3e8de35f5f82137b8a4f6591b3083e98251963d3644650a9033b8e",
  "settings": {
    "is_hidden": false
  }
}
```

### Simulate Pickup Collisions

Now that your pickup has a collision shape, add logic to detect a collision between the pickup and player and make the pickup disappear when collided with.

#### Declare the Overlap Handler

In `PickupBase.h`, in the `protected` section, declare a `void` function named `OnSphereBeginOverlap()`.

Any component that inherits from `UPrimitiveComponent`, like `USphereComponent`, can implement this function to run code when the component overlaps with some other Actor. This function takes several parameters you won’t be using; you’ll only pass the following:

- `UPrimitiveComponent* OverlappedComponent`: The component that was overlapped.
- `AActor* OtherActor`: The Actor overlapping that component.
- `UPrimitiveComponent* OtherComp`: The Actor’s component that overlapped.
- `int32 OtherBodyIndex`: The index of the overlapped component.
- `bool bFromSweep, const FHitResult& SweepResult`: Information about the collision, such as where it happened and at what angle.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Code for when something overlaps the SphereComponent. \nUFUNCTION()\nvoid OnSphereBeginOverlap(UPrimitiveComponent* OverlappedComponent, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult&amp; SweepResult);",
  "lines_of_code": 3,
  "id": 160752,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA3NTIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0ODoxNCswMDowMCJ9--18fcd3bf7557a864956c423919ce33bc1d863d5c81f302295a7f82c2fd5660b7",
  "settings": {
    "is_hidden": false
  }
}
```

Save the header file and switch to `PickupBase.cpp`.

#### Bind the Function to the Collision Event

Unreal Engine’s collision events are implemented using dynamic multicast delegates. In UE, this delegate system enables one object to call multiple functions at once, sort of like broadcasting a message to a mailing list where your subscribers are these other functions. When we bind functions to the delegate, it’s like we’re subscribing them to our mailing list. The “delegate” is our event; in this case, a collision between the player and the pickup. When the event happens, Unreal Engine calls all functions bound to that event.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Unreal Engine includes a couple of other binding functions, but you’ll want to use <code class=\"inline-code\">AddDynamic()</code> because your delegate, <code class=\"inline-code\">OnComponentBeginOverlap</code>, is a dynamic delegate. And, you’re binding a <code class=\"inline-code\">UFUNCTION</code> in a <code class=\"inline-code\">UObject</code>class, requiring <code class=\"inline-code\">AddDynamic()</code> for reflection support. For more information about dynamic multicast delegates, see Multicast Delegates<a data-document-id=\"3227462\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/multicast-delegates-in-unreal-engine\">Multi-cast Delegates</a>.  ",
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

In `PickupBase.cpp`, in `BeginPlay()`, before calling `InitializePickup();`, call the `AddDynamic` helper function to bind `OnSphereBeginOverlap()` to the sphere component’s `OnComponentBeginOverlap` event.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Called when the game starts or when spawned\nvoid APickupBase::BeginPlay()\n{\n\tSuper::BeginPlay();\n\t\n\t// --- New Code Start --- \n\t// Register the overlap event so it runs when an overlap happens\n\tSphereComponent-&gt;OnComponentBeginOverlap.AddDynamic(\n\t\tthis,\n\t\t&amp;APickupBase::OnSphereBeginOverlap\n",
  "lines_of_code": 17,
  "id": 160753,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA3NTMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0ODoxNCswMDowMCJ9--b1d7e7ec17dc89044fb7a122e92683b02b33e90d7c277ab7753eec6ab8167dd9",
  "settings": {
    "is_hidden": false
  }
}
```

To ensure Unreal Engine only ever creates a single event binding, before the line of code that binds the overlap event, call `RemoveAll(this)` on the delegate before the event binding.

`RemoveAll()` clears any existing delegate bindings associated with the passed actor.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Called when the game starts or when spawned\nvoid APickupBase::BeginPlay()\n{\n\tSuper::BeginPlay();\n\n\t// --- New Code Start --- \n\t// Ensure we don’t bind the overlap event more than once   \n\tSphereComponent-&gt;OnComponentBeginOverlap.RemoveAll(this);\n\t// --- New Code End --- \n\t// Register the overlap event so it runs when an overlap happens\n",
  "lines_of_code": 19,
  "id": 162441,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjI0NDEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0ODoxNCswMDowMCJ9--7340a23153bb552428b35d067fa99c5f36ea5475e7aba50845fdb50379ea50f9",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Bindings like this are usually done in <code class=\"inline-code\">BeginPlay()</code> as a part of runtime behavior, and you can  call <code>RemoveAll(this)</code> to guarantee the event is bound only once, even across editor during reloads and recompiles.  ",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "You could bind the the overlap event in <code class=\"inline-code\">InitiaizePickup()</code>, but we recommend performing this step outside of the function so the binding is successful even if loading and using the item data fails.",
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

Save your code.

Now, `OnSphereBeginOverlap()` will run when a character collides with the pickup’s sphere component.

#### Hide the Pickup After a Collision

Next, you'll implement the `OnSphereBeginOverlap()` function so the player can pick up the item.

To make your pickup disappear so it looks like the player picked it up, follow these steps:

1. In `PickupBase.cpp`, add the function signature for `OnSphereBeginOverlap()`.
2. Inside the function, add a debug message to signal the function is triggered properly.
3. This function runs whenever another actor collides with the pickup, so you need to make sure it’s your first-person character doing the colliding. Declare a new `AAdventureCharacter` pointer named `Character` and set it by casting `OtherActor` to your Character class’ name (this tutorial uses `AAdventureCharacter`).
4. In an `if` statement, check if `Character` is not null. Null indicates that the cast failed and that `OtherActor` was not some type of `AAdventureCharacter`.
5. In the `if` statement, hide the mesh and end the collision by: Setting the `PickupMeshComponent` to invisible using `SetVisibility(false)` Setting both the mesh and sphere component to non-collidable using `SetCollisionEnabled()`, passing the `NoCollision` option.
6. Save your code.

### Make the Pickup Respawn

Now that the character can’t interact with the pickup, make it respawn after a certain amount of time.

To implement a respawn timer for pickups, follow these steps:

1. In `PickupBase.h`, in the `protected` section, declare two variables: A bool named `bShouldRespawn`. You can use this to turn respawns on or off. Declare a float named `RespawnTime` initialized to `4.0f`. This is the time to wait until the pickup should respawn. Give both properties `EditAnywhere`, `BlueprintReadOnly`, and `Category = “Pickup | Respawn”` specifiers.
2. Also in the `protected` section, declare an `FTimerHandle` named `RespawnTimerHandle`.
3. Save the header file and return to `PickupBase.cpp`. Here, you'll use the Timer Manager to set a timer that calls `InitializePickup()` after a short wait.
4. You only want to respawn the pickup if respawns are enabled; so, at the bottom of `OnSphereBeginOverlap()`, add an `if` statement that checks if `bShouldRespawn` is true.
5. In the `if` statement, get the Timer Manager using `GetWorldTimerManager()` and call `SetTimer()` on the timer manager. This function has the following syntax: `SetTimer(InOutHandle, Object, InFuncName, InRate, bLoop, InFirstDelay);` Where: `InOutHandle` is the `FTimerHandle` that’s controlling the timer (your `RespawnTimerHandle`). `Object` is the `UObject` that owns the function you’re calling. Use this. `InFuncName` is a pointer to the function you want to call (`InitializePickup()` in this case). `InRate` is a float value specifying the time in seconds to wait before calling your function. `bLoop` makes the timer either repeat every `Time` seconds (`true`) or only fire once (`false`). `InFirstDelay` (optional) is an initial time delay before the first function call in a looping timer. If not specified, UE uses `InRate` as the delay. You only want to call `InitializePickup()` once to replace the pickup, so set `bLoop` to `false`. Set your preferred respawn time; this tutorial makes the pickup respawn after four seconds (`RespawnTime`).
6. You've turned off collision and hidden the mesh in the overlap event, so you need to restore the pickup's active state after it respawns. At the end of `InitializePickup()`: Make the `PickupMeshComponent` visible using `SetVisiblity(true)`. Repeat the `SphereComponent->SetCollisionEnabled` line of code that is in the class constructor.
7. Save your code and compile it from Visual Studio.

Your complete `OnSphereBeginOverlap()` function should look like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#include &quot;PickupBase.h&quot;\n#include &quot;ItemDefinition.h&quot;\n#include &quot;Data/ItemData.h&quot; \n\n// Sets default values\nAPickupBase::APickupBase()\n{\n\n",
  "lines_of_code": 157,
  "id": 160762,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA3NjIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0ODoxNCswMDowMCJ9--5b1ae2da0bced471eb7fd08c6e9475ef69fe60466dfb68fbe12d13cfcde7b808",
  "settings": {
    "is_hidden": false
  }
}
```

## Implement Pickups in Your Level

Now that you’ve defined the code that makes up your pickups, it’s time to test them out in your game!

To add pickups to your level, follow these steps:

1. In Unreal Editor, in the **Content Browser** asset tree, go to **Content > FirstPerson > Blueprints**.
2. In the **Blueprints** folder, create a new child folder named **Pickups** to store your pickup classes.
3. In the asset tree, go to your **C++ Classes** folder. Right-click your **PickupBase** class to create a Blueprint from that class. ![Image](https://dev.epicgames.com/community/api/documentation/image/15cbc8c4-541d-4fc2-8826-c05c266bf695)
4. Name it `BP_PickupBase`.
5. For the **Path**, select **Content/FirstPerson/Blueprints/Pickups**, and click **Create Pickup Base Class**. ![Image](https://dev.epicgames.com/community/api/documentation/image/f9df2655-bb13-4c98-841a-2b03c151f238)
6. Go back to your **Blueprints > Pickups** folder. Drag your `BP_PickupBase` Blueprint into the level. An instance of PickupBase appears in your level and is automatically selected in the **Outliner** panel. However, it doesn’t have a mesh yet. ![Image](https://dev.epicgames.com/community/api/documentation/image/49839627-7c2b-4f40-9439-d69be93ee25a)
7. With the `BP_PickupBase` actor still selected, in the **Details** panel, set the following properties: Set **Pickup Item ID** to `pickup_001`. Set **Pickup Data Table** to `DT_PickupData`. Set **Should Respawn** to **true**. ![Image](https://dev.epicgames.com/community/api/documentation/image/99dab706-6813-4627-8570-54efb0c536aa)

When you click **Play** to test your game, your pickup uses the **Pickup Item ID** to query the Data Table and retrieve data associated with `pickup_001`. The pickup uses table data and the reference to your `DA_Pickup_001` Data Asset to initialize a reference Item and load its static mesh.

![Image](https://dev.epicgames.com/community/api/documentation/image/b542012b-991b-4757-b6ba-c1a98ff45789)

When you run over the pickup, you should see it disappear, then reappear four seconds later.

### Load a Different Pickup

If you set the **Pickup Item ID** to a different value, your pickup will retrieve data from that row in the table instead.

To experiment with switching the **Pickup Item ID**, follow these steps:

1. Create a new Data Asset named **DA\_Pickup\_002**. Set the following properties in this asset: **ID**: pickup\_002 **Item Type**: Consumable **Name**: Test Name 2 **Description**: Test Description 2 **World** **Mesh**: `SM_ChamferCube` ![500](https://dev.epicgames.com/community/api/documentation/image/43c35634-3b5c-4a88-a95c-62e62e7b763c)
2. Add a new row in the `DT_PickupData` table and enter the Data Asset's information into the new row's fields. ![Image](https://dev.epicgames.com/community/api/documentation/image/41eac8a8-93f3-42c6-a83f-49afd2486558)
3. In the `BP_PickupBase` actor, change the **Pickup Item ID** to `pickup_002`.

When you click **Play** to test your game, the pickup should spawn with the values from `DA_Pickup_002` instead!

![Image](https://dev.epicgames.com/community/api/documentation/image/09ce7a4b-0f06-46cf-b051-1d11cb076cf4)

## Update Pickup Actors in the Editor

Your pickups are working in-game, but it can be difficult to visualize them in the editor since they don’t have a default mesh.

To fix this, use the `PostEditChangeProperty()` function. This is an in-editor function that Unreal Engine calls when the editor changes a property, so you can use it to keep your actors up to date in the Viewport as their properties change. For example, updating a UI element as you change a player’s default health, or scaling a sphere as you bring it closer or further away from the origin.

In this project, you’ll use it to apply the pickup’s new static mesh whenever **Pickup Item ID** changes. This way, you can change your pickup type and see it immediately update in the Viewport without needing to click Play!

To make changes to your pickups immediately in the editor, you'll:

- Declare a new `PostEditChangeProperty` function.
- Use `PropertyChangedEvent` information to get the name of the changed property.
- Apply the new property value to your pickup item.

First, to declare PostEditChangeProperty and retrieve the name of the changed property, follow these steps:

1. In `PickupBase.h`, at the end of the `protected` section, declare an `#if WITH_EDITOR` macro. This macro tells Unreal Header Tool that anything inside it should only be packaged for editor builds and not compiled for release versions of the game. End this macro with an `#endif` statement.
2. Inside the macro, declare a virtual void function override for `PostEditChangeProperty()`. This function takes a reference to the `FPropertyChangedEvent`, which includes info about the property changed, the type of change, and more. Save the header file.
3. In `PickupBase.cpp`, implement the `PostEditChangeProperty()` function. Start by calling the `Super::PostEditChangeProperty()` function to handle any parent class property changes.
4. Create a new `const FName` variable named `ChangedProperty` to store the changed property’s name.
5. To verify that the `PropertyChangedEvent` includes a `Property` and save that property, use a ternary operator with `PropertyChangedEvent.Property` as the condition. Set `ChangedPropertyName` to `PropertyChangedEvent.Property->GetFName()` if the condition is true and set it to `NAME_None` if false.

Now that you know the name of the property, you can make Unreal Engine update the mesh if it detected the ID changed. You'll need to check and resolve each soft pointer before using the data, so as a short cut, you can just call `InitializePickup()`.

To update the mesh in the editor preview, follow these steps:

1. In an `if` statement, check that `ChangedPropertyName` is named `PickupItemID` or `PickupDataTable`. To do this, call `GET_MEMBER_NAME_CHECKED()`, passing this `APickupBase` class and either `PickupItemID`. or `PickupDataTable`. This macro does a compile-time check to ensure the property you pass exists in the passed class.
2. Inside the `if` statement, you need to check and resolve the item data, the data asset, and the item's mesh, and then apply the mesh to the pickup. Since you already built the code for that in `InitializePickup()`, call that function.
3. Save your code and compile it from Visual Studio.

Your complete `PostEditChangeProperty()` function should look like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "/*\tUpdates this pickup whenever a property is changed.\n*\t@param PropertyChangedEvent - contains info about the property that was changed. */\nvoid APickupBase::PostEditChangeProperty(FPropertyChangedEvent&amp; PropertyChangedEvent)\n{\n\t// Handle parent class property changes\n\tSuper::PostEditChangeProperty(PropertyChangedEvent);\n\n\t// If a property was changed, get the name of the changed property. Otherwise use none.\n\tconst FName ChangedPropertyName = PropertyChangedEvent.Property \n\t\t? PropertyChangedEvent.Property-&gt;GetFName() \n",
  "lines_of_code": 20,
  "id": 160773,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA3NzMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0ODoxNCswMDowMCJ9--5b793659ef0ce11292a239fab593e64cd2c7d70f1a76839c0a6eba6764cf84e8",
  "settings": {
    "is_hidden": false
  }
}
```

Back in the editor, in the **Outliner**, ensure your **BP\_PickupBase** actor is selected. Change the **Pickup Item ID** from `pickup_001` to `pickup_002`, then change it back. As you change the ID, your pickup’s mesh updates in the Viewport.

![Image](https://dev.epicgames.com/community/api/documentation/image/93570ce9-c467-42f7-9d25-672873535b65)

## Next Up

Next, you’ll extend your pickup class further to create a custom gadget and equip it to your character!

- [Related Document](en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools.md)

## Complete Code

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "PickupBase.h",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;Components/SphereComponent.h&quot;\n#include &quot;AdventureCharacter.h&quot;\n#include &quot;CoreMinimal.h&quot;\n#include &quot;GameFramework/Actor.h&quot;\n#include &quot;PickupBase.generated.h&quot;\n\n",
  "lines_of_code": 76,
  "id": 160774,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA3NzQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0ODoxNCswMDowMCJ9--07ee327a5ebb92b625ac9692544c4a75efd0c4d6e312c2b019ed178d271f1bf4",
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
  "title": "PickupBase.cpp",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#include &quot;PickupBase.h&quot;\n#include &quot;ItemDefinition.h&quot;\n#include &quot;Data/ItemData.h&quot; \n\n// Sets default values\nAPickupBase::APickupBase()\n{\n\n",
  "lines_of_code": 178,
  "id": 160775,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA3NzUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo0ODoxNCswMDowMCJ9--3e312668520c793b9400e675339e957fae923bfdca552c6ccdf3989f60be4b89",
  "settings": {
    "is_hidden": false
  }
}
```
