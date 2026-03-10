# ApplyProxyDeformer

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyProxyDeformer

> Application Version: 5.7

### Description

ApplyProxyDeformer (v1)

Update the Render Mesh by applying any existing proxy deformer data.
This node can be used to deform the render mesh after the sim mesh has changed after the proxy deformer data was calculated.
It has no effect if there is no existing proxy deformer data, or if the sim or render mesh have not deformed since that data was calculated.

Input(s) :
Collection - Input/output collection

Output(s):
Collection [Passthrough] - Input/output collection

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Apply Proxy Deformer |
| Type | [FChaosClothAssetApplyProxyDeformerNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetApplyProxyDeform-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bIgnoreSkinningBlendWeights | Ignore Skinning Blend Weights (apply proxy deformer to all points) | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
