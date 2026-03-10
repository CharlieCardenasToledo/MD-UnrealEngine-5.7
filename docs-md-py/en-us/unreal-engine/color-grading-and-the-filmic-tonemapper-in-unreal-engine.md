# Color Grading and the Filmic Tonemapper

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/color-grading-and-the-filmic-tonemapper-in-unreal-engine

> Application Version: 5.7

Within the Unreal Engine, the term **Color Grading** covers the Tone Mapping function (HDR to LDR transformation) that is used with [High Dynamic Range (HDR) display output](https://dev.epicgames.com/documentation/en-us/unreal-engine/high-dynamic-range-display-output-in-unreal-engine) and further the color correction (LDR color to screen color transformation) processing of the image.

## Tone Mapping

The purpose of the **Tone Mapping** function is to map the wide range of high dynamic range (HDR) colors into low dynamic range (LDR) that a display can output. This is the last stage of post processing that is done after the normal rendering during post processing. The process of tone mapping can be thought of as a way to simulate the response that film has to light.

### Academy Color Encoding System (ACES) Filmic Tonemapper

The Filmic tonemapper that is used with Unreal Engine matches the industry standard set by the [Academy Color Encoding System (ACES)](http://www.oscars.org/science-technology/sci-tech-projects/aces) for television and film. This ensures that consistent color is preserved across multiple formats and displays while also as a way to future proof the source material since it will not have to be adjusted for each medium that comes along. The filmic tonemapper also uses the same global tonemapper that was previously used in Unreal Engine, with the exception that there is now a filmic response meaning that the S-curve shape now better simulates film stock for a better overall look.

Two places you'll immediately notice a difference is with Bloom and Exposure Levels.

#### Physically Correct Emissive and Bloom

Emissive values are now physically correct so that as the emissive power increases the color will become lighter, similarly to how colored lights work in the real world. As color gets tone mapped, if the final color is bright enough to start saturating the film / sensor, it will become white.

![Filmic Tonemapper | Emissive](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b79639b6-1088-4c5c-af35-f7a04317cef4/bloom_filmictonemapper.png)

![Legacy Tonemapper | Emissive](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5066d3bd-f742-47bb-bdc1-4f29e1302099/bloom_oldtonemapper.png)

In this example, the legacy tonemapper is compared to the new filmic tonemapper. With a high enough emissive power, the color will start to become white, unlike the legacy tonemapper where values would just become overly saturated causing areas of the material to lose its detail. With the filmic tonemapper, you can even see that the Bloom in this scene retains its physical correctness as well as it is never overly saturated, thus retaining it's reflective primary color value.

#### Exposure Levels

Exposure levels are physically correct so that colors will continue to have shape to them rather than lose detail.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd398058-3152-4150-9312-b2e474cf06d6/exposure_default.png)
