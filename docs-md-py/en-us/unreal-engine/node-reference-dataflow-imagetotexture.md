# ImageToTexture

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageToTexture

> Application Version: 5.7

### Description

ImageToTexture (v1)

Create a transient texture asset from an image

### Information

|  |  |
| --- | --- |
| Module | [DataflowEngine](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine) |
| Category | Image |
| Tags | Image Texture |
| Type | [FDataflowImageToTextureNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowImageToTextureNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image |  | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |
| TextureName |  | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TransientTexture |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UTexture2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UTexture2D)> |  |
