# Unidad 14

Rango: archivos 1561 a 1680 de 3470

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getall.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getanimationattribute.md

# Get Animation Attribute

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetAnimationAttribute

> Application Version: 5.7

### Description

Get the value of an animation attribute from the skeletal mesh

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Animation Attribute |
| Type | [FRigDispatch\_GetAnimAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigDispatch_GetAnimAttribute) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The name of the animation attribute | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| BoneName | The name of the bone that stores the attribute, default to root bone if set to none | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Default | The default value used as a fallback if the animation attribute does not exist | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore),[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString),[FQuat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),User Defined Structs,[FPoseHistoryAnimationAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PoseSearch/FPoseHistoryAnimationAttribute) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value to get / set | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore),[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString),[FQuat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core),User Defined Structs,[FPoseHistoryAnimationAttribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PoseSearch/FPoseHistoryAnimationAttribute) |  |
| Found | Returns true if the animation attribute exists with the specific type | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getanimationchannel.md

# GetAnimationChannel

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetAnimationChannel

> Application Version: 5.7

### Description

Get Bool Channel is used to retrieve a control's animation channel value
Get Float Channel is used to retrieve a control's animation channel value
Get Int Channel is used to retrieve a control's animation channel value
Get Vector2D Channel is used to retrieve a control's animation channel value
Get Vector Channel is used to retrieve a control's animation channel value
Get Rotator Channel is used to retrieve a control's animation channel value
Get Transform Channel is used to retrieve a control's animation channel value

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetAnimationChannel,Get Bool Channel,Animation,Channel,Get Float Channel,Get Int Channel,Get Vector2D Channel,Get Vector Channel,Get Rotator Channel,Get Transform Channel |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to retrieve the value for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Channel | The name of the animation channel to retrieve the value for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| bInitial | If set to true the initial value will be returned | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The current value of the animation channel | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getanimationchannelfromitem.md

# GetAnimationChannelFromItem

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetAnimationChannelFromItem

> Application Version: 5.7

### Description

Get Bool Channel is used to retrieve a control's animation channel value
Get Float Channel is used to retrieve a control's animation channel value
Get Int Channel is used to retrieve a control's animation channel value
Get Vector2D Channel is used to retrieve a control's animation channel value
Get Vector Channel is used to retrieve a control's animation channel value
Get Rotator Channel is used to retrieve a control's animation channel value
Get Transform Channel is used to retrieve a control's animation channel value

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetAnimationChannelFromItem,Get Bool Channel,Animation,Channel,Get Float Channel,Get Int Channel,Get Vector2D Channel,Get Vector Channel,Get Rotator Channel,Get Transform Channel |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item representing the channel | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| bInitial | If set to true the initial value will be returned | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The current value of the animation channel | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getarrayconnection.md

# Get Array Connection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetArrayConnection

> Application Version: 5.7

### Description

Returns the resolved array of items of the connector.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Modules |
| Tags | Connector,GetResolved,Target,Resolve |
| Type | [FRigUnit\_ResolveArrayConnector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ResolveArrayConnector) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Connector | The key of the connector to resolve | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Connector,Name="") |
| SkipSocket | If the connector is resolved to a socket the node \* will return the socket's direct parent (skipping it). | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting array of items the connector is resolved to | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |
| bIsConnected | Returns true if the connector is resolved to a target. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getat.md

# GetAt

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetAt

> Application Version: 5.7

### Description

Returns the position on a ray

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Ray |
| Tags | Ratio,Percentage |
| Type | [FRigVMFunction\_MathRayGetAt](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathRayGetAt) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Ray | The ray to query | [Ray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Origin=(X=0.000000,Y=0.000000,Z=0.000000),Direction=(X=0.000000,Y=0.000000,Z=1.000000)) |
| Ratio | The ratio to query the ray at | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting position on the ray | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getbasiclivelinkdata.md

# Get Basic LiveLink Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetBasicLiveLinkData

> Application Version: 5.7

### Description

Evaluate current Live Link Basic float property data associated with supplied subject

### Information

|  |  |
| --- | --- |
| Plugin | [LiveLinkControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/LiveLinkControlRig) |
| Category | Live Link |
| Type | [FRigUnit\_LiveLinkEvaluateBasicValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/LiveLinkControlRig/FRigUnit_LiveLinkEvaluateBasicVa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SubjectName | The name of the subject to evaluate | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| PropertyName | The name of the property to evaluate | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The resulting value of the evaluated property | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getboxcenter.md

# Get Box Center

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetBoxCenter

> Application Version: 5.7

### Description

Returns the center of a bounding box

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Box |
| Tags | Middle,Origin,Bounds,BoundingBox,Bbox |
| Type | [FRigVMFunction\_MathBoxGetCenter](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoxGetCenter) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | The box to retrieve the center for | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Center | The center of the box | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getboxsize.md

# Get Box Size

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetBoxSize

> Application Version: 5.7

### Description

Returns the size of a bounding box

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Box |
| Tags | Middle,Origin,Bounds,BoundingBox,Bbox |
| Type | [FRigVMFunction\_MathBoxGetSize](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoxGetSize) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | The box to retrieve the size for | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Size | the overall size of the box | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Extent | the half size of the box | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getboxvolume.md

# Get Box Volume

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetBoxVolume

> Application Version: 5.7

### Description

Returns the volume of a given box

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Box |
| Tags | Bbox,BoundingBox |
| Type | [FRigVMFunction\_MathBoxGetVolume](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoxGetVolume) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | The box to retrieve the volume for | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Volume | The volume of the box | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getcandidates.md

# Get Candidates

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetCandidates

> Application Version: 5.7

### Description

Returns the connection candidates for one connector

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Modules |
| Tags | Connection,Resolve |
| Type | [FRigUnit\_GetCandidates](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetCandidates) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Connector | The connector being resolved | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |
| Candidates | The items being interacted on | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getchain.md

# Get Chain

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetChain

> Application Version: 5.7

### Description

Returns a chain between two items

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Chain,Siblings,Hierarchy |
| Type | [FRigUnit\_HierarchyGetChainItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyGetChainItemAr-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Start | The first element of the chain | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| End | The last element of the chain | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bIncludeStart | If True the list of results will include the first element | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bIncludeEnd | If True the list of results will include the last element | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bReverse | If True the list of results will be reversed | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Chain | The resulting array of elements on the chain | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getchildren.md

# Get Children

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetChildren

> Application Version: 5.7

### Description

Creates an item array based on the direct or recursive children
of a provided parent item. Returns an empty array for an invalid parent item.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Bone,Joint,Collection,Filter,Parent |
| Type | [FRigUnit\_CollectionChildrenArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CollectionChildrenArray) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Parent | The parent to search the children for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bIncludeParent | If True the parent will be included in the list of results | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bRecursive | If True children of children will be included | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bDefaultChildren | When true, it will return all children, regardless of whether the parent is active or not. When false, will return only the children which are influenced by this parent | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| TypeToSearch | The type of children to look for | [Rig Element Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigElementType) | All |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The resulting array of children | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getcomponent.md

# Get Component

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetComponent

> Application Version: 5.7

### Description

Gets the component

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Type | [FRigDispatch\_GetComponentContent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigDispatch_GetComponentContent) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Key | The key of the component | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Component | The actual component | [FRigPhysicsBodyComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsBodyComponent),[FRigPhysicsControlComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsControlComponent),[FRigPhysicsJointComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsJointComponent),[FRigPhysicsSolverComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsSolverComponent) |  |
| Success | Returns true if the operation was successful. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getconnection.md

# Get Connection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetConnection

> Application Version: 5.7

### Description

Returns the resolved item of the connector.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Modules |
| Tags | Connector,GetResolved,Target,Resolve |
| Type | [FRigUnit\_ResolveConnector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ResolveConnector) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Connector | The key of the connector to resolve | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Connector,Name="") |
| SkipSocket | If the connector is resolved to a socket the node \* will return the socket's direct parent (skipping it). | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting item the connector is resolved to | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |
| bIsConnected | Returns true if the connector is resolved to a target. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getcontrolbool.md

# Get Control Bool

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlBool

> Application Version: 5.7

### Description

GetControlBool is used to retrieve a single Bool from a hierarchy.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlBool |
| Type | [FRigUnit\_GetControlBool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetControlBool) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to retrieve the bool for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoolValue | The current bool of the given bone - or identity in case it wasn't found. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getcontrolcolor.md

# Get Control Color

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlColor

> Application Version: 5.7

### Description

GetControlColor is used to retrieve the color of control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlColor,GetGizmoColor |
| Type | [FRigUnit\_GetControlColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetControlColor) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to get the color for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Color | The color of the control | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getcontrolfloat.md

# Get Control Float

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlFloat

> Application Version: 5.7

### Description

GetControlFloat is used to retrieve a single Float from a hierarchy.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlFloat |
| Type | [FRigUnit\_GetControlFloat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetControlFloat) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to retrieve the Float for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatValue | The current value of the control. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Minimum | The minimum value of the control. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Maximum | The maximum value of the control. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getcontrolinteger.md

# Get Control Integer

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlInteger

> Application Version: 5.7

### Description

GetControlInteger is used to retrieve a single Integer from a hierarchy.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlInteger,GetControlEnum |
| Type | [FRigUnit\_GetControlInteger](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetControlInteger) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to retrieve the Integer for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IntegerValue | The current value of the control. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Minimum | The minimum value of the control. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Maximum | The maximum value of the control. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getcontroloffset.md

# Get Control Offset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlOffset

> Application Version: 5.7

### Description

GetControlOffset returns the offset transform of a given control.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlOffset,Initial,InitialTransform,GetInitialTransform,GetInitialControlTransform |
| Type | [FRigUnit\_GetControlOffset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetControlOffset) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the transform for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Space | Defines if the transform should be retrieved in local or global space | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OffsetTransform | The current transform of the given item - or identity in case it wasn't found. | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getcontrolrotator.md

# Get Control Rotator

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlRotator

> Application Version: 5.7

### Description

GetControlRotator is used to retrieve a single Rotator from a hierarchy.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlRotator |
| Type | [FRigUnit\_GetControlRotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetControlRotator) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to retrieve the Rotator for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Space | Defines if the Control's Rotator should be retrieved in local or global space. | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Rotator | The current value of the control. | [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Minimum | The minimum value of the control. | [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Maximum | The maximum value of the control. | [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getcontroltransform.md

# Get Control Transform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlTransform

> Application Version: 5.7

### Description

GetControlTransform is used to retrieve a single transform from a hierarchy.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlTransform |
| Type | [FRigUnit\_GetControlTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetControlTransform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to retrieve the transform for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Space | Defines if the Control's transform should be retrieved in local or global space. | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The current value of the control. | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Minimum | The minimum value of the control. | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Maximum | The maximum value of the control. | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getcontrolvector.md

# Get Control Vector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlVector

> Application Version: 5.7

### Description

GetControlVector is used to retrieve a single Vector from a hierarchy, can be used for Controls of type "Position" or "Scale".

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlVector, GetControlPosition, GetControlScale |
| Type | [FRigUnit\_GetControlVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetControlVector) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to retrieve the Vector for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Space | Defines if the Control's Vector should be retrieved in local or global space. | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Vector | The current value of the control. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Minimum | The minimum value of the control. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Maximum | The maximum value of the control. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getcontrolvector2d.md

# Get Control Vector2D

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlVector2D

> Application Version: 5.7

### Description

GetControlVector2D is used to retrieve a single Vector2D from a hierarchy.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlVector2D |
| Type | [FRigUnit\_GetControlVector2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetControlVector2D) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to retrieve the Vector2D for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Vector | The current value of the control. | [Vector 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Minimum | The minimum value of the control. | [Vector 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Maximum | The maximum value of the control. | [Vector 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getcontrolvisibility.md

# Get Control Visibility

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlVisibility

> Application Version: 5.7

### Description

GetControlVisibility is used to retrieve the visibility of a control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlVisibility,Visibility,Hide,Show,Hidden,Visible,SetGizmoVisibility |
| Type | [FRigUnit\_GetControlVisibility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetControlVisibility) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The name of the Control to set the visibility for. | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bVisible | The visibility of the control | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getcurvevalue.md

# Get Curve Value

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetCurveValue

> Application Version: 5.7

### Description

GetCurveValue is used to retrieve a single float from a Curve

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Curve |
| Tags | GetCurveValue,float |
| Type | [FRigUnit\_GetCurveValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetCurveValue) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Curve | The name of the Curve to retrieve the transform for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Valid | True if the retrieved curve value is valid | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Value | The current transform of the given Curve - or identity in case it wasn't found. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getdistancetobox.md

# Get Distance to Box

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetDistancetoBox

> Application Version: 5.7

### Description

Returns the distance to a given box

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Box |
| Tags | Bbox,Closest,BoundingBox |
| Type | [FRigVMFunction\_MathBoxGetDistance](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoxGetDistanc-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | The box to measure the distance to | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| Position | The position to measure the distance to | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Square | if true the distance will be returned square | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Valid | Returns true if the computed distance is valid | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Distance | The distance between the box and the position | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getdrivencontrols.md

# Get Driven Controls

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetDrivenControls

> Application Version: 5.7

### Description

GetControlDrivenList is used to retrieve the list of affected controls of an indirect control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlDrivenList,Interaction,Indirect |
| Type | [FRigUnit\_GetControlDrivenList](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetControlDrivenList) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to get the list for | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Driven | The list of affected controls | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getinteraction.md

# Get Interaction

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetInteraction

> Application Version: 5.7

### Description

Returns true if the Control Rig is being interacted

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Execution |
| Tags | IsInteracting,Gizmo,Manipulation,Interaction,Tracking |
| Type | [FRigUnit\_IsInteracting](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_IsInteracting) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bIsInteracting | True if there is currently an interaction happening | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bIsTranslating | True if the current interaction is a translation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bIsRotating | True if the current interaction is a rotation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bIsScaling | True if the current interaction is scaling | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Items | The items being interacted on | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getitemmodule.md

# Get Item Module

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetItemModule

> Application Version: 5.7

### Description

Returns the namespace of a given item. This may be an empty string if the item doesn't have a namespace.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Modules |
| Tags | NameSpace |
| Type | [FRigUnit\_GetItemModuleName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetItemModuleName) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The key of the item to return the module for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IsPartOfModule | True if the item is part of a module | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Module | The name of the module of the given item | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getitemsfromcollection.md

# Get Items from Collection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetItemsfromCollection

> Application Version: 5.7

### Description

Returns an array of items provided a collection

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Items|Collections |
| Tags | Collection,Array |
| Type | [FRigUnit\_CollectionGetItems](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CollectionGetItems) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | The input collection to retrieve the items from | [Rig Element Key Collection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKeyCollection) | (Keys=) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The resulting items in the collection | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getitemsinmodule.md

# Get Items In Module

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetItemsInModule

> Application Version: 5.7

### Description

Returns all items (based on a filter) in the current module.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Modules |
| Tags | NameSpace |
| Type | [FRigUnit\_GetItemsInModule](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetItemsInModule) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TypeToSearch | The types of elements to search for | [Rig Element Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigElementType) | All |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items within the module | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getlengthatparamofspline.md

# Get Length At Param Of Spline

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetLengthAtParamOfSpline

> Application Version: 5.7

### Description

Retrieves the length from a given Spline

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Type | [FRigUnit\_GetLengthAtParamControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_GetLengthAtParamControl-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The spline to evaluate | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| U | The U value along the spline to evaluate | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Length | The resulting length | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getlengthofspline.md

# Get Length Of Spline

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetLengthOfSpline

> Application Version: 5.7

### Description

Retrieves the length from a given Spline

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Type | [FRigUnit\_GetLengthControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_GetLengthControlRigSpli-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The spline to evaluate | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Length | The resulting length of the spline | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getlivelinkinputdevicedata.md

# Get Live Link Input Device Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetLiveLinkInputDeviceData

> Application Version: 5.7

### Description

A node to evaluate a live link input device value

### Information

|  |  |
| --- | --- |
| Plugin | [LiveLinkControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/LiveLinkControlRig) |
| Category | Live Link |
| Type | [FRigUnit\_LiveLinkEvaluateInputDeviceValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/LiveLinkControlRig/FRigUnit_LiveLinkEvaluateInputDe-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SubjectName | Name of the subject we would like to get Live Link device data. This should be the subject attached to the gamepad. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InputDeviceData | Gamepad device data for the current frame. | [Live Link Gamepad Input Device Frame Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/LiveLinkInterface/FLiveLinkGamepadInputDeviceFrame-) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getmetadata.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getmodulemetadata.md

# Get Module Metadata

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetModuleMetadata

> Application Version: 5.7

### Description

Returns some metadata on a given module

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Type | [FRigDispatch\_GetModuleMetadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigDispatch_GetModuleMetadata) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The name of the metadata | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |
| Default | The default value used as a fallback if the metadata does not exist | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value to get / set | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |
| Found | Returns true if the metadata exists with the specific type | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getmodulename.md

# Get Module Name

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetModuleName

> Application Version: 5.7

### Description

Returns the name of the current module instance.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Modules |
| Tags | NameSpace |
| Type | [FRigUnit\_GetModuleName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetModuleName) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Module | The name of the module | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getnumericsuffix.md

# Get Numeric Suffix

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetNumericSuffix

> Application Version: 5.7

### Description

Tests whether this name ends with a numeric suffix

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|Name |
| Tags | Suffix,Number,Integer |
| Type | [FRigVMFunction\_GetNameNumericSuffix](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_GetNameNumericSuf-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The input name to check for a numeric suffix | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Suffix | The resulting suffix (if it exists) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Success | True if the name ends with the given numeric suffix | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getparametervaluebyname.md

# Get Parameter Value By Name

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetParameterValueByName

> Application Version: 5.7

### Description

Get the parameter value with supplied subject frame

### Information

|  |  |
| --- | --- |
| Plugin | [LiveLinkControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/LiveLinkControlRig) |
| Category | Live Link |
| Type | [FRigUnit\_LiveLinkGetParameterValueByName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/LiveLinkControlRig/FRigUnit_LiveLinkGetParameterVal-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SubjectFrame | The frame to retrieve the parameter from | [Subject Frame Handle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/LiveLinkInterface/FSubjectFrameHandle) | () |
| ParameterName | The name of the parameter to retrieve | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The resulting value of the parameter | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getparent.md

# Get Parent

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetParent

> Application Version: 5.7

### Description

Returns the item's parent

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Child,Parent,Root,Up,Top |
| Type | [FRigUnit\_HierarchyGetParent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyGetParent) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The child to look up the parent for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bDefaultParent | When true, it will return the default parent, regardless of whether the parent influences the element or not | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Parent | The resulting parent of the input child | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getparentindices.md

# Get Parent Indices

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetParentIndices

> Application Version: 5.7

### Description

Returns an array of relative parent indices for each item. Several options here
a) If an item has multiple parents the major parent (based on the weights) will be returned.
b) If an item has a parent that's not part of the collection INDEX\_NONE will be returned.
c) If an item has a parent that's not part of the collection, but a grand parent is we'll use that index instead.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Items |
| Tags | Collection,Array |
| Type | [FRigUnit\_CollectionGetParentIndicesItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CollectionGetParentIndi-_1) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The input array of items to retrieve the parent indices for | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ParentIndices | The resulting array of parent indices | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getparents.md

# Get Parents

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetParents

> Application Version: 5.7

### Description

Returns the item's parents

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Chain,Parents,Hierarchy |
| Type | [FRigUnit\_HierarchyGetParentsItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyGetParentsItem-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The child to look up the parents for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bIncludeChild | If True the child will be included in the list of results | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bReverse | If True the list of results will be reversed | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bDefaultParent | When true, it will return the default parent, regardless of whether the parent influences the element or not | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Parents | The resulting array of parents | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getparentweights.md

# Get Parent Weights

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetParentWeights

> Application Version: 5.7

### Description

Returns the item's parents' weights

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Chain,Parents,Hierarchy |
| Type | [FRigUnit\_HierarchyGetParentWeightsArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyGetParentWeigh-_1) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The child to retrieve the weights for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Weights | The weight of each parent | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementWeight](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementWeight)> |  |
| Parents | The key for each parent | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getphysicscontroldata.md

# Get Physics Control Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPhysicsControlData

> Application Version: 5.7

### Description

Gets the control data for a physics control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchyGetControlData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchyGetControlData) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsControlComponentKey | The Physics Control component from which to retrieve data | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsControl") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ControlData | The current control data (strengths etc) | [Physics Control Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlData) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getphysicsjointdriveproperties.md

# Get Physics Joint Drive Properties

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPhysicsJointDriveProperties

> Application Version: 5.7

### Description

Gets the joint drive for a physics joint component

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchyGetJointDriveData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchyGetJointDriveD-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsJointComponentKey | The Physics Joint from which to retrieve data | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsJoint") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DriveData | The current Physics Joint Drive data | [Rig Physics Drive Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsDriveData) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getphysicsjointproperties.md

# Get Physics Joint Properties

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPhysicsJointProperties

> Application Version: 5.7

### Description

Gets the joint data for a physics joint component

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchyGetJointData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchyGetJointData) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsJointComponentKey | The Physics Joint from which to retrieve data | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsJoint") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| JointData | The current Physics Joint data (state of limits and drives) | [Rig Physics Joint Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsJointData) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getphysicssolverspacedata.md

# Get Physics Solver Space Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPhysicsSolverSpaceData

> Application Version: 5.7

### Description

Retrieves the simulation space data that were generated during the simulation step, so the values
returned will relate to the previous update if the solver has not yet been stepped.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Debug |
| Type | [FRigUnit\_GetPhysicsSolverSpaceData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_GetPhysicsSolverSpaceDa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | The solver to relate this new physics element to | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| LinearVelocity | The velocity of the simulation space (in world space) | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| AngularVelocity | The angular velocity of the simulation space (in world space) | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| LinearAcceleration | The linear acceleration of the simulation space (in world space) | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| AngularAcceleration | The angular acceleration of the simulation space (in world space) | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Gravity | The gravitational acceleration that will be applied (in simulation space) | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getposecache.md

# Get Pose Cache

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCache

> Application Version: 5.7

### Description

Returns the hierarchy's pose

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State |
| Type | [FRigUnit\_HierarchyGetPoseItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyGetPoseItemArr-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Initial | If True the pose will use the initial transforms | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ElementType | The element type to retrieve the pose for | [Rig Element Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigElementType) | All |
| ItemsToGet | An optional collection to filter against | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The resulting pose | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getposecachecurve.md

# Get Pose Cache Curve

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheCurve

> Application Version: 5.7

### Description

Returns the hierarchy's pose curve value

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State |
| Type | [FRigUnit\_PoseGetCurve](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PoseGetCurve) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The pose to retrieve the curve value from | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |
| Curve | The name of the curve to retrieve | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Valid | True if the curve value has been retrieved successfully | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| CurveValue | The resulting curve value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getposecachedelta.md

# Get Pose Cache Delta

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheDelta

> Application Version: 5.7

### Description

Compares two pose caches and compares their values.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State |
| Type | [FRigUnit\_PoseGetDelta](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PoseGetDelta) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PoseA | The first pose to compare | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |
| PoseB | The second pose to compare | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |
| PositionThreshold | The delta threshold for a translation / position difference. 0.0 disables position differences. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| RotationThreshold | The delta threshold for a rotation difference (in degrees). 0.0 disables rotation differences. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| ScaleThreshold | The delta threshold for a scale difference. 0.0 disables scale differences. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| CurveThreshold | The delta threshold for curve value difference. 0.0 disables curve differences. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| ElementType | The type of elements to compare | [Rig Element Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigElementType) | All |
| Space | Defines in which space transform deltas should be computed | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | LocalSpace |
| ItemsToCompare | An optional list of items to compare | [Rig Element Key Collection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKeyCollection) | (Keys=) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PosesAreEqual | True if the poses A and B are equal | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| ItemsWithDelta | An array of items with a difference in them between poses A and B | [Rig Element Key Collection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKeyCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getposecacheitems.md

# Get Pose Cache Items

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheItems

> Application Version: 5.7

### Description

Returns the items in the hierarchy pose

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State |
| Type | [FRigUnit\_PoseGetItemsItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PoseGetItemsItemArray) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The pose to retrieve the items from | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |
| ElementType | The type of items to retrieve | [Rig Element Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigElementType) | All |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The resulting items in the pose | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getposecachetransform.md

# Get Pose Cache Transform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheTransform

> Application Version: 5.7

### Description

Returns the hierarchy's pose transform

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State |
| Type | [FRigUnit\_PoseGetTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PoseGetTransform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The pose to retrieve the transform from | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |
| Item | The item to retrieve the transform for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |
| Space | Defines if the transform should be retrieved in local or global space | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Valid | True if the transform retrieved is valid | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Transform | The resulting transform | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| CurveValue | The value of the curve (in case the pose entry was a curve) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getposecachetransformarray.md

# Get Pose Cache Transform Array

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheTransformArray

> Application Version: 5.7

### Description

Returns an array of transforms from a given hierarchy pose

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State |
| Type | [FRigUnit\_PoseGetTransformArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PoseGetTransformArray) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The pose to retrieve the transform from | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |
| Space | Defines if the transform should be retrieved in local or global space | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Valid | True if the transforms has been retrieved successfully | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Transforms | The resulting array of transforms | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getrelativetransform.md

# Get Relative Transform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetRelativeTransform

> Application Version: 5.7

### Description

GetRelativeTransform is used to retrieve a single transform from a hierarchy in the space of another transform

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Transforms |
| Tags | Offset,Local |
| Type | [FRigUnit\_GetRelativeTransformForItem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetRelativeTransformFor-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The child item to retrieve the transform for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bChildInitial | Defines if the child's transform should be retrieved as current (false) or initial (true). Initial transforms for bones and other elements in the hierarchy represent the reference pose's value. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Parent | The parent item to use. The child transform will be retrieve in the space of the parent. | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bParentInitial | Defines if the parent's transform should be retrieved as current (false) or initial (true). Initial transforms for bones and other elements in the hierarchy represent the reference pose's value. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RelativeTransform | The transform of the given child item relative to the provided parent | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getshapesettings.md

# Get Shape Settings

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetShapeSettings

> Application Version: 5.7

### Description

Retrieves the shape settings of a control

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Construction,Create,New,Control |
| Type | [FRigUnit\_HierarchyGetShapeSettings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyGetShapeSettin-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to change | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Settings | The shape settings for the control | [Rig Unit Hierarchy Add Control Shape Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddControl_Sha-) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getshapetransform.md

# Get Shape Transform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetShapeTransform

> Application Version: 5.7

### Description

GetShapeTransform is used to retrieve single control's shape transform.
This is typically only used during the Construction Event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlShapeTransform,Gizmo,GizmoTransform,MeshTransform |
| Type | [FRigUnit\_GetShapeTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetShapeTransform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the transform for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The shape transform to set for the control | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getsiblings.md

# Get Siblings

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetSiblings

> Application Version: 5.7

### Description

Returns the item's siblings

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Chain,Siblings,Hierarchy |
| Type | [FRigUnit\_HierarchyGetSiblingsItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyGetSiblingsIte-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to find the siblings for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bIncludeItem | If True the input item will be included in the list of results | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bDefaultSiblings | When true, it will return all siblings, regardless of whether the parent is active or not. When false, will return only the siblings which are influenced by the same parent | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Siblings | The resulting array of siblings of the input item | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-gettags.md

# Get Tags

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetTags

> Application Version: 5.7

### Description

Returns the metadata tags on an item

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | MetadataExists,HasKey,Tagging,FindTag |
| Type | [FRigUnit\_GetMetadataTags](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetMetadataTags) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to check the metadata for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Tags | The name of the tag to check | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-gettransform.md

# Get Transform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetTransform

> Application Version: 5.7

### Description

GetTransform is used to retrieve a single transform from a hierarchy.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Transforms |
| Tags | GetBoneTransform,GetControlTransform,GetInitialTransform,GetSpaceTransform,GetTransform |
| Type | [FRigUnit\_GetTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetTransform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to retrieve the transform for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Space | Defines if the transform should be retrieved in local or global space | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |
| bInitial | Defines if the transform should be retrieved as current (false) or initial (true). Initial transforms for bones and other elements in the hierarchy represent the reference pose's value. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The current transform of the given item - or identity in case it wasn't found. | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-gettransformarray.md

# Get Transform Array

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetTransformArray

> Application Version: 5.7

### Description

GetTransformArray is used to retrieve an array of transforms from the hierarchy.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Transforms |
| Tags | GetBoneTransform,GetControlTransform,GetInitialTransform,GetSpaceTransform,GetTransform |
| Type | [FRigUnit\_GetTransformItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetTransformItemArray) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items to retrieve the transforms for | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Space | Defines if the transforms should be retrieved in local or global space | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |
| bInitial | Defines if the transforms should be retrieved as current (false) or initial (true). Initial transforms for bones and other elements in the hierarchy represent the reference pose's value. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transforms | The current transform of the given item - or identity in case it wasn't found. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-gettransformbyname.md

# Get Transform By Name

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetTransformByName

> Application Version: 5.7

### Description

Get the transform value with supplied subject frame

### Information

|  |  |
| --- | --- |
| Plugin | [LiveLinkControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/LiveLinkControlRig) |
| Category | Live Link |
| Type | [FRigUnit\_LiveLinkGetTransformByName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/LiveLinkControlRig/FRigUnit_LiveLinkGetTransformByN-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SubjectFrame | The frame to receive a transform from | [Subject Frame Handle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/LiveLinkInterface/FSubjectFrameHandle) | () |
| TransformName | The name of the transform to retrieve | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Space | The space to retrieve the transform in | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | LocalSpace |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The resulting transform | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-getuserdata.md

# Get User Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetUserData

> Application Version: 5.7

### Description

Retrieves a value from a namespaces user data

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Tags | AssetUserData,Metadata |
| Type | [FRigDispatch\_GetUserData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigDispatch_GetUserData) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NameSpace | The namespace to look up the argument within | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Path | The path to the argument within the namespace | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Default | The default value for the argument. This is returned if the argument could not be found. | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting value for the argument. This may be the default value if the argument could not be found. | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |
| Found | A boolean flag indicating if the argument could be found. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-greater.md

# Greater

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Greater

> Application Version: 5.7

### Description

Returns true if the value A is greater than B

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Greater,Larger,Bigger,> |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first value to compare | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| B | The second value to compare | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the value A is greater than B | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-greaterequal.md

# GreaterEqual

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GreaterEqual

> Application Version: 5.7

### Description

Returns true if the value A is greater than or equal to B

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | GreaterEqual,Greater Equal,Larger,Bigger,>= |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first value to compare | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| B | The second value to compare | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the value A is greater than or equal to B | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-halfpi.md

# HalfPi

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/HalfPi

> Application Version: 5.7

### Description

Returns PI \* 0.5

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | HalfPi,Half Pi |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value of the constant | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 1.570796 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-harmonics.md

# Harmonics

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Harmonics

> Application Version: 5.7

### Description

Drives an array of items through a harmonics spectrum

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Simulation |
| Tags | Sin,Wave |
| Type | [FRigUnit\_ItemHarmonics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ItemHarmonics) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Targets | The items to drive. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_Harmonics\_TargetItem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_Harmonics_TargetItem)> | () |
| WaveSpeed | The speed of the wave to use | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| WaveFrequency | The frequency of the wave to use | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.600000,Z=0.800000) |
| WaveAmplitude | The amplitude in degrees per axis | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=70.000000,Z=0.000000) |
| WaveOffset | The positional offset of the wave | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=1.000000,Z=2.000000) |
| WaveNoise | The amount of noise to apply to the wave | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| WaveEase | The easing function to apply to the wave | [Rig VMAnim Easing Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMAnimEasingType) | Linear |
| WaveMinimum | The minimum value for the wave | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| WaveMaximum | The maximum value for the wave | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| RotationOrder | The rotation order to use when encoding the rotation | [Euler Rotation Order](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/EEulerRotationOrder) | YZX |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-hasmetadata.md

# Has Metadata

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/HasMetadata

> Application Version: 5.7

### Description

Returns true if a given item in the hierarchy has a specific set of metadata

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | MetadataExists,HasKey,SupportsMetadata,FindMetadata |
| Type | [FRigUnit\_HasMetadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HasMetadata) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to check the metadata for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the metadata to check | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Type | The type of metadata to check for | [Rig Metadata Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetadataType) | Float |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Found | True if the item has the metadata | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-hasmultipletags.md

# Has Multiple Tags

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/HasMultipleTags

> Application Version: 5.7

### Description

Returns true if a given item in the hierarchy has all of the provided tags

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | MetadataExists,HasKey,Tagging,FindTag |
| Type | [FRigUnit\_HasMetadataTagArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HasMetadataTagArray) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to check the metadata for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Tags | The name of the tag to check | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)> | () |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Found | True if the item has the metadata | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-hastag.md

# Has Tag

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/HasTag

> Application Version: 5.7

### Description

Returns true if a given item in the hierarchy has a specific tag stored in the metadata

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | MetadataExists,HasKey,Tagging,FindTag |
| Type | [FRigUnit\_HasMetadataTag](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HasMetadataTag) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to check the metadata for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Tag | The name of the tag to check | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Found | True if the item has the metadata | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-if.md

# If

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/If

> Application Version: 5.7

### Description

Chooses between two values based on a condition

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Execution |
| Tags | Branch,Condition |
| Type | [FRigVMDispatch\_If](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_If) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Condition | The condition on which we'll decide between the True and False values | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| True | The value to use if the condition is True | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |
| False | The value to use if the condition is False | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting value - either True or False based on the condition | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-ikrig.md

# IK Rig

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IKRig

> Application Version: 5.7

### Description

Supply an IK Rig asset and provide goal transforms to run IK on the skeleton.

### Information

|  |  |
| --- | --- |
| Plugin | [IKRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/IKRig) |
| Category | Hierarchy |
| Tags | IK Rig, IK |
| Type | [FRigUnit\_IKRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/IKRig/FRigUnit_IKRig) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IKRigAsset | An IK Rig asset to be evaluated. | IKRig Definition | None |
| Goals | A list of Goals to solve. These must match what is in the IK Rig, any missing Goals will have their alphas set to zero. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FIKRigGoalInput](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/IKRig/FIKRigGoalInput)> | () |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-importcollisionfromphysicsasset.md

# Import Collision From Physics Asset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportCollisionFromPhysicsAsset

> Application Version: 5.7

### Description

Imports/creates bones from the physics asset and creates collision for them.
The bones will lose their hierarchy and be placed under the specified parent - ready to be moved around.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Construction,Create,New |
| Type | [FRigUnit\_HierarchyImportCollisionFromPhysicsAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchyImportCollisio-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | Note that setting the solver component, if known, has the benefit of avoiding the need to search for an automatic solver. | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |
| bUseAutomaticSolver | If true (and the physics solver is not explicitly set), then this component will be added to any physics solver that exists above it in the hierarchy, if that solver allows automatically adding physics components. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| PhysicsAsset | The physics asset to import collision from | Physics Asset | None |
| BonesToUse | If this is empty, then all bones with bodies in the physics asset will be created. Otherwise only bodies that relate to the specified bones will be created. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)> | () |
| NameSpace | Prefix to the bone names | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | Physics\_ |
| Owner | Parent/owner for all the new bones | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoneKeys | The element keys of the bones that were created to own the physics bodies | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |
| PhysicsBodyComponentKeys | The Physics Body component keys that were created | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigComponentKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-importskeleton.md

# Import Skeleton

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportSkeleton

> Application Version: 5.7

### Description

Imports all bones (and curves) from the currently assigned skeleton.
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Skeleton,Mesh,AddBone,AddCurve,Spawn |
| Type | [FRigUnit\_HierarchyImportFromSkeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyImportFromSkel-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NameSpace | The namespace to use when importing bones and curves | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| bIncludeCurves | If True the curves will be imported | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bIncludeMeshSockets | If true the mesh sockets will be imported | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bIncludeVirtualBones | If true virtual bones will be imported | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The resulting imported items | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-init.md

# Init

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Init

> Application Version: 5.7

### Description

Sets the size of the array, initializing all elements to the given value.
Modifies the input array.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayInit](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayInit) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Array | The array to initialize. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Num | The new size of the array. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| Element | The value that is set to all elements. | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-insert.md

# Insert

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Insert

> Application Version: 5.7

### Description

Inserts an element into an array at a given index.
Modifies the input array.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayInsert](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayInsert) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Array | The array to insert an element into. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Index | The index at which to insert the element. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| Element | The element to insert into the array. | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-instantiatefromphysicsasset.md

# Instantiate From Physics Asset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/InstantiateFromPhysicsAsset

> Application Version: 5.7

### Description

Creates multiple physics components based on the supplied physics asset.
Note that the resulting simulation bodies may not precisely match the physics asset.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Construction,Create,New |
| Type | [FRigUnit\_HierarchyInstantiateFromPhysicsAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchyInstantiateFro-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | Note that setting the solver component, if known, has the benefit of avoiding the need to search for an automatic solver. | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |
| bUseAutomaticSolver | If true (and the physics solver is not explicitly set), then this component will be added to any physics solver that exists above it in the hierarchy, if that solver allows automatically adding physics components. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| PhysicsAsset | The Physics Asset to instantiate from | Physics Asset | None |
| ConstraintProfileName | Name of the constraint profile to use. If empty (or invalid), the default profile will be used | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| BonesToUse | If this is empty, then all bodies in the physics asset that match a bone in the hierarchy will be created. Otherwise only bodies that relate to the specified bones will be created. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| bEnableJoints | Whether to enable the joints authored in the physics asset. Note that you can't have drives without joints. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bEnableDrives | Whether to enable the drives authored in the physics asset. Note that if you are creating parent space controls, you may not want the drives | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bAddSimSpaceControl | Whether to create a simulation-space control for each body that was created | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bAddParentSpaceControl | Whether to create a parent-space control for each body that was created. Note that if this is set to true, then it will be created for the root-most body in the physics asset too. This is often not needed, so make sure it isn't enabled if you don't want it to be. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| SimSpaceControlData | Data for the simulation space control | [Physics Control Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlData) | (bEnabled=True,LinearStrength=0.000000,LinearDampingRatio=1.000000,LinearExtraDamping=0.000000,MaxForce=0.000000,AngularStrength=0.000000,AngularDampingRatio=1.000000,AngularExtraDamping=0.000000,MaxTorque=0.000000,LinearTargetVelocityMultiplier=1.000000,AngularTargetVelocityMultiplier=1.000000,CustomControlPoint=(X=0.000000,Y=0.000000,Z=0.000000),bUseCustomControlPoint=False,bUseSkeletalAnimation=True,bDisableCollision=False,bOnlyControlChildObject=False) |
| ParentSpaceControlData | Data for the parent space control | [Physics Control Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlData) | (bEnabled=True,LinearStrength=0.000000,LinearDampingRatio=1.000000,LinearExtraDamping=0.000000,MaxForce=0.000000,AngularStrength=0.000000,AngularDampingRatio=1.000000,AngularExtraDamping=0.000000,MaxTorque=0.000000,LinearTargetVelocityMultiplier=1.000000,AngularTargetVelocityMultiplier=1.000000,CustomControlPoint=(X=0.000000,Y=0.000000,Z=0.000000),bUseCustomControlPoint=False,bUseSkeletalAnimation=True,bDisableCollision=False,bOnlyControlChildObject=False) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKeys | The Physics Body component keys that were created | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigComponentKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey)> |  |
| PhysicsJointComponentKeys | The Physics Joint component keys that were created | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigComponentKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey)> |  |
| SimSpaceControlComponentKeys | The simulation-space Physics Control component keys that were created | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigComponentKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey)> |  |
| ParentSpaceControlComponentKeys | The parent-space Physics Control component keys that were created | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigComponentKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-instantiatephysics.md

# Instantiate physics

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Instantiatephysics

> Application Version: 5.7

### Description

Instantiates all the objects in the physics world. Some properties can't be modified after this happens.
Note that it will happen automatically during the first simulation step if it hasn't been explicitly
requested. Explicit instantiation allows the timing to be controlled, as allocations etc may cause some
delays.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_InstantiatePhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_InstantiatePhysics) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | The solver that should be instantiated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-interaction.md

# Interaction

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Interaction

> Application Version: 5.7

### Description

Event for executing logic during an interaction

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Events |
| Tags | Manipulation,Event,During,Interacting |
| Type | [FRigUnit\_InteractionExecution](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_InteractionExecution) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | The execution result | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-interpolate.md

# Interpolate

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Interpolate

> Application Version: 5.7

### Description

Linearly interpolates between A and B using the ratio T
Performs a spherical interpolation of the quaternions A and B based on the blend value T.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Interpolate,Lerp,Mix,Blend,Slerp,SphericalInterpolate |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first color to interpolate from | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=0.000000,A=1.000000) |
| B | The second color to interpolate to | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=1.000000,A=1.000000) |
| T | The blend value for the interpolation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting interpolated color | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-intersection.md

# Intersection

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Intersection

> Application Version: 5.7

### Description

Creates a new array containing the intersection between the two input arrays.
Difference here means elements that are contained in both A and B.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayIntersection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayIntersection) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | The first array to compare the other array with. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |
| Other | The second array to compare the other array with. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting intersecting array. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-intersectplane.md

# Intersect Plane

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectPlane

> Application Version: 5.7

## Intersect Plane (FRigVMFunction\_MathRayIntersectPlane)

Returns the closest point intersection of a ray with a plane

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Ray |
| Tags | Closest,Ray,Cross |
| Type | [FRigVMFunction\_MathRayIntersectPlane](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathRayIntersectP-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Ray | The ray to intersect with the plane | [Ray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Origin=(X=0.000000,Y=0.000000,Z=0.000000),Direction=(X=0.000000,Y=0.000000,Z=1.000000)) |
| PlanePoint | The point on the plane to intersect the ray with | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| PlaneNormal | The normal of the plane to intersect the ray with | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting intersection position | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Distance | The distance of the ray origin to the plane | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Ratio | The ratio along the ray up to the intersection point | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

## Intersect Plane (FRigVMFunction\_MathIntersectPlane)

Intersects a plane with a vector given a start and direction

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Tags | Collide,Intersect,Raycast |
| Type | [FRigVMFunction\_MathIntersectPlane](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathIntersectPlan-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Start | The start of the ray to intersect with the plane | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Direction | The direction of the ray to intersect with the plane | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| PlanePoint | The point on the plane to intersect with | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| PlaneNormal | The normal of the plane to intersect with | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting position on the plane | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Distance | The distance along the ray to the intersection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-intersectray.md

# Intersect Ray

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectRay

> Application Version: 5.7

### Description

Returns the closest point intersection of a ray with another ray

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Ray |
| Tags | Closest,Ray,Cross |
| Type | [FRigVMFunction\_MathRayIntersectRay](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathRayIntersectR-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first ray to intersect | [Ray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Origin=(X=0.000000,Y=0.000000,Z=0.000000),Direction=(X=0.000000,Y=0.000000,Z=1.000000)) |
| B | The second ray to intersect | [Ray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Origin=(X=0.000000,Y=0.000000,Z=0.000000),Direction=(X=0.000000,Y=0.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting intersection position. This is either on the rays themselves or at the closest position between the two. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Distance | The distance between the two rays (or 0 if they touch) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| RatioA | The ratio on the first ray at the intersection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| RatioB | The ratio on the second ray at the intersection | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-inttoname.md

# Int to Name

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/InttoName

> Application Version: 5.7

### Description

Converts an integer to a string
Converts an integer to a name

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Int |
| Tags | Int to Name,Int to String |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Number | The number to convert | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| PaddedSize | For positive numbers you can pad the result to a required width \* so rather than '13' return '00013' for a padded size of 5. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting potentially padded string | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-inverse.md

# Inverse

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Inverse

> Application Version: 5.7

### Description

Returns the inverse value
Returns the negative value
Returns the inverted transform of the input

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Inverse |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Matrix](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (XPlane=(W=0.000000,X=1.000000,Y=0.000000,Z=0.000000),YPlane=(W=0.000000,X=0.000000,Y=1.000000,Z=0.000000),ZPlane=(W=0.000000,X=0.000000,Y=0.000000,Z=1.000000),WPlane=(W=1.000000,X=0.000000,Y=0.000000,Z=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Matrix](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-isasseteditoropen.md

# Is Asset Editor Open

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsAssetEditorOpen

> Application Version: 5.7

### Description

Returns true if a graph is run with its asset editor open. This is editor only - in shipping it always returns false.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Execution |
| Tags | Debug,Open,Inspect |
| Type | [FRigVMFunction\_IsHostBeingDebugged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_IsHostBeingDebugg-) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the graph is currently open in the asset editor | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-isboxvalid.md

# Is Box Valid

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsBoxValid

> Application Version: 5.7

### Description

Returns true if the box has any content / is valid

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Box |
| Tags | IsValid,HasVolume,ContainsPoints,Bounds,BoundingBox,Bbox |
| Type | [FRigVMFunction\_MathBoxIsValid](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoxIsValid) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | The box to check | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Valid | Returns true if the box has any content / is valid | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-isempty.md

# IsEmpty

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsEmpty

> Application Version: 5.7

### Description

Returns true if the array is empty

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | FRigVMDispatch\_ArrayIsEmpty |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | The array to check for emptiness. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IsEmpty | True if the array is empty. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-isincurrentmodule.md

# Is In Current Module

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsInCurrentModule

> Application Version: 5.7

### Description

Returns true if the given item has been created by this module.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Modules |
| Tags | NameSpace |
| Type | [FRigUnit\_IsItemInCurrentModule](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_IsItemInCurrentModule) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The key of the item to check the module for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the item is owned by this module. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-isinsidebox.md

# Is Inside Box

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsInsideBox

> Application Version: 5.7

### Description

Returns true if a point is inside a given box

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Box |
| Tags | Bbox,Contains,Encompasses,BoundingBox |
| Type | [FRigVMFunction\_MathBoxIsInside](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoxIsInside) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | The box to test | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| Position | The position to check for | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | Returns true if the given point is inside the given box | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-isnearlyequal.md

# IsNearlyEqual

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsNearlyEqual

> Application Version: 5.7

### Description

Returns true if the value A is almost equal to B
Returns true if value A is almost equal to B

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | IsNearlyEqual,Is Nearly Equal,AlmostEqual,== |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first value to compare | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| B | The second value to compare | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| Tolerance | The tolerance to apply for the comparison | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the value A is almost equal to B | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-isnearlyzero.md

# IsNearlyZero

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsNearlyZero

> Application Version: 5.7

### Description

Returns true if the value is nearly zero

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | IsNearlyZero,Is Nearly Zero,AlmostZero,0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value to check | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| Tolerance | The tolerance to apply for the comparison | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the value is nearly zero | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-isnone.md

# Is None

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsNone

> Application Version: 5.7

### Description

Returns true if this name is none

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|Name |
| Tags | Empty,Valid |
| Type | [FRigVMFunction\_IsNone](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_IsNone) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The input name to check | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the input name is None | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-isposecacheempty.md

# Is Pose Cache Empty

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsPoseCacheEmpty

> Application Version: 5.7

### Description

Returns true if the hierarchy pose is empty (has no items)

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State |
| Type | [FRigUnit\_PoseIsEmpty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PoseIsEmpty) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The pose to check | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IsEmpty | True if the pose is empty | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-isvalid.md

# Is Valid

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IsValid

> Application Version: 5.7

### Description

Returns true if this name is valid / is not none

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|Name |
| Tags | Empty,Valid |
| Type | [FRigVMFunction\_IsNameValid](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_IsNameValid) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input name to check | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the name is valid/ is not None | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-item.md

# Item

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Item

> Application Version: 5.7

### Description

The Item node is used to share a specific item across the graph

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Type | [FRigUnit\_Item](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_Item) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-itemexists.md

# Item Exists

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ItemExists

> Application Version: 5.7

### Description

Returns true or false if a given item exists

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Items |
| Type | [FRigUnit\_ItemExists](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ItemExists) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to look up | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Exists | True if the item exists | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-itemnamesearch.md

# Item Name Search

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ItemNameSearch

> Application Version: 5.7

### Description

Creates an item array based on a name search.
The name search is case sensitive.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Items |
| Tags | Bone,Joint,Collection,Filter |
| Type | [FRigUnit\_CollectionNameSearchArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CollectionNameSearchArr-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PartialName | The partial name to look for | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| TypeToSearch | The type of elements to look for | [Rig Element Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigElementType) | All |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The resulting array of elements matching the filters | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-itemreplace.md

# Item Replace

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ItemReplace

> Application Version: 5.7

### Description

Replaces the text within the name of the item

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Items |
| Tags | Replace,Name |
| Type | [FRigUnit\_ItemReplace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ItemReplace) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to perform the name replace within | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |
| Old | The old name to search for | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| New | The new name to replace the old name with | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting item after the replacement | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-itemtypeequals.md

# Item Type Equals

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ItemTypeEquals

> Application Version: 5.7

### Description

Returns true if the two items' types are equal

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Items |
| Type | [FRigUnit\_ItemTypeEquals](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ItemTypeEquals) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first item to compare | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |
| B | The second item to compare | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the types of items A and B are equal | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-itemtypenotequals.md

# Item Type Not Equals

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ItemTypeNotEquals

> Application Version: 5.7

### Description

Returns true if the two items's types are not equal

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Items |
| Type | [FRigUnit\_ItemTypeNotEquals](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ItemTypeNotEquals) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first item to compare | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |
| B | The second item to compare | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the types of items A and B are not equal | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-join.md

# Join

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Join

> Application Version: 5.7

### Description

Joins a string into multiple sections given a separator

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Tags | Combine |
| Type | [FRigVMFunction\_StringJoin](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringJoin) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Values | An array of input strings to join | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> | () |
| Separator | The separator to use when joining the parts | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting joined string | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-kalmanfilter.md

# KalmanFilter

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/KalmanFilter

> Application Version: 5.7

### Description

Averages a value over time.
This uses a Kalman Filter internally.
Averages a transform over time.
This uses a Kalman Filter internally.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Time |
| Tags | KalmanFilter,Average Over Time (Float),Average,Smooth,Average Over Time (Vector),Average Over Time (Transform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value to filter | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| BufferSize | The buffer size to use (the higher the more precise) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 16 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting averaged / filtered value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-lawofcosine.md

# LawOfCosine

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/LawOfCosine

> Application Version: 5.7

### Description

Computes the angles alpha, beta and gamma (in radians) between the three sides A, B and C

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | LawOfCosine,Law Of Cosine |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The length of the first edge of the triangle | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |
| B | The length of the second edge of the triangle | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |
| C | The length of the third edge of the triangle | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AlphaAngle | The angle between B and C | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |
| BetaAngle | The angle between A and C | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |
| GammaAngle | The angle between A and B | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |
| bValid | True if the results are valid | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-left.md

# Left

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Left

> Application Version: 5.7

### Description

Returns the left most characters of a string

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Tags | Start,Begin |
| Type | [FRigVMFunction\_StringLeft](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringLeft) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input string to retrieve the left most characters of | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Count | The number of characters to retrieve | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting left most characters of the input string | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-length.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-lengthsquared.md

# Length Squared

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/LengthSquared

> Application Version: 5.7

### Description

Returns the squared length of the vector

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Tags | Length,Size,Magnitude |
| Type | [FRigVMFunction\_MathVectorLengthSquared](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathVectorLengthS-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input vector to compute the squared length of | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting squared length of the vector | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-less.md

# Less

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Less

> Application Version: 5.7

### Description

Returns true if the value A is less than B

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Less,Smaller,< |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first value to compare | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| B | The second value to compare | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the value A is less than B | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-lessequal.md

# LessEqual

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/LessEqual

> Application Version: 5.7

### Description

Returns true if the value A is less than or equal to B

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | LessEqual,Less Equal,Smaller,<= |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first value to compare | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| B | The second value to compare | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the value A is less than or equal to B | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-linetracebyobjecttypes.md

# Line Trace By Object Types

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/LineTraceByObjectTypes

> Application Version: 5.7

### Description

Performs a line trace against the world and return the first blocking hit. The trace is filtered by object types only, the collision response settings are ignored.
You can create custom object types in Project Setting - Collision

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Collision |
| Tags | Line,Raytrace,Collision,Collide,Trace |
| Type | [FRigUnit\_LineTraceByObjectTypes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_LineTraceByObjectTypes) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Start | Start of the trace in rig / global space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| End | End of the trace in rig / global space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| ObjectTypes | The types of objects that this trace can hit | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TEnumAsByte](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EObjectTypeQuery](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/EObjectTypeQuery)>> | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bHit | Returns true if there was a hit | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HitLocation | Hit location in rig / global Space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HitNormal | Hit normal in rig / global Space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-linetracebytracechannel.md

# Line Trace By Trace Channel

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/LineTraceByTraceChannel

> Application Version: 5.7

### Description

Performs a line trace against the world and return the first blocking hit using a specific channel. Target objects can have different object types, but they need to have the same trace channel set to "block" in their collision response settings.
You can create custom trace channels in Project Setting - Collision.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Collision |
| Tags | Line,Raytrace,Collision,Collide,Trace |
| Type | [FRigUnit\_LineTraceByTraceChannel](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_LineTraceByTraceChannel) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Start | Start of the trace in rig / global space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| End | End of the trace in rig / global space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| TraceChannel | The 'channel' that this trace is in, used to determine which components to hit | [Trace Type Query](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/ETraceTypeQuery) | TraceTypeQuery1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bHit | Returns true if there was a hit | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HitLocation | Hit location in rig / global Space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HitNormal | Hit normal in rig / global Space | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-make.md

# Make

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Make

> Application Version: 5.7

### Description

Composes a struct out of its elements

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core |
| Tags | Compose,Composition,Create,Constant |
| Type | [FRigVMDispatch\_MakeStruct](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_MakeStruct) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Elements | The elements of the structure to make | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Struct | The created structure | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-makeabsolute.md

# Make Absolute

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeAbsolute

> Application Version: 5.7

### Description

Returns the absolute global rotation within a parent's rotation
Returns the absolute global transform within a parent's transform
Returns the absolute global vector within a parent's vector

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Make Absolute,Local,Global,Relative |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Local | The input local rotation to make absolute | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| Parent | The parent global rotation to make the local absolute to | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Global | The resulting global rotation | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-makearray.md

# Make Array

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeArray

> Application Version: 5.7

### Description

Creates a new array from its elements.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | Make,MakeArray,Constant,Reroute |
| Type | [FRigVMDispatch\_ArrayMake](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayMake) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Values | The elements of the array to create. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | The resulting array. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-makearticulationdrivedata.md

# Make Articulation Drive Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeArticulationDriveData

> Application Version: 5.7

### Description

Helper to simplify creation of drive data for a typical articulation (i.e. no linear drive, but
with an angular drive)

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Construction,Create,New,Body,Skeleton |
| Type | [FRigUnit\_MakeArticulationDriveData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_MakeArticulationDriveDa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bEnableAngularDrive | Whether to enable the angular drive | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AngularDriveMode | The type of drive. Note that SLERP drives don't work if any axis is locked | [Angular Drive Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/EAngularDriveMode__Type) | SLERP |
| AngularStrength | The strength used to drive angular motion | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| AngularDampingRatio | The amount of damping associated with the angular strength. A value of 1 Results in critically damped motion where the control drives as quickly as possible to the target without overshooting. Values > 1 result in more damped motion, and values below 1 result in faster, but more "wobbly" motion. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| AngularExtraDamping | The amount of additional angular damping. This is added to the damping that comes from AngularDampingRatio and can be useful when you want damping even when AngularStrength is zero. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SkeletalAnimationVelocityMultiplier | The amount of skeletal animation velocity to use in the targets | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DriveData | The drive data that can be set in a Physics Joint, reflecting the setup specified here. | [Rig Physics Drive Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsDriveData) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-makearticulationjointdata.md

# Make Articulation Joint Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeArticulationJointData

> Application Version: 5.7

### Description

Helper to simplify creation of joint data for a typical articulation (i.e. locked linear motion,
but with an angular limit)

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Construction,Create,New,Body,Skeleton |
| Type | [FRigUnit\_MakeArticulationJointData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_MakeArticulationJointDa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AngularLimit | The angular limit in Degrees (twist, swing1, swing2) -ve indicates the limit range is free | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=-1.000000,Y=-1.000000,Z=-1.000000) |
| SoftStrength | If limited, then this will be used to control the softness of the limit -ve indicates the limit is hard A value of 1 is reasonably soft | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=-1.000000,Y=-1.000000,Z=-1.000000) |
| SoftDampingRatio | If limited, then this will be used to control the damping ratio of the limit | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| JointData | Joint data that can be used in a Physics Joint, calculated according to the values set here, and configured to act as a "normal" articulation joint. | [Rig Physics Joint Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsJointData) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-makedrivedata.md

# Make Drive Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeDriveData

> Application Version: 5.7

### Description

Helper to simplify creation of drive data

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Construction,Create,New,Body,Skeleton |
| Type | [FRigUnit\_MakeDriveData](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_MakeDriveData) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bEnableLinearDrive | Whether to enable the linear drive (not normally used for character joints) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| LinearStrength | The strength used to drive linear motion | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| LinearDampingRatio | The amount of damping associated with the linear strength. A value of 1 Results in critically damped motion where the control drives as quickly as possible to the target without overshooting. Values > 1 result in more damped motion, and values below 1 result in faster, but more "wobbly" motion. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| LinearExtraDamping | The amount of additional linear damping. This is added to the damping that comes from LinearDampingRatio and can be useful when you want damping even when LinearStrength is zero. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bEnableAngularDrive | Whether to enable the angular drive | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AngularDriveMode | The type of drive. Note that SLERP drives don't work if any axis is locked | [Angular Drive Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/EAngularDriveMode__Type) | SLERP |
| AngularStrength | The strength used to drive angular motion | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| AngularDampingRatio | The amount of damping associated with the angular strength. A value of 1 Results in critically damped motion where the control drives as quickly as possible to the target without overshooting. Values > 1 result in more damped motion, and values below 1 result in faster, but more "wobbly" motion. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| AngularExtraDamping | The amount of additional angular damping. This is added to the damping that comes from AngularDampingRatio and can be useful when you want damping even when AngularStrength is zero. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SkeletalAnimationVelocityMultiplier | The amount of skeletal animation velocity to use in the targets | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DriveData | The drive data, representing the properties specified here, that can be set on a Physics Joint | [Rig Physics Drive Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsDriveData) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-makequat.md

# Make Quat

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeQuat

> Application Version: 5.7

### Description

Makes a quaternion from its components

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Quaternion |
| Tags | Make,Construct,Constant |
| Type | [FRigVMFunction\_MathQuaternionMake](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathQuaternionMak-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| X | The X of the quaternion | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Y | The Y of the quaternion | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Z | The Z of the quaternion | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| W | The W of the quaternion | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting composed quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-makerelative.md

# Make Relative

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeRelative

> Application Version: 5.7

### Description

Returns the relative local rotation within a parent's rotation
Returns the relative local transform within a parent's transform
Returns the relative local vector within a parent's vector

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Make Relative,Local,Global,Absolute |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Global | The global rotation quaternion to make relative | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| Parent | The parent global rotation to make the input relative to | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Local | The resulting relative rotation | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-maketransformarrayrelative.md

# Make Transform Array Relative

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeTransformArrayRelative

> Application Version: 5.7

### Description

Treats the provided transforms as a chain with global / local transforms, and
projects each transform into the target space. Optionally you can provide
a custom parent indices array, with which you can represent more than just chains.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Transform |
| Tags | Local,Global,Absolute,Array,Accumulate |
| Type | [FRigVMFunction\_MathTransformAccumulateArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathTransformAccu-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transforms | The input transform array to accumulate | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TargetSpace | Defines the space to project to | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |
| Root | Provides the parent transform for the root | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| ParentIndices | If this array is the same size as the transforms array the indices will be used to look up each transform's parent. They are expected to be in order. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |

