# Get Sphere Covering Sphere Count

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetSphereCoveringSphereCount

> Application Version: 5.7

### Description

Get Sphere Covering Sphere Count (v1)

Report the number of spheres in a sphere covering

Input(s) :
SphereCovering [Intrinsic] - The sphere covering to evaluate

Output(s):
NumSpheres - Number of spheres in the sphere covering

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | SphereCovering |
| Type | [FSphereCoveringCountSpheresNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSphereCoveringCountSpheresNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SphereCovering | The sphere covering to evaluate | [FDataflowSphereCovering](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowSphereCovering) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NumSpheres | Number of spheres in the sphere covering | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
