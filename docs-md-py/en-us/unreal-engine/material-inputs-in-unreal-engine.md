# Material Inputs

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/material-inputs-in-unreal-engine

> Application Version: 5.7

This page documents all the available inputs on the Main Material Node. By feeding data (by way of constants, parameters, and textures) into these inputs, you can define the surface properties of your Material and create an almost infinite variety of physical surfaces.

Not all inputs are required for every Material, and some Material types require inputs that are not visible on the Main Material Node by default.

## Inputs and Material Properties

When you change certain Material properties in the Details panel, you will notice that some inputs on the Main Material Node turn white (indicating that they are enabled), while others are grayed out.

Three material properties control which inputs are enabled in the Material:

* **Blend Mode** - This controls how your Material blends with the pixels behind it.
* **Shading Model** - This defines how light is calculated for the surface of the Material.
* **Material Domain** - This dictates how the Material is intended to be used. For instance, whether it is meant to be part of a surface, a Light Function, or a Post Process Material.

If an input you need for your Material is disabled, it is because one or more of the above properties is set incorrectly. For example, if you are trying to make a pane of glass, but the opacity input is disabled. The solution in that example is to change the **Blend Mode** to **Translucent**.

## Base Color

Base Color defines the overall color of the Material. In principle, Base Color should represent the diffuse light reflected off a surface, minus any specular reflections/highlights.

If taken from the real world, base color textures should be photographed using a polarizing filter. Polarization removes the specular of nonmetals when aligned.

![Base Color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e93bf7b7-94c0-4548-b011-17315b208d62/base-color.png)

## Metallic

The Metallic input controls how 'metal-like' your surface will be. Metallic accepts any value between 0 and 1, but in a majority of cases Metallic is considered an either/or property.

* Nonmetals have a Metallic value of 0.
* Metals have a Metallic value of 1.

For pure surfaces, such as pure metal, pure stone, or pure plastic this value will be 0 or 1, not anything in between. When creating hybrid surfaces like corroded, dusty, or rusty metals, you may find that you need some value between 0 and 1.

![Metallic Value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8eae3894-43a8-4f4c-9b05-6707f0fb8e74/metallic-slider-00.png)
![Metallic Value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61502971-7603-49a3-9b6c-29b144770705/metallic-slider-05.png)
![Metallic Value 1](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/598fa6c5-35b4-4d18-ad8b-e66fda094ce7/metallic-slider-10.png)

**Metallic values of 0, 0.5, and 1.**

When using metallic masks, the values in the texture should be pure black or pure white. Only use grayscale values if you specifically mean to create a blend (corroded metal, for example).

## Specular

Specularity is a measure of how much light a surface reflects. The Specular input takes a value between 0 and 1, and defines the extent to which a surface is reflective:

* **Value of 0** - Fully non-reflective
* **Value of 1** - Fully reflective
* The default value is 0.5, which represents approximately 4% reflectivity.

![Specular value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f5e91e51-6b1b-4a19-92a3-9a9b17f23922/spec-slider-00.png)
![Specular value 0.5](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/28410273-6094-4c8b-91fd-88995237a401/spec-slider-05.png)
![Specular value 1](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff0dbe2d-9816-47ac-89bf-943a918bca4a/spec-slider-10.png)

**Specular values of 0, 0.5, and 1**

## Roughness

The Roughness input controls how rough or smooth a Material's surface is. Rough Materials scatter reflected light in more directions than smooth Materials. This value controls how blurry or sharp a reflection is (or how broad or tight a specular highlight is).

* A Roughness of 0 (smooth) results in a mirror-like reflection.
* A Roughness of 1 (rough) results in a diffuse or matte surface.

![Roughness Value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c38614c0-e729-4e27-89ac-8ae5cfec484d/roughness-slider-00.png)
![Roughness Value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/507b367d-49bd-49fb-a0e0-25c62d4f97fa/roughness-slider-10.png)
![Roughness Value 1](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6623ee94-76ed-4898-a4c0-afb1f9b12cf3/roughness-slider-20.png)

**Roughness values of 0, 0.5, and 1.**

Most surfaces are not uniformly rough or smooth. Roughness is a property that is frequently mapped on your objects in order to add physical variation to the surface.

Scratches on metal, scuffs on a wood floor, or fingerprints on plastic are examples of materials that would require a roughness map.

![Roughness map](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4982eb29-f942-4732-95df-ee41186bec3e/roughness-map.png)
