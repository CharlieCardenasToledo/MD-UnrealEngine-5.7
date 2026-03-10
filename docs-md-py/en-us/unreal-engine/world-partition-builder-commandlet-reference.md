# World Partition Builder Commandlet Reference

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition-builder-commandlet-reference

> Application Version: 5.7

**World Partition** introduces a builder commandlet framework through the **UWorldPartitionBuilderCommandlet** and the **UWorldPartitionBuilder** base class.

These commandlets are used to automate batch processes and generate or modify data in World Partition Levels. Large worlds will not have to be loaded all at once to do things like generating HLODs, AI Nav Data, or resave a large number of Actors.

## World Partition HLODs Builder

HLODs are generated using the **World Partition HLODs Builder** commandlet. Running this commandlet creates the HLOD Actors for your World Partition cells according to the generation settings you specified in your HLOD Layers.

![Image](https://dev.epicgames.com/community/api/documentation/image/b3df917e-e941-4db9-991c-1b9600a6c477)

Command: `UnrealEditor.exe "C:\Users\user.name\Documents\Unreal Projects\MyProject\MyProject.uproject" "/Game/ThirdPersonBP/Maps/OpenWorldTest" -run=WorldPartitionBuilderCommandlet -AllowCommandletRendering -builder=WorldPartitionHLODsBuilder`

For more information about using Hierarchical Levels of Detail (HLODs) in World Partition and using the WorldPartitionHLODsBuilder commandlet, see the [World Partition - Hierarchical Level of Detail](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition---hierarchical-level-of-detail-in-unreal-engine) documentation.

## World Partition MiniMap Builder

The **World Partition MiniMap Builder** commandlet generates or updates the minimap that displays in the WorldPartition Editor window.

![Image](https://dev.epicgames.com/community/api/documentation/image/dee9f8d1-66db-4d3f-a019-36c26d16d275)

Command: `UnrealEditor.exe "C:\Users\user.name\Documents\Unreal Projects\MyProject\MyProject.uproject" "/Game/ThirdPersonBP/Maps/OpenWorldTest" -run=WorldPartitionBuilderCommandlet -AllowCommandletRendering -builder=WorldPartitionMiniMapBuilder`

## World Partition Rename Duplicate Builder

The **World Partition Rename Duplicate Builder** commandlet automates the process of renaming or duplicating an existing World Partition Level and all its actors.

![Image](https://dev.epicgames.com/community/api/documentation/image/751af0da-47ec-41c0-89f4-b6eefc300e19)

Command: `UnrealEditor.exe "C:\Users\user.name\Documents\Unreal Projects\MyProject\MyProject.uproject" "/Game/ThirdPersonBP/Maps/OpenWorldTest" -run=WorldPartitionBuilderCommandlet -SCCProvider=None -builder=WorldPartitionRenameDuplicateBuilder -NewPackage=/Game/ThirdPersonBP/Maps/NewPackage`

This will create a duplicate World Partition Level of the **OpenWorldTest** map named **NewPackage** and leave the original map untouched.

To rename your World Partition map rather than make a copy, add the `-Rename` argument.

## World Partition Resave Actors Builder

The **World Partition Resave Actors Builder** commandlet resaves all Actors of a World Partition Level and supports a class filter to resave only a subset of Actors.

![Image](https://dev.epicgames.com/community/api/documentation/image/a50a3133-7c8d-45b6-a345-5626e943e5ad)

Command: `UnrealEditor.exe "C:\Users\user.name\Documents\Unreal Projects\MyProject\MyProject.uproject" "/Game/ThirdPersonBP/Maps/OpenWorldTest" -run=WorldPartitionBuilderCommandlet -SCCProvider=None -builder=WorldPartitionResaveActorsBuilder`

When you execute the above example, all of the Actor's packages in the OpenWorldTest level are resaved.

You can use the `-ActorClass` argument to specify only a subset of Actors to be resaved. For example, adding `-ActorClass=StaticMeshActor` will resave only the Static Mesh Actors in the specified Level.

## World Partition Foliage Builder

In a World Partition map, the default Instanced Foliage Grid Size for Foliage Instances is 256 meters. The **World Partition Foliage Builder** commandlet is used to change the Instanced Foliage Grid Size for existing World Partition level.

![Image](https://dev.epicgames.com/community/api/documentation/image/2a9a6972-785a-41e4-a2ca-96d92a5462a5)

Command: `UnrealEditor.exe QAGame Playground.umap -run=WorldPartitionBuilderCommandlet -Builder=WorldPartitionFoliageBuilder -NewGridSize=Value`

For more information on using Foliage Mode with World Partition, see the [Foliage Mode](building-virtual-worlds/open-world-tools/foliage-mode) documentation.

## World Partition Navigation Data Builder

The **World Partition Navigation Data Builder** commandlet rebuilds the navmesh in your World Partition Level.

![Image](https://dev.epicgames.com/community/api/documentation/image/07f49799-d7cf-44fa-92b0-020478f13370)

Command: `UnrealEditor.exe "C:\Users\user.name\Documents\Unreal Projects\MyProject\MyProject.uproject" "/Game/ThirdPersonBP/Maps/OpenWorldTest" -run=WorldPartitionBuilderCommandlet -AllowCommandletRendering -builder=WorldPartitionNavigationDataBuilder -SCCProvider=None`

This commandlet takes the following arguments:

| Optional Argument | Description |
| --- | --- |
| **-SCCProvider** | Specifies which source control provider to use. To run without source control, specify `-SCCProvider=None`. |
| **-Verbose** | Displays verbose logging. |
| **-Log** | Outputs log to a specific file. |
| **-CleanPackages** | Wipes all navigation data packages instead of building them. |

## World Partition Smart Object Collection Builder

The World Partition Smart Object Collection Builder commandlet rebuilds the smart object collection from all the smart object components in your World Partition Level.

![Image](https://dev.epicgames.com/community/api/documentation/image/f7272067-0015-40ef-999f-b3e65e10ec25)

Command: `UnrealEditor.exe "C:\Users\user.name\Documents\Unreal Projects\MyProject\MyProject.uproject" "/Game/ThirdPersonBP/Maps/OpenWorldTest" -run=WorldPartitionBuilderCommandlet -builder=WorldPartitionSmartObjectCollectionBuilder`

When you execute the above example, all of the Smart Object Collection in the OpenWorldTest level are rebuilt. You can use the `-SCCProvider` argument with this commandlet to specify which source control provider to use.

## World Partition PCG Builder

The **World Partition PCG Builder** commandlet loads the level completely, waits for async processes to complete such as static mesh builds, then schedules generation on matching PCG components. When all generation is complete the process saves the World Partition level and exits.

![Image](https://dev.epicgames.com/community/api/documentation/image/7ee255be-880a-49fc-8787-539b958b569a)

Command Line: `UnrealEditor.exe "C:\Users\user.name\Documents\Unreal Projects\MyProject\MyProject.uproject" "/Game/ThirdPersonBP/Maps/OpenWorldTest" -Unattended -AllowCommandletRendering -run=WorldPartitionBuilderCommandlet -Builder=PCGWorldPartitionBuilder -IncludeGraphNames=PCG_GraphA;PCG_GraphB`

Console Command: `pcg.BuildComponents -IncludeGraphNames=PCG_GraphA;PCG_GraphB`

This commandlet takes the following arguments:

| Optional Argument | Description |
| --- | --- |
| **-IncludeGraphNames** | Includes a list of graph names in the generation, separated by `;`. If provided, the system will schedule generation of all PCG components with the first graph assigned, then the same for the second graph, and so on. If omitted then PCG components will not be filtered by graph. |
| **-GenerateComponentEditingModeLoadAsPreview** | Components that are saved with the Editor Mode **Load As Preview** will be considered for generation when this argument is used. |
| **-GenerateComponentEditingModeNormal** | Generates components with Editing Mode set to **Normal**. By default only components that are saved with the Editing Mode **Load As Preview** are generated. |
| **-GenerateComponentEditingModePreview** | Generates components with Editing Mode set to **Preview**. By default only components that are saved with the Editing Mode **Load As Preview** are generated. |
| **-IgnoreGenerationErrors** | Submits the result to source control, regardless of errors (but the errors are still reported and the job status will still be Failed). This can be used to keep the job online even in the presence of errors, but should be used with caution. By default, any error that occurs while a component is generating will be registered with the builder and will fail the build job, and the results will not be submitted. |
| **-IncludeActorIDs** | Includes a list of unique actor IDs separated by `;`. If provided only PCG components on matching actors will be generated. Particularly useful for debugging a single component/actor. |
| **-OneComponentAtATime** | Schedules generation of one component at a time and wait for each generation to finish before scheduling a new component. Useful while debugging to ensure async processes are not interfering with each other. |
| **-PCGBuilderSettings** | Specifies a **PCGBuilderSettings** asset to use when setting up the builder commandlet. All commandlet arguments override the arguments set in the PCGBuilderSettings asset. |
| **-IterativeCellLoading** | Processes the world using a specific cell size to avoid loading everything at once. Loaded components generate and save. They are then unloaded and the builder moves to a different cell. This is useful for large worlds where loading the whole world causes memory issues. |
| **-IterativeCellSize** | Overrides the default cell size when using **IterativeCellLoading**. Default is `25600`. |
| **-Unattended** | Avoids initializing the Editor UI, runs in console instead. |
| **-AllowCommandletRendering** | Initializes rendering subsystem. Useful because PCG has some functionality that utilizes the GPU. |
| **-AutoSubmit** | Attempts to submit the result to source control, if available. |
| **-AssetGatherAll** | Builds the full asset registry for all assets in the project. Required if the builder needs to access assets not referenced in the level. |

## World Partition RVT Builder

The **World Partition RVT Builder** commandlet finds all of the runtime virtual texture components in your World Partition Level, and for any that have an associated `StreamingTexture` asset, it rebuilds the asset. Those assets are baked low-resolution versions of the runtime virtual textures, used to render in the distance to improve performance.

![RVT commandlet example](https://dev.epicgames.com/community/api/documentation/image/a63e5758-8dca-4bd5-8bf3-04c9dc574b91)

Command Line: `UnrealEditor.exe "C:\Users\user.name\Documents\Unreal Projects\MyProject\MyProject.uproject" -run=WorldPartitionBuilderCommandlet -Builder=PCGWorldPartitionBuilder "/Game/ThirdPersonBP/Maps/OpenWorldTest" -AllowCommandletRendering`

For more information on using streaming runtime virtual textures, see [Runtime Virtual Texturing](https://dev.epicgames.com/documentation/en-us/unreal-engine/runtime-virtual-texturing-in-unreal-engine#streaming-virtual-texture-build).
