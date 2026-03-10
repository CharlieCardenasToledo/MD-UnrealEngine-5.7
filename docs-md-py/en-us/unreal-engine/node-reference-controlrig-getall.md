# Get All

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetAll

> Application Version: 5.7

### Description

Creates an item array for all elements given the filter.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Bone,Joint,Collection,Filter,Parent |
| Type | [FRigUnit\_CollectionGetAll](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CollectionGetAll) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TypeToSearch | The type of elements to look for | [Rig Element Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigElementType) | All |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The resulting array of elements | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |
