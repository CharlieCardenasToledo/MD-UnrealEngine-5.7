# Contact Shadows

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/contact-shadows-in-unreal-engine

> Application Version: 5.7

When creating scenery and characters for your application, there are times when you'll want to add visual depth to
the rendering. Adding **Contact Shadows** is a great way to improve the visual depth and fidelity of your scene
because they provide a more accurate approximation of shadowing, allowing you to add a contoured shadow that
might not be achieved with other shadowing algorithms.

## Adding Detail to your Characters

One use case for enabling Contact Shadows for a given [Point Light](https://dev.epicgames.com/documentation/en-us/unreal-engine/point-lights-in-unreal-engine)
is to render an additional Level of Detail (LOD) for your characters. The following images should give you a good idea of
what Contact Shadows can add to a character. As you drag the comparison slider from right to left, you'll notice that the
character located within the radius of a Point Light with enabled Contact Shadows exhibits additional details that aren't
present when Contact Shadows are turned off.

![Contact Shadow Off](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/29e93c0f-e7e5-4ff1-8d06-0174da724976/contactshadow_off.png)

![Light's Contact Shadow Length = 0.1](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c140af9-7d04-4393-931a-66aaee31a2ba/contactshadow_on.png)

When you turn on Contact Shadows, you're directing the renderer to execute a per-pixel screen space algorithm on a
per-light basis. This means that the Contact Shadow algorithm is executing a light computation pass,
performing scene depth buffer ray marching so as to determine whether the queried pixel is to be occluded from the
Point Light source that has Contact Shadows enabled.

## Scenes with Contact Shadows

Another use case for enabling Contact Shadows is to eliminate the need for computing parallax occlusion mapping shadows
within a material's pixel shader that only supports one light. The following image provides a comparison of parallax
occlusion mapping materials with and without Contact Shadows enabled.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/36e80507-397a-4aa3-acf8-435f94d6d343/contactshadow_comparison.png)
