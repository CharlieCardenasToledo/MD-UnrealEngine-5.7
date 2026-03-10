# ML Deformer Framework

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ml-deformer-framework-in-unreal-engine

> Application Version: 5.7

The **Machine Learning** (**ML**) **Deformer** is a framework in **Unreal Engine** that you can use to obtain high-fidelity mesh deformations for characters and objects at runtime. Using an Alembic file (`.abc`), containing a set of desired mesh deformation data, you can train one of Unreal Engine’s ML Deformer models to make an approximation to this high quality mesh deformation with high performance at runtime.

The ML Deformer training process relies on three inputs:

1. A **Skeletal Mesh** asset.
2. An **Animation Sequence** asset of your character posed in different positions covering a wide range of motion
3. A **Geometry Cache** asset that contains the desired mesh deformations in those poses.

Using these three inputs, the ML Deformer framework outputs a trained **ML Deformer** asset which can be used in combination with the **ML Deformer Component** in a character's blueprint to select mesh deformations at runtime.

The ML Deformer Editor contains a suite of tools and settings that you can use to fine tune and test the training process to achieve high quality mesh deformations at runtime.

The following document is an overview of the ML Deformer Framework in Unreal Engine, including a reference material for the ML Deformer asset, the ML Deformer editor, and the ML Deformer Component. This document also includes infomation about the different ML Deformer models that are used to train the ML Deformer system, such as the **Neural Morph model** and **Nearest Neighbor model**.

#### Prerequisites

* The **ML Deformer Framework** is a [Plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine) and must be enabled prior to use. Navigate in the Unreal Engine menu to **Edit > Plugins**, locate **ML Deformer Framework** in the **Animation** section, and enable it. After enabling the plugin, you will need to restart the editor.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d66b38f9-4fd9-4541-894f-1fd863500e25/image_0.png)

* You have a character model, containing a mesh and a skeleton, that can be used in both Unreal Engine and Autodesk Maya.

## ML Deformer Setup Guide

To reference a comprehensive setup guide about using the ML Deformer framework to select high quality mesh deformations at runtime, see the **Using the ML Deformer** documentation.

## ML Deformer Editor

Here you can reference an overview of the ML Deformer Editor, and a breakdown of its panels and tools.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e2baa37b-01b1-47d1-bb13-cc26a29de3c2/image_1.png)

1. [Editor Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/ml-deformer-framework-in-unreal-engine#toolbar)
2. [Visualization Panel](https://dev.epicgames.com/documentation/en-us/unreal-engine/ml-deformer-framework-in-unreal-engine#visualizationpanel), used to inspect data. Settings in this panel don’t impact the trained model and are purely to visualize and inspect.
3. [Viewport](https://dev.epicgames.com/documentation/en-us/unreal-engine/editor-viewports-in-unreal-engine)
4. [Sequencer Timeline](https://dev.epicgames.com/documentation/404), used to control and scrub through training or test animation sequence playback.
5. [Details Panel](https://dev.epicgames.com/documentation/en-us/unreal-engine/ml-deformer-framework-in-unreal-engine#detailspanel), which contains all training related settings for the ML Defromer.

### Toolbar

Here you can reference a list of the ML Deformer Editor’s Toolbar, and a description of each tools function:

| Name | Tool | Description |
| --- | --- | --- |
| **Train Model** | ImageAltText | When selected this button will begin training the model using the properties in the ML Deformer Editor’s **Details** panel, to generate Morph Targets of your character’s mesh deformations.  This button will be disabled when training can not be performed, due to missing inputs or other errors. The exact errors will be reported in the UI as well. |
| **Model Selection** | ImageAltText | Here you can select the ML Deformer model you would like to use. You can select which model you would like to train the ML Deformer with from the available options in the drop down-menu. Changing the selected model will wipe your current session, so it is recommended to only change this right after creating a new ML Deformer asset.  The ML Deformer models available depend on the model plugins you have enabled. Each model type has its own plugin. |
| **Editor Mode** | ImageAltText | Here you can toggle the ML Deformer to either the **Training** mode or the **Testing** mode.   * The **Training** mode allows you to inspect your training data. You will find all training related settings in the **Details** panel. * The **Testing** mode is used to view the resulting deformation of the trained model. You can access testing and debug settings in the **Visualization** panel during testing. |
| **Tools** | ImageAltText | Here you can access the ML Deformer Editor’s Tools. Using the Drop Down Menu, select the tool to open each tool’s options where you can adjust its properties and run the operation. You can access the following tools using the Tools menu button:   * [Key Pose Extraction Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/ml-deformer-framework-in-unreal-engine#keyposeextractiontool) * [Get Neighbor Stats](https://dev.epicgames.com/documentation/en-us/unreal-engine/ml-deformer-framework-in-unreal-engine#getneighborstats)   The tools contained in this menu are currently mostly applicable when working with the **Nearest Neighbor** ML Deformer model.  For more information about the individual tools and a list of their properties and a description of their functionality, see their respective sections below. |
| **Debug Actor** | ImageAltText | Here you can select what Actor you would like to debug. By selecting an actor using the drop-down menu, you can view the deformations on an actor in an active Play In Editor (PIE ) session. After selecting an actor and world, the Actor in the ML Deformer Editor’s viewport will show the same pose as in your PIE session. Only actors using the currently opened ML Deformer asset can be picked to debug.  Projects often blend several animations together and do procedural modifications such as IK, debugging can be helpful, as you can test only with a single animation sequence in the ML Deformer editor when not debugging.  You can refresh the list of available actors for debug using the Refresh button in the toolbar. ImageAltText |

#### Key Pose Extraction Tool

When using the Nearest Neighbor ML Deformer model, you can use the Key Pose Extraction tool to extract key pose data from your characters training animation sequence, as well as generate geometry cache data. After making any property adjustments, use the **Extract** button at the bottom of the window to begin the operation.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cfdf284e-5abe-4c3f-be25-a721aafa0fb7/image_2.png)
