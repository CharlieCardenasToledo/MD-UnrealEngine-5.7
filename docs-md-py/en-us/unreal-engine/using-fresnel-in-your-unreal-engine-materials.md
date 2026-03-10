# Using Fresnel in Your Materials

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-fresnel-in-your-unreal-engine-materials

> Application Version: 5.7

Often when creating a film or cinematic, you need a way to better highlight the silhouette of a character or set piece. This lighting technique is referred to as rim lighting, or edge lighting, and involves adding additional lights to help differentiate the character's silhouette from the background. While this works nicely for film, adding additional lights to any 3D scene adds extra complexity that can quickly become difficult to manage.

Unreal Engine offers a solution to this at the Material level. Using **Fresnel**, artists can simulate rim lighting in the Material of a character or prop, giving them more control over the look and feel of the effect. Fresnel is an inherent property of many naturally occuring Materials, including glass, water, and some types of fabric and paint. The techniques in this tutorial will help you simulate those Materials more accurately.

## Fresnel

**Fresnel** is the term used to describe how the light you see reflects at different intensities based on the angle of view. For example, if you are standing over a pool looking straight down, you will not see a lot of reflections on the water. As you move your head so that the water in the pool becomes parallel to your eye level, you will begin to notice more and more reflections on the surface of the water. Water and glass both exhibit strong Fresnel tendencies, meaning they appear relatively transparent when viewed straight-on, and reflect more light at glancing angles.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9ca5ba10-301e-432f-b4c4-42226e4cc7c3/fresnel-glass-01.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/554d6823-d6f7-4ab0-a4ce-f8ace1e2d23c/fresnel-glass-02.png)

**Note how the glass in the picture frames is transparent when viewed straight on, and shows more reflections when viewed from the side.**

In Unreal Engine, the **Fresnel Material Expression** calculates a falloff based on the [dot product](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#dotproduct) of the surface normal and the direction to the camera. When the surface normal points directly at the camera, a value of 0 is output meaning there should be no Fresnel effect happening. When the surface normal is perpendicular to the camera, a value of 1 is output meaning the full effect of the Fresnel should be taking place. The result is then clamped to [0, 1] so you do not have any negative color in the center. The following image demonstrates this concept.

![Fresnel viewing angle example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5a7ad170-4814-4658-8c39-6fdbe2cccb26/fn_caculation_example.png)
