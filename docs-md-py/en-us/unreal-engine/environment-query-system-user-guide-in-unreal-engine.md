# Environment Query System User Guide

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-user-guide-in-unreal-engine

> Application Version: 5.7

This page covers the typical workflows for enabling, creating, and editing Environmental Query System (EQS) assets.

## Enabling EQS

Before you can start working with EQS, you will need to enable it from the **Project Settings** menu.

- Under the **Settings > Plugins** section, enable the **Environment Query Editor** option if necessary. ![Enable the **Environment Query Editor** option](https://dev.epicgames.com/community/api/documentation/image/b3930453-cb70-4378-bf19-e3835bbfc9e1)

## Creating an EQS Query

To create an EQS Asset:

1. Click the **+Add** button in the **Content Drawer**, then under **Artificial Intelligence**, select **Environment Query**. ![Click the +Add button in the Content Drawer, then under Artificial Intelligence, select Environment Query](https://dev.epicgames.com/community/api/documentation/image/e3d6f298-7291-4d93-9c95-8299e68acc33)
2. Enter in a name for your new EQS asset. ![Enter in a name for your new EQS asset](https://dev.epicgames.com/community/api/documentation/image/f405ca6a-c610-4c82-8890-7645aa2425be)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "In addition to Environment Query, you can create custom <a data-document-id=\"3229052\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/eqs-node-reference-generators-in-unreal-engine\">Generator</a> and <a data-document-id=\"3229053\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/eqs-node-reference-contexts-in-unreal-engine\">Context</a> Blueprint assets in the Content Drawer.",
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

## Editing an EQS Query

Inside the EQS asset, you can use a [Generator](https://dev.epicgames.com/documentation/en-us/unreal-engine/eqs-node-reference-generators-in-unreal-engine) to produce the locations or Actors that will be tested and weighted, provide a [Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/eqs-node-reference-contexts-in-unreal-engine) or frame of reference, and [Tests](https://dev.epicgames.com/documentation/en-us/unreal-engine/eqs-node-reference-tests-in-unreal-engine) to determine which item from the Generator is the best option. The following section will illustrate how to create each of these within the EQS asset.

To add a Generator:

- Right-click in the EQS Graph and select your desired Generator type. ![Right-click in the EQS Graph and select your desired Generator type](https://dev.epicgames.com/community/api/documentation/image/85b315b7-3fcc-48f1-93f5-5bdb9fbe7902) After adding a Generator, drag off the Root node and connect it to your Generator. ![Drag off the Root node and connect it to your Generator](https://dev.epicgames.com/community/api/documentation/image/7e45b128-3202-4c79-b952-c3c0dd4d0587)

To add a Test:

- Right-click on a Generator and select a Test to add. ![Right-click on a Generator and select a Test to add](https://dev.epicgames.com/community/api/documentation/image/7f045468-253c-4db6-b38b-ab5c8108ed19) After adding a Test, it will appear attached to the Generator. Select the Test to adjust properties in the **Details**panel. ![Select the Test to adjust properties in the Details panel](https://dev.epicgames.com/community/api/documentation/image/c257838d-9f31-4e9a-ba48-727d368dc10c)

To define a Context:

- In the **Details**panel for a Test, change the **EnvQueryContext** to your desired Context. ![Change the EnvQueryContext to your desired Context](https://dev.epicgames.com/community/api/documentation/image/58998bc0-274b-489c-98de-39c38341853f)

## Previewing an EQS Query

You can preview the results of an EQS Query inside the Editor, where weighted/filtered results will be represented by debugging spheres.

![You can preview the results of an EQS Query inside the Editor](https://dev.epicgames.com/community/api/documentation/image/9a3694b8-5fca-41e0-8743-6888987eb130)

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

## Using EQS with Behavior Trees

After creating EQS Query, you can run the query inside a [Behavior Tree](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-trees-in-unreal-engine) as part of a **Task.**

1. Inside a Behavior Tree, right-click and add the **Run EQS Query** Task node. ![Right-click and add the Run EQS Query Task node](https://dev.epicgames.com/community/api/documentation/image/6a2765cd-de3b-4e09-b51c-0bd2f5350b5d)
2. For **Run EQS** **Query**, assign the **Query Template** (desired EQS asset) to execute, and the **Blackboard Key** it should return. ![Assign the Query Template to execute and the Blackboard Key it should return](https://dev.epicgames.com/community/api/documentation/image/e6cd5a07-6d57-45fa-aed8-d906c13a0819) The Blackboard Key that is returned will be the highest weight result (Object or Vector). In the example above, we have an EQS Query that is used to locate the Player and provide that location back to a Blackboard Key called **MoveToLocation.**

## Using EQS with Native Code

While EQS Queries generally run within Behavior Trees, you can also use them directly from native code. The following example shows a hypothetical query that finds a safe place for a character or item to spawn within a specific zone:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// These names must match the variable names used in the query\n\tstatic const FName SafeZoneIndexName = FName(TEXT(&quot;SafeZoneIndex&quot;));\n\tstatic const FName SafeZoneRadiusName = FName(TEXT(&quot;SafeZoneRadius&quot;));\n\n\t// Run a query to find a safe spawn point based on the zone&#39;s index and a safety radius\n\tbool AMyActor::RunPlacementQuery(const UEnvQuery* PlacementQuery)\n\t{\n\t\tif (PlacementQuery)\n\t\t{\n\t\t\t// Set up a query request\n",
  "lines_of_code": 26,
  "id": 163121,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjMxMjEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxMzoyNSswMDowMCJ9--0ebfbd66c596f0764ba1e0bd94f70ecf3dff8df7b33c36f0f51f45f2bbd0a4be",
  "settings": {
    "is_hidden": false
  }
}
```
