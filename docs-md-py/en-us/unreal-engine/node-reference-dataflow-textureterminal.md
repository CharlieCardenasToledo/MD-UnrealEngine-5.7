# TextureTerminal

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TextureTerminal

> Application Version: 5.7

### Description

TextureTerminal (v1)

* terminal node to a save a dependent 2D texture

### Information

|  |  |
| --- | --- |
| Module | [DataflowEngine](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine) |
| Category | Terminal |
| Type | [FDataflowTextureTerminalNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowTextureTerminalNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image |  | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |
| TextureAsset |  | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UTexture2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/UTexture2D)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image |  | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |
