# Environment Query System Overview

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-overview-in-unreal-engine

> Application Version: 5.7

The **Environment Query System** (or EQS for short) is a feature within the AI Tools in Unreal Engine 5 (Unreal Engine) that can be used for collecting data about the environment. Then, through the use of a [Generator](https://dev.epicgames.com/documentation/en-us/unreal-engine/eqs-node-reference-generators-in-unreal-engine), the system can ask questions about that data through a variety of user-defined [Tests](https://dev.epicgames.com/documentation/en-us/unreal-engine/eqs-node-reference-tests-in-unreal-engine), returning the best **Item** that fits the types of questions being asked. Some example use-cases for EQS could be to find the closest health pickup or ammo, figure out which enemy is the highest threat, or find a line of sight to the Player (an example of which is shown below).

![Find line of sight to the Player](https://dev.epicgames.com/community/api/documentation/image/c6918146-ec89-4f3e-a9a3-62d117e91aa2)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The conceptual idea and theory behind EQS come from Unreal Engine 3's <strong>Environment Tactical Query</strong> (ETQ) system which you can read more about in the following article, <a href=\"https://epicgames.box.com/s/b5vbufy1pp58k638wkrdp6xeht53k1zb\">Asking the Environment Smart Questions</a>.",
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

## EQS Basics

EQS Query assets can be created in the **Content Drawer**and can be edited inside a special **Environmental Query Editor**. The Environmental Query Editor is a node-based editor where you can add a Generator node to produce Items, add your desired Tests to run on those Items and the [Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/eqs-node-reference-contexts-in-unreal-engine) in which to run them. Unreal Engine supplies many Generator types by default, however, you can create your custom Generators through Blueprint (or C++ for even faster execution).

![Add a Distance Test to our existing Generator](https://dev.epicgames.com/community/api/documentation/image/5efbbd2f-5ee2-4cf8-b355-bcb9f0e0faf5)

_Above, we add a Distance Test to our existing Generator._

Similar to Generators, there are several different types of Tests you can run to filter and (or) score the Items returned. Unlike Generators, custom Tests can only be created through C++. Multiple Tests can be added to a Generator and is a common practice to narrow down the Item results that are returned. The order in which you add Tests to a Generator does not matter as filter Tests are done before scoring Tests. This is done so that fewer Items are returned and need to be scored. Refer to the table below for the type of tests.

| Node Type | Description |
| --- | --- |
| **Generator** | This produces the locations or Actors, referred to as **Items**, that will be tested and weighted. |
| **Contexts** | These are a frame of reference for the various Tests and Generators. |
| **Tests** | These are how the Environment Query decides which Item from the Generator is the "best" option. |

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Please refer to the <a data-document-id=\"3229054\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-node-reference-in-unreal-engine\">EQS Node Reference</a> page for more information on each type.",
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

Once you have set up your EQS Query, you can run it through a [Behavior Tree](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-trees-in-unreal-engine) using the **Run EQS Query**Task node.

![Run EQS Query Task node](https://dev.epicgames.com/community/api/documentation/image/a865b3d5-28fa-4d4c-97dc-95a8b7ab6d3f)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For a full walk-through of creating and using an EQS Query, please see the <a href=\"making-interactive-experiences/artificial-intelligence/environment-query-system/EQS-quick-start\">EQS Quick Start Guide</a>.",
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

## Enabling EQS

Before you can start working with EQS, you will need to enable it from the **Project Settings** menu.

- Under the **Settings > Plugins** section, enable the **Environment Query Editor** option if necessary. ![Enable the Environment Query Editor option](https://dev.epicgames.com/community/api/documentation/image/2c0fe2e2-91df-4423-982b-05e371b93aa9)

## Previewing an EQS Query

You can preview the results of an EQS Query inside the Editor, where weighted/filtered results will be represented by debugging spheres.

![Debug Spheres](https://dev.epicgames.com/community/api/documentation/image/b6094552-eab3-4242-96b3-67c7903d7fd3)

In the image above, we debug an EQS Query that returns a location that provides a line of sight to the Player Character in the Level.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Please see <a data-document-id=\"3229057\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/ai-debugging-in-unreal-engine\">AI Debugging</a> or <a data-document-id=\"3229058\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-testing-pawn-in-unreal-engine\">EQS Testing Pawn</a> for more information.",
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
