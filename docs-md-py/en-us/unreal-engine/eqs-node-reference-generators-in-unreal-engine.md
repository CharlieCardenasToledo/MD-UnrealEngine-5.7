# EQS Node Reference: Generators

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/eqs-node-reference-generators-in-unreal-engine

> Application Version: 5.7

Within the Environmental Query System (EQS), **Generators**are used to produce the locations or Actors (referred to as **Items**) that will be tested and weighted, with the highest weight location or Actor being returned to the [Behavior Tree](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-trees-in-unreal-engine). There are different types of Generators that you can use to retrieve information and they can be created either in Blueprint or C++.

## Actors of Class

![Actors Of Class](https://dev.epicgames.com/community/api/documentation/image/80cecc59-145b-44ca-817d-ac0ed41e59e7)

The **Actors of Class**Generator finds all of the Actors of a given class within the specified **Search Radius**around the **Search Center**. The Actors returned can be used as Items in your tests.

![The Actors of Class Generator finds all of the Actors of a given class within the specified Search Radius around the Search Center](https://dev.epicgames.com/community/api/documentation/image/650f963e-ca35-4429-bee8-71b03867ddef)

| Property | Description |
| --- | --- |
| **Searched Actor Class** | The Actor class to look for (for example, Pawn, Character). |
| **Generate Only Actors in Radius** | If enabled, this will only return Actors of the specified **Searched Actor Class** within the **Search Radius.**If disabled, it will return all Actors of the specified **Searched Actor Class**in the game world. You can also optionally include user-defined **Data Bindings**to go along with this option. |
| **Search Radius** | The max distance to look for the specified **Searched Actor Class**. |
| **Search Center** | The context to center to search for, such as from the Querier or perhaps some other context. |
| **Option Name** | This property is inherited from the base class of the Generator ActorsOfClass. It is mostly used when displaying the Name of this Generator (for example, HUDs or output messages). |
| **Auto Sort Tests** | If enabled, Tests will automatically be sorted for best performance before the query is run. |

## Composite

![Composite Generator](https://dev.epicgames.com/community/api/documentation/image/2523463c-725f-4bef-b701-6404dbc46edf)

When setting up an EQS Query, there may be instances where you want to include more than one **Generator**in a test case. With the **Composite**node, you can add multiple **Generators** to an array, which can be used in your Tests.

![With the Composite node you can add multiple Generators to an array](https://dev.epicgames.com/community/api/documentation/image/c4903e02-c515-4a54-a7c8-e678f181f87f)

| Property | Description |
| --- | --- |
| **Generators** | Enables you to add multiple Generators to include in the test. |
| **Allow Different Item Types** | This allows tests to be performed on Generators with different Item types. |
| **Forced Item Type** | The Item type to use in Tests. For example Actor, Direction, or Point. |
| **Option Name** | This property is inherited from the base class of the Generator ActorsOfClass. It is mostly used when displaying the name of this Generator (for example, HUDs or output messages). |
| **Auto Sort Tests** | If enabled, Tests will automatically be sorted for best performance before the query is run. |

## Current Location

![Current Location](https://dev.epicgames.com/community/api/documentation/image/b5e652c5-8e7f-45d1-ad39-f6945fb386e0)

The **Current Location** Generator can be used to get the location of the specified **Query Context** to validate Tests.

![The Current Location Generator can be used to get the location of the specified Query Context for the purposes of validating Tests](https://dev.epicgames.com/community/api/documentation/image/2c2f082c-720f-4e9b-9a79-00a0f6fa7970)

| Property | Description |
| --- | --- |
| **Query Context** | The Context to use in the Test and its current location. |
| **Option Name** | This property is inherited from the base class of the Generator ActorsOfClass. It is mostly used when displaying the Name of this Generator (for example, HUDs or output messages). |
| **Auto Sort Tests** | If enabled, Tests will automatically be sorted for best performance before the query is run. |

## Custom Generators

In addition to the Generator types provided by the Engine, you can create your custom Generators by creating a new Blueprint of the **EnvQueryGenerator\_BlueprintBase** class type.

![Custom Generators](https://dev.epicgames.com/community/api/documentation/image/9df205e2-8615-4c21-bd2c-ca333f306477)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Generators developed in C++ will execute generally faster than that developed through Blueprint.",
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

Once created, your custom Generator will be available within an Environmental Query:

![Your custom Generator will be available within an Environmental Query](https://dev.epicgames.com/community/api/documentation/image/94ae4c23-e721-4185-941c-e25f9c5d61bd)

Inside your custom Generator, there is a function you can override called **Do Item Generation**:

![There is a function you can override called Do Item Generation](https://dev.epicgames.com/community/api/documentation/image/b1ed51a4-002f-4d00-8d0c-8d8160a0e2d1)

When you override this function, you'll get an array of locations that are the Context locations passed in from the Environmental Query.

![You will get an array of locations that are the Context locations passed in from the Environmental Query](https://dev.epicgames.com/community/api/documentation/image/2857e377-92a1-4699-845f-3c89490678fb)

Depending on the Context, the array may vary. For example, this could be an array of just a single entry containing the location of the Querier, or, it could be the locations of every health pickup inside your Level.

Since functions can only return one value, the Do Item Generation function has two arrays it can pass back to the Environment Query: **Add Generated Actor** and **Add Generated Vector**.

![Add Generated Actor](https://dev.epicgames.com/community/api/documentation/image/b5663b34-87ac-4607-a677-53b632a3460d)

The Add Generated Actor node will add an Actor to the Actor return array. This node can also be used with the **Add Generated Vector**node (below) to also return location values. How the Generator determines what it is passing back to the Behavior Tree is based on what Blackboard key you are setting from the Environment Query node.

![Add Generated Actor](https://dev.epicgames.com/community/api/documentation/image/28032580-9a5d-485b-b6a0-76efda14cd34)

## Points: Circle

![Circle Generator](https://dev.epicgames.com/community/api/documentation/image/72123bac-ed42-4699-af80-9c2ffd644194)

The **Points: Circle** Generator radiates traces out from the **Circle Center**, returning the hits on the edge of the radius (of the generated Circle) as Items.

![Circle Generator radiates traces out from the Circle Center](https://dev.epicgames.com/community/api/documentation/image/373738c3-39cd-40c1-876c-2a3f6536ee4c)

| Property | Description |
| --- | --- |
| **Circle Radius** | The max radius of the circle that will expand out from the **Circle Center** context. |
| **Spawn Between** | The space (in centimeters) between the Items generated on the outer edge of the circle. |
| **Number Of Points** | The number of Items to be generated on a circle. |
| **Arc Direction** | Define the mode at which the arc direction is determined. You can choose between **Two Points**(direction from the location of one context to another) or **Rotation**(where the context's rotation will be used as a direction). |
| **Arc Angle** | Defines the angle at which the arc is measured in degrees. |
| **Circle Center** | The context used as the center for the circle. |
| **Ignore Any Context Actors when Generating Circle** | When enabled, ignore tracing into context Actors when generating the circle. |
| **Circle Center ZOffset** | Optional offset to apply to the context in the Z-axis. |
| **Trace Data** | Options related to how the trace is performed. **Trace Mode**: Shape used for geometry tracing. **Navigation Filter**: Navigation filter used for tracing. **Extent X**: Shape parameter for the trace. |
| **Projection Data** | If the resulting Items should be projected onto the NavMesh (and which NavMesh data set to use). |
| **Option Name** | This property is inherited from the base class of the Generator ActorsOfClass. It is mostly used when displaying the Name of this Generator (for example, HUDs or output messages). |
| **Auto Sort Tests** | If enabled, Tests will automatically be sorted for best performance before the query is run. |

## Points: Cone

![Cone Generator](https://dev.epicgames.com/community/api/documentation/image/bcad4d6f-8329-4300-aa2d-8a964824faaf)

The **Points: Cone** radiates a trace out from the **Center Actor**in the shape of a cone with the specified **Cone Degrees**as Items.

![Cone radiates a trace out from the Center Actor in the shape of a cone with the specified Cone Degrees as Items](https://dev.epicgames.com/community/api/documentation/image/0deb400c-e46e-4a2b-914c-ed13937f38b7)

| Property | Description |
| --- | --- |
| **Aligned Points Distance** | The distance between each point on the same angle. |
| **Cone Degrees** | Maximum degrees of the generated cone. |
| **Angle Step** | The step of the angle increase. Angle step must be greater than or equal to one. Smaller values generate fewer Items. |
| **Range** | Distance to generate the cone from the context. |
| **Center Actor** | The Actor (or Actors) that will generate a cone in their facing direction. |
| **Include Context Location** | Whether to include **Center Actor**locations when generating Items. |
| **Projection Data** | If the resulting Items should be projected onto the NavMesh (and which NavMesh data set to use). |
| **Option Name** | This property is inherited from the base class of the Generator ActorsOfClass. It is mostly used when displaying the Name of this Generator (for example, HUDs or output messages). |
| **Auto Sort Tests** | If enabled, Tests will automatically be sorted for best performance before the query is run. |

## Points: Donut

![Donut Generator](https://dev.epicgames.com/community/api/documentation/image/f870b9ea-008f-4dd3-9fe7-ebf1baf5360f)

The **Points: Donut**Generator, creates a shape-based trace with the user specified **Number Of Rings** radiating from the **Center**Context.

![Donut Generator, creates a shape based trace with the user specified Number Of Rings radiating from the Center Context](https://dev.epicgames.com/community/api/documentation/image/1cbecab4-8f44-4337-afbb-48966fa54528)

| Property | Description |
| --- | --- |
| **Inner Radius** | The minimum distance between point and context. |
| **Outer Radius** | The maximum distance between point and context. |
| **Number of Rings** | The number of rings to generate. |
| **Points Per Rig** | Number of Items to generate for each ring. |
| **Arc Direction** | Define the mode in which the arc direction is determined. You can choose between **Two Points** (direction from the location of one context to another) or **Rotation** (where the context's rotation will be used as a direction). |
| **Arc Angle** | Defines the angle at which the arc is measured in degrees. |
| **Use Spiral Pattern** | If enabled, the rings of the wheel will be rotated in a spiral pattern. If disabled, they will all be at a zero rotation, looking more like spokes on a wheel. |
| **Center** | The context to center the search on, such as from the Querier or perhaps some other context. |
| **Projection Data** | If the resulting Items should be projected onto the NavMesh (and which NavMesh data set to use). |
| **Option Name** | This property is inherited from the base class of the Generator ActorsOfClass. It is mostly used when displaying the Name of this Generator (for example, HUDs or output messages). |
| **Auto Sort Tests** | If enabled, Tests will automatically be sorted for best performance before the query is run. |

## Points: Grid

![Grid Generator](https://dev.epicgames.com/community/api/documentation/image/3636af36-9a6d-437b-9254-ac116b15d1f7)

The **Points: Grid**Generator will generate a grid of Items around the specified querier assigned under **Generate Around**.

![Grid Generator will generate a grid of Items around the specified querier assigned under Generate Around](https://dev.epicgames.com/community/api/documentation/image/20c1e9ef-f8ef-4f98-82a0-3609afebbf45)

| Property | Description |
| --- | --- |
| **GridHalfSize** | The height and width of the grid of Items to generate. |
| **Space Between** | The distance between the grid Items. |
| **Generate Around** | The context used to generate the grid around. |
| **Projection Data** | If the resulting Items should be projected onto the NavMesh (and which NavMesh data set to use). |
| **Option Name** | This property is inherited from the base class of the Generator ActorsOfClass. It is mostly used when displaying the Name of this Generator (for example, HUDs or output messages). |
| **Auto Sort Tests** | If enabled, Tests will automatically be sorted for best performance before the query is run. |

## Points: Pathing Grid

![Pathing Grid](https://dev.epicgames.com/community/api/documentation/image/07a8a99e-a2de-429e-a5ce-73352036cb5e)

You can use **Points: Pathing Grid**to generate a grid around the given Context location.

![Pathing Grid to generate a grid around the given Context location](https://dev.epicgames.com/community/api/documentation/image/35a53beb-ba5c-48f3-8cd1-9d2f7eda7add)

| Property | Description |
| --- | --- |
| **Path to Item** | If the pathfinding direction should be towards (enabled) or away (disabled) from the Item. |
| **Navigation Filter** | Navigation filter to use in pathfinding. |
| **GridHalfSize** | Half of square's extent (edge distance). |
| **Space Between** | Defines the generation density of points on the grid. |
| **Generate Around** | The context used to generate the grid around. |
| **Projection Data** | If the resulting Items should be projected onto the NavMesh (and which NavMesh data set to use). |
| **Option Name** | This property is inherited from the base class of the Generator ActorsOfClass. It is mostly used when displaying the Name of this Generator (for example, HUDs or output messages). |
| **Auto Sort Tests** | If enabled, Tests will automatically be sorted for best performance before the query is run. |
| **Scan Range Multiplier** | Multiplier for the max distance between point and context. |
