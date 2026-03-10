# Environment Query System Quick Start

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-quick-start-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "It is recommended that you proceed through the <a data-document-id=\"3228784\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---quick-start-guide\">Behavior Tree Quick Start Guide</a> or have some prior knowledge of Blueprints and Behavior Trees in Unreal Engine 5 before proceeding with this guide.",
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

The **Environment Query System (EQS)** can be used within [Behavior Trees](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-trees-in-unreal-engine) to poll the environment through a variety of [Tests](https://dev.epicgames.com/documentation/en-us/unreal-engine/eqs-node-reference-tests-in-unreal-engine), then based on the results of those Tests, can make decisions on how to proceed. Some example use cases for EQS could be to have an AI character find a cover location away from the Player or to find the nearest health or ammo in the Level.

An Environment Query is made up of several different pieces. You can call an Environment Query from a Behavior Tree, and then the actual Environment Query will use its [Generator](https://dev.epicgames.com/documentation/en-us/unreal-engine/eqs-node-reference-generators-in-unreal-engine), reference its [Contexts](https://dev.epicgames.com/documentation/en-us/unreal-engine/eqs-node-reference-contexts-in-unreal-engine), and use its Tests to give the Behavior Tree the highest weighted result.

In this guide, we create an AI that randomly moves around the environment until seeing the player. When seeing the player, the AI uses the EQS system to find a location in the environment that provides the best vantage point while maintaining its distance. This can be useful in situations where you have an AI character that performs some form of ranged attack, as the AI will keep its distance from the player and try to retain a line of sight as seen in the example below.

[Video: 1_87evva97](https://dev.epicgames.com/community/api/cms/videos/1_87evva97/embed.html)

By the end of this guide, you will have a basic understanding of the following systems:

1. Blueprint Visual Scripting
2. AI Controllers
3. Blackboards
4. Behavior Trees
5. Environmental Query System (EQS)
6. EQS Contexts
7. AI Debugging Tools

## 1 - Required Project Setup

In this step, we'll set up our project with some of the assets we'll need for our AI as well as enable the EQS system.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For this guide, we are using a new <strong>Blueprint Third Person Template</strong> project.",
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

1. Inside your project, in the **Settings > Plugins** section, enable the **Environment Query Editor** option if necessary. ![In the Project Settings,enable the Environment Query Editor option](https://dev.epicgames.com/community/api/documentation/image/a3579263-9816-4329-8d3e-9bc45487b571) Enabling the EQS system will allow you to create and access EQS-related assets.
2. In the **Content > ThirdPerson > Blueprints** folder, copy the **BP\_ThirdPersonCharacter** over to a new folder called **AI**. ![Copy the BPThirdPersonCharacter over to a new folder called AI](https://dev.epicgames.com/community/api/documentation/image/16788de7-6922-45d4-b176-006aa980d02b)
3. In the **AI** folder, create the following three AI assets from the **+Add > Create Advanced Asset > Artificial Intelligence** option: ![In the AI folder create the following three AI assets from the Add option](https://dev.epicgames.com/community/api/documentation/image/63c01e23-ef70-4f5e-a1f8-699b92db10c1) **Blackboard** named **BB\_Enemy** **Behavior Tree** named **BT\_Enemy** **Environment Query** named **EQS\_FindPlayer**
4. Create a new **Blueprint Class** of the **AIController** type and call it **AIC\_Enemy**. ![Create a new Blueprint Class of the AIController type and call it AIC_Enemy](https://dev.epicgames.com/community/api/documentation/image/f53807cc-538b-475c-87f4-d7decdc3540e)
5. Create a new **Blueprint Class** of the **EnvQueryContext\_BlueprintBase** type and call it **EQC\_PlayerContext**. ![Create a new Blueprint Class of the EnvQueryContextBlueprintBase type and call it EQCPlayerContext](https://dev.epicgames.com/community/api/documentation/image/61c63ce7-32a1-4149-9dec-f8b82b64b4bc) **Contexts** can be used in the EQS system for reference when applying various Tests, for example, "EQS, how close am I to the specified Context" is a Test we could run. This asset will be used to provide the Player Character as a Context when we perform Tests a little later in this guide.

## 2 - Environment Query Context

In this step, we establish a Context for the EQS system of the Player Character that will be used in Tests later in the guide.

1. Open the **EQC\_PlayerContext** asset, then in the **My Blueprint** panel, override the **Provide Single Actor** function. ![In the My Blueprint panel override the Provide Single Actor function](https://dev.epicgames.com/community/api/documentation/image/6546cd3d-aac5-4e10-bc37-a1a07191c954) You can provide individual **Actors** or **Locations** as a Context as well as a set of **Actors** or **Locations**.
2. In the **Provide Single Actor** function, use a **Get Player Character** call as the **Resulting Actor**. ![Use a Get Player Character call as the Resulting Actor](https://dev.epicgames.com/community/api/documentation/image/075af71f-ff7b-49d7-a48c-58b3d3f6307c) This will retrieve the Player Character at run-time as the Context.

## 3 - EQS Setup

In this step, we jump into the EQS editor and set up the Tests for finding a location that has a line of sight to the Player Character.

1. Inside **EQS\_FindPlayer**, drag off the **Root** node in the graph and add a **Points: Grid** node. ![Drag off the Root node in the graph and add a Points: Grid node](https://dev.epicgames.com/community/api/documentation/image/ee497d4c-1295-4af0-8668-fb51cc962063) Several different types of **Generators** are used to create **Items** about a Context. Those items are then used in Tests (for example, how far is Item X from Context Y). From the results of the Tests, Items are culled or scored and can be used to determine what is the "best" (highest or lowest scoring) option. In this example, we will generate a series of points on a grid around the AI that will put it into a position where it can see the Player Character.
2. In the **Details** panel, change the **GridHalfSize** to **800** and the **Space Between** to **150.0**. ![Change the GridHalfSize to 800 and the Space Between to 150.0 in the details panel](https://dev.epicgames.com/community/api/documentation/image/c9ca99dd-78b0-41a2-bce6-ebcf6df4f359) These settings are used to define the possible number of points to test against and the distance between those points. For performance reasons, you will want to keep this to a manageable size, as having a grid too large may start to impact your game's performance. Using the **Generate Around** field, you can determine where the grid should be placed (in this case, around the querier or AI character). While it will also work if we set **Generate Around** to use the Player Context we created, we don't want the AI to move up to a point on the grid near the Player if it already has a line of sight to the Player. The **Projection Data** option provides additional fields for determining how the grid is generated, for this example, we can leave these as default but you can come back and adjust these settings if you desire.
3. Right-click on the **SimpleGrid** node and under **Add Test** select **Trace**. ![Right-click on the SimpleGrid node and under Add Test select Trace](https://dev.epicgames.com/community/api/documentation/image/95280ee8-0044-4fdd-9419-72a4e4946c8c) The **Trace** Test will be used to determine if a point on the grid can see the Player Character.
4. Right-click and add another Test, of the **Distance** type**.** ![Right-click and add another Test of the Distance type](https://dev.epicgames.com/community/api/documentation/image/09d43228-f30e-4f6f-9947-60c367be8a93) After the **Trace** Test returns points that can see the Player Character, the **Distance** Test will be used to score those points based on their proximity to the Player Character.
5. Select the **Trace** Test, then in the **Details** panel set the following options: ![Select the Trace Test and in the Details panel set the following options](https://dev.epicgames.com/community/api/documentation/image/301349b8-bfca-4c50-880f-c852f20e41ad) **Test Purpose** = **Filter Only** **Context** = **EQC\_PlayerContext** **Bool Match** = **Disabled** Here we are providing the Player Character as the point of reference (Context) in the **Trace** Test for visibility. By disabling the **Bool Match** option, we are stating that we want to filter out any points that cannot see the Player Character.
6. Select the **Distance** Test, then in the **Details** panel, change the **Test Purpose** to **Score Only** and the **Scoring Factor** to **-1.0**. ![Change the Test Purpose to Score Only and the Scoring Factor to -1.0 in the Details panel](https://dev.epicgames.com/community/api/documentation/image/0acbfb65-4ccb-47ec-946f-ed1a0b0e4181) The **Distance** Test Purpose is to score the Items returned and the Scoring Factor of -1.0 scores points that are closer to the Player's Character. If we leave this as 1.0, it will return points that are furthest away from the player which may cause the AI to run right past the Player Character in an attempt to reach the furthest point. There are additional scoring options such as clamping the scores to a minimum or maximum value, changing the **Scoring Equation** which changes the curve equation applied to the normalized score before being multiplied by the **Scoring Factor**, defining the **Normalization Type** or assigning a **Reference Value** used to normalize scores. For this example, we can leave these all at their default settings.

## 4 - Blackboard and Behavior Tree Setup

In this step, we set up the Blackboard Keys and lay out the branches of our Behavior Tree.

1. In the **BB\_Enemy** Blackboard asset, create the following three Keys: ![Create the following three Keys in the BB_Enemy Blackboard asset](https://dev.epicgames.com/community/api/documentation/image/37c1a2c4-d479-4fa1-b4d3-74712b971c82) **Bool** named **HasLineOfSight** **Vector** named **MoveToLocation** **Object** with **Base Class** set to **Actor** named **TargetActor** These Keys will be used to update and move between branches in our Behavior Tree.
2. Open the **BT\_Enemy** Behavior Tree and create the graph below using **Selectors**, **Sequences**, and a **Wait Task** node: ![Open the BT_Enemy Behavior Tree and create the graph below using Selectors, Sequences and a Wait Task node](https://dev.epicgames.com/community/api/documentation/image/a8df7bc3-8ee5-41ab-877a-a29f7f6c1dfd) Above, we have three main branches. The left most branch uses a **Selector** node (which we have named **In Combat**) to switch between two **Sequence** nodes (one called **Attack** and another called **Move into Position**). When the AI is not executing the "In Combat" branch, it will execute the next branch which we have named **Patrolling**. In the event for some reason, the AI is not in either combat or patrolling, we have a fail-safe task to wait (which we have set to 1 second) before trying to move to another branch.

## 5 - Behavior Tree: Patrol Setup

In this step, we set up the patrolling branch of the Behavior Tree.

1. Off the **Patrolling** Sequence node, add a **Move To** Task (set to **MoveToLocation**) and a **Wait** Task (set to **5** +/- **1** second). ![Add a Move To Task and a Wait Task oiff the Patrolling Sequence node](https://dev.epicgames.com/community/api/documentation/image/65d6a1ce-d773-4be5-9141-9dd5406d9091) This will instruct the AI to move to the Blackboard Key **MoveToLocation** and then wait the specified time, however, we still need to define the vector value for **MoveToLocation.**
2. From the Toolbar create a **New Task**, then in the **Content Drawer**, call it **BTT\_RandomLocation.** ![From the Toolbar create a New Task then in the Content Drawer call it BTT_RandomLocation](https://dev.epicgames.com/community/api/documentation/image/bb80f787-2c17-498a-b027-6ec31f0da8cb)
3. In **BTT\_RandomLocation**, recreate the Blueprint Graph below: ![Blueprint Graph](https://dev.epicgames.com/community/api/documentation/image/0f5cc6d8-163d-4b6b-825b-1200bddcda10) Using an **Event Receive Execute AI** node, off the **Controlled Pawn** you can **Get Actor Location** and use that as the **Origin** for the **Get Random Reachable Point in Radius** function (which we've set to **1000** as the **Radius**). Use the **Return Value** from the **GetRandomReachablePointInRadius** node as a **Branch** condition. Off the **True** pin, use the **Random Location** value and **Set Blackboard Value as Vector** with the Key being a **Blackboard Key Selector** variable called **MoveToLocation**. Off the **False** pin, **Set Blackboard Value as Vector** with **Get Actor Location** as the **Value**. This is if a random point is not found, we take the character's existing location before trying to find a new location. End the Task with both execution wires feeding into a **Finish Execute** node with **Success** enabled.
4. In the Behavior Tree, add the **BTT\_RandomLocation** Task (setting **MoveToLocation** in the **Details** panel) as the first node under **Patrolling**. ![Add the BTT_RandomLocation Task in the Behavior Tree](https://dev.epicgames.com/community/api/documentation/image/bf97da32-2730-41c0-a6f6-9d86021eb49d)

## 6 - Behavior Tree: In Combat Setup

In this step, we set up the tasks associated with the In Combat branch including our EQS\_FindPlayer query used to find a location that has a line of sight to the Player Character.

1. Right-click on the **In Combat** Selector and add a **Decorator** of the **Blackboard** type with the following settings: ![Right-click on the In Combat Selector and add a Decorator of the Blackboard type](https://dev.epicgames.com/community/api/documentation/image/32c903a7-2d88-47e1-9850-fe8307198b96) **Observer aborts** set to **Lower Priority** **Blackboard Key** set to **TargetActor** Here we are stating that once TargetActor becomes set, execute the In Combat branch aborting any lower priority tasks.
2. Right-click on the **Attack** Sequence and add a **Decorator** of the **Blackboard** type with the following settings: ![Right-click on the Attack Sequence and add a Decorator of the Blackboard type](https://dev.epicgames.com/community/api/documentation/image/611fa747-8688-4c38-9b23-cdd68d3bad0f) **Notify Observer** set to **On Value Change** **Observer aborts** set to **Lower Priority** **Blackboard Key** set to **HasLineOfSight** Here we are stating that if **HasLineOfSight** is Set, then execute the Attack branch. If **HasLineOfSight** is not set, execute a different branch until **HasLineOfSight** is set again.
3. Off the **Attack** node add a **Rotate to face BB entry** (set to **TargetActor**). ![Off the Attack node, add a Rotate to face BB entry](https://dev.epicgames.com/community/api/documentation/image/50595842-3d50-452d-ac3c-1c85ee1dea44) This will cause the AI to rotate towards the TargetActor while in the "attack" branch. For this example, we do not have an attack to give our AI however this is something you can add later on if you desire.
4. Off the **Move Into Position** node, use the **Run EQSQuery** node. ![Off the Move Into Position node use the Run EQSQuery node](https://dev.epicgames.com/community/api/documentation/image/2295faf9-c0e5-46b1-b594-5817afe5a702) The Run EQSQuery node can be used to execute an EQS Query that will update the assigned Blackboard Key.
5. In the **Details** panel for the **Run EQSQuery** node, set the **Blackboard Key** to **MoveToLocation** and the **Query Template** to **EQS\_FindPlayer**. ![Set the Blackboard Key to MoveToLocation and the Query Template to EQSFindPlayer](https://dev.epicgames.com/community/api/documentation/image/cb921b9c-afbd-4fb3-b858-d5851f4c3e6d)
6. Add a **MoveTo** (set to **MoveToLocation)** and **Rotate to face BB entry** (set to **TargetActor**) following the **Run EQS Query.** ![Add a MoveTo and Rotate to face BB entry following the Run EQS Query](https://dev.epicgames.com/community/api/documentation/image/1d5f17c3-bd4d-484a-9487-7608b36a7eba) The Behavior Tree will run the EQS Query to update the Blackboard Key **MoveToLocation** and the AI will then move to that location and rotate to face the **TargetActor** (Player Character). The full Behavior Tree should look like the following: ![Behavior Tree](https://dev.epicgames.com/community/api/documentation/image/716eddba-21c8-4528-a9f9-c987f50fd61a)

## 7 - AI Controller Setup

In this step, we set up our AI Controller to run our Behavior Tree as well as provide a way for the AI to see the Player Character using AI Perception.

1. In the **AIC\_Enemy** Blueprint, add an **Event On Possess** and connect to a **Run Behavior Tree** (set to **BT\_Enemy)**. ![IAdd an Event On Possess and connect to a Run Behavior Tree](https://dev.epicgames.com/community/api/documentation/image/24aa36be-bfd5-4d2e-b8a4-c9f5d5cbf05d)
2. Add an **AIPerception** component with the following **AI Sight config** settings: ![Add an AIPerception component with the following AI Sight config settings](https://dev.epicgames.com/community/api/documentation/image/1fa43335-e70f-44d0-ab9e-c1c991ef83e7) **Senses Config** add an **AI Sight config** **Detect Neutrals** set to **enabled** This will enable the AI to sense other Actors and fire an event when an Actor has been perceived by the Perception system. Currently, by default, Players do not get assigned an affiliation and can only be assigned one through C++ code. To circumvent this, we are enabling neutrals to be detected by the Perception system and will use Actor tagging to only perceive Actors tagged as "Player".
3. For the **AIPerception** component, under **Events**, add an **On Target Perception Updated** then promote the **Actor** pin to a variable called **Perceived Actor.** ![Add an On Target Perception Updated then promote the Actor pin to a variable called Perceived Actor](https://dev.epicgames.com/community/api/documentation/image/561bb45f-48f2-476b-8036-02e28d57ea9d) *Click image for full view.* When the AI perceives something, that Actor will be stored as a variable which we will use later to update our Blackboard.
4. Add two **Branch** nodes with the following conditions: ![Add two Branch nodes with the conditions](https://dev.epicgames.com/community/api/documentation/image/05d5b8f8-c08a-42f7-b62e-c3da5332ac68) *Click image for full view.* 1st Branch **Condition** set to **Actor Has Tag** with the **Tag** of **Player** and the **Target** beingthe **Actor** from **Perception Updated**. 2nd Branch **Condition** set to **Successfully Sensed** from the **Stimulus** pin of **Perception Updated** Event. Above, if the perceived Actor has the Tag of Player, the Branch continues to check if that Actor was successfully sensed or not. If it doesn't have the Tag of Actor (another enemy perhaps) it does not proceed on.
5. Off the **False** pin of the 2nd Branch, add the 3 nodes shown below: ![Off the False pin of the 2nd Branch, add the 3 nodes](https://dev.epicgames.com/community/api/documentation/image/ea18ab66-8df7-4910-8848-ac0fd06a5f8a) Above we have a **Set Timer by Event** node (set to **8.0**) and promoted the **Return Value** to a variable called **LostSightTimer**. We then assign a Custom Event we created and called **LostSight** as the **Event Delegate.**
6. Create 2 Functions in the **My Blueprint** panel called: **UpdateSightKey** and **UpdateTargetKey**. ![Create UpdateSightKey and UpdateTargetKey Functions in the My Blueprint panel](https://dev.epicgames.com/community/api/documentation/image/ce5a539e-335f-4120-aa82-da26378d6a87) We will use these two functions to update our Blackboard Keys that are used to make decisions in our Behavior Tree.
7. For **UpdateSightKey**, add a **Bool** input called **HasLineOfSight**. ![Add a Bool input called HasLineOfSight](https://dev.epicgames.com/community/api/documentation/image/5642cec6-8c5a-4c7d-bc24-830219749696)
8. In **UpdateSightKey** right-click and get the **Blackboard** variable, then **Set Value as Bool** with **Key Name** using **HasLineOfSight**. ![In UpdateSightKey right-click and get the Blackboard variable and Set Value as Bool with Key Name using HasLineOfSight](https://dev.epicgames.com/community/api/documentation/image/c8539793-57e4-487b-8ce1-6bb5e1e7ea27) This enables us to use this function to pass through a bool value to our Blackboard Key, updating the **HasLineOfSIght** key.
9. For **UpdateTargetKey**, add an **Actor** input called **TargetActor**. ![Add an Actor input called TargetActor for UpdateTargetKey](https://dev.epicgames.com/community/api/documentation/image/e39a799d-8eef-4514-bdf8-ac11970aa0d3)
10. In **UpdateTargetKey** right-click and get the **Blackboard** variable, then **Set Value as Object** with **Key Name** using **TargetActor**. ![In UpdateTargetKey right-click and get the Blackboard variable and Set Value as Object with Key Name using TargetActor](https://dev.epicgames.com/community/api/documentation/image/15b3a356-1ab6-4326-9998-f6f441baa01c) Similar to the UpdateSightKey function, this is used to update the Blackboard Key **TargetActor** with whatever Actor we pass through.
11. Add **UpdateSightKey** and **UpdateTargetActor** functions to the **False** condition as shown: ![Add UpdateSightKey and UpdateTargetActor functions to the False condition](https://dev.epicgames.com/community/api/documentation/image/b04db920-278d-4ea9-b5b3-b3830ad4f5dc) When the AI Perception does not successfully sense the Actor who has the tag of Player, the false condition will start a timer (storing it in a handle for later) and will update the Blackboard Key **HasLineOfSight** to false. After the time specified (8.0 seconds), the Custom Event **LostSight** will execute, clearing the **TargetActor** Blackboard Key (meaning we no longer are targeting the Player and have lost sight of them).
12. Off the **True** pin of the 2nd Branch, use **LostSIghtTimer** and **Clear and Invalidate Timer by Handle**. ![Off the True pin of the 2nd Branch use LostSIghtTimer and Clear and Invalidate Timer by Handle](https://dev.epicgames.com/community/api/documentation/image/87d0c6d6-42e3-4a75-a20c-8fb1add49d73) This will stop and reset the Timer used when losing sight of the Player Character.
13. Add the **UpdateSightKey** (set to **enabled)** and **UpdateTargetKey** (set to **Perceived Actor**). ![Add the UpdateSightKey and UpdateTargetKey](https://dev.epicgames.com/community/api/documentation/image/573d33cb-5694-40a1-8c36-86ca858c6d40) The full graph should look similar to below: ![Full Graph](https://dev.epicgames.com/community/api/documentation/image/b70c6022-47cb-4276-bfea-b3e37eba4cb6) Our AI Controller is now set up, runs our Behavior Tree, and updates our Blackboard Keys based on when we perceive an Actor with the tag Player through the AI Perception system.

## 8 - Final Setup

In this step, we set up the enemy AI Character Blueprint, add the Tag Player to the Player Character Blueprint so it can be perceived by the AI, and add a NavMeshBoundsVolume and some meshes so the AI knows how to move around the environment and we can break line of sight easier.

1. Open **BP\_Enemy**, in the **Details** panel, enable **Use Controller Rotation Yaw** and set **AI Controller Class** to **AIC\_Enemy**. ![Open BP_Enemy and in the Details panel enable Use Controller Rotation Yaw and set AI Controller Class to AIC_Enemy](https://dev.epicgames.com/community/api/documentation/image/301c2750-46b4-4439-99cf-1c50aff1fe6e) For the AI to execute the rotate task inside the Behavior Tree, we need to enable Controller Rotation Yaw. We also assign the custom AI Controller class that has our logic in it and runs the Behavior Tree. Optionally, we deleted all the script that was copied over from the Player Character (as well as the Camera Component) as we will not need it for the AI Character.
2. From the **Modes** panel, add a **NavMeshBoundsVolume** to the Level and scale it so it encapsulates the Level. ![Add a Nav Mesh Bounds Volume to the Level and scale it so it encapsulates the Level from the Modes panel](https://dev.epicgames.com/community/api/documentation/image/c31676ca-72ed-4544-98df-ca1cfbede813)
3. Right-click on the **BP\_ThirdPersonCharacter** in the Level, then select **Edit BP\_hirdPersonCharacter**. ![Right-click on the BPThirdPersonCharacter in the Level, then select Edit BPThirdPersonCharacter](https://dev.epicgames.com/community/api/documentation/image/60546ca0-bf14-4e7c-96e4-633f2c34a7fa)
4. In the **Details** panel, search for **Tag**, then add a **Tag** called **Player**. ![Search for Tag, then add a Tag called Player in the Details panel](https://dev.epicgames.com/community/api/documentation/image/637c24f6-a720-4299-8fd2-3a5a8142d2b3) Inside our **AIC\_Enemy** Blueprint when the AI Perception system perceives an Actor, this Actor has the tag of Player so our Branch will be evaluated as True.
5. Inside the Level, scale up and add multiple versions of the **Cube Mesh** to provide additional cover points to break the line of sight. ![Scale up and add multiple versions of the Cube Mesh to provide additional cover points to break line of sight](https://dev.epicgames.com/community/api/documentation/image/fdb52842-d75b-43b8-aae5-d1d4cf4dbd05)
6. Click the **Play** button from the Toolbar to play in the Level.

## 9 - End Result

While playing in the Editor, the AI will patrol around randomly until seeing the Player. After seeing the Player, it will rotate and face the Player and attempt to move to a new location when losing sight of the Player. Using EQS, it will find a location that will provide a line of sight to the Player but remain a distance away. If it does not see the Player again while moving to a new location, after some time the AI will give up chasing and go back to patrolling as portrayed in the video below.

[Video: 1_87evva97](https://dev.epicgames.com/community/api/cms/videos/1_87evva97/embed.html)

You can use the [AI Debugging Tools](https://dev.epicgames.com/documentation/en-us/unreal-engine/ai-debugging-in-unreal-engine) to view any active EQS queries (in addition to Behavior Trees or Perception info). To activate AI Debugging at runtime, press the **'** (apostrophe) key, then select 1 (for general AI debugging), 2 (for Behavior Trees), 3 (for EQS), or 4 (for AI Perception). Below, we activate AI Debugging and bring up the EQS Debugging tools.

[Video: 1_7uo0j5cp](https://dev.epicgames.com/community/api/cms/videos/1_7uo0j5cp/embed.html)

While the EQS Debugging tools are running, you can see the points from our Grid test along with their score values. You will also see which point was selected, denoted with the text **Winner**. These tools are useful to see which points are being evaluated and why one point may have been selected over another point based on the score values.

In addition to using the EQS Debugging tools, there is a special type of Pawn called the **EQS Testing Pawn** that can be used to debug EQS queries while in the Editor. You can create this Pawn, by creating a new Blueprint Class of the **EQS Testing Pawn** Class.

![You can create EQS Testing Pawn by creating a new Blueprint Class of the EQS Testing Pawn Class](https://dev.epicgames.com/community/api/documentation/image/f00ae485-f8f4-4f8b-823b-0e57d97e6fcf)

Our current setup uses the Player Character as a Context for evaluation in our EQS Test. To test while the game is not running, we would need to make a slight modification to the **EQS\_PlayerContext** Blueprint and override the **Provide Actors Set** function.

![We need to make a slight modification to the EQS_PlayerContext Blueprint and override the Provide Actors Set function](https://dev.epicgames.com/community/api/documentation/image/da80cd69-5dd6-4d40-b9e3-58c0a6e81907)

We can use **Get All Actors of Class** set to **BP\_ThirdPersonCharacter** which provides the **Resulting Actors Set**:

![We can use Get All Actors of Class set to BP_ThirdPersonCharacter which provides the Resulting Actors Set](https://dev.epicgames.com/community/api/documentation/image/49087c48-8e91-4bb2-a8b5-a771ebe6067c)

When adding the EQS Testing Pawn to the Level, in the **Details** panel, you can assign the **Query Template** (which we've set to our **EQS\_FindPlayer** query).

![You can assign the Query Template in the Details panel,](https://dev.epicgames.com/community/api/documentation/image/932a2532-1365-4973-b095-f97fbefbd25e)

This enables you to see the results of your test while in you are in the Editor as seen below:

[Video: 1_nyr7ia05](https://dev.epicgames.com/community/api/cms/videos/1_nyr7ia05/embed.html)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "EQS Data is also being recorded through VisLog which you can reference. Please see <strong>Visual Logger</strong> for more information.",
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
