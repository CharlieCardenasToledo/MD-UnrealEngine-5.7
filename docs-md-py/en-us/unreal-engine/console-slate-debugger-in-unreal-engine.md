# Console Slate Debugger

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/console-slate-debugger-in-unreal-engine

> Application Version: 5.7

While developing the user-interface (UI) for applications, UI developers sometimes need to debug Slate, which is where the **Console Slate Debugger** can help. Console Slate Debugger hooks into the available systems in [FSlateDebugging](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/Debugging/FSlateDebugging?application_version=5.5) to print internal Slate data. Additionally, as the UI focus changes (or attempts to change), developers will need to know what system is handling those focus updates.

![Console Slate Debugger](https://dev.epicgames.com/community/api/documentation/image/3243aa16-9259-4c3c-bf40-106a2c40d849)

_Console Slate Debugger_

Extensions for Console Slate Debugger include the following:

- GlobalInvalidation, which helps to identify the widgets responsible for a costly frame.
- A paint option that displays widgets that were painted in a given frame.
- An additional routing option to see how the system chooses a widget as the event handler.
- Additional filter and event console commands.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "This page's screenshots are taken from the Lyra Sample Game project. To test SlateDebugger commands in Lyra, use the command <code>Slate.EnableGlobalInvalidation 1</code> to enable <a data-document-id=\"3232598\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/invalidation-in-slate-and-umg-for-unreal-engine\">Global Invalidation</a>, as it is not active by default.",
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

## SlateDebugger

While running the project in PIE mode, press the tilde (~) key to open the PIE Console, and type `SlateDebugger`.

[Video: V_8ffb6v](https://dev.epicgames.com/community/api/cms/videos/V_8ffb6v/embed.html)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "SlateDebugger logs are typically written to a <code>[ProjectName].txt</code> log file under <code>[ProjectName]/Saved/Logs</code>.",
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

### Event Commands

Slate Debugger offers a lot of different commands to pinpoint specific information like enabling or disabling specific logs and filtering events. If more information is needed CaptureStack can also provide the call stack of the triggered event.

| SlateDebugger.Event | Command Description |
| --- | --- |
| **Start** | Alias for `SlateDebugger.Event.Start` that starts the Slate Console Debugger. |
| **Stop** | Alias for `SlateDebugger.Event.Stop` that stops the Slate Console Debugger. |
| **SetInputFilter** | Enables or disables specific input filters. |
| **SetFocusFilter** | Enables or disables specific focus filters. |
| **LogWarning** | Logs warning events. |
| **LogInputEvent** | Logs input events. |
| **LogFocusEvent** | Logs focus events. |
| **LogExecuteNavigationEvent** | Logs execute navigation events. |
| **LogCaptureStateChangeEvent** | Logs cursor state change events. |
| **LogCursorChangeEvent** | Logs cursosr change events. |
| **LogAttemptNavigationEvent** | Logs attempt navigation events. |
| **InputRoutingModeEnabled** | If enabled, outputs the route taken by an input event. |
| **EnableAllInputFilters** | Enables all input filters. |
| **DisableAllInputFilters** | Disables all input filters. |
| **EnableAllFocusFilters** | Enables all focus filters. |
| **DisableAllFocusFilters** | Disables all focus filters. |
| **CaptureStack** | If enabled, captures the stack when there are events. |

### Invalidate Commands

These commands allow you to use the Invalidate command to show on-screen widgets that are invalidated. Each invalidated widget will be highlighted in different colors based on the type of invalidation.

![SlateDebugger.Invalidate displays the state of each widget during the invalidation process.](https://dev.epicgames.com/community/api/documentation/image/246dc72f-eabe-4194-ab81-86aac289b3be)

_SlateDebugger.Invalidate displays the state of each widget during the invalidation process._

| SlateDebugger.Invalidate | Command Description |
| --- | --- |
| **Enable** | Starts the Invalidation Widget debug tool and display when widgets invalidate or stop the Invalidation Widget debug tool, depending on the current status. |
| **Start** | Starts the Invalidation Widget debug tool and displays when widgets invalidate. |
| **Stop** | Stops the Invalidation Widget debug tool. |
| **SetInvalidateRootReasonFilter** | Enables the Invalidate Widget Reason Filters. |
| **SetInvalidateWidgetReasonFilter** | Enable the Invalidate Root Reason filters. |
| **ToggleLegend** | Displays the color legend. |
| **ToggleLogInvalidateWidget** | Logs the invalidated widget to the console. |
| **ToggleWidgetNameList** | Displays the name of the invalidated widget. |

### Paint Commands

This command is used to highlight widgets that are painted in each frame. This can be useful to identify widgets that are painted even if they did not change. Note that volatile widgets are painted every frame.

![SlateDebugger.Paint displays which widgets are re-drawing on the screen.](https://dev.epicgames.com/community/api/documentation/image/36d32b46-a4cf-4b12-8c05-1de812b24b4a)

_SlateDebugger.Paint displays which widgets are re-drawing on the screen._

| SlateDebugger.Paint | Command Description |
| --- | --- |
| **Enable** | Starts the Paint Widget debug tool and display when widgets paint or stop the Paint Widget debug tool, depending on the current status. |
| **Start** | Starts the Paint Widget debug tool and displays when widgets paint. |
| **Stop** | Stops the Paint Widget debug tool. |
| **LogOnce** | Logs the widgets that paint once during the last update |
| **LogWarningIfWidgetIsPaintedMoreThanOnce** | Logs a warning if a widget paints more than once in the same frame. |
| **MaxNumberOfWidgetDisplayedInList** | Displays the maximum number of widgets that will display when `DisplayWidgetNameList` is active. |
| **ToggleWidgetNameList** | Displays painted widget names. |

### Update Commands

This command is used to highlight widgets that are updated more often than needed. Since Widget Update can be overridden or executed in Blueprint, it is a common source of poor performance if the widget code was not designed correctly.

![SlateDebugger.Update displays which widgets are updating with color coded information. This image is set to filter for only Repaint events, which use yellow.](https://dev.epicgames.com/community/api/documentation/image/f06298e5-5646-4fac-abc9-b177f9ebc0ac)

_SlateDebugger.Update displays which widgets are updating with color coded information. This image is set to filter for only Repaint events, which use yellow._

| SlateDebugger.Update | Command Description |
| --- | --- |
| **Enable** | Starts the Update Widget debug tool and displays when widgets update, or stops the Update Widget debug tool, depending on the current status. |
| **Start** | Starts the Update Widget debug tool and display when widgets update. |
| **Stop** | Stops the Update Widget debug tool. |
| **SetInvalidationRootIdFilter** | Only display widgets that are part of an invalidation root. |
| **SetWidgetUpdateFlagsFilter** | Logs a warning if a widget paints more than once in the same frame. |
| **ToggleLegend** | Displays the color legend. |
| **ToggleUpdateFromPaint** | Displays widgets that do not have an update flag but which are still updated as a side effect of another widget. |
| **ToggleWidgetNameList** | Displays the names of Update Widgets. |
