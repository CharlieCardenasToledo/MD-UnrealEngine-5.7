# Customized UVs

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/customized-uvs-in-unreal-engine-materials

> Application Version: 5.7

On GPU's, the vertex shader is run for every vertex, and the pixel shader is run for every pixel. Almost all the material nodes in Unreal Engine 4 are run for every pixel. While a **UV Coordinate** node can be either part of the vertex or pixel shader, the **CustomizedUVs** feature is only run in the vertex shader, and offers a performance increase over running the same calculations in the pixel shader. This offers an excellent way to speed up even just tiling a texture. While the system is not limited in the math you run on the UVs, the result will depend on the tessellation of your mesh.

Note: Customized UVs are currently only implemented for certain component types: Static Meshes, Skeletal Meshes, BSP, landscape, and mesh particles. Notably Sprite particles do not support Customized UVs yet.

## Properties

In the **Material Editor**, you can set the number of **CustomizedUVs** input pins by selecting the main material node and editing the **Num Customized UVs** property in the **Material** category. If **Num Customized UVs** is set to a number greater than 0, CustomizedUVs pins will show on the main material node.

![Customized UVs Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/19979182-c648-45ea-8e8d-2779110023ee/customized-uv-properties.png)

## Non-Linear Math

The general rule is that if the computation you are doing is using constants (camera position, time, vector parameters, etc.) or varies linearly with per-vertex attributes, then doing that work in the vertex shader will give the same results as doing them in the pixel shader. Varying linearly means only operations that will result in straight lines, no curves, such as multiplication and addition. Squaring a variable, using sine, cosine, or operations like `length` will result in a non-linear equation.

Whether or not non-linear math will produce a desirable result will depend on the detail of the mesh it is being applied to:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0bd30e75-a602-43d3-90d8-2b1022a2ac96/cuvs_highvslowdetailmesh.png)

*The mesh on the left is a 9x9 polygon grid, while the one on the right is a 4x4 polygon grid.*

Click to enlarge image.

In contrast, if this same math is directly inputted into a texture, it will be evaluated in the pixel shader producing the same result regardless of mesh detail.



Click to enlarge image.

## Linear Math

Scaling (multiplying) UVs by a parameter will work the same in both. The UVs are per-vertex attributes, and scaling is a linear operation. The images below show when doing linear operations, CustomizedUVs, which are calculated in the vertex shader, produce the same effect as doing the same calculation in the pixel shader.

![UV Tiling on Vertex Shader](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f161e89-55da-4a68-b52a-01fc49b06cb4/linear-math-01.png)
![UV Tiling on Pixel Shader](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/21fe34e8-699b-4e2d-a2e3-32ac3078f698/linear-math-02.png)

**In this example the result is the same whether the UV tiling is caluculated in the vertex shader (with customized UVs) or in the pixel shader.**

## How it works

The CustomizedUV pins pass through the texture coordinates (UVs) in the mesh by default. Then when you place a Texcoord node in a pixel shader input (like BaseColor), you are still getting the mesh's texture coordinates. However, if you do something in CustomizedUV0 and then use Texcoord 0 in the BaseColor input, you will get the modified UV value. Note that Texture sample nodes use TexCoord 0 by default.

**Shader Model 5** on PC can use 8 custom UVs, while **OpenGL ES2** on mobile can only use 3.

Here is an example, the original material is mapping a texture using world space y and z.

![Texture mapped in world space](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/af88441e-66f4-4b85-b955-9760cd3e970b/customized-uvs-example-01.png)
