# Shading Models

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/shading-models-in-unreal-engine

> Application Version: 5.7

Shading Models control how your Material reflects incoming light. Or, put another way, it controls how the input data that makes up the Material is used to create the final look.

![Shading Models drop-down menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4f84c669-276f-4ab1-8d36-49164bf0688c/shading-models.png)

Unreal Engine has many **Shading Models** designed to achieve specific looks for the Materials you set up. For instance, the **Default Lit** Shading Model is a general purpose model you will likely use for most of your surfaces. Unreal also includes Shading Models designed for specific surface types. For example, the **Clear Coat**, **Hair**, and **Cloth** Shading Models are tailored to provide natural results for those specific types of Materials.

## Unlit

The **Unlit** Shading Model only outputs Emissive for color, making this perfect for special effects such as fire or any light emitting object. Note that in this example, the Material is not casting light into the scene. Instead, its high Emissive value results in a glow effect, which is also picked up by the dirt mask applied to the camera. It appears to illuminate, but no lighting or shadows are cast by this object. Emissive Materials can cast light into the scene if Lumen is enabled, or with Lightmass when [Use Emissive for Static Lighting](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-emissive-material-input-in-unreal-engine#emissivematerialswithstaticlighting) is turned on.

![Unlit example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6ad228af-59ef-4ab6-aca0-1f3cc7dee5f1/unlitexample.png)

When using the Unlit Shading Model, you have access to the following inputs:

* Emissive Color
* World Position Offset
* Pixel Depth Offset

## Default Lit

**Default Lit** is the default shading model and is likely the one that you will use most often. This shading model makes use of direct and indirect lighting, as well as specularity for reflections.

![Default Lit Shading Model](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/55b49956-c620-4a87-9b51-ffd0af5fc5e9/defaultlitobjects.png)

When using the Default Lit Shading Model, you have access to the following inputs:

* Base Color
* Metallic
* Specular
* Roughness
* Emissive Color
* Normal
* World Position Offset
* Ambient Occlusion
* Pixel Depth Offset

## Subsurface

The **Subsurface** Shading Model simulates the effect of subsurface scattering. This is a real-world phenomenon in which light penetrates a surface and then diffuses throughout it. Subsurface scattering is readily apparent on objects such as ice, wax candles, and skin.

The Subsurface model (as well as the Preintegrated Skin model described below) relies on the **Subsurface Color** input. This input defines the color of the matter just beneath the surface of the object. When light scatters through the surface, the Subsurface Color becomes visible.

For human skin, you can often get good results using a dark red color, which simulates blood circulating beneath the surface. In the Ice Elemental below, a dark blue-green color (with a variety of calculations based on lighting) is used to give a sense of translucent depth to the surface.

For more information, see the [Subsurface Shading Model documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/subsurface-shading-model-in-unreal-engine).

![Ice subsurface scattering example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/47c25b0f-23c6-4eb0-97f9-cdfbd4a48c82/iceelemental.png)

When using the Subsurface Shading Model, you have access to the following inputs:

* Base Color
* Metallic
* Specular
* Roughness
* Emissive Color
* Opacity
* Normal
* World Position Offset
* Subsurface Color
* Ambient Occlusion
* Pixel Depth Offset

## Preintegrated Skin

The **Preintegrated Skin** Shading Model is very similar to the Subsurface model, but prioritizes lower performance cost while sacrificing some accuracy. While not physically perfect, this Shading Model often gives nice results for human skin with better performance than the Subsurface method. In the image below, the character's flesh uses the Preintegrated Skin Shading Model.

![Infiltrator demo preintegrated skin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7d336589-8c60-4078-adfd-69c607f1f8cc/infiltratorpreintegrated.png)

When using the Preintegrated Skin Shading Model, you have access to the following inputs:

* Base Color
* Metallic
* Specular
* Roughness
* Emissive Color
* Opacity
* Normal
* World Position Offset
* Subsurface Color
* Ambient Occlusion
* Pixel Depth Offset

## Clear Coat

The **Clear Coat** Shading Model is used to better simulate multilayer Materials that have a thin translucent layer of film over the surface of a standard Material. This Shading Model was specifically designed to model smooth colored films over a non-colored metal. However, you can use this Shading Model with both metal and non-metal surfaces.

Some examples include acrylic or lacquer clear coats, and colored films over metals such as soda cans and car paint.

![Clear coat Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a9c4c49c-f3d7-4bf8-90b8-103a925c49fe/clearcoat_1.png)

Note that the flecks were done in the Material Editor and are not part of the Shading Model

### Dual-Normal Clear Coat

The Clear Coat Shading Model also has an option to add a second Normal Map for the surface that is below the clear coat layer. This enables the Material to more accurately model complex Materials such as carbon fiber and car paints, which have a different geometric or reflective surface than the clear coat layer.

|  |  |
| --- | --- |
| Clear Coat with Bottom Normal | Photograph of real-world Clear Coat Material |
| Clear Coat with Bottom Normal | Actual Photograph |

When using the Clear Coat Shading Model, you have access to the following inputs:

* Base Color
* Metallic
* Specular
* Roughness
* Emissive Color
* Normal
* World Position Offset
* Clear Coat
* Clear Coat Roughness
* Ambient Occlusion
* Pixel Depth Offset

## Subsurface Profile

The [Subsurface Profile Shading Model](https://dev.epicgames.com/documentation/en-us/unreal-engine/subsurface-profile-shading-model-in-unreal-engine) is very similar in nature to both the Subsurface and Preintegrated Skin Shading Model, but it is geared towards higher-end skin rendering. If you are trying to simulate skin, especially human skin, this is the highest quality Shading Model to use for that purpose.

![Standard Shading](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/611fc72d-d1c2-4cf5-9839-8a393cdc1ac9/results_1.png)

![Subsurface Profile Shading](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c156dedf-8775-4992-ac55-4bba279f2991/results_2.png)

When using the Subsurface Profile Shading Model, you have access to the following inputs:

* Base Color
* Metallic
* Specular
* Roughness
* Emissive Color
* Opacity
* Normal
* World Position Offset
* Ambient Occlusion
* Pixel Depth Offset

## Two Sided Foliage

The **Two Sided Foliage** Shading Model allows light transmission through the surface of the Material creating natural, uniform looking results, like light passing through the leaves of a tree. The subsurface color is used to define the amount of light transmission and is used for creating masks for things such as the stems and veins of the leaves.

The Two Sided Foliage Shading Model helps eliminate some issues present in the [Subsurface](https://dev.epicgames.com/documentation/en-us/unreal-engine/shading-models-in-unreal-engine#subsurface) scattering model, which works well on skin or thicker surfaces, but is not as accurate for thin surfaces like leaves. Similarly, using the **Default Lit** shading model for foliage can lead to incorrect looking results. In the example below, the Default Lit result appears almost black on the underside surfaces because it does not simulate any sort of light transmission, which is critical for natural looking foliage.

![Default Lit](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f1c12574-74d6-4ba9-af6e-a19412c79d06/twosidedfoliage_defaultlit.png)

![Two Sided Foliage](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d26aca51-10f8-4f8a-ad68-cdff9039d91f/twosidedfoliage_enabled.png)

When using the Two Sided Foliage Shading Model, you have access to the following inputs:

* Base Color
* Metallic
* Specular
* Roughness
* Emissive Color
* Normal
* World Position Offset
* Subsurface Color
* Ambient Occlusion
* Pixel Depth Offset

## Hair

The **Hair** Shading Model enables you to create natural looking hair that simulates multiple specular highlights: one representing the color of light, and another representing a mix of hair and light color.

![Hair shading model example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/209ce7c6-8488-4571-aba5-5e25b3ca32e0/hair_scraggle.jpg)
