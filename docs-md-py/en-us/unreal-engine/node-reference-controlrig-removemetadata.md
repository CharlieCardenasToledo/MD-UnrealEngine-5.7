# Remove Metadata

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RemoveMetadata

> Application Version: 5.7

### Description

Removes an existing metadata filed from an item

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | DeleteMetadata |
| Type | [FRigUnit\_RemoveMetadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_RemoveMetadata) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to remove the metadata from | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the metadata to remove | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Removed | True if the metadata has been removed | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
