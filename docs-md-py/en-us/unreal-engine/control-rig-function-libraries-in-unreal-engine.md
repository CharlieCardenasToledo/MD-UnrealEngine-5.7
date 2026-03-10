# Control Rig Function Libraries

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-function-libraries-in-unreal-engine

> Application Version: 5.7

Similar to [Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine), you can share user-created functions between asset graphs by making the function "public". Unlike Blueprints, which only share functions to child classes, Control Rig functions can be shared project-wide. You can create custom function libraries, and share them with all Control Rig graphs in your project.

This document provides a guide for the best practices for creating function libraries in Control Rig, and shows how you can access the default engine-provided function library.

## New Function Library

The following steps will show you how to create and use a new Control Rig function library.

### Create Control Rig Container

As custom functions can only exist inside Control Rig Assets, the first step will be to create a Control Rig Asset. This Control Rig should not be linked to any particular Skeletal Mesh, as it will be used primarily to contain your functions.

In the [Content Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-in-unreal-engine), click **Add (+)**, then select **Animation > Control Rig**. In the **Create Control Rig Blueprint** dialog window, select **ControlRig** and click **Create**. Open the Control Rig after it is created.

![create control rig](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4ec9afad-26bc-4206-819a-a76d0842a919/createrig1.png)


For the purposes of this asset, your function libraries *are* Control Rig Assets, and do not include dependencies on any particular skeleton. As a container of functions, this allows for the asset to be as lightweight as possible.

### Create Public Function

In the [Control Rig Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-editor-in-unreal-engine), create a new function by clicking **Add (+)** on the **Functions** section of **My Blueprint**.

![create control rig function](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a72d9e45-b4b4-4135-a079-da0c7c72ea5b/createfunction1.png)

Next, select the function, and in the **Details** panel set **Access Specifier** to **Public**. This makes the function publicly accessible in all Control Rigs.

![public function](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/206a721e-e7f9-4470-89ff-c5cdd8ae874c/createfunction2.png)

### Setup Data in Function

From within your function, you can create any arbitrary contained logic you want, including metadata on the function such as tooltip descriptions and context menu categories.

In this example, **For Each** and **Set Control Visibility** nodes were created and connected to the function's **Entry** and **Return** nodes.

![function example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c988d2d-5ef3-461c-82a6-a4832f61eb44/functionsetup1.png)

To create variable inputs on the Entry node, select **Entry** and click **Add (+)** on the **Inputs** category in the **Details** panel. In this example, the following variables were created:

* **Rig Element Key**, as an **Array** type.
* **Boolean**, as a **Single** type.

![variable setup](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f9ee76da-b076-48bd-ac6e-32421aee4064/functionsetup2.png)

Next, connect the variable inputs to their corresponding nodes.

![variable connection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/83f768e6-bb87-4a02-af21-3035bfd5105c/functionsetup3.png)

Optionally, you can also edit the **Node Settings** properties in the **Details** panel to add categorization, tooltip, or other helpful properties to the function.

![function settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0079e5a2-ff39-4e9b-9133-d81697e24dbd/functionsetup4.png)

| Name | Description |
| --- | --- |
| **Category** | Filling this property puts the node within the named context menu category. This category is visible when adding the node in the Control Rig graph. |
| **Keywords** | Adds search terms you can use to find this function when searching for it using the context menu. |
| **Description** | Adds a tooltip description for this function. You can view the tooltip when hovering your cursor either on the context menu item, or on the node after it is added to the graph. |
| **Color** | Sets the color of the function node header. You can preview the look of your node by expanding the **Node Defaults** category. |

### Referencing the Function

To add your shared function in another Control Rig, right-click in the **Rig Graph** and add your function from the context menu. Shared functions also display their folder path in the node header for reference.

![add function](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e26e4ae6-a66f-451b-8872-532abe43fe35/functionref1.png)
