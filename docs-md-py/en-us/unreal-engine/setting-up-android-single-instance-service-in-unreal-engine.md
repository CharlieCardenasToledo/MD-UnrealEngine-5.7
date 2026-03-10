# Setting Up Android Single Instance Service

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-android-single-instance-service-in-unreal-engine

> Application Version: 5.7

This guide explains how to set up Android Single Instance Service (ASIS) in Unreal Engine, then how to create, package, and run your Unreal Engine project as an Android application.

## Set up Android SDK and NDK

To set up ASIS, you must first set up the Android Software Development Kit (SDK) and Android Native Development Kit (NDK) in Unreal Engine. Unreal Engine uses Android Studio and the Android SDK Command-Line Tools to download and install the Android SDK components required to develop Android projects.

To set up the Android SDK and NDK, follow these steps:

1. Follow the steps on the [Setting Up Android SDK and NDK](https://dev.epicgames.com/documentation/en-us/unreal-engine/set-up-android-sdk-ndk-and-android-studio-using-turnkey-for-unreal-engine?application_version=5.5) page.
2. If you are using Unreal Engine 5.5 or higher, enable the following SDK Platforms and Tools: **SDK Tools** > **Android SDK Build-Tools 36** > **35.0.0** and **34.0.0** ![SDK Tools > Android SDK Build-Tools 36 > 35.0.0 and 34.0.0](https://dev.epicgames.com/community/api/documentation/image/4805fd3d-1c59-4b3e-89f9-19674f97a456) **SDK Tools** > **NDK (Side by side)** > **25.1.8937393** ![SDK Tools > NDK (Side by side) > 25.1.8937393](https://dev.epicgames.com/community/api/documentation/image/c3d5889d-407b-41c1-af75-750806f9026b) **SDK Platforms** > **Android 14.0 ("UpsideDownCake")**, API Level 34 ![SDK Platforms > Android 14.0 ("UpsideDownCake"), API Level 34, Revision 3](https://dev.epicgames.com/community/api/documentation/image/1bec09c8-739a-40bb-a07f-0b1ede84e8fd)

## Create a New Project from the ASIS Template

After the Android SDK and NDK are installed, you can setup the ASIS template plugin. The plugin is delivered as a separate archive, so manual steps need to be done to prepare the Unreal Engine source code.

### Get Unreal Engine source code

Pull the latest source code from the UE5 Main in either Perforce or Github. For more information on using Perforce and Github with Unreal Engine, refer to the following resources:

- [Using Perforce as Source Control](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-perforce-as-source-control-for-unreal-engine)
- [How To Use Unreal Engine 5 - Perforce](https://www.perforce.com/blog/vcs/how-use-unreal-engine-5-perforce)
- [Accessing Unreal Engine source code on Github](https://www.unrealengine.com/en-US/ue-on-github)
- [Downloading Unreal Engine Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine)
- [Building Unreal Engine from Source](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source)

### Set Up the ASIS Plugin

1. Navigate to the ASIS Templates folder.

1. Navigate to the ASIS Templates folder. If you're using Perforce, navigate to `UE5_Main\Engine\Restricted\NotForLicensees\Plugins\AndroidSingleInstanceService\Templates\` If you're using GitHub, access the `ue5-main` branch and navigate to `ue5-main\Engine\Restricted\NotForLicensees\Plugins\AndroidSingleInstanceService`.
2. Copy the **TP\_HMI\_ASIS** folder to `UE5_Main\Templates\` (Perforce) or `ue5-main\Templates\` (GitHub).
3. Copy the following code and paste it in `UE5_Main\Templates\TemplateCategories.ini` (Perforce) or `ue5-main\Templates\TemplateCategories.ini` (GitHub):
4. Run **UnrealEditor**. The Unreal Project Browser should now include a new HMI template: ![The new HMI template in the Unreal Project Browser.](https://dev.epicgames.com/community/api/documentation/image/064bc529-a97b-4e9b-a555-90d1d4caec11)
5. Click **Create**. The project should look like the following screenshot: ![A screenshot of Unreal Engine, showing a blank HMI project created from the template.](https://dev.epicgames.com/community/api/documentation/image/316b10fa-ac4a-4156-ac36-f72862a03c7e)

Add ASIS Plugin to an Existing Project

## Add ASIS Plugin to an Existing Project

If you have an existing project you want to add ASIS to, follow these steps:

1. Go to **Edit** > **Plugins**and enable **AndroidSingleInstanceService**. ![Screenshot of the enabled AndroidSingleInstanceService plugin](https://dev.epicgames.com/community/api/documentation/image/61a68dd3-fa01-4188-97bf-40934caee4bb)
2. Copy the following code and paste it into the `{Project_Name}/Config/DefaultGame.ini` file:
3. In Unreal Engine, go to **Edit** > **Project Settings.**
4. Under **Plugins** > **AndroidSingleInstanceService**, enable the following settings: ![The Android Single Instance Service settings](https://dev.epicgames.com/community/api/documentation/image/9a0995f5-67be-4c14-a577-e58ddb820adb) **Compile ASISProject** **Enable asis libs generation** **Use AndroidSingleInstanceService**

## Package and Run the ASIS Project

After setting up ASIS in your Unreal Engine project, you can package and run the project as an Android application.

To package the ASIS project as an Android application, follow these steps:

1. In the Main Toolbar, click **Platforms** > **Android** > **Package Project**. ![The Package Project menu item](https://dev.epicgames.com/community/api/documentation/image/7932f70c-52a5-4add-8367-8a51bb4e2734)
2. Check the **Output Log** to make sure the build was successful. ![The Output Log showing a successful build.](https://dev.epicgames.com/community/api/documentation/image/a5702abe-77d4-4fd9-a3cc-9e9e544c27a9)

The package is saved by default to `/Documents/UnrealProjects/_packages/ASIS_Package`.

![The ASIS package folder](https://dev.epicgames.com/community/api/documentation/image/8c4d1055-1c28-4715-b549-b315b4707d9c)

### Communicating Between The Android Application and the Unreal Engine APK

After packaging the application, you can use an example client application to communicate with the Unreal Engine APK.

The Unreal Engine package includes 3 main parts:

- An **APK** with Android Service. It is located in the folder that was chosen while project package dialog.
- A set of ASIS helper libraries that are used in the client applications.
- An example client application that communicates with the service. This is not located in the packaged Unreal Engine project, but the Binaries folder of your Unreal Engine Project (`\Unreal Projects\{Project_Name}\Binaries\Android`). ![The example application in the Binaries folder.](https://dev.epicgames.com/community/api/documentation/image/e7619fc2-1635-4b2d-8fd9-e26e8f13cc91)

You can use Android Studio to open the example Android project. It will automatically go through the Android build process when you open it.

You can also build the project using the following command line prompt:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "command_line",
  "title": "",
  "code_preview": "cd {Project_Name}\\Binaries\\Android\\ExampleUseCase_{Project_Name}\\\ngradlew assembleDebug",
  "lines_of_code": 2,
  "id": 42762,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0Mjc2MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU3KzAwOjAwIn0=--b7b0c3f472e5061d97096b401917ced9c46461b96e64645855454439a1ccc69b",
  "settings": {
    "is_hidden": false
  }
}
```

This command will generate an APK file at  `{Project_Name}\Binaries\Android\ExampleUseCase_{Project_Name}\app\build\outputs\apk\debug\app-debug.apk`.

In Android Studio, with an Android device selected, you can run the application by pressing **Shift**+ **F10,** or by clicking the **Play** button in the top toolbar.

![The Play button in Android Studio](https://dev.epicgames.com/community/api/documentation/image/69a185de-e7b8-4bc6-a238-2dac361443ca)

To install the APK on your Android device, run the following `adb` command:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "adb install {Project_Name}.apk",
  "lines_of_code": 1,
  "id": 42763,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0Mjc2MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU3KzAwOjAwIn0=--3e8a49bb7ca3e0210d1ebc0b2a8c46c70905a7a3601611f6d3b47575a72fa0c4",
  "settings": {
    "is_hidden": false
  }
}
```

In the application on your device, tap **Activate View1**, **Activate View2**, and **Activate View3** to view the Android Service communicating with the Unreal Engine application.

![The Android app, showing the three views.](https://dev.epicgames.com/community/api/documentation/image/00778065-0b86-4da8-b8fd-cc615db138f3)
