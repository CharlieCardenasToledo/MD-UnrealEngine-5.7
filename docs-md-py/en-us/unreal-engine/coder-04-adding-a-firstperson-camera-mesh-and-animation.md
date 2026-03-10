# Add a First-Person Camera, Mesh, and Animation

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation

> Application Version: 5.7

## Before You Start

Ensure you've completed the following objectives in the previous section, [Configure Character Movement](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-03-configure-character-movement-with-cplusplus-in-unreal-engine):

- Understand how Input Actions and Input Mapping Contexts work.
- Set up a character with forward, backward, left, right, and jump movements.

## First-Person Camera Controls

To change the camera orientation, we change the **Rotation** value of the camera’s **Transform** property. To rotate in a 3D space, objects use **Pitch**, **Roll**, and **Yaw** to control what direction they turn and along what axis.

- **Pitch**: Controls rotation along the horizontal (X) axis. Changing it rotates an object up or down, similar to nodding your head.
- **Yaw**: Controls rotation along the vertical (Y) axis. Changing it rotates an object left or right, similar to rotating right or left.
- **Roll**: Controls rotation along the longitudinal (Z) axis. Changing it rolls an object side to side, similar to leaning your head right or left.

![Image](https://dev.epicgames.com/community/api/documentation/image/b9ab7e88-76a2-46a5-9986-74516d90c03b)

Cameras in first-person games usually use Yaw and Pitch to control movement. Roll may become relevant if you’re programming a game where you need to rotate an airplane or spaceship or if you need to simulate peeking around corners.

### Explore Camera Movement in Blueprints

Open `BP_FirstPersonCharacter` to view the default character’s camera control logic in the **Blueprint Editor**. In the **EventGraph**, look at two nodes in the top-left corner of the **Camera Input** node group.

![Image](https://dev.epicgames.com/community/api/documentation/image/c540ea4d-b631-417f-b45f-de84844d1ba1)

Just like with `IA_Move`, the `IA_Look` input action has an **Axis2D Value Type**, so it splits movement into both **X** and **Y** values. This time, X and Y become the custom **Aim** function's **Yaw** and **Pitch** inputs.

Double-click the **Aim** function node to see the logic inside. The **Add Controller Yaw Input** and **Pitch Input** function nodes add the values to the character.

![Image](https://dev.epicgames.com/community/api/documentation/image/d190be74-4e4f-4d03-b6c9-d6c8b4b0b556)

### Explore First-Person Character Components

Go to `BP_FirstPersonCharacter`‘s **Viewport** tab to view a 3D preview of the Actor and its components.

In the **Components** tab, you’ll see a structured hierarchy of attached components that define the character in the world.

Character Blueprints are automatically instantiated with:

- a **Capsule Component** that makes the character collide with objects in the world.
- a **Skeletal Mesh** component that enables animations and visualizes the character. In the **Details** panel, you’ll see this character uses `SKM_Manny_Simple` as its **Skeletal Mesh Asset**.
- A **Character Movement Component** that allows the character to move around.

![Image](https://dev.epicgames.com/community/api/documentation/image/b2e2edf0-692b-4888-b3a9-a83167cd123e)

This character also has a second **Skeletal Mesh** named **FirstPersonMesh** (also using `SKM_Manny_Simple`) that is a child of the main mesh component. In first-person games, characters usually have separate meshes for both third-person and first-person contexts:

- The third-person mesh is only visible to other players or when the player is in a third-person view.
- The first-person mesh is visible to the player when they are in first-person view.

The **FirstPersonMesh** has a child **Camera Component** named **FirstPersonCamera**. This camera determines the player’s first-person view and rotates with the character as they look around. In this part of the tutorial, you’ll use C++ to instantiate a camera on your character at runtime and position it to match this camera’s position.

For more information about Character components, see the [Characters Gameplay Framework documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/characters-in-unreal-engine).

## Implement Look Input in Code

To implement this camera functionality in code, just like the movement you implemented in the previous step, you’ll bind the `IA_Look` input action to a function and then bind that function to your character.

### Declare the Look() Function and Variables

To declare the function and variables you need to implement and control the camera-look input action, follow these steps:

1. In Visual Studio, open your character’s `.h` file.
2. When your character is built at runtime, you’ll tell UE to add a camera component to it and position the camera dynamically. To enable this functionality, add a new `#include` for `”Camera/CameraComponent.h”`:
3. In the header’s `protected` section, declare a `TObjectPtr` to a `UInputAction` named `LookAction`. Give this pointer the same `UPROPERTY()` macro as `MoveAction` and `JumpAction`. This will point to the `IA_Look` Input Action.
4. In the `public` section, declare a new function named `Look()` that takes a const `FInputActionValue` reference named `Value`. Ensure you add a `UFUNCTION()` macro to the function.
5. After the `Look()` function declaration, declare a `TObjectPtr` to a `UCameraComponent` named `FirstPersonCameraComponent`. To expose this property to Unreal Editor, add a `UPROPERTY()` macro with `VisibleAnywhere` and `Category = Camera` arguments so it appears in the **Camera**section of the **Details**panel.
6. Also in the `public` section, declare an `FVector` named `FirstPersonCameraOffset`. Initialize it to an `FVector` with the default values in the code block below. Include `EditAnywhere` and `Category = Camera` in its `UPROPERTY` macro so you can adjust it in Unreal Editor if needed. This offset positions the camera when the character spawns.
7. You need two more properties to adjust how close-up objects (like the character's body) appear in the camera's view. Declare the following `float` variables: `FirstPersonFieldOfView`: The horizontal field of view (in degrees) that this camera should use when rendering `FirstPerson`-tagged primitive components. Set to `70.0f`. `FirstPersonScale`: The scale this camera should apply to `FirstPerson`-tagged primitive components. Set to `0.6f`. Give these properties a `UPROPERTY` macro with `EditAnywhere` and `Category = Camera` specifiers.
8. Declare a new `TObjectPtr` to a `USkeletalMeshComponent` named `FirstPersonMeshComponent`. Give it a `UPROPERTY()` macro with `VisibleAnywhere` and `Category = Mesh` arguments.
9. Save the file.

You’ve now set up declarations for the following:

- First-person mesh (which correlates to the child **FirstPersonMesh** you saw in the Blueprint)
- Camera component
- `Look()` function
- `IA_Look` Input Action

Your character’s `.h` file should look like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;Camera/CameraComponent.h&quot;\n#include &quot;GameFramework/Character.h&quot;\n#include &quot;EnhancedInputComponent.h&quot;\n#include &quot;EnhancedInputSubsystems.h&quot; \n#include &quot;InputActionValue.h&quot;\n#include &quot;AdventureCharacter.generated.h&quot;\n",
  "lines_of_code": 79,
  "id": 64878,
  "url_signature": "eyJzbmlwcGV0X2lkIjo2NDg3OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjEyOjA5KzAwOjAwIn0=--d504cb10fc782cb42ebb5031797db94e5990d3062d57cb2d4dd3329e1e6289a4",
  "settings": {
    "is_hidden": false
  }
}
```

### Add Look Input with Look()

Now you can implement the Look() function so it applies the Look input action to the player camera position. Just as with `IA_Move`, `IA_Look` returns an FVector2D value when triggered.

To implement the camera input logic, follow these steps:

1. Open your Character Blueprint’s `.cpp` file.
2. Below the `Move()` function, add a new function definition for `Look()`.
3. Inside the function, get the value of the `FInputActionValue` inside a new `FVector2D` named `LookAxisValue`.
4. In an `if` statement, check if the Controller is valid. If it is, call `AddControllerYawInput()` and `AddControllerPitchInput()`, passing the `LookAxisValue.X` and `LookAxisValue.Y` values, respectively.

Your complete `Look()` function should look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "void AAdventureCharacter::Look(const FInputActionValue&amp; Value)\n{\n\tconst FVector2D LookAxisValue = Value.Get&lt;FVector2D&gt;();\n\n\tif (Controller)\n\t{\n\t\tAddControllerYawInput(LookAxisValue.X);\n\t\tAddControllerPitchInput(LookAxisValue.Y);\n\t}\n}",
  "lines_of_code": 10,
  "id": 64880,
  "url_signature": "eyJzbmlwcGV0X2lkIjo2NDg4MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjEyOjA5KzAwOjAwIn0=--20abf92896650f728e3cf08d15f00813f3196c083d43960915a54e8ab1c0f807",
  "settings": {
    "is_hidden": false
  }
}
```

### Bind Look Functionality to Input with SetupPlayerInputComponent

Inside `SetupPlayerInputComponent()`, similar to the movement actions, you’ll bind the `Look()` function to the `LookAction` Input Action.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Called to bind functionality to input\nvoid AAdventureCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)\n{\n\n\tif (UEnhancedInputComponent* EnhancedInputComponent = CastChecked&lt;UEnhancedInputComponent&gt;(PlayerInputComponent))\n\t{\n\t\t// Bind Movement Actions\n\t\tEnhancedInputComponent-&gt;BindAction(MoveAction, ETriggerEvent::Triggered, this, &amp;AAdventureCharacter::Move);\n\t\t\n\t\t// Bind Jump Actions\n",
  "lines_of_code": 22,
  "id": 64881,
  "url_signature": "eyJzbmlwcGV0X2lkIjo2NDg4MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjEyOjA5KzAwOjAwIn0=--10cfc2bd773f4b1fd0798969f648aedf8910d44ec0f11cc01e4563839cbfd122",
  "settings": {
    "is_hidden": false
  }
}
```

Save your code and compile it by clicking **Build** in Visual Studio.

### Assign a Look Input Action in the Blueprint

Last, assign an Input Action to the Character Blueprint’s new **Look Action** property.

To assign look controls to your character, follow these steps:

1. In Unreal Editor, open your Character Blueprint. Click **Compile** in the main editor if the blueprint didn't update with its new properties.
2. In the **Details** panel, in the **Input** section, set **Look Action** to `IA_Look`. ![Image](https://dev.epicgames.com/community/api/documentation/image/96cc4d51-d545-4dcb-a71d-64ef60e7ad93)
3. Compile and save your Blueprint.

### Test Look Movements

If you press **Play** to test out your game, you’ll be able to look around and move your character in any direction you want!

![Image](https://dev.epicgames.com/community/api/documentation/image/08d7cd36-87fb-46ba-b5fd-e40827683874)

Note that while your in-game view appears to come from a first-person camera, you don’t actually have a camera component on your character yet. Instead, Unreal Engine simulates a view from the center of your character’s capsule component. In the next step, you’ll learn to change this by adding a camera to your Character class.

## Create Components at Runtime

Next, you’ll finish creating your character’s first-person mesh and camera by instantiating the `FirstPersonCameraComponent` and `FirstPersonMeshComponent` pointers you declared in the header file.

To get started, return to your character’s `.cpp` file.

At the top of the file, you’ll see the **class constructor** (`AAdventureCharacter()` in this tutorial). This class runs when the object is allocated in memory and it sets the default values for your character. This is where you’ll add additional components.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "When adding code to the class constructor or <code class=\"inline-code\">BeginPlay()</code>, consider when each is executed in the Actor's lifecycle and if other objects are initialized yet. ",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "When the class constructor runs, other components or actors may not exist yet. <code class=\"inline-code\">BeginPlay()</code> runs when when gameplay starts or when the Actor is spawned, so the Actor and all its components are fully initialized and registered, and it's safe to reference other Actors here.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Also, because of the way Unreal Engine handles timing of attachment, physics, networking, or parent-child relationships behind the scenes, some operations behave more reliably when done in <code class=\"inline-code\">BeginPlay()</code>, even if they technically could be done earlier.",
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

### Create a Camera Component

To add components to the Character class, you’ll use the `CreateDefaultSubobject()` template function. It returns a pointer to the new component and takes the following arguments:

`CreateDefaultSubobject<type>(TEXT(“Name”));`

Where *type* is the type of subobject you’re creating and *Name* is the internal name Unreal Engine uses to identify the subobject and display it in the editor.

To add a camera component to the character, follow these steps:

1. In the class constructor, set the `FirstPersonCameraComponent` pointer to the result of calling `CreateDefaultSubobject()` of type `UCameraComponent`. In the `TEXT` argument, name the object ”FirstPersonCamera”. This creates a default camera component as a child component of the Character class.
2. To ensure the camera was properly instantiated, check that `FirstPersonCameraComponent` isn’t null.

### Create a Mesh Component

Set `FirstPersonMeshComponent` to another `CreateDefaultSubobject` function call. This time, use `USkeletalMeshComponent` as the type and “FirstPersonMesh” as the name. Remember to add a `check` afterwards.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Sets default values\nAAdventureCharacter::AAdventureCharacter()\n{\n \t// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n\tPrimaryActorTick.bCanEverTick = true;\n \n\tFirstPersonCameraComponent = CreateDefaultSubobject&lt;UCameraComponent&gt;(TEXT(&quot;FirstPersonCamera&quot;));\n\tcheck(FirstPersonCameraComponent != nullptr);\n\n\t// --- New Code Start ---\n",
  "lines_of_code": 17,
  "id": 64885,
  "url_signature": "eyJzbmlwcGV0X2lkIjo2NDg4NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjEyOjA5KzAwOjAwIn0=--8a8f455a3e1c7e25cb8d80313f41e065112dc39a67d717b12f1032b40d0d63ef",
  "settings": {
    "is_hidden": false
  }
}
```

### Attach and Configure the Mesh

Now that your mesh is created, attach it to the character and enable first-person rendering on it.

In these steps, you'll use the `SetupAttachment()` function, which attaches one scene component to another, establishing a parent-child relationship in the component hierarchy.

To set up the player mesh, follow these steps:

1. In the class constructor, call the `SetupAttachment()` function on the object that `FirstPersonMeshComponent` points to and pass it the parent component. In this case, the parent should be the character’s default skeletal mesh, which you can get using `GetMesh()`.
2. In the character's header file, you declared a camera field of view and scale to use for components close to the camera. To make these camera properties apply to the first-person mesh, set the mesh's `FirstPersonPrimitiveType` property to `FirstPerson`.
3. Set the first-person mesh collision profile name to `NoCollision` to prevent the first-person mesh from colliding with the environment. The first-person mesh should only provide camera-space visuals for the owning player. The Character Blueprint's Capsule Component provides a simpler collision shape.
4. Your first-person camera settings shouldn't apply to the third-person mesh, so set the third-person mesh component's `FirstPersonPrimitiveType` to `WorldSpaceRepresentation`.

### Set Mesh and Shadow Visibility

So far, your character has a first and third-person skeletal mesh that overlap during gameplay. However, the first-person mesh should be invisible to other players and the third-person mesh should be invisible to you, the player.

To configure first-person and third-person mesh visibility, follow these steps:

1. In `BeginPlay()`, after the global engine pointer check, call `SetOnlyOwnerSee()` on `FirstPersonMeshComponent`, passing `true` to make the first-person mesh visible only to the owning player.
2. For the third-person mesh, use `SetOwnerNoSee()` to hide the mesh from the owning player.
3. You've set up the character's first-person mesh as a first-person primitive, which is rendered in the camera-space first-person rendering pass and therefore doesn't contribute to world shadows. To give the character a shadow, enable the `CastShadow` and `bCastHiddenShadow` properties on the third-person mesh, since that mesh is a regular world object and participates in world shadow rendering.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "In general, initialization belongs in the constructor, but these actions work more reliably in <code>BeginPlay()</code>.  ",
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

### Attach the Camera Component

The `SKM_Manny_Simple` skeletal mesh used in this tutorial has a collection of preset **sockets** (or bones) used for animation. To attach components to the character mesh, you'll use a socket as an attachment point. 
Each socket has a name, so you can reference sockets in code using an `FName` string.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "<code class=\"inline-code\">FName</code> is a special string-like type used in Unreal Engine to store unique, immutable names in a memory-efficient way.",
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

It’s best to position the camera near the character’s head, so you’ll pass the `Head` socket name to `SetupAttachment()` to attach the camera to that socket. You’ll move the camera closer to the character’s eyes next.

In the character's constructor, use another `SetupAttachment()` call to attach the camera component to the first-person mesh.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Sets default values\nAAdventureCharacter::AAdventureCharacter()\n{\n \t// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n\tPrimaryActorTick.bCanEverTick = true;\n \n\tFirstPersonCameraComponent = CreateDefaultSubobject&lt;UCameraComponent&gt;(TEXT(&quot;FirstPersonCamera&quot;));\n\tcheck(FirstPersonCameraComponent != nullptr);\n\t\n\t// Create a first person mesh component for the owning player.\n",
  "lines_of_code": 27,
  "id": 64890,
  "url_signature": "eyJzbmlwcGV0X2lkIjo2NDg5MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjEyOjA5KzAwOjAwIn0=--eb61ba4b4092a665d72edeea7c4890807cf56a190dd863ac4dd4ef00c49cb4b3",
  "settings": {
    "is_hidden": false
  }
}
```

For more information about what sockets are and how they’re created, see [Skeletal Mesh Sockets](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-sockets-in-unreal-engine).

### Configure the Camera

When you initialized your camera component, you attached it to the character’s Head socket. However, the camera looks more accurate when it’s positioned at the character’s eyes. The camera is also pointing down by default, so you'll need to rotate it behind the character's head.

To finish setting up the player camera, follow these steps:

1. To move and rotate the camera into position, after the camera's `SetupAttachment` line in the class constructor, call `SetRelativeLocationAndRotation()`, passing the `FirstPersonCameraOffset` and a new `FRotator` set to `(0.0f, 90.0f, -90.0f)`.
2. To make the camera rotate with the character during gameplay, set `FirstPersonCameraComponent`'s `bUsePawnControlRotation` property to `true`. This makes the camera inherit rotation from its parent Pawn so when the character turns, the camera follows.
3. Apply your First Person Field of View and First Person Scale rendering values to the camera component's corresponding settings. Set the component's `bEnableFirstPersonFieldOfView` and `bEnableFirstPersonScale` properties to `true`. Then, assign the default FOV and scale values you declared earlier.
4. Save and compile your code.

Your character’s constructor should look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Sets default values\nAAdventureCharacter::AAdventureCharacter()\n{\n\t// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it\n\tPrimaryActorTick.bCanEverTick = true;\n\n\t// Create a first person camera component\n\tFirstPersonCameraComponent = CreateDefaultSubobject&lt;UCameraComponent&gt;(TEXT(&quot;FirstPersonCamera&quot;));\n\tcheck(FirstPersonCameraComponent != nullptr);\n\n",
  "lines_of_code": 38,
  "id": 64894,
  "url_signature": "eyJzbmlwcGV0X2lkIjo2NDg5NCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjEyOjA5KzAwOjAwIn0=--3019cbbfdad4d6711f3e510436a0ff600aa109fd566b19fdd56b0f267ecdc941",
  "settings": {
    "is_hidden": false
  }
}
```

## Assign Meshes in Unreal Editor

Your camera controls are set up, but you still have one step left — use the editor to add the Skeletal Mesh assets to the variables you declared in code.

To add a Skeletal Mesh to a Character Blueprint, follow these steps:

1. In Unreal Editor, if it’s not open already, open your Character Blueprint.
2. So far, Unreal Engine has likely categorized your Blueprint as a Data-Only Blueprint Class and only displays a list of properties in the Blueprint Editor. To convert the asset to a regular Blueprint Class, click the **Open Full Blueprint Editor** link in the **NOTE** above the list of properties. ![Image](https://dev.epicgames.com/community/api/documentation/image/4e7b986f-9170-4fb3-a8b9-cd72347d20ce)
3. Click the **Viewport** tab so you can see a preview of the character and its components.
4. In the **Components** panel, ensure the root **BP\_*[CharacterName]*** is selected.
5. In the Blueprint Editor, click **Compile** to make your character's new components appear in the **Components** panel. ![Image](https://dev.epicgames.com/community/api/documentation/image/1c81a7b2-8267-4346-b4e0-dc38604cf39a)
6. In the **Details** panel, in the **Mesh** section, your character has two **Skeletal Mesh Asset** slots instead of one because you created `FirstPersonMeshComponent` in code. Click the arrow in each property’s dropdown menu and select `SKM_Manny_Simple` for both meshes. ![Image](https://dev.epicgames.com/community/api/documentation/image/6c5113a8-b280-4fe1-8fbc-f29972de6a3f) When you set the **FirstPersonMeshComponent**, your camera should move into position behind the character’s head.
7. As a final adjustment, use the Blueprint Editor to transform the character's mesh so it's inside the Capsule Component and facing the same direction as the Arrow Component: In the **Components** panel, select the root. In the **Details** panel, In the **Transform > Mesh** section, change the **Rotation**'s **Z** value to `-90`. Change the **Location**'s Z value to `-95`. ![Image](https://dev.epicgames.com/community/api/documentation/image/50a75665-c900-4851-ab45-0bdab8f6bc10)
8. Save your Blueprint and click **Compile**.

If you play your game and look down, you should see the first-person mesh on your character! The mesh rotates as you look around, and your camera matches that movement. The third-person mesh is hidden at runtime and only other players can see it.

However, your character is still in a static T-pose, so next you'll use an Animation Blueprint to add animations to your character and finish bringing it to life!

## Add Animations to Your Character

In code, you can access animation logic through instances of the **UAnimInstance** class, which is a controller that determines what animations are blended and played on a Skeletal Mesh based on state and other variables. Animation Blueprints also derive from `UAnimInstance`, and you can reference them in C++ with the `UAnimBlueprint` type.

Building an Anim Instance class is outside the scope of this tutorial; instead, you’ll add the First Person template’s prebuilt Animation Blueprint to your character. This Blueprint includes the animations and logic your character needs to play different movement and idle animations.

Animations in Unreal Engine are set on a per-mesh basis, so you’ll need separate animations for both your first and third-person meshes. Because your third-person mesh is hidden when the game begins, you only need to set animations on the first-person mesh.

To add an animation property and Animation Blueprint to your character, follow these steps:

1. At the top of your character's `.h` file, forward-declare the `UAnimBlueprint` class. This class represents the Animation Blueprints in your project.
2. In the `public` section, declare a `TObjectPtr` to a `UAnimBlueprint` named `FirstPersonDefaultAnim`. Give it the `UCLASS()` macro with `EditAnywhere` and `Category = Animation`.
3. In your character's `.cpp` file, in `BeginPlay()` after the `check` line, call `FirstPersonMeshComponent->SetAnimInstanceClass()`. Even though you haven’t defined an Anim Instance class in code, you can generate a class from the Animation Blueprint using `GeneratedClass`.
4. On the next line, call `SetAnimInstanceClass()` again to assign the AnimInstance to the third-person mesh so if you create a multi-player game, other players will see your character animating.
5. Save your code and compile it from Visual Studio.
6. In Unreal Editor, return to your Character Blueprint, compile it, and select the root **BP\_*[CharacterName]***component.
7. In the **Details** panel, under **Animation**, set the **First Person Default Anim** to `ABP_Unarmed`. ![Image](https://dev.epicgames.com/community/api/documentation/image/9efb584b-d6c4-4bf8-b759-6d64804bff27)
8. Save your Blueprint and compile it.

## Test Your Character

Press **Play** to test out your game. If you look down, you'll see the first-person mesh animate as you move! Try moving around and jumping to see the different animations controlled by this Blueprint.

![Image](https://dev.epicgames.com/community/api/documentation/image/1aa18e06-e960-4c7d-92eb-8a9a34635932)

## Next Up

In the next section, you’ll learn how to create an item for your character to pick up and use!

- [Related Document](en-us/unreal-engine/coder-05-manage-item-and-data-in-an-unreal-engine-game.md)

## Complete Code

Here is the complete code built in this section:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "AdventureCharacter.h",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;Camera/CameraComponent.h&quot;\n#include &quot;GameFramework/Character.h&quot;\n#include &quot;EnhancedInputComponent.h&quot;\n#include &quot;EnhancedInputSubsystems.h&quot; \n#include &quot;InputActionValue.h&quot;\n",
  "lines_of_code": 85,
  "id": 64898,
  "url_signature": "eyJzbmlwcGV0X2lkIjo2NDg5OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjEyOjA5KzAwOjAwIn0=--8c2b241f2b0814abaea5d2979ad09ed43399e7eafa1211548f86535d05ffed62",
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
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n\n#include &quot;AdventureCharacter.h&quot;\n\n// Sets default values\nAAdventureCharacter::AAdventureCharacter()\n{\n\t// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it\n\tPrimaryActorTick.bCanEverTick = true;\n",
  "lines_of_code": 143,
  "id": 64899,
  "url_signature": "eyJzbmlwcGV0X2lkIjo2NDg5OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjEyOjA5KzAwOjAwIn0=--37589951e901af8be3fc281b96b31789b1606481dc8524f76ead928962a832b7",
  "settings": {
    "is_hidden": false
  }
}
```
