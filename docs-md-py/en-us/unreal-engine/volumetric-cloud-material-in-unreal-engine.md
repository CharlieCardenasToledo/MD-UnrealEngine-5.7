# Volumetric Cloud Material

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-cloud-material-in-unreal-engine

> Application Version: 5.7

The [Volumetric Clouds](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-cloud-component-in-unreal-engine) component is driven by a volume material. This volumetric cloud material includes parameters in named categories that are simple, clear, and easy to understand when defining the types and shapes of clouds you want, and making them look like storm clouds.

## Recommended Workflow with the Volumetric Cloud Material

The material used for rendering clouds with the volumetric cloud component is located in the Engine Content folder under `Engine/EngineSky/VolumetricClouds`. The material is named `m_SimpleVolumetricCloud_Inst` and is derived from `m_SimpleVolumetricClouds`.

Making changes to any content in the Engine Content folder directly has an effect on any projects and components that references this material. For this reason, we strongly recommend you make material instances of this material in your project’s Content folder. This way, you can make many variations to support different cloud types and shapes without overwriting the original material that is used by default.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8893728c-e766-40e0-9e72-89382b556a76/vcm-scene.png)

Default look and location of Volumetric Cloud Shader in Blank Game Template.

## Cloud Material Instance Settings

When you open the Volumetric Cloud material instance or create one of your own from the original, you will find the parameters are grouped into categories that define the look, shape, and effects of different clouds.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/552eacd1-5631-4fc1-9bac-eef8982ca2c8/vcm-materialinstanceparameters.png)

Volumetric cloud parameter groups in a material instance.

### Cloud Layout

The **Cloud Layouts** parameters are broken into textures and cloud types. The textures define the shapes, location, and mask for the cloud material and parameters to control the different types of clouds.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/83ec7821-ec20-415f-b797-784c4ae5eab6/vcm-cloudlayout.gif)

Volumetric Cloud Shader Layout Parameters.

The cloud type parameters use color channels to align with different types of cloud formations. There are four types of cloud types aligned with the red, green, blue, and alpha channels of the cloud textures. These cloud types are:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |
| Stratocumulus | Altostratus | Cirrostratus | Nimbostratus (Storm) |

The Cloud Type section has the following settings:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/35fa69ed-1ba8-4e03-9252-9bfedaf1b520/vcm-cloudlayout-parameters.png)
