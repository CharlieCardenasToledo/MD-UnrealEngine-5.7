# Screen Space Global Illumination

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/screen-space-global-illumination-in-unreal-engine

> Application Version: 5.7

**Screen Space Global Illumination** (SSGI) is an **Unreal Engine** feature that aims to create natural-looking lighting by adding dynamic indirect lighting to objects within the screen view. SSGI also makes it possible to have dynamic lighting from emissive surfaces, such as neon lights or other bright surfaces.

Screen Space Global Illumination works best as a supplimental indirect lighting illumination method to precomputed lighting from [Lightmass](https://dev.epicgames.com/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine).

![SSGI Disabled with Baked Lighting](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d654c308-b491-47d4-87ab-1fa766eb5ebc/01-screen-space-disabled.png)

![SSGI Enabled with Baked Lighting](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/39af55d7-5363-4376-8b38-edd9c5728fe5/02-screen-space-enabled.png)

## Using SSGI

Use the following properties and console variables when working with SSGI.

You can enable Standalone SSGI in the **Post Process Volume** settings by enabling the **Method** and choosing **Screen Space (Beta)** from the dropdown menu.

![Enable Global SSGI](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8fb7bb8a-e000-404d-b72c-a15a4fa49b64/03-screen-space-enable-ssgi.png)
