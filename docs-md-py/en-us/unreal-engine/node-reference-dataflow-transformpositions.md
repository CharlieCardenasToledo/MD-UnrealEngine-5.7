# TransformPositions

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformPositions

> Application Version: 5.7

### Description

TransformPositions (v1)

Chaos Cloth Asset Transform Positions Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Transform Positions |
| Type | [FChaosClothAssetTransformPositionsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetTransformPositio-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bTransform2DSimPositions | Enable Transforming 2D Sim Mesh Positions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Sim2DScale | 2D Sim Transform scale. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000) |
| Sim2DRotation | 2D Sim Transform rotation angle in degrees. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Sim2DTranslation | 2D Sim Transform translation. | [FVector2f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000) |
| Sim2DPattern | Sim Pattern to transform. All patterns will be used when set to -1. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |
| bTransform3DSimPositions | Enable Transforming 3D Sim Mesh Positions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Sim3DScale | 3D Sim Transform scale. | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| Sim3DRotation | 3D Sim Transform rotation angle in degrees (Euler Angles) | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Sim3DTranslation | 3D Sim Transform translation. | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| bTransformRenderPositions | Enable Transforming Render Positions | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| RenderScale | Render Transform scale. | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| RenderRotation | Render Transform rotation angle in degrees (Euler Angles) | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| RenderTranslation | Render Transform translation. | [FVector3f](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| RenderPattern | Render Pattern to transform. All patterns will be used when set to -1. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
