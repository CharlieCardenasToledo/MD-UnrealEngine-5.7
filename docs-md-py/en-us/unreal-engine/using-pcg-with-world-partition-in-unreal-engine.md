# Using PCG with World Partition

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-with-world-partition-in-unreal-engine

> Application Version: 5.7

When PCG assets are assigned to an [World Partition - Data Layer](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine) and a [HLOD Layer](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition---hierarchical-level-of-detail-in-unreal-engine), the PCG graph generates the actors and assigns them to the same data layer and HLOD layer.

## Using Data Layers

In the example below, there are two [partitioned](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-generation-modes-in-unreal-engine?application_version=5.5) PCG volumes. One generates rock meshes and is assigned to the **DL\_Rocks** data layer. The other generates tree meshes and is assigned to the **DL\_Trees** data layer.

![A generated tree selected in the Data Layers window. It is assigned to the DL_Trees data layer.](https://dev.epicgames.com/community/api/documentation/image/7f41308e-7e80-43bc-b066-f214bec47e57)

Selecting the generated meshes in the **Data Layers** window shows that the rocks are automatically assigned to **DL\_Rocks** and the trees are automatically assigned to **DL\_Trees**.

### Data Layer Settings for Spawn Actor and Create Target Actor Nodes

The Spawn Actor and Create Target Actor nodes each have a setting called Data Layer Source Type that controls how the node assigns actors to a Data Layer.

![The Data Layer Settings.](https://dev.epicgames.com/community/api/documentation/image/d745a953-5fa4-4f86-8eec-f0c1aa9f0810)

The Data Layer Source Type can be set to the following options:

- **Self**: The Spawn Actor or Create Target Actor node assigns the same Data Layers to the spawned actors as the source PCG Component actor.
- **Data Layer References**: The node assigns Data Layers using an input Param Data set by the **Data Layer Reference** **Attribute**.

The Spawn Actor and Create Target Actor nodes support filtering using the **Included Data Layers** and **Excluded Data Layers** properties, which can be inputs or direct references.

There is also an **Add Data Layers** category where you can specify additional Data Layers to assign, either as input or as direct references.

### Get Actor Data Layers

The **Get Actor Data Layers** node reads the **ActorReference** attribute from the inputs, and then outputs all the Data Layers used by those inputs into the **DataLayerReference** attribute. The output is a single Param Data that contains one entry per Data Layer asset.

![The Get Actor Data Layers node](https://dev.epicgames.com/community/api/documentation/image/abc9347a-f0a1-4cf7-89b6-139810b08562)

### Partition By Actor Data Layers

The **Partition By Actor Data Layers** node takes Point Data as input, and outputs one or more partitions of Point Data based on the Data Layers in the input Point Data.

![The Partition by Actor Data Layers node.](https://dev.epicgames.com/community/api/documentation/image/3171c002-2977-45b4-9ca2-88992e18b9db)

The node resolves input points using an **ActorReference** attribute to get the Data Layers used by the Actor. Then it creates a Point Data and a Data Layer Partition for every combination of those Data Layers found on the input.

To include or exclude data layers from the process, use the **Included Data Layers** and **Excluded Data Layers** inputs on the node, or use **DataLayer** asset references in the node settings.

![Using a DataLayer asset reference in the node settings](https://dev.epicgames.com/community/api/documentation/image/b3143f0a-7e69-476e-80e6-688d2edf1442)

_Using a DataLayer asset reference in the node settings_

When using Included Data Layers, any other Data Layer will be ignored. When using Excluded Data Layers, all Data Layers will be considered except for the excluded Data Layers.

#### Example 1

The input data has three Points that point to three different actors. One actor uses **DataLayerA**, and the other two actors use **DataLayerB**.

The output will include two Point Data, and two Data Layer Partitions (stored as Param Data).

The first Point Data will contain the point that is using **DataLayerA.**The second Point Data will contain both points that are using **DataLayerB**.

The first Data Layer Partition will contain one entry with a **DataLayerReference** attribute pointing to the **DataLayerA** asset. The second partition will contain one entry with a **DataLayerReference** attribute pointing to the **DataLayerB** asset.

#### Example 2

The input has the following Points:

- a Point that resolves to **DataLayerA**
- a Point that resolves to **DataLayerB**
- a Point that resolves to both **DataLayerA** and **DataLayerB**

The output will include three Point Data with a single point each, and three Param Data.

The first Point Data will contain the point that is using DataLayerA. The second Point Data will contain the point that is using DataLayerB. The third Point Data will contain the point that is using both **DataLayerA** and **DataLayerB**.

The first Data Layer Partition will contain one entry with a DataLayerReference attribute pointing to the DataLayerA asset. The second partition will contain one entry with a DataLayerReference attribute pointing to the DataLayerB asset.  The third partition will contain two entries, one that points to the **DataLayerA** asset and one that points to the **DataLayerB** asset.

## Using HLOD Layers

In the example below, there is a **Surface Sampler** that generates rock meshes.

![A Blueprint graph showing a Surface Sampler.](https://dev.epicgames.com/community/api/documentation/image/2a51cc62-2c69-4209-a36a-3d7b572ab9f2)

The PCG Graph that contains the sampler is set to assign all of its components and actors to an HLOD layer called **MyHLODLayer**.

![The PCG graph's HLOD settings.](https://dev.epicgames.com/community/api/documentation/image/9f850fc5-aadf-4cf0-9415-3c29a0b2bc9b)

Selecting the generated meshes shows that the generated rocks are automatically assigned to **MyHLODLayer**.

![Multiple rock meshes are selected. All of them are assigned to MyHLODLayer.](https://dev.epicgames.com/community/api/documentation/image/af15da0b-8106-4810-90eb-99caa3ed644c)

### HLOD Settings for Spawn Actor and Create Target Actor Nodes

The Spawn Actor and Create Target Actor nodes each have a setting called **HLODSource Type** that controls how the node assigns actors to an HLOD Layer.

![The HLODSource Type setting](https://dev.epicgames.com/community/api/documentation/image/3a3b365e-7caf-4a1e-b649-231d1f016d25)

The **HLODSource Type** can be set to the following options:

- **Self**: The Spawn Actor or Create Target Actor node assigns the same HLOD Layer to the spawned actors as the source PCG Component actor.
- **Reference**: The node assigns an HLOD Layer through a direct reference to the HLOD Layer on the node settings.
- **Template**: The node uses the HLOD Layer reference from its Template Actor.
