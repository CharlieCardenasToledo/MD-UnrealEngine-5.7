# Shape Exists

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ShapeExists

> Application Version: 5.7

### Description

Checks whether or not a shape is available in the rig's shape libraries

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Tags | Shape,Gizmo,Library,Exists,Contains |
| Type | [FRigUnit\_ShapeExists](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ShapeExists) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ShapeName | The name of the shape to search for | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the shape name exists in any of the shape libraries | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
