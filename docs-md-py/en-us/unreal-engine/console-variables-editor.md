# Console Variables Editor

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/console-variables-editor

> Application Version: 5.7

The **Console Variables Editor** is a panel that displays information about all the console variables set in the project, and provides a central location to view and modify all the variables. You can create presets to use the same console variables and values across multiple projects. The Console Variables Editor also supports controlling variables across multiple computers in a [Multi-User](https://dev.epicgames.com/documentation/en-us/unreal-engine/multi-user-editing-in-unreal-engine) session.

![Console Variables Editor user interface](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ebdfa8ee-5cf5-4194-a8c3-9327ef0f2f56/console-variables-editor.png)

The Console Variables Editor plugin also adds Blueprint API for accessing and controlling console variable presets created in the Console Variables Editor. Refer to the [Blueprint API Reference](https://docs.unrealengine.com/5.0/BlueprintAPI/ConsoleVariablesEditor) for more details.

To use the Console Variables Editor, enable the **Console Variables Editor** plugin in your project. Refer to [Working with Plugins](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine) for steps on enabling plugins in a project.

![Console Variables Editor plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/339e3127-0b08-4d31-98d4-96497c3d5a6d/console-variables-editor-plugin.png)

In the main menu, choose **Window > Console Variables** to open the Console Variables Editor. You can dock this panel anywhere in Unreal Editor.

![Open Console Variables Editor from the main menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eb529ff9-a087-4fb9-b7e0-108fbd35418e/open-console-variables.png)

## Console Variables List

The list contains all currently tracked console variables and executed commands. When you first open the Console Variables Editor, a blank preset is loaded with no console variables added. If **Add All Changed Console Variables to Current Preset** is set to **True** in the plugin settings, then you may see variables in the list already since console variables are often set through Project Settings.

To add console variables and commands to the list, click **(+) Add Console Variable** and search for a command or variable in the input box. As you enter text, a list appears below the text field showing matched console variable names, but console commands, such as `stat unit`, may not appear in the suggested list.

If the console variable you enter is valid, it then appears in the list. If you enter a console variable or command with a valid value, the command is executed with that value and the console variable appears in the list with its new value.

![Clicks add console variable button and enters the console command ](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b6f9a175-75d4-4150-9403-ad2470c639fc/enter-console-command.gif)

When you add a variable to the list, the current value is saved as the **preset value**. Each individual variable can be reset to its startup value or have its changes temporarily reverted by unchecking the row's checkbox.

![Checks and unchecks row to show how the value changes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/933edb8d-dbee-4c28-9dc6-68a8bfe5f79a/uncheck-check-row.gif)

You can remove a console variable from the list by hovering over the right side of its row and clicking **Remove**. When you remove the console variable from the list, its value is reset to the value it had when the plugin was loaded.

![Remove console variable button appears on hover in the row](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a53b191c-84c0-40fb-8d24-68a25b6a1f5a/remove-console-variable.png)
