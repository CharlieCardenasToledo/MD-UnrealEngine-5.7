# Making Macros

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/making-macros-in-unreal-engine

> Application Version: 5.7

**Macros** are essentially the same as collapsed graphs of nodes. They have an entry point and exit point designated by tunnel nodes. Each tunnel can have any number of execution or data pins which are visible on the macro node when used in other Blueprints and graphs.

## Creating Macros

In this tutorial, you will create a **Macro** to check if a Character has enough energy to jump. If they do have enough energy, then your macro will deplete energy from the player, print their current value to the screen, then call the jump function. If they do not have enough energy, your macro will print to the screen that "they are out of energy", and prevent them from jumping.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For this example, we are using the Blueprint Third Person Project with <strong>Starter Content</strong> enabled.",
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

1. After **Creating** and **Launching** your project, navigate to the `Content/ThirdPerson/Blueprints` folder, and open the **BP\_ThirdPersonCharacter** Blueprint. ![Image](https://dev.epicgames.com/community/api/documentation/image/10a981fc-99e7-4439-9f1f-18817bb23598)
2. Navigate to the **My Blueprint** window, then click the **Add Macro** button. ![Image](https://dev.epicgames.com/community/api/documentation/image/8392533a-889a-42a8-af48-a14a56ae36fe)
3. A new macro is created, select it and press **F2** to rename it to **EnergyCheck**. ![Image](https://dev.epicgames.com/community/api/documentation/image/01cf17a5-fb25-44a0-824d-02f689a1f209)
4. With the macro selected, navigate to **Details** > Inputs**, click** Add(+) **to create a new** Input **named** BeginCheck**, then change its type to** Exec\*\* (Execution pin) ![Image](https://dev.epicgames.com/community/api/documentation/image/5033fae6-7cbd-485c-a9bd-e0f37f777dc8)
5. Navigate to **Details >** **Outputs**, and click **Add(+)** to create two new Outputs. Name one **HasEnergy** and the other **NoEnergy**, then set the **Exec** pin types. ![Image](https://dev.epicgames.com/community/api/documentation/image/fcffb8b0-52e3-4ab7-b63a-e3f2668cad50) For the Input, use an Exec pin called **BeginCheck** to start the Macro. Next, create a script that checks if the player has enough energy to jump and if so, execute the **HasEnergy** pin. If the player does not have enough energy, execute the **NoEnergy** pin.
6. Inside the **My Blueprint** window, click the **Add Variable** button to create a new float variable named **Energy**. ![Image](https://dev.epicgames.com/community/api/documentation/image/396269be-d1a8-4459-be6d-e90841c4843b)
7. On the Toolbar, click **Compile**, then select **Energy** and navigate to the **Details** panel to set its value to **100**. ![Image](https://dev.epicgames.com/community/api/documentation/image/7937517c-63f2-407f-b1d5-2686e208ec81)
8. In the **Energy** graph, click **B** + **Left-click** to create a **Branch** node.
9. While holding **Ctrl,** drag the **Energy** float variable from the **My Blueprint** tab into the macro graph, click and drag off the output pin to search for a **Greater** operator node, then connect the output pin to the **Branch**.
10. While holding **Alt**, drag in the **Energy** variable to add a **Set** node. ![Image](https://dev.epicgames.com/community/api/documentation/image/7891c47f-dba1-4643-afb5-442ec8b0bf87)
11. **Ctrl** drag in **Energy** again and connect it to a **Subtact**(**-**) node, set to **10** and connect it to the **Set** node. With this script, we define if Energy is > 0, subtract 10 from the current Energy value.
12. **Right-click** in the graph and add a **Print String** node, then connect the **Set Energy** node to the **In String** pin. ![Image](https://dev.epicgames.com/community/api/documentation/image/e01278ba-7166-42bc-9712-8fb4753b39b6) A **Conversion** node is added which converts the value of Energy into a string printed to the screen, displaying its value.
13. Off the **False** pin of the **Branch**, add another **Print String** node and enter the text **"Out of Energy!"** in the box. Then connect the first and second **Print String** nodes to the **HasEnergy** and **NoEnergy** pins, respectively. The macro is now set up to check (and if applicable, subtract from) the **Energy** variable and print if the player has enough energy or not, which is used to determine if the player can jump or not. Now, you need to implement the macro after pressing the "Jump" key, but before the Jump action is executed.
14. On the **EventGraph**, drag off the **Pressed** pin of **InputAction Jump** node and search for **EnergyCheck**. ![Image](https://dev.epicgames.com/community/api/documentation/image/b60fe910-b285-4b2a-aaf9-e7a7b99168e8) You should see that the macro you created is listed under **Utilities** and has the Macro icon next to its name.
15. When the macro is added, the Jump script should look similar to below. ![Image](https://dev.epicgames.com/community/api/documentation/image/8a5100ee-2c87-4499-9005-d39c3bdfea5e)
16. Click the **Compile** and **Save** buttons, then close the Blueprint. ![Image](https://dev.epicgames.com/community/api/documentation/image/92a69de0-a170-4739-a594-aad7d7d50589)
17. Click **Play** on the main **Toolbar** in the **Editor**. ![Image](https://dev.epicgames.com/community/api/documentation/image/a524e8d7-de7d-410c-8f97-47528c394d67) When you press the **Spacebar** to jump, in the upper left corner of the screen the value of **Energy** is printed to the screen. When **Energy** is 0, you should no longer be able to jump.

## End Result

![Image](https://dev.epicgames.com/community/api/documentation/image/eec25176-bf40-4c4c-935b-e19a2965aab0)

This is a basic example of using a Macro to execute and consolidate a script into a single node, improving the readability of our Event Graph and main character script.
Additionally, you could call this Macro in other instances. For example, if you have some other action that reduces the player's energy, and you want to check if they have enough energy to perform the action (like attacking), you could run this Macro to check if the player has enough energy to Attack after pressing your Attack key then execute an attack off of the **HasEnergy** exec pin.
