# Unidad 13

Rango: archivos 1441 a 1560 de 3470

---

## Fuente: .\docs-md-py\en-us\unreal-engine\niagara-settings-in-the-unreal-engine-project-settings.md

# Niagara

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-settings-in-the-unreal-engine-project-settings

> Application Version: 5.7

## Niagara

### Niagara

| **Setting** | **Description** |
| --- | --- |
| **Additional Parameter Types** | If enabled, you can save a struct of parameters into the project. You can then reuse your struct in different Niagara scripts.  Create a struct Asset through the **Content Browser**: right-click in an empty area, then select **Blueprints > Structure**. |
| **Additional Payload Types** | If enabled, you can save a payload struct in your project. A payload is also a struct of parameters, but with the additional ability to perform read and write events on it. |
| **Additional Parameter Enums** | Save an enum into your project for reuse in different Niagara scripts. |
| **Show Convertible Inputs in Stack** | If enabled, the "link input" menu will also show variables of different types, as long as there is a conversion script for them. |
| **Systems Support Large World Coordinates** | If enabled, active effects rebase the simulation positions to not lose precision.  If you don't need this setting, disable it to skip unnecessary rebasing calculations. |
| **Enforce strict type checks in the graph** | If enabled, types like positions and vectors can't be assigned to each other without an explicit conversion step.  If disabled, type checks are loosened and some types can be implicitly converted into each other.  Don't disable this when working with large world coordinates. |
| **Default Effect Type** | Default effect type to use for effects that don't define their own.  Can be `null`. |
| **Position Pin Type Color** | Position pin type color.  The other pin colors are defined in the general editor settings. |

### Viewport

| **Setting** | **Description** |
| --- | --- |
| **System Viewport in Orbit Mode** | Sets the default navigation behavior for the system preview viewport. |

### Scalability

| **Setting** | **Description** |
| --- | --- |
| **Quality Levels** | The quality levels Niagara uses. |

### Renderer

| **Setting** | **Description** |
| --- | --- |
| **Component Renderer Warnings Per Class** | Info texts that the component renderer displays based on the selected component class. |
| **Default Render Target Format** | The default render target format used by all Niagara Render Target Data Interfaces unless overridden.  You can choose from the following options:   * **RTF R8:** R channel, 8 bit per channel fixed point, range [0, 1]. * **RTF RG8:** RG channels, 8 bit per channel fixed point, range [0, 1]. * **RTF RGBA8:** RGBA channels, 8 bit per channel fixed point, range [0, 1]. * **RTF RGBA8 SRGB:** RGBA channels, 8 bit per channel fixed point, range [0, 1]. RGB is encoded with sRGB gamma curve. Alpha is always stored as linear. * **RTF R16f:** R channel, 16 bit per channel floating point, range [-65504, 65504]. * **RTF RG16f:** RG channels, 16 bit per channel floating point, range [-65504, 65504]. * **RTF RGBA16f:** RGBA channels, 16 bit per channel floating point, range [-65504, 65504]. * **RTF R32f:** R channel, 32 bit per channel floating point, range [-3.402823 x 10^38, 3.402823 x 10^38]. * **RTF RG32f:** RG channels, 32 bit per channel floating point, range [-3.402823 x 10^38, 3.402823 x 10^38]. * **RTF RGBA32f:** RGBA channels, 32 bit per channel floating point, range [-3.402823 x 10^38, 3.402823 x 10^38]. * **RTF RGB10A2:** RGBA channels, 10 bit per channel fixed point and 2 bit(s) of alpha. |
| **Default Grid Format** | The default buffer format used by all Niagara Grid Data Interfaces unless overridden.  You can choose from the following options:   * **Float:** 32-bit per channel floating point, range [-3.402823 x 10^38, 3.402823 x 10^38] * **Half Float:** 16-bit per channel floating point, range [-65504, 65504] * **Unsigned Normalized Byte:** 8-bit per channel fixed point, range [0, 1]. |
| **Default Renderer Motion Vector Setting** | The default setting for motion vectors in Niagara renderers.  You can choose from the following options:   * **Precise:** Motion vectors are generated precisely (ideal for motion blur and temporal anti-aliasing). Requires relevant emitters to store more data per particle, and may affect vertex processing performance. * **Approximate:** Approximates the motion vectors from current velocity. Saves memory and performance, but can result in lower quality motion blur and/or anti-aliasing. |
| **Default Pixel Coverage Mode** | The default setting for pixel coverage mode when automatic is set on the Niagara Renderer.  You can choose from the following options:   * **Enabled:** When the renderer is set to automatic mode, pixel coverage is enabled. * **Disabled:** When the renderer is set to automatic mode, pixel coverage is disabled. |

### Skeletal Mesh Data Interface (DI)

| **Setting** | **Description** |
| --- | --- |
| **Gpu Max Bone Influences** | Controls the maximum number of influences that the Skeletal Mesh Data Interface can use on the GPU.  Changing this setting requires restarting the Editor.  You can choose from the following options:   * **Allow Max 4:** Allow up to 4 bones to be sampled. * **Allow max 8:** Allow up to 8 bones to be sampled. * **Unlimited:** Allow an unlimited amount of bones to be sampled. |
| **Gpu Uniform Sampling Format** | Controls the format used for uniform sampling on the GPU.  Changing this setting requires restarting the Editor.  You can choose from the following options:   * **Full:** 64 bits per entry. Allow for the full int32 range of triangles (2 billion). * **Limited 24.8:** 32 bits per entry. Allow for ~16.7 million triangles and 8 bits of probability precision. * **Limited 23.9:** 32 bits per entry. Allow for ~8.4 million triangles and 8 bits of probability precision. |
| **Adjacency Triangle Index Format** | Controls the format used for specifying triangle indexes in adjacency buffers.  Changing this setting requires restarting the Editor.  You can choose from the following options:   * **Full:** 32 bits per entry. Allow for the full int32 range of triangles (2 billion). * **Half:** 16 bits per entry. Allow for half (int16) range of triangles (64k). |

### Static Mesh DI

| **Setting** | **Description** |
| --- | --- |
| **Allow Distance Fields (Experimental)** | When enabled, the Static Mesh data interface is allowed to sample from the distance field data (if present) on the GPU.  Enabling this feature will move all systems that contain Static Mesh samples into the `PostRenderOpaque` tick group regardless of the features used.  Changing this setting requires restarting the Editor. |

### Async GPU Trace DI

| **Setting** | **Description** |
| --- | --- |
| **Trace Provider Priorities (Experimental)** | Defines how traces tagged as Project Default will be interpreted when using the `AsyncGpuTrace` data interface.  The system will go through (starting at element 0) to find the first available provider. |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\niagara-systems-as-a-service.md

# Systems as a Service

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-systems-as-a-service

> Application Version: 5.7

## Overview

Before 5.4 the APIs provided for spawning Niagara systems mostly supported a one-to-one relationship between system instances and gameplay events/external triggers. The Niagara systems had little in the way of allowing external code to pass in information on when to spawn particles and how to initialize them outside of activation and moving the component. This presents a problem if many instances of the same system need to be spawned in a short period of time, as the activation cost, and instance counts can cause major performance issues. Conceptually Systems as a Service (SaaS) takes a many-to-one approach between external triggers and system instances. That is to say that one system instance can handle spawning particles from multiple triggers without needing to be reactivated, avoiding the costs associated with activation and ticking multiple instances.

User parameters, and the Array Data Interfaces made it possible for advanced users to “inject” particles into an existing system, but there were limitations to this workflow, and it required lots of manual data management when building the arrays. Additionally there’s a trade off between the size of a SaaS System Instance, and instance culling that the array-based approach has to manage manually. As an extreme example, if all particle effects in a project were in the same system, in most cases the particles offscreen would greatly outnumber those onscreen, but their simulations would still be run, since the system itself would always be active.

To address the issue more generally, and make the setup easier, we developed Niagara Data Channels, which serve as a generic way for passing data between Niagara systems and gameplay. The main focus has been supporting the SaaS use case, but there are other use cases for Data Channels that we won’t cover here. We created a specific type of Data Channel, the Islands Data Channel, that handles subdividing a level, and spawning instances of a system into those “islands” for data that’s written within its bounds. The Data Channel asset defines the data it will contain, and what systems it will spawn, and handles everything automatically when data is written to it.

We are going to cover both approaches in this guide both to give options and a comparison between the two, and to show an upgrade path. The Lyra project used array based spawning in previous versions, and for 5.4 we updated its impacts to support using Niagara Data Channels, so we will be using Lyra as both example cases.

When sending payload data, either with arrays or Data Channels, the general flow will be writing the data, usually from gameplay code, spawning particles based on that data in the Niagara system, and reading back that data to initialize the particle.

## User Parameter SaaS

At its simplest a User Parameter can be used to change the spawn rate, or burst count of a particle system, which could be used to “add” particles to an existing system. For things like muzzle flashes that are attached to a single component and don’t need to respond to a projectile’s direction, this could be a viable setup, with limited need for managing the Niagara component’s lifetime or position. For more complex use cases like impacts and tracers, array based spawning can serve as a way of passing payloads of data to the system. Prior to 5.4 this was the only strategy employed for Lyra’s impacts for Concrete and Glass surfaces, and is still used for tracers. For 5.4 it's still the default behavior, but can now be toggled to use the experimental data channels feature.

### Lyra Impacts from Arrays

Lyra impacts are managed by the B\_WeaponImpacts class. An instance of this is created in the class B\_Weapon from the “Fire” custom event. Having a separate object owning impacts solved an issue where impacts would despawn when switching weapons. B\_WeaponImpacts has a default system template for each surface type, and will spawn that system when a new impact on that surface occurs. If an existing system for that surface is close enough to a new impact, that system instance will be used instead of spawning a new one. Once the impact system instance is found or created, the relevant data (e.g. Impact Positions, Impact Normals, Muzzle Position) is written to the corresponding user parameters on that system.

#### Writing Data

Since the payload data is already an array, it can be written to the system directly using the functions in UNiagaraDataInterfaceArrayFunctionLibrary, e.g. Set Niagara Array Vector, Set Niagara Array Float, Set Niagara Array Position. Each surface has a different system associated with it, so before writing the data it's easiest to sort it by the surface type.

Begin Object Class=/Script/BlueprintGraph.K2Node\_FunctionEntry Name="K2Node\_FunctionEntry\_0" ExportPath="/Script/BlueprintGraph.K2Node\_FunctionEntry'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_FunctionEntry\_0'"
LocalVariables(0)=(VarName="CurrentSystemTemplate",VarGuid=CCF92258429BA2DF98198C98D9FFC48D,VarType=(PinCategory="object",PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraSystem'"),FriendlyName="Current System Template",Category=NSLOCTEXT("KismetSchema", "Default", "Default"),PropertyFlags=5)
LocalVariables(1)=(VarName="Impact System",VarGuid=0FFEA59B419383C35AF1B880337BBBDC,VarType=(PinCategory="object",PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'"),FriendlyName="Impact System",Category=NSLOCTEXT("KismetSchema", "Default", "Default"),PropertyFlags=5)
LocalVariables(2)=(VarName="Current Position",VarGuid=E0B43EC4415CD1473B7322BDE9B78C78,VarType=(PinCategory="struct",PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'"),FriendlyName="Current Position",Category=NSLOCTEXT("KismetSchema", "Default", "Default"),PropertyFlags=5)
ExtraFlags=201457664
FunctionReference=(MemberName="SpawnFromArrays")
bIsEditable=True
ErrorType=1
NodeGuid=ECB739804E9D0DE7D169C0B885D46555
CustomProperties Pin (PinId=CDED4CB0493EFB9DC5ECB482D31F1950,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_3 B16669EC48710C52DA5A54A3E0CB8859,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=198987324B50AE3023DA239029E0C875,PinName="SurfaceType",Direction="EGPD\_Output",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="SurfaceType\_Default",AutogeneratedDefaultValue="SurfaceType\_Default",LinkedTo=(K2Node\_Knot\_0 7BC321F04188CA2D80765BB28A5F0B73,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties UserDefinedPin (PinName="SurfaceType",PinType=(PinCategory="byte",PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'"),DesiredPinDirection=EGPD\_Output,PinDefaultValue="SurfaceType\_Default")
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Select Name="K2Node\_Select\_1" ExportPath="/Script/BlueprintGraph.K2Node\_Select'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_Select\_1'"
NumOptionPins=4
IndexPinType=(PinCategory="byte",PinSubCategory="",PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'")
Enum="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'"
EnumEntries(0)="SurfaceType\_Default"
EnumEntries(1)="SurfaceType1"
EnumEntries(2)="SurfaceType2"
EnumEntries(3)="SurfaceType3"
NodePosX=576
NodePosY=80
NodeGuid=4EF130F94F6C924D7EDFDBB30A0F3582
CustomProperties Pin (PinId=B74F76114E77DC6A5DF769B9B8925F06,PinName="SurfaceType\_Default",PinFriendlyName=NSLOCTEXT("UObjectDisplayNames", "EPhysicalSurface.SurfaceType\_Default", "Default"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraSystem'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_62 80F45063482ACF8AA9F06FB498250733,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=C6406A1247806A365D5999867DE68A25,PinName="SurfaceType1",PinFriendlyName="Character",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraSystem'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_61 12685BE54B83EEF92A66E4BC720CA2C0,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=318E2D3D4D214BB6A406A9A9017154BC,PinName="SurfaceType2",PinFriendlyName="Concrete",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraSystem'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_55 B6B4C970404DE1A80D4A198DDF63113C,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=D607D53943C768544839D192B97B82DB,PinName="SurfaceType3",PinFriendlyName="Glass",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraSystem'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_56 A0F8B1BA4D1D05B7251FC9BF1B2FF535,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=AA7B7336428093026DC0D2A0B24F22E1,PinName="Index",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="SurfaceType\_Default",LinkedTo=(K2Node\_Knot\_0 656935224AD1F38D5E0919AC37403765,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=66E3CA454CE4E8ECEFD4BEB75D0461B4,PinName="ReturnValue",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraSystem'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_3 4268DEDA41430968998EC2B9F99EFA05,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_55" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_55'"
VariableReference=(MemberName="Concrete",MemberGuid=2EA160BC4C34F738CC888FAF9F1F684F,bSelfContext=True)
NodePosX=352
NodePosY=160
NodeGuid=B9672DA54FA2CE188332AAAAA7A0CF2D
CustomProperties Pin (PinId=B6B4C970404DE1A80D4A198DDF63113C,PinName="Concrete",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraSystem'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Select\_1 318E2D3D4D214BB6A406A9A9017154BC,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=C6B2493A458292743C7705BA93006A89,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.BlueprintGeneratedClass'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts\_C'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_56" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_56'"
VariableReference=(MemberName="Glass",MemberGuid=3E024C3149F24DFC0BA1A1AD45396FF4,bSelfContext=True)
NodePosX=352
NodePosY=208
NodeGuid=CA83367247F3D992F5B8DDA548A1AE43
CustomProperties Pin (PinId=A0F8B1BA4D1D05B7251FC9BF1B2FF535,PinName="Glass",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraSystem'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Select\_1 D607D53943C768544839D192B97B82DB,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=ED057CE14110AA94684677B27C18DF00,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.BlueprintGeneratedClass'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts\_C'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_61" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_61'"
VariableReference=(MemberName="Character",MemberGuid=7F50E6CB40A649FBEF10DFBC3FE9F0B6,bSelfContext=True)
NodePosX=352
NodePosY=112
NodeGuid=6BCB8F73463174D39CA5FEB270C49C9F
CustomProperties Pin (PinId=12685BE54B83EEF92A66E4BC720CA2C0,PinName="Character",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraSystem'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Select\_1 C6406A1247806A365D5999867DE68A25,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=6A144648461637422653E1BA09392F54,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.BlueprintGeneratedClass'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts\_C'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_62" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_62'"
VariableReference=(MemberName="Default",MemberGuid=FB7097C0470CD3B9795AD8A16F7F96DC,bSelfContext=True)
NodePosX=352
NodePosY=64
NodeGuid=095BEBAC40A5B5B0418B2A81C51E4851
CustomProperties Pin (PinId=80F45063482ACF8AA9F06FB498250733,PinName="Default",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraSystem'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Select\_1 B74F76114E77DC6A5DF769B9B8925F06,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=D17966944DBB9EC9336E0896AA9AE6C1,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.BlueprintGeneratedClass'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts\_C'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableSet Name="K2Node\_VariableSet\_3" ExportPath="/Script/BlueprintGraph.K2Node\_VariableSet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableSet\_3'"
VariableReference=(MemberScope="SpawnFromArrays",MemberName="CurrentSystemTemplate",MemberGuid=CCF92258429BA2DF98198C98D9FFC48D)
NodePosX=816
NodePosY=16
NodeGuid=35126BC0447879948FFEF5A6F4E5B1A8
CustomProperties Pin (PinId=B16669EC48710C52DA5A54A3E0CB8859,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_FunctionEntry\_0 CDED4CB0493EFB9DC5ECB482D31F1950,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=BC5923D04CEF787A02D184B40918C50F,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_IfThenElse\_0 705307A64A8618237E3EF7A295009582,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=4268DEDA41430968998EC2B9F99EFA05,PinName="CurrentSystemTemplate",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraSystem'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Select\_1 66E3CA454CE4E8ECEFD4BEB75D0461B4,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=3A74C3D14E4800EBD7DC59AF472A1064,PinName="Output\_Get",PinToolTip="Retrieves the value of the variable, can use instead of a separate Get node",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraSystem'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_1 C9C9065D42A1D2EDCA742481452F3122,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_0" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_Knot\_0'"
NodePosX=336
NodePosY=304
NodeGuid=53A46F6E43318094C26843B1E97D3513
CustomProperties Pin (PinId=7BC321F04188CA2D80765BB28A5F0B73,PinName="InputPin",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_FunctionEntry\_0 198987324B50AE3023DA239029E0C875,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=656935224AD1F38D5E0919AC37403765,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Select\_1 AA7B7336428093026DC0D2A0B24F22E1,K2Node\_Knot\_7 D64915C844779132F14D80B7AA7D4D54,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_0" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_0'"
VariableReference=(MemberName="ImpactBuckets",MemberGuid=F6FA52F946E7E71540C651AC19610825,bSelfContext=True)
NodePosX=816
NodePosY=208
ErrorType=1
NodeGuid=6FDE42084553FAE92C8EE0B31A66EBCD
CustomProperties Pin (PinId=CCFE483B4B20CA50B0F4929724EAD70F,PinName="ImpactBuckets",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.UserDefinedStruct'/Game/Effects/Blueprints/SurfaceImpacts.SurfaceImpacts'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_GetArrayItem\_1 CAAF92F84F2A7D4113DCE293987DB89A,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=A4D856B34BAB843865D7E09937F59F45,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.BlueprintGeneratedClass'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts\_C'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_IfThenElse Name="K2Node\_IfThenElse\_0" ExportPath="/Script/BlueprintGraph.K2Node\_IfThenElse'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_IfThenElse\_0'"
NodePosX=1312
NodeGuid=06DC0E9D4428C305F0E737B788FE73F2
CustomProperties Pin (PinId=705307A64A8618237E3EF7A295009582,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_3 BC5923D04CEF787A02D184B40918C50F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=F55DF9894B25374CBB8B628FA511A16B,PinName="Condition",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="true",AutogeneratedDefaultValue="true",LinkedTo=(K2Node\_CallFunction\_1 B342EE684E2C1FD49564059DF46C9DC3,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=A3A2DCEE46BCB5C0392D2CA880519A7C,PinName="then",PinFriendlyName=NSLOCTEXT("K2Node", "true", "true"),Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_5 28621B1E474B215CA4C1FCB56F7525B3,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=5B0217EC486413D45238A78A80B0B599,PinName="else",PinFriendlyName=NSLOCTEXT("K2Node", "false", "false"),Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_1" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_CallFunction\_1'"
bIsPureFunc=True
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.KismetSystemLibrary'",MemberName="IsValid")
NodePosX=1088
NodePosY=64
NodeGuid=0C68D93842A99C4F978560AB5FC8591C
CustomProperties Pin (PinId=674F0BA5457C2CDA0C121FB168F118F0,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.KismetSystemLibrary'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Script/Engine.Default\_\_KismetSystemLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=C9C9065D42A1D2EDCA742481452F3122,PinName="Object",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/CoreUObject.Object'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=True,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_3 3A74C3D14E4800EBD7DC59AF472A1064,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=B342EE684E2C1FD49564059DF46C9DC3,PinName="ReturnValue",Direction="EGPD\_Output",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="false",AutogeneratedDefaultValue="false",LinkedTo=(K2Node\_IfThenElse\_0 F55DF9894B25374CBB8B628FA511A16B,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_5" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_5'"
VariableReference=(MemberName="Impact Systems",MemberGuid=4B7428E54385D474E0943B90102C9F2D,bSelfContext=True)
NodePosX=1456
NodePosY=160
NodeGuid=80317BF24DF0B4EA224EC38A56E2E19A
CustomProperties Pin (PinId=5A35C8AB40A5635F3EABBB8187463F8B,PinName="Impact Systems",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallArrayFunction\_1 92D70DE34F898A38DBF0E99B7F426851,K2Node\_GetArrayItem\_3 A62FA692491A004E766219AB8CB240A1,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=FF1C43514ADB069B4A33B1B83CEC1FA6,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.BlueprintGeneratedClass'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts\_C'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_IfThenElse Name="K2Node\_IfThenElse\_1" ExportPath="/Script/BlueprintGraph.K2Node\_IfThenElse'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_IfThenElse\_1'"
NodePosX=2128
NodeGuid=E231A15346FA3309F76D068C016E9965
CustomProperties Pin (PinId=B6D50751460C2AED23C813A05272AB11,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_5 A5CDB5A64F8FDC9117DDFAB12F45F575,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=85DF16FE44FADA1C7D462EB8841322D4,PinName="Condition",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="true",AutogeneratedDefaultValue="true",LinkedTo=(K2Node\_CallArrayFunction\_1 3FDEB63F47E9F4A21D0DE5934E5AFC9D,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=0338236C4E35F550FC318382116F5ACA,PinName="then",PinFriendlyName=NSLOCTEXT("K2Node", "true", "true"),Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_MacroInstance\_0 62B258414E56E3B658367E8A708C07ED,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=F5B201AE40DD72E6621224AC73220113,PinName="else",PinFriendlyName=NSLOCTEXT("K2Node", "false", "false"),Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_15 CE4B48F14BCBAC17B869568620D1FD7A,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_1" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_Knot\_1'"
NodePosX=1472
NodePosY=304
NodeGuid=5BB7C72944C72947A5756EBE78B97BD7
CustomProperties Pin (PinId=DF504C384206F6265B999B90738332E2,PinName="InputPin",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_7 682C4F91497FAD2F23BEE89F7DEC13CF,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=408F64624BAFD2FFE39A14A5F50044DC,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_8 199806A14E7161DDA6877C9AC42654BF,K2Node\_CallFunction\_0 9EB82CB34460C92D9D519291B66A4A49,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_15" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_CallFunction\_15'"
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Niagara.NiagaraFunctionLibrary'",MemberName="SpawnSystemAtLocation")
NodePosX=2880
NodePosY=96
NodeGuid=13C0BBB4496254B4226B9C90BF638319
CustomProperties Pin (PinId=CE4B48F14BCBAC17B869568620D1FD7A,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_IfThenElse\_1 F5B201AE40DD72E6621224AC73220113,K2Node\_IfThenElse\_2 C9B86AE04FDEE23CEED1FAB992C8EDDA,K2Node\_MacroInstance\_0 E45CD9194D7AEE489244558679369253,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=87C86ED048761C6256BB7BB3E39CBD61,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_1 968032A94E606254B44FEC8A55BB163C,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=C40A30E640DE491498CF78A824DBCE8D,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraFunctionLibrary'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Script/Niagara.Default\_\_NiagaraFunctionLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=BAE05DC44BC2AB486E6297B5EF71F9F2,PinName="WorldContextObject",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/CoreUObject.Object'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=True,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=F75CFC5849502CDFB64290BA543A751C,PinName="SystemTemplate",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraSystem'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_4 CE71BE654FBC5AC711C335B4B83D45E1,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=07F08E50411AE7BA0950409DB8F9D167,PinName="Location",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node\_VariableGet\_9 7B2DD7E2419997AC5C723E8F48ACC1F3,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=422236474D582A686C65978EC602C960,PinName="Rotation",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Rotator'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=62C2D5514957829795BCDEA3C25CDC93,PinName="Scale",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="1.000000,1.000000,1.000000",AutogeneratedDefaultValue="1.000000,1.000000,1.000000",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=02D64AD9438D88FC1295319C191E6819,PinName="bAutoDestroy",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="true",AutogeneratedDefaultValue="true",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=E12A7537427B217EBC4557AF665AACFA,PinName="bAutoActivate",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="true",AutogeneratedDefaultValue="true",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=C31F3E734F2B31E377E105A894DBFF34,PinName="PoolingMethod",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/Niagara.ENCPoolMethod'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="None",AutogeneratedDefaultValue="None",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=B3B6E993499FC3694187A99EDA31E604,PinName="bPreCullCheck",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="true",AutogeneratedDefaultValue="true",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=DE662CAB42C980D2D136BC8340303F40,PinName="ReturnValue",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_1 8167793E4E690344AD5EF98EC6D8D8F6,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_4" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_4'"
VariableReference=(MemberScope="SpawnFromArrays",MemberName="CurrentSystemTemplate",MemberGuid=CCF92258429BA2DF98198C98D9FFC48D)
NodePosX=2432
NodePosY=144
NodeGuid=F73B800C4BDF6DBE3AB92584D9A7203F
CustomProperties Pin (PinId=CE71BE654FBC5AC711C335B4B83D45E1,PinName="CurrentSystemTemplate",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraSystem'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_15 F75CFC5849502CDFB64290BA543A751C,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_BreakStruct Name="K2Node\_BreakStruct\_0" ExportPath="/Script/BlueprintGraph.K2Node\_BreakStruct'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_BreakStruct\_0'"
bMadeAfterOverridePinRemoval=True
ShowPinForProperties(0)=(PropertyName="ImpactPositions\_6\_4DAE749E4058967754F0BB873262A3B7",PropertyFriendlyName="ImpactPositions",bShowPin=True,bCanToggleVisibility=True)
ShowPinForProperties(1)=(PropertyName="ImpcatNormals\_5\_E3297B4A4DE28BD6A85D8EA46FD6060A",PropertyFriendlyName="ImpcatNormals",bShowPin=True,bCanToggleVisibility=True)
StructType="/Script/Engine.UserDefinedStruct'/Game/Effects/Blueprints/SurfaceImpacts.SurfaceImpacts'"
NodePosX=1168
NodePosY=384
ErrorType=1
NodeGuid=DD25FDCE480909253A47EBB3C9F0C63C
CustomProperties Pin (PinId=0B557E3D4DE5AA89089B71A02F922F71,PinName="SurfaceImpacts",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.UserDefinedStruct'/Game/Effects/Blueprints/SurfaceImpacts.SurfaceImpacts'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=True,PinType.bIsConst=True,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_GetArrayItem\_1 C404B60149F8A6EFE43217906C2A0DB3,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=7ED65D35410B86B32D90918BC669A018,PinName="ImpactPositions\_6\_4DAE749E4058967754F0BB873262A3B7",PinFriendlyName="ImpactPositions",PinToolTip="Impact Positions\nArray of Vectors",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_GetArrayItem\_0 43C578F84B90C15E48E40C92E6AE88DC,K2Node\_Knot\_2 CF288C4847A202E7486132AF56560F13,),PersistentGuid=4DAE749E4058967754F0BB873262A3B7,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=7D59C6914326F83FFDDAE8BEA9FF3CA2,PinName="ImpcatNormals\_5\_E3297B4A4DE28BD6A85D8EA46FD6060A",PinFriendlyName="ImpcatNormals",PinToolTip="Impcat Normals\nArray of Vectors",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_5 1621378846F9A46E8B2E36A90E8715EA,),PersistentGuid=E3297B4A4DE28BD6A85D8EA46FD6060A,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_GetArrayItem Name="K2Node\_GetArrayItem\_0" ExportPath="/Script/BlueprintGraph.K2Node\_GetArrayItem'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_GetArrayItem\_0'"
bReturnByRefDesired=False
NodePosX=1552
NodePosY=400
NodeGuid=460711DD474597F62C2001AE8308A7EB
CustomProperties Pin (PinId=43C578F84B90C15E48E40C92E6AE88DC,PinName="Array",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_BreakStruct\_0 7ED65D35410B86B32D90918BC669A018,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=E18A1E934BC00A26986F86B264307F92,PinName="Dimension 1",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=A4DCA07E45668116A3537D9B965EA414,PinName="Output",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_5 365833A7414570B8EA81CBB39F62003D,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_5" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_CallFunction\_5'"
bIsPureFunc=True
bIsConstFunc=True
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.SceneComponent'",MemberName="K2\_GetComponentLocation")
NodePosX=1856
NodePosY=304
ErrorType=1
NodeGuid=CCCF4BE446C97ECA0EF852A00254066F
CustomProperties Pin (PinId=E835C3CF48E929AAE75E9AA88AF70E62,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.SceneComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_GetArrayItem\_3 9C24CF4C4FB61D78E41CCC9EEF1F865C,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=2EB6735548EB7A93435865B75E42927D,PinName="ReturnValue",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node\_CallFunction\_33 8C5ADB36478107391F4666AD87EFAE3F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_PromotableOperator Name="K2Node\_PromotableOperator\_1" ExportPath="/Script/BlueprintGraph.K2Node\_PromotableOperator'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_PromotableOperator\_1'"
OperationName="Greater"
bIsPureFunc=True
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.KismetMathLibrary'",MemberName="Greater\_DoubleDouble")
NodePosX=2544
NodePosY=304
NodeGuid=E5C3109244B6E2D9A02807A8C1E313A6
CustomProperties Pin (PinId=60F050C64B8E56E2AE87288C08150E45,PinName="A",PinType.PinCategory="real",PinType.PinSubCategory="double",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_33 7E70F8EB4DCD4D3D072324A5E4230878,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=4CDBB0BD4A71A3C128A487A1ED54D4B8,PinName="B",PinType.PinCategory="real",PinType.PinSubCategory="double",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_6 F3705CC9498C939D02ABD79F17A16F39,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=DE528BA8408A76808D6CFEA80FD8A6E6,PinName="ReturnValue",Direction="EGPD\_Output",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_IfThenElse\_2 87D222824187F5C0A9C61386294B3459,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=5A77BC0F4378B4503740B0A5E4264C15,PinName="ErrorTolerance",PinType.PinCategory="",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_PromotableOperator Name="K2Node\_PromotableOperator\_2" ExportPath="/Script/BlueprintGraph.K2Node\_PromotableOperator'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_PromotableOperator\_2'"
OperationName="Multiply"
bIsPureFunc=True
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.KismetMathLibrary'",MemberName="Multiply\_DoubleDouble")
NodePosX=2160
NodePosY=400
NodeGuid=F0DEFC164B84B5A1671FD597860E9107
CustomProperties Pin (PinId=ED1E321545CBC687DAB7A082EAEE50C7,PinName="A",PinType.PinCategory="real",PinType.PinSubCategory="double",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_46 2C8514364951DA9EB9D883B9C5EC0D14,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=F201F5774EC132F3BEEA938CD1B2B662,PinName="B",PinType.PinCategory="real",PinType.PinSubCategory="double",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_46 2C8514364951DA9EB9D883B9C5EC0D14,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=FEE42885409C388CEFD268992BC004A8,PinName="ReturnValue",Direction="EGPD\_Output",PinType.PinCategory="real",PinType.PinSubCategory="double",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_6 EE4D9ADF42808AA828BBC7989F018C56,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_46" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_46'"
VariableReference=(MemberName="Distance Threshold",MemberGuid=D753EC2543396162010DB38869748320,bSelfContext=True)
NodePosX=1920
NodePosY=416
NodeGuid=98B5956344729ABE8F39C587BF18C116
CustomProperties Pin (PinId=2C8514364951DA9EB9D883B9C5EC0D14,PinName="Distance Threshold",Direction="EGPD\_Output",PinType.PinCategory="real",PinType.PinSubCategory="double",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0.0",AutogeneratedDefaultValue="0.0",LinkedTo=(K2Node\_PromotableOperator\_2 ED1E321545CBC687DAB7A082EAEE50C7,K2Node\_PromotableOperator\_2 F201F5774EC132F3BEEA938CD1B2B662,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=15B3B5D445F8AA6A3FD7B692E08A456C,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.BlueprintGeneratedClass'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts\_C'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_33" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_CallFunction\_33'"
bIsPureFunc=True
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.KismetMathLibrary'",MemberName="Vector\_DistanceSquared")
NodePosX=2256
NodePosY=288
NodeGuid=478E69C345EBF13767ABA08B10CD46AA
CustomProperties Pin (PinId=6DF66C6E42AFA7D6E51746BFB184EB83,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.KismetMathLibrary'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Script/Engine.Default\_\_KismetMathLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=641A4A8D439E9754CC49EEA4867C446C,PinName="V1",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node\_VariableGet\_11 7B2DD7E2419997AC5C723E8F48ACC1F3,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=8C5ADB36478107391F4666AD87EFAE3F,PinName="V2",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node\_CallFunction\_5 2EB6735548EB7A93435865B75E42927D,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=7E70F8EB4DCD4D3D072324A5E4230878,PinName="ReturnValue",Direction="EGPD\_Output",PinType.PinCategory="real",PinType.PinSubCategory="double",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0.0",AutogeneratedDefaultValue="0.0",LinkedTo=(K2Node\_PromotableOperator\_1 60F050C64B8E56E2AE87288C08150E45,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_IfThenElse Name="K2Node\_IfThenElse\_2" ExportPath="/Script/BlueprintGraph.K2Node\_IfThenElse'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_IfThenElse\_2'"
NodePosX=2656
NodeGuid=ED16633E4EF23FD4E71C22B4FD79740C
CustomProperties Pin (PinId=671E39144A0355F6C90FF0A5E9D4E9A6,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_MacroInstance\_0 E06AF1814217B5EF9F784FABB34531C0,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=87D222824187F5C0A9C61386294B3459,PinName="Condition",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="true",AutogeneratedDefaultValue="true",LinkedTo=(K2Node\_PromotableOperator\_1 DE528BA8408A76808D6CFEA80FD8A6E6,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=F7C171574282A335950DBEB4696C705B,PinName="then",PinFriendlyName=NSLOCTEXT("K2Node", "true", "true"),Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_4 985CEB0D416477F4F48757A7F5FECD5F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=C9B86AE04FDEE23CEED1FAB992C8EDDA,PinName="else",PinFriendlyName=NSLOCTEXT("K2Node", "false", "false"),Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_15 CE4B48F14BCBAC17B869568620D1FD7A,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableSet Name="K2Node\_VariableSet\_4" ExportPath="/Script/BlueprintGraph.K2Node\_VariableSet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableSet\_4'"
VariableReference=(MemberScope="SpawnFromArrays",MemberName="Impact System",MemberGuid=0FFEA59B419383C35AF1B880337BBBDC)
NodePosX=3744
NodePosY=16
NodeGuid=1F61CF944E212D69C4A891B920B57D31
CustomProperties Pin (PinId=985CEB0D416477F4F48757A7F5FECD5F,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_IfThenElse\_2 F7C171574282A335950DBEB4696C705B,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=58FF75F44FABC38075831996B35B4DA6,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_6 0DE1E4A34DC5EE48AD24F09E3B91D5C7,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=50D4EEA8430B39C04B56609BDDC5089A,PinName="Impact System",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_GetArrayItem\_3 9C24CF4C4FB61D78E41CCC9EEF1F865C,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=933FBA72469D63BC1B5805AC796C4E2A,PinName="Output\_Get",PinToolTip="Retrieves the value of the variable, can use instead of a separate Get node",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_6" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_CallFunction\_6'"
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.SceneComponent'",MemberName="K2\_SetWorldLocation")
NodePosX=4032
NodePosY=-16
NodeGuid=D04CCC3A4D3E89AE1BEA0581EF48FC7B
CustomProperties Pin (PinId=0DE1E4A34DC5EE48AD24F09E3B91D5C7,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_4 58FF75F44FABC38075831996B35B4DA6,K2Node\_CallArrayFunction\_2 D9B248E143B5517819CCB194004D936F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=26F2D51740BF275A2323429B976F4505,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_2 872EA81A473798F4065A11A87CE1A36A,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=D89E939D46E22B5035B946AFE91B64AF,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.SceneComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_12 BD1C122B4EFE2F4F8E7E57BBD7321C0D,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=ECC53E26472035DDCB8D47922E1C0E8B,PinName="NewLocation",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node\_VariableGet\_8 D8D6EEA84E00D2E87C37D3846D143637,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=76768D564894D3B7D6558680DD8B71AA,PinName="bSweep",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="false",AutogeneratedDefaultValue="false",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=BC33DB844244AE33F37B50B48B464683,PinName="SweepHitResult",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/Engine.HitResult'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=42ED38314F18A087EADC74BA698415D7,PinName="bTeleport",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="false",AutogeneratedDefaultValue="false",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_17" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_CallFunction\_17'"
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataInterfaceArrayFunctionLibrary'",MemberName="SetNiagaraArrayVector")
NodePosX=5104
NodeGuid=0777821A4F0D7AE977A0288337A41CFC
CustomProperties Pin (PinId=7840618943162EA45033C1B28F6245AE,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_9 7EC563514C2371F102A47EBB205C0B53,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=1FB2030A416BF03AA11FA99FF151317C,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_12 1FA7A00E4DBF17EEFF39209F73211D93,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=EE21134E46A17C4685E6EA93FBBC67D2,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataInterfaceArrayFunctionLibrary'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Script/Niagara.Default\_\_NiagaraDataInterfaceArrayFunctionLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=33507A9C4F387E1B7F5C6D8AD3D47D36,PinName="NiagaraSystem",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_15 BD1C122B4EFE2F4F8E7E57BBD7321C0D,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=88D14B4643B52C97E1B89BA38EF3CDEE,PinName="OverrideName",PinType.PinCategory="name",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="User.ImpactNormals",AutogeneratedDefaultValue="None",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=D3EBA376496E0888B24216A4522836FF,PinName="ArrayData",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=True,PinType.bIsConst=True,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_4 9D1AF1F847D18B64DB3B2AA24D38D804,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_2" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_CallFunction\_2'"
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataInterfaceArrayFunctionLibrary'",MemberName="SetNiagaraArrayPosition")
NodePosX=4449
NodeGuid=C0244EEE446B35E4DD29809E915FDC2D
CustomProperties Pin (PinId=872EA81A473798F4065A11A87CE1A36A,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_6 26F2D51740BF275A2323429B976F4505,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=2ADAD8D64E11154E5F298CA87397CD54,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_9 7EC1114245280A1AF8797C9575DF6B6D,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=22440E9D463AAC64E8D7DC917F3C85D8,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataInterfaceArrayFunctionLibrary'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Script/Niagara.Default\_\_NiagaraDataInterfaceArrayFunctionLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=F1F945E8464E7B8F4F1F6A9A72F98F1C,PinName="NiagaraSystem",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_13 BD1C122B4EFE2F4F8E7E57BBD7321C0D,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=72795FF949B3DE170FB7EAA11A1A80D5,PinName="OverrideName",PinType.PinCategory="name",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="User.ImpactPositions",AutogeneratedDefaultValue="None",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=382487BC4AB7086BC77F98B986A1E774,PinName="ArrayData",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=True,PinType.bIsConst=True,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_3 D124C6C24700755994F9EC9476DBA5DB,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_7" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_7'"
VariableReference=(MemberName="MuzzlePosition",MemberGuid=C4AFE4234A52853FE10B6E86751F2152,bSelfContext=True)
NodePosX=5328
NodePosY=208
NodeGuid=914471C341FE0DE7FFD9FD857EBFFAFB
CustomProperties Pin (PinId=C851E94647CA1FAF051DE0BF90D44A37,PinName="MuzzlePosition",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node\_CallFunction\_12 CCC3BC4648F5586304C6998F2C47351C,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=301DDF024D8F0FCB69215EAA26846651,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.BlueprintGeneratedClass'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts\_C'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_12" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_CallFunction\_12'"
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",MemberName="SetVariablePosition")
NodePosX=5440
NodePosY=-16
NodeGuid=0D7378644D035F2E81C0AFA169A4073A
CustomProperties Pin (PinId=1FA7A00E4DBF17EEFF39209F73211D93,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_17 1FB2030A416BF03AA11FA99FF151317C,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=2F03BD93433D39690025F5B60F647532,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_11 82C3061A48D2E7F499BBE992212FB943,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=32C9484848B003655FA507A17ACF4F49,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_6 BD1C122B4EFE2F4F8E7E57BBD7321C0D,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=12CE1AEF4ED4A8CD379C9E94A61ACEAF,PinName="InVariableName",PinType.PinCategory="name",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="User.MuzzlePosition",AutogeneratedDefaultValue="None",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=CCC3BC4648F5586304C6998F2C47351C,PinName="InValue",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node\_VariableGet\_7 C851E94647CA1FAF051DE0BF90D44A37,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_9" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_CallFunction\_9'"
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",MemberName="SetVariableInt")
NodePosX=4736
NodePosY=-16
NodeGuid=5B2D682D4A0628A1CEC649AB97427DE4
CustomProperties Pin (PinId=7EC1114245280A1AF8797C9575DF6B6D,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_2 2ADAD8D64E11154E5F298CA87397CD54,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=7EC563514C2371F102A47EBB205C0B53,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_17 7840618943162EA45033C1B28F6245AE,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=4BC9EC644689A444108DBB90DFF1B7BD,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_14 BD1C122B4EFE2F4F8E7E57BBD7321C0D,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=D337A93E4A0EC63F6882699670F08CC9,PinName="InVariableName",PinType.PinCategory="name",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="NumberOfHits",AutogeneratedDefaultValue="None",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=D39E461043967332E449D99F7D3B5683,PinName="InValue",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_CallArrayFunction\_0 0C005F194F286B3AEF5411850D9E30FF,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallArrayFunction Name="K2Node\_CallArrayFunction\_0" ExportPath="/Script/BlueprintGraph.K2Node\_CallArrayFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_CallArrayFunction\_0'"
bIsPureFunc=True
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.KismetArrayLibrary'",MemberName="Array\_Length")
NodePosX=4320
NodePosY=512
NodeGuid=6DF36AD44D19605DE226848677FA755D
CustomProperties Pin (PinId=11DB88B7477A0506781AF8BA553E76C4,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.KismetArrayLibrary'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Script/Engine.Default\_\_KismetArrayLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=D906FAFB49226693A2B466962CC1AC5D,PinName="TargetArray",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=True,PinType.bIsConst=True,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_3 D124C6C24700755994F9EC9476DBA5DB,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=0C005F194F286B3AEF5411850D9E30FF,PinName="ReturnValue",Direction="EGPD\_Output",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_CallFunction\_9 D39E461043967332E449D99F7D3B5683,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableSet Name="K2Node\_VariableSet\_5" ExportPath="/Script/BlueprintGraph.K2Node\_VariableSet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableSet\_5'"
VariableReference=(MemberScope="SpawnFromArrays",MemberName="Current Position",MemberGuid=E0B43EC4415CD1473B7322BDE9B78C78)
NodePosX=1600
NodePosY=16
NodeGuid=306466754A0B478C385C45A55EAF9A5E
CustomProperties Pin (PinId=28621B1E474B215CA4C1FCB56F7525B3,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_IfThenElse\_0 A3A2DCEE46BCB5C0392D2CA880519A7C,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=A5CDB5A64F8FDC9117DDFAB12F45F575,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_IfThenElse\_1 B6D50751460C2AED23C813A05272AB11,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=365833A7414570B8EA81CBB39F62003D,PinName="Current Position",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node\_GetArrayItem\_0 A4DCA07E45668116A3537D9B965EA414,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=9D690D63417DCF69505A6B89B0ECE3E6,PinName="Output\_Get",PinToolTip="Retrieves the value of the variable, can use instead of a separate Get node",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_8" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_8'"
VariableReference=(MemberScope="SpawnFromArrays",MemberName="Current Position",MemberGuid=E0B43EC4415CD1473B7322BDE9B78C78)
NodePosX=3824
NodePosY=176
NodeGuid=547593EB46ABFE29A92FF881F4AC4AFF
CustomProperties Pin (PinId=D8D6EEA84E00D2E87C37D3846D143637,PinName="Current Position",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node\_CallFunction\_6 ECC53E26472035DDCB8D47922E1C0E8B,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_11" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_11'"
VariableReference=(MemberScope="SpawnFromArrays",MemberName="Current Position",MemberGuid=E0B43EC4415CD1473B7322BDE9B78C78)
NodePosX=2080
NodePosY=304
NodeGuid=79E642204F05A075FE7C7095F6470EDE
CustomProperties Pin (PinId=7B2DD7E2419997AC5C723E8F48ACC1F3,PinName="Current Position",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node\_CallFunction\_33 641A4A8D439E9754CC49EEA4867C446C,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_2" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_Knot\_2'"
NodePosX=1664
NodePosY=592
NodeGuid=406D933D4E85987171AF1DAD481F3643
CustomProperties Pin (PinId=CF288C4847A202E7486132AF56560F13,PinName="InputPin",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_BreakStruct\_0 7ED65D35410B86B32D90918BC669A018,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=5FD5F9C4474C28C708E3A48A2135A7D2,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_3 975EE3FB48C3EA9F86423E96BCD50351,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_3" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_Knot\_3'"
NodePosX=4080
NodePosY=544
NodeGuid=A95FF4B042B6224742B8389DC341B5B9
CustomProperties Pin (PinId=975EE3FB48C3EA9F86423E96BCD50351,PinName="InputPin",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_2 5FD5F9C4474C28C708E3A48A2135A7D2,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=D124C6C24700755994F9EC9476DBA5DB,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallArrayFunction\_0 D906FAFB49226693A2B466962CC1AC5D,K2Node\_CallFunction\_2 382487BC4AB7086BC77F98B986A1E774,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_4" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_Knot\_4'"
NodePosX=4944
NodePosY=672
NodeGuid=5085399F4AAF22E04C5C5B8BBD99FFD7
CustomProperties Pin (PinId=38A1007246BAC641A80BA1AE33FCB3BE,PinName="InputPin",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_5 87301582460C99AE50B04589ECD816EE,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=9D1AF1F847D18B64DB3B2AA24D38D804,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_17 D3EBA376496E0888B24216A4522836FF,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_5" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_Knot\_5'"
NodePosX=1584
NodePosY=720
NodeGuid=5EE73FF74F4866675D8E7F9444B59D59
CustomProperties Pin (PinId=1621378846F9A46E8B2E36A90E8715EA,PinName="InputPin",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_BreakStruct\_0 7D59C6914326F83FFDDAE8BEA9FF3CA2,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=87301582460C99AE50B04589ECD816EE,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_4 38A1007246BAC641A80BA1AE33FCB3BE,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_6" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_Knot\_6'"
NodePosX=2464
NodePosY=400
NodeGuid=B0EF44A742FCA93AC952C8BB7A89ACE2
CustomProperties Pin (PinId=EE4D9ADF42808AA828BBC7989F018C56,PinName="InputPin",PinType.PinCategory="real",PinType.PinSubCategory="double",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_PromotableOperator\_2 FEE42885409C388CEFD268992BC004A8,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=F3705CC9498C939D02ABD79F17A16F39,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="real",PinType.PinSubCategory="double",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_PromotableOperator\_1 4CDBB0BD4A71A3C128A487A1ED54D4B8,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_7" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_Knot\_7'"
NodePosX=688
NodePosY=304
NodeGuid=3CF66F05405676861B1656B76AED3FEB
CustomProperties Pin (PinId=D64915C844779132F14D80B7AA7D4D54,PinName="InputPin",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_0 656935224AD1F38D5E0919AC37403765,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=682C4F91497FAD2F23BEE89F7DEC13CF,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_1 DF504C384206F6265B999B90738332E2,K2Node\_CallFunction\_7 660FE84A4B2135A709FFF3BC2C9AE1D5,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_8" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_Knot\_8'"
NodePosX=1872
NodePosY=496
NodeGuid=FF474CD9461951F2ADFD169508FFB92B
CustomProperties Pin (PinId=199806A14E7161DDA6877C9AC42654BF,PinName="InputPin",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_1 408F64624BAFD2FFE39A14A5F50044DC,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=29E32F6E493080577846B4A980B0A0CB,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_9 6104588B4F76ADFC7557BD855C02510F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_10" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_10'"
VariableReference=(MemberName="Impact Systems",MemberGuid=4B7428E54385D474E0943B90102C9F2D,bSelfContext=True)
NodePosX=3296
NodePosY=208
NodeGuid=44929D80498E80992797F6BB126EE2E1
CustomProperties Pin (PinId=FE04AE274452BEFD24A730B0EA0F2C26,PinName="Impact Systems",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallArrayFunction\_2 0B991E144F2B0927E299A4BB0D97C6CC,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=93756C9D428FDAF6A0D285AA435115D0,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.BlueprintGeneratedClass'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts\_C'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_9" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_Knot\_9'"
NodePosX=2448
NodePosY=496
NodeGuid=5D4240094D3C9E0B8B42D98587FED893
CustomProperties Pin (PinId=6104588B4F76ADFC7557BD855C02510F,PinName="InputPin",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_8 29E32F6E493080577846B4A980B0A0CB,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=A99F562040CCB1DB8A2CCE8162FDC5C1,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_13 A4EC66464265C96817C06D878013CB32,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_9" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_9'"
VariableReference=(MemberScope="SpawnFromArrays",MemberName="Current Position",MemberGuid=E0B43EC4415CD1473B7322BDE9B78C78)
NodePosX=2624
NodePosY=224
NodeGuid=532262604176D4F0A0EF12B6ED741797
CustomProperties Pin (PinId=7B2DD7E2419997AC5C723E8F48ACC1F3,PinName="Current Position",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node\_CallFunction\_15 07F08E50411AE7BA0950409DB8F9D167,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableSet Name="K2Node\_VariableSet\_1" ExportPath="/Script/BlueprintGraph.K2Node\_VariableSet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableSet\_1'"
VariableReference=(MemberScope="SpawnFromArrays",MemberName="Impact System",MemberGuid=0FFEA59B419383C35AF1B880337BBBDC)
NodePosX=3264
NodePosY=112
NodeGuid=5765BF054C3227211BFEEDB0D6802F1F
CustomProperties Pin (PinId=968032A94E606254B44FEC8A55BB163C,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_15 87C86ED048761C6256BB7BB3E39CBD61,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=132EF3F54AECE57CC1251C9CBD590B36,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallArrayFunction\_2 530892BE4EE618D799BFE28840A7FC30,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=8167793E4E690344AD5EF98EC6D8D8F6,PinName="Impact System",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_15 DE662CAB42C980D2D136BC8340303F40,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=89026867485D6FA2B10E9DA51890ADB4,PinName="Output\_Get",PinToolTip="Retrieves the value of the variable, can use instead of a separate Get node",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallArrayFunction\_2 3D80600F4493D92B4F47C0B7FC57334F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_12" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_12'"
VariableReference=(MemberScope="SpawnFromArrays",MemberName="Impact System",MemberGuid=0FFEA59B419383C35AF1B880337BBBDC)
NodePosX=3792
NodePosY=304
NodeGuid=2AEB7BAA41CFB3EA8639408B612F3C44
CustomProperties Pin (PinId=BD1C122B4EFE2F4F8E7E57BBD7321C0D,PinName="Impact System",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_6 D89E939D46E22B5035B946AFE91B64AF,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_13" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_13'"
VariableReference=(MemberScope="SpawnFromArrays",MemberName="Impact System",MemberGuid=0FFEA59B419383C35AF1B880337BBBDC)
NodePosX=4352
NodePosY=256
NodeGuid=B97B6BB44B03A9F4A3BCE1B267180A20
CustomProperties Pin (PinId=BD1C122B4EFE2F4F8E7E57BBD7321C0D,PinName="Impact System",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_2 F1F945E8464E7B8F4F1F6A9A72F98F1C,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_14" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_14'"
VariableReference=(MemberScope="SpawnFromArrays",MemberName="Impact System",MemberGuid=0FFEA59B419383C35AF1B880337BBBDC)
NodePosX=4528
NodePosY=336
NodeGuid=90CDDFB34D57588B0BD47A94ABF18ADF
CustomProperties Pin (PinId=BD1C122B4EFE2F4F8E7E57BBD7321C0D,PinName="Impact System",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_9 4BC9EC644689A444108DBB90DFF1B7BD,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_15" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_15'"
VariableReference=(MemberScope="SpawnFromArrays",MemberName="Impact System",MemberGuid=0FFEA59B419383C35AF1B880337BBBDC)
NodePosX=5088
NodePosY=336
NodeGuid=C1FFE00C44D9EECB631DDEACA5026655
CustomProperties Pin (PinId=BD1C122B4EFE2F4F8E7E57BBD7321C0D,PinName="Impact System",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_17 33507A9C4F387E1B7F5C6D8AD3D47D36,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_6" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_VariableGet\_6'"
VariableReference=(MemberScope="SpawnFromArrays",MemberName="Impact System",MemberGuid=0FFEA59B419383C35AF1B880337BBBDC)
NodePosX=5328
NodePosY=272
NodeGuid=7A08500E4A635C33D3EAABB55783FEEB
CustomProperties Pin (PinId=BD1C122B4EFE2F4F8E7E57BBD7321C0D,PinName="Impact System",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_12 32C9484848B003655FA507A17ACF4F49,K2Node\_CallFunction\_11 E7565A6147F0F0CACEDE8CB20ACB57BF,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_GetArrayItem Name="K2Node\_GetArrayItem\_1" ExportPath="/Script/BlueprintGraph.K2Node\_GetArrayItem'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_GetArrayItem\_1'"
NodePosX=976
NodePosY=208
NodeGuid=86EB4D2F44377C366C092BA3400D88E9
CustomProperties Pin (PinId=CAAF92F84F2A7D4113DCE293987DB89A,PinName="Array",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.UserDefinedStruct'/Game/Effects/Blueprints/SurfaceImpacts.SurfaceImpacts'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_0 CCFE483B4B20CA50B0F4929724EAD70F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=25E883DA485A4A630953EEA7D45FB9C8,PinName="Dimension 1",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_CallFunction\_7 F859CD384F83802F9D10EB9B518F6139,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=C404B60149F8A6EFE43217906C2A0DB3,PinName="Output",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.UserDefinedStruct'/Game/Effects/Blueprints/SurfaceImpacts.SurfaceImpacts'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=True,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_BreakStruct\_0 0B557E3D4DE5AA89089B71A02F922F71,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_7" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_CallFunction\_7'"
bIsPureFunc=True
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.KismetMathLibrary'",MemberName="Conv\_ByteToInt")
NodePosX=800
NodePosY=272
NodeGuid=56872B09494251C3407F43B6FB376408
CustomProperties Pin (PinId=B75147B64641DA9D655E58BFAE9AAD5B,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.KismetMathLibrary'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Script/Engine.Default\_\_KismetMathLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=660FE84A4B2135A709FFF3BC2C9AE1D5,PinName="InByte",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_Knot\_7 682C4F91497FAD2F23BEE89F7DEC13CF,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=F859CD384F83802F9D10EB9B518F6139,PinName="ReturnValue",Direction="EGPD\_Output",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_GetArrayItem\_1 25E883DA485A4A630953EEA7D45FB9C8,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_11" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_CallFunction\_11'"
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.ActorComponent'",MemberName="Activate")
NodePosX=5808
NodePosY=-16
NodeGuid=36549B0D45A48BDE8F8BB48B8D58A5F8
CustomProperties Pin (PinId=82C3061A48D2E7F499BBE992212FB943,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_12 2F03BD93433D39690025F5B60F647532,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=480745C04FF6103612DA58B6B51A3178,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=E7565A6147F0F0CACEDE8CB20ACB57BF,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.ActorComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_6 BD1C122B4EFE2F4F8E7E57BBD7321C0D,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=CE5EADA94551647D54A3478C18789C39,PinName="bReset",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="false",AutogeneratedDefaultValue="false",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/UnrealEd.EdGraphNode\_Comment Name="EdGraphNode\_Comment\_6" ExportPath="/Script/UnrealEd.EdGraphNode\_Comment'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.EdGraphNode\_Comment\_6'"
bCommentBubbleVisible\_InDetailsPanel=False
NodePosX=792
NodePosY=-96
NodeWidth=736
NodeHeight=256
bCommentBubblePinned=False
bCommentBubbleVisible=False
NodeComment="If no tempalte is set up for this surface, don't spawn any particles."
NodeGuid=553C702F4D5AE627F26DF4BE9B5AA998
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallArrayFunction Name="K2Node\_CallArrayFunction\_1" ExportPath="/Script/BlueprintGraph.K2Node\_CallArrayFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_CallArrayFunction\_1'"
bIsPureFunc=True
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.KismetArrayLibrary'",MemberName="Array\_IsValidIndex")
NodePosX=1760
NodePosY=80
NodeGuid=94973C0B4621BD5CA62F91BFBC75C112
CustomProperties Pin (PinId=0FC3B2CE466AF169F4DB8F9963ECE5E4,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.KismetArrayLibrary'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Script/Engine.Default\_\_KismetArrayLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=92D70DE34F898A38DBF0E99B7F426851,PinName="TargetArray",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=True,PinType.bIsConst=True,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_5 5A35C8AB40A5635F3EABBB8187463F8B,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=4942FF8B4872C872BF00848FD6E9C34F,PinName="IndexToTest",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_CallFunction\_0 E5D16E1F4134FFB945AD34AD95E80704,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=3FDEB63F47E9F4A21D0DE5934E5AFC9D,PinName="ReturnValue",Direction="EGPD\_Output",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="false",AutogeneratedDefaultValue="false",LinkedTo=(K2Node\_IfThenElse\_1 85DF16FE44FADA1C7D462EB8841322D4,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_0" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_CallFunction\_0'"
bIsPureFunc=True
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.KismetMathLibrary'",MemberName="Conv\_ByteToInt")
NodePosX=1584
NodePosY=304
NodeGuid=DCC7330241B484AD9C75D5AF874AC252
CustomProperties Pin (PinId=31D836DA4C9527173E2EF89EC65751B2,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.KismetMathLibrary'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Script/Engine.Default\_\_KismetMathLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=9EB82CB34460C92D9D519291B66A4A49,PinName="InByte",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_Knot\_1 408F64624BAFD2FFE39A14A5F50044DC,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=E5D16E1F4134FFB945AD34AD95E80704,PinName="ReturnValue",Direction="EGPD\_Output",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_CallArrayFunction\_1 4942FF8B4872C872BF00848FD6E9C34F,K2Node\_GetArrayItem\_3 C756B7C243362FC77EBA9FAE3856592F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_GetArrayItem Name="K2Node\_GetArrayItem\_3" ExportPath="/Script/BlueprintGraph.K2Node\_GetArrayItem'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_GetArrayItem\_3'"
bReturnByRefDesired=False
NodePosX=1744
NodePosY=160
NodeGuid=1919310941D289B9F06B58863BA0AE53
CustomProperties Pin (PinId=A62FA692491A004E766219AB8CB240A1,PinName="Array",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_5 5A35C8AB40A5635F3EABBB8187463F8B,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=C756B7C243362FC77EBA9FAE3856592F,PinName="Dimension 1",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_CallFunction\_0 E5D16E1F4134FFB945AD34AD95E80704,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=9C24CF4C4FB61D78E41CCC9EEF1F865C,PinName="Output",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_4 50D4EEA8430B39C04B56609BDDC5089A,K2Node\_CallFunction\_5 E835C3CF48E929AAE75E9AA88AF70E62,K2Node\_MacroInstance\_0 5DD6F6FA410D5876E296BCAB2ADD98C7,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallArrayFunction Name="K2Node\_CallArrayFunction\_2" ExportPath="/Script/BlueprintGraph.K2Node\_CallArrayFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_CallArrayFunction\_2'"
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.KismetArrayLibrary'",MemberName="Array\_Set")
NodePosX=3504
NodePosY=96
NodeGuid=4416567443D2FAC5D0E78D9AB2C38AC2
CustomProperties Pin (PinId=530892BE4EE618D799BFE28840A7FC30,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_1 132EF3F54AECE57CC1251C9CBD590B36,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=D9B248E143B5517819CCB194004D936F,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_6 0DE1E4A34DC5EE48AD24F09E3B91D5C7,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=0E6A84B54D37D1A0C9DFA6B136868723,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.KismetArrayLibrary'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Script/Engine.Default\_\_KismetArrayLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=0B991E144F2B0927E299A4BB0D97C6CC,PinName="TargetArray",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=True,PinType.bIsConst=True,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_10 FE04AE274452BEFD24A730B0EA0F2C26,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=00715BCE40A42E1E549B93871CB622C1,PinName="Index",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_CallFunction\_13 BE45F28446130CDE4681FE8CB7CA3C6C,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=3D80600F4493D92B4F47C0B7FC57334F,PinName="Item",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=True,PinType.bIsConst=True,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_1 89026867485D6FA2B10E9DA51890ADB4,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=CADFC81D4782BCEDDD2DC3913CE7E9A0,PinName="bSizeToFit",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="true",AutogeneratedDefaultValue="false",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_13" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_CallFunction\_13'"
bIsPureFunc=True
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.KismetMathLibrary'",MemberName="Conv\_ByteToInt")
NodePosX=3280
NodePosY=480
NodeGuid=F46DF0BE4F74BE85B6E46F91EA27FB1C
CustomProperties Pin (PinId=D6E352FB4B324A2A25FCF1AE4DF1512B,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.KismetMathLibrary'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Script/Engine.Default\_\_KismetMathLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=A4EC66464265C96817C06D878013CB32,PinName="InByte",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_Knot\_9 A99F562040CCB1DB8A2CCE8162FDC5C1,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=BE45F28446130CDE4681FE8CB7CA3C6C,PinName="ReturnValue",Direction="EGPD\_Output",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_CallArrayFunction\_2 00715BCE40A42E1E549B93871CB622C1,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/UnrealEd.EdGraphNode\_Comment Name="EdGraphNode\_Comment\_7" ExportPath="/Script/UnrealEd.EdGraphNode\_Comment'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.EdGraphNode\_Comment\_7'"
bCommentBubbleVisible\_InDetailsPanel=False
NodePosX=1827
NodePosY=246
NodeWidth=880
NodeHeight=256
bCommentBubblePinned=False
bCommentBubbleVisible=False
NodeComment="Distance check using sqaured distance. "
NodeGuid=B600048B4D8C3A2E7C014AA3711CA624
End Object
Begin Object Class=/Script/UnrealEd.EdGraphNode\_Comment Name="EdGraphNode\_Comment\_8" ExportPath="/Script/UnrealEd.EdGraphNode\_Comment'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.EdGraphNode\_Comment\_8'"
bCommentBubbleVisible\_InDetailsPanel=False
NodePosX=2120
NodePosY=-78
NodeWidth=752
NodeHeight=208
bCommentBubblePinned=False
bCommentBubbleVisible=False
NodeComment="If no valid system is found, or if it's too far away, spawn a new one."
NodeGuid=AE2427DF4F1203D627C2FDBE32516B25
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_MacroInstance Name="K2Node\_MacroInstance\_0" ExportPath="/Script/BlueprintGraph.K2Node\_MacroInstance'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromArrays.K2Node\_MacroInstance\_0'"
MacroGraphReference=(MacroGraph="/Script/Engine.EdGraph'/Engine/EditorBlueprintResources/StandardMacros.StandardMacros:IsValid'",GraphBlueprint="/Script/Engine.Blueprint'/Engine/EditorBlueprintResources/StandardMacros.StandardMacros'",GraphGuid=64422BCD430703FF5CAEA8B79A32AA65)
NodePosX=2352
NodeGuid=BEA55BF04E03BC3412AD089B1C45D2AB
CustomProperties Pin (PinId=62B258414E56E3B658367E8A708C07ED,PinName="exec",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_IfThenElse\_1 0338236C4E35F550FC318382116F5ACA,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=5DD6F6FA410D5876E296BCAB2ADD98C7,PinName="InputObject",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/CoreUObject.Object'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_GetArrayItem\_3 9C24CF4C4FB61D78E41CCC9EEF1F865C,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=E06AF1814217B5EF9F784FABB34531C0,PinName="Is Valid",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_IfThenElse\_2 671E39144A0355F6C90FF0A5E9D4E9A6,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=E45CD9194D7AEE489244558679369253,PinName="Is Not Valid",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_15 CE4B48F14BCBAC17B869568620D1FD7A,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object

#### Spawning

There are two Niagara system assets that support array spawning for Lyra impacts, NS\_ImpactGlass and NS\_ImpactConcrete. These systems are comprised of emitters based on the same parent assets that are then customized in the systems. These emitters use Spawn Burst Instantaneous modules to spawn their particles and the custom module NM\_ImpactSpawnAttributes to read the data from the array user parameters. Some of the spawn modules have a fixed size, and some use the passed in User.NumberOfHits parameter to modulate the number of particles spawned.

#### Reading from Arrays

The Impact Spawn Attributes module is a bit more involved. It uses the particle’s execution index, along with a start offset and the number of hits to index into the provided arrays. The start offset was originally used because all data from all impact surface types were bundled into the same array. The start offset was the index where a particular surface’s data started, so each system would read from the offset that corresponded to its surface type. The Number of hits was used as a modulus to loop the particles back around if there were more particles than impact positions. The module then used this data to calculate values that were used elsewhere in the simulation, for example the impact normal, tangent and particle position.

With the refactor to support data channels, the arrays for this data were separated into structs based on surface type. This makes it easier to support different spawning strategies for different surface types, and eliminates the need for the start offset.

With the way these systems were set-up they looped once, and never spawned more than one burst of particles per activation. This avoided any issues where the array data may have been out of date. Values can be read and removed from the end of the array to clear the data as it is read with the Remove Last Elem node. This approach doesn’t work for these impact systems as the data needs to be read multiple times as there are multiple emitters. The values could be cleared externally or in the particle simulations, but that could lead to race conditions. Re-activating the system with fresh data is an acceptable compromise, though there is overhead to re-activating the system.

## Data Channel SaaS

Data channels handle many aspects of the SaaS approach automatically, including writing data to the correct systems, spawning and placing those systems, and system lifetime management. This simplifies the use case, and optimizes some of these steps to offer better performance than an array based approach. For an intro tutorial to Niagara Data Channels follow the link below. To summarize: creating a Niagara Data Channel asset defines the structure of the data being sent to Niagara systems, and in the case of the Islands Data Channels, defines what systems to spawn, and how to spawn them when data is written to that data channel. The system then defines the behavior for spawning particles and reading that data to be used within the wider simulation. Data channels provide nodes to facilitate conditional spawning, and spawn ranges to allow for spawning a variable amount of particles and in different circumstances.

### Lyra Impacts from Data Channels

Just like with the array implementation for impacts, the Data Channel implementation relied on the B\_WeaponImpacts Blueprint class. Since Data Channels handle Niagara system spawning automatically, having a separate object from the weapon to manage the lifetime of the impacts is not necessary, but has been kept for a more direct comparison. Additionally the bucketing of impacts based on surface types is not strictly necessary either, since the data channel uses one merged system to handle all surface types.

#### Writing Data

The Data Channel specific behavior is handled in the function Spawn from Data Channels, which initiates a data channel write based on the number of impacts and the first position written to the array. This data is passed in to the search params, which are used to find the correct island to use for the current batch of writes, which determines the system written to. In the Lyra example it is assumed that the impacts will be close to the first position written, though it’s possible to have impacts spread further apart, for example the shotgun spread could collide partially with close geometry, and partially with geometry far away.

Once the batch has been initiated with “Write to Niagara Data Channel (Batch)”, the Impact Positions array is iterated over to write all the impact data to the data channel. The batched writes will accumulate the data written in this loop, and then publish it to the Niagara simulation when finished. For the data channels the two systems NS\_ImpactGlass and NS\_ImpactConcrete were merged into one system NS\_ImpactDataChannel. The emitters from the previous systems were versioned and updated to spawn from the data channel in their emitter update script, and read from it in their particle spawn scripts.

Begin Object Class=/Script/BlueprintGraph.K2Node\_FunctionEntry Name="K2Node\_FunctionEntry\_0" ExportPath="/Script/BlueprintGraph.K2Node\_FunctionEntry'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_FunctionEntry\_0'"
LocalVariables(0)=(VarName="Current Read Index",VarGuid=9298375C41113AEE02D02CB244C05E7C,VarType=(PinCategory="int"),FriendlyName="Current Read Index",Category=NSLOCTEXT("KismetSchema", "Default", "Default"),PropertyFlags=5)
LocalVariables(1)=(VarName="NewLocalVar",VarGuid=2275ABC44FE449E9C8DC6E80EFCCA452,VarType=(PinCategory="struct",PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",ContainerType=Array),FriendlyName="New Local Var",Category=NSLOCTEXT("KismetSchema", "Default", "Default"),PropertyFlags=5)
ExtraFlags=201457664
FunctionReference=(MemberName="SpawnFromDataChannels")
bIsEditable=True
NodePosX=-544
NodeGuid=F6F0DF04447620551D35F6B2CE1A45A7
CustomProperties Pin (PinId=98CBD6A548ACA18F40FD3B8C2C7BEB5D,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_1 D3C3D6D540E17935BD6955B01B521B06,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=21647E534B962D45C85A4CBA955B86CC,PinName="SurfaceType",Direction="EGPD\_Output",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="SurfaceType\_Default",AutogeneratedDefaultValue="SurfaceType\_Default",LinkedTo=(K2Node\_Knot\_11 6AD7944A436CC15DC94CCCB02B942DF8,K2Node\_CallFunction\_0 3D69DF7D45D763237F7CFFA830A3C57F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties UserDefinedPin (PinName="SurfaceType",PinType=(PinCategory="byte",PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'"),DesiredPinDirection=EGPD\_Output,PinDefaultValue="SurfaceType\_Default")
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_1" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_CallFunction\_1'"
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelLibrary'",MemberName="WriteToNiagaraDataChannel")
NodePosX=1248
AdvancedPinDisplay=Shown
NodeGuid=004E5A924203E98B599D48960B491799
CustomProperties Pin (PinId=D3C3D6D540E17935BD6955B01B521B06,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_FunctionEntry\_0 98CBD6A548ACA18F40FD3B8C2C7BEB5D,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=0F56293340E0096655FFDDA1770F3635,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_MacroInstance\_1 8E6CD9144DC9D8DDDD0E3CB6EF8506C5,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=988F76F44201FA85D7A0AD9896B8765B,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelLibrary'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Script/Niagara.Default\_\_NiagaraDataChannelLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=47600C134446CAFD2A44FDACEB9D373D,PinName="WorldContextObject",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/CoreUObject.Object'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=True,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=B3D4B609424D8FD20056BBAFC96B2B86,PinName="Channel",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelAsset'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=True,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Game/Effects/DataChannels/ImpactDataChannel.ImpactDataChannel",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=4F74024640B8295D379978A53C8B1E23,PinName="SearchParams",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/Niagara.NiagaraDataChannelSearchParameters'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_MakeStruct\_0 A227292C4BC0427594862697A4E37FEF,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=True,bOrphanedPin=False,)
CustomProperties Pin (PinId=AE6359A74C1F45004B383481330889D6,PinName="Count",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_CallArrayFunction\_0 45E838C0471B5BBED2B5E382554C4676,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=213D4B5648F66C30C10E2983A9922C8F,PinName="bVisibleToGame",PinFriendlyName="Visible to Blueprint",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="true",AutogeneratedDefaultValue="false",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=B30DA017418E1D620715A8A9D942C9AB,PinName="bVisibleToCPU",PinFriendlyName="Visible to Niagara CPU",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="true",AutogeneratedDefaultValue="false",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=E9AF422943E1C8B24E56B8BF7B171ECB,PinName="bVisibleToGPU",PinFriendlyName="Visible to Niagara GPU",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="true",AutogeneratedDefaultValue="false",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=63E015C64D4C3D4014BDE78B3D0E5F31,PinName="DebugSource",PinType.PinCategory="string",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=True,bOrphanedPin=False,)
CustomProperties Pin (PinId=C92F6397465C124113B0B398AC350302,PinName="ReturnValue",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_0 7B327EA341E55FA5E06CB384D5ED0A61,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_MakeStruct Name="K2Node\_MakeStruct\_0" ExportPath="/Script/BlueprintGraph.K2Node\_MakeStruct'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_MakeStruct\_0'"
bMadeAfterOverridePinRemoval=True
ShowPinForProperties(0)=(PropertyName="OwningComponent",PropertyFriendlyName="Owning Component",PropertyTooltip=NSLOCTEXT("UObjectToolTips", "NiagaraDataChannelSearchParameters:OwningComponent", "In cases where there is an owning component such as an object spawning from itself etc, then we pass that component in. Some handlers may only use it's location but others may make use of more data."),CategoryName="Parameters",bShowPin=True,bCanToggleVisibility=True)
ShowPinForProperties(1)=(PropertyName="Location",PropertyFriendlyName="Location",PropertyTooltip=NSLOCTEXT("UObjectToolTips", "NiagaraDataChannelSearchParameters:Location", "In cases where there is no owning component for data being read or written to a data channel, we simply pass in a location. We can also use this when bOverrideLocaiton is set."),CategoryName="Parameters",bShowPin=True,bCanToggleVisibility=True)
ShowPinForProperties(2)=(PropertyName="bOverrideLocation",PropertyFriendlyName="Override Location",PropertyTooltip=NSLOCTEXT("UObjectToolTips", "NiagaraDataChannelSearchParameters:bOverrideLocation", "If true, even if an owning component is set, the data channel should use the Location value rather than the component location. If this is false, the NDC will get any location needed from the owning component."),CategoryName="Parameters",bShowPin=True,bCanToggleVisibility=True)
StructType="/Script/CoreUObject.ScriptStruct'/Script/Niagara.NiagaraDataChannelSearchParameters'"
NodePosX=768
NodePosY=208
NodeGuid=0DE76C3A4AE5FF7308C3EBA17BF4CB3C
CustomProperties Pin (PinId=A227292C4BC0427594862697A4E37FEF,PinName="NiagaraDataChannelSearchParameters",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/Niagara.NiagaraDataChannelSearchParameters'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_1 4F74024640B8295D379978A53C8B1E23,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=507AD86D46A7B0F20FDEEE9EDEE592EE,PinName="OwningComponent",PinFriendlyName="Owning Component",PinToolTip="Owning Component\nScene Component Object Reference\n\nIn cases where there is an owning component such as an object spawning from itself etc, then we pass that component in. Some handlers may only use it's location but others may make use of more data.",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.SceneComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=True,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_13 E369BB8749DF782D46497E93DFD49790,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=DD8C43D740E02161A02ACE926EB0738E,PinName="Location",PinFriendlyName="Location",PinToolTip="Location\nVector\n\nIn cases where there is no owning component for data being read or written to a data channel, we simply pass in a location. We can also use this when bOverrideLocaiton is set.",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0.000000,0.000000,0.000000",AutogeneratedDefaultValue="0.000000,0.000000,0.000000",LinkedTo=(K2Node\_GetArrayItem\_2 625D64134194F5237F7A52B04BADD606,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=F28F13424B45C34F37A9D8B00F156C4A,PinName="bOverrideLocation",PinFriendlyName="Override Location",PinToolTip="Override Location\nBoolean\n\nIf true, even if an owning component is set, the data channel should use the Location value rather than the component location. If this is false, the NDC will get any location needed from the owning component.",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="true",AutogeneratedDefaultValue="False",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_5" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_CallFunction\_5'"
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",MemberName="WritePosition")
NodePosX=2128
NodePosY=-16
NodeGuid=A4A27DFD431695C703EBCB91B8D112B6
CustomProperties Pin (PinId=FE8B8A684C7AF4BE7318CE9CE4A22755,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_1 2BCB0E7E4C3C187414C79D9A19BDCB71,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=19A11C5A45EDFFB87C81F8817786763B,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_6 E28C152D49EAD23864C29F8A50539A66,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=022641664D1A2AC03545E2ABC26A1B60,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_0 9F1D682541D0F7377B1746A075EFC3F0,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=CC314FF148733912C89F6C990247A3C7,PinName="VarName",PinType.PinCategory="name",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="ImpactPosition",AutogeneratedDefaultValue="None",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=749E18A8477E7A71D80B1699E8066FE3,PinName="Index",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_VariableGet\_3 8902C55F403793DAE42E2BAD8ED33A12,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=7F8AFCFF4892715A9EAD988B7B0E8A07,PinName="InData",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node\_GetArrayItem\_0 1EC946004C11B194A8150EA774A8BB12,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_4" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_VariableGet\_4'"
VariableReference=(MemberScope="SpawnFromDataChannels",MemberName="Current Read Index",MemberGuid=9298375C41113AEE02D02CB244C05E7C)
NodePosX=1648
NodePosY=512
NodeGuid=F7AF56644C6A70F908F424AA827CBF70
CustomProperties Pin (PinId=8902C55F403793DAE42E2BAD8ED33A12,PinName="Current Read Index",Direction="EGPD\_Output",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_GetArrayItem\_0 54A8C449445BCFEDA5C35FB3C587B652,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_GetArrayItem Name="K2Node\_GetArrayItem\_0" ExportPath="/Script/BlueprintGraph.K2Node\_GetArrayItem'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_GetArrayItem\_0'"
bReturnByRefDesired=False
NodePosX=1872
NodePosY=480
NodeGuid=08839A9A41EAF7714CC34E8D517415AD
CustomProperties Pin (PinId=3142C40647D0C1655922E5A681223D3A,PinName="Array",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_7 F16A104F4471BE3DFA02C096AEE4C00A,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=54A8C449445BCFEDA5C35FB3C587B652,PinName="Dimension 1",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_VariableGet\_4 8902C55F403793DAE42E2BAD8ED33A12,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=1EC946004C11B194A8150EA774A8BB12,PinName="Output",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_5 7F8AFCFF4892715A9EAD988B7B0E8A07,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_6" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_CallFunction\_6'"
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",MemberName="WriteVector")
NodePosX=2576
NodePosY=-16
NodeGuid=7584341A4F7F03D6BEFCFBBFB1BD2173
CustomProperties Pin (PinId=E28C152D49EAD23864C29F8A50539A66,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_5 19A11C5A45EDFFB87C81F8817786763B,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=B37AC333456076773702B2B03F2DE389,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_7 F1E4D90C4125C3529BFB038797087A91,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=0FD5220E47BA978B103638A9FF628547,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_1 4C49AEF24BAB416CB9838BBCEFF419B1,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=DFB7E8C140856AA0821FE8AE1EA74DA9,PinName="VarName",PinType.PinCategory="name",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="ImpactNormal",AutogeneratedDefaultValue="None",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=445CF6184F082FA9A2A4D5BF11D9A906,PinName="Index",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_VariableGet\_5 8902C55F403793DAE42E2BAD8ED33A12,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=949301744C6F9C73A63246B2AA0FDF0C,PinName="InData",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node\_GetArrayItem\_1 97541EFA4BE58E3986BC0D9345841A52,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_5" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_VariableGet\_5'"
VariableReference=(MemberScope="SpawnFromDataChannels",MemberName="Current Read Index",MemberGuid=9298375C41113AEE02D02CB244C05E7C)
NodePosX=2160
NodePosY=224
NodeGuid=2B5DBFF84B3305F9E725DAAFB93C98D5
CustomProperties Pin (PinId=8902C55F403793DAE42E2BAD8ED33A12,PinName="Current Read Index",Direction="EGPD\_Output",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_GetArrayItem\_1 8112A6344B699E724D60D8944065AEBA,K2Node\_CallFunction\_6 445CF6184F082FA9A2A4D5BF11D9A906,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_GetArrayItem Name="K2Node\_GetArrayItem\_1" ExportPath="/Script/BlueprintGraph.K2Node\_GetArrayItem'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_GetArrayItem\_1'"
bReturnByRefDesired=False
NodePosX=2400
NodePosY=192
NodeGuid=73C6E5E946F3E3A356312B92B45A0DB0
CustomProperties Pin (PinId=E48A80DB41BD3453A6B92F8B4CC70D9E,PinName="Array",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_9 3B6CBD974D613D207E9B19B99E841E47,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=8112A6344B699E724D60D8944065AEBA,PinName="Dimension 1",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_VariableGet\_5 8902C55F403793DAE42E2BAD8ED33A12,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=97541EFA4BE58E3986BC0D9345841A52,PinName="Output",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_6 949301744C6F9C73A63246B2AA0FDF0C,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_0" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_Knot\_0'"
NodePosX=1680
NodePosY=384
NodeGuid=73A05A0849B62C99C745C296C797B700
CustomProperties Pin (PinId=7B327EA341E55FA5E06CB384D5ED0A61,PinName="InputPin",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_1 C92F6397465C124113B0B398AC350302,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=9F1D682541D0F7377B1746A075EFC3F0,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_1 1584EB23473AC9DCD584548F9F6DDE79,K2Node\_CallFunction\_5 022641664D1A2AC03545E2ABC26A1B60,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_1" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_Knot\_1'"
NodePosX=2192
NodePosY=384
NodeGuid=5811FBC64A236EF28B609284D7DED01C
CustomProperties Pin (PinId=1584EB23473AC9DCD584548F9F6DDE79,PinName="InputPin",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_0 9F1D682541D0F7377B1746A075EFC3F0,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=4C49AEF24BAB416CB9838BBCEFF419B1,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_6 0FD5220E47BA978B103638A9FF628547,K2Node\_Knot\_2 5BDB4E0446F4D419E7D34DAC4624A055,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_7" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_CallFunction\_7'"
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",MemberName="WritePosition")
NodePosX=3120
NodePosY=-16
NodeGuid=10AA3CA44ECCC337737AAE92B96DCE4D
CustomProperties Pin (PinId=F1E4D90C4125C3529BFB038797087A91,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_6 B37AC333456076773702B2B03F2DE389,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=1127311E4EA7C36A75D82AB5511FD9B4,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_2 190DF600420D9BF5609EAC8380E5D3B3,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=BAFA669E420F480C2D4167ACB5318AFF,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_2 AB1509784F0D3808E2E187856618A37F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=8ED283C7463C75126305AB947AF3151A,PinName="VarName",PinType.PinCategory="name",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="MuzzlePosition",AutogeneratedDefaultValue="None",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=9A2CCB714BD0FD47C25992B54F68CC44,PinName="Index",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_VariableGet\_1 8902C55F403793DAE42E2BAD8ED33A12,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=6246E5C940C0FAC17ABF24A9292863BA,PinName="InData",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node\_VariableGet\_6 BC1F773B4B06616575AAA4A82B405E15,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_2" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_Knot\_2'"
NodePosX=2592
NodePosY=384
NodeGuid=ED671DF84F66A1B03E7D289B3288DE92
CustomProperties Pin (PinId=5BDB4E0446F4D419E7D34DAC4624A055,PinName="InputPin",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_1 4C49AEF24BAB416CB9838BBCEFF419B1,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=AB1509784F0D3808E2E187856618A37F,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_7 BAFA669E420F480C2D4167ACB5318AFF,K2Node\_Knot\_3 060ADAA848AFDDB530293CB567CE0470,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_6" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_VariableGet\_6'"
VariableReference=(MemberName="MuzzlePosition",MemberGuid=C4AFE4234A52853FE10B6E86751F2152,bSelfContext=True)
NodePosX=2976
NodePosY=256
NodeGuid=EF18F88A4538A68865F1A39AEA265410
CustomProperties Pin (PinId=BC1F773B4B06616575AAA4A82B405E15,PinName="MuzzlePosition",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node\_CallFunction\_7 6246E5C940C0FAC17ABF24A9292863BA,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=C2076C8C48A91B4EAD318A9E1BB32950,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.BlueprintGeneratedClass'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts\_C'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_3" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_Knot\_3'"
NodePosX=3184
NodePosY=384
NodeGuid=B8DE32734F954A234662DFBADF0530E3
CustomProperties Pin (PinId=060ADAA848AFDDB530293CB567CE0470,PinName="InputPin",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_2 AB1509784F0D3808E2E187856618A37F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=3F07C3E84BB6AB3723AE1FA9373E44FD,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_2 1994E1B748C00752F044EFA58D736E4D,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_2" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_VariableGet\_2'"
VariableReference=(MemberScope="SpawnFromDataChannels",MemberName="Current Read Index",MemberGuid=9298375C41113AEE02D02CB244C05E7C)
NodePosX=3504
NodePosY=144
NodeGuid=5511C7A54C47F6F2D0551F92F5CF3FA4
CustomProperties Pin (PinId=8902C55F403793DAE42E2BAD8ED33A12,PinName="Current Read Index",Direction="EGPD\_Output",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_CallFunction\_2 E3FA5D4047E3988E1D33E5981874BA86,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_13" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_VariableGet\_13'"
VariableReference=(MemberName="DefaultSceneRoot",bSelfContext=True)
NodePosX=560
NodePosY=160
NodeGuid=05A05BF545E732311A4A38B5E8685770
CustomProperties Pin (PinId=E369BB8749DF782D46497E93DFD49790,PinName="DefaultSceneRoot",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.SceneComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_MakeStruct\_0 507AD86D46A7B0F20FDEEE9EDEE592EE,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=774292384BF8C9C78CB5068BB477AD5E,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.BlueprintGeneratedClass'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts\_C'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_0" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_VariableGet\_0'"
VariableReference=(MemberName="ImpactBuckets",MemberGuid=F6FA52F946E7E71540C651AC19610825,bSelfContext=True)
NodePosX=-144
NodePosY=128
ErrorType=1
NodeGuid=04DE9C3A42ECDF30BF4ACC94224F2E22
CustomProperties Pin (PinId=7D1D5DAC46FFF258821DCCB08B214317,PinName="ImpactBuckets",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.UserDefinedStruct'/Game/Effects/Blueprints/SurfaceImpacts.SurfaceImpacts'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_GetArrayItem\_3 4EF0465A4ED13815909F2A80908E6864,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=1D02D29542F5486442BCB98B7DAE4182,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.BlueprintGeneratedClass'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts\_C'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_BreakStruct Name="K2Node\_BreakStruct\_0" ExportPath="/Script/BlueprintGraph.K2Node\_BreakStruct'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_BreakStruct\_0'"
bMadeAfterOverridePinRemoval=True
ShowPinForProperties(0)=(PropertyName="ImpactPositions\_6\_4DAE749E4058967754F0BB873262A3B7",PropertyFriendlyName="ImpactPositions",bShowPin=True,bCanToggleVisibility=True)
ShowPinForProperties(1)=(PropertyName="ImpcatNormals\_5\_E3297B4A4DE28BD6A85D8EA46FD6060A",PropertyFriendlyName="ImpcatNormals",bShowPin=True,bCanToggleVisibility=True)
StructType="/Script/Engine.UserDefinedStruct'/Game/Effects/Blueprints/SurfaceImpacts.SurfaceImpacts'"
NodePosX=192
NodePosY=112
ErrorType=1
NodeGuid=CF5C30E440CAAB179E65CE83114D3588
CustomProperties Pin (PinId=D455E72442EC6BD4A3AE5AB49A8487D0,PinName="SurfaceImpacts",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.UserDefinedStruct'/Game/Effects/Blueprints/SurfaceImpacts.SurfaceImpacts'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=True,PinType.bIsConst=True,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_GetArrayItem\_3 733E168D495DA848D61BAE8A1AF89381,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=710584D241093B8F654703B5B80BE15A,PinName="ImpactPositions\_6\_4DAE749E4058967754F0BB873262A3B7",PinFriendlyName="ImpactPositions",PinToolTip="Impact Positions\nArray of Vectors",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_4 48CE3ACB44F727843322EEA1D6B6E97E,),PersistentGuid=4DAE749E4058967754F0BB873262A3B7,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=9D83E8984982BEE4F8F9C1B4A62DC01D,PinName="ImpcatNormals\_5\_E3297B4A4DE28BD6A85D8EA46FD6060A",PinFriendlyName="ImpcatNormals",PinToolTip="Impcat Normals\nArray of Vectors",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_10 CE6587834826A60FF71D5A8D46CBF9CC,),PersistentGuid=E3297B4A4DE28BD6A85D8EA46FD6060A,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_GetArrayItem Name="K2Node\_GetArrayItem\_2" ExportPath="/Script/BlueprintGraph.K2Node\_GetArrayItem'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_GetArrayItem\_2'"
bReturnByRefDesired=False
NodePosX=576
NodePosY=240
NodeGuid=F0050310432C33426A28BD97E547E3DE
CustomProperties Pin (PinId=F13F989A4AE6C8286168ABA4679EB4B8,PinName="Array",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_4 80FDABFD45010A67E2B9E292DB0090DA,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=735B784C439160D8C6847A8E7C1D3EB9,PinName="Dimension 1",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=625D64134194F5237F7A52B04BADD606,PinName="Output",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_MakeStruct\_0 DD8C43D740E02161A02ACE926EB0738E,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallArrayFunction Name="K2Node\_CallArrayFunction\_0" ExportPath="/Script/BlueprintGraph.K2Node\_CallArrayFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_CallArrayFunction\_0'"
bIsPureFunc=True
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.KismetArrayLibrary'",MemberName="Array\_Length")
NodePosX=768
NodePosY=112
NodeGuid=D499A07F4A2A65F3DEF687B5D33C535C
CustomProperties Pin (PinId=7BAECAF5440EA67A318A908D371FF4D9,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.KismetArrayLibrary'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Script/Engine.Default\_\_KismetArrayLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=4B4602CF409CE74EB70B1BA221A980DC,PinName="TargetArray",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=True,PinType.bIsConst=True,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_4 80FDABFD45010A67E2B9E292DB0090DA,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=45E838C0471B5BBED2B5E382554C4676,PinName="ReturnValue",Direction="EGPD\_Output",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_CallFunction\_1 AE6359A74C1F45004B383481330889D6,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_4" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_Knot\_4'"
NodePosX=480
NodePosY=144
NodeGuid=8DFA946947B774AF76BC84912DFDDEC7
CustomProperties Pin (PinId=48CE3ACB44F727843322EEA1D6B6E97E,PinName="InputPin",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_BreakStruct\_0 710584D241093B8F654703B5B80BE15A,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=80FDABFD45010A67E2B9E292DB0090DA,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallArrayFunction\_0 4B4602CF409CE74EB70B1BA221A980DC,K2Node\_GetArrayItem\_2 F13F989A4AE6C8286168ABA4679EB4B8,K2Node\_Knot\_8 ACA866FC4ECEED1F8BE10FB72539F265,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_MacroInstance Name="K2Node\_MacroInstance\_1" ExportPath="/Script/BlueprintGraph.K2Node\_MacroInstance'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_MacroInstance\_1'"
MacroGraphReference=(MacroGraph="/Script/Engine.EdGraph'/Engine/EditorBlueprintResources/StandardMacros.StandardMacros:ForEachLoop'",GraphBlueprint="/Script/Engine.Blueprint'/Engine/EditorBlueprintResources/StandardMacros.StandardMacros'",GraphGuid=99DBFD5540A796041F72A5A9DA655026)
ResolvedWildcardType=(PinCategory="struct",PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",ContainerType=Array)
NodePosX=1584
NodeGuid=CE0044B048B81611980DF8AE7F9BE6B9
CustomProperties Pin (PinId=8E6CD9144DC9D8DDDD0E3CB6EF8506C5,PinName="Exec",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_1 0F56293340E0096655FFDDA1770F3635,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=DF6598A74EF2773042D16998886F504E,PinName="Array",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_7 F16A104F4471BE3DFA02C096AEE4C00A,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=159881E545FCF12F1A3131AD9B7013CC,PinName="LoopBody",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_1 43CE09DD4833ADB3B6B58E8DD6DA7276,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=81BA8EBD49F2DE7A43D0578ED346E7E8,PinName="Array Element",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=5A37E2C341E17B38216507855907304A,PinName="Array Index",Direction="EGPD\_Output",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableSet\_1 594815A34B2E9BF0B16BB88019D71E5D,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=BEF1E47C4D3975CFB38538BB2C35927A,PinName="Completed",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_7" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_Knot\_7'"
NodePosX=1344
NodePosY=496
NodeGuid=82932C5941CE5522EC16BF98FE57B929
CustomProperties Pin (PinId=1028174B4E75168A8DC33BB660D7AEF1,PinName="InputPin",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_8 909AC6CF4BA9903B9C01BCA7AEFB9CBD,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=F16A104F4471BE3DFA02C096AEE4C00A,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_MacroInstance\_1 DF6598A74EF2773042D16998886F504E,K2Node\_GetArrayItem\_0 3142C40647D0C1655922E5A681223D3A,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_8" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_Knot\_8'"
NodePosX=528
NodePosY=496
NodeGuid=1A9820484C63147FBCE5FAB00F7A63B7
CustomProperties Pin (PinId=ACA866FC4ECEED1F8BE10FB72539F265,PinName="InputPin",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_4 80FDABFD45010A67E2B9E292DB0090DA,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=909AC6CF4BA9903B9C01BCA7AEFB9CBD,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_7 1028174B4E75168A8DC33BB660D7AEF1,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableSet Name="K2Node\_VariableSet\_1" ExportPath="/Script/BlueprintGraph.K2Node\_VariableSet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_VariableSet\_1'"
VariableReference=(MemberScope="SpawnFromDataChannels",MemberName="Current Read Index",MemberGuid=9298375C41113AEE02D02CB244C05E7C)
NodePosX=1824
NodePosY=16
NodeGuid=013CF9314E5FEAE0B3CDCC98933E7267
CustomProperties Pin (PinId=43CE09DD4833ADB3B6B58E8DD6DA7276,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_MacroInstance\_1 159881E545FCF12F1A3131AD9B7013CC,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=2BCB0E7E4C3C187414C79D9A19BDCB71,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_5 FE8B8A684C7AF4BE7318CE9CE4A22755,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=594815A34B2E9BF0B16BB88019D71E5D,PinName="Current Read Index",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_MacroInstance\_1 5A37E2C341E17B38216507855907304A,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=90897F3A4489B7D347CF66A0A361BCA1,PinName="Output\_Get",PinToolTip="Retrieves the value of the variable, can use instead of a separate Get node",Direction="EGPD\_Output",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_9" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_Knot\_9'"
NodePosX=2128
NodePosY=560
NodeGuid=F3C1B81F4E966AA3C768909702ED7BFE
CustomProperties Pin (PinId=8B6B5B65439662B5D9F63BA922CC5657,PinName="InputPin",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_10 5883CA834A22C633A38896AB7EE9C9BC,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=3B6CBD974D613D207E9B19B99E841E47,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_GetArrayItem\_1 E48A80DB41BD3453A6B92F8B4CC70D9E,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_10" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_Knot\_10'"
NodePosX=512
NodePosY=544
NodeGuid=5208BAE74FE7AD1449A2BB88163780F0
CustomProperties Pin (PinId=CE6587834826A60FF71D5A8D46CBF9CC,PinName="InputPin",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_BreakStruct\_0 9D83E8984982BEE4F8F9C1B4A62DC01D,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=5883CA834A22C633A38896AB7EE9C9BC,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.ScriptStruct'/Script/CoreUObject.Vector'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_9 8B6B5B65439662B5D9F63BA922CC5657,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_1" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_VariableGet\_1'"
VariableReference=(MemberScope="SpawnFromDataChannels",MemberName="Current Read Index",MemberGuid=9298375C41113AEE02D02CB244C05E7C)
NodePosX=2960
NodePosY=176
NodeGuid=39B3FDAA451F07964F7F6DA1FA124F07
CustomProperties Pin (PinId=8902C55F403793DAE42E2BAD8ED33A12,PinName="Current Read Index",Direction="EGPD\_Output",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_CallFunction\_7 9A2CCB714BD0FD47C25992B54F68CC44,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_11" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_Knot\_11'"
NodePosX=-160
NodePosY=592
NodeGuid=A9E05C194E4B73AB90AF22A94A7557E7
CustomProperties Pin (PinId=6AD7944A436CC15DC94CCCB02B942DF8,PinName="InputPin",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_FunctionEntry\_0 21647E534B962D45C85A4CBA955B86CC,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=F6DBD91B4024E7675C3A99B511431B45,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_5 3C0D25B94377A779224E64966B62606E,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_GetArrayItem Name="K2Node\_GetArrayItem\_3" ExportPath="/Script/BlueprintGraph.K2Node\_GetArrayItem'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_GetArrayItem\_3'"
NodePosY=128
NodeGuid=23E84BE64F82131ACB9A95AB44938E9B
CustomProperties Pin (PinId=4EF0465A4ED13815909F2A80908E6864,PinName="Array",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.UserDefinedStruct'/Game/Effects/Blueprints/SurfaceImpacts.SurfaceImpacts'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=Array,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_0 7D1D5DAC46FFF258821DCCB08B214317,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=16DAB8454A82A7FE171F28B89181D07F,PinName="Dimension 1",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_CallFunction\_0 8C3460914B23164753C6D091BF87975F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=733E168D495DA848D61BAE8A1AF89381,PinName="Output",Direction="EGPD\_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.UserDefinedStruct'/Game/Effects/Blueprints/SurfaceImpacts.SurfaceImpacts'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=True,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_BreakStruct\_0 D455E72442EC6BD4A3AE5AB49A8487D0,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_0" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_CallFunction\_0'"
bIsPureFunc=True
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.KismetMathLibrary'",MemberName="Conv\_ByteToInt")
NodePosX=-144
NodePosY=192
NodeGuid=1C9486BE4734A6D88BD2CE921EE0285D
CustomProperties Pin (PinId=AADEA233439135F6181DB79FDB28F100,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.KismetMathLibrary'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject="/Script/Engine.Default\_\_KismetMathLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=3D69DF7D45D763237F7CFFA830A3C57F,PinName="InByte",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_FunctionEntry\_0 21647E534B962D45C85A4CBA955B86CC,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=8C3460914B23164753C6D091BF87975F,PinName="ReturnValue",Direction="EGPD\_Output",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_GetArrayItem\_3 16DAB8454A82A7FE171F28B89181D07F,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_3" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_VariableGet\_3'"
VariableReference=(MemberScope="SpawnFromDataChannels",MemberName="Current Read Index",MemberGuid=9298375C41113AEE02D02CB244C05E7C)
NodePosX=1968
NodePosY=144
NodeGuid=1F4F19924CEAE7E667789780B134CE54
CustomProperties Pin (PinId=8902C55F403793DAE42E2BAD8ED33A12,PinName="Current Read Index",Direction="EGPD\_Output",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_CallFunction\_5 749E18A8477E7A71D80B1699E8066FE3,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/UnrealEd.EdGraphNode\_Comment Name="EdGraphNode\_Comment\_0" ExportPath="/Script/UnrealEd.EdGraphNode\_Comment'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.EdGraphNode\_Comment\_0'"
bCommentBubbleVisible\_InDetailsPanel=False
NodePosX=535
NodePosY=-66
NodeWidth=704
NodeHeight=432
bCommentBubblePinned=False
bCommentBubbleVisible=False
NodeComment="Assuming impacts are clustered. We search based on the first position, and write all positions to the same writer."
NodeGuid=CBF8BA86442720262A2700B06B5B4D71
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_2" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_CallFunction\_2'"
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",MemberName="WriteEnum")
NodePosX=3712
NodePosY=-16
NodeGuid=6F25D7F642C5BDDB652745968A78FC1F
CustomProperties Pin (PinId=190DF600420D9BF5609EAC8380E5D3B3,PinName="execute",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_7 1127311E4EA7C36A75D82AB5511FD9B4,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=CA89116B4A705D62391133A92C494A39,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=1994E1B748C00752F044EFA58D736E4D,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Niagara.NiagaraDataChannelWriter'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_3 3F07C3E84BB6AB3723AE1FA9373E44FD,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=07FC26244DD247252FA58889D0598FEC,PinName="VarName",PinType.PinCategory="name",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="ImpactSurface",AutogeneratedDefaultValue="None",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=E3FA5D4047E3988E1D33E5981874BA86,PinName="Index",PinType.PinCategory="int",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_VariableGet\_2 8902C55F403793DAE42E2BAD8ED33A12,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=5CE80A29434A389BAC81C4BA0366022A,PinName="InData",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="0",AutogeneratedDefaultValue="0",LinkedTo=(K2Node\_Knot\_5 9138102D469B4A6332C601847C33C873,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_Knot Name="K2Node\_Knot\_5" ExportPath="/Script/BlueprintGraph.K2Node\_Knot'/Game/Effects/Blueprints/B\_WeaponImpacts.B\_WeaponImpacts:SpawnFromDataChannels.K2Node\_Knot\_5'"
NodePosX=3312
NodePosY=576
NodeGuid=962BF8B744AFF0F1885F7BB5266F9809
CustomProperties Pin (PinId=3C0D25B94377A779224E64966B62606E,PinName="InputPin",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_Knot\_11 F6DBD91B4024E7675C3A99B511431B45,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=9138102D469B4A6332C601847C33C873,PinName="OutputPin",Direction="EGPD\_Output",PinType.PinCategory="byte",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Enum'/Script/PhysicsCore.EPhysicalSurface'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_2 5CE80A29434A389BAC81C4BA0366022A,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object

#### Spawning

Particles are spawned from data channels in an emitter module by calling “Spawn Conditional” on a Data Channel Reader that has been initialized to read from the corresponding data channel. For Lyra impacts this is mainly handled by the NM\_ImpactSpawnDataChannel module.

The spawn logic is handled in UNiagaraDataInterfaceDataChannelRead::SpawnConditional, which checks to see if there is any data to be read from the data channel, then creates a spawn info for each instance of data. There are other mechanisms for conditional spawning, with the ability to accumulate or override the number of particles to spawn for each spawn info. The conditional logic can be used to control things like only spawning from specific surfaces, and the accumulation overrides can be used to chain multiple spawn calls together. For example, having a system that spawns extra particles, but only for a given surface.

In NS\_ImpactDataChannel the module NM\_ImpactSpawnDataChannel takes a Min and Max particle count and spawns the burst regardless of the surface, since the behavior is largely the same for both surfaces. NE\_ImpactSparksConcrete on the other hand, only spawns from concrete impacts, so it uses NM\_SpawnDataChannelConditional to specify a surface type that it should spawn on. Two or more instances of NM\_SpawnDataChannelConditional could be used in conjunction to filter the particles to multiple surfaces, or a custom module could be written that has more complex behavior.

#### Reading from Data Channels

For impacts, the Data Channel data is meant to initialize particles, and is read once in the Particle Spawn script stage with the NM\_ImpactReadDataChannel module. NM\_ImpactReadDataChannel recreates NM\_ImpactSpawnAttributes, just with a different source for its data. It uses the Data Channel Interface stored in the spawn module to read the data using the spawn group as the index. When the particles are spawned with Spawn Conditional it sets their spawn group to correspond to the index of their data in the Data Channel. When reading the data back, it returns a bool if the read was successful, so the module selects from default data, or the data read from the Data Channel based on this.

Instead of using the spawn index, we have now added Get NDCSpawn Data on the Data Channel Reader data interface, that lets you retrieve the Data Channel index based on the Emitter and Particle's exec index when it spawned.

## Profiling Results

It's important to validate performance changes to ensure they meet expectations. In the case of Data Channels vs Arrays both approaches should be fairly performant, with Data Channels likely outperforming arrays with respect to spawning systems, and arrays potentially outperforming Data Channels in simulation cost, since the array systems are less complicated. However, since the array approach used two systems instead of one, there may be less overhead with a combined system if both surface types occur with a similar frequency. Additionally comparing both methods could uncover further optimization opportunities.

For these comparisons we will look at the spawn costs and systems costs. The captures were taken from a Development build of Lyra, and an elimination game with bots was captured using insights.

### Spawning Performance

![Timing info for spawning impacts using arrays](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d7730ea3-683e-4d52-ad18-cea4927a9902/niagara-sas-1.png)

Spawning particles from arrays had an average timing of .17ms, which is fairly performant. Based on the profiling, though Spawn System At Location was called about 50% of the time, which likely indicates the distance threshold for creating a new system is too small, and we could avoid spawning as many systems with a larger distance threshold.

![Timing info for spawning impacts from Data Channels](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4f409341-3b02-4b54-9668-cf115620f06a/niagara-sas-2.png)

Spawning from data channels had an average timing of .05ms, which is almost a 3.5 times speed up.

### Niagara System Performance

![Timing info for array based Niagara Systems](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4e1efc7a-5ab2-4cb5-adac-fa5e9ffdeada/niagara-sas-3.png)

Here is the performance characteristics of the Concrete impact Niagara system, with the overall timing of the glass impact system for comparison as well. Both average .02ms, but the count for concrete greatly exceeds that of glass. This could indicate an issue for merging the systems for data channels, if the overhead for merging glass impacts isn't outweighed by the speed up from reducing system instances, since there aren't many to reduce to begin with, but we pay the overhead with every impact.

It's worth noting that despite contributing less time on average per frame, the Niagara systems are run far more frequently than their spawning logic, so optimizations here could potentially have a greater impact on the average performance of the game. That being said reducing spikes in frame timing to something more consistent, and amortizing those costs over more frames will lead to more steady frame rates, so it may still be preferable to save on spawning costs at the expense of slightly heavier simulation costs.

![Timing info for Data Channel Impact System with default extents](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/172bf641-dd28-4c5e-91fc-92961fe6c844/niagara-sas-4.png)

Here is the breakdown for NS\_ImpactDataChannel. It's average timing is .03ms, which is less than the combined average of the array systems, but the imbalance of their frequency mean that its performance is about on par, if not a little less performant than before. This makes intuitive sense, since the system has more emitter instances and has more complicated logic for handling multiple surface types. It's also worth noting that the bounds of the systems used in the two approaches have vastly different characteristics.

For array spawning the distance threshold was 500 units, which caused more instances covering less volume each. This is a good case for culling unnecessary particles, but a bad case for instance counts. On the other hand for data channels, the extents were 5000 units on each axis, which lead to fewer instances covering more volume each, which has the inverse result of favoring culling less, and having fewer instances. It's possible, likely even, that some of the per-frame overhead for the NS\_ImpactDataChannel comes from running the simulation of many particles that are off screen.

For testing, I halved the extent values to 2500 for the data channels, causing the volume the cover to shrink by 8, and did another test.

![Timing info for Data Channel Impact System with smaller extents](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/66749994-f874-4ccd-b77a-f79eb4b54a4d/niagara-sas-5.png)

In this test their average frame time was .02ms, bringing it back in line with the averages seen in the array systems, and it's spawning characteristics didn't change. This seems to confirm that the original extents were too big, and couldn't leverage culling from scalability as well. There are likely further optimizations that can be done at the asset level for the system, and further tweaks could be made to the extents to optimize these times, but they are low enough already that further time spent is better focused elsewhere. This does demonstrate that consideration still needs to be taken when choosing the correct settings for data channels in your level.

---

## Fuente: .\docs-md-py\en-us\unreal-engine\nintendo-switch-2.md

# Nintendo Switch 2

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/nintendo-switch-2

> Application Version: 5.7

Get started developing for Nintendo Switch 2 with Unreal Engine.

Access to the Unreal Engine Nintendo Switch 2 documentation is available without additional cost or licensing to any Unreal Engine developer who has met all NDA requirements and been granted the necessary permissions.

To gain access to Nintendo Switch 2 documentation:

- If your company has already completed the console request process, ask your administrator to grant you Nintendo Switch 2 access from the **Unreal Engine > Consoles** page on the [Epic Developer Portal](https://dev.epicgames.com/portal).
- If your company or you have not already begun the console request process then submit a **first time** or **additional access** request at [forms.unrealengine.com/s/form-console-access-request](https://forms.unrealengine.com/s/form-console-access-request). You will need to provide confirmation of you or your company’s approved Nintendo Switch 2 developer status and may need to accept an Epic Games Console NDA. Epic staff will guide you through the process.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Console documentation is not currently provided on the UE documentation site. Instead it is available for download from a <a href=\"https://forums.unrealengine.com/t/getting-started-with-switch-2/2541621\">thread on the private Switch 2 Development forum</a> for Unreal Engine.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

---

## Fuente: .\docs-md-py\en-us\unreal-engine\nne-denoiser-in-unreal-engine.md

# NNE Denoiser

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/nne-denoiser-in-unreal-engine

> Application Version: 5.7

The **NNE Denoiser** is a path tracer denoiser that allows importing and running custom neural denoiser networks through the NNE runtimes. Models are imported as regular **UNNEModelData** assets and the denoising inference can be run on CPU, GPU or RDG depending on the capabilities of the selected runtime.

The plugin ships with different versions of Intel’s Open Image Denoiser (fast, balanced and high quality, each with and without alpha) that can be used instead of a custom model.

## Changing Presets

The NNEDenoiser plugin settings allow the user to select a denoiser asset for spatial denoising, whether they are run on CPU, GPU or RDG and which runtime to be used. To let the path tracer use the neural networks defined in these settings, you need to set `r.PathTracing.Denoiser.Name` to `NNEDenoiser`.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/500d1395-dddc-4e64-b59f-158a47266f6b/nned-1.png)

### Denoiser Asset

Models together with their input and output mapping are described inside data assets. Changing the data asset will change the model to be used for denoising.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5606004a-ea2e-4a79-964b-0e1648ebdb58/nned-2.png)

Make sure that both checkboxes for **Show Engine Content** and **Show Plugin Content** are ticked inside the **Browse Settings** (the gear icon), if the assets for Intel’s Open Image Denoiser do not show up in the drop down.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f66dd1c6-65fc-42ef-bc8f-f47f8dcd0433/nned-3.png)

### Runtime Type

This dropdown defines where the denoising will be done. Depending on the runtime selected and whether it is available on the current platform or not, different options will work or not. Please refer to the capabilities of the individual runtimes to see what configurations are valid.

#### CPU

This will copy the noisy results to CPU, run inference there, and upload results back to the GPU. Note that the two device copies can slow down the denoising.

#### GPU

This will copy the noisy results to CPU, pass it to the runtime, which will copy it to GPU for inference and back, so it will finally be copied to GPU again.

Due to the 4 device copies, it is not recommended to use this setting, unless there is no other runtime available to run the model, or running the model on CPU is slower.

#### RDG

This setting is the most efficient, since the noisy image is denoised on device, without copying to CPU. It is the recommended setting if a corresponding runtime is available.

### Runtime Name Override

This field can be used to override the NNE runtime that is used. Please refer to the individual runtimes for the names to be used here. Also note that the plugin containing the runtime must be enabled manually to make it work. Additionally, the runtime selected must be compatible with the **Runtime Type** and able to run the selected model.

## Custom Neural Denoiser Networks

To use a custom neural network as denoiser, a neural network model, the definition of input and output mappings as well as a NNEDenoiser asset are needed.

### Model

A neural network can simply be added by dragging and dropping a neural network file into the content editor, which will create a **UNNEModelData** asset. Please note that different runtimes support different file formats. The runtime that supports the format needs to be enabled to be able to import the neural network successfully.

### Input/Output Mapping

A neural network can have multiple input and output tensors and each tensor can have multiple channels. To map the data provided by the path tracer (for example, Color, Normal, Albedo, and so on) to the input tensors and channels of the neural network, a mapping file needs to be defined.

To create a new mapping:

1. Right-click in the content window of the editor and select **Data Table** from the **Miscellaneous** menu.
2. Search in the opening dialogue for **NNEDenoiserInputMappingData** and select it.
3. For each channel of each input tensor of the neural network, add a new line for each.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/462509d0-e430-4e8f-a9ea-2347cbb1ecc1/nned-4.png)

Similarly, another asset for defining the output mappings can be created.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/50fceaac-515d-48e8-baa4-1c2dc97e06c9/nned-5.png)

| Property | Description |
| --- | --- |
| **Row Name Selection Box** | This is an arbitrary name that you can choose to describe your model input channel. It does not have to relate to the actual input name of the model. |
| **Resource** | The resource indicates from which path tracer resource the data is mapped from. |
| **Frame Index** | This index defines from which frame the path tracer data is mapped from. Index 0 will take the data from the current frame, negative numbers will map data from previous frames while positive indices will access future frames. |
| **Tensor Index** | This is the index of the input tensor of the model. Index i will map the data to the i-th input tensor of the model. |
| **Tensor Channel** | This is the index of the channel of the input tensor of the model. Index i will map the data to the i-th channel of the input tensor of the model. |
| **Resource Channel** | This is the index of the channel of the path tracer resource. Index i will map the data from the i-th channel of the path tracer resource. |

### Asset

NNEDenoiser assets define a model, input and output mappings as well as tiling configurations and are then used in the plugin settings to select which model will be used by the path tracer. To create a new custom asset right click into the content window of the editor, select Miscellaneous and then Data Asset. Search in the opening dialogue for NNEDenoiser Asset and select it. Select the model you imported and the mappings you defined in the corresponding dropdowns.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fe1c766e-99b9-44a9-b91a-1bd5c8cfb203/nned-6.png)

Then define the tiling configuration according to your model characteristics.

| Property | Description |
| --- | --- |
| **Size Alignment** | Tile sizes are chosen so that they are divisible by this number. Some operators of some runtimes can run faster if certain alignment criteria are met. This only has an effect if the model supports dynamic sizes. |
| **Overlap** | Defines how much neighboring tiles need to overlap to account for the receptive field of the model. This is defined by the radius of pixels in the input that contribute to an output pixel. |
| **Max Size** | The maximum size of each tile. This only has an effect if the model supports dynamic sizes. |
| **Min Size** | The minimum size of each tile. This only has an effect if the model supports dynamic sizes. |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-absolute.md

# Absolute

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Absolute

> Application Version: 5.7

### Description

Returns the absolute (positive) value

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Absolute,Abs,Neg |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-accumulateadd.md

# AccumulateAdd

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateAdd

> Application Version: 5.7

### Description

Adds a value over time over and over again
Adds a vector over time over and over again

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Accumulate |
| Tags | AccumulateAdd,Accumulate Add (Float),Simulate,++,Accumulate Add (Vector) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Increment | The increment to add for every iteration | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| InitialValue | The initial value to start at | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| bIntegrateDeltaTime | If True the integration will be relying on the delta time to create more deterministic results with varying framerates. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting accumulated value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-accumulatedtime.md

# Accumulated Time

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulatedTime

> Application Version: 5.7

### Description

Simulates a time value - can act as a timeline playing back

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Accumulate |
| Tags | Playback,Pause,Timeline |
| Type | [FRigVMFunction\_Timeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_Timeline) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Speed | The speed to apply to the played back time | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Time | The played back / accumulated time in seconds | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-accumulatelerp.md

# AccumulateLerp

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateLerp

> Application Version: 5.7

### Description

Interpolates two values over time over and over again
Interpolates two vectors over time over and over again
Interpolates two quaternions over time over and over again
Interpolates two transforms over time over and over again

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Accumulate |
| Tags | AccumulateLerp,Accumulate Lerp (Float),Simulate,Ramp,Accumulate Lerp (Vector),Accumulate Lerp (Quaternion),Accumulate Lerp (Transform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TargetValue | The target value to interpolate towards | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| InitialValue | The initial value to start at | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| Blend | The blend to use for the interpolation. This value may be scaled down based on the Integrate Delta Time setting | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bIntegrateDeltaTime | If True the integration will be relying on the delta time to create more deterministic results with varying framerates. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting accumulated value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-accumulatemul.md

# AccumulateMul

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateMul

> Application Version: 5.7

## AccumulateMul ()

Multiplies a value over time over and over again
Multiplies a vector over time over and over again

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Accumulate |
| Tags | AccumulateMul,Accumulate Mul (Float),Simulate,\*\*,Accumulate Mul (Vector) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Multiplier | The multiplier to apply for every iteration | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1.000000 |
| InitialValue | The initial value to start at | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1.000000 |
| bIntegrateDeltaTime | If True the integration will be relying on the delta time to create more deterministic results with varying framerates. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting accumulated value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

## AccumulateMul ()

Multiplies a quaternion over time over and over again
Multiplies a transform over time over and over again

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Accumulate |
| Tags | AccumulateMul,Accumulate Mul (Quaternion),Simulate,\*\*,Accumulate Mul (Transform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Multiplier | The multiplier to apply for every iteration | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| InitialValue | The initial value to start at | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| bFlipOrder | If True the multiplier will be pre-multiplied, otherwise post-multiplied | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bIntegrateDeltaTime | If True the integration will be relying on the delta time to create more deterministic results with varying framerates. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting accumulated value | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-accumulaterange.md

# AccumulateRange

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateRange

> Application Version: 5.7

### Description

Accumulates the min and max values over time

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Accumulate |
| Tags | AccumulateRange,Accumulate Range (Float),Range,Accumulate Range (Vector) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value to accumulate the min and max value of | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Minimum | The accumulated minimum value of the input | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Maximum | The accumulated maximum value of the input | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-acos.md

# Acos

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Acos

> Application Version: 5.7

### Description

Returns the inverse cosinus value (in radians) of the given value

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Acos,Arccos |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-add.md

# Add

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Add

> Application Version: 5.7

## Add ()

Returns the sum of the two values

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Add,Sum,+ |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first color for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=0.000000,A=1.000000) |
| B | The second color for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=0.000000,A=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting color | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) |  |

## Add (FRigVMDispatch\_ArrayAdd)

Adds an element to an array and returns the new element's index.
Modifies the input array.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayAdd](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayAdd) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Array | The array to add an element to. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Element | The element to add to the array. | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Index | The index of the newly added element. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-adddeformer.md

# Add Deformer

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AddDeformer

> Application Version: 5.7

### Description

Adds a deformer to the Skeletal Mesh Component

### Information

|  |  |
| --- | --- |
| Module | [OptimusCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OptimusCore) |
| Category | Deformer Graph |
| Type | FRigUnit\_AddOptimusDeformer |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-addmultipletags.md

# Add Multiple Tags

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AddMultipleTags

> Application Version: 5.7

### Description

Sets multiple tags on an item

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | AddTags,MetadataExists,HasKey,Tagging,FindTag,SetTags |
| Type | [FRigUnit\_SetMetadataTagArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetMetadataTagArray) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to set the metadata for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Tags | The tags to set for the item | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)> | () |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-addspaces.md

# Add Spaces

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AddSpaces

> Application Version: 5.7

### Description

Adds available spaces for a given control. This is used for the space switching widget.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Children,AddParent,Constraint,Space |
| Type | [FRigUnit\_AddAvailableSpaces](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AddAvailableSpaces) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The available spaces to add for a given control | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| Spaces | The spaces to add | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKeyWithLabel](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKeyWithLabel)> | ((Key=(Type=Control))) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-addtag.md

# Add Tag

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AddTag

> Application Version: 5.7

### Description

Sets a single tag on an item

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | MetadataExists,HasKey,Tagging,FindTag,SetTag |
| Type | [FRigUnit\_SetMetadataTag](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetMetadataTag) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to set the metadata for | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Tag | The name of the tag to set | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-aim.md

# Aim

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Aim

> Application Version: 5.7

### Description

Aligns the rotation of a primary and secondary axis of an item to a global target.
Note: This node operates in global space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Lookat |
| Type | [FRigUnit\_AimItem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimItem) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The name of the item to align | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Primary | The primary target for the aim | [Rig Unit Aim Item Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimItem_Target) | (Weight=1.000000,Axis=(X=1.000000,Y=0.000000,Z=0.000000),Target=(X=1.000000,Y=0.000000,Z=0.000000),Kind=Location,Space=(Type=Bone,Name="")) |
| Secondary | The secondary target for the aim - also referred to as PoleVector / UpVector | [Rig Unit Aim Item Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimItem_Target) | (Weight=1.000000,Axis=(X=0.000000,Y=0.000000,Z=1.000000),Target=(X=1.000000,Y=0.000000,Z=0.000000),Kind=Location,Space=(Type=Bone,Name="")) |
| Weight | The weight of the change - how much the change should be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| DebugSettings | The debug setting for the node | [Rig Unit Aim Bone Debug Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimBone_DebugSettings) | (bEnabled=False,Scale=10.000000,WorldOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-aimconstraint.md

# Aim Constraint

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AimConstraint

> Application Version: 5.7

### Description

Orients an item such that its aim axis points towards a global target.
Note: This node operates in global space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Constraints |
| Tags | Lookat, Aim |
| Type | [FRigUnit\_AimConstraintLocalSpaceOffset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimConstraintLocalSpace-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The name of the item to apply aim | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |
| bMaintainOffset | Maintains the offset between child and weighted average of parents based on initial transforms | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Filter | Filters the final rotation by axes based on the euler rotation order defined in the node's advanced settings If flipping is observed, try adjusting the rotation order | [Filter Option Per Axis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FFilterOptionPerAxis) | (bX=True,bY=True,bZ=True) |
| AimAxis | Child is rotated so that its AimAxis points to the parents | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| UpAxis | Child is rotated around the AimAxis so that its UpAxis points to/Aligns with the WorldUp target | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| WorldUp | Defines how Child should rotate around the AimAxis. This is the aim target for the UpAxis | [Rig Unit Aim Constraint World Up](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimConstraint_WorldUp) | (Target=(X=0.000000,Y=0.000000,Z=1.000000),Kind=Direction,Space=(Type=None,Name="")) |
| Parents | The array of parents to constaint this aim to | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FConstraintParent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FConstraintParent)> | (()) |
| AdvancedSettings | The advanced settings to use for the constraint | [Rig Unit Aim Constraint Advanced Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimConstraint_AdvancedS-) | (DebugSettings=(bEnabled=False,Scale=10.000000,WorldOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))),RotationOrderForFilter=XZY) |
| Weight | The weight to use when applying the resulting transform to the child | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-aimmath.md

# Aim Math

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AimMath

> Application Version: 5.7

### Description

Outputs an aligned transform of a primary and secondary axis of an input transform to a world target.
Note: This node operates in world space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Lookat |
| Type | [FRigUnit\_AimBoneMath](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimBoneMath) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InputTransform | The transform (in global space) before the aim was applied (optional) | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Primary | The primary target for the aim | [Rig Unit Aim Item Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimItem_Target) | (Weight=1.000000,Axis=(X=1.000000,Y=0.000000,Z=0.000000),Target=(X=1.000000,Y=0.000000,Z=0.000000),Kind=Location,Space=(Type=Bone,Name="")) |
| Secondary | The secondary target for the aim - also referred to as PoleVector / UpVector | [Rig Unit Aim Item Target](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimItem_Target) | (Weight=1.000000,Axis=(X=0.000000,Y=0.000000,Z=1.000000),Target=(X=1.000000,Y=0.000000,Z=0.000000),Kind=Location,Space=(Type=Bone,Name="")) |
| Weight | The weight of the change - how much the change should be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| DebugSettings | The debug setting for the node | [Rig Unit Aim Bone Debug Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimBone_DebugSettings) | (bEnabled=False,Scale=10.000000,WorldOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting transform | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-alphainterp.md

# AlphaInterp

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AlphaInterp

> Application Version: 5.7

### Description

Takes in a float value and outputs an accumulated value with a customized scale and clamp
Takes in a vector value and outputs an accumulated value with a customized scale and clamp
Takes in a quaternion value and outputs an accumulated value with a customized scale and clamp

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Time |
| Tags | AlphaInterp,Alpha Interpolate,Alpha,Lerp,LinearInterpolate |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value to interpolate | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| Scale | The scale to apply to the interpolation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Bias | The bias to use for the interpolation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bMapRange | If True the input value will be mapped using the min and max range | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| InRange | The minimum and maximum for the input range | [Input Range](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FInputRange) | (Min=0.000000,Max=1.000000) |
| OutRange | The minimum and maximum for the output range | [Input Range](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FInputRange) | (Min=0.000000,Max=1.000000) |
| bClampResult | If True the output value will be clamped by the min and max | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ClampMin | The minimum for the output's clamp range | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| ClampMax | The maximum for the output's clamp range | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bInterpResult | If True to the output result will be further intepolated | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| InterpSpeedIncreasing | The output interpolation increasing speed | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| InterpSpeedDecreasing | The output interpolation decreasing speed | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting interpolated value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-and.md

# And

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/And

> Application Version: 5.7

### Description

Returns true if both conditions are true

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Boolean |
| Tags | && |
| Type | [FRigVMFunction\_MathBoolAnd](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoolAnd) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first value for the operation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| B | The second value for the operation | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting value | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-anglebetween.md

# Angle Between

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AngleBetween

> Application Version: 5.7

### Description

Returns the angle between two vectors in radians

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Type | [FRigVMFunction\_MathVectorAngle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathVectorAngle) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first vector to measure the angle between | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| B | The second vector to measure the angle between | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The angle between A and B in radians | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-append.md

# Append

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Append

> Application Version: 5.7

### Description

Appends the another array to the main one.
Modifies the input array.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayAppend](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayAppend) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Array | The array to append the other array to. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Other | The second array to append to the first one. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-applyposecache.md

# Apply Pose Cache

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ApplyPoseCache

> Application Version: 5.7

### Description

Sets the hierarchy's pose

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State |
| Type | [FRigUnit\_HierarchySetPoseItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchySetPoseItemArr-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The pose to apply to the hierarchy | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |
| ElementType | The types of element to apply the pose for | [Rig Element Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigElementType) | All |
| Space | The space to use to apply the pose in | [Rig VMTransform Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | LocalSpace |
| ItemsToSet | An optional collection to filter against | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Weight | The weight to use when applying the transforms | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-arrayaverage.md

# ArrayAverage

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ArrayAverage

> Application Version: 5.7

### Description

Returns the average of the given array

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | ArrayAverage,Array Average |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | The array of numbers to average | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Average | The resulting average | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-arraysum.md

# ArraySum

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ArraySum

> Application Version: 5.7

### Description

Returns the sum of the given array

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | ArraySum,Array Sum |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | The array of numbers to add up | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)>   [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Sum | The resulting sum of all numbers | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-asin.md

# Asin

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Asin

> Application Version: 5.7

### Description

Returns the inverse sinus value (in radians) of the given value

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Asin,Arcsin |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-at.md

# At

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/At

> Application Version: 5.7

### Description

Returns an element of an array by index.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | Get Index,At Index,[] |
| Type | [FRigVMDispatch\_ArrayGetAtIndex](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayGetAtIndex) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | The array to retrieve an element from. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |
| Index | The index of the element to retrieve. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Element | The element at the given index. | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-atan.md

# Atan

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Atan

> Application Version: 5.7

### Description

Returns the inverse tangens value (in radians) of the given value

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Atan,Arctan |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-atan2.md

# Atan2

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Atan2

> Application Version: 5.7

### Description

Returns the arctangent of the specified A and B coordinates.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Atan2,Arctan |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first number for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |
| B | The second number for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting number | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-axis.md

# Axis

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Axis

> Application Version: 5.7

### Description

Extracts an axis from a quaternion rotation

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Quaternion |
| Tags | GetAxis,xAxis,yAxis,zAxis |
| Type | [FRigVMFunction\_MathQuaternionGetAxis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathQuaternionGet-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Quaternion | The input quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| Axis | The axis to extract | [Axis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/EAxis__Type) | X |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting extracted axis | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-backwardssolve.md

# Backwards Solve

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/BackwardsSolve

> Application Version: 5.7

### Description

Event for driving elements based off the skeleton hierarchy

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Events |
| Tags | Inverse,Reverse,Backwards,Event |
| Type | [FRigUnit\_InverseExecution](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_InverseExecution) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | The execution result | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-basicfabrik.md

# Basic FABRIK

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicFABRIK

> Application Version: 5.7

### Description

The FABRIK solver can solve N-Bone chains using
the Forward and Backward Reaching Inverse Kinematics algorithm.
For now this node supports single effector chains only.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | N-Bone,IK |
| Type | [FRigUnit\_FABRIKItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_FABRIKItemArray) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The chain to use | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| EffectorTransform | The transform of the effector in global space | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Precision | The precision to use for the fabrik solver | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Weight | The weight of the solver - how much the IK should be applied. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bPropagateToChildren | If set to true all of the global transforms of the children of this bone will be recalculated based on their local transforms. Note: This is computationally more expensive than turning it off. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| MaxIterations | The maximum number of iterations. Values between 4 and 16 are common. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| bSetEffectorTransform | The option to set the effector transform | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-basicik.md

# Basic IK

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIK

> Application Version: 5.7

### Description

Solves the two bone IK given two bones.
Note: This node operates in world space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | TwoBone,IK |
| Type | [FRigUnit\_TwoBoneIKSimplePerItem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_TwoBoneIKSimplePerItem) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ItemA | The name of first item | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| ItemB | The name of second item | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| EffectorItem | The name of the effector item (if exists) | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Effector | The transform of the effector | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| PrimaryAxis | The major axis being aligned - along the item | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| SecondaryAxis | The minor axis being aligned - towards the polevector | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=1.000000,Z=0.000000) |
| SecondaryAxisWeight | Determines how much the secondary axis roll is being applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| PoleVector | The polevector to use for the IK solver This can be a location or direction. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| PoleVectorKind | The kind of pole vector this is representing - can be a direction or a location | [Control Rig Vector Kind](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/EControlRigVectorKind) | Direction |
| PoleVectorSpace | The space in which the pole vector is expressed | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bEnableStretch | If set to true the stretch feature of the solver will be enabled | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| StretchStartRatio | The ratio where the stretch starts | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.750000 |
| StretchMaximumRatio | The maximum allowed stretch ratio | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.250000 |
| Weight | The weight of the solver - how much the IK should be applied. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| ItemALength | The length of the first item. If set to 0.0 it will be determined by the hierarchy | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| ItemBLength | The length of the second item. If set to 0.0 it will be determined by the hierarchy | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bPropagateToChildren | If set to true all of the global transforms of the children of this bone will be recalculated based on their local transforms. Note: This is computationally more expensive than turning it off. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugSettings | The settings for debug drawing | [Rig Unit Two Bone IKSimple Debug Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_TwoBoneIKSimple_DebugSe-) | (bEnabled=False,Scale=10.000000,WorldOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-basicikpositions.md

# Basic IK Positions

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIKPositions

> Application Version: 5.7

### Description

Solves the two bone IK given positions
Note: This node operates in world space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | TwoBone,IK |
| Type | [FRigUnit\_TwoBoneIKSimpleVectors](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_TwoBoneIKSimpleVectors) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Effector | The position of the effector | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Root | The position of the root of the triangle | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| PoleVector | The position of the pole of the triangle | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| bEnableStretch | If set to true the stretch feature of the solver will be enabled | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| StretchStartRatio | The ratio where the stretch starts | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.750000 |
| StretchMaximumRatio | The maximum allowed stretch ratio | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.250000 |
| BoneALength | The length of the first bone. If set to 0.0 it will be determined by the hierarchy | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| BoneBLength | The length of the second bone. If set to 0.0 it will be determined by the hierarchy | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Elbow | The resulting elbow position | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-basiciktransforms.md

# Basic IK Transforms

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIKTransforms

> Application Version: 5.7

### Description

Solves the two bone IK given transforms
Note: This node operates in world space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | TwoBone,IK |
| Type | [FRigUnit\_TwoBoneIKSimpleTransforms](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_TwoBoneIKSimpleTransfor-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Root | The transform of the root of the triangle | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Effector | The transform of the effector | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Elbow | The resulting elbow transform | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PoleVector | The position of the pole of the triangle | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| PrimaryAxis | The major axis being aligned - along the bone | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| SecondaryAxis | The minor axis being aligned - towards the polevector | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=1.000000,Z=0.000000) |
| SecondaryAxisWeight | Determines how much the secondary axis roll is being applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bEnableStretch | If set to true the stretch feature of the solver will be enabled | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| StretchStartRatio | The ratio where the stretch starts | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.750000 |
| StretchMaximumRatio | The maximum allowed stretch ratio | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.250000 |
| BoneALength | The length of the first bone. If set to 0.0 it will be determined by the hierarchy | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| BoneBLength | The length of the second bone. If set to 0.0 it will be determined by the hierarchy | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-boxfromarray.md

# Box from Array

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/BoxfromArray

> Application Version: 5.7

### Description

Returns bounding box of the given array of positions

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Box |
| Tags | ArrayBounds,CreateBox,CreateBoundingBox,NewBox,NewBoundingBoxMakeBox,MakeBoundingBox,BoundingBox,Bbox,Bounds |
| Type | [FRigVMFunction\_MathBoxFromArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoxFromArray) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | The array of input positions | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | The resulting bounding box | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Minimum | The resulting minimum value of the bounding box | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Maximum | The resulting maximum value of the bounding box | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Center | The resulting center value of the bounding box | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Size | The resulting size value of the bounding box | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-branch.md

# Branch

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Branch

> Application Version: 5.7

### Description

Executes either the True or False branch based on the condition

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Execution |
| Tags | If |
| Type | [FRigVMFunction\_ControlFlowBranch](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_ControlFlowBranch) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | The input execution pin to hook up to the graph | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Condition | The condition based on which to pick between the True and False branches | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| True | The branch to run if the condition is True | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| False | The branch to run if the condition is False | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Completed | The execute flow to run when the True or False branch is complete | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-break.md

# Break

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Break

> Application Version: 5.7

### Description

Decomposes a struct into its elements

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core |
| Tags | Decompose,Decomposition |
| Type | [FRigVMDispatch\_BreakStruct](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_BreakStruct) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Struct | The structure to break up into its elements | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Elements | The elements of the structure | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-calculatephysicscollision.md

# Calculate Physics Collision

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CalculatePhysicsCollision

> Application Version: 5.7

### Description

Discards any existing collision data and replaces it with a box based on the joint positions.
Note that this must be called before the physics solver is instantiated/stepped.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchyAutoCalculateCollision](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchyAutoCalculateC-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| MinAspectRatio | For boxes: The minimum box extent, as a proportion of the maximum box extent. For capsules: The minimum radius, as a proportion of the length (not including the radius) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.250000 |
| MinSize | For boxes: The minimum side length. For capsules: The minimum radius | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-cast.md

# Cast

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast

> Application Version: 5.7

## Cast ()

Turns the given bool into a float value
Turns the given bool into an integer value
Makes a color from a single float
Makes a color from a single double
Returns the double cast to an int (this uses floor)
Returns the double cast to a float
Returns the float cast to an int (this uses floor)
Returns the float cast to a double
Returns the int cast to a float
Returns the int cast to a double
Makes a transform from a matrix
Makes a matrix from a transform
Makes a quaternion from a rotator
Retrieves the rotator
Makes a quaternion based transform from a euler based transform
Retrieves a euler based transform from a quaternion based transform
Makes a vector from a single float
Makes a vector from a single double
Casts the provided item key to its name

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Tags | Cast,To Float,To Integer,From Float,Make,Construct,From Double,To Int,To Double,To Transform,From Transform,From Rotator,To Rotator,To Euler Transform,To Name,Engine Test Rig VM Custom Type from Int,Engine Test Rig VM Custom Type to Int |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The bool value to convert | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Matrix](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Euler Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FEulerTransform)   [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)   FEngineTest\_CustomType | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting float number (0 or 1) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor)   [Matrix](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Euler Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FEulerTransform)   FEngineTest\_CustomType |  |

## Cast (FRigVMDispatch\_CastEnumToInt)

Casts from enum to int

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Enum |
| Tags | As |
| Type | [FRigVMDispatch\_CastEnumToInt](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_CastEnumToInt) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The enum value to cast to an integer | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting integer value | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

## Cast (FRigVMDispatch\_CastIntToEnum)

Casts from int to enum

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Enum |
| Tags | As |
| Type | [FRigVMDispatch\_CastIntToEnum](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_CastIntToEnum) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The integer value to cast to an enum value | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting enum value | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

## Cast (FRigVMDispatch\_CastObject)

Casts between object types

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Object |
| Tags | As |
| Type | [FRigVMDispatch\_CastObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_CastObject) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The object to cast to a new type | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting cast object. This may be potentially nullptr as well if the cast was not successful. | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-ccdik.md

# CCDIK

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CCDIK

> Application Version: 5.7

### Description

The CCID solver can solve N-Bone chains using
the Cyclic Coordinate Descent Inverse Kinematics algorithm.
For now this node supports single effector chains only.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | N-Bone,IK |
| Type | [FRigUnit\_CCDIKItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CCDIKItemArray) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The chain to use | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| EffectorTransform | The transform of the effector in global space | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Precision | The precision to use for the fabrik solver | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Weight | The weight of the solver - how much the IK should be applied. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| MaxIterations | The maximum number of iterations. Values between 4 and 16 are common. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| bStartFromTail | If set to true the direction of the solvers is flipped. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| BaseRotationLimit | The general rotation limit to be applied to bones | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 30.000000 |
| RotationLimits | Defines the limits of rotation per bone. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_CCDIK\_RotationLimitPerItem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CCDIK_RotationLimitPerI-)> | () |
| bPropagateToChildren | If set to true all of the global transforms of the children of this bone will be recalculated based on their local transforms. Note: This is computationally more expensive than turning it off. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-ceiling.md

# Ceiling

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Ceiling

> Application Version: 5.7

## Ceiling ()

Returns the closest higher full number (integer) of the value

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Ceiling,Round |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value to apply the ceiling to | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting closest higher full number (integer) of the input value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |
| Int | The result as an integer value | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

## Ceiling (FRigVMFunction\_MathVectorCeil)

Returns the closest higher full number (integer) of the value for each component

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Tags | Round |
| Type | [FRigVMFunction\_MathVectorCeil](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathVectorCeil) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-chainharmonics.md

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

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-chaininfo.md

# Chain Info

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ChainInfo

> Application Version: 5.7

### Description

Retrieves various pieces of info about an interpolated transform hierarchy from an rig element item list

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Chain |
| Type | [FRigUnit\_ChainInfo](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ChainInfo) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items to use to interpret the chain | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Param | The parameter value down the chain of items from 0 to 1 | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bCalculateStretch | If True calculate stretch factors of chain and current segment | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bInitial | If True use initial transform values for chain | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bDebug | Enable debug draw for node | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DebugScale | Debug draw scale | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InterpolatedTransform | The interpolated transform at the chain's input parameter | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| ChainLength | The length of the interpolated chain | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| ParamLength | The parametric length of the interpolated chain | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| ChainStretchFactor | Stretch factor of chain | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| SegmentInfo | Segment Info | [Rig Unit Chain Info Segment Info](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ChainInfo_SegmentInfo) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-chop.md

# Chop

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Chop

> Application Version: 5.7

### Description

Returns the left or right most characters from the name chopping the given number of characters from the start or the end
Returns the left or right most characters from the string chopping the given number of characters from the start or the end

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core |
| Tags | Chop,Truncate,-,Remove,Subtract,Split |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The input name to chop | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | None |
| Count | Number of characters to remove from left or right | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |
| FromEnd | if set to true the characters will be removed from the end | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Remainder | the part of the name without the chopped characters | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Chopped | the part of the name that has been chopped off | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-clamp.md

# Clamp

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Clamp

> Application Version: 5.7

### Description

Clamps the given value within the range provided by minimum and maximum
Clamps the given value within the range provided by minimum and maximum for each component

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Clamp,Range,Remap |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The number to clamp | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| Minimum | The Minimum for the resulting range | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| Maximum | The Maximum for the resulting range | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting clamped value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-clamplength.md

# ClampLength

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ClampLength

> Application Version: 5.7

### Description

Clamps the length of a given vector between a minimum and maximum

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Tags | Unit,Normalize,Scale |
| Type | [FRigVMFunction\_MathVectorClampLength](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathVectorClampLe-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input vector to clamp the length of | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| MinimumLength | The minimum length to clamp by | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaximumLength | The maximum length to clamp by | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting clamped input vector \* (or 0,0,0 in case the input was also 0,0,0) | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-clampspatially.md

# ClampSpatially

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ClampSpatially

> Application Version: 5.7

### Description

Clamps a transform's position using a plane collision, cylindric collision or spherical collision.
Clamps a position using a plane collision, cylindric collision or spherical collision.
The collision happens both towards an inner envelope (minimum) and towards an outer envelope (maximum).
You can disable the inner / outer envelope / collision by setting the minimum / maximum to 0.0.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | ClampSpatially,Clamp Spatially,Collide,Collision |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input transform to clamp | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Axis | The axis to use for the filter | [Axis](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/EAxis__Type) | X |
| Type | The filter / spatial mode to use | [Rig VMClamp Spatial Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMClampSpatialMode__Type) | Plane |
| Minimum | The minimum allowed distance at which a collision occurs. Note: For capsule this represents the radius. Disable by setting to 0.0. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Maximum | This maximum allowed distance. A collision will occur towards the center at this wall. Note: For capsule this represents the length. Disable by setting to 0.0. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 100.000000 |
| Space | The space this spatial clamp happens within. The input position will be projected into this space. | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bDrawDebug | Draws debug information if True | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DebugColor | The color to use for the debug draw | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| DebugThickness | The thickness to use for the debug draw | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting transform with a clamped position | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-clone.md

# Clone

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Clone

> Application Version: 5.7

### Description

Clones an array and returns a duplicate.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayClone](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayClone) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | The array to clone | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Clone | The duplicate of the input array. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-closestparameterfromspline.md

# Closest Parameter From Spline

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ClosestParameterFromSpline

> Application Version: 5.7

### Description

Retrieves the closest U value from a given Spline and a position

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Type | [FRigUnit\_ClosestParameterFromControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_ClosestParameterFromCon-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The spline to evaluate | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| Position | The position to evaluate | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| U | The U value at the closest location on the spline | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-collectionfromitems.md

# Collection from Items

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CollectionfromItems

> Application Version: 5.7

### Description

Returns a collection provided a specific array of items.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Items|Collections |
| Tags | Collection,Array |
| Type | [FRigUnit\_CollectionItems](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CollectionItems) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The input array of items | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | ((Type=Bone)) |
| bAllowDuplicates | If True the collection may contain duplicates | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | The resulting collection | [Rig Element Key Collection](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKeyCollection) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-concat.md

# Concat

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Concat

> Application Version: 5.7

### Description

Concatenates two names together to make a new name
Concatenates two strings together to make a new string

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core |
| Tags | Concat,Add,+,Combine,Merge,Append |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first / left name to concatenate | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | None |
| B | The second / right name to concatenate | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting concatenated name | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-connector.md

# Connector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Connector

> Application Version: 5.7

### Description

Event for filtering connection candidates

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Events |
| Tags | Event,During,Resolve,Connect,Filter |
| Type | [FRigUnit\_ConnectorExecution](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ConnectorExecution) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | The execution result | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-constant.md

# Constant

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Constant

> Application Version: 5.7

### Description

Provides a constant value to the graph

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core |
| Tags | Value,Reroute |
| Type | [FRigVMDispatch\_Constant](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_Constant) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The constant value defined in this node | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-constructionevent.md

# Construction Event

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ConstructionEvent

> Application Version: 5.7

### Description

Event to create / configure elements before any other event

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Events |
| Tags | Create,Build,Spawn,Setup,Init,Fit |
| Type | [FRigUnit\_PrepareForExecution](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PrepareForExecution) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | The execution result | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-contains.md

# Contains

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Contains

> Application Version: 5.7

### Description

Returns true or false if a given name exists in another given name

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core |
| Tags | Contains,Find,Has,Search |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The input name to search within | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | None |
| Search | The name to search for | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if a given name exists in another given name | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-cos.md

# Cos

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Cos

> Application Version: 5.7

### Description

Returns the cosinus value of the given value (in radians)

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Cos |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-createparentrelationship.md

# Create Parent Relationship

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CreateParentRelationship

> Application Version: 5.7

### Description

Adds a new parent to an element. The weight for the new parent will be 0.0.
You can use the SetParentWeights node to change the parent weights later.

If you just want to add a space to a control you can use the 'Add Spaces' node.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Children,Parent,Constraint,Space,AddParent |
| Type | [FRigUnit\_AddParent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AddParent) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The child to be parented under the new parent | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| Parent | The new parent to be added to the child | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| DisplayLabel | The optional display label for the parent constraint / space | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-createposecache.md

# Create Pose Cache

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CreatePoseCache

> Application Version: 5.7

### Description

Creates the hierarchy's pose

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State,MakePoseCache,NewPoseCache,EmptyPoseCache |
| Type | [FRigUnit\_HierarchyCreatePoseItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyCreatePoseItem-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Entries | The entries to create | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_HierarchyCreatePoseItemArray\_Entry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyCreatePoseItem-_1)> | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The resulting pose | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-criticalspringdamp.md

# Critical Spring Damp

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CriticalSpringDamp

> Application Version: 5.7

### Description

Damps a float using a spring damper
Damps a vector using a spring damper
Damps a quaternion using a spring damper

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Damp|Experimental |
| Tags | Critical Spring Damp,Critical Spring Damp (Float),Critical Spring Damp (Vector),Critical Spring Damp (Quat) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value to damp | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| ValueVelocity | The velocity of the value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Target | The target to damp towards | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| SmoothingTime | The time to apply smoothing for | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.200000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-cross.md

# Cross

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Cross

> Application Version: 5.7

### Description

Returns the cross product between two vectors

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Tags | ^ |
| Type | [FRigVMFunction\_MathVectorCross](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathVectorCross) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first vector for the operation | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| B | The second vector for the operation | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting vector | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-curve.md

# Curve

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Curve

> Application Version: 5.7

### Description

Provides a constant curve to be used for multiple curve evaluations

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Animation |
| Tags | Curve,Profile |
| Type | [FRigVMFunction\_AnimRichCurve](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_AnimRichCurve) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Curve | The pass through animation rich curve | [Runtime Float Curve](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FRuntimeFloatCurve) | (EditorCurveData=(Keys=((),(Time=1.000000,Value=1.000000)),DefaultValue=340282346638528859811704183484516925440.000000,PreInfinityExtrap=RCCE\_Constant,PostInfinityExtrap=RCCE\_Constant),ExternalCurve=None) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-curveexists.md

# Curve Exists

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CurveExists

> Application Version: 5.7

### Description

CurveExists is used to check whether a curve exists or not.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Curve |
| Tags | CurveExists,bool |
| Type | [FRigUnit\_CurveExists](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CurveExists) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Curve | The name of the Curve to retrieve the transform for. | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Exists | Boolean indicating whether the named curve exists or not. Does not indicate whether the curve's value is valid or not. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-damp.md

# Damp

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Damp

> Application Version: 5.7

### Description

Damps a float value using exponential decay damping
Damps a vector value using exponential decay damping
Damps a quaternion value using exponential decay damping

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Damp|Experimental |
| Tags | Damp,Damp (Float),Damp (Vector),Damp (Quaternion) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value to damp | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| Target | The target value to damp towards | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| SmoothingTime | The time to apply smoothing for | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.200000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | Resulting damped value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-degrees.md

# Degrees

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Degrees

> Application Version: 5.7

### Description

Returns the degrees of a given value in radians

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Degrees |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-deltafromprevious.md

# DeltaFromPrevious

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DeltaFromPrevious

> Application Version: 5.7

### Description

Computes the difference from the previous value going through the node

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Time |
| Tags | DeltaFromPrevious,DeltaFromPrevious (Float),Difference,Velocity,Acceleration,DeltaFromPrevious (Vector),DeltaFromPrevious (Quaternion),DeltaFromPrevious (Transform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value to compute the delta of | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Delta | The resulting delta from the previous iteration | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| PreviousValue | The value from the previous iteration | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-deltatime.md

# Delta Time

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DeltaTime

> Application Version: 5.7

### Description

Returns the time gone by from the previous evaluation

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Animation |
| Type | [FRigVMFunction\_GetDeltaTime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_GetDeltaTime) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The current delta time in seconds | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-difference.md

# Difference

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Difference

> Application Version: 5.7

### Description

Creates a new array containing the difference between the two input arrays.
Difference here means elements that are only contained in either A or B.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayDifference](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayDifference) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | The first array to compare the other array with. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |
| Other | The second array to compare the other array with. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting difference array. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-disablecollisionbetween.md

# Disable Collision Between

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DisableCollisionBetween

> Application Version: 5.7

### Description

Disables collision between two bodies

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchyDisableCollisionBetween](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchyDisableCollisi-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey1 | Component key for the first body | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| PhysicsBodyComponentKey2 | Component key for the second body | [Rig Component Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-discardmatches.md

# Discard Matches

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DiscardMatches

> Application Version: 5.7

### Description

Discards matches during a connector event

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Modules |
| Tags | Connection,Resolve,Match |
| Type | [FRigUnit\_DiscardMatches](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_DiscardMatches) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Excluded | The items being interacted on | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Message | The message to send to the user interface when discarding matches | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-distancebetween.md

# Distance Between

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DistanceBetween

> Application Version: 5.7

### Description

Returns the distance from A to B

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Type | [FRigVMFunction\_MathVectorDistance](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathVectorDistanc-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first vector to measure the distance between | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| B | The second vector to measure the distance between | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The distance between the two vectors A and B | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-distancetoplane.md

# Distance To Plane

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DistanceToPlane

> Application Version: 5.7

### Description

Find the point on the plane that is closest to the given point and the distance between them.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Tags | Distance,Plane,Closest,Project |
| Type | [FRigVMFunction\_MathDistanceToPlane](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathDistanceToPla-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Point | The point to measure against the plane | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| PlanePoint | A point on the plane to measure agains | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| PlaneNormal | The normal of the plane to measure agains | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ClosestPointOnPlane | The resulting closest point on the plane | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| SignedDistance | The distance to the plane as a signed (positive or negative) value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-distributerotation.md

# Distribute Rotation

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DistributeRotation

> Application Version: 5.7

### Description

Distributes rotations provided across a array of items.
Each rotation is expressed by a quaternion and a ratio, where the ratio is between 0.0 and 1.0
Note: This node adds rotation in local space of each item!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | TwistBones |
| Type | [FRigUnit\_DistributeRotationForItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_DistributeRotationForIt-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items to use to distribute the rotation | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Rotations | The list of rotations to be applied | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_DistributeRotation\_Rotation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_DistributeRotation_Rota-)> | () |
| RotationEaseType | The easing to use between to rotations. | [Rig VMAnim Easing Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMAnimEasingType) | Linear |
| Weight | The weight of the solver - how much the rotation should be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-divide.md

# Divide

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Divide

> Application Version: 5.7

### Description

Returns the division of the two values

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Divide,Division,Divisor,/ |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first number for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| B | The second number for the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting number | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-dot.md

# Dot

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Dot

> Application Version: 5.7

## Dot (FRigVMFunction\_MathQuaternionDot)

Returns the dot product between two quaternions

### Information

|  |  |  |
| --- | --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |  |
| Category | Math|Quaternion |  |
| Tags | Dot, |  |
| Type | [FRigVMFunction\_MathQuaternionDot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathQuaternionDot) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first quaternion to compute the dot product for | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| B | The second quaternion to compute the dot product for | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting dot product between two quaternions | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

## Dot (FRigVMFunction\_MathVectorDot)

Returns the dot product between two vectors

### Information

|  |  |  |
| --- | --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |  |
| Category | Math|Vector |  |
| Tags | Dot, |  |
| Type | [FRigVMFunction\_MathVectorDot](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathVectorDot) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first vector compute the dot product for | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| B | The second vector compute the dot product for | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting dot product between A and B | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-drawarc.md

# Draw Arc

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawArc

> Application Version: 5.7

### Description

Draws an arc in the viewport, can take in different min and max degrees

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw Ellipse, Draw Circle |
| Type | [FRigVMFunction\_DebugArcNoSpace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_DebugArcNoSpace) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The transform of the arc to draw | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Color | The color to use for the debug draw | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| Radius | The radius of the arc to draw | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| MinimumDegrees | The minimum angle in degrees of the arc | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaximumDegrees | The maximum angle in degrees of the arc | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 360.000000 |
| Thickness | The line thickness to use for the debug draw | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Detail | The detail to use when drawing the arc | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 16 |
| WorldOffset | The world offset to pre-multiply the positions with | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bEnabled | If set to False the debug drawing will be skipped | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-drawbox.md

# Draw Box

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawBox

> Application Version: 5.7

### Description

Draws a box in the viewport

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | BoundingBox,Bbox |
| Type | [FRigVMFunction\_DebugBoxNoSpace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_DebugBoxNoSpace) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | The input bounding box to draw | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| Color | The color to use for the debug draw | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| Thickness | The line thickness to use for the debug draw | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| WorldOffset | The world offset to pre-multiply the positions with | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bEnabled | If set to False the debug drawing will be skipped | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-drawhierarchy.md

# Draw Hierarchy

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawHierarchy

> Application Version: 5.7

### Description

Draws vectors on each bone in the viewport across the entire hierarchy

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Debug |
| Type | [FRigUnit\_DebugHierarchy](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_DebugHierarchy) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | the items to draw the pose for. if this is empty we'll draw the whole hierarchy | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Scale | The scale to apply to the drawn transform | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| Color | The color to use when drawing | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=1.000000,A=1.000000) |
| Thickness | The line thickness to use when drawing | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| WorldOffset | The world offset to pre-multiply the drawn transform with | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bEnabled | If set to False the debug drawing will be skipped | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-drawline.md

# Draw Line

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawLine

> Application Version: 5.7

### Description

Draws a line in the viewport given a start and end vector

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Type | [FRigVMFunction\_DebugLineNoSpace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_DebugLineNoSpace) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The global start position of the line | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| B | The global end position of the line | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Color | The color to use for the drawing | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| Thickness | The line thickness to use for the drawing | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| WorldOffset | The world offset to pre-multiply the positions with | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bEnabled | If set to False the debug drawing will be skipped | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-drawlinestrip.md

# Draw Line Strip

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawLineStrip

> Application Version: 5.7

### Description

Draws a line strip in the viewport given any number of points

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Type | [FRigVMFunction\_DebugLineStripNoSpace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_DebugLineStripNoS-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | The array of input positions to treat as a line-strip | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |
| Color | The color to use for the drawing | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| Thickness | The line thickness to use for the drawing | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| WorldOffset | The world offset to pre-multiply the positions with | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bEnabled | If set to False the debug drawing will be skipped | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-drawposecache.md

# Draw Pose Cache

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawPoseCache

> Application Version: 5.7

### Description

Draws vectors on each bone in the viewport across the entire pose

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Debug |
| Type | [FRigUnit\_DebugPose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_DebugPose) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The input pose to draw | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |
| Items | the items to draw the pose cache for. if this is empty we'll draw the whole pose cache | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Scale | The scale to apply to the drawn transform | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| Color | The color to use when drawing | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=1.000000,A=1.000000) |
| Thickness | The line thickness to use when drawing | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| WorldOffset | The world offset to pre-multiply the drawn transform with | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bEnabled | If set to False the debug drawing will be skipped | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-drawrectangle.md

# Draw Rectangle

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawRectangle

> Application Version: 5.7

### Description

Draws a rectangle in the viewport given a transform

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw Square |
| Type | [FRigVMFunction\_DebugRectangleNoSpace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_DebugRectangleNoS-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The transform of the rectangle to draw | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Color | The color to use for the debug draw | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| Scale | The scale to apply to the debug draw | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| Thickness | The line thickness to use for the debug draw | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| WorldOffset | The world offset to pre-multiply the positions with | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bEnabled | If set to False the debug drawing will be skipped | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-drawspline.md

# Draw Spline

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawSpline

> Application Version: 5.7

### Description

Draws the given spline in the viewport

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Type | [FRigUnit\_DrawControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_DrawControlRigSpline) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The spline to draw | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| Color | The color to use for the debug draw | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| Thickness | The line thickness to use when drawing the spline | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Detail | The detail to use to render the spline | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 16 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-drawtransform.md

# Draw Transform

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawTransform

> Application Version: 5.7

### Description

Given a transform, will draw a point, axis, or a box in the viewport

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Type | [FRigVMFunction\_DebugTransformMutableNoSpace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_DebugTransformMut-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The transform to draw | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Mode | The mode to use when drawing the transform | [Rig Unit Debug Transform Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigUnitDebugTransformMode) | Axes |
| Color | The debug color to use | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| Thickness | The line thickness to use | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Scale | The scale to scale the transform by | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| WorldOffset | The world offset to pre-multiply the transform with | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bEnabled | If False the debug drawing will be skipped | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-drawtransformarray.md

# Draw Transform Array

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawTransformArray

> Application Version: 5.7

### Description

Given a transform array, will draw a point, axis, or a box in the viewport

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Type | [FRigVMFunction\_DebugTransformArrayMutableNoSpace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_DebugTransformArr-_1) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transforms | An array of input transforms to draw | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |
| ParentIndices | An array of parent indices for each transform. If this is specified lines will be drawn from each child to parent to represent a hierarchy. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |
| Mode | The mode to use when drawing the transforms | [Rig Unit Debug Transform Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigUnitDebugTransformMode) | Axes |
| Color | The debug color to use | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=1.000000,A=1.000000) |
| Thickness | The line thickness to use | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Scale | The scale to scale the transforms by | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| WorldOffset | The world offset to pre-multiply the transforms with | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bEnabled | If False the debug drawing will be skipped | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-e.md

# E

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/E

> Application Version: 5.7

### Description

Returns E

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | E,Euler |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value of the constant | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 2.718282 |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-ease.md

# Ease

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Ease

> Application Version: 5.7

### Description

Returns the eased version of the input value

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Animation |
| Tags | Easing,Profile,Smooth,Cubic |
| Type | [FRigVMFunction\_AnimEasing](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_AnimEasing) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value to ease using the easing functions | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Type | The type of easing to apply | [Rig VMAnim Easing Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMAnimEasingType) | CubicEaseInOut |
| SourceMinimum | The minimum value of the input | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SourceMaximum | The maximum value of the input | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| TargetMinimum | The minimum value of the output | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| TargetMaximum | The maximum value of the output | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting eased output value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-easetype.md

# EaseType

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EaseType

> Application Version: 5.7

### Description

A constant value of an easing type

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Animation |
| Tags | Constant |
| Type | [FRigVMFunction\_AnimEasingType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_AnimEasingType) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Type | The pass through constant easing type | [Rig VMAnim Easing Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMAnimEasingType) | CubicEaseInOut |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-endprofilingtimer.md

# End Profiling Timer

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EndProfilingTimer

> Application Version: 5.7

### Description

Ends an existing profiling timer for debugging, used in conjunction with Start Profiling Timer

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Debug |
| Tags | Measure,StopProfiling,Meter,Profile |
| Type | [FRigUnit\_EndProfilingTimer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_EndProfilingTimer) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NumberOfMeasurements | The number of measurements to take for profiling | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |
| Prefix | The prefix to use when printing to the log | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Timer |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-endswith.md

# EndsWith

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EndsWith

> Application Version: 5.7

### Description

Tests whether this name ends with given name
Tests whether this string ends with given string

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core |
| Tags | EndsWith,Ends With,Right |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The input name to search within | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | None |
| Ending | The ending name to look for | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | True if the given input name ends with the given ending | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-equals.md

# Equals

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Equals

> Application Version: 5.7

### Description

Compares any two values and return true if they are identical

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core |
| Tags | Same,== |
| Type | [FRigVMDispatch\_CoreEquals](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_CoreEquals) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first value to compare | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |
| B | The second value to compare | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The boolean result of the comparison | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-evaluatecurve.md

# Evaluate Curve

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateCurve

> Application Version: 5.7

### Description

Evaluates the provided curve. Values are normalized between 0 and 1

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Animation |
| Tags | Curve,Profile |
| Type | [FRigVMFunction\_AnimEvalRichCurve](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_AnimEvalRichCurve) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value to evaluate the curve at | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Curve | The curve to evaluate | [Runtime Float Curve](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/FRuntimeFloatCurve) | (EditorCurveData=(Keys=((),(Time=1.000000,Value=1.000000)),DefaultValue=340282346638528859811704183484516925440.000000,PreInfinityExtrap=RCCE\_Constant,PostInfinityExtrap=RCCE\_Constant),ExternalCurve=None) |
| SourceMinimum | The minimum range of the input value (typically 0.0) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SourceMaximum | The maximum range of the input value (typically 1.0) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| TargetMinimum | The minimum range of the output | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| TargetMaximum | The maximum range of the output | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The evaluated value of the curve at the input value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-evaluatelivelinkframeanimation.md

# Evaluate Live Link Frame (Animation)

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateLiveLinkFrameAnimation

> Application Version: 5.7

### Description

Evaluate current Live Link Animation associated with supplied subject

### Information

|  |  |
| --- | --- |
| Plugin | [LiveLinkControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/LiveLinkControlRig) |
| Category | Live Link |
| Type | [FRigUnit\_LiveLinkEvaluteFrameAnimation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/LiveLinkControlRig/FRigUnit_LiveLinkEvaluteFrameAni-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SubjectName | The name of the subject to evaluate a frame for | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| bDrawDebug | If True debug data will be drawn for the subject | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DebugColor | The color to use for the debug drawing | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| DebugDrawOffset | The world offset to use when drawing the debug data | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SubjectFrame | The resulting subject's frame | [Subject Frame Handle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/LiveLinkInterface/FSubjectFrameHandle) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-evaluatelivelinkframetransform.md

# Evaluate Live Link Frame (Transform)

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateLiveLinkFrameTransform

> Application Version: 5.7

### Description

Evaluate current Live Link Transform associated with supplied subject

### Information

|  |  |
| --- | --- |
| Plugin | [LiveLinkControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/LiveLinkControlRig) |
| Category | Live Link |
| Type | [FRigUnit\_LiveLinkEvaluteFrameTransform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/LiveLinkControlRig/FRigUnit_LiveLinkEvaluteFrameTra-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SubjectName | The name of the subject to evaluate | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| bDrawDebug | If True debug data will be drawn | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DebugColor | The color to use for the debug drawing | [Linear Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| DebugDrawOffset | The world offset to use for the debug drawing | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The resulting transform of the subject | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-expandbox.md

# Expand Box

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ExpandBox

> Application Version: 5.7

### Description

Expands the size of the box by a given amount

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Box |
| Tags | Bbox,Scale,Grow,Shrink,BoundingBox |
| Type | [FRigVMFunction\_MathBoxExpand](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoxExpand) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | the box to expand | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| Amount | the amount to grow / shrink the box by | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | the resulting expanded box | [Box](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-exponential.md

# Exponential

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Exponential

> Application Version: 5.7

### Description

Computes the base-e exponential of the given value

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Exponential |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-false.md

# False

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/False

> Application Version: 5.7

### Description

Returns false

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Boolean |
| Tags | No |
| Type | [FRigVMFunction\_MathBoolConstFalse](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoolConstFals-) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value of the constant | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-filteritemsbytags.md

# Filter Items by Tags

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FilterItemsbyTags

> Application Version: 5.7

### Description

Filters an item array by a list of tags

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | MetadataExists,HasKey,SupportsMetadata |
| Type | [FRigUnit\_FilterItemsByMetadataTags](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_FilterItemsByMetadataTa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items to filter | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Tags | The tags to find | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)> | () |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |
| Inclusive | If set to true only items with ALL of tags will be returned, if set to false items with ANY of the tags will be removed | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The results of the filter | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-find.md

# Find

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Find

> Application Version: 5.7

## Find (FRigVMFunction\_StringFind)

Finds a string within another string

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Tags | IndexOf |
| Type | [FRigVMFunction\_StringFind](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringFind) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input string to search within | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Search | The string to search for | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Found | True if the search string was found in the input string | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Index | The index of the search string within the input string (or INDEX\_NONE) | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

## Find (FRigVMDispatch\_ArrayFind)

Searchs a potential element in an array and returns its index.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayFind](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayFind) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | The array to search within. | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |
| Element | The element to look for. | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Index | The index of the found element (or -1). | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Success | True if the element has been found. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-findclosestitem.md

# Find Closest Item

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FindClosestItem

> Application Version: 5.7

### Description

Returns the item with the closest distance to the provided point in global space.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Find,Closest,Item,Transform,Bone,Joint |
| Type | [FRigUnit\_FindClosestItem](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_FindClosestItem) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The list of items to test | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Point | The point in global space to test against | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item closest to the provided point | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-finditemswithmetadata.md

# Find Items with Metadata

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FindItemswithMetadata

> Application Version: 5.7

### Description

Returns all items containing a specific set of metadata

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | MetadataExists,HasKey,SupportsMetadata |
| Type | [FRigUnit\_FindItemsWithMetadata](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_FindItemsWithMetadata) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The name of the metadata to find | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Type | The type of metadata to find | [Rig Metadata Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetadataType) | Float |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items containing the metadata | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-finditemswithmultipletags.md

# Find Items with multiple Tags

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FindItemswithmultipleTags

> Application Version: 5.7

### Description

Returns all items with a specific set of tags

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | MetadataExists,HasKey,SupportsMetadata |
| Type | [FRigUnit\_FindItemsWithMetadataTagArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_FindItemsWithMetadataTa-_1) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Tags | The tags to find | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName)> | () |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items containing the metadata | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-finditemswithtag.md

# Find Items with Tag

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FindItemswithTag

> Application Version: 5.7

### Description

Returns all items with a specific tag

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | MetadataExists,HasKey,SupportsMetadata |
| Type | [FRigUnit\_FindItemsWithMetadataTag](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_FindItemsWithMetadataTa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Tag | The name of the tag to find | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items containing the metadata | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-fitchainonsplinecurve.md

# Fit Chain on Spline Curve

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FitChainonSplineCurve

> Application Version: 5.7

### Description

Fits a given chain to a spline curve.
Additionally provides rotational control matching the features of the Distribute Rotation node.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Tags | Fit,Resample,Spline |
| Type | [FRigUnit\_FitChainToSplineCurveItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_FitChainToSplineCurveIt-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items to align | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Spline | The curve to align to | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| Alignment | Specifies how to align the chain on the curve | [Control Rig Curve Alignment](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/EControlRigCurveAlignment) | Stretched |
| Minimum | The minimum U value to use on the curve | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Maximum | The maximum U value to use on the curve | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| SamplingPrecision | The number of samples to use on the curve. Clamped at 64. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 12 |
| PrimaryAxis | The major axis being aligned - along the bone | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| SecondaryAxis | The minor axis being aligned - towards the pole vector. You can use (0.0, 0.0, 0.0) to disable it. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| PoleVectorPosition | The position of the pole vector used for aligning the secondary axis. Only has an effect if the secondary axis is set. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Rotations | The list of rotations to be applied along the curve | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_FitChainToCurve\_Rotation](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_FitChainToCurve_Rotatio-)> | () |
| RotationEaseType | The easing to use between to rotations. | [Rig VMAnim Easing Type](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMAnimEasingType) | Linear |
| Weight | The weight of the solver - how much the rotation should be applied | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bPropagateToChildren | If set to true all of the global transforms of the children of this bone will be recalculated based on their local transforms. Note: This is computationally more expensive than turning it off. | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugSettings | The debug settings to use | [Rig Unit Fit Chain to Curve Debug Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_FitChainToCurve_DebugSe-) | (bEnabled=False,Scale=1.000000,CurveColor=(R=1.000000,G=1.000000,B=0.000000,A=1.000000),SegmentsColor=(R=1.000000,G=0.000000,B=0.000000,A=1.000000),WorldOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))) |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-fitsplinecurveonchain.md

# Fit Spline Curve on Chain

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FitSplineCurveonChain

> Application Version: 5.7

### Description

Fits a given spline curve to a chain.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Tags | Fit,Resample,Spline |
| Type | [FRigUnit\_FitSplineCurveToChainItemArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_FitSplineCurveToChainIt-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The curve to align | [Control Rig Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items to align to | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-flipflop.md

# FlipFlop

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FlipFlop

> Application Version: 5.7

### Description

Returns true and false as a sequence.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Boolean |
| Tags | Toggle,Changed,Different |
| Type | [FRigVMFunction\_MathBoolFlipFlop](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathBoolFlipFlop) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| StartValue | The initial value to use for the flag | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Duration | The duration in seconds at which the result won't change. Use 0 for a different result every time. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting value | [bool](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-floor.md

# Floor

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Floor

> Application Version: 5.7

## Floor ()

Returns the closest lower full number (integer) of the value

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Floor,Round |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value to apply the floor to | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting closest lower full number (integer) of the input value | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |
| Int | The result as an integer value | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

## Floor (FRigVMFunction\_MathVectorFloor)

Returns the closest lower full number (integer) of the value for each component

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Tags | Round |
| Type | [FRigVMFunction\_MathVectorFloor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathVectorFloor) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The result of the operation | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-foreach.md

# For Each

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ForEach

> Application Version: 5.7

### Description

Loops over the elements in an array.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayIterator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayIterator) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | The array to iterate over | [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Completed | The Completed execute argument. | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Element | The current element. | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |
| Index | The index of the current element. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Count | The count of all elements in the array. | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Ratio | A float ratio from 0.0 (first element) to 1.0 (last element). | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-foreachposecacheelement.md

# For Each Pose Cache Element

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ForEachPoseCacheElement

> Application Version: 5.7

### Description

Given a pose, execute iteratively across all items in the pose

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Collection,Loop,Iterate |
| Type | [FRigUnit\_PoseLoop](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PoseLoop) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The pose to loop over | [Rig Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item for the current pose entry | [Rig Element Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |
| GlobalTransform | The global transform for the current pose entry | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| LocalTransform | The local transform for the current pose entry | [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| CurveValue | The curve value for the current pose entry | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Index | The index of the current pose entry | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Count | The overall count of entries in the pose | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Ratio | Ranging from 0.0 (first item) and 1.0 (last item) This is useful to drive a consecutive node with a curve or an ease to distribute a value. | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Completed | The branch to run when the loop has completed | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-forloop.md

# For Loop

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ForLoop

> Application Version: 5.7

### Description

Given a count, execute iteratively until the count is up

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Execution |
| Tags | Iterate |
| Type | [FRigVMFunction\_ForLoopCount](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_ForLoopCount) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Count | The number of iterations for this loop | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Index | The index of the current iteration | [int32](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Ratio | The ratio of the current iteration (from 0.0 for the first to 1.0 for the last) | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Completed | The completed branch to run once the loop has finished all iterations | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-forwardssolve.md

# Forwards Solve

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ForwardsSolve

> Application Version: 5.7

### Description

Event for driving the skeleton hierarchy with variables and rig elements

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Events |
| Tags | Begin,Update,Tick,Forward,Event |
| Type | [FRigUnit\_BeginExecution](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_BeginExecution) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | The execution result | [Execute Context](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-framestoseconds.md

# Frames to Seconds

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FramestoSeconds

> Application Version: 5.7

### Description

Converts frames to seconds based on the current frame rate

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Animation |
| Type | [FRigVMFunction\_FramesToSeconds](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_FramesToSeconds) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Frames | The input value representing a number of frames to convert to seconds | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Seconds | The resulting time in seconds | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-fromaxisandangle.md

# From Axis And Angle

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FromAxisAndAngle

> Application Version: 5.7

### Description

Makes a quaternion from an axis and an angle in radians

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Quaternion |
| Tags | Make,Construct |
| Type | [FRigVMFunction\_MathQuaternionFromAxisAndAngle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathQuaternionFro-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Axis | The axis to use for the quaternion | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| Angle | The angle in radians to use for the quaternion | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting composed quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-fromeuler.md

# From Euler

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FromEuler

> Application Version: 5.7

### Description

Makes a quaternion from euler values in degrees

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Quaternion |
| Tags | Make,Construct |
| Type | [FRigVMFunction\_MathQuaternionFromEuler](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathQuaternionFro-_1) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Euler | The euler representation of the rotation in degrees. | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| RotationOrder | The rotation order to use when interpreting the euler angles | [Euler Rotation Order](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/EEulerRotationOrder) | ZYX |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting composed quaternion | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-fromstring.md

# From String

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FromString

> Application Version: 5.7

### Description

Converts a string into any value

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Type | [FRigDispatch\_FromString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigDispatch_FromString) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| String | The string to convert the value from | [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting value based on the string | [Wildcard](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-fromtwovectors.md

# From Two Vectors

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FromTwoVectors

> Application Version: 5.7

### Description

Makes a quaternion from two vectors, representing the shortest rotation between the two vectors.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Quaternion |
| Tags | Make,Construct |
| Type | [FRigVMFunction\_MathQuaternionFromTwoVectors](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathQuaternionFro-_4) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | A vector representing a direction prior to rotation | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| B | A vector representing a direction after a rotation | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The quaternion representing the rotation from A to B | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-fromvectors.md

# From Vectors

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FromVectors

> Application Version: 5.7

### Description

Makes a matrix from its vectors

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Matrix |
| Tags | Make,Construct |
| Type | [FRigVMFunction\_MathMatrixFromVectors](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathMatrixFromVec-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Origin | The input origin for the matrix | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| X | The input X component for the matrix | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| Y | The input Y component for the matrix | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=1.000000,Z=0.000000) |
| Z | The input Z component for the matrix | [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting matrix | [Matrix](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-fromworld.md

# From World

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FromWorld

> Application Version: 5.7

### Description

Converts a transform from world space to rig (global) space
Converts a position / location from world space to rig (global) space
Converts a rotation from world space to rig (global) space

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | From World,Global,Local,World,Actor,ComponentSpace,ToRig |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input transform in world | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Global | The result transform in global / rig space | [Quat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

## Fuente: .\docs-md-py\en-us\unreal-engine\node-reference-controlrig-fullbodyik.md

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

