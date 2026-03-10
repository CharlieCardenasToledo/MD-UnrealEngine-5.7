# User Scene Textures for Post Process Materials

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-material-user-scene-textures-in-unreal-engine

> Application Version: 5.7

**User Scene Textures** are user-defined transient render targets that can be written and read in post process materials, making it possible to support multi-pass post process effects.

This guide demonstrates how you can use User Scene Textures to create a variable blur effect on screen whereby there is no blur in the middle of the screen and varying amounts of blur towards the outer edge of the screen. The blur effect is achieved by interpolating between the original scene color and two downsampled and blurred User Scene Textures, each generated with a two-pass separable gaussian filter. This method can provide better efficiency than a single-pass blur.

![With the Variable Blur Post Process Material Effect](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5712e835-6330-4157-b9e1-ec4ea8a41e6d/ust-comparison-1.png)

![Without any Post Process Materials Applied](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8e65cb70-9397-4a88-9144-bb4e5a28a6c5/ust-comparison-2.png)

In this guide, you’ll set up the following:

* A material to downsample and blur user scene textures.
* Materials to blur along the horizontal and vertical parts of the screen.
* Multiple material instances to create the read and write elements of User Scene Textures.
* Explore some debugging options for this type of effect with console commands and material logic.

## Preliminary Material Creation

To begin with, you’ll start by creating three separate materials. Each of these materials will be used to build out the different elements needed to create a variable blur post process effect. This starts with one material to downsample, and two materials to each blur the horizontal and vertical components of the effect. These materials will be used later in this guide to create material instances to read and write to User Scene Textures that will create this multi-pass effect.

Follow these steps to get started creating this effect:

1. In the **Content Browser**, click the **Add (+)** button and create three **Materials**.
2. **Name** each material as follows:
   1. Downsample
   2. BlurHoriz
   3. BlurVert

You should have three materials that look like this:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fde0fd40-929b-4cc2-9121-07087bfb1ddb/ust-material-creation.png)
