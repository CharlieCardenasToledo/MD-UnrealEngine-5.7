# MakeRotator

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRotator

> Application Version: 5.7

### Description

MakeRotator (v1)

Make a Rotator

Input(s) :
Pitch - Rotation around the right axis (around Y axis), Looking up and down (0=Straight Ahead, +Up, -Down)
Yaw - Rotation around the up axis (around Z axis), Turning around (0=Forward, +Right, -Left)
Roll - Rotation around the forward axis (around X axis), Tilting your head, (0=Straight, +Clockwise, -CCW)

Output(s):
Rotator - Rotator output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Transform |
| Type | [FMakeRotatorDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeRotatorDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pitch | Rotation around the right axis (around Y axis), Looking up and down (0=Straight Ahead, +Up, -Down) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Yaw | Rotation around the up axis (around Z axis), Turning around (0=Forward, +Right, -Left) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Roll | Rotation around the forward axis (around X axis), Tilting your head, (0=Straight, +Clockwise, -CCW) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Rotator | Rotator output | [FRotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
