# ImageCombineChannels

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageCombineChannels

> Application Version: 5.7

### Description

ImageCombineChannels (v1)

Combine channels into a single RGBA image
Outputs are single channel images

Input(s) :
Red - Red channel - if not connected, use black color
Green - Green channel - if not connected, use black color
Blue - Blue channel - if not connected, use black color
Alpha - Alpha channel - if not connected, use black color

Output(s):
Image - Output image recombined from input channels

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Image |
| Type | [FDataflowImageCombineChannelsNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImageCombineChannelsNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ResolutionOptions | resolution option | [EDataflowImageCombineResolutionOption](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/EDataflowImageCombineResolutionO-) | Highest |
| Resolution | resolution of the output image if the resolution option is set to user defined | [EDataflowImageResolution](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/EDataflowImageResolution) | Resolution512 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Red | Red channel - if not connected, use black color | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |
| Green | Green channel - if not connected, use black color | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |
| Blue | Blue channel - if not connected, use black color | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |
| Alpha | Alpha channel - if not connected, use black color | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image | Output image recombined from input channels | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |
