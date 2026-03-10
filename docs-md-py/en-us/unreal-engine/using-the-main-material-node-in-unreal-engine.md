# Using the Main Material Node

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-main-material-node-in-unreal-engine

> Application Version: 5.7

**Materials** are created using a specialized coding language called **High Level Shading Language** or HLSL. HLSL allows Materials to send instructions directly to the graphics hardware, giving artists and coders control over what is displayed on screen. Inside Unreal Engine 5 (UE5) the **Material Expression** nodes that are used to create Materials contain small snippets of this HLSL code.

The inputs on the **Main Material Node** are the last stop in a UE5 Material graph. Whatever combination of Material Expression nodes is connected to the inputs on the Main Material Node is what determines the overall appearance of the final Material when it is compiled and used in your Level.

![UE5 Main Material Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4d10e4fe-111a-4a32-b150-fa25bbe06453/main-material-node-ue5.png)

The Main Material Node with default inputs.

## Material Inputs

Each **input** on the Main Material Node defines a single unique aspect of the appearance and surface properties of your Material. For example, if you connect a **Constant3Vector** to the **Base Color** input and give it a value of (1,0,0), you can make the Material red.

![Vector 3 in Base Color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/53baddc5-8cf3-4408-b73f-c4eb595b4ee4/base-color.png)

This Material graph only explicitly defines a single aspect of the Material—its Base Color.

However, the overall appearance of the Material is the collective result of all the enabled inputs in the Main Material Node. Enabled input pins are white on the Main Material Node, and disabled inputs are grayed out.

![Enabled inputs in Main Material Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4a947be3-2c18-4840-9932-b1f4fdf22ff8/active-inputs.png)

Inputs that do not receive any data from Material expressions in the graph simply revert to their default values. For example, even though there is nothing plugged into Metallic, Specular, or Roughness, these properties still contribute to the appearance of the Material.

![Empty material inputs](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a67964db-9463-4d62-9738-bd7a085f1fe8/empty-inputs.png)

* **Metallic** defaults to 0 (non-metallic).
* **Specular** defaults to 0.5.
* **Roughness** defaults to 0.5.

Therefore, a Material with those values plugged into Metallic, Specular, and Roughness looks exactly the same as the one shown previously.

![Default values](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e296cabd-a72a-4e72-be5d-688be71d2d7e/default-no-inputs.png)
![Default Spec Metallic Roughness](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/42c8a0ae-2102-48ed-ae61-3d95560fc5f1/default-spec-metallic-roughness.png)
![New values in color and roughness](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1ff62541-d032-4d02-a238-26232ed12f43/new-values.png)

Slider: Note that the preview render does not change when default values are connected the the Main Material Node.

By changing the values, you can alter the appearance and surface properties of the Material. In the third image, the roughness value is changed from **0.5 to 0.07**, and the Material appears more polished. Changing the values in the **Constant3Vector** to **(0,0,1)** makes the Base Color blue instead of red.

### Understanding Material Inputs

UE5 uses a **Physically Based Rendering** (PBR) workflow for Materials, meaning Materials closely approximate the way surfaces interact with light in the real world. To create Materials effectively it is important to understand exactly how each input affects the final Material. These two pages provide foundational information about the PBR Materials workflow in Unreal Engine 5.

* Read the [Physically Based Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine) overview to learn best practices for creating Materials in a PBR workflow.
* Read the [Material Inputs](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-inputs-in-unreal-engine) page for examples and descriptions of what each input on the Main Material Node does.

### Enabled and Disabled Inputs

Some of the input pins in the Main Material Node are enabled by default, while others are disabled. The following properties in the **Details Panel** determine which inputs are enabled.

* Material Domain
* Blend Mode
* Shading Model

![Default Main Material Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/af693307-51cd-451d-8537-8839f389eeec/enabled-inputs.png)
