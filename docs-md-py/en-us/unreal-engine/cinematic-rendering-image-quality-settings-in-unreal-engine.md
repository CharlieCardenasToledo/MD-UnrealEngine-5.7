# Image Settings

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine

> Application Version: 5.7

You can add a variety of settings to jobs in the Movie Render Queue. These include additional rendering settings like anti-aliasing, color output adjustments, console commands, and more.

#### Prerequisites

* You have completed the prerequisite steps from the Movie Render Queue section of the **[Movie Render Pipeline](https://dev.epicgames.com/documentation/404)** page.

You can choose which settings you want to add by clicking the **+ Setting** dropdown menu in the Movie Render Queue's window and selecting an item under the **Settings** category.

![render iamge setting list](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f6fb1ed1-3e9c-4c04-8619-5de651ef08df/addsetting.png)

Once added, you can enable and disable them using the toggle switch, and you can select them to customize their properties.

| Name | Description |
| --- | --- |
| [**Output**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine#output) | The Output setting controls your output file's directory, file name, frame rate, and output resolution. Your file name and directory path can be customized using `{token}` format strings. Output is a required setting and cannot be deleted from the settings window. |
| [**Anti-Aliasing**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine#anti-aliasing) | Anti-aliasing controls the number of samples used to produce the final render. There are two types of sampling that produce the render: **Spatial** and **Temporal**. |
| [**Burn In**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine#burnin) | Burn In enables adding custom watermarks to your render, which contain information about the render and shot. You can choose whether the Burn In is added to the final image, or is rendered to a separate layer. |
| [**Camera**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine#camera) | The Camera setting contains settings for the shutter timing and you can specify an overscan percentage to render extra pixels around the edges of your images. |
| [**Color Output**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine#coloroutput) | The Color Output setting overrides Unreal's default color space settings with a custom **[OpenColorIO (OCIO)](https://dev.epicgames.com/documentation/en-us/unreal-engine/color-management-with-opencolorio-in-unreal-engine)** configuration. You can also use it to disable the **Tone Curve** portion of post-processing even if not using an OCIO-based workflow. |
| [**Console Variables**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine#consolevariables) | Console Variables enables console commands to be designated when the render begins. This is useful when trying to apply quality settings that are too computationally expensive for real-time preview in the Editor. The variables will be reverted upon the render completing. |
| [**Debug Options**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine#debugoptions) | Debug Options contain options for debugging certain render behaviors. Typically you do not need to use these options unless you're troubleshooting issues within your renders. |
| [**Game Overrides**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine#gameoverrides) | Game Overrides change several common game-related settings, such as Game Mode and Cinematic Quality settings. This is useful if the game's normal mode displays UI elements or loading screens that you do not want to capture. |
| [**High Resolution**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine#highresolution) | The High Resolution settings enable the use of tiled renders to produce larger images without being constrained by maximum texture sizes or memory limits on GPUs. |

## Output

Output contains settings related to the sequence's resolution and file formatting. Output is a required setting and cannot be deleted from the settings window.

![render output settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/00b7c8b2-5e59-46bf-a0f6-b5e98613e5c2/outputsetting.png)

| Property | Description |
| --- | --- |
| **Output Directory** | Designates the file directory where the export saves. |
| **File Name Format** | Determines the file name format given to the export. You can use format string tokens to allow for custom naming. Slashes (/) can also be used here to designate subfolders relative to the **Output Directory**. |
| **Output Resolution** | Determines the export resolution. |
| **Use Custom Frame Rate** | Enables you to use a custom frame rate different from the one in the Level Sequence. |
| **Output Frame Rate** | Determines the new framerate if you enabled **Use Custom Frame Rate**. |
| **Override Existing Output** | Enables you to automatically overwrite any files with the same file name. If disabled, an integer, such as 1, will be appended to the file name. |
| **Zero Pad Frame Numbers** | Determines how many numbers to pad the output frame numbers. For example a value of 2 will output \_01, and a value of 4 will output \_0001 for your file name suffix. |
| **Frame Number Offset** | Adds a specified number to the frame numbers when writing to the disk during rendering. This allows you to offset issues regarding negative numbers for labeling frames, which confuses most software. So, instead of writing -2, -1, 0, 1 to the disk, you can write out 98, 99, 100, 101 by setting the Frame Number Offset to 100. |
| **Handle Frame Count** | Determines the number of frame handles to include for each shot. This will expand each shot section by the given number of frames on both sides and render them. |
| **Output Frame Step** | The amount of frames to skip for every frame. For example, setting the value to 2 sets the rendering to every other frame. For the frames that are skipped, the game will still tick to make the results between rendering every frame and every stepped frame more consistent. Some image quality differences will be visible (due to a different temporal history). This feature is experimental. |
| **Use Custom Playback Range** | Enables you to designate a custom playback range different from the sequence. |
| **Custom Start Frame** | Determines the frame start if you enabled Custom Playback Range. Start frame is Inclusive. |
| **Custom End Frame** | Determines the frame end if you enabled Custom Playback Range. End frame is Exclusive, so a **Start Time** of 0 and an **End Time** of 1 will render only one frame (frame 0). |
| **Auto Version** | If enabled, Movie Render Queue will check the most recent version number from the last render in the output directory, increment it by 1, then use that value for the next render's version number. |
| **Version Number** | If **Auto Version** is disabled, the value in this field will be used as the version number for the render output if using the `{version}` token. |

### Format String Information

The **File Name Format** property allows for using custom tokens, known as **Format Strings** to allow for customizing a file name format. When a token is specified in the file name format, it will be replaced with the intended name when the files are being rendered and saved.

![format string token](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c288f9d-0081-4c89-a3af-c44186b84808/formatstring.png)

The following tokens are available for you to use:

| Token Name | Description |
| --- | --- |
| **{level\_name}** | The name of the level the render is occurring in. |
| **{sequence\_name}** | The Level Sequence Asset name. |
| **{frame\_rate}** | The frame rate of the sequence, or the overridden frame rate if Use Custom Frame Rate is enabled. |
| **{date}** | Today's date, formatted by {year}.{month}.{day}. |
| **{year}** | The current year when the render begins. |
| **{month}** | The current month when the render begins. |
| **{day}** | The current day when the render begins. |
| **{time}** | The current time when the render begins, formatted by {hours}.{minutes}.{seconds}. Uses a 24 hour clock scale. |
| **{frame\_number}** | The frame number of the sequence being rendered. This token will be stripped for any video output, as it is meant only for image sequence files. |
| **{frame\_number\_shot}** | The frame number of the shot being rendered. This token will be stripped for any video output, as it is meant only for image sequence files. |
| **{frame\_number\_rel}** | The frame number of the sequence being rendered, relative to 0 regardless of the frame start number. Useful if you have sequences that begin in negative regions. This token will be stripped for any video output, as it is meant only for image sequence files. If using time dilation, this value will be used for `{frame_number}` as well. |
| **{frame\_number\_shot\_rel}** | The frame number of the shot being rendered, relative to 0 regardless of the frame start number. Useful if you have sequences that begin in negative regions. This token will be stripped for any video output, as it is meant only for image sequence files. If using time dilation, this value will be used for `{frame_number_shot}` as well. |
| **{camera\_name}** | The currently active camera actor name in Sequencer. |
| **{shot\_name}** | The name of the Shot Section in the Level Sequence, otherwise falls back to sequence asset names. |
| **{render\_pass}** | Will be replaced with the name of the Render Pass the image is for during rendering. Automatically inserted if rendering multiple render passes to ensure final images have unique names. |
| **{output\_resolution}** | The full output resolution, formatted by {width}\_{height}. |
| **{output\_width}** | The output resolution's width. |
| **{output\_height}** | The output resolution's height. |
| **{version}** | The version number defined by either **Auto Version** or **Version Number**. |
| These tokens become available to use as you add settings to your list. |  |
| **{ts\_count}** | The **Temporal Sample** count of your Anti-aliasing setting, if [**Anti-Aliasing**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine#anti-aliasing) is being used. |
| **{ss\_count}** | The **Spatial Sample** count of your Anti-aliasing setting, if [**Anti-Aliasing**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine#anti-aliasing) is being used. |
| **{shutter\_timing}** | The **Shutter Timing** property of your Camera setting, if [**Camera**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine#camera) is being used. |
| **{overscan\_percentage}** | The **Overscan** Percentage property of your Camera setting, if [**Camera**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine#camera) is being used. |
| **{tile\_count}** | The **Tile Count** property of your High Resolution setting, if [**High Resolution**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine#highresolution) is being used. |
| **{overlap\_percent}** | The **Overlap Ratio** property of your High Resolution setting, if [**High Resolution**](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine#highresolution) is being used. |

## Anti-Aliasing

Anti-Aliasing controls the number of samples used to produce a final frame. The Movie Render Queue adds the ability to combine multiple renders together to produce a final frame. This significantly increases the quality of anti-aliasing, motion blur, and can decrease noise from ray tracing. There are two types of sampling that produce the final frame: **Temporal** and **Spatial**.

![anti aliasing render settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6640a7e1-34cb-48da-8548-fc5f65c16f9b/aasetting.png)

**Temporal sampling** takes the time the camera shutter is open (based on the camera/post-processing Motion Blur Amount setting) and slices the frame into corresponding time slices. The engine then evaluates at the center of each time slice while using the standard engine motion blur to interpolate between each time slice. This enables rotational motion blur by representing the motion blur as many small directional motion blurs.

Because the engine is ticked (and by extension time passes in the world) these are called *temporal* samples. For each temporal sample, there are as many renders accumulated according to the **Spatial Sample Count** variable. Using too many temporal samples will create too small of a delta time for the engine to handle and will result in warnings after a render.

**Spatial sampling** takes each sample that is going to be rendered and renders it multiple times, each time jittering the camera a little bit. This is useful for renders where you have a very short motion blur duration and still need more samples to increase anti-aliasing or reduce noise.

Any combination of spatial and temporal sampling produces the same pattern of offsets used for anti-aliasing. This means that it is generally more efficient to put your samples into temporal sampling instead of spatial, since non-moving objects will receive the same anti-aliasing, and moving objects will be blurred, hiding the aliasing.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a2af76db-aa3c-4a73-9615-45760241e6d7/tsseq1.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e98a76f5-9284-4b2c-91ca-71e6e3ea2f89/tsseq2.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d1e28441-0831-4ff2-be1e-d91eeaca6568/tsseq3.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9f458828-0afa-44d9-8ec5-6ac104747f1e/tsseq4.png)
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f23b4c5b-438b-4650-b5cd-dda7433e8e60/tsseq5.png)

**Increasing the Temporal Sample count will result in smoother, radial motion blur.**

You can use Spatial and Temporal sampling with TAA to experiment with anti-aliasing results, though it is not recommended in most cases. If TAA is enabled then there is a limit on how many unique positions are chosen for anti-aliasing. This limit is defined by **r.TemporalAASamples**, which defaults to 8. If TAA is enabled and you have more than 8 samples, you should enable **Override Anti-Aliasing** and set it to **None** to disable TAA, or increase **r.TemporalAASamples** to match the sample count resulting from **Spatial Count x Temporal Count**.

If you use a Temporal Sample Count higher than 1, the sequence will be evaluated on either side of the frame. This means that you will need to extend your tracks in Sequencer to cover the time one frame before the start of your sequence, otherwise there will be no data to sample. Sections will be auto-expanded to cover the timespan evaluated by the first temporal sample. Some track types, like animation or audio, cannot automatically be expanded and will be skipped. You will be notified post render which sections need to be expanded by hand.

| Name | Description |
| --- | --- |
| **Spatial Sample Count** | Determines how many accumulated renders are in each Temporal Sample. |
| **Temporal Sample Count** | Determines how many time intervals each frame is divided into. |
| **Override Anti-Aliasing** | Enables you to choose a different anti-aliasing method using the **Anti-Aliasing Method** property. |
| **Anti Aliasing Method** | When Override Anti-Aliasing is enabled, this field will select the desired anti-aliasing method.   * **None**: Disables anti-aliasing. Recommended if you are using 8 or more spatial/temporal samples. * **FXAA**: Smooths jagged pixels in screen-space rather than using data from the 3D meshes in the world, which is faster than TAA or MSAA, but less precise for fine details. * **TemporalAA**: Uses Temporal Anti-Aliasing. This is the default algorithm for motion blur used in Unreal Engine which uses the information from previous frames to anti-alias the current frame. May cause ghosting, especially if a moving object is in front of a noisy background. * **MSAA**: Not supported. |
| **Use Camera Cut for Warm Up** | When enabled, the system will determine the amount of warmup frames based on the Camera Cut section before the start time. This feature will cause these frames to be evaluated during warmup which enables you to have characters animate from their reference pose with cloth, or have particles/cloth appear to continue motion from the previous shot. camera cut warm up |
| **Render Warm Up Frames** | If enabled, Movie Render Queue will submit each Engine Warm Up frame to the GPU to be rendered. This can be useful if your content must be rendered to properly warm up, such as GPU particles or virtual texturing. If disabled Engine Warm Up frames will tick the game thread but not submit renders to the GPU. |
| **Render Warm Up Count** | Controls the number of samples used to build the temporal history before rendering begins. When a camera cut or shot occurs, the temporal history used by TAA is cleared to prevent "ghosts" from the previous camera angle appearing. To allow anti-aliasing on the first frame, this history must be rebuilt. All samples are taken at the same time without ticking the engine between them. This happens immediately before rendering starts regardless of the number of **Engine Warm Up Count** frames or whether or not **Render Warm Up Frames** is enabled. |
| **Engine Warm Up Count** | Indicates the number of frames to run the engine for before rendering begins. These frames are not submitted to the GPU unless **Render Warm Up Frames** is enabled. Typically the warmup is useful when you need time for cloth physics, particles, or other dynamics to settle into the right position before rendering starts. |

## Burn In

Burn In allows for adding custom watermarks to your render, typically these would be timecode related. You can choose whether the burn in is applied to the final image, or rendered to a separate layer

![render burn in setting](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0ee5fa89-e534-4512-9e04-aa73a185c823/burnsetting.png)
