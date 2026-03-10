# GetArrayElement

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetArrayElement

> Application Version: 5.7

### Description

GetArrayElement (v1)

Get an element from an array

Input(s) :
Array [Intrinsic] - Array to get the element from
Index - Index to get the element at

Output(s):
Array [Passthrough] - Array to get the element from
Element - Element from the array at the specified index

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Array |
| Tags | Index At |
| Type | [FDataflowGetArrayElementNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowGetArrayElementNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | Array to get the element from | [FDataflowArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowArrayTypes) | () |
| Index | Index to get the element at | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | Array to get the element from | [FDataflowArrayTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowArrayTypes) |  |
| Element | Element from the array at the specified index | [FDataflowAllTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAllTypes) |  |
