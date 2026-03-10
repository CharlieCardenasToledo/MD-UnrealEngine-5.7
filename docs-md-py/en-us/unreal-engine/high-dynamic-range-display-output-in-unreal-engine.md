# High Dynamic Range Display Output

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/high-dynamic-range-display-output-in-unreal-engine

> Application Version: 5.7

You can output to High Dynamic Range (HDR) displays to take advantage of features such as higher contrast and a wider color gamut! The goal here is to give the displayed images characteristics that are more like natural light conditions experienced in the "real world". This is part of the move to the **Academy Color Encoding System** (ACES) standard wiich is a pipeline to ensure the consistent color is preserved across multiple formats and displays, and also as a way to *future-proof* the source material used without having to adjust it for another medium.

![Low Dynamic Range (LDR) ](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/80f8f93b-2d90-4534-b365-353eac4197df/ue5_1-low-dynamic-range.png)

![High Dynamic Range (HDR) ](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3c92f44e-2bf9-4860-9272-44973ed6b081/ue5_1-high-dynamic-range.png)

This example is simulated and purely for demonstration purposes only. It is impossible to convey HDR differences on an LDR screen.

With the current implementation, the full processing of the rendered scene is handled through what is known as the **ACES Viewing Transform**. This process works by using scene-referred and display-referred images.

* **Scene-referred** images maintain the original *linear light* values of the source materials without limiting the exposure range.
* **Display-referred** is the final image transformed into the color space of the display being used.

By using this pipeline, the source files do not have to be edited each time they are used with a different display to guarantee correct coloring. Instead, the display being output maps it to the correct color space.

The ACES Viewing Transform works in the following order in the viewing pipeline:

* **Look Modification Transform (LMT)** - This part of the process takes the ACES color-encoded image that has had a creative "look" (color grading and correction) applied to it and then outputs the images rendered with ACES in combination with the Reference Rendering Transform (RRT) and an Output Device Transform (ODT).
* **Reference Rendering Transform (RRT)** - Then, this part takes the scene-referred color values and converts them to display-referred. In this process, it enables the rendered images to not rely on a specific display and, instead, can ensure a larger gamut and dynamic range that is correct for the specific display it's being output to, including ones that have yet to be created.
* **Output Device Transform (ODT)** - Finally, this takes the HDR Data output of the RRT to then match it with the different devices and color spaces they can display. Because of this, each target requires its own ODT to be matched against (eg Rec709, Rec2020, DCI-P3, etc.).

For additional information on the ACES Viewing Transform, you can download the PDF documentation from the [ACES GitHub](https://github.com/ampas/aces-dev/tree/master/documents) page or follow the links in the Reference Material section of this page.

## Enabling HDR Output

You can enable HDR output at runtime by toggling the console variables or by using the **GameUserSettings** node in Blueprints.

![Enabling HDR Output](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9abbd79-4000-4eaf-83eb-791fadfb5846/ue5_1-high-dynamic-range-display-game-user-settings.png)
