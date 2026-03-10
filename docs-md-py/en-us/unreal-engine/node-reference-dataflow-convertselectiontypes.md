# ConvertSelectionTypes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertSelectionTypes

> Application Version: 5.7

### Description

ConvertSelectionTypes (v1)

Convert Selection types

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection
In [Intrinsic] - Input value

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertSelectionTypesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertSelectionTypesDataflowNo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bAllElementsMustBeSelected | If true then for converting vertex/face selection to transform/geometry selection all vertex/face must be selected for selecting the associated transform/geometry or going from vertex to face selection all vertices must be selected to select the face | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| In | Input value | [FDataflowSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) | (Value=()) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Out | Output value | [FDataflowSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) |  |
