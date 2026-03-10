# TextureToImage

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TextureToImage

> Application Version: 5.7

### Description

TextureToImage (v1)
Experimental

Import a texture asset as an image. Texture must have CPU availability.

### Information

|  |  |
| --- | --- |
| Module | [DataflowEngine](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine) |
| Category | Image |
| Tags | Texture Image |
| Type | [FDataflowTextureToImageNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowTextureToImageNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TextureAsset |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UTexture2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UTexture2D)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image |  | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |
