# Volumetric Cloud Component

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-cloud-component-in-unreal-engine

> Application Version: 5.7

The Volumetric Cloud component is a physically-based cloud rendering system that uses a material-driven approach to give artists and designers the freedom to create any type of clouds they need for their projects. The cloud system handles dynamic time-of-day setups that is complemented by the [Sky Atmosphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/sky-atmosphere-component-in-unreal-engine) and [Sky Light](https://dev.epicgames.com/documentation/en-us/unreal-engine/sky-lights-in-unreal-engine) using the real time capture mode. The system provides scalable, artist-defined clouds that can adapt to projects using ground views, flying, and ground to outer space transitions.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a75c0db7-50bb-4aab-a6e3-ea7a91d0cc2c/vt_cloudexamples.png)

## How are clouds rendered?

Previously, rendering clouds in real-time for games and cinematics have primarily been achieved through static materials applied to a sky dome mesh or a similar approach. Now, the volumetric cloud system uses a three-dimensional volume texture that is ray-marched to represent cloud layers in real-time. The material-driven approach provides the most flexibility for artists and designers to create clouds that can move across the sky, of any type, and can handle different times of day.

The sections that follow explore and break down the cloud system's elements that contribute to rendering them for real-time rendering.

### Ray Marching the Cloud Volume

The participating media that makes up clouds require complex lighting simulations that either aren't possible, or are too expensive, for real time simulation on consumer-grade hardware. The Volumetric Cloud system employs ray- marching and approximation to simulate cloud rendering for scalable real-time performance across many supported platforms and devices. This makes it possible to support real time time-of-day simulations that support the multiple light scattering effect of lighting, shadowing from clouds and onto clouds, light contribution from the ground onto the bottom layer of clouds, and much more.

### Light Multiple Scattering

Light rays that travel through a volume have the potential to scatter on particles within the volume before reaching your eye, or a camera sensor. This effect of light is called multiple scattering, and it is what defines the distinct appearance of clouds. In a cloud, the droplets that make up the cloud usually lead to an albedo that is close to a value of 1, meaning that light is almost never absorbed within the volume. Light that is not absorbed passes through the volume making the scattering effect very complex in the process. The multiple scattering effect of the participating media affects light travel through the cloud volume; it's what makes them look bright while also appearing very thick.

The complexity of multiple scattering in real-time rendering is solved by using an approximation of realistic scattering by tracing multiple octaves (or steps) of light transmittance in the volume material. The **Volumetric Advanced Material Output** expression enables you to set the number of octaves used along with the amount of multiple scattering contribution, occlusion, and eccentricity that happens.

The example below shows the difference between no octaves used (single scattering), one octave, and two octaves of multiple scattering approximation. High octaves apply additional scattering approximations to your cloud material but make the shader more expensive in the process.

For games projects, it is recommended to only use a single octave of light multiple scattering for performance considerations. However, you can use high Contribution and low Occlusion values on the **Volumetric Advanced Material** expression in your cloud material to similar effect without impact to performance. See the Volumetric Material section below.

**Ground View:**

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea32a389-202c-4268-8536-59ab759fb449/octaves_groundview_0.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8305906b-e061-4e52-9705-de14f457265a/octaves_groundview_1.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3f09cedd-4c0c-48de-ae19-bb215ce8170c/octaves_groundview_2.png)

Drag the slider to change the number of Multiple Scattering Approximation Octaves used from 0 - 2.

**Higher Altitude View:**

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c5ad0755-cb2a-410e-b9ec-0346215fb7ff/octaves_cloudview_0.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a3f283ad-8784-42d8-a654-f09a6d0f2876/octaves_cloudview_1.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a5c263f3-6795-41d9-bdb1-66dfde255dd2/octaves_cloudview_2.png)

Drag the slider to change the number of Multiple Scattering Approximation Octaves used from 0 - 2.

### Cloud Occlusion and Shadowing

An important aspect of clouds is due to how they occlude light and cast shadow on surfaces. Cloud occlusion and shadowing is primarily handled by atmosphere lights and the volume material used to represent the cloud. These components enable you to control different aspects that define the look of your clouds, such as having sunlight shafts, or cloud self shadowing.

#### Volume Ray Marching and Shadow Maps

There are two modes for cloud shadowing available which can be toggled in the cloud material used; the default **Ray Marched** and **Beer Shadow Maps** (BSM).

![Ray Marched](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5674a151-a062-4658-8a96-6a1a56132e63/shadows_raymarched.png)

![Beer Shadow Maps](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1c9ba6e8-7f50-4562-8483-77b747ddcd42/shadows_beershadowmaps.png)

* **Ray marching the volume shadow** uses secondary ray marching to get sharp, colored shadows but is limited in distance that shadows can be traced due to the limited number of samples that can be used. Ray-marched shadows are good for ground to sky to space transitions even though they are more expensive.
* **Beer shadow maps** use cascaded shadow maps to support far shadow distances for clouds and casting shadows on the ground. They are also faster to render, but are less accurate and lack volumetric self shadow color. Beer shadow maps are usually enough for clouds viewed from the ground.

For console platforms, such as Xbox One and PlayStation 4 or other systems using similar specifications, Beer shadow maps are recommended for cloud shadowing.

Toggle between these modes inside of your cloud volume material by adding a **Volumetric Advanced Material Output** expression to your material graph. With the node selected, toggle the **Ray March Volume Shadow** checkbox from the Details panel to switch between two types of shadowing.

![Cloud shadowing mode selection from Details panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/32d076a5-6649-4d61-94ec-bf867ee2bcc0/material-shadows-type-selection.png)
