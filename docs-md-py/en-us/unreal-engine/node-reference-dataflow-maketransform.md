# MakeTransform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeTransform

> Application Version: 5.7

### Description

MakeTransform (v1)

Make an FTransform
Note: Originaly this version was depricated and replaced with FMakeTransformDataflowNode\_v2 but when AnyRotationType was
introduced with the ConvertAnyRotation node FMakeTransformDataflowNode\_v2 became obsolete and this version became the current version again

Input(s) :
InTranslation - Translation
InRotation - Rotation as Euler
InScale - Scale

Output(s):
OutTransform - Result transform

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Transform |
| Type | [FMakeTransformDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeTransformDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InTranslation | Translation | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| InRotation | Rotation as Euler | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| InScale | Scale | [FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutTransform | Result transform | [FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
