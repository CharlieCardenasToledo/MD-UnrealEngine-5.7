# Handheld AR Template Technical Reference

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/handheld-ar-template-technical-reference

> Application Version: 5.7

The Handheld AR Template is a starting point for creating augmented reality projects for iOS and Android devices. While the [Handheld AR Template Quickstart](https://dev.epicgames.com/documentation/en-us/unreal-engine/handheld-ar-template-quickstart-in-unreal-engine) provides the steps for setting up the template and deploying it on a mobile device, this guide will provide more technical guidance on how the template works, where its key features are implemented, and how to modify its functionality.

## Basics

The Handheld AR Template is displayed with two parts:

* The feed from the user's camera.
* The *virtual scene*, which exists in Unreal Engine's 3D world.

The user's camera feed is captured automatically when they start an **AR Session**, while the virtual scene is rendered on top of that. As a representation of the user, the [Pawn](https://dev.epicgames.com/documentation/en-us/unreal-engine/player-controllers-in-unreal-engine) contains logic for interacting with objects within the virtual scene, including planes defined by the initial scan and placeable objects. A HUD is overlaid on this composited display, providing configuration options and other tools.

For more information about the user journey for the Handheld AR Template, refer to the [Handheld AR Template Quickstart](https://dev.epicgames.com/documentation/en-us/unreal-engine/handheld-ar-template-quickstart-in-unreal-engine).

## Application Flow

The Handheld AR Template opens directly to **HandheldARBlankMap** both in the Editor and on application startup. This map does not feature any Actors apart from the helper Actors used to point to documentation on mobile device setup. Its main function is to override the Game Mode to **BP\_ARGameMode** so that the application will use the [Game Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine) classes that are responsible for running the application and setting up the virtual scene.

![The template project displaying HandheldARBlankMap](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e0e038f7-db61-4ac3-b974-ac439687415f/initialmap.png)

BP\_ARGameMode starts the player with **BP\_ARPawn**, which is responsible for initializing the UI by adding **BP\_MainMenu** to the user's viewport. Once BP\_MainMenu is set up, it provides a prompt to the user to start scanning the environment. This begins an **AR session** and displays the user's camera feed, then tells BP\_ARPawn to define a series of planes based on the available flat surfaces in the environment.

BP\_ARPawn uses a simple state machine to track what step of the user journey the application is currently on. This state machine tracks these factors:

* Has the user scanned their environment and set up planes in the virtual scene?
* Has the user selected a plane to interact with?
* Has the user placed an object on the selected plane?

Based on the user's progress through the user journey, the Pawn changes the way the application responds to their input and triggers prompts in the HUD to walk them through setup steps.

## Actors

### AR Pawn

The Handheld AR Template uses a custom Pawn called **BP\_ARPawn**. This Pawn is responsible for initialization, building and updating the virtual scene, and handling the user's input.

#### Initialization

The AR Pawn adds BP\_MainMenu to the user's viewport on BeginPlay. BP\_MainMenu is then responsible for setting up the AR scene and handling prompts based on the current state of the application.

#### State Control

The AR Pawn implements a simple state machine to support the different steps in the user journey outlined in the above sections. The state is controlled by a series of booleans under the **State** category.

![The booleans that control the state machine for this template](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f17791e9-4871-4ce5-9ed1-0c39e7c70636/statemachinebooleans.png)

These include:

* **ScanningIsDone**: The initial scanning process is complete and planes are placed in the virtual scene.
* **PlaneIsSelected**: The user has selected a plane.
* **ObjectIsPlaced**: The user has placed the virtual object on a plane and can now interact with it.

As the user follows the prompts from the HUD, these change from false to true, triggering the application to move to the next step in the user journey. The Pawn refers to these when processing touch input and when handling the Tick event to update the scene.

#### Camera Depth Scene Texture

The AR Pawn is also responsible for fetching the camera depth scene texture, which is used for placing objects in the virtual scene. This information is fetched as soon as the user gives the application permission to use the camera, but before the application completes its AR scan. The depth texture is stored in **CameraDepthTexture**, which is then used in the **Create Plane Candidate** function when the Pawn updates the visuals for planes. If CameraDepthTexture is not available, it uses **CameraDepthFallback** instead.

#### Light Intensity Estimation

During the Tick event, the AR Pawn calls the **Feed Light Estimate** function. This obtains current light estimate data from the AR session. If the data is valid, it updates the directional light and skylight in the map with color and intensity settings based on the camera feed. This creates lighting in the virtual scene that roughly matches lighting in the user's real-world environment.

#### AR Plane Creation

Once the AR session has finished scanning the environment, the AR Pawn begins updating the **PlaneCandidate** Actor in the virtual scene. This process checks to see if tracked objects in the environment fit valid **AR Plane Geometry**. Typically, a device's sensors can detect anywhere between five and twenty objects.

After that, the Pawn calls **Create Plane Candidate** to spawn a **BP\_Plane** Actor and place it in the appropriate location in the virtual scene. Plane candidates are updated once per second. To reduce visual complexity on screen, this process is set up so that the AR Pawn only tracks one plane candidate at any given time, favoring the closest object tracked by the AR session. As the user moves around the environment, they will see different plane candidates appear and disappear.

When the user selects a plane candidate, the BP\_Plane is locked in place as the **SelectedPlane** instead.

#### Gesture Processing and Manipulating the Virtual Scene

The AR Pawn is the only blueprint that consumes input, so it is responsible for all gesture recognition.

The **InputTouch** event handles single-touch inputs for either selecting a plane or placing a virtual object, depending on whether or not the user has a plane selected. Because two-finger gestures and swipes are not available until the user selects a virtual object, this touch input is very simple and does not require any special input actions.

![The InputTouch Event](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/11d952b3-75bf-442b-a70b-86279f342564/inputtouchevent.png)

After the user has both placed a plane and selected a virtual object, input is handled by the **OneFingerAction** and **TwoFingerAction** input actions, as well as an input axis called **TwoFingerMapping**. These are defined in the input bindings under **Project Settings > Input**.

![Input Actions displayed in the Project Settings menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7c8049eb-7b8d-4f36-a367-280fb2f45b02/inputactions.png)

The OneFingerAction and TwoFingerAction input actions are represented with events in the AR Pawn's event graph. These events do not trigger any functions when interacting with planes and objects. Instead, they record data that the AR Pawn can use to pick what type of gesture is appropriate during general input handling.

![Input Actions displayed in the AR Pawn's blueprint graph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/40aa843c-e1b5-4620-8d21-38651d8db14f/inputactionsarpawn.png)

The Tick event calls **Reset Recognized Gesture** to clean up information about previous gestures, then calls the **One Finger Gesture Recognition** and **Two Finger Gesture Recognition** functions to process the data gathered from the input action events. This includes the deltas for position, direction, and travelled distance of touch inputs.

These functions set an enum for the appropriate gesture, called **Current Transformation**. A switch on Current Transformation then chooses whether to use the Translate, Rotate, or Scale functions on the selected placeable object. The object itself handles these transformation functions.

![Gesture controls displayed in the AR Pawn's blueprint graph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/448f5ae5-37d4-4e7e-a7a9-abe70f3c04de/inputgesturecontrols.png)

### Placeable Objects

![An example of a placeable object](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2adfe810-d522-4d47-b97d-ce3b667dc152/placeableobjectexample.png)

The **BP\_Placeable** blueprint is the base class for all placeable objects in the Handheld AR Template, including planes. It encapsulates everything related to a placeable virtual object: visuals, transformation logic, and HUD interaction logic with a widget component. On BeginPlay, the placeable object will choose an asset based on what type of product you are creating with the **Assign Product Asset** function. The model selected depends on the category you choose when setting up the template.

| Application Category | Model |
| --- | --- |
| Games | Games placeable object |
| Automotive, Product Design, and Manufacturing | Automotive placeable object |
| Architecture, Engineering, and Construction | Architectural placeable object |

#### Controlling Visuals

Placeable objects use the **Set Visuals** function to control the display of both the model's materials and the UI widgets displayed alongside them. This function is called from **Set Placeable Position**, **Set Placeable Rotation**, and **Set Placeable Scale**.

If an interaction is active, the Tick event will call **Update Interaction**. This function will update the placeable object's UI widget with new information based on how the user moves, rotates, or scales it. There are several utility functions for getting text appropriate to each transformation.

#### Placing Objects on AR Planes

The AR Pawn spawns a BP\_Placeable actor from the Input Touch event and assigns it to the **Placeable Object** variable.

### AR Planes

The Handheld AR Template represents virtual planes with BP\_Plane actors. These are created by the AR Pawn using the **Update Plane Candidate** and **Create Plane Candidate** functions. Create Plane Candidate in turn calls **Initialize Plane**, which handles setup of BP\_Plane's materials and color.

The static mesh attached to BP\_Plane is a simple plane consisting of two triangles, with complex collision turned on and the **Collision Presets** set to **BlockAllDynamic**. This makes it possible to detect the surface of the plane with any type of trace.

The default state of a BP\_Plane actor is its unselected state. In this state, it uses **DM\_Scan** as its material instance, displaying ripples to indicate that the device is currently scanning the environment.

![BP_Plane using DM_Scan as its material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3c717cd1-62a2-4c87-aaa3-d42e6231dc9c/scanningmaterialexample.png)
