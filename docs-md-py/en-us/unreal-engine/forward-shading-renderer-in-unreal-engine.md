# Forward Shading Renderer

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/forward-shading-renderer-in-unreal-engine

> Application Version: 5.7

By default, Unreal Engine uses a Deferred Renderer as it provides the most versatility and grants access to more rendering features.
However, there are some trade-offs in using the Deferred Renderer that might not be right for all VR experiences.
**Forward Rendering** provides a faster baseline, with faster rendering passes, which may lead to better performance on VR platforms.
Not only is Forward Rendering faster, it also provides better anti-aliasing options than the Deferred Renderer, which may lead to better visuals.

## Enabling Forward Shading

To enable the Forward Shading Renderer:

1. In the **Edit** menu, open the **Project Settings**.
2. Select the **Rendering** tab on the left and locate the **Forward Shading** category.
3. Enable **Forward Shading**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eab4247a-87d1-411a-b12e-feea4a4924f7/enableforwardshading.png)

You will be prompted to restart the editor where after the restart, you can begin using the Forward Renderer options and features.

## Enabling Multisample Anti-Aliasing

To use Multisample Anti-Aliasing (MSAA):

1. In the **Edit** menu, open the **Project Settings**.
2. Select the **Rendering** tab on the left and locate the **Default Settings** category.
3. Set the **Anti-Aliasing Method** property to **MSAA**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8d7bf6f1-c962-4c2e-bcb7-87ca6a695781/enablemsaa.png)

The forward renderer supports both MSAA and Temporal Anti-Aliasing (TAA) and in most cases, TAA is preferable because it removes both geometric aliasing and specular aliasing.
In VR however, the constant sub-pixel movement introduced by head tracking generates unwanted blurriness, making MSAA a better choice.
Projects that choose to use MSAA will want to build content to mitigate specular aliasing.
Additionally, the **Normal to Roughness** feature can help reduce specular aliasing from detailed normal maps and automatic LOD generation for static meshes can flatten features on distant meshes to help reduce aliasing from small triangles.

In our tests, using MSAA instead of TAA increases GPU frame time by about 25% (actual cost will depend on your content).

Below an example is given with Temporal AA enabled versus 4X MSAA enabled.

![With Temporal AA](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/84368f4e-2515-42ce-8105-2ef1a4126a75/temporalaa.png)

![With 4X MSAA](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c417b2c-074e-411a-9de4-cbfcfcb7de54/msaa.png)



You can use the console variable `r.MSAACount` to control how many MSAA samples are computed for every pixel. `r.MSAACount 1` disables MSAA.
Assigning `r.MSAACount 0` will fall back to using Temporal AA, which allows for convenient toggling between Anti-Aliasing methods.

## Performance and Features

Switching from the Deferred Renderer to the Forward Renderer may provide you with an increase in performance for your project.

The forward renderer can be faster than the deferred renderer for some content. Most of the performance improvement comes from features that can be disabled per material.
By default, only the nearest reflection capture will be applied without parallax correction unless the material opts-in to High Quality Reflections, height fog is computed per-vertex, and planar reflections are only applied to materials that enable it.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8cb0e8b-611b-4048-8f59-66cc7b5fb1b8/forwardshading.png)
