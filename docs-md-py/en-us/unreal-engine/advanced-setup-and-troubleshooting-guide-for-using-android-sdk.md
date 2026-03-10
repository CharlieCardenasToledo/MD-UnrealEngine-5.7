# Advanced Android SDK Setup

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/advanced-setup-and-troubleshooting-guide-for-using-android-sdk

> Application Version: 5.7

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For a simplified Android SDK setup workflow, try the <a data-document-id=\"3235411\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/set-up-android-sdk-ndk-and-android-studio-using-turnkey-for-unreal-engine?application_version=5.5\">Setting Up Android SDK and NDK</a> guide, which partially automates the setup process. Refer to this guide if you have conflicting Android SDK installations or need troubleshooting.",
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

Unreal Engine uses the **Android Software Development Kit (SDK)** distributed with **Android Studio** for all essential Android development components, including the **Android Native Development Kit (NDK)**. This page provides a walkthrough for setting up Android Studio and ensuring that Unreal Engine recognizes these components correctly, and some troubleshooting tips for managing NDK installations and earlier engine builds.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you try to run the SetupAndroid script before all prerequisites are met, it will fail to find the needed SDK components. Therefore, when troubleshooting Android SDK installation, <strong>review this page in its entirety</strong>, as the setup process depends on the steps being followed in the order listed.",
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

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Due to an update to the Android SDK Command-line Tools in February 2023, users on Unreal Engine 4.27 through 5.1 need to edit the SetupAndroid script used in this tutorial. This documentation is for UE 5.4 and newer. If you are experiencing problems, refer to the documentation for your version of Unreal Engine.",
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

## Recommended Setup

Make sure that **Unreal Editor** and the **Epic Games Launcher** are both closed to ensure that there are no problems with either the installation of NDK components or setting your environment variables for the engine.

If you need to support an earlier installation of Unreal Engine, refer to the section on Manually Targeting SDK Paths. You can find the needed NDK version for your version of Unreal Engine in the [Android Development Requirements](https://dev.epicgames.com/documentation/en-us/unreal-engine/android-development-requirements-for-unreal-engine?application_version=5.6) page.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Unreal Engine 5.3 and newer uses jbr (OpenJDK 17) for its JDK installation, but UE 5.2 and older use jre (Java 1.8). This means that when you uninstall your previous Android Studio installation, you may lose jre and cause errors in UE 5.2 and older.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "If you need to support UE 5.2 and older, before continuing, locate the jre directory and copy it somewhere outside the Android Studio directory to avoid losing it. You can then target this folder manually in your older versions of Unreal Engine. See Manually Target SDK Paths for more information.",
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

## Install Android Studio

Before setting up the required SDK and NDK components on your computer, you need to install **Android Studio**.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Refer to <a data-document-id=\"3954565\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/android-development-requirements-for-unreal-engine?application_version=5.6\">Android Development Requirements</a> for information about which Android Studio and NDK versions are compatible with your current version of Unreal Engine.",
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

1. Navigate to the [Android Studio Archive](https://developer.android.com/studio/archive) in your web browser. Scroll down to **Android Studio Koala Feature Drop | 2024.1.2 Patch 1 September 17, 2024**. Unfold the dropdown, and download the appropriate installer or zip file for your operating system. ![Select Android Studio Koala Feature Drop 2024.1.2 Patch 1 September 17, 2024 on the Android Studio archive page](https://dev.epicgames.com/community/api/documentation/image/9fd4e3d0-1bb7-4613-97df-c063bf8d461b)
2. Run the **Android Studio installer**. In the **Android Studio Setup** dialog, click **Next** to continue.
3. In the **Choose Components** dialog, leave the default components enabled. Click **Next** to continue.
4. In the **Install Locations** dialog, make sure the installation location is set to the default. Click **Next** to continue.
5. In the **Choose Start Menu Folder** dialog, click **Install** to begin the installation process.
6. When the installation finishes, click **Next** to begin setting up components.
7. When setup completes, make sure the **Start Android Studio** box is checked and click **Finish** to exit the installer.

## Set Up Android Studio for First-Time Use

When you start your new install of Android Studio for the first time, follow these steps:

1. When the **Data Sharing** dialog appears, choose whether or not you want to send usage statistics to Google. This is an option you may choose at your discretion, and selecting either choice will continue to the next step.
2. In the **Welcome to Android Studio** dialog, click the **More Actions** dropdown and click **SDK Manager**. ![The Welcome to Android Studio dialog. The SDK Manager option is highlighted in the More Actions dropdown.](https://dev.epicgames.com/community/api/documentation/image/7745725f-11b5-428e-940c-1c29d59fa2d3)
3. In the **Android SDK** system settings, click the **Edit** button next to **Android SDK Location**. ![Edit the Android SDK Location](https://dev.epicgames.com/community/api/documentation/image/472da502-1519-4525-bd21-9448da9bd822)
4. In the **SDK Components Setup** dialog, the needed components are already selected. Click **Next** to install them. ![Installing the SDK Components](https://dev.epicgames.com/community/api/documentation/image/aa54eb57-ccf1-4822-8b5b-3df2e1d948df)
5. In the **Verify Settings** window, click **Next** again to continue the installation.
6. When installation completes, click **Finish**.
7. In the **Settings** menu, click the **SDK Tools** tab. This displays a list of optional components.
8. Check the **Show Package Details** box to display all available SDK components.
9. Check the box for **Android SDK Command-line Tools (latest)**. Click **Apply** to download and install this component. ![Installing Android SDK Command-Line Tools](https://dev.epicgames.com/community/api/documentation/image/eda7b0d0-ade8-45c7-8a59-a7ff86e02944)
10. Click **OK** to dismiss the window and close the welcome dialog.

## Finalize the Android Studio Installation on Your OS

After completing all of the above steps, you need to finalize your installation to make sure your environment is fully set up before proceeding. Each operating system requires a different step to finalize installation.

| Operating System | Required Action |
| --- | --- |
| Windows | Restart your computer. |
| Linux | Close your terminal window and reopen it. |
| macOS | Either close your terminal window and reopen it, or log out and log back in. |

## Reset or Verify Your Environment Variables

The steps in this section are primarily for users moving from UE 5.2 and earlier to UE 5.3 and newer, who may need to reset their environment variables. If you are working with a fresh installation of UE and Android Studio, continue to the next section.

This is especially important for users who have used AGDE for debugging, as UE and AGDE now both target the jbr directory and do not need separate environment variables.

1. Open your computer's **System Properties**.
2. Click the **Environment Variables** button.
3. If you have an environment variable called `AGDE_JAVA_HOME`, delete it. This variable is no longer necessary, as both Unreal Engine and AGDE now use the same Java version.
4. Reset or verify the following environment variables. Replace `(Username)` with your username, and `(NDK Version Number)` with the directory name for the version number needed for your installation.

If you need to support an earlier version of Unreal Engine, we recommend following the above steps to maintain compatibility with current and future versions of Unreal Engine. To preserve the paths for your previous versions of Unreal Engine, we recommend that you edit your Project Settings and manually target the SDK paths for their versions of Android SDK, NDK, and JDK. Refer to Manually Target SDK Paths below for more information.

## Run the SetupAndroid Script

With the necessary Android SDK components installed, you can use the `SetupAndroid` script to download and install the appropriate version of Android NDK.

1. Open the `Engine/Extras/Android` directory and run the appropriate `SetupAndroid` script for your operating system: `SetupAndroid.bat` – Windows `SetupAndroid.command` – Mac `SetupAndroid.sh` – Linux.
2. The script prompts you to accept the Android SDK license agreement. Type **Y** and press **Enter** to accept.
3. When the installation completes, press any key to dismiss the command prompt.
4. Restart your computer for all changes to take effect.

The install directory for NDK should be `C:/Users/[Username]/AppData/Local/Android/SDK/ndk/`, where `[Username]` is your login name for your computer. You should see a folder containing the required NDK version in this location.

## Manually Target SDK Paths

If you followed the instructions above without encountering problems, Unreal Engine will automatically associate the SDK paths for the Android SDK, the current Android NDK version, and the Java Development Kit (JDK). However, if you are using an earlier version of the Unreal Engine alongside Android Studio, you may need to manually target your SDK paths to be compatible. You will most likely need to do this if you are migrating from UE 5.0, 5.1, or 5.2 to UE 5.3 or later.

To find the SDK paths, open **Edit** > **Project Settings**, then go to the **Platforms** > **Android** > **Android SDK** section.

![Configure Manual SDKs in Project Settings/Platforms/Android/Android SDK in Unreal Editor](https://dev.epicgames.com/community/api/documentation/image/63aca34f-88a4-4f5d-bccf-cdc7a5245936)

If these fields are blank, UE falls back on a set of default paths used by the installation process in the previous sections. If you have multiple installations of these components, or have installed them in non-standard directories, you can manually provide their paths here. Alternatively, you can open `BaseEngine.ini` and provide them under the `[/Script/AndroidPlatformEditor.AndroidSDKSettings]` section.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "[/Script/AndroidPlatformEditor.AndroidSDKSettings]\n    SDKPath = (Path=&quot;C:\\Filepath&quot;)\n    NDKPath = (Path=&quot;C:\\Filepath&quot;)\n    JDKPath = (Path=&quot;C:\\Filepath&quot;)",
  "lines_of_code": 4,
  "id": 131761,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzE3NjEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0MSswMDowMCJ9--0fab077741fd7268ba1fc15ba7842b1f073bef5c891385305b9143f8b61747d5",
  "settings": {
    "is_hidden": false
  }
}
```

If the entries for SDKPath, NDKPath, and JDKPath do not exist in your `BaseEngine.ini`, they will use the default path to the Android home directory.
