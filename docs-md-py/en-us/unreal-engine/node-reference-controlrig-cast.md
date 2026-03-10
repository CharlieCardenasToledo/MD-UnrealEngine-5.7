# Cast

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast

> Application Version: 5.7

## Cast ()

Turns the given bool into a float value
Turns the given bool into an integer value
Makes a color from a single float
Makes a color from a single double
Returns the double cast to an int (this uses floor)
Returns the double cast to a float
Returns the float cast to an int (this uses floor)
Returns the float cast to a double
Returns the int cast to a float
Returns the int cast to a double
Makes a transform from a matrix
Makes a matrix from a transform
Makes a quaternion from a rotator
Retrieves the rotator
Makes a quaternion based transform from a euler based transform
Retrieves a euler based transform from a quaternion based transform
Makes a vector from a single float
Makes a vector from a single double
Casts the provided item key to its name

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Tags | Cast,To Float,To Integer,From Float,Make,Construct,From Double,To Int,To Double,To Transform,From Transform,From Rotator,To Rotator,To Euler Transform,To Name,Engine Test Rig VM Custom Type from Int,Engine Test Rig VM Custom Type to Int |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The bool value to convert | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Matrix](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Euler Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FEulerTransform)   [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)   FEngineTest\_CustomType | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting float number (0 or 1) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor)   [Matrix](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Euler Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FEulerTransform)   FEngineTest\_CustomType |  |

## Cast (FRigVMDispatch\_CastEnumToInt)

Casts from enum to int

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Enum |
| Tags | As |
| Type | [FRigVMDispatch\_CastEnumToInt](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_CastEnumToInt) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The enum value to cast to an integer | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting integer value | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

## Cast (FRigVMDispatch\_CastIntToEnum)

Casts from int to enum

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Enum |
| Tags | As |
| Type | [FRigVMDispatch\_CastIntToEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_CastIntToEnum) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The integer value to cast to an enum value | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting enum value | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

## Cast (FRigVMDispatch\_CastObject)

Casts between object types

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Object |
| Tags | As |
| Type | [FRigVMDispatch\_CastObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_CastObject) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The object to cast to a new type | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting cast object. This may be potentially nullptr as well if the cast was not successful. | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |
