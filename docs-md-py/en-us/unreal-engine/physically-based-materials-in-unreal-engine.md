# Physically Based Materials

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine

> Application Version: 5.7

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c327e06a-0458-4fab-b450-5a0a8f027786/physmatheader.png)

This document is designed to provide guidelines and best practices for working within Unreal Engine's **physically based Materials** system. It assumes that you have some familiarity with the Material creation process in Unreal. If you are completely new to Materials in Unreal, you may prefer to start with the [Essential Material Concepts](https://dev.epicgames.com/documentation/en-us/unreal-engine/essential-unreal-engine-material-concepts) page.

This page focuses only on the Material attributes that are directly related to the physically based shading workflow. For a complete breakdown of all inputs on the Main Material node, see the [Material Inputs](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-inputs-in-unreal-engine) page.

## What Does Physically Based Mean?

**Physically based rendering** (PBR) means that surfaces approximate the way light behaves in the real world, as opposed to the way we intuitively think it should. Materials that adhere to PBR principles are more accurate and typically more natural looking than a shading workflow that relies fully on artist intuition to set parameters.

Physically based Materials work equally well in all lighting environments. In addition, Material values can be less complex and interdependent, resulting in a more user-friendly Material creation workflow. These benefits are applicable even for non-photorealistic rendering, as evident in films from Pixar [[4]](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine#smits) and Disney [[3]](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine#burley).

For an in depth technical look at Unreal Engine's physically based Material and shading model, refer to this SIGGRAPH presentation [2](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine#karis).

## PBR Material Attributes

These are the Material attributes that are directly related to the physically based aspect of Unreal Materials.

* [Base Color](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine#basecolor)
* [Roughness](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine#roughness)
* [Metallic](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine#metallic)
* [Specular](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine#specular)

All of these inputs are designed to accept values between 0 and 1. In the case of Base Color this means a color or texture sample with RGB values that fall between 0 and 1.

Physically based values can be measured from real world Materials. Some examples are given below.

### Base Color

Base Color defines the overall color of the Material. The Base Color input accepts a **Vector3 (RGB)** value where each channel is automatically clamped between 0 and 1.

![Base Color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5c4dc23f-b578-4eec-9060-1cfb75fbf2c4/base-color.png)

If taken from the real world, this is the color when photographed using a polarizing filter (polarization removes the specular of nonmetals when aligned).

**Measured BaseColor values for nonmetals (intensity only):**

| Material | BaseColor Intensity |
| --- | --- |
| Charcoal | 0.02 |
| Fresh asphalt | 0.02 |
| Worn asphalt | 0.08 |
| Bare soil | 0.13 |
| Green grass | 0.21 |
| Desert sand | 0.36 |
| Fresh concrete | 0.51 |
| Ocean Ice | 0.56 |
| Fresh snow | 0.81 |

**Measured BaseColors for metals:**

| Material | BaseColor (R, G, B) |
| --- | --- |
| Iron | (0.560, 0.570, 0.580) |
| Silver | (0.972, 0.960, 0.915) |
| Aluminum | (0.913, 0.921, 0.925) |
| Gold | (1.000, 0.766, 0.336) |
| Copper | (0.955, 0.637, 0.538) |
| Chromium | (0.550, 0.556, 0.554) |
| Nickel | (0.660, 0.609, 0.526) |
| Titanium | (0.542, 0.497, 0.449) |
| Cobalt | (0.662, 0.655, 0.634) |
| Platinum | (0.672, 0.637, 0.585) |

### Roughness

The Roughness input controls how rough or smooth a Material's surface is. In the Material this manifests as how sharp or blurry reflections appear on the Material.

Rough Materials scatter reflected light in more directions than smooth Materials, which results in diffuse, sometimes subtle reflections. Smooth surfaces reflect light more uniformly, resulting in clear, focused reflections or specular highlights.

* A Roughness of 0 (smooth) results in a mirror reflection.
* A Roughness of 1 (rough) results in a diffuse or matte surface.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/214b071e-334f-4d92-99f3-bead35cc2ef1/roughness_nonmetal.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/83e75954-9364-4c72-a2de-7c872ab5d431/roughness_metal.png)

Roughness values from 0 to 1. Nonmetal top, metal bottom.

![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a26b60de-6af0-421b-a243-8c1915a3b08f/roughness-slider-00.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/beb9fcfd-945d-4e3e-8d90-eda1f376ed1b/roughness-slider-01.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/128aaa0c-8f8e-4585-aa08-c465eeee0cd5/roughness-slider-02.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ec1f5040-515d-4e29-a711-7d113b2eae10/roughness-slider-03.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9d2f4c13-9884-4f1c-9da6-39785a3eabc5/roughness-slider-04.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/73df6818-770b-434d-912b-91478d10beba/roughness-slider-05.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1956dab5-8343-4e61-b6df-a6fc98d89752/roughness-slider-06.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/269dc105-ffeb-4160-8960-18969d1b5ec3/roughness-slider-07.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c8088029-f72e-43a3-9a19-668f28c2212c/roughness-slider-08.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1d0bb797-4c40-46ec-b9f8-7d2552ed4dc7/roughness-slider-09.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8b34497f-1966-43a6-9e45-017cbcbfd5fa/roughness-slider-10.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/360754bd-878f-4ac4-9453-04d4aa9e7a6a/roughness-slider-11.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/25b84917-afa1-41b0-87f3-4ae862fd4c04/roughness-slider-12.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c498b499-40f8-4a51-b0a8-e2842df208c9/roughness-slider-13.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/79a7f477-3e47-4114-9a6a-7962154bddaf/roughness-slider-14.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/055e0ac1-edef-4b20-93e9-6fc2aa956d1a/roughness-slider-15.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e9389d3-6286-449b-bcd0-e8cd5a42adf4/roughness-slider-16.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4ab69bd7-1f6a-4344-9af2-0150b5740f53/roughness-slider-17.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/76375c7c-aa25-47a0-ab1c-dab965bbfbec/roughness-slider-18.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93f6cc74-3f88-4f11-9bc2-e92f9cc11653/roughness-slider-19.png)
![Roughness value 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1432aebc-b944-4f4a-8518-29a32a85b5ea/roughness-slider-20.png)

**Roughness values from 0 to 1.**

#### Mapping Roughness

Roughness is frequently mapped on objects using a grayscale texture to add physical variation to a surface. Dark areas on a roughness map appear mirrorlike on the Material, while light areas are rough and appear less reflective.

The video below shows the Roughness value increasing from 0 to 1, with a perlin texture controlling the distribution of **light (rough)** and **dark (smooth)** values. At 0, the Material preview is completely mirrorlike. At 1, the Material is perfectly matte. In-between values are more interesting, as parts of the surface appear smooth and parts appear rough.

Roughness maps are frequently used to add scruffs, smudges, or other imperfections to Materials like plastic and metal.

#### Roughness vs. Specular

The interplay between roughness and specular is an important point to understand, particularly if you were working in Unreal Engine before the PBR workflow was adopted.

**Specularity** refers to the amount of [specular light](https://en.wikipedia.org/wiki/Specular_reflection) reflected by a surface. This value is inherent to the Material type, and usually the default value of 0.5 is accurate. The Specular input is **not used for reflection/specularity maps** or to add surface variation. These should be handled in the Roughness map.

### Metallic

The Metallic input accepts a value between 0 and 1, and defines whether your Material behaves as a metal or nonmetal.

In most cases, you should treat Metallic as a binary property in Unreal Engine. For pure surfaces, such as pure metal, pure stone, pure plastic, and so on, you should set Metallic to **either 0 or 1**, not anything in between. When creating hybrid surfaces like corroded, dusty, or rusty metals, you may find that you need some value between 0 and 1.

* **Nonmetals** have a Metallic value of 0. This is the default value.
* **Metals** have a Metallic value of 1.

![Metallic values](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c9ce65a-a57b-4d94-869a-a7ce986e0a80/metallic.png)
