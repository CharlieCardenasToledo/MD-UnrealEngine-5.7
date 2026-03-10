# UMG Safe Zones

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-safe-zones-in-unreal-engine

> Application Version: 5.7

**Safe Zone** widgets are an essential part of developing a game user interface (UI) that can run on a lot of different devices. Safe zones are designed to keep the UI from displaying somewhere that it can technically use but the player can't see, such as the edge of a TV display or under the notch and home bar of the iPhoneX. The UMG Designer enables you to test the resolution (or rotation) of the device with your UI and applied Safe Zone widgets.

When you add a **Safe Zone** widget to the **Designer** , the widget will scale any other widgets that are made children of it from the **Hierarchy** panel. These child widgets will scale and adjust anytime there is an "unsafe" zone.

![Without Safe Zone widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4d899957-1bf7-40c7-809d-0845d371a05c/withoutsafezone_opt-1.png)

![With Safe Zone widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/79f15dfc-7524-4d77-98ca-54c6ea7220c7/withsafezone_opt.png)

In this example, a 1080p display has a **Uniform Safe Zone** area of 0.9 (red) for testing and debugging purposes. When the widgets are parented to a Safe Zone widget, the child widgets will scale to the safe zone area. This prevents widgets from being cut off at the screen edge deemed "unsafe". This can be seen in the example, with the "My Menu" title text.

## Setting and Testing Safe Zone Resolutions

In UMG (or for [Play-in-Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine) settings), the screen sizes chosen are now linked with [Device Profiles](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-device-profiles-in-unreal-engine) which also takes into account the [Mobile Content Scale Factor](https://dev.epicgames.com/documentation/en-us/unreal-engine/performance-guidelines-for-mobile-devices-in-unreal-engine#mobilecontentscalefactor), meaning that the final resolution and DPI scale will change based on the selected device.

To test the screen resolution of a device, use the UMG **Designer** viewport to select the **Screen Size** dropdown and select from the listed devices.

![ScreenSizeSelection.png](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/57d5da6d-b88b-4e4f-8374-7b121b00c2b6/screensizeselection_opt.png)
