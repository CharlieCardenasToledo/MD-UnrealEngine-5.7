# Temporal Super Resolution

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/temporal-super-resolution-in-unreal-engine

> Application Version: 5.7

**Temporal Super Resolution** (TSR) is a platform-agnostic [Temporal Upscaler](https://dev.epicgames.com/documentation/en-us/unreal-engine/temporal-upscalers-in-unreal-engine) that enables Unreal Engine to render beautiful 4K images. Images come at a fraction of the cost by amortizing some of the costly rendering calculating across many frames. TSR does this by rendering a lower internal resolution than what Temporal Anti-Aliasing Upsampling (TAAU) in Unreal Engine 4 could do.

TSR provides a native high-quality upsampling technique to meet the demand of next-generation games. It realizes the possibilities needed with the fidelity and details required by [Nanite](https://dev.epicgames.com/documentation/404) geometry while rendering frames at much lower resolutions to accommodate enough performance for [Lumen](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-global-illumination-and-reflections-in-unreal-engine).

The comparison below demonstrates the quality and performance differences between frames rendered at native 4K and those rendered at 1080p upscaled to 4K. With TSR, it's possible to achieve image quality near 4K resolution while also reducing GPU frame time by half.

![4k frames rendered at native 4K resolution. Frame Time: 57.50 ms](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bdccd6c1-0bb5-46f4-83ac-737e1b6c93fc/7-tsr-1.png)

![4k frames rendered at 1080p resolution. Frame Time: 33.37 ms](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5cc31808-34a8-45c3-a7c0-f75f254dda06/7-tsr-2.png)



These images are both 4K images. If you want to compare their fully uncompressed resolution, right-click on each and save them to your computer.

Temporal Super Resolution has the following properties:

* Rendered frames approach the quality of native 4K with input resolutions as low as 1080p.
* Less "ghosting" artifacts against high-frequency backgrounds than was visible with Unreal Engine 4's default anti-aliasing method, Temporal Anti-Aliasing.
* Reduced flickering on geometry with high complexity, such as those rendered with Nanite.
* Supports Dynamic Resolution scaling on console platforms.
* Runs on any hardware that supports D3D11, D3D12, Vulkan, Metal, PlayStation 5, and Xbox Series S | X with shaders specifically optimized for PlayStation 5 and Xbox Series S | X GPU architectures.

In the rendering chain, Temporal Super Resolution happens after depth of field and everything that follows is upscaled, such as motion blur, bloom, and so on.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c3aa09e5-8ad3-4db9-85cf-2a82269ca33b/8-pipeline-tsr.png)
