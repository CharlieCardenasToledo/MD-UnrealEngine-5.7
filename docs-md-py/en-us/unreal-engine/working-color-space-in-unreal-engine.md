# Working Color Space

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/working-color-space-in-unreal-engine

> Application Version: 5.7

Working Color Space lets you define the color space of the Unreal Engine(UE) Renderer. You can change the color space of the UE Renderer if you are working with textures created in a different color space, or to work in a specific color space for the display you are using.

![image alt text](https://dev.epicgames.com/community/api/documentation/image/277c109d-3884-47e2-8bab-763dd84eee39)

Unreal Engine defaults to sRBG/REC709 but you can choose to use another color space from the provided list, or you can define a custom color space using chromaticity coordinates.

To adjust the Working Color Space:

1. Navigate to **Edt > Project Settings > Rendering > Working Color Space.**
2. Select the Working Color Space dropdown and choose the color space you want to use for your project.

![image alt text](https://dev.epicgames.com/community/api/documentation/image/bc6affe9-2a18-4e47-a989-d9a906def43f)

Unreal Engine supports the following color spaces:

| Color Space | Description |
| --- | --- |
| sRGB / Rec709 | sRGB / Rec uses the parameter values for the HDTV standards for production and international programme exchange from the International Telecommunication Union (ITU). |

For more information, refer to the [ITU parameter values](https://www.itu.int/rec/R-REC-BT.709/en) |

| Rec2020 | Rec2020 uses theparameter values for ultra-high definition television systems for production and international programme exchange from the ITU. |
| --- | --- |

For more information, refer to the [ITU parameter values](https://www.itu.int/rec/R-REC-BT.2020-0-201208-S/en) |

| ACES AP0 | For more information about the ACES color spaces, refer to the [Academy Color Encoding Specification documentation](https://docs.acescentral.com/) |
| --- | --- |
| ACES AP1 / ACEScg |   |
| P3DCI | For more information about the P3DCI color space, refer to the [International Color Consortium website](https://www.color.org/chardata/rgb/DCIP3.xalter) |
| P3D65 | For more information about the P3DCI color space, refer to the [International Color Consortium website](https://www.color.org/chardata/rgb/DCIP3.xalter) |
| Custom | To use a custom color space, enter the Red, Green, Blue and White Chromaticity coordinate values that you want to use for your custom color space. |

## Texture Settings: Input Conversions

- (Advanced) Source Color Settings Color Space When the Color Space is set to None (default), no conversions are applied. When the Color Space is manually specified, conversions to the working color space are automatically applied when the texture is serialized. If the working color space is changed, textures are automatically re-serialized with the updated conversion. Encoding Override Source encoding of the texture, exposing more options than just sRGB. *Note: This differs from the sRGB checkbox, which specifies the stored encoding of the texture resource in the engine.*

![image alt text](https://dev.epicgames.com/community/api/documentation/image/19a188af-7224-4c88-82dc-1fe765b79447)
