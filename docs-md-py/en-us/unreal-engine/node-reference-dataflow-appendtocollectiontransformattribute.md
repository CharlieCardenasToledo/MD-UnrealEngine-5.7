# AppendToCollectionTransformAttribute

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendToCollectionTransformAttribute

> Application Version: 5.7

### Description

AppendToCollectionTransformAttribute (v1)

@todo(deprecate), move to GeometryCollection as AppendCollectionTransformDataflowNode

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FAppendToCollectionTransformAttributeDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FAppendToCollectionTransformAttr-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AttributeName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | ComponentTransform |
| GroupName |  | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | ComponentTransformGroup |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TransformIn |  | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
