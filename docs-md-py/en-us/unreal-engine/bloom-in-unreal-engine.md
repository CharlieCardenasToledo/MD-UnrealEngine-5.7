# Bloom

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/bloom-in-unreal-engine

> Application Version: 5.7

**Bloom** is a real world light phenomena that can greatly add to the perceived realism of a rendered image at a moderate render performance cost. Bloom can be seen by the naked eye when looking at very bright objects that are on a much darker background. Even brighter objects also cause other effects (streaks, lens flares), but those are not covered by the classic bloom effect. Because our displays (TV, TFT, etc.) usually do not support HDR (high dynamic range), we cannot really render very bright objects. Instead we simulate the effects that happen in the eye (retina subsurface scattering), when light hits the film (film subsurface scattering), or in front of the camera (milky glass filter). The effect might not always be physically correct but it can help to hint the relative brightness of objects or add realism to the LDR (low dynamic range) image that is shown on the screen.

![Bloom Effect](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6341888d-0b4c-4761-b121-c89809b49f38/bloom.png)

Bloom can be implemented with a single Gaussian blur. For better quality, we combine multiple Gaussian blurs with different radius. For better performance, we do the very wide blurs
in much lower resolution. In UE3, we had 3 Gaussian blurs in the resolution 1/4, 1/8, and 1/16. We now have multiple blurs name Blur1 to 5 in the resolution 1/2 (Blur1) to 1/32 (Blur5).

We combine the blurs differently to get more control and higher quality. For best performance, the high resolution blurs (small number) should be small and wide blurs should mostly make
use of the low resolution blurs (large number).

| Property | Description |
| --- | --- |
| **Intensity** | Scales the color of the whole bloom effect (linear). Possible uses: fade in or out over time, darken. See the [examples below](https://dev.epicgames.com/documentation/en-us/unreal-engine/bloom-in-unreal-engine#intensity). |
| **Threshold** | Defines how many luminance units a color needs to have to affect bloom. In addition to the threshold, there is a linear part (one unit wide) where the color only partly affects the bloom. To have all scene colors contributing to the bloom, a volume of -1 needs to be used. Possible uses: tweak for some not real HDR content, dream sequence. See the [examples below](https://dev.epicgames.com/documentation/en-us/unreal-engine/bloom-in-unreal-engine#threshold). |
| **#1#2#3#4#5 Tint** | Modifies the brightness and color of each bloom. Using a black color will not make this pass faster but that can be done. |
| **#1#2#3#4#5 Size** | The size in percent of the screen width. Is clamped by some number. If you need a larger number, use the next lower resolution blur instead (higher number). See the [examples below](https://dev.epicgames.com/documentation/en-us/unreal-engine/bloom-in-unreal-engine#size). |

#### Intensity

|  |  |  |
| --- | --- | --- |
| Bloom Intensity - 0 | Bloom Intensity - 1 | Bloom Intensity - 5 |
| 0.0 | 1.0 | 5.0 |

#### Threshold

![Threshold - 0.0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8697c12a-627c-47b5-9127-7d2b08f91edf/bloom_threshold_0_small.png)

![Threshold - 10.0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9fa084a3-688a-4fd6-bf17-ed6bdc211087/bloom_threshold_10_small.png)

#### Size

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bloom Tint 1 | Bloom Tint 2 | Bloom Tint 3 | Bloom Tint 4 | Bloom Tint 5 |
| #1 | #2 | #3 | #4 | #5 |

## Bloom Convolution

The Bloom **Convolution** effect enables you to add custom bloom kernel shapes with a texture that represent physically realistic bloom effects whereby the scattering
and diffraction of light within the camera or eye that give rise to bloom is modeled by a mathematical convolution of a source image with a kernel image.

![Convolution for Bloom: Enabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1507851b-c586-4c10-8f5c-fe81d233cf11/fftbloom_enabled.png)

![Convolution for Bloom: Disabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4dd0a23c-bc00-418e-9ba7-2ddfda1abd58/fftbloom_disabled.png)

In this example, the bloom technique produces a continuum of responses ranging from star-like bursts to diffuse glowing regions.

The kernel represents the response of the optical device to a single point source in the center of the viewing field. Each pixel in the source contributes some of its brightness
to neighbors as prescribed by the kernel image. The brighter the source pixel the more visible the bloom it produces. Under the hood this energy conserving scatter is formulated
as a convolution operations and accelerated by use of a Fast Fourier Transform (FFT).

Bloom Convolution is designed for use with with in-game or offline cinematics or on high-end hardware, while the ***Standard* bloom should be used for most game applications**.
In assessing the trade off, the *Standard* bloom has a significant performance advantage but it is not conservative (it can result in an overall brightening of the image)
and it lacks the visual complexity of the Bloom Convolution.

To enable Bloom Convolution, navigate to the **Lens** section of the Post Process Volume and next to **Method** use the selection box to choose **Convolution**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df3e1788-9243-475f-8b53-46bbe4d601b5/convolution-bloom-settings.png)
