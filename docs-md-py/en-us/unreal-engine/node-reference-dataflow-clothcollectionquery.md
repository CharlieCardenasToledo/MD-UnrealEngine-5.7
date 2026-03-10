# ClothCollectionQuery

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothCollectionQuery

> Application Version: 5.7

### Description

ClothCollectionQuery (v1)

Query a Managed Array Collection about its Cloth Collection properties.

Input(s) :
Collection - Input/output collection (Output is always a passthrough)

Output(s):
Collection [Passthrough] - Input/output collection (Output is always a passthrough)
bIsClothCollection - Is this collection a valid cloth collection
bHasClothSimMesh - Does this collection have a cloth sim mesh
bHasClothRenderMesh - Does this collection have a cloth render mesh
bHasClothProxyDeformer - Does this collection have proxy deformer data
bBooleanPropertyValue - Result of querying BooleanPropertyName. Default value if property doesn't exist matches node value.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Collection Query |
| Type | [FChaosClothAssetCollectionQueryNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetCollectionQueryN-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BooleanPropertyName | Name of boolean property to query | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | PropertyName |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection (Output is always a passthrough) | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection (Output is always a passthrough) | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| bIsClothCollection | Is this collection a valid cloth collection | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bHasClothSimMesh | Does this collection have a cloth sim mesh | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bHasClothRenderMesh | Does this collection have a cloth render mesh | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bHasClothProxyDeformer | Does this collection have proxy deformer data | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bBooleanPropertyValue | Result of querying BooleanPropertyName. Default value if property doesn't exist matches node value. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
