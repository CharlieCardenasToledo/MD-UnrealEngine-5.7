# Material Data Types

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/material-data-types-in-unreal-engine

> Application Version: 5.7

Understanding how data is represented and manipulated in the [Material Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-editor-user-guide) is one of the principle concepts in Unreal Engine Material creation. The inputs on the [Main Material Node](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-main-material-node-in-unreal-engine), which define the physical attributes of a Material, are each programmed to accept a specific type of data. Similarly, many of the Material Expression nodes used to build Materials will fail to compile unless they receive a specific kind of data on their inputs.

This page provides an overview of the four data types available in the Material Editor and examples of how they are frequently used.

## Float Data Types

In computer graphics, a **float** is a data type that stores a single numeric value, positive or negative. Float is short for floating-point, which means the number contains a decimal place and does not need to be a whole number (or integer). Examples of float values might include 1.0, -0.5, or 2.0.

Ultimately all the data types in the Material Editor are variations of the float variable. Where they differ is in the quantity of values they store. Whereas a float represents a single number, a float2 stores two discrete floating-point values. For example: (1.0, 0.5).

The following table breaks down the four data types available in the Material Editor.

| Data Type | Material Expression(s) | Data Structure | Common Uses |
| --- | --- | --- | --- |
| Float | Constant, Scalar Parameter | (r) | Metallic, Roughness, arithmetic operations |
| Float2 | Constant2Vector | (r, g) | UV or XY coordinates, Scale |
| Float3 | Constant3Vector | (r, g, b) | Color (r, g, b) or 3D coordinates (x, y, z) |
| Float4 | Constant4Vector, Vector Parameter, Textures | (r, g, b, a) | Color with alpha channel, Textures (r, g, b, a) |

### Float

As described above, a **float** stores a single floating-point value. It can be positive or negative and contains a decimal place. There are two Material Expressions you can use to define a float.

#### Constant Material Expression

A **Constant Material Expression** node stores a single constant float value. Because it is a constant, this value does not change after the Material is compiled. The image below shows a Constant node which holds a value of **1.0**.

![Constant Material Expression](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5134eaf6-0a17-4323-b6a3-a2bae6c34802/constant-expression.png)

#### Scalar Parameter

A **Scalar Parameter** also stores a float. Unlike a Constant, the Scalar Parameter also becomes a named variable that you can modify in a Material Instance after the Material is compiled, or even at runtime. The image below shows a Scalar Parameter with a name of Roughness, and a default value of **0.6**. You could use this to define the Material's roughness attribute, while providing artists a way to override the value in a Material instance.

![Scalar Parameter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ff2264d-528f-4b1e-9ecd-231012ce9a86/scalar-parameter.png)

For more information about when and how to use Scalar Parameters instead of Constants, read the [Instanced Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine) documentation.

#### Examples

Certain inputs on the [Main Material Node](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-main-material-node-in-unreal-engine) are defined by a float. For example, the **Metallic**, **Specular**, and **Roughness** [inputs](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-inputs-in-unreal-engine) all accept a float value between 0 and 1. Therefore, you can pass a Constant Material Expression or Scalar Parameter directly into the Main Material Node to define these attributes.

![Scalar and Constant Material Expressions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3797e8de-f293-418c-8b29-bfed99382fd4/scalar-and-constant-example.png)

Constants and Scalar Parameters are often used to control the magnitude of some effect. Below, a Scalar Parameter named Emissive Power is multiplied by a solid color and passed into the **Emissive Color** input. Changing the value in the **Emissive Power** parameter makes the emissive output brighter or dimmer.

![Scalar parameter as Emissive Power](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/42f2c045-bb33-45d6-bd05-acb448a6a62f/scalar-multiplier.png)

### Float2

A **Float2** stores two numeric values. For example: (2.0, 3.0).

In the Material Editor, the **Constant2Vector** Material Expression is used to define a float2. Below, a Constant2Vector is shown with values of **2.0** and **3.0** in each of its two channels.

![Constant2Vector node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed163c7a-63c1-4c69-908c-a814342855ab/constant-2-vector.png)

#### Constant2Vector

The **Constant2Vector** is useful anytime you need to define or modify an attribute that requires two-channel data. In the details panel, the two values are labeled **R** and **G**, referring to the red and green channels in rgb color, but that is only one possible use. Coordinates (UV, XY) and scale (width, height) are other attributes you could define with a Constant2Vector.

In the example below, a Constant2Vector is added to a **Texture Coordinates** node to modify the position of the texture on a plane. In the first slide, the values in the Constant2Vector are (0, 0), so the texture position is unchanged.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b1145371-3f34-4031-a0e9-df6fbdc1912f/texture-coords-01.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0103bfed-5ef0-40ea-a144-61c45543d03e/texture-coords-02.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2242c951-e493-45b9-8a22-433479d8c5ab/texture-coords-03.png)

**The values in the Constant2Vector control the texture position.**

When the R value is changed to 0.5, the texture shifts along the horizontal axis, because it is being added to the U coordinate of the texture. This causes the texture to wrap around the left and right edges of the plane. When the G value is changed to 0.5, the texture shifts vertically. The center of the texture is now at the four corners of the plane.

### Float3

A **float3** stores three numeric values. In the Material Editor, the **Constant3Vector** node defines a float3.

![Constant3Vector node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/adaa2dfc-1fe3-4a95-a174-f8c1a6f2c17d/constant-3-vector-expression.png)
