# ConvertIndexToSelection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertIndexToSelection

> Application Version: 5.7

### Description

ConvertIndexToSelection (v1)

Convert Index to Selection

Input(s) :
Collection [Intrinsic] - Collection for the selection
In [Intrinsic] - Input value

Output(s):
Collection [Passthrough] - Collection for the selection
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertIndexToSelectionTypesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertIndexToSelectionTypesDat-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| In | Input value | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Out | Output value | [FDataflowSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) |  |
