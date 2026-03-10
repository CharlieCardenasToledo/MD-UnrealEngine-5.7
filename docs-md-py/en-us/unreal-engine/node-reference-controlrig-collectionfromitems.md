# Collection from Items

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CollectionfromItems

> Application Version: 5.7

### Description

Returns a collection provided a specific array of items.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Items|Collections |
| Tags | Collection,Array |
| Type | [FRigUnit\_CollectionItems](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CollectionItems) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The input array of items | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | ((Type=Bone)) |
| bAllowDuplicates | If True the collection may contain duplicates | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | The resulting collection | [Rig Element Key Collection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKeyCollection) |  |
