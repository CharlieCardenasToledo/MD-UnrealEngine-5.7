# ImageFromColor

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageFromColor

> Application Version: 5.7

### Description

ImageFromColor (v1)

Create a RGBA image from a single color at a specific resolution
Outputs are single channel images

Input(s) :
FillColor - color to fill the image with
Resolution - resolution of the output image

Output(s):
Image - Output image

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Image |
| Type | [FDataflowImageFromColorNode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImageFromColorNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FillColor | color to fill the image with | [FLinearColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=0.000000,A=1.000000) |
| Resolution | resolution of the output image | [EDataflowImageResolution](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/EDataflowImageResolution) | Resolution16 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image | Output image | [FDataflowImage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |
