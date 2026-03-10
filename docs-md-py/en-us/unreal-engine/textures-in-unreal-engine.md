# Textures

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/textures-in-unreal-engine

> Application Version: 5.7

**Textures** are image assets that are primarily used in Materials but can also be directly applied outside of Materials, like when using an texture for a heads up display (HUD).

For Materials, textures are mapped to surfaces which the Material is applied to. Textures can be used for a variety of calculations within a Material by being applied directly to an input (such as, Base Color), used as a mask, or using the RGBA values for other calculations.

Materials may make use of several textures that are all sampled and applied for different purposes. For instance, a simple material may have a Base Color texture, a Specular texture, and a Normal Map texture. In addition, there may be a map for Emissive and Roughness stored in the alpha channels of one or more of these same textures. Packing multiple values in a single texture allows them to be used more readily while saving draw calls for performance and reducing disk space.

## Importing Textures

Textures are imported into the engine through the **Content Browser** by using the **Import** button or by dragging-and-dropping images directly from your operating system's windows into the Content Browser.

[Video: 1_o8f82b89](https://dev.epicgames.com/community/api/cms/videos/1_o8f82b89/embed.html)

A variety of image formats and file types are supported:

- .bmp
- .float
- .jpeg
- .jpg
- .pcx
- .png
- .psd
- .tga
- .dds (Cubemap or 2D)
- .exr (HDR)
- .tif (TIFF)
- .tiff (TIFF)

When importing your textures, consider the following suggestions for the dimensions of your textures:

- Use power of two sizes when possible, such as 32, 64, 128, 2048, and so on. Power of two values can be mipmapped and streamed. Non-power of two sizes are never streamed and do not generate mipmaps.
- Some GPUs have hardware limits in the maximum size texture they can support. For example, some GPUs may not support texture sizes larger than 8192 pixels (8k).

## Texture Graph Editor

The **Texture Graph Editor** provides artists a node-based interface to procedurally create and edit textures in Unreal Engine.

![Texture Graph Editor in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/2a10ace1-f488-4774-9e4a-ce9c616b38ee)

You can combine texture graphs with Blueprints, materials, and material functions for unique workflows that are only possible within Unreal Engine. The editor works in conjunction with the Texture Asset Editor, which provides additional controls for managing the texture asset.

For more information, see [Getting started with Texture Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-texture-graph-in-unreal-engine).

## Texture Asset Editor

The **Texture Asset Editor** is a standalone window where you can view and edit texture assets.

![texture asset editor interface](https://dev.epicgames.com/community/api/documentation/image/2be9f14b-9ab0-4799-ab89-266f1bdfe8c9)

From this editor window, you can view the texture and its color channels. The **Details** panel provides additional information about the imported texture along with a set of properties to configure the texture. This includes being able to set the compression, adjust brightness and saturation, set level of detail, and much more.

For more information, see [Texture Asset Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-asset-editor-in-unreal-engine).

## Texture Workflows and Optimizations

The following topics details some common workflows and optimizations you do with textures in your projects.

- [Related Document](en-us/unreal-engine/getting-started-with-texture-graph-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/texture-format-support-and-settings-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/texture-streaming-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/virtual-texturing-in-unreal-engine.md)
