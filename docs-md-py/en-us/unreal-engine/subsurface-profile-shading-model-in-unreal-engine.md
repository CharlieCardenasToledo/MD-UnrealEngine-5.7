# Subsurface Profile Shading Model

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/subsurface-profile-shading-model-in-unreal-engine

> Application Version: 5.7

Unreal Engine offers a specific shading method for rendering realistic skin or wax surfaces, which is called **Subsurface Profile** shading.

The Subsurface Profile shading method is similar to the Subsurface method, but with a fundamental difference in how it renders: Subsurface Profile is based in **screen space**. This is because screen space rendering is a more effective to display the subtle subsurface effects seen in human skin, where backscattering is a secondary effect only seen in few cases, such as ears. In the following document will cover what Subsurface Profiles are and how you can use them in your work.

![Not using SubsurfaceProfile](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7768a0e5-2af1-487a-b141-d061ec6f9943/results_1.png)

![Using SubsurfaceProfile](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9be3a852-8ae8-4ccb-a262-3dd4754deb96/results_2.png)



Special thanks to Lee Perry-Smith and his company [Infinite Realities](http://ir-ltd.net) for their assistance with this documentation, also for providing the 3D scanned head model.

## What is a Subsurface Profile

The Subsurface Scattering Profile data is an asset that can be created, shared, and saved in the **Content Browser**. The data is intended to be authored by artists and controls the distance the light in the Subsurface should scatter, the color of the Subsurface, and the falloff color of the light once it has exited the object. This data can then be applied to a Subsurface Material. Subsurface Profile data can also be tweaked interactively, meaning that you do not need to re-compile the material to see the results of edits.

## Enabling, Creating, and Using a Subsurface Profile

There are many different ways of using Sub Surface profiles in Unreal Engine. In the following section, we will take a look at each of these ways.

### Creating A Subsurface Profile

To create a Subsurface Profile, first Right-click inside of the **Content Browser**. Then select the **Materials & Textures** option and then select the **Subsurface Profile** option.

![Create Subsurface Profile](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4b3d6574-20f5-4903-8395-9a12e63fc6c6/create-subsurface-profile.png)
