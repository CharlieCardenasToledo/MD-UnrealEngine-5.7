# GetPhysicsSolvers

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetPhysicsSolvers

> Application Version: 5.7

### Description

GetPhysicsSolvers (v1)

Get physics solvers from context

Output(s):
PhysicsSolvers - Physics solvers coming from the context and filtered with the groups

### Information

|  |  |
| --- | --- |
| Module | [DataflowSimulation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation) |
| Category | Physics|Solver |
| Tags | DataflowSimulationTag |
| Type | [FGetPhysicsSolversDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FGetPhysicsSolversDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimulationGroups | Simulation groups to filter the output solvers properties | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolvers | Physics solvers coming from the context and filtered with the groups | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |
