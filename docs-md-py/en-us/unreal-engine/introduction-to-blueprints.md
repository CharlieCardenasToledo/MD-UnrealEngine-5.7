# Blueprint Foundations

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-blueprints

> Application Version: 5.7

To create the functionality for gameplay objects in your level, you’ll use **Blueprint Visual Scripting**. Blueprints in Unreal Engine are assets with a physical representation and special functionality, like the player being able to pick them up.

The Blueprint Visual Scripting system can be used to create functionality without writing code, as you are using a node-based interface to create a gameplay object’s behavior.

There are different types of Blueprint assets (including data-only Blueprints), but the most common type you’ll be working with is a Blueprint Class, often shortened as **Blueprint**.

A Blueprint Class is like a recipe that uses components, variables, and Blueprint Visual Scripting to describe the properties and behaviors of objects in your game. You add instances of Blueprint classes to your level.

## Before You Begin

You’ll need a Unreal Editor project based on the [First Person](https://dev.epicgames.com/documentation/en-us/unreal-engine/create-your-first-project-in-unreal-engine#creating-a-project-with-the-first-person-template) or Third Person template (any variant).

## Open an Existing Blueprint

You created your project from a template, so there are several Blueprints that are already included in your project that you can explore and use.

One example of a Blueprint Class is the jump pad Blueprint, which has functionality that boosts the player upwards. You can add instances of this Blueprint anywhere in your level.

To open the jump pad Blueprint, follow these steps:

1. In Unreal Engine, click the **Content Drawer** button at the bottom-left corner of the screen. Alternatively, you can hold down **CTRL** and press **Space**.
2. Navigate to the **LevelPrototyping > Interactable > JumpPad** folder.
3. You will see a `BP_JumpPad` asset, which is a Blueprint Class. Double-click the asset to open it in the **Blueprint Editor**. ![BP_JumpPad](https://dev.epicgames.com/community/api/documentation/image/41ec457e-9e81-49e0-8590-c0435d2aa493)
4. By default, the Blueprint opens in a new window. You can dock a window by clicking the tab with the asset’s name near the top-left corner of the window and dragging it next to the level’s tab in the main editor. [Video: V_QAKFZS](https://dev.epicgames.com/community/api/cms/videos/V_QAKFZS/embed.html)

## Building a Level Object With Components

Let’s take a look at `BP_JumpPad`. At the top portion of the window, you can see three tabs: **Viewport**, **EventGraph**, and **Construction** **Script**.

![Blueprint Editor](https://dev.epicgames.com/community/api/documentation/image/629de3a7-cd38-4527-8030-4cc42f31dae0)

Click the **Viewport** tab. You will see the jump pad’s visual representation, with a particle effect playing on a loop. Similar to using the viewport in the main level editor, you use a Blueprint’s Viewport to see and edit a Blueprint.

In this tab, you’ll see the Blueprint’s **Components**, or the pieces that define what the Blueprint is and what is added to your level.

[Video: V_C7vj1p](https://dev.epicgames.com/community/api/cms/videos/V_C7vj1p/embed.html)

Use the **Components** tab to add, remove, and reorganize the Blueprint’s components. Let’s take a closer look at the components that are attached to the jump pad:

![BP_JumpPad Components](https://dev.epicgames.com/community/api/documentation/image/72d3be11-a1dd-418b-95e4-c205ab0f57e8)

`BP_JumpPad` has a **Point Light** component. Click the Point Light object in the components list or Viewport. You can use the **Transform** tools to move and rotate this light source.

On the right-hand side of the Blueprint Editor, you will see the **Details** panel, which lists the properties related to this light component. You can edit the **Intensity** of this light source, the **Light Color**, and more.

![Details Panel of BP_JumpPad](https://dev.epicgames.com/community/api/documentation/image/35233f00-6a1b-468a-a276-9c42ab0290ef)

## Creating Blueprint Functionality

Next to the **Viewport** tab, you can see the **EventGraph** and **Construction Script** tabs. These two tabs are used to add functionality to your Blueprint based on when they run. Here, you’ll create the logic that tells the Blueprint’s components how to behave.

The **Construction Script** runs when the level object spawns, either during gameplay or when you add it to your level in Unreal Editor. It also executes in the editor when you transform or change a property of an actor, so you see the result immediately in the viewport.

If you click on the **Construction Script** tab, you will see a **Construction Script** node that executes a chain of actions that set up the jump pad’s color and other properties when it first appears in the level (or is **spawned**).

![BP_JumpPad Construction](https://dev.epicgames.com/community/api/documentation/image/d8fb983b-f68e-4cf6-9f1b-fa3f4c5e8866)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Navigating the Blueprint Graph:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "enhanced_list",
      "style": "unordered",
      "items": [
        [
          {
            "type": "paragraph",
            "content": "<b>Pan: </b>Right-click and drag.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "<b>Zoom: </b>Use the mouse wheel.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "<b>Frame selection:</b> Press <b>F</b> to center on selected nodes.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "<b>Fit all: </b>Press <b>A</b> to view the entire graph.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "J<b>ump to: </b>Double-click a function or event node to find it in a graph or its graph tab.",
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

Click the **Event Graph** tab. The **Event Graph** contains logic that runs in response to events that happen during gameplay, such as responding to player input, triggering animations, or playing sounds. Any time you think, “when this happens, I want to do that,” you need to start with an event.

In the jump pad’s event graph, you will see a list of nodes that get executed when an actor overlaps with this Blueprint — meaning when the player walks over this Blueprint in-game. Then, it makes the character perform a jump move, but with a higher velocity than normal.

![BP_JumpPad EventGraph](https://dev.epicgames.com/community/api/documentation/image/c121bd7e-85cc-409c-864f-f1c601a365b1)

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "To find a specific node in a graph, use the <b>CTRL + F</b> shortcut in the graph views to search for a node. For example, to take a look at the <b>Event ActorBeginOverlap</b> node, use the <b>CTRL + F</b> shortcut and type <b>Event ActorBeginOverlap</b> in the search field. Select the result to pan the view to that node.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "video",
      "video_id": "V_DdqGzD",
      "provider": "kaltura",
      "caption": "",
      "autoplay": false,
      "loop": false,
      "width": 1200,
      "video": {
        "height": 1440,
        "width": 2560,
        "identifier": "V_DdqGzD"
      },
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

A node that can execute actions has an **Execution pin**, also known as an exec pin, marked by the white triangle on this node. If a node’s exec pin is not connected to another node, the triangle will have a white outline but no color.

| Connected Nodes | Disconnected Nodes |
| --- | --- |
| ![Connected Nodes](https://dev.epicgames.com/community/api/documentation/image/7868a072-55d1-4c2e-aa5a-70aba17845c4) | ![Disconnected Nodes](https://dev.epicgames.com/community/api/documentation/image/426c75ac-754e-465b-a848-11b005e6b131) |

In addition to the **exec** pin, a node can also have other pins. For example, the **Event ActorBeginOverlap** has a pin for **Other Actor**, which is a reference to the level object (actor) that overlaps with the `BP_JumpPad` level object.

You’ll notice that the **Event** node does not have any **input exec** pin. This is because an **Event** node runs as soon as the defined event has been triggered. In this example, when an actor overlaps with `BP_JumpPad`’s actor in-game, this event will trigger.

The **Event ActorBeginOverlap** node’s exec pin is connected to the **Cast To Character** node. This means that when an actor in the world, like the Player, overlaps with the jump pad actor, this Blueprint will execute the **Cast To Character** node.

If you disconnect the **Event ActorBeginOverlap** node’s **exec** pin from the **Cast To Character** node, but keep the **Other Actor** pin connected, nothing will happen since the exec pins are not connected — meaning that the **Event** node does not trigger the **Cast To Character** node.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can remove the connection between two nodes by using the shortcut <b>ALT + Left Click</b>. Create a new connection by dragging from one pin to another. Pins can only connect if their data types are compatible.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "video",
      "video_id": "V_4iAzmb",
      "provider": "kaltura",
      "caption": "",
      "autoplay": false,
      "loop": false,
      "width": 1200,
      "video": {
        "height": 1440,
        "width": 2560,
        "identifier": "V_4iAzmb"
      },
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

## Add Comments to a Blueprint

You can add comments into your Blueprints to create visual-only notes that group nodes together and explain what each part of the Blueprint does. Comments help you and your team members know at a glance what functionality your nodes are performing and keep your Blueprints organized.

When building Blueprint logic, first focus on creating the functionality, and then highlight the nodes you have added and add a comment to contain and describe them.

To add a comment in a Blueprint, follow these steps:

1. Click the graph to ensure it's the active panel.
2. Press **C** on your keyboard. This adds a comment box.
3. Double-click the text field at the top of the box to enter a comment.
4. To resize the comment, ensure the comment is selected (highlighted with a yellow outline), and drag an edge or corner.
5. To group notes within a comment, drag those nodes inside the bounds of the comment.

You can also select one or multiple nodes and press **C** to add a comment that contains the selected nodes.

[Video: V_ZguVNu](https://dev.epicgames.com/community/api/cms/videos/V_ZguVNu/embed.html)

## Using Variables to Store Blueprint Information

A Blueprint can have **variables**. A variable is a container that holds a value, like a number for the movement speed of the player, a reference to the static mesh that an asset uses, how many trees there are in a level, and more. Blueprints can use these values while executing functionality.

Look at the **My Blueprint** panel on the left side of the blueprint editor.

![BP_JumpPad MyBlueprint](https://dev.epicgames.com/community/api/documentation/image/9c52632a-1e27-4fc7-bfde-9fb9e5511eda)

Under the **Variables** section, you can see two variables: **Velocity** and **Color Target**. Click the **Velocity** variable to select it. In the **Details** panel, you can now see various properties related to this variable. At the very bottom of the list, you will see the **Default Value** category, where **Velocity** is a parameter that can be changed.

![BP_JumpPad Velocity Default Value](https://dev.epicgames.com/community/api/documentation/image/3f572939-e766-459d-9fa0-27f5b2e5f4c3)

In this case, **Velocity** is set to **0**, **0**, **800**. This means that the velocity that’s applied to the player is **800** units in the **Z axis**, which means **upwards**. So, the jump pad’s functionality takes the Velocity variable into account and says “when the player walks over this jump pad, move them **upwards** at **800** cm/second.”

If you look at the jump pad’s variables, you’ll see they have open **Eye** icons next to them. This means that these variables are **public and editable** variables, which makes them editable on all instances of that Blueprint in your level.

![Eye Icon](https://dev.epicgames.com/community/api/documentation/image/831094e4-223d-49db-a4fb-7fea8b6493e6)

To see an example of how variables can be edited outside of a Blueprint, follow these steps:

1. Click your level’s tab near the top-left corner of Unreal Editor to go back to the **Level Editor**.
2. Open the **Content Browser** and, in the JumpPad folder, drag the `BP_JumpPad` asset into the level to a desired location. Make sure it’s selected.
3. In the **Details** panel, find the category named **Default**. Under this category, you can see the two variables you saw earlier — **Velocity** and **Color Target**. These are visible here since these two variables are listed as public. ![Public Variables](https://dev.epicgames.com/community/api/documentation/image/258fa865-6d07-4e5d-87a7-c3d11509b0fd)
4. Go back to the `BP_JumpPad` tab. Under the **My Blueprint > Variables** section, click on the **Eye** icon of the Velocity variable to make it not editable. The open eye changes to a closed eye.
5. To apply your changes, click the **Compile** button on the top-left corner of the Blueprint Editor window.
6. Go back to the Level Editor, select the **BP\_JumpPad** actor, and look under the **Details > Default** section again. The Velocity variable is missing because it’s no longer instance editable.
7. Go back to the Blueprint Editor and click the Eye icon next to the Velocity variable again.
8. **Save** and **Compile** the Blueprint.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "When variables are public and editable, they can also be used by other Blueprints. For instance, in the player character Blueprint, you could detect collisions between the player and jump pad, and then read or change the jump pad’s Velocity from within the character’s event graph. If the variable is not set to public and editable, this isn’t possible.",
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

For more information about the Blueprints system, see [Blueprints Visual Scripting](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine).

## Using Blueprints to Make a Puzzle Game

You can use the **Design a Puzzle Adventure** set of tutorial documentation to use Blueprints to build a functional 3D puzzle solving platforming game.

- [Related Document](en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine.md)
