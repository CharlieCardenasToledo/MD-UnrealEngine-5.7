# Auto Exposure

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/auto-exposure-in-unreal-engine

> Application Version: 5.7

The **Post Process Volume** provides controls for setting up **Exposure** (more commonly called eye adaptation), which automatically adjusts how bright or darker the scene looks. This effect recreates the experience of human eyes adjusting to different lighting conditions, like when walking from a dimly lit interior to a brightly lit exterior, or the other way around.

## Exposure Metering Modes

The engine offers several types of metering modes to choose from when setting up auto exposure in your scenes. These different metering modes provide settings that accurately mimic real-world cameras, giving you control over exposure in your scenes through the post process.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c24fd1dd-902b-44ad-a775-efffd10558eb/exposuremeteringmodes.png)

* **Auto Exposure Histogram** mode provides finer control over auto exposure with advanced settings constructed from a 64-bin histogram. This is the default exposure metering mode in Unreal Engine.
* **Auto Exposure Basic** mode provides fewer settings, but is a faster method that computes single values by downsampling exposure.
* **Manual** mode enables the use of **Camera** settings within the Post Process and Cameras settings to control exposure, rather than using only the settings found in the **Exposure** category.

### Histogram and Basic Algorithm

**Auto Exposure Basic** and **Auto Exposure Histogram** metering modes both calculate the overall luminance of the scene, and brighten or darken the scene to an expected value, but they differ in how they calculate scene luminance.

* The **Auto Exposure Basic** algorithm uses the average of the log luminance of the scene to determine the target exposure value.
* The **Auto Exposure Histogram** mode first calculates a histogram of the log luminance scene. Then, the histogram is analyzed to determine the average luminance value.

The Basic and Histogram modes use different algorithms to calculate the average luminance of the scene. However, once the average luminance value is determined, both algorithms treat that luminance as middle gray. In photography, this middle gray point is sometimes referred to as "18% gray" or "18% middle gray," referring to the amount of light that is reflected by a gray card.

### Manual Algorithm

The **Manual** metering mode allows the user to select a single, fixed exposure value that is unaffected by the luminance in the scene. If **Apply Physical Camera Exposure** is disabled in the post process settings, the exposure value will be linear brightness:

```
	Exposure = 1/(2^(EV100 + Exposure Compensation))
```

If **Apply Physical Camera Exposure** is applied, EV100 is calculated as the following formula. Otherwise, it is 0.

```
	EV100 = log2(Aperture^2 / Shutter Speed * 100/ISO)
```

Exposure in the following formula defines the relationship between the scene surface luminance (L, which is measured in cd/m2) and pixel brightness (B) before the tonemapper and exposure compensation are applied.

```
	B = Exposure * L
```

You can verify this formula's result by disabling the tonemapper through the viewport show flags (**Show > Post Processing**), and inspect the scene brightness using the Pixel Inspector. Also note that the [editor EV100 override setting](https://dev.epicgames.com/documentation/en-us/unreal-engine/auto-exposure-in-unreal-engine#editorviewportoverride) directly sets the EV100 exposure used in this equation.

The **Exposure Compensation** (also called **ExpComp** for short) defines an additional scale of 2^ExpComp on top of the exposure computed from the current metering mode, except when using the EV100 editor override.

## Local Exposure

**Local Exposure** is a technique that automatically applies local adjustments to exposure — within artist-controlled parameters — to preserve both highlight and shadow detail on top of the existing global exposure system. This is especially useful for projects with challenging high dynamic range scenes using dynamic lighting, in which applying a single global exposure adjustment is not enough to avoid blown out highlights and completely dark shadows.

Projects using dynamic time-of-day systems can encounter scenes with both under and over exposed areas in the final image, such as indoor scenes with very bright outdoors visible through a door or window, which can be problematic for gameplay. For example, the scene below is an example where there are under and over exposed areas.

![With Exposure Only](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3eeae557-8439-4e03-a710-8d8b4c029402/local-exposure-disabled.png)

![With Local Exposure](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/57fe6a7b-bc9c-41e0-b71a-007c535d051f/local-exposure-enabled.png)



Local Exposure helps achieve a more consistent final image when carefully crafted lighting per scene is not feasible, and it should always be set up when using [Lumen Global Illumination](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-global-illumination-and-reflections-in-unreal-engine).

[Local Exposure settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/auto-exposure-in-unreal-engine#localexposuresettings) are found in the Post Process Volume settings under the **\*Lens > Local Exposure** category.

![Post Process Volume Local Exposure settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9afc8642-9022-4fba-ada5-0ef62fd41793/local-exposure-settings.png)
