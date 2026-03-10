# Configure Character Movement

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-03-configure-character-movement-with-cplusplus-in-unreal-engine

> Application Version: 5.7

## Before You Start

Ensure you've completed the following objectives in the previous section, [Create a Player Character With Input Actions](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-02-create-a-player-character-with-input-actions-in-cplusplus):

- Created a Character C++ class.
- Learned how Input Actions and Input Mapping Contexts work.

## Learn to Link Input and Movement

Explore a sample Character Blueprint to learn how Input Actions, Input Mapping Contexts, and code combine to produce movement. Then, learn to replicate that functionality in code.

### Visualize Input in Blueprints

The `BP_FirstPersonCharacter` class that comes with the First Person template is a great example of how Blueprints and Input Actions interact.

In the **Content Browser** asset tree, navigate to **Content > FirstPerson > Blueprints**. Double-click the `BP_FirstPersonCharacter` class to open it in the **Blueprint Editor**.

![Image](https://dev.epicgames.com/community/api/documentation/image/335372f9-9e38-41ea-97f0-73fccce55012)

The Blueprint’s **Event Graph is**in the middle of the **Blueprint Editor**. The **EventGraph** is a node graph that uses events and function calls to perform an ordered series of actions in response to gameplay. In this graph, there’s node groups for **Camera Input**, **Movement Input**, and **Jump Input**.

![Image](https://dev.epicgames.com/community/api/documentation/image/11481b1c-562a-42bf-b656-0c9d0f6501b3)

### Understand Jump Input Logic

Zoom in to the **Jump Input** group. The **EnhancedInputAction IA\_Jump** node represents the `IA_Jump` input action asset you explored in the last step.

![Image](https://dev.epicgames.com/community/api/documentation/image/d2e12589-84af-48de-93ef-02b51519e836)

When the Input Action is triggered, it fires the **Started** and **Triggered** events. The node’s **Started** event leads to a function node named **Jump**. This Blueprint’s parent Character class has built-in jump functionality, and this function is called whenever **IA\_Jump** is triggered by a button press.

When the jump finishes, the node triggers a **Completed** event. This event leads to another function node, **Stop Jumping**, which it also inherits from the Character class.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": " Jump Input logic also adds touch controls, but these aren’t covered in this tutorial.",
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

### Understand Movement Input Logic

Next, look at the **Movement Input** group. This group also starts with a node corresponding to an Input Action, `IA_Move`.

![Image](https://dev.epicgames.com/community/api/documentation/image/974d3c54-f5dc-412f-a425-918f91fedfe6)

The **IA\_Move** node has a **Triggered** event that fires when any buttons bound to `IA_Move` are pressed.

**IA\_Move** also contains **Action Value X** and **Action Value Y**, which are the **X** and **Y** movement values produced by player input. Because the **X** and **Y** values are separate, you need to apply each of them to the character individually.

The **Move** node is a custom function node that applies movement to the character. You can see on the node and in its Details panel that it takes two inputs named Left/Right and Forward/Backward, and IA\_Move’s X and Y movement values are passed into these inputs.

Double-click the Move node or click the **Move** tab above the graph to view the logic inside the function.

![Image](https://dev.epicgames.com/community/api/documentation/image/14748971-a4b3-44eb-ab3f-824690aca03d)

The function starts with a function entry node with its input values.

The **Left/Right** node group contains an **Add Movement Input** function node that adds movement to the character based on two values: **World Direction** and **Scale Value**.

**World Direction** is the direction the character is facing in the world, and the **Scale Value** is the amount of movement to apply. Since this node handles **Left/Right** movement, it uses the **Get Actor** **Right Vector** function node to first get the right vector of the character’s position in the world, and then uses the **Left / Right** input (or the Input Action's X value**)** as the **Scale Value** to apply movement along that vector.

If `Left / Right` is positive, the character moves up the X axis, or to the right. If `Left / Right` is negative, the character moves down the X axis, or to the left.

The **Forward/Backward** group has the same setup as the **Left/Right** group, but instead uses the **Forward / Backward** input (the Input Action's Y value**)** to determine the **Scale Value** along the actor’s **Forward Vector**.

Replicating these nodes in code requires a little more effort but gives precise control over how and where your character moves.

### Assign Input to a Player With a PlayerController

The Input Mapping Context maps player input to Input Actions, but you also need to connect that input context to the player. The default player does this with the PlayerController class and input subsystem.

The PlayerController asset acts as a bridge between the human player and any in-game pawns they are controlling. It receives and processes player input and translates that input into commands, then the Pawn receives those commands and figures out how to perform that movement in the game world. You can use the same PlayerController to control different Pawns.

The PlayerController can also:

- Disable input during cutscenes or menus.
- Track scores or other player data.
- Spawn or hide UI elements

The separation between PlayerController and Character allows for flexibility and data persistence. For example, being able to switch characters (such as when a player dies) without losing player data or input handling logic because this lives within the PlayerController).

To explore how to set this up in Blueprints, back in the **Blueprints** folder in the **Content Browser**, open the `BP_FirstPersonPlayerController` Blueprint.

![Image](https://dev.epicgames.com/community/api/documentation/image/7b104eaa-57a1-4c08-b7cd-9e3100813415)

PlayerController classes have an Enhanced Input Local Player Subsystem. This is a subsystem that is attached to a specific local player and manages that player’s input context and mappings at runtime. Use it to manage what inputs are active and swap between input contexts at runtime. To learn more about UE subsystems, see [Programming Subsystems](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-subsystems-in-unreal-engine).

When the game begins, if the **Enhanced Input Local Player Subsystem** is valid, it calls **Add Mapping Context** to bind the `IMC_Default` Input Mapping Context to the player’s input subsystem. In other words, this group of nodes activates this set of inputs for the player.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "enhanced_list",
      "style": "unordered",
      "items": [
        [
          {
            "type": "paragraph",
            "content": "While this PlayerController logic is in a separate Blueprint from the other movement logic, in C++, you’ll implement this all within the Character class so a second C++ class isn’t necessary.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "<code class=\"inline-code\">BP_FirstPersonCharacter</code>'s event graph shows another way to apply Input Mapping Contexts that involves waiting until the Pawn is possessed. This approach isn't covered in this tutorial, but you can explore it on your own.",
            "settings": {
              "is_hidden": false
            }
          }
        ]
      ],
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

## Set Up Your Character Class

Now that you’ve seen how movement works in Blueprints, it’s time to build it in code, then test out moving your character around the level! You’ll start by adding all necessary modules and `#include` statements, then declare the classes, functions, and properties you’ll need to implement character movement.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "  The code examples in this tutorial use a project named <code class=\"inline-code\">AdventureGame</code> and a Character class named <code class=\"inline-code\">AdventureCharacter</code>.",
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

### Add the Enhanced Input System

You've already ensured the Enhanced Input System is enabled in Unreal Editor, but you'll also have to manually declare it it in your project's `Build.cs` and add certain components to your Character class.

To use the Enhanced Input System in your C++ project, follow these steps:

1. Open your project in Visual Studio and open `[ProjectName].Build.cs` (located in the `Source` folder with your project’s other class files). This file tells Unreal Engine what modules you need to build your project.
2. In the `PublicDependencyModuleNames` function call, add `“EnhancedInput”` to the list of modules:
3. Save and close the `Build.cs` file.

To add Enhanced Input System components to your Character class, follow these steps:

1. Open your Character’s `.h` file. Near the top of the file, add the following include statements: `#include “EnhancedInputComponent.h”` adds the Enhanced Input component module. `#include “InputActionValue.h”` enables access to the Input Action Values produced by your Input Actions. `#include “EnhancedInputSubsystems.h”` enables access to the local player subsystem.
2. After the `#include` statements, declare three new classes: `UInputMappingContext` `UInputAction` `UInputComponent` These classes already exist in the Enhanced Input module. Declaring an existing object like this is called forward declaration and it tells the compiler that the class exists and that you’ll be using it.

### Declare an InputMappingContext Pointer

In the `protected` section of your character’s `.h` file, use `TObjectPtr` to add a new `UInputMappingContext` pointer named `FirstPersonContext`. This is a pointer to the Input Mapping Context that links your Input Actions to button presses.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<code class=\"inline-code\">TObjectPtr</code> is a smart pointer wrapper in Unreal Engine that is a safer way to reference <code class=\"inline-code\">UObject</code>-derived types. It’s an editor-aware, garbage collection-safe replacement for raw <code class=\"inline-code\">UObject</code> pointers. It’s a hard reference, so it keeps the object loaded at runtime. We recommend declaring pointers this way when programming with Unreal Engine.  ",
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

Add the following declaration to the .h file:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UCLASS()\nclass ADVENTUREGAME_API AAdventureCharacter : public ACharacter\n{\n\tGENERATED_BODY()\n\npublic:\n\t// Sets default values for this character&#39;s properties\n\tAAdventureCharacter();\n\nprotected:\n",
  "lines_of_code": 28,
  "id": 160787,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA3ODcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyNyswMDowMCJ9--091e504990c6010e8130d0c8cd29eead04104565cf5812ce52213c7b303ac2b2",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The U prefix identifies the InputMappingContext as a UObject.",
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

The `UPROPERTY()` macro that comes before a variable declaration tells Unreal Engine about that variable. Unreal Header Tool uses the macro to process information about your code and controls where the variable can be accessed, how it appears in the editor, and more.

This pointer has the following `UPROPERTY` values:

- `EditAnywhere`: Exposes the property to Unreal Editor in the class’ **Details** panel.
- `BlueprintReadOnly`: Blueprints can access this property but not edit it.
- `Category = Input`: The property will appear under a section named **Input** in the class’ **Details** panel. Categories are useful for organizing your code and can make navigating the editor much easier.

### Declare Jump and Move InputAction Pointers

Also in the `protected` section, add two `UInputAction` pointers named `MoveAction` and `JumpAction`. These are pointers to the `IA_Jump` and `IA_Move` Input Actions.

Give these the same `UPROPERTY()` macro as `UInputMappingContext`.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "protected:\n\t// Called when the game starts or when spawned\n\tvirtual void BeginPlay() override;\n\n\tUPROPERTY(EditAnywhere, BlueprintReadOnly, Category = Input)\n\tTObjectPtr&lt;UInputMappingContext&gt; FirstPersonContext;\n\n\t// --- New Code Start --- \n\n\t// Move Input Actions\n",
  "lines_of_code": 18,
  "id": 160788,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA3ODgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyNyswMDowMCJ9--9344ccdea410812f52cdb7e07454c3d9af98cea6335318792c4d9358e91b544b",
  "settings": {
    "is_hidden": false
  }
}
```

### Declare the Move() Function

Your Input Actions produce Input Action Values, and you’ll pass these values to a new function that uses these values to apply movement to your character.

In the `public` section of the file, declare a new function named `Move()` that takes a const `FInputActionValue` reference named `Value`.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "public:\t\n\t// Called every frame\n\tvirtual void Tick(float DeltaTime) override;\n\n\t// Called to bind functionality to input\n\tvirtual void SetupPlayerInputComponent(class UInputComponent* PlayerInputComponent) override;\n\n\t// --- New Code Start --- \n\n\t// Handles 2D Movement Input\n",
  "lines_of_code": 16,
  "id": 160789,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA3ODksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyNyswMDowMCJ9--86c608e0e0449dacfec437551db09a26b09da983ee90d20d2c778457777d9e3f",
  "settings": {
    "is_hidden": false
  }
}
```

The `UFUNCTION()` macro that comes before the function declaration makes Unreal Header Tool aware of the function.

Save the file. Your character’s header file should now look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;GameFramework/Character.h&quot;\n#include &quot;EnhancedInputComponent.h&quot;\n#include &quot;EnhancedInputSubsystems.h&quot; \n#include &quot;InputActionValue.h&quot;\n#include &quot;AdventureCharacter.generated.h&quot;\n\nclass UInputMappingContext;\n",
  "lines_of_code": 48,
  "id": 160790,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA3OTAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyNyswMDowMCJ9--2cc81ce1dde921580aab22111fb2d40acc1d6a78e42ec18eea5da6b4fecb2eb9",
  "settings": {
    "is_hidden": false
  }
}
```

## Implement Movement Functions

Now that you’ve declared the properties you need for character movement, in your character’s `.cpp` file, you’ll design your functions to mimic the functionality you saw in the default character’s Blueprint.

### Set up the Move() Function

To start implementing the `Move()` function you declared in your `.h` file, follow these steps:

1. Open your character’s `.cpp` class and add a new function definition for `Move()` at the end of the file.
2. When exploring the default character’s Input Actions, you saw that `IA_Move` has a **Value Type** of **Axis2D (Vector2D)**, so it returns an FVector2D value when triggered. Inside `Move()`, get the value of the `FInputActionValue` and store that inside a new FVector2D named `MovementValue`:
3. Next, before you do anything with that movement value, add an `if` statement to check if the Controller is valid. `Controller` is a pointer to the controller possessing this Actor and it must be valid for movement to work.

### Add 2D Movement Input with Move()

To produce left, right, forward, and backward movement in the Character Blueprint, the event graph added movement input by combining `IA_Move`’s **Action Value X** and **Action Value Y** with the Actor’s right vector and forward vector. You’ll implement this in code within the `Move()` function.

To apply the movement value to the character, follow these steps:

1. Inside the `if` statement, call `GetActorRightVector()` to store the Actor’s right vector in a new `FVector` named `Right`.
2. Then, call `AddMovementInput()` to add movement to the character, passing `Right` and the `MovementValue.X`.
3. Repeat this process for forward and backward movement storing the`GetActorForwardVector()` result in an FVector named `Forward`. Apply the movement with `MovementValue.Y`.

Your complete `Move()` function should look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "void AAdventureCharacter::Move(const FInputActionValue&amp; Value)\n{\n\t// 2D Vector of movement values returned from the input action\n\tconst FVector2D MovementValue = Value.Get&lt;FVector2D&gt;();\n\n\t// Check if the controller posessing this Actor is valid\n\tif (Controller)\n\t{\n\t\t// Add left and right movement\n\t\tconst FVector Right = GetActorRightVector();\n",
  "lines_of_code": 17,
  "id": 160797,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA3OTcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyNyswMDowMCJ9--746bf44518179561575eb34aa64ff0ddf49eec7c573d24304158c35bbb3dacd3",
  "settings": {
    "is_hidden": false
  }
}
```

### Bind Movement to Input with SetupPlayerInputComponent

Next, link your `Move` function to the `FirstPersonContext` input mapping context you declared earlier.

The function for this, `SetupPlayerInputComponent()`, is already defined in your character’s `.cpp` file since it’s inherited from ACharacter. This function takes a UInputComponent and uses it to set up player input.

#### Check for an Enhanced Input Component

By default, your character's `SetupPlayerInputComponent()` function starts with a call to the `SetupPlayerInputComponent()` function from ACharacter which checks if an input component exists on the character.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Called to bind functionality to input\nvoid AAdventureCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)\n{\n\tSuper::SetupPlayerInputComponent(PlayerInputComponent);\n}",
  "lines_of_code": 5,
  "id": 160798,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA3OTgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyNyswMDowMCJ9--43810b29cec85b34df35b3880382d2be3c028a679ebceda4887a1609d764afb6",
  "settings": {
    "is_hidden": false
  }
}
```

This only checks if a regular input component exists on the character, and you need to check if an Enhanced Input component is present instead, so delete this call to the parent class’ `SetupPlayerInputComponent()` function.

Instead, in an if statement, declare a new `UEnhancedInputComponent` pointer named `EnhancedInputComponent`. Set this equal to the result of calling `CastChecked()` on the `PlayerInputComponent` passed to this function while casting it to `UEnhancedInputComponent`.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Called to bind functionality to input\nvoid AAdventureCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)\n{\n\t// --- New Code Start --- \n\tif (UEnhancedInputComponent* EnhancedInputComponent = CastChecked&lt;UEnhancedInputComponent&gt;(PlayerInputComponent))\n\t{\n\n\t}\n\t// --- New Code End --- \n}",
  "lines_of_code": 10,
  "id": 160799,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA3OTksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyNyswMDowMCJ9--534274ba91f46ada4e4c7ba23b425945649bc0a07ecec73120f45c9d169a5db2",
  "settings": {
    "is_hidden": false
  }
}
```

#### Bind Movement Actions

Inside the `if` statement, call the `BindAction()` function from the `EnhancedInputComponent`.

Pass the following arguments to the function:

- `MoveAction`: The input action to bind (declared in the character’s `.h` file).
- `Triggered` event from `ETriggeredEvent` : The type of trigger for the event.
- `this`: The character to bind to.
- `Move()`: A reference to the function you want to bind.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "\tif (UEnhancedInputComponent* EnhancedInputComponent = CastChecked&lt;UEnhancedInputComponent&gt;(PlayerInputComponent))\n\t{\n\t\t// --- New Code Start --- \n\t\t\n\t\t// Bind Movement Actions\n\t\tEnhancedInputComponent-&gt;BindAction(MoveAction, ETriggerEvent::Triggered, this, &amp;AAdventureCharacter::Move);\n\t\t\n\t\t// --- New Code End --- \n\t}",
  "lines_of_code": 9,
  "id": 160800,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA4MDAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyNyswMDowMCJ9--ee495124b90520fee966770e6f9395f287f7125701c656d1ef63cfaa55a4f540",
  "settings": {
    "is_hidden": false
  }
}
```

Now when **IA\_Move** is triggered, it calls the `Move()` function to add movement to your character!

#### Bind Jump Actions

Next, add two bindings to IA\_Jump, one to start jumping and another to stop jumping.

You’ll use the following arguments:

- `JumpAction`, the Input Action pointer to IA\_Jump you declared in the `.h` file.
- `Started` and `Completed` trigger events.
- `Jump` and `StopJumping` functions inherited from and defined in the ACharacter parent class.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "\tif (UEnhancedInputComponent* EnhancedInputComponent = CastChecked&lt;UEnhancedInputComponent&gt;(PlayerInputComponent))\n\t{\n\t\t// Bind Movement Actions\n\t\tEnhancedInputComponent-&gt;BindAction(MoveAction, ETriggerEvent::Triggered, this, &amp;AAdventureCharacter::Move);\n\n\t\t// --- New Code Start --- \n\t\t\n\t\t// Bind Jump Actions\n\t\tEnhancedInputComponent-&gt;BindAction(JumpAction, ETriggerEvent::Started, this, &amp;ACharacter::Jump);\n\t\tEnhancedInputComponent-&gt;BindAction(JumpAction, ETriggerEvent::Completed, this, &amp;ACharacter::StopJumping);\n",
  "lines_of_code": 13,
  "id": 160801,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA4MDEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyNyswMDowMCJ9--5cb5bf9ab376421099660b59384706369d7b0b8c7762dbe21f05e0ce127304da",
  "settings": {
    "is_hidden": false
  }
}
```

Your `SetupPlayerInputComponent()` function should now look like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Called to bind functionality to input\nvoid AAdventureCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)\n{\n\t// Check the UInputComponent passed to this function and cast it to an UEnhancedInputComponent\n\tif (UEnhancedInputComponent* EnhancedInputComponent = CastChecked&lt;UEnhancedInputComponent&gt;(PlayerInputComponent))\n\t{\n\t\t// Bind Movement Actions\n\t\tEnhancedInputComponent-&gt;BindAction(MoveAction, ETriggerEvent::Triggered, this, &amp;AAdventureCharacter::Move);\n\t\t\n\t\t// Bind Jump Actions\n",
  "lines_of_code": 14,
  "id": 160802,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA4MDIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyNyswMDowMCJ9--071e476c4edc984483804fea2f35a34075685bb03ed555ff21d98d8de5dc9957",
  "settings": {
    "is_hidden": false
  }
}
```

### Bind the Input Mapping to the Character

You’ve bound your inputs to your functions, but you still need to bind your input mapping context to your character. You’ll do this in your character’s `BeginPlay()` function so input is set up when the game starts.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<code class=\"inline-code\">BeginPlay()</code> is a virtual function in the parent <code class=\"inline-code\">AActor</code> class, and it's called when the game starts or when an Actor is spawned and fully initialized in the world. Use it for logic that should run once for that Actor at the start of gameplay.",
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

To add the inputs to the player character when the game starts, follow these steps:

1. In `BeginPlay()`, check if the global engine pointer is null before proceeding.
2. In an `if` statement, create a new `APlayerController` pointer named `PlayerController`. Set this to the result of casting `Controller` to `APlayerController`. The `if` statement ensures execution only proceeds if the pointer isn’t null.
3. Now you need to get the Enhanced Input Local Player Subsystem and add the `FirstPersonContext` input mapping context (declared in your `.h` file) to the subsystem. In another `if` statement, create a new `UEnhancedInputLocalPlayerSubsystem` pointer named `Subsystem` by calling `ULocalPlayer::GetSubsystem()`, passing the current player. You can get the current player by calling `PlayerController->GetLocalPlayer()`.
4. Add the mapping context to the subsystem by calling `AddMappingContext()`, passing the mapping context and a priority of `0` to set this mapping context as the highest priority.
5. After both if statements, add a new debug message to verify that your game is using your custom Character class.

Your `BeginPlay()` function should look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Called when the game starts or when spawned\nvoid AAdventureCharacter::BeginPlay()\n{\n\tSuper::BeginPlay();\n\n\tcheck(GEngine != nullptr);\n\n\t// Get the player controller for this character\n\tif (APlayerController* PlayerController = Cast&lt;APlayerController&gt;(Controller))\n\t{\n",
  "lines_of_code": 20,
  "id": 160807,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA4MDcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyNyswMDowMCJ9--a3c6e32a45bef3ec375268ab01b0c5ec0aa8ae1f03015c0b72cf16232e719d4c",
  "settings": {
    "is_hidden": false
  }
}
```

Save your `.h` header and `.cpp` implementation files in Visual Studio, then click **Build** to compile your project.

## Set Variables in the Character Blueprint

To finish setting up these movement controls, use your character’s Blueprint to assign assets to the variables you declared in code.

To populate your Character’s new properties with assets, follow these steps:

1. In Unreal Editor, if it’s not open already, open your Character Blueprint.
2. In the **Details**panel, search for `Input` to filter for that category. ![Image](https://dev.epicgames.com/community/api/documentation/image/44309d7f-b7c1-44b4-bf85-58d80ce6c084)
3. In the **Input** category of properties, set the following properties: Set **First Person Context** to `IMC_Adventure`. Set **Move Action** to `IA_Move`. Set **Jump Action** to `IA_Jump`. ![Image](https://dev.epicgames.com/community/api/documentation/image/e3d6242d-5325-42d1-bb46-aea78fc2fbad)
4. Save your Blueprint and click **Compile** to compile it.

## Test Character Movement

Press **Play** in the **Level Editor Toolbar** to start **Play In Editor** mode. When the game begins, you should see “Hello World!” and “We are using AdventureCharacter” printed on the screen. You should be able to move around using the WASD or arrow keys and jump using the Spacebar!

![Image](https://dev.epicgames.com/community/api/documentation/image/6d149f06-7936-4816-b05d-d7dffb3dfabd)

## Next Up

You have a moving character, but it’s still missing a proper mesh and camera. In the next section, you’ll learn how to create a camera component, bind it to your character, and add skeletal meshes to get a real first-person viewpoint!

- [Related Document](en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation.md)

## Complete Code

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "AdventureCharacter.h",
  "code_preview": "#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;GameFramework/Character.h&quot;\n#include &quot;EnhancedInputComponent.h&quot;\n#include &quot;EnhancedInputSubsystems.h&quot; \n#include &quot;InputActionValue.h&quot;\n#include &quot;AdventureCharacter.generated.h&quot;\n\nclass UInputMappingContext;\n",
  "lines_of_code": 48,
  "id": 160808,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA4MDgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyNyswMDowMCJ9--ba4e6ad133bc54e999eae0c0d66def89b6ded5c93d9992d8b9b0dc0fc192b084",
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
  "code_preview": "#include &quot;AdventureCharacter.h&quot;\n\n// Sets default values\nAAdventureCharacter::AAdventureCharacter()\n{\n \t// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n\tPrimaryActorTick.bCanEverTick = true;\n\n}\n\n",
  "lines_of_code": 73,
  "id": 160809,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA4MDksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyNyswMDowMCJ9--f2076f78ff8ed74dfd26313d9948c3de525db0ca2dd153340b5b5e91c0fb9860",
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
  "title": "AdventureGame.Build.cs",
  "code_preview": "using UnrealBuildTool;\n\npublic class AdventureGame : ModuleRules\n{\n\tpublic AdventureGame(ReadOnlyTargetRules Target) : base(Target)\n\t{\n\t\tPCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;\n\n        PublicDependencyModuleNames.AddRange(new string[] { &quot;Core&quot;, &quot;CoreUObject&quot;, &quot;Engine&quot;, &quot;InputCore&quot;, &quot;EnhancedInput&quot; });\n\n",
  "lines_of_code": 21,
  "id": 160810,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjA4MTAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyNyswMDowMCJ9--04f3026421b2aa4addcf10f56ea39142ee58980270cc9e21fb18590f6d71816b",
  "settings": {
    "is_hidden": false
  }
}
```
