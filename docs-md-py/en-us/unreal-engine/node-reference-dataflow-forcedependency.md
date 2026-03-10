# ForceDependency

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ForceDependency

> Application Version: 5.7

### Description

ForceDependency (v1)

Force an evaluation dependency between two values

Input(s) :
Value - Evaluating Value will force an evaluation of DependentValue
DependentValue - Evaluating Value will force an evaluation of DependentValue

Output(s):
Value [Passthrough] - Evaluating Value will force an evaluation of DependentValue

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | FlowControl |
| Type | [FDataflowForceDependencyNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowForceDependencyNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DependentValue | Evaluating Value will force an evaluation of DependentValue | [FDataflowAnyType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) | () |
| Value | Evaluating Value will force an evaluation of DependentValue | [FDataflowAnyType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | Evaluating Value will force an evaluation of DependentValue | [FDataflowAnyType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) |  |
