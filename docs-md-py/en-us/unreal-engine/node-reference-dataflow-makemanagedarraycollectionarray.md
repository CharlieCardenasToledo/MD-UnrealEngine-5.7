# MakeManagedArrayCollectionArray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeManagedArrayCollectionArray

> Application Version: 5.7

### Description

MakeManagedArrayCollectionArray (v1)

Append an element to an array of ManagedArrayCollections.

Input(s) :
Array [Intrinsic] - Array to append to. If no input connection, a new array will be created
Element - The element to append.

Output(s):
Array [Passthrough] - Array to append to. If no input connection, a new array will be created

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Array |
| Tags | Make Managed Array Collection |
| Type | [FDataflowMakeManagedArrayCollectionArrayNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowMakeManagedArrayCollect-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | Array to append to. If no input connection, a new array will be created | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection)> |  |
| Element | The element to append. | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | Array to append to. If no input connection, a new array will be created | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection)> |  |
