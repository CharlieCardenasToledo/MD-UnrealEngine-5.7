# Get Metadata

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetMetadata

> Application Version: 5.7

### Description

Gets some metadata for the provided item

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Type | [FRigDispatch\_GetMetadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigDispatch_GetMetadata) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item storing the metadata | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the metadata | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |
| Default | The default value used as a fallback if the metadata does not exist | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value to get / set | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |
| Found | Returns true if the metadata exists with the specific type | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
