# Object Binding Track

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-actor-tracks-in-unreal-engine

> Application Version: 5.7

In Sequencer, you can add **[Static Mesh Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/static-mesh-actors-in-unreal-engine)**, **[Skeletal Mesh Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-actors-in-unreal-engine)**, and other kinds of Actors in order to animate them. All Actors in Sequencer are referenced by using the **Object Binding Track**, which enables access to their properties, components, and variables.

This guide provides an overview of the Object Binding Track, how bindings work with it, how to access Actor components within Sequencer, and how to work with automatic track creation.

#### Prerequisites

* You have an understanding of **[Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine)** and its **[Interface](https://dev.epicgames.com/documentation/404)**.
* You have an understanding of **[Blueprint Visual Scripting](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine)**.

## Creation

Object Binding tracks are created whenever you add an Actor to Sequencer through a variety of methods.

You can add Actors to your sequence by navigating within the **Track (+)** menu to the **Actor To Sequencer** submenu. From here you can choose any Actor currently in your Level to add to your sequence, or you can search for a specific Actor using the search bar.

![actor to sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/66aebe8f-f16f-465c-ba5d-86ccce453b3c/addactor.gif)


If an Actor is already selected in your Level, then it will be listed at the top of the **Actor To Sequencer** list for convenience.

You can also drag Actors from other windows, like the **[Outliner](https://dev.epicgames.com/documentation/en-us/unreal-engine/outliner-in-unreal-engine)** and add them into Sequencer.

![sequencer drag and drop actor add](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6b2e8a5c-d43f-4c46-b336-2688183d9b7e/addactor2.png)

### Binding

When Actors are added to Sequencer, the Object Binding Track is created and is bound to the chosen Actor. The binding enables certain property tracks and components to become available that are dependent on the Actor's class.

For example, when the track binds to a **[Skeletal Mesh Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-actors-in-unreal-engine)**, it enables the creation of the **[Animation Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-animation-track-in-unreal-engine)**, which is a track specific to the **Skeletal Mesh Component**.

![skeletal mesh actor component animation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dc3c70a1-e214-492f-81e1-3c049d669695/animationtrack.png)

Actor bindings can be changed or removed by right-clicking the track and navigating to the **Assign Actor** menu.

![assign actor bind](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/37eb8d49-855e-4a1f-8078-3f89d17af252/assignactor.png)

To change an Object Binding Track's binding, you can either choose the new Actor directly from the Actor list in the **Assign Actor** menu, or select the new Actor and click **Replace with Selected**.

![replace with selected](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5501e8bc-ee96-4751-bb89-23e81e1c77c3/replaceactor.gif)


When rebinding between different classes of Actors, any class-specific tracks will remain, but will no longer function unless the new binding contains a compatible component for the track.

To remove a binding, right-click the Object Binding Track, navigate to the Assign Actor menu, and select **Remove All**. You may also select **Remove Selected** if the same Actor is selected in the viewport.

![remove object binding](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/127e52b9-89df-43fd-93e8-5da516294edb/removebinding.png)

Bindings can also be changed with **[Blueprint Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine)**. You can locate binding functions when calling Blueprint functions from a Level Sequence reference object by navigating to **Sequencer > Player > Bindings**. From here you can choose to use explicit binding functions, such as **Set Binding**, or changing bindings [**By Tag**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-tags-and-groups-in-unreal-engine#tags).

![sequencer player bindings blueprints](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1c077d22-2294-49e3-be93-d452fc6c7d07/bindingbp.png)

### Multi Binding

Multiple Actors can also be bound to the track, enabling a single track to control several Actors at once. When more than one Actor is bound, the track is denoted with a **yellow chevron**, and the number of bound Actors is displayed in brackets next to the track name.

![multiple object binding](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3ab6f9e-527b-4ebf-9a45-89d7f57dc4f7/chevron.png)

Binding multiple Actors can be useful in situations where you want to change the properties of multiple Actors at once, such as when adjusting all lights in an area.

![multiple binding lights](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/427549df-17fb-4064-984b-c48bcda6160d/multilightsexample.gif)

You can also share data between multiple characters in your cinematic, then control their visibility during runtime, enabling conditional characters or objects to be visible when the scene plays.

![conditional characters multiple bindings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5005712b-9226-4e39-b794-c72496a27647/multiactorexample.png)

To bind multiple Actors to the same track, select your required Actors from the viewport, then right-click a currently existing Object Binding Track, and select **Assign Actor > Add Selected**.

![create multiple bindings sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4d5894b7-36ce-4316-bd5f-b19fc54f1491/multibind.gif)


You can bind Actors of different classes together, however you will only be able to access the components of the first bound Actor. Shared properties, such as [**Transform**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine#transformtrack), will still function correctly though.

## Accessing Components

Typically, Actors only have a single component, and the most often used properties for that component are filtered down when adding tracks to the Actor. You can access the full range of an Actor's properties by adding a component track, and adding properties from that component.

This is done by clicking the **Track (+)** dropdown on the Object Binding Track, and selecting the component from the **Components** category. Then click the **Track (+)** dropdown on the component track to view all available component properties.

![sequencer component properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b33247c1-1ed0-47f1-832f-f919ec5fa580/components.png)

Actor Blueprints, or Blueprints with multiple components can also have their components accessed in the same way. In this example, an Actor Blueprint contains a **Skeletal Mesh Component**, **Point Light Component**, and a **Camera Component**. These components and their subcomponents are accessible in the **Components** category when clicking the **Track (+)** dropdown.

![blueprint actor sequencer components](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f138afb-2062-4467-a330-a680a0f482e2/components2.png)

## Automatic Track Creation

When adding certain Actors to Sequencer, you may notice that tracks are automatically created with them. For example:

* **[Static Mesh Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/static-mesh-actors-in-unreal-engine)** will automatically create a [**Transform Track**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine#transformtrack).

  ![static mesh sequencer auto track](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7ad327a1-ec3b-45ab-aa63-76a57d8774d9/staticmesh.png)
* **[Skeletal Mesh Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-actors-in-unreal-engine)** will automatically create a [**Transform Track**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine#transformtrack) and an **[Animation Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-animation-track-in-unreal-engine)**.

  ![skeletal mesh sequencer auto track](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0f80e2d0-35c9-420e-8445-bba54e05aa30/skellymesh.png)
* **[Cine Camera Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine)** will automatically create a [**Transform Track**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine#transformtrack) and a **Camera Component** with **Aperture**, **Focal Length**, and **Focus Distance** property tracks.

  ![camera actor sequencer auto track](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c23ad0dc-48a6-4d4f-9c18-8c2cc4da83d9/cinecamera.png)
* **[Light Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine)** will automatically create a **Light Component** with **Intensity** and **Light Color** property tracks.

  ![lights sequencer auto track](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a5031eef-3739-4e09-8ea2-98eb268a2934/light.png)

This occurs because of the **Tracks Settings** located in the [**Sequencer Plugins Project Settings**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-editor-and-project-settings-in-unreal-engine#projectsettings). You can locate these settings by opening the **Project Settings** window, and locating **Level Sequencer** in the **Plugins** category.

![sequencer track settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/89b6d81e-c0af-4985-a5ae-1cb57392c999/projectsettings.png)
