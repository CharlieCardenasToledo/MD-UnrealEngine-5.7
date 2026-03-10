# Dynamic Asset Selection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/dynamic-asset-selection-in-unreal-engine

> Application Version: 5.7

You can use a combination of **Proxy**, **Proxy Table** and **Chooser Table** assets to build dynamic asset selection logic, to drive animations based on variables in your project. For example, you can use Proxy and Proxy Table assets to select what kind of animation set should be loaded and used for your character, such as different weapon sets. Alternatively, you can use Chooser Tables to dynamically select individual animation assets, such as different hit reactions based on the location your character is hit, using contextual variables from your project.

You can use the following document to learn more about setting up a dynamic animation selection system in Unreal Engine.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Though this documentation focusses on using Choosers and Proxy Tables to select animation related assets such as Animation Sequences, Montages, or AnimInstance classes, the system itself is generic and can be used to select any type of Asset, Object, or Class.",
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

#### Prerequisites

- Enable the **Chooser** plugin. Navigate in the **Menu Bar** to **Edit** > **Plugins** and locate **Chooser** in the **Animation** section, or use the **Search Bar**. Enable the plugin and restart the editor. ![Image](https://dev.epicgames.com/community/api/documentation/image/32f3966a-7151-4175-9685-088079350b3b)
- Your project contains a set of animations you wish to dynamically select based on contextual situation at runtime. This could be unique cosmetic animation sets, relevant gameplay animations such as contextual animation sineros, or animation sets relevant to equipable items like weapons.
- Your project contains a functional Animation Blueprint, that you can build dynamic Animation selection logic in.

## Set Up an Animation Selection System

Here you can read about how to set up an animation chooser system in your project to dynamically select hit reaction animation playback based on context in your project at runtime.

### Create a Proxy Asset

A **Proxy Asset** is used to store the contextual information of which [Proxy Table](https://dev.epicgames.com/documentation/en-us/unreal-engine/dynamic-asset-selection-in-unreal-engine#create-proxy-table-assets) asset is active, and other relevant variables.

To create a Proxy Asset, use (**+**) **Add** in the **Content Browser** and navigate to **Miscellaneous** > **Proxy Asset**.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/7e4c7625-13ea-4865-ad1e-49e721967ebb)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Create a Proxy Asset for each animation set you wish to dynamically select animations from to drive the character, such as an idle, walk, or run set.",
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

After creating the Proxy Assets, open each to access their settings.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/c8c12200-d70c-431d-acfc-b3ecb6bc1d3a)

For each Proxy Asset, set the **Type** property to the animation asset type you are using, in this case `AnimSequenceBase`.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/f06f223a-7b91-47b7-ab7b-e4a731d67ebd)

Set the **Context Data** property to the **Animation Blueprint** option by adding a new **Index** array using (**+**) **Add**, selecting **Context Object Type Class** option.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/fc2d51fb-9318-4f0a-be4a-b471b8fec501)

Expand the **Index** array's settings and set the **Class** property to use your Animation Blueprint, in this case `ABP_Manny`. Then ensure the **Direction** property is set to **Read**.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/ffe06d54-8359-4fdb-b77d-555c36904ae1)

### Animation Blueprint Set Up

After setting up your Proxy Asset, you must create a variable in your character's animation blueprint in order to store the active proxy table during runtime. To create this variable, open your characters Animation Blueprint and create a new Variable in the **My Blueprint** panel using (**+**) **Add**. Then set the Variable type to a **Proxy Table Object Reference**. After creating the variable, **save** and **compile** your Animation Blueprint.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/1fd84cbf-af18-4b53-a121-e17d3a89d890)

The Proxy Table variable will be used in your animation graph by an Evaluate Proxy node, to determine the active Proxy Table at runtime.

### Create Proxy Table Assets

A **Proxy Table** asset is used to store the animation assets sets, that can be dynamically selected at runtime. For example, one Proxy Table may store a character's Idle animations while another may store its Walking or Running animation set.

To create a Proxy Table asset, use (**+**) **Add** in the **Content Browser** and navigate to **Miscellaneous** > **Proxy Table**.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/15228117-f019-43d0-9850-e35fa233ac4a)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Create a Proxy Table asset for every contextual situation that a different animation set would be needed, such as locomotion animation sets for unarmed characters and characters holding a pistol or rifle.",
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

After creating a Proxy Table asset, open the asset to access the Proxy Table's values.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/2aff21eb-b96e-4cb8-beee-f6df86f79470)

In the ProxyTable, add an entry for each **Proxy Asset** using (**+**) **Add Row** and selecting asset. You can then assign the associated animation asset from the set using the Value Column.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/04b9fca7-3606-4e90-9237-40ced04d43c8)

In the following workflow example, a `ProxyTable_Unarmed` asset is assigned an `Unarmed_Idle` and an `Unarmed_Walk` animations to the respective `ProxyAsset_Idle` and `ProxyAsset_Walk` rows. Then in a `ProxyTable_Pistol` asset, the same Proxy Asset rows are assigned with a `Pistol_Idle` and `Pistol_Walk` animations respectively.

| ProxyTable\_Unarmed | ProxyTable\_Pistol |
| --- | --- |
| ![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/9b740a53-fcc5-4760-b811-7192cf11283c) | ![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/79d11da4-4869-4c96-9218-2b2150bd2984) |

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The Value column can also contain a <strong>Class</strong> reference, a <strong>Chooser Asset</strong>, or a <strong>Lookup Proxy</strong> for more dynamic animation selection systems.",
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

### Using Proxy Tables at Runtime

You can use Proxy Table assets at runtime using an [Animation Node function](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-node-functions-in-unreal-engine) on a Sequence Player node. To create a new function to select a Proxy Table asset, select the Sequence Player node, and add a new Function at the **On Update** binding.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/49825a10-9194-46fb-9514-14b88f1d8d18)

Add an **Evaluate Proxy** node from the **On Update** node.

Then select the node and select the Proxy Asset in the Proxy property using the drop down.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/831bf96d-c54b-498b-8e42-5afe53fd6185)

Then promote the result to a Variable, and connect the output to the Sequence Player node.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/153272fc-be81-4f26-870e-73e9f427d072)

You can then set the active Proxy Table asset on the Evaluate Proxy node using a variety of methods, such as a Chooser Table, to dynamically change the animation set driving the character.

[Video: V_hTPqF2](https://dev.epicgames.com/community/api/cms/videos/V_hTPqF2/embed.html)

### Create a Chooser Table Asset

A chooser asset is used to store animation data sets that comprise of an animations various iterations, that can be selected and played back based on the context. For example, a chooser table may contain a set of hit reaction animations, with each entry being an animation that reacts based on a different part of the body being hit (arms, legs, chest, head), that can then be selected based on a contextual variable, such as the location of the hit.

To create a Chooser Table asset, use (**+**) **Add** in the **Content Browser** and navigate to **Miscellaneous** > **Chooser Table**.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/dad6ad4d-3055-4f33-9483-be80ab05ec2e)

After creating a Chooser Table, you can open the asset to access its properties.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/5ce2b151-48f0-4ce0-a210-2f18b24a0289)

Create a new Array element in the Context Data property using (**+**) **Add** and set the property to the **Context Object Type Class** option. Then expand the Index array, and set the **Class** property to your character's animation blueprint and ensure the **Direction** property is set to **Read**. You can then set the Output Object Type to the animation asset you are using. This workflow example is using Animation Sequences, so the **AnimSequenceBase** class option was selected.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/fda67403-01ce-45cb-b597-f2e72758bda5)

In the Chooser Table panel, you can begin to add Columns, in order to set the Variables from the animation blueprint you wish to influence the selection process using the (**+**) **Add Column** button. After creating a Column, you can define which Variable from your Animation Blueprint can influence the selection, and the values or states of the variable that must be reached in order to select the Animation Sequence asset within each row.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/8c971be2-2633-451a-8bf7-c681b7361e5c)

In this workflow example, the boolean variable `IsCrouching` will select the `MM_HangingIdle` animation when the value is false, and will select the `MM_Rifle_Walk_Left` when the value is true. The `MoveemntAngle` Variable will select the `MM_HangingIdle` when the value is between `-100` and `100`, while the `MM_Rilfe_Walk_Left` animation will only be selected when the value is `0.0`.

In order to drive the characters animations using this selection process, you must set your Proxy Table Entry to **Evaluate Chooser** and assign the Chooser Table asset.

![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/9c126446-5212-46cd-b251-1f77d1830ee6)

Now the selected animation will change based both on the active Proxy Table asset and the selection made by the Chooser Table.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "You can also use ChooserTables without ProxyTables using an Evaluate Chooser node in your animation blueprint graph or state machine.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 25815807,
      "caption": "",
      "alt_text": "ImageAltText",
      "image": {
        "id": 25815807,
        "file_name": "image_20.png",
        "file_size": 37008,
        "content_type": "image/png",
        "created_at": "2025-07-18T15:16:22.839+00:00",
        "height": 281,
        "width": 562,
        "storage_key": "71ae2b5a-72e2-4910-83ab-496dc1692cd9",
        "context": "documentation"
      },
      "storage_key": "71ae2b5a-72e2-4910-83ab-496dc1692cd9",
      "context": "documentation",
      "width": null,
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
