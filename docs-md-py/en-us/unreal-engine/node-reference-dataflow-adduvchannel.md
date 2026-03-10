# AddUVChannel

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddUVChannel

> Application Version: 5.7

### Description

AddUVChannel (v1)

* Add a new UV channel to the collection
* note that there's a maximum of 8 channels that can be handled by a collection

Input(s) :
Collection [Intrinsic] - Target Collection

Output(s):
Collection [Passthrough] - Target Collection
UVChannel - Index of the added UV channel

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|UV |
| Type | [FAddUVChannelDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAddUVChannelDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DefaultValue | Value to initialize the UV with | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| UVChannel | Index of the added UV channel | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
