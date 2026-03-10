# EQS Node Reference: Contexts

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/eqs-node-reference-contexts-in-unreal-engine

> Application Version: 5.7

Within the Environment Query System (EQS), **Contexts** provide a frame of reference for any [Tests](https://dev.epicgames.com/documentation/en-us/unreal-engine/eqs-node-reference-tests-in-unreal-engine) or [Generators](https://dev.epicgames.com/documentation/en-us/unreal-engine/eqs-node-reference-generators-in-unreal-engine) used. A Context can be as simple as the **Querier**(who is performing the Test) or more complex such as **All Actors of a Type**. A Generator, such as a **Points: Grid**, can use a Context that returns multiple locations or Actors. This will create a grid (of the defined size and density) at the location of each Context. In addition to Engine supplied Contexts, you can create custom Contexts in Blueprint with the **EnvQueryContext\_BlueprintBase**class or through C++ code.

## EnvQueryContext\_Item

**Items**are created by the Generator, and if using the **EQS Testing Pawn**, they are the spheres that appear in the Editor. An EnvQueryContext\_Item is either a location (FVector) or an Actor (AActor).

## EnvQueryContext\_Querier

The **Querier** is the Pawn that is currently possessed by an AI Controller and is executing the [Behavior Tree](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-trees-in-unreal-engine) that initiated the Environment Query. An example of where Querier as the Context could be used is if you want to search the environment around the AI character for an item they can use or find a place that provides cover from the player, or just to determine the current location of the AI performing the query.

In the **Details** panel for a Generator type, you can assign the Querier as a Context for the following properties:

| Generator | Property |
| --- | --- |
| **Actors of Class** | **Search Center** ![Actors of Class](https://dev.epicgames.com/community/api/documentation/image/2d5da4d4-d10a-4f20-b23b-55aab3317831) |
| **Current Location** | **Query Context** ![Current Location](https://dev.epicgames.com/community/api/documentation/image/bf0e86fd-5d8e-4e6e-b1ee-0c2bdb30f51a) |
| **Points: Circle** | **Circle Center** ![Circle Point](https://dev.epicgames.com/community/api/documentation/image/5a9fe7ae-0008-4a4e-810e-a4d4186bcc0d) |
| **Points: Cone** | **Center Actor** ![Cone Point](https://dev.epicgames.com/community/api/documentation/image/2849ed6b-22c9-4908-b27d-8ea19f9dc271) |
| **Points: Donut** | **Center** ![Donut Point](https://dev.epicgames.com/community/api/documentation/image/091ed0df-b616-4617-8896-dec4e0317c8f) |
| **Points: Grid** | **Generate Around** ![Grid Point](https://dev.epicgames.com/community/api/documentation/image/41ef7457-8c9f-4779-acf9-564d1d635431) |
| **Points: Pathing Grid** | **Generate Around** ![Pathing Grid Point](https://dev.epicgames.com/community/api/documentation/image/a7d18056-6498-4759-9187-1f9bb1b2d373) |

## EnvQueryContext\_BlueprintBase

You can create a custom Context through Blueprint using the **EnvQueryContext\_BlueprintBase** Class. This provides four functions that can be overridden, enabling you to add your custom Contexts for use within Tests in a query.

To use a custom Context:

1. Create a new Blueprint of the **EnvQueryContext\_BlueprintBase** class. ![Create a new Blueprint of the EnvQueryContext BlueprintBase class](https://dev.epicgames.com/community/api/documentation/image/f4df9fe5-bb51-4ba6-b37f-fee9a7b99c4a)
2. In EnvQueryContext\_BlueprintBase, click **Override** and select the type of function you wish to use. ![Click Override and select the type of function you wish to use](https://dev.epicgames.com/community/api/documentation/image/a4c8d362-32dd-4c96-8e9c-5b6b070350ec)

Refer to the table below for a description of each function override:

| Function | Description |
| --- | --- |
| Provide Single Location | This returns a single location (vector). How you generate that location is up to you. For example, the function below will return the trace hit location of a random Actor (one that is found in the DesiredObjectType array, such as Pawn, Vehicle) found within 1500 cm of the Querier: ![Provide Single Location](https://dev.epicgames.com/community/api/documentation/image/1e9296db-61b7-4ff1-8cff-44202818ff4c) |
| Provide Single Actor | This returns a single Actor. You can obtain that Actor through any method you desire. In this example, the function will return Player 0's controlled Actor: ![Provide Single Actor](https://dev.epicgames.com/community/api/documentation/image/2adb4b22-37c0-43bc-9d63-4ea48267e198) |
| Provide Locations Set | This returns an array of locations (vectors). How you generate these locations is up to you. In the example below, this function will trace from 16 evenly spaced locations on a circle with a radius of 1500 units, returning successful hits on the environment: ![Provide Locations Set](https://dev.epicgames.com/community/api/documentation/image/fb5b7bae-f29b-410e-a87a-b571cb482ee6) |
| Provide Actors Set | This returns an array of Actors. You can use any desired method to obtain those Actors. In the example below, we use a Get All Actors of Class node to retrieve our specified class as the Actors to return: ![Provide Actors Set](https://dev.epicgames.com/community/api/documentation/image/16d70a6a-9785-4439-88c2-828af4e0e58f) |
