# Mobile Depth of Field

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mobile-depth-of-field-in-unreal-engine

> Application Version: 5.7

The following depth of field (DOF) method provides an optimized and low-cost depth of field effect for mobile platforms using the Forward rendering path.

## Gaussian

Gaussian depth of field has been removed for use with the **Deferred Renderer** and **Desktop Forward Renderer** and only supports mobile platforms. To use this Gaussian DOF while working in Editor on a desktop computer, enable one of the mobile platform previewers using the [Mobile Previewer](https://dev.epicgames.com/documentation/404).

The **Gaussian** depth of field method blurs the scene using a standard [Gaussian blur](https://en.wikipedia.org/wiki/Gaussian_blur) (or smoothing) function. Gaussian DOF blur foreground and background uses a fixed-size Gaussian blur kernel, which is very fast on lower-end hardware, such as mobile. This enables performance to be maintained with lower overhead costs where performance is critical.

![No Depth of Field](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/de97a6e1-6034-49b2-b419-57f1b9271f33/image_0.png)

![Gaussian Depth of Field](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c2e0113b-b934-4ab8-b1cd-5d2432ab4bf5/image_1.png)

## Visualizing Depth of Field

These layers, including transition regions, can be visualized using the **Depth of Field layers** show flag in the Level Viewport under **Show > Visualize**.

![Final Scene](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0a0dd33c-deed-49dc-af7c-f75c9b769e6b/image_2.png)

![Depth of Field Visualization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c80f531-29bb-43c7-ae7d-a3d28b307a99/image_3.png)

Visualizing the **Depth of Field Layers** also includes useful information relevant to the DOF method selected by including the properties and their currently set values.

![Information relevant to the DOF method selected by including the properties and their currently set values](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c111feb1-0814-498e-b698-ef9c91b47d0f/ue5_1-image-4.png)
