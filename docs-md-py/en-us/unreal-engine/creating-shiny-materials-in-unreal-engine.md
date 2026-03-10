# Creating Shiny Materials

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-shiny-materials-in-unreal-engine

> Application Version: 5.7

Every object in the real world has some degree of shininess to it. In some cases this shininess (or reflectivity) is obvious, as with mirrors, chrome, or glass. Other times it is more subtle, as with painted wood, or smooth but unpolished stone / concrete.

In Unreal Engine, you can simulate the shininess of objects using the **Metallic, Specular, and Roughness** [Material inputs](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-inputs-in-unreal-engine). This tutorial demonstrates a few common ways to introduce shininess in your Materials.

## Shininess

When light strikes a surface in the real world, some of it is absorbed, some of it is scattered, and some is directly reflected. Scattered light is referred to as a **diffuse reflection**. When you see an object in the world that does not appear reflective, like a tree trunk, you are mostly seeing scattered or diffuse light. Light that is directly reflected is known as **specular reflection**. When you see your image reflected on a chrome faucet, or in a puddle of water, you are seeing specular reflections.

Shininess in Unreal Engine is not a technical term, but an aesthetic one. In this tutorial shininess is referring to the ability of a surface to produce coherent, mirror-like reflections. The exact properties of these reflections are defined by the Metallic, Specular, and Roughness inputs.

## Roughness & Shininess

**Roughness** plays a major role in determining the shininess of a Material. The Roughness input takes a value from **0 to 1**.

![Roughness Value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b0e71e68-dfa1-473a-82ca-1040dde87a61/roughness-example-01.png)

* The lower the Roughness value, the more mirror-like the Material will appear. When Roughness is **0**, the Material behaves like a perfect mirror.
* The higher the Roughness value, the less shiny a surface will appear. When Roughness is **1**, the Material appears fully diffuse.

Below is a demonstration of how Roughness can affect the shininess of a Material. In this case, the sphere is in an empty environment so the highlight seen on the model is a direct reflection of the light source.

![Roughness scale for nonmetals](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cd4496c7-af4f-4667-be49-85ee3194f356/roughness-spectrum-nonmetal-cubemap.png)

The sphere on the far left has a Roughness value of **0**, and the light source is reflected as a sharp, precise highlight. As the Roughness value is increased from **0** to **1**, the highlight becomes blurrier and the sphere appears less shiny.

## Metallic & Shininess

The apparent shininess of **Metallic** objects is also determined by the Roughness value. Low Roughness values produce a shiny Metallic Material and high Roughness values produce a Material that appears less shiny. The key difference between a metal and non-metal Material is in the way the color of the specular reflection is calculated.

* When the Metallic value is **0**, specular highlights reflect the color of the environment and light sources.
* When the Metallic value is **1**, specular highlights are tinted by the Base Color of the Material.

![Non-metal Material Graph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2761e40a-25b3-4ae3-acf5-d6af2701c2c4/metal-non-metal-01.png)
![Metallic Material Graph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1f820032-f51d-4da0-acd8-166028568b56/metal-non-metal-02.png)

**Note how the color of the reflections is influenced by the Base Color when the Metallic value changes from 0 to 1.**

The example below shows how the Roughness value affects a metallic Material. This Material has a Metallic value of **1**, which stays constant through all the images. There is also a solid blue color passed into the **Base Color** input to show how Base Color influences the color of reflections on a metallic Material.

![Roughness scale for metals](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7331f7aa-ab4a-4514-a89c-1255d8fd53b6/roughness-spectrum-metal-cubemap.png)
