# FilterSimulationProxies

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSimulationProxies

> Application Version: 5.7

### Description

FilterSimulationProxies (v1)

Filter simulation proxies from context

Input(s) :
SimulationProxies - Simulation proxies coming from the context and filtered with the groups

Output(s):
FilteredProxies - Simulation proxies coming from the context and filtered with the groups

### Information

|  |  |
| --- | --- |
| Module | [DataflowSimulation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation) |
| Category | Physics|Proxy |
| Tags | DataflowSimulationTag |
| Type | [FFilterSimulationProxiesDataflowNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FFilterSimulationProxiesDataflow-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimulationGroups | Simulation groups to filter the output solvers properties | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimulationProxies | Simulation proxies coming from the context and filtered with the groups | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FilteredProxies | Simulation proxies coming from the context and filtered with the groups | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |
