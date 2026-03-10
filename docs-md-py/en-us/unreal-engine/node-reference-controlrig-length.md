# Length

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Length

> Application Version: 5.7

## Length (FRigVMFunction\_MathVectorLength)

Returns the length of the vector

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Tags | Size,Magnitude |
| Type | [FRigVMFunction\_MathVectorLength](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathVectorLength) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input vector to compute the length for | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting length of the vector | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

## Length (FRigVMFunction\_StringLength)

Returns the length of a string

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Type | [FRigVMFunction\_StringLength](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringLength) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input string to retrieve the length for | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Length | The resulting length of the input string | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
