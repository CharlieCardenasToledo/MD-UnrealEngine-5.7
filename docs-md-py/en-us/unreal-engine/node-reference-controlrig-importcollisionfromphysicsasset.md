# Import Collision From Physics Asset

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportCollisionFromPhysicsAsset

> Application Version: 5.7

### Description

Imports/creates bones from the physics asset and creates collision for them.
The bones will lose their hierarchy and be placed under the specified parent - ready to be moved around.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Construction,Create,New |
| Type | [FRigUnit\_HierarchyImportCollisionFromPhysicsAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchyImportCollisio-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | Note that setting the solver component, if known, has the benefit of avoiding the need to search for an automatic solver. | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |
| bUseAutomaticSolver | If true (and the physics solver is not explicitly set), then this component will be added to any physics solver that exists above it in the hierarchy, if that solver allows automatically adding physics components. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| PhysicsAsset | The physics asset to import collision from | Physics Asset | None |
| BonesToUse | If this is empty, then all bones with bodies in the physics asset will be created. Otherwise only bodies that relate to the specified bones will be created. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)> | () |
| NameSpace | Prefix to the bone names | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | Physics\_ |
| Owner | Parent/owner for all the new bones | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoneKeys | The element keys of the bones that were created to own the physics bodies | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |
| PhysicsBodyComponentKeys | The Physics Body component keys that were created | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigComponentKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey)> |  |
