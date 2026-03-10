# CollectionSelectionSetOperation

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionSetOperation

> Application Version: 5.7

### Description

CollectionSelectionSetOperation (v1)

Runs boolean operation on selection ( support all selection types )

Input(s) :
SelectionA [Intrinsic] - First Selection object
SelectionB [Intrinsic] - Second Selection object

Output(s):
Selection - Array of the selected bone indices after operation

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection |
| Type | [FCollectionSelectionSetOperationDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSelectionSetOperation-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Operation | Boolean operation | [ESetOperationEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ESetOperationEnum) | Dataflow\_SetOperation\_AND |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SelectionA | First Selection object | [FDataflowSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) | (Value=()) |
| SelectionB | Second Selection object | [FDataflowSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) | (Value=()) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Selection | Array of the selected bone indices after operation | [FDataflowSelectionTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) |  |
