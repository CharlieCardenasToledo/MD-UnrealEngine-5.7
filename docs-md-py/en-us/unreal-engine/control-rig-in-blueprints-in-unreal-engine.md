# Control Rig Component

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-in-blueprints-in-unreal-engine

> Application Version: 5.7

**Control Rig** can be called in Blueprints using the **Control Rig Component**. Using this component, you can drive Control Rigs with gameplay logic in Blueprints, reinitialize Control Rigs to fit differently proportioned characters, and attach non-skeletal mesh objects to the Control Rig hierarchy.

This document provides an overview of the Control Rig Component, how to add it to your Blueprint, and the features it enables.

#### Prerequisites

* You have created a Control Rig asset for a character and know how to create controls. See the **[Control Rig Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-create-control-rigs-in-unreal-engine)** page for information on how to do this.
* You have created an **Actor Blueprint** that contains a skeletal mesh component, and have an understanding of **[Blueprints Visual Scripting](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine)**.

## Component Setup

The **Control Rig Component** is created by clicking the **Add (+)** button in the Blueprint Components panel and selecting **Control Rig** in the **Animation** category.

![create control rig component](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/204272d7-8a19-4d5c-b0fe-f907c6b32d1b/addcomponent.png)

Next, select the **Control Rig Component** and assign your default **Control Rig Class** in the **Details** panel. Click the dropdown menu next to Control Rig Class and assign your class.

![control rig class](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bce65278-78ea-48cf-9d7e-df841ef00e8c/class.png)


After assigning the Control Rig Class, bones from the Control Rig will be visible in the viewport. You can hide these by disabling **Draw Bones** in the Control Rig Component Details panel.

![draw bones](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/542cac33-3c9b-46f4-a9cf-b6c0506c24c1/drawbones2.gif)

### Mapping Setup

Lastly, you will need to **map** the Control Rig to the Skeletal Mesh, which must be done on the **Pre Initialize Event** from the Control Rig Component. This is done to form the connection between the **Skeletal Mesh Component** and the **Control Rig Component**.

With the Control Rig Component selected, click the **Add (+)** button next to **On Pre Initialize** in the Details panel. This will create the corresponding event in the Event Graph.

![on pre initialize event](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2dd9a962-94d5-4cac-b3ff-fdf0919ca69a/preinitial.png)

Next, drag from the **Component** pin and select **Add Mapped Skeletal Mesh** from the context menu. Add a reference to your Skeletal Mesh Component, and connect it to the **Skeletal Mesh Component** pin.

![add mapped skeletal mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/451c5e8d-53aa-4717-bc31-fb3b5d7ddb3e/mapping.png)

## Overview

Once you have completed the [**Component Setup**](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-in-blueprints-in-unreal-engine#componentsetup), you can start using the Control Rig Component in your blueprints. With it, you can use basic functions, such as getting or setting **[Rig Elements](https://dev.epicgames.com/documentation/en-us/unreal-engine/controls-bones-and-nulls-in-control-rig-in-unreal-engine)**, editing details, and creating new mapping connections.

![control rig functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a4657d7b-1798-45c6-bf20-38515c56864a/overview.png)

### Details

The following is the list of relevant details of the Control Rig Component:

| Name | Description |
| --- | --- |
| **Control Rig Class** | The Control Rig Class to instantiate. A Control Rig asset must be specified here. |
| **Mapped Elements** | This array is used to manually define default mappings for the Control Rig |
| **Reset Transform Before Tick** | Enabling this will cause Control Rig transforms to update before each tick. |
| **Reset Initials Before Setup** | Enabling this will cause the initial transforms on Bones, Nulls, and Controls to reset prior to the **Setup Event**. |
| **Update Rig on Tick** | Enabling this ensures the rig will update when the component ticks. |
| **Update in Editor** | Allows for Control Rig behavior to be visible in the viewport without needing to play or simulate. |
| **Enable Lazy Evaluation** | Enabling this will make the Control Rig only evaluate if any of the mapped inputs have changed. |
| **Position Threshold** | The position or translation threshold to use when **Lazy Evaluation** is enabled. |
| **Rotation Threshold** | The rotation threshold in degrees to use when **Lazy Evaluation** is enabled. |
| **Scale Threshold** | The scale threshold to use when **Lazy Evaluation** is enabled. |
| **Draw Bones** | Enables drawing bones imported from the **Control Rig Class**. draw bones |

### Events

Control Rig can call the following events from the Control Rig Component. These events can be added to the Event Graph by either selecting the Control Rig Component and navigating to the **Events** category in the Details panel, or by right-clicking in the Event Graph and selecting **Add Event for Control Rig > Control Rig**.

![control rig blueprint events](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/053fed63-5267-40a0-96d9-8aa9799bfad9/events.png)
