# Bonus: Spawn New Cubes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-11-spawn-new-cubes-mechanic-in-unreal-engine

> Application Version: 5.7

In this tutorial, you’ll learn to create a blueprint that spawns new cubes in the level when the player stands on top of a switch. Use this gameplay object to allow players to get new cubes in any puzzle room where cubes can be lost or destroyed.

![Image](https://dev.epicgames.com/community/api/documentation/image/acb5e69c-81b2-421a-b1d6-4330b58198e2)

For the cube spawner, you’ll create a blueprint that only contains the spawning functionality, so you have the flexibility to use any piece of geometry or art asset to create the effect of cubes falling out of that geometry.

Creating this blueprint isn’t mandatory if you’ve followed along with the sample level, but you may want to include this cube-regeneration mechanic in your project if you continue expanding the puzzle adventure game.

## Before You Begin

Make sure you understand these topics covered in the previous sections of the [Design a Puzzle Adventure](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine) tutorial series:

- Blueprint basics, including Blueprint Interfaces, custom events, and variables.

You’ll need the following assets created in [Puzzles: Switches and Cubes](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine):

- `BP_Cube` Blueprint
- `BP_Switch` Blueprint
- `BPI_Interaction` Blueprint Interface

## Create a New Blueprint

First, create a new blueprint asset for the cube spawner. This blueprint will implement the `BPI_Interaction` Blueprint Interface so it can respond to `BP_Switch`, which uses the events in that interface.

To set up a new blueprint, follow these steps:

1. In the **Content Browser**, go to the **Content > Adventure Game > Designer > Blueprints > Activation** folder.
2. Right-click and select **Blueprint Class**. In the class-selection window, select the **Actor** class.
3. Name this blueprint `BP_CubeSpawn` and open the blueprint. ![Image](https://dev.epicgames.com/community/api/documentation/image/20d358c1-2e92-4e17-be3e-f57b3755a03d)
4. In the Blueprint Editor, go to the **EventGraph** tab.
5. At the top portion of the blueprint editor, click the **Class Settings** button.
6. In the **Details** panel, under the **Interfaces** section, click the **Add** dropdown next to **Implemented Interfaces** and select **BPI Interaction**. ![Image](https://dev.epicgames.com/community/api/documentation/image/86044b86-ec29-4912-a3d2-46539dceb790)
7. Click **Compile** and **Save**.

After adding the `BPI_Interaction` interface, under the **My Blueprint** panel, you’ll see a new section named Interfaces. This section contains the **fnBPISwitchOff** and **fnBPISwitchOn** events that are part of the BPI Interaction interface.

![Image](https://dev.epicgames.com/community/api/documentation/image/515de780-c79f-4e95-8ae5-677d5c9c1db0)

In `BP_CubeSpawn`, you’ll use the **fnBPISwitchOn** event to define what happens when the player steps on a switch and triggers this event.

## Build the Cube-Spawning Logic

Before implementing the logic to spawn the cubes, consider how the cube spawning system should work:

- To spawn a cube, the player must activate the switch, which uses the interface you added in the previous section.
- There should be a maximum number of cubes the player can spawn so they don’t overfill the area with cubes.
- If the player tries to spawn more cubes than the maximum amount, destroy the first spawned cube. You’ll keep track of the spawned cubes with an array variable.
- The cube spawner should use a short cooldown timer so the player can not spawn new cubes too quickly.

### Check Cube-Spawning Conditions

To start the cube spawner’s event graph, first check if a new cube can spawn and if the player has created the maximum number of cubes.

To check if a new cube can spawn, follow these steps:

1. In the **My Blueprint** panel, under the **Interfaces** category, double-click the **fnBPISwitchOn** interface to add it to the graph.
2. From the **fnBPISwitchOn** node, drag the **exec** pin and add a **Branch** node.
3. On the **Branch** node, drag the **Condition** pin, select **Promote to variable**, and name this variable `CanSpawn`. You’ll use this variable to check if the cooldown has passed or not. ![Image](https://dev.epicgames.com/community/api/documentation/image/5ccb4c7e-233a-48a4-8bc1-57616081c5d8)
4. In the **My Blueprint** panel, create a new variable named `CubesSpawned` of type **Integer**. This keeps track of the spawned cubes in the level.
5. Create another variable named `MaxNumCubes`. This variable sets the maximum number of cubes that the player can spawn.
6. Set up **MaxNumCubes**: Set its type to **Integer**. Click its **eye** icon to make it public and editable. In the **Details** panel, click the **Category field and enter** `Setup`. Click **Compile** and set the variable’s **Default Value** to `3`. So far, your variables list should look like this: ![Image](https://dev.epicgames.com/community/api/documentation/image/cb6efabb-7820-4179-8b44-d47b592609d9)
7. From the **Branch** node, drag off the **True** pin and add a second **Branch** node.
8. From the second **Branch** node, drag the **Condition** pin and add a **Less Than (<)** node.
9. Set up the **Less Than**node to check if the number of cubes spawned is less than the max number of cubes allowed: From the **Variables** list, drag **CubesSpawned** onto the **Less Than**node’s top input pin. Drag the **MaxNumCubes** variable onto the bottom input pin. ![Image](https://dev.epicgames.com/community/api/documentation/image/28ceb8a0-4ccf-4d26-9f44-0f78bd9f25e2)

### Count Spawned Cubes and Destroy Extra Cubes

If the current number of cubes the player has spawned is less than the maximum, execution passes through the second Branch node's True pin. In this case, you can skip directly to the logic that adds 1 to the cube count before spawning a cube.

To increment the number of spawned cubes, follow these steps:

1. From the second **Branch** node, drag the **True** pin and add an **Increment Int** node. Move the new node to add extra space between it and the **Branch** node.
2. From the **Variables** list, drag **CubesSpawned** onto the **Increment Int** node’s input pin. ![Image](https://dev.epicgames.com/community/api/documentation/image/06e57175-c122-4d2b-b2e1-a0f7d71293a8)

Next, add the logic for the opposite scenario — where the **Cubes Spawned** value is greater than the **Max Num Cubes** value, or when execution passes through the Branch's False pin. If the player has reached the maximum number of cubes, destroy the oldest cube before spawning a new one.

To destroy a cube to make room for a new cube, follow these steps:

1. From the second **Branch** node, drag the **False** pin and add a **Destroy Actor** node.
2. From the **Destroy Actor** node, drag the **Target** pin and add a **Get (a copy)** node.
3. Keep the **Get** node’s second input pin set to **0**, since an array’s list begins at 0 and you want to retrieve the first element.
4. From the **Get** node, drag off the **Array** input node and select **Promote to variable**.
5. Name the new variable `SpawnedCubes`. You’ll use this array to store every cube the player spawns into the level. ![Image](https://dev.epicgames.com/community/api/documentation/image/385bce81-9bea-4dc6-ad04-a41185ef8ee9)
6. From the **Destroy Actor** node, drag the **exec** pin and add a **Remove Index** node.
7. Drag its **Array** input and add a **Get Spawned Cubes** reference node. ![Image](https://dev.epicgames.com/community/api/documentation/image/ce766216-34d3-4cd4-a333-4618167d840e)
8. Double-click the wire between the second **Branch** node and the **Increment Int** node to create a movable **reroute** node. Drag the **reroute** node closer to the **Increment Int** node.
9. Connect the **Remove Index** node’s output **exec** pin to the **reroute** node. ![Image](https://dev.epicgames.com/community/api/documentation/image/2bd3911f-bdf6-4829-8206-c852c3aac2d1) (You can also connect the **Remove Index** node directly to the **Increment Int** node.)

Now, before a cube spawns, the blueprint either increments the **CubesSpawned** counter or deletes a cube and then increments the **CubesSpawned** counter. Next, you’ll add the logic that spawns a new cube.

### Spawn a Cube

Now that you’ve checked if the player can create a cube and ensured there aren’t too many cubes in the level, you can spawn a new `BP_Cube` actor.

To spawn a new cube, follow these steps:

1. From the **Add** node, drag the **exec** pin and add a **Spawn Actor from Class** node.
2. Set up the **SpawnActor** node: Click the dropdown menu next to the **Class** pin, search for, and then select `BP_Cube`. The node’s name changes from **SpawnActor NONE** to **SpawnActor BP Cube**. Right-click on the orange **Spawn Transform** pin and select **Split Struct Pin**. Three new pins replace the Spawn Transform pin: **Spawn Transform Location**, **Spawn Transform Rotation**, and **Spawn Transform Scale**. ![Image](https://dev.epicgames.com/community/api/documentation/image/c260d9ae-3c9c-4b08-8449-f83fb241b02b) Right click in the Event Graph and search for then select a **Get Actor Transform** node. Right click on the **Return Value** pin and select **Split Struct**. Connect the **Location** and **Rotation pins** to the corresponding pins in the **Spawn Actor** node. ![Image](https://dev.epicgames.com/community/api/documentation/image/09df0e19-b340-405f-81ee-40701fbaf007)
3. From the **SpawnActor** node, drag the **exec** pin and add an **Add** node under the **Array** category (you can also search for `Add Array` and select the **Add** node).
4. On the **Add Array**node, do the following: Drag the **Array** input pin and add a **Get Spawned Cubes** node. Connect the node's bottom input pin to the **SpawnActor** node’s **Return Value** pin. ![Image](https://dev.epicgames.com/community/api/documentation/image/b77a32bb-3cf9-4b68-a95b-78cd299af9da)
5. When the player spawns a cube, they shouldn’t be able to spawn one again until a cooldown timer expires. Drag the **Add Array** node’s exec pin and add a **Set Can Spawn** node. Keep **Can Spawn** set to false (does not have a checkmark). ![Image](https://dev.epicgames.com/community/api/documentation/image/f1d30a73-7db0-4e04-960f-f33febb9e5a5)

### Implement a Cooldown Timer

Use the **CanSpawn** variable and a **Delay** node to prevent the player from spawning another cube until a set amount of time has passed.

To create and trigger an event that resets the cube-spawn cooldown timer, follow these steps:

1. Right-click somewhere empty in the EventGraph, and search for and select **Add Custom Event**.
2. Name the new event `EvResetSpawn` and move it under the **Event fnBPISwirchOn** node.
3. Drag the **EvResetSpawn** event node’s **exec** pin and add a **Delay** node. ![Image](https://dev.epicgames.com/community/api/documentation/image/8c00c890-7104-4a1c-aa29-76a3fb16fbcc)
4. On the **Delay** node, drag the **Duration** pin and select **Promote to variable**. Name the variable `SpawnCooldown`.
5. Set up the new **SpawnCooldown** variable: Ensure its type is **Float**. Click its eye icon to make it public and editable. Change its **Category** to **Setup**. Click **Compile** and then set its default value to `1`. Your complete list of variables should look like this: ![Image](https://dev.epicgames.com/community/api/documentation/image/5385566e-304f-42a3-bdf9-989a9ad427ad)
6. From the **Delay** node, drag the **Completed** pin and add a **Set Can Spawn** node. Make sure to toggle this node’s **Can Spawn** value to true. ![Image](https://dev.epicgames.com/community/api/documentation/image/c8ca4825-645b-480f-8dd5-434ea2cafbad)
7. Return to the **Set Can Spawn** node at the end of your cube-spawning logic. Drag the **Set Can Spawn** node’s exec pin and add an **EvResetSpawn** node to trigger the event and spawn cooldown delay. ![Image](https://dev.epicgames.com/community/api/documentation/image/78aa8ea1-2df2-4700-a3c9-fd2ff2f13491)
8. Click **Save** and **Compile**.

Now, your EventGraph should look like this:

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you use the snippet below, ensure your blueprint has the custom variables, event, and BP interface mentioned in the instructions above.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "To copy these nodes into your blueprint, click <b>Copy Snippet</b>, go to your event graph, and press <b>Ctrl+V</b>. After copying the logic into your blueprint editor, you may need to delete the blue<b> Ev Reset Spawn</b> node and re-add it manually after the <b>Set Can Spawn</b> node.",
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

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "blueprint",
  "title": "",
  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_CustomEvent Name=&quot;K2Node_CustomEvent_1&quot; ExportPath=&quot;/Script/BlueprintGraph.K2Node_CustomEvent&#39;/Game/AdventureGame/Designer/Blueprints/Activation/BP_CubeSpawn.BP_CubeSpawn:EventGraph.K2Node_CustomEvent_1&#39;&quot;\n   CustomFunctionName=&quot;EvResetSpawn&quot;\n   NodePosX=-1728\n   NodePosY=400\n   NodeGuid=BC7DF61D40D79CBF550AECA80ABACC95\n   CustomProperties Pin (PinId=A2AF852D4ABF45DBF9EA8798A5A568C8,PinName=&quot;OutputDelegate&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;delegate&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(MemberParent=&quot;/Script/Engine.BlueprintGeneratedClass&#39;/Game/AdventureGame/Designer/Blueprints/Activation/BP_CubeSpawn.BP_CubeSpawn_C&#39;&quot;,MemberName=&quot;EvResetSpawn&quot;,MemberGuid=BC7DF61D40D79CBF550AECA80ABACC95),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n   CustomProperties Pin (PinId=F679A3914AACC1A5A1E642BBEA784923,PinName=&quot;then&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_CallFunction_6 DAC6A0244B615147C7F644B00349C3D7,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\nEnd Object\nBegin Object Class=/Script/BlueprintGraph.K2Node_SpawnActorFromClass Name=&quot;K2Node_SpawnActorFromClass_0&quot; ExportPath=&quot;/Script/BlueprintGraph.K2Node_SpawnActorFromClass&#39;/Game/AdventureGame/Designer/Blueprints/Activation/BP_CubeSpawn.BP_CubeSpawn:EventGraph.K2Node_SpawnActorFromClass_0&#39;&quot;\n   NodePosX=1680\n",
  "lines_of_code": 369,
  "id": 160375,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjAzNzUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzozNyswMDowMCJ9--4311559f805acbd7e6607d70f3ee724bf9c8040056293eff871d78de119fded9",
  "settings": {
    "is_hidden": false
  }
}
```

You can now exit the blueprint editor and return to the level editor.

## Add the Cube Spawn Blueprint to the Level

Next, you’ll set up a `BP_CubeSpawn` and a `BP_Switch` to the level.

The cube-spawner blueprint has no visual components, so you can place it within any geometry or art assets to create the effect of a cube falling out of that geometry.

Pick a location in your level and use the meshes in the **Content > LevelPrototyping > Meshes** folder to block out some geometry to represent the cube spawner.

If you’re using the sample level, you can place it in the space at the back of Room 1. For this example, we’ll use a cylinder to represent a pipe that the cubes can spawn inside and fall out of.

Then, to set up a `BP_CubeSpawn` in a level, follow these steps:

1. In the **Content Browser**, navigate to the **Content > Adventure Game > Designer > Blueprints > Activation** folder.
2. Drag the `BP_CubeSpawn` blueprint into a desired location in the level. [Video: V_PiUfFm](https://dev.epicgames.com/community/api/cms/videos/V_PiUfFm/embed.html)
3. From the **Content Browser**, drag the `BP_Switch` blueprint into the level within line of sight of the cube spawner. ![Image](https://dev.epicgames.com/community/api/documentation/image/f52d0277-a8a7-4f77-b2d7-327a7dcfa91a)
4. Select the `BP_Switch` actor in the level.
5. In the **Details** panel, under the **Setup** section, add a new array element to the **Interact Object List**.
6. Use the dropdown next to **Index [0]** to select the `BP_CubeSpawn` actor. This passes the **fnBPISwitchOn** event from this switch to the `BP_CubeSpawn` actor. ![Image](https://dev.epicgames.com/community/api/documentation/image/c914d0ed-6f51-4175-bf4e-d6f3a238e4e3) ![Image](https://dev.epicgames.com/community/api/documentation/image/d8c20d74-46af-4dda-8d60-0cce7b1aa67e)
7. Select the `BP_CubeSpawn` actor. Optionally change the **Max Cubes Allowed** variable to the number of cubes you want to allow in the level.

Now, if you play the game, you can step on the switch to spawn new cubes.

[Video: V_unwx3P](https://dev.epicgames.com/community/api/cms/videos/V_unwx3P/embed.html)

## Next Up

To continue working on your level by adding materials, lighting, post-process effects, sound, and visual effects, try the Artist Track Tutorial Series:

- [Related Document](en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game.md)

If you are interested in packaging your project, as a standalone program to test and share, see the following documentation:

- Related Document
