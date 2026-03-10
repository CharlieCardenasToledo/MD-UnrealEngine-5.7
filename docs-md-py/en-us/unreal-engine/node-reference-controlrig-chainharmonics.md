# Chain Harmonics

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ChainHarmonics

> Application Version: 5.7

### Description

Given a root will drive all items underneath in a chain based harmonics spectrum

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Simulation |
| Type | [FRigUnit\_ChainHarmonicsPerItem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ChainHarmonicsPerItem) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ChainRoot | The root of the chain to apply the harmonics to | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Speed | The speed of the harmonics effects | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| Reach | The reach settings Reach lets the chain "lean" towards the target trying to reach it. | [Rig Unit Chain Harmonics Reach](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ChainHarmonics_Reach) | (bEnabled=False,ReachTarget=(X=0.000000,Y=0.000000,Z=0.000000),ReachAxis=(X=1.000000,Y=0.000000,Z=0.000000),ReachMinimum=0.000000,ReachMaximum=0.000000,ReachEase=Linear) |
| Wave | The wave settings A wave is a rocking back and forth motion to be applied to all / some axes. | [Rig Unit Chain Harmonics Wave](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ChainHarmonics_Wave) | (bEnabled=True,WaveFrequency=(X=1.000000,Y=0.600000,Z=0.800000),WaveAmplitude=(X=0.000000,Y=1.000000,Z=0.000000),WaveOffset=(X=0.000000,Y=1.000000,Z=2.000000),WaveNoise=(X=0.000000,Y=0.000000,Z=0.000000),WaveMinimum=0.000000,WaveMaximum=1.000000,WaveEase=Linear) |
| WaveCurve | The curve to use when evaluating the wave | [Runtime Float Curve](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FRuntimeFloatCurve) | (EditorCurveData=(Keys=((),(Time=1.000000,Value=1.000000)),DefaultValue=340282346638528859811704183484516925440.000000,PreInfinityExtrap=RCCE\_Constant,PostInfinityExtrap=RCCE\_Constant),ExternalCurve=None) |
| Pendulum | The pendulum settings The harmonic pendulum uses a simple spring interpolation to allow to follow secondary motion. | [Rig Unit Chain Harmonics Pendulum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ChainHarmonics_Pendulum) | (bEnabled=False,PendulumStiffness=2.000000,PendulumGravity=(X=0.000000,Y=0.000000,Z=0.000000),PendulumBlend=0.750000,PendulumDrag=0.980000,PendulumMinimum=0.000000,PendulumMaximum=0.100000,PendulumEase=Linear,UnwindAxis=(X=0.000000,Y=1.000000,Z=0.000000),UnwindMinimum=0.200000,UnwindMaximum=0.050000) |
| bDrawDebug | if True the debug drawing will be enabled | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DrawWorldOffset | The world offset to be used when debug drawing | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
