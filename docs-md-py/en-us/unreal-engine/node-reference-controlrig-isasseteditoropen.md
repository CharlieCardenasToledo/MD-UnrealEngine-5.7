# Is Asset Editor Open

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsAssetEditorOpen

> Application Version: 5.7

### Description

Returns true if a graph is run with its asset editor open. This is editor only - in shipping it always returns false.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Execution |
| Tags | Debug,Open,Inspect |
| Type | [FRigVMFunction\_IsHostBeingDebugged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_IsHostBeingDebugg-) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the graph is currently open in the asset editor | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
