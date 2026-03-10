# Open Doors with Keys

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine

> Application Version: 5.7

Now that the player can pick up keys in the game, you’ll add the functionality to unlock and open doors when the player has picked up the required key. In this part of the tutorial, you will modify the `BP_DoorFrame` blueprint and explore **Functions** in Blueprints.

Unlockable doors provide a way to control the flow of the game and provide a sense of progression to the player. The project we are currently working on is divided into rooms. Therefore, picking up keys to unlock doors provides a logical progression path to the player.

[Video: V_SfBJaE](https://dev.epicgames.com/community/api/cms/videos/V_SfBJaE/embed.html)

## Before You Begin

Make sure you understand these topics covered in the previous sections of the [Design a Puzzle Adventure](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine) tutorial series:

- [Blueprint basics](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-blueprints), including [Blueprint Interfaces](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-interface-in-unreal-engine).
- Creating variants of an object using a Map variable.

You’ll need the following assets created in the previous tutorial, [Create a Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine):

- `BP_Key`
- `BPL_FPGame` Blueprint Function library
- `BPI_PlayerKeys` Blueprint Interface
- Three `BP_DoorFrame` instances placed in your level between rooms or hallways.

## Add Color Options to the Door

Since the first-person template already has a door blueprint, you can modify the existing blueprint to add the functionality of unlocking doors with a key.

Your door needs a few things to work with the key system you defined in the previous part of this tutorial. Just like the key, your door needs to know that the actor interacting with it implements the `BPI_PlayerKeys` interface.

The door should change its color to match the key that it accepts, meaning it needs to know what Key Type can unlock it. Last, it needs the same KeyMap variable with red, yellow, and blue color combinations.

### Create Variables for Interacting with the Player and Keys

To add new variables to the `BP_DoorFrame` blueprint, follow these steps

1. Go to the **Content Browser**, navigate to the **LevelPrototyping** > **Interactable** > **Door** folder, and open the `BP_DoorFrame` blueprint.
2. In the **My Blueprint** panel, in the **Variables** section, add a new variable named **UseKey**, with the type **Boolean**. This determines if the door needs a key to open it.
3. Create another variable named **RequiredKey** of the type **Enum Key Type**. This determines the key required to open the door. ![Add Variables](https://dev.epicgames.com/community/api/documentation/image/af3fe9dd-cf49-45b4-b7c9-6a65dcf62b33)
4. Click the **Eye** icon next to both variables so the eye is open, making them **editable**.
5. Select the **UseKey** variable. In the **Details** panel, enter `Setup`as its **Category**.
6. Select **RequiredKey** and change its **Category** to **Setup**.
7. Create a new variable named **Other Actor** of the type **Actor** > **Object Reference**. This stores the actor interacting with the door and you'll use it to check if the player has overlapped with the door volume. ![Image](https://dev.epicgames.com/community/api/documentation/image/c7b0d15b-b190-43f6-82c9-43515d0eb0ec)

### Build the Key Map Variable

Just like you did in `BP_Key`, you’ll add the map variable that maps key types to material colors. However, with the door, you don’t want the door meshes to change shape, so you won’t add new mesh shapes to the map.

To build the door’s KeyMap variable, follow these steps:

1. Create a variable named **KeyMap**, of the type **Enum Key Type**.
2. Click this variable, and in the **Details** panel, click the **Container** dropdown and select **Map**.
3. Change the map’s value type to **Struct Key Data**. ![Set Struct Key Data Type](https://dev.epicgames.com/community/api/documentation/image/f5dbf1cf-acdc-470c-b49a-8b34f8f6d497)
4. **Compile** the blueprint to add KeyMap values.
5. Under the map’s **Default Value** section, **Add** (**+**) 3 new elements to the **Key Map**. ![Add Key Map Entries](https://dev.epicgames.com/community/api/documentation/image/e7df8100-5737-485f-a9ec-79171f8a6f75)
6. For each map element, add the corresponding **Key Material**: `M_BasicColor_Yellow` `M_BasicColor_Red` `M_BasicColor_Blue` ![Add materials to corresponding Key Map Index](https://dev.epicgames.com/community/api/documentation/image/63660e73-14e0-4fcb-b374-15fd6ce1da04)
7. For each element, ensure the **Key Mesh** says **None**. To remove a mesh, click the dropdown and select **Clear** at the top of the list.
8. **Save** and **Compile** the door blueprint.

### Add Color-Changing Blueprint Logic

With your variables set up, you can add the color-changing functionality by modifying the blueprint graph.

First, you need to change the door to have red, blue, and yellow color options that are controlled by the new **RequiredKey** variable you added. The door should change its color as you set it up in the level, not when the gameplay starts. Therefore, you will use the **Construction Script** tab to create this functionality.

To add the door’s color options, follow these steps:

1. Navigate to the door’s **Construction Script** tab, where you can create functionality for when the door is created. In the graph, find the purple **Construction Script** node that starts off the logic in this function.
2. On the **Sequence** node that’s connected to the **Construction Script**, use **Add pin**(**+**) to create one more pin, named **Then 2**, which you can use to build upon the chain. ![Sequence Node Add Pin](https://dev.epicgames.com/community/api/documentation/image/744e84b2-c936-4b40-bd02-ec78cc0a397a)
3. Drag the **Then 2** pin to an empty part of the graph and create a **Branch** node.
4. Drag the **Condition** pin of the **Branch** node and create a **Get Use Key** node. Now, the Branch tests if the door should use keys or not. ![Branch Node Logic](https://dev.epicgames.com/community/api/documentation/image/e313562c-35a2-4382-a292-e4db858aa14e)
5. Drag the **True** pin of the **Branch** node and create a **Fn BPLSet** Key node. This is the library function that applies a new material color (and mesh, if provided) to an array of static meshes.
6. Drag the **Fn BPLSet Key** node’s **Static Mesh Array** pin and create a **Make Array** node.
7. Click the **Add pin (+)** button on the **Make Array** node.
8. From the **Make Array** node, drag the first pin, **[0]**, and create a **Get Door** node.
9. Drag the second pin, **[1]**, and create a **Get Door 2** node. This makes an array based on the two static mesh components, **Door** and **Door 2**.
10. From the **Fn BPLSet Key** node, drag the **Key Map** pin and create a **Get Key Map** node. This is a reference to the door’s **KeyMap** variable.
11. Then, drag the **Key** pin and create a **Get Required Key** node, which is a reference to the **RequiredKey** variable you added earlier.
12. **Compile** and **Save** the blueprint.

The door’s Construction Script should now have the following after the **Then 3** pin of the **Sequence** node:

![Final Door Blueprint Logic](https://dev.epicgames.com/community/api/documentation/image/9cfde287-a6b8-4f77-9e9e-b97b81ebaf97)

_Final Door Blueprint Logic_

Here's a copyable version of this logic:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "blueprint",
  "title": "Door Construction Script",
  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_IfThenElse Name=&quot;K2Node_IfThenElse_3&quot; ExportPath=&quot;/Script/BlueprintGraph.K2Node_IfThenElse&#39;/Game/LevelPrototyping/Interactable/Door/BP_DoorFrame.BP_DoorFrame:UserConstructionScript.K2Node_IfThenElse_3&#39;&quot;\n   NodePosX=736\n   NodePosY=896\n   NodeGuid=8BC6340843BC9EA444C6CBAA0C9620B9\n   CustomProperties Pin (PinId=6A8C24B540716DD50D3CE5A007B8032E,PinName=&quot;execute&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_ExecutionSequence_0 7D281C82433DA16FF2012FA4045C79FD,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n   CustomProperties Pin (PinId=FD72D7314D271B22C0A1ABB2140DDADA,PinName=&quot;Condition&quot;,PinType.PinCategory=&quot;bool&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue=&quot;true&quot;,AutogeneratedDefaultValue=&quot;true&quot;,LinkedTo=(K2Node_VariableGet_24 51C968E1470C3A2E625E099DD8BCAFC9,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n   CustomProperties Pin (PinId=01BE085446295FD6D9585FA992951BE9,PinName=&quot;then&quot;,PinFriendlyName=NSLOCTEXT(&quot;K2Node&quot;, &quot;true&quot;, &quot;true&quot;),Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_46 72FE519C4CD513F31B8203AD286B0262,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n   CustomProperties Pin (PinId=F1B08B5943B47918D9E5889193F900F0,PinName=&quot;else&quot;,PinFriendlyName=NSLOCTEXT(&quot;K2Node&quot;, &quot;false&quot;, &quot;false&quot;),Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\nEnd Object\nBegin Object Class=/Script/BlueprintGraph.K2Node_VariableGet Name=&quot;K2Node_VariableGet_24&quot; ExportPath=&quot;/Script/BlueprintGraph.K2Node_VariableGet&#39;/Game/LevelPrototyping/Interactable/Door/BP_DoorFrame.BP_DoorFrame:UserConstructionScript.K2Node_VariableGet_24&#39;&quot;\n",
  "lines_of_code": 83,
  "id": 153167,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTMxNjcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzozMiswMDowMCJ9--da144feab408749dbba83734b7e1b1d7296fa73390f0e9a4f97298b196d89766",
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
      "content": "If copying and pasting this snippet into <code class=\"inline-code\">BP_DoorFrame’s Construction Script</code>, you’ll need to add a third pin to the existing <b>Sequence </b>node and then connect that pin to the <b>Branch</b> node’s exec pin.",
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

### Test the Door Colors

After color-coding the door game object, you can set the doors to not open unless the player has the correct key.

In your level, select one of your `BP_DoorFrame` instances.

In the **Details** panel, enter Key in the search field at the top. This reveals two options: **Use Key** and **Required Key**. Change the **Required Key** to a different key type. The door’s color should change to match the key type.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you toggle<b> Use Key</b> to <b>false</b>, the door’s color won’t update, since you set that as a condition in the blueprint.",
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

[Video: V_NQZ53P](https://dev.epicgames.com/community/api/cms/videos/V_NQZ53P/embed.html)

As a reminder, this is the benefit of using the **Construction Script** graph tab in the Blueprint Editor. You can see changes happen in the level editor instead of having to wait to enter game mode.

## Build Key-Based Door Logic

Next, you can build the functionality to check what keys the player has. For this, you will define a custom function named **fnHasKey** in the `BP_DoorFrame` blueprint that checks if the player has the required key.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": " A function is a reusable set of blueprint nodes that performs a specific task.  ",
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

### Create a Function That Checks for Keys

This function will compare the door's required key with the player character's array of keys and return a true or false (boolean) value. You'll use a local variable for that boolean return value.

To create a function with a local variable, follow these steps:

1. In the `BP_DoorFrame`blueprint, in the **My Blueprint** panel, use **Add** (**+**) next to the **Functions** section. This is similar to adding a variable, but instead, you’re adding a function.
2. Name the new function **fnHasKey**. ![Name the Function FnHasKey](https://dev.epicgames.com/community/api/documentation/image/b78b8e46-8833-410e-bad9-7b8d630e15df)
3. Since a function can have its own set of nodes, it opens in its own **fnHasKey** tab with a separate node graph. If you close this tab and need to re-open it, double-click the function in the **Functions** list.
4. In the **My Blueprint** panel, you will see a new section at the bottom that’s called **Local Variables (FnHasKey)**. Create a new **Local Variable** using **Add** (**+**) next to that section.
5. Name the variable **HasRequiredKey** and set its type to **Boolean**. ![Has Required Key Variable](https://dev.epicgames.com/community/api/documentation/image/ba20411a-e8e6-41ca-96b9-63f22c5b6a33)

With the function set up, you can add logic that checks if the player has the right key.

To check if the actor in the door’s volume has the required key, follow these steps:

1. Drag the pin of the **fnHasKey** function entry node and create a **Sequence** node. This organizes the function’s logic into a sequence of actions that run in order.
2. Drag the Then 0 pin of the Sequence node and create an **Fn BPIGet Keys (Message)** node. This is the interface function that returns an array of keys the player has already found.
3. Drag the **Target** pin of the **Fn BPIGet Keys** node and create a **Get Other Actor** node. Once you set up the door’s event graph, this variable will store the actor overlapping the door’s volume. ![FnKeys Logic](https://dev.epicgames.com/community/api/documentation/image/a15e8c58-2859-4c99-9590-8f86b35f95d5)
4. Drag the **HasRequiredKey** local variable near the **Fn BPIGet Keys** node and select **Set**.
5. Drag the **Exec** pin of the **FN BPIGet Keys** node and connect it to the **Set** **HasRequiredKey** node.
6. From the Set **HasRequiredKey** node, drag the **HasRequiredKey** pin and create a **Contains Item** node, listed under the **Array** section of the search. This node checks if a specific item is in an array and returns true or false.
7. From the **Contains Item** node, drag the **Target Array** pin (the square pin) and connect it to the **Held Keys** pin of the **Fn BPIGet Keys** node.
8. Drag the **Item to Find** pin (that looks like a circle) of the **Contains Item** node, and create a **Get Required Key** node.

This is what your function’s graph should look like so far:

![FnHasKey Function Logic](https://dev.epicgames.com/community/api/documentation/image/dfc1bca9-e042-4e9e-8bfa-44f099316fc8)

_FnHasKey Function Logic_

This sequence of actions checks if the keys held by the **OtherActor** (variable) contain the **RequiredKey** (variable). If so, it will set **HasRequiredKey** to **true**.

Now, pass the **HasRequiredKey** result to the rest of the blueprint. To do this, use a **Return** node, which stops the execution of a function and returns a value to the blueprint that called the function.

To end the function with a **Return** node, follow these steps:

1. From the **Sequence** node, drag the **Then 1** pin, search for **Return** in the node actions list, and select **Add Return Node**.
2. To make the function return a value, it needs an output. Click the **Return Node** to highlight it.
3. In the **Details** panel, use **Add** (**+**) next to the **Outputs** section at the bottom. This adds a new output, which is the value it passes out of this function.
4. Name this output **KeyFound** and change its type to **Boolean**.
5. Back in the graph, drag the **Key Found** pin of the **Return** node, and create a **Get HasRequiredKey** node.

The complete FnHasKey function graph should now look like the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "blueprint",
  "title": "FnHasKey Function",
  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_FunctionEntry Name=&quot;K2Node_FunctionEntry_0&quot; ExportPath=&quot;/Script/BlueprintGraph.K2Node_FunctionEntry&#39;/Game/LevelPrototyping/Interactable/Door/BP_DoorFrame.BP_DoorFrame:FnHasKey.K2Node_FunctionEntry_0&#39;&quot;\n   LocalVariables(0)=(VarName=&quot;HasRequiredKey&quot;,VarGuid=BA52789E4082458C407C30ACB00E7DDA,VarType=(PinCategory=&quot;bool&quot;),FriendlyName=&quot;Has Required Key&quot;,Category=NSLOCTEXT(&quot;KismetSchema&quot;, &quot;Default&quot;, &quot;Default&quot;),PropertyFlags=5)\n   ExtraFlags=201457664\n   FunctionReference=(MemberName=&quot;FnHasKey&quot;)\n   bIsEditable=True\n   NodePosX=112\n   NodePosY=-80\n   NodeGuid=4FDCED0544DF70071CD1C8A8D384960C\n   CustomProperties Pin (PinId=88EB78FE4E03E70DC96ED9AEBB181C66,PinName=&quot;then&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_ExecutionSequence_0 AF2806494E835CAF86D028A700D36C0D,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\nEnd Object\n",
  "lines_of_code": 212,
  "id": 153168,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTMxNjgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzozMiswMDowMCJ9--a4163ab39bfd60e7e21f69c7e488e704c31b39974ace852b3ca7791053c637d3",
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
      "content": "If you copy this snippet into your project, you need to connect the <b>FnHasKey</b> function entry node to the <b>Sequence </b>node.",
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

### Lock and Unlock Doors With Keys

Now you can modify the door to open if all the necessary conditions are true.

Just like with the key, you’ll need to check if the character implements the `BPI_PlayerKeys` interface (the player’s “permission slip”) before they can try to open a door that uses keys.

So before it opens, the door must check for the following conditions:

- The door is set up to use keys (UseKey = True).
- The overlapping actor is the player (it implements BPI\_PlayerKeys).
- The player has the required key type.

To test if the actor interacting with the door is the player, follow these steps:

1. In `BP_DoorFrame`’s Event Graph, find the **Event ActorBeginOverlap** node. This collection of nodes controls what happens when a character steps into the door’s collision volume. You’ll add a blueprint interface and key requirement to this logic so the door won’t open unless the actor is the player and they have the right key.
2. Disconnect the **Event ActorBeginOverlap** node from the **Door Control** node by holding **Alt** and clicking the wire between the two nodes. Move the **Event** node back so you have space for more node actions before the **Door Control**. [Video: V_MYDxxk](https://dev.epicgames.com/community/api/cms/videos/V_MYDxxk/embed.html)
3. From the **Event ActorBeginOverlap** node, drag its pin and add a **Set Other Actor** node. Connect the **Other Actor** pin of the **Event** node to the **Other Actor** pin of the **Set** node. ![Event Actor Begin Overlap Set Other Actor Variable](https://dev.epicgames.com/community/api/documentation/image/0a2dde42-2081-4465-a859-0619fc4d3720) This stores the actor that overlapped with the door area.
4. From the **Set Other Actor** node, drag the blue **Value** pin and create a **Does Object Implement Interface** node. Set the **Interface** value to `BPI_PlayerKeys`. ![Does Object Implement Interface Node](https://dev.epicgames.com/community/api/documentation/image/406e3068-e75d-46ef-aa56-97bbc59b3c9a)
5. From the **Set Other Actor** node, drag the **Exec** pin and create a new **Branch** node.

To check that the door uses keys, follow these steps:

1. Drag the **True** pin of the **Branch** node and create an **Fn Has Key** node, which is the function that you created earlier in this tutorial. It takes the key type required to open the door and checks the player’s **Held Keys** array for that key type. Calling this function here will execute the nodes in it.
2. From the **Fn Has Key** node, drag the **Exec** pin and create a new **Branch** node.
3. Connect the **Key Found** pin of the **Fn Has Key** node to the **Condition** pin of the **Branch** node.
4. Connect the new **Branch** node’s **True** pin to the **Door Control** node’s **Play** pin. ![Door Control Node](https://dev.epicgames.com/community/api/documentation/image/d51c5428-94ec-4723-a357-251eeb40e35f)

So far, this logic only allows the door to open when the player has the right key. The door should also open when:

- The door doesn’t require keys, or
- A non-player character tries to get through the door.

The first **Branch** node and **And** node tests for both of these conditions. If either is **false**, the **Branch** is also **false**.

To ensure the door opens for NPCs and when keys aren’t required, follow these steps:

1. Connect the **False** pin of the first **Branch** node directly to the **Door Control** node’s **Play** pin. You can use connectors by double-clicking on a wire between two nodes to organize your blueprint. ![Blueprint Connections Logic](https://dev.epicgames.com/community/api/documentation/image/9f921fc3-8ce3-48e8-aab9-5031a0dbe2c5)
2. **Compile** and **Save** the blueprint.

Now, when the actor does not implement the key interface, or the door does not require keys (**UseKeys** = False), the door still opens.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "In this tutorial, we designed the doors to allow NPCs to pass through them. If you’d like your game to work differently, go ahead and try to change the graph yourself.",
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

The new `BP_DoorFrame`  Event Graph logic should look like the following:

![BP_DoorFrame Event Graph Logic](https://dev.epicgames.com/community/api/documentation/image/cd144c2d-621f-48e8-87c4-0fe02d8bb0bf)

_BP_DoorFrame Event Graph Logic_

## Add Comments to a Blueprint

You can add comment blocks in your blueprints to create visual-only notes that group nodes together and explain what each part of the blueprint does. Comments help you and your team members know at a glance what functionality your nodes are performing and keep your blueprints organized.

When building blueprint logic, first focus on creating the functionality, and then highlight the nodes you have added and add a comment to contain and describe them.

To add a comment in a blueprint, follow these steps:

1. Click the graph to ensure it's the active panel.
2. Press **C** on your keyboard. This adds a comment box.
3. Double-click the text field at the top of the box to enter a comment.
4. To resize the comment, ensure the comment is selected (highlighted with a yellow outline), and drag an edge or corner.
5. To group notes within a comment, drag those nodes inside the bounds of the comment.

You can also select one or multiple nodes and press **C** to add a comment that contains the selected nodes.

[Video: V_4PLlSQ](https://dev.epicgames.com/community/api/cms/videos/V_4PLlSQ/embed.html)

## Test Your Doors

Go back to your level in the **Level Editor**. Use your doors’ Required Key property to set them up with different colors and add a **BP\_Key** for each color.

Now, play the game. If you walk up to the door without picking up a key, the door will not open.

But if you pick up the key, the door opens when you approach it. When you move far enough away, it’ll close automatically.

After picking up one key color, try to open a door that’s a different color. The door should stay closed.

[Video: V_Xmwqu9](https://dev.epicgames.com/community/api/cms/videos/V_Xmwqu9/embed.html)

If you're working with this tutorial's sample level, select the door that leads to **Hallway 2** and change its required key to the blue key. Next, select the door that leads to **Hallway 3** and change its required key to the red key. Make the door to **Hallway 1** yellow.

![Color Coded Doors and Keys](https://dev.epicgames.com/community/api/documentation/image/077f807d-a855-4788-b653-9ec08eab5506)

_Color Coded Doors and Keys_

### Add Feedback with Debug Messages

If you want to check what’s happening in a blueprint during gameplay, you can use **Print String** nodes to display messages on screen. Unreal Engine doesn’t display these messages in a final game.

Try adding a **Print String** node to confirm the type of key the player has picked up.

To display a debug message with Print String nodes, follow these steps:

1. In the `BP_AdventureCharacter` Event Graph, go to the set of nodes that starts with **Event fnBPIAddKey** and adds keys to the **HeldKeys** array.
2. Drag from the **Add** node’s **Exec** pin and add a **Print String** node.
3. The **In String** is the text that appears on-screen. Enter custom text, or connect the **Event** node’s **Key Type** pin to **In String**. This displays the key the player is picking up. ![Debug Logic](https://dev.epicgames.com/community/api/documentation/image/431a6198-18c0-47ee-bc29-63fc9bd33acf)
4. **Compile** the blueprint.
5. Play your game again and pick up the keys. You’ll see debug text confirming each key color as you pick them up.
6. When you’re done, go back to the node graph and delete the **Print String** and **Enum to String** nodes. **Compile** and **Save** the blueprint.

If something isn’t working as expected in a blueprint, you can add Print String nodes after calculations, event calls, or function calls to help track what’s happening with values and flow.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can also open a blueprint while the game is playing, its wires light up to show the logic running in real time. This <b>Execution Tracing</b> is a quick way to spot what’s happening alongside your Print String messages.",
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

## Place Pickup Items

So far, you’ve been placing keys on the floor. To make this more interesting and engaging for the player, try introducing a platforming element.

In this tutorial’s sample level, we added some verticality by placing the key in a high place so the player has to jump to the key. Here, there’s a minor risk of falling and having to start over.

![Level Layout with Functional Keys](https://dev.epicgames.com/community/api/documentation/image/3d00a4d8-f733-40ca-af13-34f558d89984)

_Level Layout with Functional Keys_

The player practices jumping on the first and second platforms before they are put to the test with the more difficult final jump to the pillar.

## Try the Sample Level

If you’d like to add the new pieces of the room designed in this part of the tutorial series instead of creating your own, copy the snippets below.

### Start Room’s Blockout

This text snippet contains the ramp, recessed floor, column, and two platform meshes added to create the path to the yellow key.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "Starting Room Layout",
  "code_preview": "Begin Map\n   Begin Level\n      Begin Actor Class=/Script/Engine.StaticMeshActor Name=Floor_168 Archetype=&quot;/Script/Engine.StaticMeshActor&#39;/Script/Engine.Default__StaticMeshActor&#39;&quot; ExportPath=&quot;/Script/Engine.StaticMeshActor&#39;/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.Floor_168&#39;&quot;\n         Begin Object Class=/Script/Engine.StaticMeshComponent Name=&quot;StaticMeshComponent0&quot; Archetype=&quot;/Script/Engine.StaticMeshComponent&#39;/Script/Engine.Default__StaticMeshActor:StaticMeshComponent0&#39;&quot; ExportPath=&quot;/Script/Engine.StaticMeshComponent&#39;/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.Floor_168.StaticMeshComponent0&#39;&quot;\n         End Object\n         Begin Object Name=&quot;StaticMeshComponent0&quot; ExportPath=&quot;/Script/Engine.StaticMeshComponent&#39;/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.Floor_168.StaticMeshComponent0&#39;&quot;\n            StaticMesh=&quot;/Script/Engine.StaticMesh&#39;/Engine/MapTemplates/SM_Template_Map_Floor.SM_Template_Map_Floor&#39;&quot;\n            bUseDefaultCollision=False\n            StaticMeshDerivedDataKey=&quot;STATICMESH_34081786561B425A9523C94540EA599D_359a029847e84730ba516769d0f19427Simplygon_5_5_2156_18f808c3cf724e5a994f57de5c83cc4b_680318F3495BDBDEBE4C11B39CD497CE000000000100000001000000000000000000803F0000803F00000000000000000000344203030300000000&quot;\n            MaterialStreamingRelativeBoxes(0)=4294901760\n",
  "lines_of_code": 132,
  "id": 153169,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTMxNjksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzozMiswMDowMCJ9--c7d2dfcb86196e340f779ceccad440a4e27f3d3ac4a90c31d47f2f56c8a9990c",
  "settings": {
    "is_hidden": false
  }
}
```

To Start Room’s new blockout shapes, follow these steps:

- In Unreal Editor, remove all keys from **Start Room** so they don’t get lost in the new geometry.
- Click **Copy Full Snippet**.
- In Unreal Editor, ensure the viewport is the active panel (click anywhere in the viewport or **Outliner** and press **Esc**), and then press **Ctrl** + **V.**
- Three floor pieces are covering the new recessed floor. In the viewport, click each and press **Delete**. ![Sample Copy Paste Demo](https://dev.epicgames.com/community/api/documentation/image/753d0a8f-d593-4971-82c4-c913743a802b)

## Next Up

Your player character can pick up keys, but there’s no feedback to tell them what they have picked up so far. In the next section, you’ll create a heads-up display (HUD) for the player that shows them the keys in their inventory.

- [Related Document](en-us/unreal-engine/designer-04-player-hud-in-unreal-engine.md)
