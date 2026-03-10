# Setting Up a New AR Project

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-a-new-ar-project-in-unreal-engine

> Application Version: 5.7

This guide shows how to create a new empty project in Unreal Engine and add the necessary Blueprints and configurations to turn it into an AR experience.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you want to start with an AR project that is set up already, see the following AR templates:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "enhanced_list",
      "style": "unordered",
      "items": [
        [
          {
            "type": "paragraph",
            "content": "<a data-document-id=\"3235599\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/handheld-ar-template-quickstart-in-unreal-engine\">Handheld AR Template for iOS and Android</a>",
            "settings": {
              "is_hidden": false
            }
          }
        ]
      ],
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

Follow these steps to create a new Unreal Engine project and level with minimal rendering features enabled. Blank projects open with the default level, which includes a Sky Sphere and Atmosphere Fog objects. These objects will persistently overlay everything in AR, so it's useful to start with an empty level when creating an AR experience to control what will be displayed.

1. Launch **Unreal Engine** from the [Epic Games Launcher](https://www.epicgames.com/store/en-US/download).
2. In the **Unreal Project Browser** window, choose **Games**. ![Choose Games in the Unreal Project Browser](https://dev.epicgames.com/community/api/documentation/image/6d64fbe4-d2ce-4588-b19b-47841047f7dd)
3. Select the **Blank Template**. ![Select the Blank Template](https://dev.epicgames.com/community/api/documentation/image/842a7347-825c-4e96-83ad-219abf1da87f)
4. For the **Project Defaults**, choose the following: Blueprint Scalable Raytracing Disabled Mobile No Start Content ![Choose Project Defaults](https://dev.epicgames.com/community/api/documentation/image/9a3a19a3-9de4-4ed2-b0a6-e663b75f307b)
5. In the main menu, select **Edit > Plugins**, and in the **Plugins** windows, search for and enable the **AR Utilities** plugin. Click **Restart Now**, and wait for Unreal Engine to restart. ![Enable the AR Utilities plugin](https://dev.epicgames.com/community/api/documentation/image/bf7b3b85-3a9a-45ec-b3f8-2db433c83bde)
6. From the Editor, choose **File > New Level…** and choose **Empty Level**. Make sure to name and save your level. In this example, the level is named **Main**. ![Select Empty Level](https://dev.epicgames.com/community/api/documentation/image/b1ce08b4-1931-48a5-8f82-393d3512a432)
7. In the main navigation, choose **Edit > Project Settings.**
8. In the Project Settings window, select **Maps & Modes** under the **Project** section. Set the **Editor Startup Map** and the **Game Default Map** to the new level **Main.** ![Project Settings Maps & Modes](https://dev.epicgames.com/community/api/documentation/image/dadf4eef-c917-4cb6-83e0-703a3db36cff)

## Adding a Pawn and Game Mode

In Unreal Engine, a [pawn](https://dev.epicgames.com/documentation/en-us/unreal-engine/pawn-in-unreal-engine) is the physical representation of the user and defines how the user interacts with the world. The [Game Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-mode-and-game-state-in-unreal-engine)
object defines the rules of the experience, such as which pawn object
to use. In order to build a new AR project, you need to set up the pawn
so you can interact with the environment when you run your app.

Follow the steps below to create a Pawn and Game Mode for your AR project.

1. Right-click in the **Content Drawer** and choose **Blueprint Class** from the list. In the **Pick Parent Class** window, select **Pawn**. Name the asset **ARPawn**. ![Select Blueprint Class](https://dev.epicgames.com/community/api/documentation/image/72eb0e8b-6752-4f21-95f9-f0ceabef2193) ![Pick Actor as parent class](https://dev.epicgames.com/community/api/documentation/image/aa6a120c-33c1-4ea9-9510-4b24f7948660)
2. Double-click the **ARPawn** object in the **Content Drawer** to open it in the **Blueprint Editor**. In the Blueprint Editor, choose **Add Component** and search for **Camera**. ![Add a Camera component](https://dev.epicgames.com/community/api/documentation/image/1066dc85-5cc2-421d-84b7-71e35b131d73)
3. Make sure the **Camera** component's parent is **DefaultSceneRoot**. ![Make sure DefaultSceneRoot is the Camera component's parent](https://dev.epicgames.com/community/api/documentation/image/7bceb098-d307-497e-95f5-f1a47b36458f)
4. Right-click in the **Content Drawer** and choose **Blueprint Class** from the list. In the **Pick Parent Class** window, select **Game Mode Base**. Name the asset **ARGameMode**. ![Select Game Mode Base as the parent class](https://dev.epicgames.com/community/api/documentation/image/0eb67d97-fa6f-4ad7-958c-7290bb4d2a09)
5. Double-click **ARGameMode** to edit the settings. Set **Default Pawn Class** to **ARPawn**. ![Set Default Pawn Class to ARPawn](https://dev.epicgames.com/community/api/documentation/image/30f81e2a-f2f4-4c77-a457-eb9645992113)
6. In the main navigation, choose **Edit > Project Settings** to open the **Project Settings** window.
7. In the **Project Settings** window under the **Project** section on the left, select **Maps & Modes**. Set **Default GameMode** to **ARGameMode.** Set **Default Pawn Class** to **ARPawn**. ![Set the Default Game Mode and the Default Pawn Class](https://dev.epicgames.com/community/api/documentation/image/6c612806-8dff-4619-ae58-791c1b2a8427)

## Creating an AR Session

The function **Start AR Session** requires an ARSessionConfig object, which defines all the AR-specific capabilities for the project. See [UARSessionConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AugmentedReality/UARSessionConfig?application_version=5.6) for more information on what each setting is.

Follow the steps below to add the AR session logic to your project.

1. Right-click in the **Content Drawer**. Choose **Miscellaneous > Data Asset** to open the **Pick Data Asset Class** window. ![Select Data Asset](https://dev.epicgames.com/community/api/documentation/image/47306ce0-0180-4ee9-a434-aecc133f827e)
2. In the **Pick Data Asset Class** window, choose **ARSessionConfig**. Name the data asset **ARSessionConfig**. Open the asset and select **Save** to confirm the default AR options. ![Pick ARSessionConfig as the data asset instance](https://dev.epicgames.com/community/api/documentation/image/83b0121d-ee47-4ae7-b71c-190aef74d4a7)
3. Double-click the **ARPawn** asset to open it in the **Blueprint Editor**. Add the function **Set Tracking Origin**. Set the **Origin** value to **Floor Level**. ![Set Tracking Origin node value set to Floor Level](https://dev.epicgames.com/community/api/documentation/image/973016e3-f034-4025-af51-558c071472c6)
4. Add the function **Start AR Session**. Set **Session Config** asset to **ARSessionConfig**. ![Start AR Session node value set to ARSessionConfig](https://dev.epicgames.com/community/api/documentation/image/005bab3e-810c-4d67-924f-c309c41a97b6)
5. Add the function **Stop AR Session**. ![Add Stop AR Session node](https://dev.epicgames.com/community/api/documentation/image/34694341-9c57-44f9-b3fd-e94c4359c4d3)

When you launch your project on your device, you will now be able to
navigate your AR environment. See the documentation for your AR platform
for detailed steps on how to launch your Unreal project on your device.

## On Your Own

In this guide, you learned how to create a new AR project, and add the necessary Blueprints to get started building an AR app.
