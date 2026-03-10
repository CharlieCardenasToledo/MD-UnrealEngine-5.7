# Branch

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Branch

> Application Version: 5.7

### Description

Branch (v1)

Dataflow Branch Node

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | FlowControl |
| Type | [FDataflowBranchNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowBranchNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TrueValue |  | [FDataflowAnyType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) | () |
| FalseValue |  | [FDataflowAnyType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) | () |
| bCondition |  | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result |  | [FDataflowAnyType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) |  |
