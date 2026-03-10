# MakeBox

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeBox

> Application Version: 5.7

### Description

MakeBox (v1)

Make a box

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Box |
| Type | [FMakeBoxDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeBoxDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DataType |  | [EMakeBoxDataTypeEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EMakeBoxDataTypeEnum) | Dataflow\_MakeBox\_DataType\_MinMax |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Min |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Max |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=10.000000,Y=10.000000,Z=10.000000) |
| Center |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Size |  | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=10.000000,Y=10.000000,Z=10.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box |  | [FBox](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
