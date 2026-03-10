# Full Body IK

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FullBodyIK

> Application Version: 5.7

### Description

Based on a Position Based solver at core, this node can solve multi chains within a root using multi effectors

### Information

|  |  |
| --- | --- |
| Module | [PBIK](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PBIK) |
| Category | Hierarchy |
| Tags | FBIK, Position Based, PBIK, IK, Full Body, Multi, Effector, N-Chain, FB, HIK, HumanIK |
| Type | [FRigUnit\_PBIK](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PBIK/FRigUnit_PBIK) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Root | This is usually the top-most skinned bone; often the "Pelvis" or "Hips", but can be set to any bone. Bones above the root will be ignored by the solver. Bones that are located *between* the Root and the effectors will be included in the solve. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Effectors | An array of effectors. These specify target transforms for different parts of the skeleton. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FPBIKEffector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PBIK/FPBIKEffector)> | () |
| BoneSettings | Per-bone settings to control the resulting pose. Includes limits and preferred angles. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FPBIKBoneSetting](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PBIK/FPBIKBoneSetting)> | () |
| ExcludedBones | These bones will be excluded from the solver. They will not bend and will not contribute to the constraint set. Use the ExcludedBones array instead of setting Rotation Stiffness to very high values or Rotation Limits with zero range. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)> | () |
| Settings | Global solver settings. | [PBIKSolver Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/PBIK/FPBIKSolverSettings) | (Iterations=20,SubIterations=0,MassMultiplier=1.000000,bAllowStretch=False,RootBehavior=PrePull,PrePullRootSettings=(RotationAlpha=0.000000,RotationAlphaX=1.000000,RotationAlphaY=1.000000,RotationAlphaZ=1.000000,PositionAlpha=1.000000,PositionAlphaX=1.000000,PositionAlphaY=1.000000,PositionAlphaZ=1.000000),GlobalPullChainAlpha=1.000000,MaxAngle=30.000000,OverRelaxation=1.300000) |
