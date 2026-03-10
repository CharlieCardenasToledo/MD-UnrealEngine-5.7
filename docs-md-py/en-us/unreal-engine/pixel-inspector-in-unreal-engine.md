# Pixel Inspector

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/pixel-inspector-in-unreal-engine

> Application Version: 5.7

The **Pixel Inspector** tool is a Developer Tool that
will allow you to diagnose the pixels that make up the colors in your
scene. If you want to know why a pixel is producing an unexpected color
(or maybe what Material input is driving a pixel's color), you can use
the Pixel Inspector's **Inspect Mode** to output information that is driving the pixel's visual result.

## Using the Pixel Inspector

To enable and use the Pixel Inspector:

1. From the Main Editor Window go to the **Tools** menu option under **Debug** and select **Pixel Inspector**. ![Pixel Inspector under Debug in the Tools menu.](https://dev.epicgames.com/community/api/documentation/image/871defc2-9f40-4cd3-abe1-b899b585a98d) The Pixel Inspector Window will open. ![Pixel Inspector window](https://dev.epicgames.com/community/api/documentation/image/bcd7d47a-6b6c-4e03-96aa-d1bae36face7)
2. Click the **Search** (magnifying glass) button to start pixel inspection.
3. Move the mouse over any viewport (Level, Material, Blueprint, or other) to populate the Pixel Inspector data fields in realtime. ![Using the Pixel Inspector](https://dev.epicgames.com/community/api/documentation/image/c39fb988-f09f-4282-9060-756764647d41)
4. Press Escape to stop inspection and populate the Pixel Inspector data fields with the last inspected pixel.

## Pixel Inspector Data Reference

Below are the data fields that will become populated with a pixel's information during inspection:

| Option | Description |
| --- | --- |
| Viewport ID | Displays the ID of which viewport the Pixel Inspector is drawing from. |
| Coordinate | Displays the X/Y coordinates from the current inspection (can be manually set). |
| Final Color |   |
| Context Colors | Displays the Context Colors associated with the current inspection. |
| Final Color | Final RGBA 8bits Color after tone mapping (default value is black). |
| Scene Color |   |
| Scene Color | The RGB Scene Color applied from the current inspection. |
| Pre-Exposure | Defines the upper bounds for the brightness range of the generated histogram. It remaps the range of SceneColor around camera exposure, limiting the render target required to support HDR lighting values. |
| HDR |   |
| Luminance | HDR Luminance value for current inspection. |
| HDR Color | The HDR RGB Color value being applied. |
| GBuffer A |   |
| Normal | The Normal applied from the GBufferA channel. |
| Per Object GBuffer Data | The amount of per object data from the GBufferA Channel. |
| GBuffer B |   |
| Metallic | The Metallic value applied from the GBufferB R Channel. |
| Specular | The Specular value applied from the GBufferB G Channel. |
| Roughness | The amount of Roughness applied from the GBufferB B Channel. |
| Material Shading Model | The shading model from the GBufferB A Channel encoded with Selective Output Mask. |
| Selective Output Mask | The value for the Selective Output Mask from the GBufferB A Channel encoded with Shading Model. |
| GBuffer C |   |
| Base Color | The base color value applied from the GBufferC RGB Channels. |
| Indirect Irradiance | The value of Indirect Irradiance from the GBufferC A Channel encoded with Ambient Occlusion (AO). |
| Ambient Occlusion | The value of AO from the GBufferC A Channel encoded with Indirect Irradiance. Defines the upper bounds for the brightness range of the generated histogram. It remaps the range of SceneColor around camera exposure, limiting the render target required to support HDR lighting values. |
