# Transform from SRT

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformfromSRT

> Application Version: 5.7

### Description

Composes a Transform (and Euler Transform) from its components.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Transform |
| Tags | EulerTransform,Scale,Rotation,Orientation,Translation,Location |
| Type | [FRigVMFunction\_MathTransformFromSRT](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathTransformFrom-_2) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Location | The location for the desired transform | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Rotation | The euler angles in degrees for the desired transform | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| RotationOrder | The rotation order to interpret the euler angles by | [Euler Rotation Order](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/EEulerRotationOrder) | XYZ |
| Scale | The scale for the desired transform | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The result as a transform | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| EulerTransform | The result as a euler transform | [Euler Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FEulerTransform) |  |
