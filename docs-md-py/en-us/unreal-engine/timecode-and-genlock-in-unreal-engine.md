# Timecode and Genlock

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/timecode-and-genlock-in-unreal-engine

> Application Version: 5.7

By default, the Unreal Editor generates its own timecode, based on the current system time on your computer. This timecode is set by default to run at 30 frames per second, but the engine typically renders many more frames than 30 in any given second. So, typically multiple consecutive frames in the output will get assigned the same timecode value.

When you're working with professional video, you often have to keep timecode in sync between multiple different video feeds and signal processing devices. To do this, you may need to make the Unreal Engine's timecode match the timecode of the video feed you're working with. In some cases, you may want to go even further, and lock the engine so that it only produces one single frame for each frame of video that comes in through a reference input — we refer to this as *genlock*.

This page describes how to make the Unreal Engine adopt the timecode values from a port that you specify on your AJA card instead of generating its own, and how to genlock the Unreal Engine to that timecode signal.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Timecode and genlock management is under active development, and is likely to change in future versions.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

## Visualizing Timecode in the Unreal Editor

To see the actual timecode values being used by the Unreal Engine while you're working in the Unreal Editor, use the **Timecode Provider** panel. You can find this panel in the main menu under **Window > Virtual Production > Timecode Provider**.

![Image](https://dev.epicgames.com/community/api/documentation/image/7fe33b65-e66c-483f-8397-8b8365c3af03)

It displays the current timecode, the timecode provider (the source of the timecode values), and the number of timecode frames that are being generated within each second. You can dock this panel anywhere in the UI of the main Level Editor.

Alternatively, you can use the following console command:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "stat timecode",
  "lines_of_code": 1,
  "id": 162546,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjI1NDYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNzo0NiswMDowMCJ9--3d56cf397c1045a96e6cd9ae58ce3a06baf0b1d2f8ce0833988fb22aa4810099",
  "settings": {
    "is_hidden": false
  }
}
```

You'll see the values printed in the Unreal Editor viewport, in **HH:MM:SS:FF** format:

![Timecode display in the viewport](https://dev.epicgames.com/community/api/documentation/image/32832f3c-2153-4601-917f-4b97619357d5)

If you have the Unreal Engine set up to adopt timecode from an input signal, or to genlock to a video signal, you'll also see the source of the timecode and genlock. For example:

![Genlocked and synchronized timecode in the viewport](https://dev.epicgames.com/community/api/documentation/image/d436e46c-3cfa-4aa8-a39a-c8dff349db52)

You can use this command to confirm that the Unreal Engine is generating frames at the rate you're expecting, and that it's using the same timecode values as your input video.

## Setting up Timecode and Genlock

The following steps show how to make the Unreal Engine adopt its timecode values from an input SDI video feed coming in from an AJA or Blackmagic device, and how to make the Unreal Engine lock its frame rate to that feed so that it generates only one frame of output for each frame of input.

1. Right-click in the Content Browser, and choose **Create Basic Asset > Blueprint Class**. ![Create new Blueprint class](https://dev.epicgames.com/community/api/documentation/image/3a3367d3-6027-4196-aa8c-a9c93700f38d)
2. In the **Pick Parent Class** window, expand the **All Classes** section (1). Search for and select the **AjaTimecodeProvider** class (pictured) or **BlackmagicTimecodeProvider** class (2), then click **Select** (3). ![TimecodeProvider parent classes](https://dev.epicgames.com/community/api/documentation/image/b0aa5392-8f19-4fa7-a9ef-911f37cf599a) Back in the Content Browser, give your new Asset a descriptive name, such as **AJA\_Timecode\_Port** or **Blackmagic\_Timecode\_Port**.
3. Double-click your new Asset to open it up in the Blueprint Editor, and set up the properties in the **Details** panel. To read the timecode from an incoming video stream, set the **Video Configuration** or **Media Configuration** to point to the port on your AJA or Blackmagic card, and (if applicable) the type of timecode to read from the feed (LTC or VITC). If you are using an AJA card, and you want to read the timecode from a reference port on the card rather than from a video stream, enable **Use Reference In** and set the **Reference Configuration** instead of the **Video Configuration**.
4. **Compile** and **Save** your Blueprint class, and close the Blueprint Editor.
5. If you want to genlock the Unreal Engine to your video source, repeat the previous instructions to create and set up another Blueprint class, but this time use **AjaCustomTimeStep** or **BlackmagicCustomTimeStep** as the parent class. ![Custom Time Step Provider parent classes](https://dev.epicgames.com/community/api/documentation/image/ace7a7b0-5690-4687-9217-ade5a00993ed)
6. This class requires similar settings to the **AjaTimecodeProvider** or **BlackmagicTimecodeProvider**: ![Custom Time Step Provider settings](https://dev.epicgames.com/community/api/documentation/image/946c5970-acdb-489d-8e2e-aa29643f2dca) AJA cards also offer additional settings; see the tooltips for details.
7. From the main menu, choose **Edit > Project Settings**. In the **Project Settings** window, open the **Engine > General Settings** category (1), and find the **Timecode** section (2). From the **TimecodeProvider** drop-down list, select the timecode port Asset that you created. ![Set the TimecodeProvider in the Project Settings](https://dev.epicgames.com/community/api/documentation/image/c9e27f3f-ef15-4904-a219-42e69c588953)
8. If you want to genlock the Unreal Engine to your video source, find the **Framerate** section above, and expand the advanced properties at the bottom of the section. From the **Custom TimeStep** drop-down list, select the genlock port Asset that you created. ![Set the Custom TimeStep in the Project Settings](https://dev.epicgames.com/community/api/documentation/image/d43b3da0-6740-425a-8a66-1a459470cf9c)
9. Close the Unreal Editor and restart your Project.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you use Media Profiles to set up multiple different media configurations for your Project, you can also override these default Project-level settings for Timecode and Timestep Providers in each Media Profile. For more information, see <a data-document-id=\"3233352\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/supporting-multiple-media-configurations-in-unreal-engine\">Supporting Multiple Media Configurations</a>.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```

### End Result

As long as you have video input coming in to the port you set up for the timecode provider and custom timestep classes, and that video has the resolution, frame rate and timecode format that you specified, the Unreal Engine should adopt your video's timecode and lock its frame update frequency so that it generates one output frame for each input frame.

To verify that this is working, use one of the options described under [Visualizing Timecode in the Unreal Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/timecode-and-genlock-in-unreal-engine).

## Timecode Texel Encoding

For debugging purposes, the Media Source and Media Output Assets for AJA and Blackmagic devices can encode the timecode of each frame into the video image by illuminating pixels in white. This can be useful if you need a visual way to verify that a given frame of video actually matches the timecode signal that accompanies it.

Timecode is usually expressed in the format **HH:MM:SS:FF**, for a total of eight digits. Each of these digits is assigned a row in the texture output, starting from the top of the image. Within each of those rows, count from the left of the image to value of that timecode digit to find the pixel that represents the timecode value. The leftmost pixel is pixel number 0.

So, for example, given the timecode value 12:08:44:12:

- On the first row, the second pixel from the left is lit (pixel number 1).
- On the second row, the third pixel from the left is lit (pixel number 2).
- On the third row, the leftmost pixel from the left is lit (pixel number 0).
- On the fourth row, the ninth pixel from the left is lit (pixel number 8).
- and so on.
