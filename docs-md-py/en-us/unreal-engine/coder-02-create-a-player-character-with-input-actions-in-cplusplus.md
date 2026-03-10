# Create a Player Character With Input Actions

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-02-create-a-player-character-with-input-actions-in-cplusplus

> Application Version: 5.7

## Before You Begin

Ensure you've completed these objectives from the previous section,  [Set Up and Compile Your Project](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine):

- Created a project based on the First Person template with a custom Game Mode C++ class.
- Verified your project is using the Enhanced Input system.

## Set Up a New Character

You’ve set up a new C++ project with a custom Game Mode. Now, you’ll add a new Character class, extend it to Blueprints, and set it as the default player pawn in your Game Mode.

### Create a C++ Character Class

Actor assets are any object that can be placed in a level. Pawns are Actors that can be controlled by players or AI, and Characters are a special type of Pawn that are used as player characters. To learn more about these Actor classes, see the [Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/actors-in-unreal-engine), [Pawns](https://dev.epicgames.com/documentation/en-us/unreal-engine/pawn-in-unreal-engine), and Characters class information in UE’s Gameplay Framework documentation.

To create a new Character class and add C++ to your project, follow these steps:

1. In the editor’s main menu, go to **Tools** > **New C++ Class**.
2. In the **Choose Parent Class** window, select **Character**, and click **Next**. ![Image](https://dev.epicgames.com/community/api/documentation/image/8f7cef69-6c4c-468f-a581-d8cecc1f2ffa)
3. Enter a name for the new class (this tutorial uses `AdventureCharacter`), select **Public**, then click **Create Class**. ![Image](https://dev.epicgames.com/community/api/documentation/image/e8da9a77-8c21-4edd-a937-0709b967a18f)
4. Unreal Engine automatically opens the new class files in Visual Studio (VS). Return to VS to find your new files.

### Extend Your C++ Character to Blueprints

Just like you did with your Game Mode, derive a blueprint from the AdventureCharacter C++ class:  to create a Blueprint for that character in the `Blueprints` folder.

1. In the **Content Browser**, in the **C++ Classes** folder, right-click your Character class and select **Create Blueprint class based on*****<CharacterName>**.* ![Image](https://dev.epicgames.com/community/api/documentation/image/985e032a-c433-4f54-bc4c-fafec0534123)
2. Name the Blueprint. This tutorial uses `BP_AdventureCharacter`.
3. For the **Path**, select **Content > FirstPerson > Blueprints**, and click **Create Adventure Character**.
4. In the Blueprint's tab, click **Save**.

### Change the Default Player Character

To use your new character in-game, set it as the Default Pawn Class used in your project's Game Mode.

To set your Character as the default player character, follow these steps:

1. If your Game Mode Blueprint isn’t already open, in the **Content Browser**, double-click your GameMode Blueprint to open it in the Blueprint Editor.
2. In the Blueprint’s **Details** panel, expand **Classes**. This is where you can set different default classes for this Game Mode to use.
3. Change **Default Pawn Class** to your Character Blueprint (`BP_AdventureCharacter`). ![Image](https://dev.epicgames.com/community/api/documentation/image/06dcf980-32f7-4aa5-a9d6-b27d5514e5b0)
4. In the top-left corner of the window, click **Compile**, and click **Save**. ![Image](https://dev.epicgames.com/community/api/documentation/image/70686208-8db4-4b90-91ce-09bf2f01ea2a)

If you return to the level editor and play the game, you won't be able to move or look around. This is because your new character doesn't have a body, camera, or actions yet. You'll use C++ to add these features in the following sections of this tutorial series.

## Exploring Input Actions

The default character in the First Person template uses a set of preexisting Input Actions that combine with Blueprints to make the character move, jump, and look around.

![Image](https://dev.epicgames.com/community/api/documentation/image/0808ad8a-7396-4acb-9581-7eb743bf7e74)

_Showing the moveset of the default first-person character._

Open up and explore these Input Actions to learn how they power this character’s movements.

In the **Content Browser** asset tree, go to the **Content** > **Input** > **Actions** folder. You’ll see three Input Actions named `IA_Jump`, `IA_Look`, and `IA_Move` that correspond to jumping, looking, and moving around, respectively.

![Image](https://dev.epicgames.com/community/api/documentation/image/b19f91c8-007d-4442-98d3-4e1f5897a628)

Double-click `IA_Jump` to open it and see its **Details** panel.

![Image](https://dev.epicgames.com/community/api/documentation/image/be10baf5-aa75-4574-8a06-f2761333c75a)

The character’s Input Actions use the following properties to define what type of action it is and what it does:

| **Property** | **Description** |
| --- | --- |
| **Value Type** | Determines what type of value this input action contains. Choose a Value Type depending on the type of movement you want to capture with this Input Action. For example, `IA_Jump` is a **Digital (bool)** type, meaning it has an on and off state (jumping or not jumping) corresponding to a bool value. **Axis1D** is a float value to capture one-dimensional movement (scrolling in and out) or a scalar adjustment (changing movement speed). **Axis2D** is a vector of two floats that captures two-dimensional movement, such as WSAD controls. **Axis3D** is a vector of three floats that captures three-dimensional movement, such as flying or swimming controls. |
| **Triggers** | Create triggers to represent the action’s possible states so you can build logic with these triggers in Blueprints or code. When the button mapped to `IA_Jump` is **Pressed** or **Released**, the corresponding trigger fires an event. |
| **Modifiers** | Modifies the raw input value that UE receives before it sends them to any input triggers. |

## Exploring Input Mapping Contexts

Input actions don’t work alone; they need an Input Mapping Context to know what button should trigger them and in what context. This is a collection of mappings that describe the rules for triggering an Input Action. You can create and customize multiple Input Mapping Contexts and turn them on and off dynamically to suit the needs of your game.

The default character already has an Input Mapping Context that you can find in the Content Browser in **Content** > **Input**. Double-click `IMC_Default` to open it and view its **Details** panel.

![Image](https://dev.epicgames.com/community/api/documentation/image/7af5ecaa-5f0d-4318-8b6b-0e19b1494a21)

`IMC_Default` contains three **Mappings** that map each of the three Input Actions to user inputs. Each mapping pulls in the Input Action’s triggers and modifiers.

### Mapping a Jump Action

Expand the **IA\_Jump** mapping. You’ll see it has two control bindings: **Space Bar** and **Gamepad Face Button Bottom**. If you press either of these buttons in-game, **IA\_Jump** is triggered.

![Image](https://dev.epicgames.com/community/api/documentation/image/83cccc9a-c3bb-407d-8f5e-1993d53ea48f)

### Mapping 2D Movement with Keyboard Keys

Next, expand **IA\_Move** to view its nine bindings corresponding to the WASD keys, arrow keys, and gamepad left thumbstick.

![Image](https://dev.epicgames.com/community/api/documentation/image/d78470f1-45e1-43bd-8b0f-c5dd15bfa9a2)

Creating two-dimensional movement from several individual keys requires a bit more setup than the simple boolean jump.

A key press is one-dimensional, returning a value of 0 when not pressed or 1 when pressed. This works perfectly for the D or Right arrow keys because they should move our character in a positive direction along the X axis (in other words, to the right). However, we need our character to move forward, left, and backwards as well. In other words, we want values 0 to 1 and 0 to -1 on both the X axis and Y axis.

So, to get values that create movement in all directions, the Input Actions use **Modifiers** to transform the input value to a different axis or to a negative value.

For example, expand the **A** control binding and its **Modifiers** to see how it’s configured. You’ll see it has the **Negate** modifier. This means that when the key is pressed, the value of 1.0 gets negated to -1.0, which moves your character down the X axis, or to the left.

![Image](https://dev.epicgames.com/community/api/documentation/image/5e664f7d-eb73-408c-8074-bdb73f262861)

Expanding the **Negate** modifier lets you specify whether you want to negate X, Y, or Z axis values. These are all enabled by default, but you can restrict negation to specific axes depending on your needs.

![Image](https://dev.epicgames.com/community/api/documentation/image/e19bdedb-3873-4f96-9d37-9679112b4d51)

Now, expand the **S** control binding. To create backwards movement on the Y axis, this binding has two modifiers: a **Swizzle Input Axis Values** that changes the input from X to Y axis, and a **Negate**.

![Image](https://dev.epicgames.com/community/api/documentation/image/b557c16c-596d-4be3-8ece-993bb6775f93)

Expand the **Swizzle Input Axis Values** modifier. The **Order** option specifies how axis values should be reordered. In this case, the Input Action is using **YXZ**, so the X and Y axis are swapped from the default XYZ ordering.

### Mapping 2D Movement on a Gamepad

The gamepad thumbstick uses a 2D-axis for input rather than a 1D button press, so this mapping only needs one control binding to handle thumbstick movement.

If you expand the **Modifiers** for **Gamepad Left Thumbstick 2D-Axis**, you’ll see the **Dead Zone** and **Scalar** modifiers.

![Image](https://dev.epicgames.com/community/api/documentation/image/76187436-eb9f-458c-ad88-ea5206e4c9ca)

**Dead Zone** specifies the thresholds above and below which input is ignored. Use it to filter out small input values near the center of the thumbstick that are often unintentional due to the stick not centering perfectly or slight finger pressure.

**Scalar** specifies how much to multiply each of the X, Y, and Z axis values by so you can control how fast your character moves in each direction.

### Mapping Look Controls on Gamepad and Mouse

Expand the `IA_Look` action mapping. This Input Action is bound to the **Gamepad Right Thumbstick 2D-Axis** control.

![Image](https://dev.epicgames.com/community/api/documentation/image/70e38ae8-5d85-4ad5-8fa4-770b128030e9)

It only needs a **Dead Zone** modifier to filter out errors.

The default character has a separate mapping context for mouse-based camera controls. Go back to the **Content Browser** and open `IMC_MouseLook`. This IMC creates bindings for the `IA_MouseLook` Input Action which is identical to `IA_Look`.

By using separate thumbstick and mouse Input Actions, you can have different modifiers for each input and treat them as separate input paths. However, in this tutorial, you’ll combine everything into one Input Mapping Context.

Expand the **IA\_MouseLook** action mapping. This Input Action is bound to the **Mouse XY 2D-Axis** control.

![Image](https://dev.epicgames.com/community/api/documentation/image/e5904bbc-8e1d-4273-84ec-ce17404a64d5)

The mouse control binding already uses a 2D axis, so the only modifier it needs is a Y-axis **Negate** to make the character look down when you move the mouse up. This is traditional for first-person games, but you can delete this modifier to invert your look controls.

## Modify an Input Mapping Context

Since you’re just starting out in a new project, combine all input mappings into one Input Mapping Context.

To create your own IMC based on the default player’s mapping contexts, follow these steps:

1. In the **Content Browser**, in the **Content** > **Input** folder, right-click `IMC_Default` and select **Duplicate**.
2. Name the mapping context `IMC_Adventure`, then double-click it to open it.
3. Under **Mappings**, expand the **IA\_Look** mapping.
4. Click the **plus (+)**button next to **IA\_Look** to add a new control binding. ![Image](https://dev.epicgames.com/community/api/documentation/image/4988d5ff-1530-4754-9c2e-b6eec825fc01)
5. Click **None** to open the key value dropdown list, expand **Mouse**, and select **Mouse XY 2D-Axis**. ![Image](https://dev.epicgames.com/community/api/documentation/image/0ce02f8b-b2d8-46b6-93d9-422926508bc0)
6. In the mouse control binding, click the **+** button next to **Modifiers**, and change **None** to **Negate**.
7. Expand the **Index [0]** modifier and deselect **X** and **Z**. This modifier should only negate the Y axis.
8. Click **Save** and close the mapping context.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "To invert your camera controls, you can add or remove Negate modifiers from your thumbstick or mouse control bindings.",
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

## Next Up

In the next section, you’ll learn how the default character's Blueprint connects player input to character movement and start to recreate this in code.

- [Related Document](en-us/unreal-engine/coder-03-configure-character-movement-with-cplusplus-in-unreal-engine.md)
