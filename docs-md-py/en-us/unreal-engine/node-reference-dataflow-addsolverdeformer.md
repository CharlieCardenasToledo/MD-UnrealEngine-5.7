# AddSolverDeformer

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddSolverDeformer

> Application Version: 5.7

### Description

AddSolverDeformer (v1)

Add a graph deformer to the groom simulation

Input(s) :
PhysicsSolvers - Physics solvers to advance in time
SimulationTime - Delta time to use to advance the solver

Output(s):
PhysicsSolvers [Passthrough] - Physics solvers to advance in time

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsSolver](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsSolver) |
| Category | Physics|Solver |
| Tags | DataflowSimulationTag |
| Type | [FAddSolverDeformerDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/HairStrandsSolver/FAddSolverDeformerDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MeshDeformer | Graph deformer solver the component is using | [TObjectPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UOptimusDeformer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OptimusCore/UOptimusDeformer)> | None |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimulationTime | Delta time to use to advance the solver | [FDataflowSimulationTime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationTime) | () |
| PhysicsSolvers | Physics solvers to advance in time | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolvers | Physics solvers to advance in time | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |
