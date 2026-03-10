# Implement a Projectile

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine

> Application Version: 5.7

## Before You Begin

Ensure you’ve completed the following objectives in the previous section, [Equip Your Character](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools):

- Created a respawning pickup item and added it to your level
- Created an equippable dart launcher for your character to hold and use

## Basic Projectiles

Your character can hold your dart launcher, and your tool has control bindings to use it, but it’s not quite living up to its name. In this section, you’ll implement projectile logic to make darts launch out from the equipped item.

Unreal Engine has a **Projectile Movement** component class that you can add to an actor to turn it into a projectile. It includes many helpful variables, such as projectile speed, bounciness, and gravity scale.

To handle the math of implementing projectiles, you’ll need to think about several things:

- The initial transform, velocity, and direction of the projectile.
- Whether you want to spawn projectiles from the center of the character or the tool they have equipped.
- What behavior you want the projectile to exhibit when it collides with another object.

## Create a Projectile Base Class

You’ll first create a base projectile class, and then subclass from it to create unique projectiles for your tools.

To start setting up a base projectile class, follow these steps:

1. In the Unreal Editor, go to **Tools > New C++ Class**. Select **Actor** as the parent class and name the class `FirstPersonProjectile`. Click **Create Class**.
2. In VS, go to `FirstPersonProjectile.h`. At the top of the file, forward declare both a `UProjectileMovementComponent` and a `USphereComponent`. You’ll use a simple sphere component to simulate collisions between the projectile and other objects.
3. Add the `BlueprintType` and `Blueprintable` specifiers to expose this class to Blueprints:
4. Open `FirstPersonProjectile.cpp`, at the top of the file, add an include statement for `"GameFramework/ProjectileMovementComponent.h"` and `"Components/SphereComponent.h"` to include the projectile movement and collision component classes.

### Implement Projectile Behavior When Hitting Objects

To make your projectile more realistic, you can make it exert some force (an impulse) on objects it hits. For example, if you are shooting at a physics-enabled block, the projectile would nudge the block along the ground. Then, remove the projectile after impact instead of letting it live out its default lifespan. Create an `OnHit()` function to implement this behavior.

To implement projectile on-hit behavior, follow these steps:

1. In `FirstPersonProjectile.h`, in the `public` section, define a `float` property named `PhysicsForce`. Give it a `UPROPERTY()` macro with `EditAnywhere`, `BlueprintReadOnly`, and `Category = “Projectile | Physics”`. This is the amount of force the projectile imparts when it hits something.
2. Define a `void` function `OnHit()`. This is a function from AActor that's called when the actor collides with another component or actor. It takes the following arguments: `HitComp`: The component that was hit. `OtherActor`: The actor that was hit. `OtherComp`: The component that created the hit (in this case, the projectile’s CollisionComponent). `NormalImpulse`: The normal impulse of the hit. `Hit`: A `FHitResult` reference that contains more data about the hit event such as time, distance, and location.
3. In `FirstPersonProjectile.cpp`, implement the `OnHit()` function you defined in your header file. Inside `OnHit()`, in an `if` statement, check that: `OtherActor` isn't null and isn't the projectile itself. `OtherComp` isn't null and is also simulating physics. This checks that the projectile hit an object that wasn’t itself and participates in physics.
4. Inside the `if` statement, use `AddImpulseAtLocation()` to add an impulse to the `OtherComp` component. Pass this function the velocity of the projectile multiplied by the `PhysicsForce` and apply it at the location of the projectile actor.
5. Since this projectile hit another actor, remove the projectile from the scene by calling `Destroy()`.

Your complete `OnHit()` function should look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "void AFirstPersonProjectile::OnHit(UPrimitiveComponent* HitComp, AActor* OtherActor, UPrimitiveComponent* OtherComp, FVector NormalImpulse, const FHitResult&amp; Hit)\n{\n\t// Only add impulse and destroy projectile if we hit a physics\n\tif ((OtherActor != nullptr) &amp;&amp; (OtherActor != this) &amp;&amp; (OtherComp != nullptr) &amp;&amp; OtherComp-&gt;IsSimulatingPhysics())\n\t{\n\t\tOtherComp-&gt;AddImpulseAtLocation(GetVelocity() * PhysicsForce, GetActorLocation());\n\n\t\tDestroy();\n\t}\n}",
  "lines_of_code": 10,
  "id": 163662,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM2NjIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODo1NyswMDowMCJ9--8ed4facd4427be5d1d654119aba085af58f928e6a3b905d2669e0fec05a1412b",
  "settings": {
    "is_hidden": false
  }
}
```

### Add the Projectile’s Mesh, Movement, Collision Components

Next, add a static mesh, projectile movement logic, and a collision sphere to your projectile and define how the projectile should move.

To add these components to your projectile, follow these steps:

1. In `FirstPersonProjectile.h`, in the `public` section, declare a `TObjectPtr` to a `UStaticMeshComponent` named `ProjectileMesh`. This is the static mesh of the projectile in the world. Give it a `UPROPERTY()` macro with `EditAnywhere`, `BlueprintReadOnly`, and `Category = “Projectile | Mesh“`.
2. In the `protected` section, declare: A `TObjectPtr` to a `USphereComponent` named `CollisionComponent`. A `TObjectPtr` to a `UProjectileMovementComponent` named `ProjectileMovement`. Give both of these a `UPROPERTY()` macro with `VisibleAnywhere`, `BlueprintReadOnly`, and `Category = “Projectile | Components”`. The `ProjectileMovementComponent` handles movement logic for you. It calculates where its parent Actor should go based on velocity, gravity, and other variables. Then, during `tick`, it applies the movement to the projectile.
3. In `FirstPersonProjectile.cpp`, in the `AFirstPersonProjectile()` constructor function, create default subobjects for the projectile’s mesh, collision, and projectile movement components. Then, attach the projectile mesh to the collision component.
4. Call `InitSphereRadius()` to initialize the `CollisionComponent` size.
5. Set the name of the collision component’s collision profile to `”Projectile”` using `BodyInstance.SetCollisionProfileName()`. In Unreal Editor, your collision profiles are stored under **Project Settings** > **Engine** > **Collision**, and you can define up to 18 custom collision profiles to use in code. The default behavior of this ”Projectile” collision profile is **Block**, and this creates collisions on any object it collides with.
6. You defined an `OnHit()` function earlier to activate when the projectile hits something, but you need a way to notify when that collision occurs. To do this, use the `AddDynamic()` macro to subscribe a function to `OnComponentHitEvent` in `CollisionComponent`. Pass this macro the `OnHit()` function.
7. Set the `CollisionComponent` as the projectile’s `RootComponent` and as the `UpdatedComponent` for the movement component to track.
8. Initialize the `ProjectileMovement` component with the following values: `InitialSpeed`: The initial speed of the projectile when it spawns. Set this to `3000.0f`. `MaxSpeed`: The maximum speed of the projectile. Set this to `3000.0f`. `bRotationFollowVelocity`: Whether the object should rotate to make the direction of its velocity. For example, how a paper airplane dips up and down as it rises and falls. Set this to `true`. `bShouldBounce`: Whether the projectile should bounce off obstacles. Set this to `true`. `Bounciness`: How much velocity is preserved after a collision, where lower values cause the projectile to lose more energy. Set this to `0.4f`. Friction: How much tangential (sideways) velocity is preserved after impact. Set this to `0.8f`.

### Set the Projectile’s Lifespan

By default, you’ll make the projectile disappear a few seconds after firing it. However, once you derive your projectile Blueprints in the editor, you can experiment with changing or removing this default time to try filling your level up with foam darts!

To make the projectile disappear after a number of seconds, follow these steps:

1. In `FirstPersonProjectile.h`, in the `public` section, declare a float named `ProjectileLifespan`. Give it a `UPROPERTY()` macro with `EditAnywhere`, `BlueprintReadOnly`, and `Category = “Projectile | Lifespan”`. This is the lifespan of the projectile in seconds.
2. In `FirstPersonProjectile.cpp`, at the end of the `AFirstPersonProjectile()` constructor function, set the `InitialLifeSpan` of the projectile to `ProjectileLifespan` to make it disappear after five seconds.

Your complete `FirstPersonProjectile.h` should look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;GameFramework/Actor.h&quot;\n#include &quot;FirstPersonProjectile.generated.h&quot;\n\nclass UProjectileMovementComponent;\nclass USphereComponent;\n",
  "lines_of_code": 53,
  "id": 163673,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM2NzMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODo1NyswMDowMCJ9--f0450b27c99f520f7dd2379249db60cb261b90a4f8e56710c50dad92c4dc1b26",
  "settings": {
    "is_hidden": false
  }
}
```

Your complete `AFirstPersonProjectile.cpp` should look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#include &quot;FirstPersonProjectile.h&quot;\n#include &quot;GameFramework/ProjectileMovementComponent.h&quot;\n#include &quot;Components/SphereComponent.h&quot;\n\n// Sets default values\nAFirstPersonProjectile::AFirstPersonProjectile()\n{\n \t// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n",
  "lines_of_code": 75,
  "id": 163674,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM2NzQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODo1NyswMDowMCJ9--3bfd6122091c5e54addaeb9e78a1e1cc8e940dcb85fdf50f796811eb961d011e",
  "settings": {
    "is_hidden": false
  }
}
```

## Get the Character Camera Direction

Projectiles should spawn from the dart launcher itself, so you’ll need to do some math to know where the dart launcher is and where it’s pointing. Since the launcher is attached to the player character, these values are going to change based on where the character is and where they’re looking.

Your first-person character contains some of the positional information you need to launch a dart, so start by modifying your Character class to capture that information with a line trace and return the result.

To use a trace to get the information you need from your character, follow these steps:

1. In VS, open your Character’s `.h` and `.cpp` files.
2. In the `.h` file, in the `public` section, declare a new function named `GetCameraTargetLocation()` that returns an `FVector`. This function will return the location in the world that the character is looking at.
3. In your character's `.cpp` file, implement the `GetCameraTargetLocation()` function. Start by declaring an `FVector` named `TargetPosition` to return.
4. Create a pointer to `UWorld` by calling `GetWorld()`.
5. Add an `if` statement to check that `World` isn’t null. In the `if` statement, declare a `FHitResult` named `Hit`.
6. To find the point that your character is looking at, you’re going to simulate a line trace along the vector the character is looking down to some distant point. If the line trace collides with an object, you know where in the world your character is looking. In the if statement, declare two `const FVector` values named `TraceStart` and `TraceEnd`: Set `TraceStart` to the location of the `FirstPersonCameraComponent`. Set `TraceEnd` to `TraceStart` plus the forward vector of the camera component multiplied by a very large number. This ensures that the trace will go far enough to collide with most objects in your world as long as your character isn’t staring at the sky. (If the character is looking at the sky, `TraceEnd` is the terminal point of the line trace.)
7. Call `LineTraceSingleByChannel()` from the `UWorld` to simulate the trace. Pass it `Hit`, `TraceStart`, `TraceEnd`, and an `ECollisionChannel::ECC_Visibility`. This simulates a line trace from `TraceStart` to `TraceEnd`, colliding with any visible objects and storing the result of the trace in `Hit`. `ECollisionChannel::ECC_Visibility` is the channel to use for tracing, and these channels define what types of objects your trace should try to hit. Use `ECC_Visibility` for line-of-sight camera checks. The `Hit` value now contains information about the hit result, such as the location and normal of the impact. It also knows if the hit was a result of an object collision. The location of impact (or the end point of the trace line) is the camera target location to return.
8. Use a ternary operator to set `TargetPosition` to either the `Hit.ImpactPoint` if the hit was a blocking hit and `Hit.TraceEnd` if not. Then, return the `TargetPosition`.

Your complete `GetCameraTargetLocation()` function should look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FVector AAdventureCharacter::GetCameraTargetLocation()\n{\n\t// The target position to return\n\tFVector TargetPosition;\n\n\tUWorld* const World = GetWorld();\n\n\tif (World != nullptr)\n\t{\n\t\t// The result of the line trace\n",
  "lines_of_code": 25,
  "id": 163682,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM2ODIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODo1NyswMDowMCJ9--4dc0886c4041e7201379c7e29ae972b623d846f6c40ff4ee29124c26ea2d0c0f",
  "settings": {
    "is_hidden": false
  }
}
```

## Spawn Projectiles with DartLauncher::Use()

Now that you have a way to know where the character is looking, you can implement the rest of the projectile logic in your dart launcher’s `Use()` function. You’ll get the location and direction to launch the projectile, then spawn the projectile.

To get the location and rotation the projectile should spawn at, follow these steps:

1. In `DartLauncher.h`, at the top of the file, add a forward declaration for `AFirstPersonProjectile`.
2. In the `public` section, declare a `TSubclassOf<AFirstPersonProjectile>` property named `ProjectileClass`. This will be the projectile that the dart launcher spawns. Give this the `UPROPERTY()` macro with `EditAnywhere` and `Category = "Projectile"`. `DartLauncher.h` should now look like the following:
3. `DartLauncher.cpp`, add include statements for: `”Kismet/KismetMathLibrary.h”`. Projectile math can be complicated, and this file includes several functions you’ll use for launching projectiles. `"FirstPersonProjectile.h"` `"EnhancedInputComponent.h"`
4. In the DartLauncher’s `Use()` implementation, after the debug message: Get the `UWorld` by calling `GetWorld()`. Add an `if` statement to check that `World` and the `ProjectileClass` are not null. In the `if` statement, get the position the character is looking at by calling `OwningCharacter->GetCameraTargetLocation()`.
5. Projectiles should spawn from the tool the character is holding, but not from the center of the equipped object. The dart launcher’s `SKM_Pistol` mesh has a ”Muzzle” socket you can use to set a precise spawn point for your darts. In the `if` statement, declare a new `FVector` named `SocketLocation` and set it to the result of calling `GetSocketLocation(“Muzzle”)` on the `ToolMeshComponent`.
6. Declare an `FRotator` named `SpawnRotation`. This is the rotation (pitch, yaw, and roll values) of the projectile as it spawns. Set this to the result of calling `FindLookAtRotation()` from the kismet math library, passing the `SocketLocation` and `TargetPosition` you got from the player character. `FindLookAtRotation` calculates and returns the rotation you’d need at `SocketLocation` to face `TargetPosition`.
7. Declare an `FVector` named `SpawnLocation`, and set it to the result of adding the `SocketLocation` and the forward vector of the `SpawnRotation` multiplied by `10.0`.

Now that you’ve got a location and rotation, you’re ready to spawn the projectile.

To spawn a projectile, follow these steps:

1. Still in the `Use()` function, in the `if` statement, declare a `FActorSpawnParameters` named `ActorSpawnParams`. This class includes information about where and how to spawn the actor.
2. Set the `SpawnCollisionHandlingOverride` value in `ActorSpawnParams` to `ESpawnActorCollisionHandlingMethod::AdjustIfPossibleButDontSpawnIfColliding`. This line of code tries to find a place to spawn the projectile where it isn’t colliding with another Actor (such as inside a wall) and won’t spawn it if a suitable location isn’t found.
3. Use `SpawnActor()` to spawn the projectile at the muzzle of the dart launcher, passing `ProjectileClass`, `SpawnLocation`, `SpawnRotation`, and `ActorSpawnParams`.

Your complete `Use()` function should now look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "void ADartLauncher::Use()\n{\n\tGEngine-&gt;AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT(&quot;Using the dart launcher!&quot;));\n\n\tUWorld* const World = GetWorld();\n\tif (World != nullptr &amp;&amp; ProjectileClass != nullptr)\n\t{\n\t\tFVector TargetPosition = OwningCharacter-&gt;GetCameraTargetLocation();\n\t\t\t\n\t\t// Get the correct socket to spawn the projectile from\n",
  "lines_of_code": 22,
  "id": 163692,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM2OTIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODo1NyswMDowMCJ9--bc422ef4d949a8e1fc916ad779d609555bdcf72fcdff627a36e9fe1801a77ba7",
  "settings": {
    "is_hidden": false
  }
}
```

## Derive a Foam Dart Class and Blueprint

Now that all the spawning logic is done, it’s time to build a real projectile! Your dart launcher class needs a subclass of `AFirstPersonProjectile` to launch, so you’ll need to build one in code to use in your level.

To derive a foam dart projectile class to use in-game, follow these steps:

1. In Unreal Editor, go to **Tools > New C++ Class**.
2. Go to **All Classes**, search for and select **First Person Projectile** as the parent class, and name the class `FoamDart`. Click **Create Class**. ![Image](https://dev.epicgames.com/community/api/documentation/image/ae41edfd-1522-4175-a05c-0594e642e7a2)
3. In VS, leave these files as-is, save your code, and compile it.

In this tutorial, you won’t be implementing any custom projectile code beyond what you defined in `FirstPersonProjectile`, but you can modify the `FoamDart` class on your own to suit the needs of your project. For example, you could try making the dart projectiles stick to objects instead of disappearing or bouncing around.

To create a foam dart Blueprint, follow these steps:

1. In Unreal Editor, create a Blueprint class based on **FoamDart** and name it `BP_FoamDart`. Save this in your `FirstPerson/Blueprints/Tools` folder. ![Image](https://dev.epicgames.com/community/api/documentation/image/5f6c7328-0a6e-4e60-9559-94d290f92506)
2. With the Blueprint open, select the **Projectile Mesh** component and set the **Static Mesh** to `SM_FoamBullet`. ![Image](https://dev.epicgames.com/community/api/documentation/image/9f2f6022-fc58-427d-aca4-248c455c0cb2)
3. The foam dart mesh appears in the **Viewport**. Zoom in or press **F** to look at the orientation of the mesh. The rounded end is the front of the dart, and it should be pointing up the X axis so your darts fire in the correct orientation (`ProjectileMovement` assumes +X is forward). Rotate the dart on the Z (blue) axis +90 degrees.
4. Compile and save your Blueprint.
5. In the **Content Browser**, open **`BP_DartLauncher`**.
6. In its **Details** panel, in the new **Projectile** section, set the **Projectile Class**to `BP_FoamDart`. ![Image](https://dev.epicgames.com/community/api/documentation/image/8de5f4e5-4d59-408c-aff3-064c2efcbaf2)
7. Click **Compile** and **Save**.

It’s time for the big reveal. Save your assets and click **Play**. When the game begins, you can run to the dart launcher to pick it up. Pressing the left mouse button spawns a projectile from the muzzle of the dart launcher and bounces it around the level! These projectiles should disappear after five seconds and impart a small physics force on objects they collide with (including you!).

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If the dart launcher doesn't fire and you don't see the \"Using the dart launcher!\" debug message, ensure you've assigned <code class=\"inline-code\">IA_UseTool</code> to the <b>Use Action</b> property in your character's Blueprint.",
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

## Bonus: Adjust Projectiles and Tools

Optionally implement these final adjustments to make your dart launcher and darts look their best.

#### Make Fallen Projectiles Lie Flat

In `FirstPersonProjectile.cpp`, when the projectile hits something, check if the projectile has hit the ground (a flat horizontal surface) and if it has, make it lie flat.

At the top of `OnHit()`, add this code:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// If we hit the ground (mostly-up surface normal), lay the dart flat.\nif (FVector::DotProduct(Hit.ImpactNormal, FVector::UpVector) &gt; 0.7f)\n{\n    FRotator Flat = GetActorRotation();\n    Flat.Pitch = 0.f;\n    Flat.Roll = 0.f;\n    SetActorRotation(Flat);\n\n    return;\n}",
  "lines_of_code": 10,
  "id": 163693,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM2OTMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODo1NyswMDowMCJ9--549fcfec881bd2430b14c7ec2e4b8729f991f2f2869a98f317517351ec2cf8ec",
  "settings": {
    "is_hidden": false
  }
}
```

## Next Up

Congratulations! You’ve completed the First-Person Programmer Track tutorial and learned a lot along the way!

You’ve implemented custom characters and movement, created pickups and data assets, and even made equippable tools with their own projectiles. You’ve got everything you need to take this project and turn it into something all your own.

Here are a few suggestions:

- Can you expand the player’s inventory with different types of items? What about stacks of items?
- Can you combine pickups and projectiles to create pickupable ammo? How about implementing this ammo system in the dart launcher?
- Can you develop the idea of consumables into equippable consumables? How about a health pack the player holds, or a ball they can pick up and throw?

## Complete Code

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "FirstPersonProjectile.h",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;GameFramework/Actor.h&quot;\n#include &quot;FirstPersonProjectile.generated.h&quot;\n\nclass UProjectileMovementComponent;\nclass USphereComponent;\n",
  "lines_of_code": 53,
  "id": 163694,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM2OTQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODo1NyswMDowMCJ9--875f8b2068a039ed3dff017d75ad56192eb7ca42f8f05efb4e77fd1735b6474f",
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
  "title": "FirstPersonProjectile.cpp",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#include &quot;FirstPersonProjectile.h&quot;\n#include &quot;GameFramework/ProjectileMovementComponent.h&quot;\n#include &quot;Components/SphereComponent.h&quot;\n\n// Sets default values\nAFirstPersonProjectile::AFirstPersonProjectile()\n{\n \t// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n",
  "lines_of_code": 86,
  "id": 163695,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM2OTUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODo1NyswMDowMCJ9--56ad3cdd3061b3c5e3ed0b20390d26167cfa70bfc0cc72a136e8a8409011049d",
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
  "lines_of_code": 118,
  "id": 163696,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM2OTYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODo1NyswMDowMCJ9--f3ebe4fce8dd771ca8dfce2e98c1d5df13088ada5bbd07925144e05b1bd26434",
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
  "lines_of_code": 260,
  "id": 163697,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM2OTcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODo1NyswMDowMCJ9--e8475a200876b6e701767746ae9e75f0a7a287b649be9099dee18bdb096789c6",
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
  "title": "DartLauncher.h",
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;EquippableToolBase.h&quot;\n#include &quot;DartLauncher.generated.h&quot;\n\nclass AFirstPersonProjectile;\n\n",
  "lines_of_code": 26,
  "id": 163698,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM2OTgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODo1NyswMDowMCJ9--4e28d865890ca29f53e658c30aef301c59e9c89df0e364017852ce1dbe923e71",
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
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n\n#include &quot;Tools/DartLauncher.h&quot;\n#include &quot;FirstPersonProjectile.h&quot;  \n#include &quot;Kismet/KismetMathLibrary.h&quot;\n#include &quot;EnhancedInputComponent.h&quot; \n#include &quot;AdventureCharacter.h&quot;\n\n\n",
  "lines_of_code": 51,
  "id": 163699,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM2OTksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODo1NyswMDowMCJ9--9d1534245716179840b1a00de0f03a243690816fca1e8ea11ed2517e3de312d8",
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
  "code_preview": "// Copyright Epic Games, Inc. All Rights Reserved.\n\n#pragma once\n\n#include &quot;CoreMinimal.h&quot;\n#include &quot;GameFramework/Actor.h&quot;\n#include &quot;EnhancedInputSubsystems.h&quot;    //\n#include &quot;Animation/AnimBlueprint.h&quot;\n#include &quot;Components/SkeletalMeshComponent.h&quot;\n#include &quot;EquippableToolBase.generated.h&quot;\n",
  "lines_of_code": 62,
  "id": 163700,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjM3MDAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzo1ODo1NyswMDowMCJ9--b440343666411db9ba4d024b57c221c57ae9b2f65633e864c57c5be93dbccb41",
  "settings": {
    "is_hidden": false
  }
}
```
