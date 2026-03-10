# Material Data Manipulation and Arithmetic

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/material-data-manipulation-and-arithmetic-in-unreal-engine

> Application Version: 5.7

The [Material Data Types](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-data-types-in-unreal-engine) page introduced the four ways data is represented in the Material Editor. To create Materials effectively it is necessary not only to know these data types, but also how to manipulate data and control the way information travels through your Material Graph.

Two topics are discussed in this document.

1. [Manipulating data types](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-data-manipulation-and-arithmetic-in-unreal-engine#manipulatingdatatypes): How to combine floats into a multi-channel vector, and conversely, how to isolate information out of a larger data type.
2. [Material Graph arithmetic](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-data-manipulation-and-arithmetic-in-unreal-engine#materialgrapharithmetic): Rules and processes for performing arithmetic operations in a Material with different data types.

## Manipulating Data Types

Just because a piece of information originates as one data type does not mean it needs to stay that way. For example, you can combine or **Append** two Scalar Parameters (floats) into a two-channel vector (float2) in order to pass them into an input that requires two-channel data. Conversely, you can use a **ComponentMask** to retrieve a specific subset of channels out of a larger vector.

The Material Expressions documented in this section provide ways to combine and separate data to control the way information flows through your Material Graph.

### AppendVector

An AppendVector Material Expression combines the data in **Input A** with the data in **Input B**, and outputs a multi-channel vector (float2, float3, or float4). In this example, two Constants are appended together to output a float2: **(1, 2)**.

![AppendVector Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d5d67ebb-41e2-4f6b-b1be-14309dc5ed79/append-node.png)

#### Example Use Case

The Append node is often useful when you want the ability to modify two values independently of one another, but need to pass them into an input that requires multi-channel data. The graph below gives artists a way to control the Tiling or **UV scale** of a texture in a Material Instance, but only uniformly.

![UV Tiling controls uniform](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aa6c8b32-d29b-4dec-9a43-3ae148b512c2/tiling-uniform.png)

The shortcoming in this example is that the Material Graph only contains one parameter, but UV Coordinates have two channels. With this solution you cannot control the width and height of the texture independently.

You can solve this by using an **AppendVector**. Create a separate Scalar Parameter for each axis and then pass them into the Append node. The Append node combines the two parameters into a float2, which is then multiplied by the Texture Coordinates.

![UV tiling controls two-channel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d66d30cc-34f2-4d93-9e94-09fa71dfc567/append-vector.png)

Since **Tiling X** and **Tiling Y** are parameterized separately, you can now control the width and height of the texture independently.

#### Append Order

The AppendVector expression combines data in the order it is attached to the node. The data in Input B is always appended to the end of the data in Input A. Consider the two images below.

![Append order initial](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ce11d3bf-2b35-440e-8df5-a16eb8039603/append-order-01.png)
![Append order reversed](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8f3ef04b-2c39-4635-ade5-631b235b3cd0/append-order-02.png)

* In the first slide, the appended result is **(0.05, 0.2, 0.8)**, or light blue as the node preview shows.
* In the second slide, the appended result is **(0.8, 0.05, 0.2)**, or pink as the node preview shows.

### AppendMany

**AppendMany** is a [Material Function](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-functions-overview) that works the same way as the AppendVector expression, but can combine up to four separate float/scalar values into a multi-channel vector.

![AppendMany Material Function](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6ea0ecf5-3da3-4554-877d-05fc547ced71/append-many.png)
