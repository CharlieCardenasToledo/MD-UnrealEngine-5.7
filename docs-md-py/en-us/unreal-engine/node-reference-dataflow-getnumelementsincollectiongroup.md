# GetNumElementsInCollectionGroup

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetNumElementsInCollectionGroup

> Application Version: 5.7

### Description

GetNumElementsInCollectionGroup (v1)

Returns number of elements in a group in a Collection

Input(s) :
Collection [Intrinsic] - Collection for the custom attribute

Output(s):
NumElements - Number of elements for the attribute

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FGetNumElementsInCollectionGroupDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetNumElementsInCollectionGroup-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GroupName | Standard group names | [EStandardGroupNameEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EStandardGroupNameEnum) | Dataflow\_EStandardGroupNameEnum\_Transform |
| CustomGroupName | User specified group name | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the custom attribute | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NumElements | Number of elements for the attribute | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
