# Mass Debugger Overview

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mass-debugger-overview

> Application Version: 5.7

## Overview

The **Mass Debugger** tool has been significantly improved with many new features including: real-time inspection of entity fragment data, entity-specific fragment access breakpoints, **Gameplay Debugger** integration, and improved processor inspection.

## Using the Mass Debugger

To launch the Mass Debugger select **Tools > Debug > Mass Debugger** from the editor. Note: If you have launched previous versions of the Mass Debugger you may need to reset the layout to see the new tabs (**Window > Reset Layout** in the Mass Debugger window).

### UI Workflow

To view Processor data access overlaps:

1. Open the Mass Debugger.
2. Use the **Environment Picker** to select the Mass runtime environment you wish to inspect.
3. Open the **Processors Tab** (Window > Processors).
4. Find the Processor you want to inspect in the list.
5. Click the **Show Fragment Access** button on processor entry.
6. Click a fragment from the **Queries** list on the expanded processor entry.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The color of the processors will change based on the access of each processor. \n\nGreen indicates read (const) access and red indicates write (mutable) access.",
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

![Image of the screen to view Processor data access overlaps.](https://dev.epicgames.com/community/api/documentation/image/e3ebe57b-c5cd-41af-a0ce-f2454cc0cf8b)

To inspect fragment data on an entity from the Mass Debugger with an active environment selected:

1. Open the **Entities Tab** (**Window > Entities**, or use any of the contextual **Show Entities** buttons throughout the debugger UI).
2. Click the **Select Fragments** dropdown and check the fragments you want to inspect. Note: the list of fragments is contextual to composition of listed entities. Note: Only member variables of the selected fragment structs marked as UPROPERTY will be displayed. No other editor visibility metadata is required.

To set a fragment write breakpoint for a specific fragment on a specific entity:

1. Show the fragment data for the desired entity in the **Entities Tab**.
2. Click the **Set Write Breakpoint** button.
3. Note: the breakpoint will trigger in the EntityIterator code for the MassExecutionContext::EntitiyIterator. Only code using that iterator or wrappers for that iterator will trigger breakpoints this way. The triggering code will usually be two or three levels up the callstack.
4. To clear the breakpoint from the IDE and resume execution, use the watch feature in your IDE and set the bDisableThisBreakpoint variable to “true” or “1”.

![Image of the screen for the Select Fragments tab with fragment details for each fragment.](https://dev.epicgames.com/community/api/documentation/image/d4c1fcf2-d409-4542-a452-53a71d94a0e7)

To set a fragment write breakpoint for a given fragment to trigger for whichever entity is selected:

1. Open the **Fragments** tab.
2. Find the desired fragment.
3. Click the **Break on writes for the selected entity** button.
4. Use the **Entities** tab or the **Gameplay Debugger Tool** (“EnableGDT” console command) to select an entity.

![Image of the Fragments tab and how to select a specific entity with a circle toggle.](https://dev.epicgames.com/community/api/documentation/image/4b32a5a6-4db3-480c-b5fd-b66e1243dd51)

## Limitations

- Breakpoints functionality has only been tested in Visual Studio 2022 and might not be supported in other IDEs
- Breakpoints only trigger for code that uses MassExecutionContext::CreateEntityIterator for entity iteration
- Fragment inspection requires UPROPERTY RTTI and thus will only show member variables with UPROPERTY markup
