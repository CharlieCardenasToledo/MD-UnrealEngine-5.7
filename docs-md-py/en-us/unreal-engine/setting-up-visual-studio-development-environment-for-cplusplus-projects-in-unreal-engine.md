# Setting Up Visual Studio

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine

> Application Version: 5.7

Unreal Engine (UE) is designed to integrate smoothly with **Visual Studio** (VS), providing the means to quickly make code changes in your projects and immediately see results upon compilation. Setting up VS to work with UE can help improve developers' efficiency and overall user experience.

This document covers the basics for setting up your Unreal Engine-to-Visual Studio workflow.

## Version Compatibility

The following table lists which versions of VS are integrated with the binary version of UE.

| Unreal Engine Version | VS 2019 Version | VS 2022 Version |
| --- | --- | --- |
| 5.7 | Not supported | 17.8 or later, 17.14 recommended (Default) |
| 5.6 | Not supported | 17.8 or later, 17.14 recommended (Default) |
| **5.5** | Not supported | 17.8 or later, 17.10 recommended (Default) |
| **5.4** | Not supported | 17.4 or later, 17.8 recommended (Default) |
| **5.3** | 16.11.5 or later | 17.4 or later, 17.6 recommended (Default) |
| **5.2** | 16.11.5 or later | 17.4 or later (Default) |
| **5.1** | 16.11.5 or later (Default) | 17.4 or later |

Other software versions:

| Software | Minimum Version | Recommended Version |
| --- | --- | --- |
| **MSVC** | 14.44.35214 | 14.44.35214 |
| **Windows SDK** | 10.0.19041.0 | 10.0.22621.0 or newer |
| **LLVM** | 18.1.3 | 18.1.8 |
| **.NET** | .NET 8.0 | .NET 8.0 |

## Verifying UE Prerequisites

If you installed UE from the Epic Games Launcher or cloned it from GitHub, the UE Prerequisite Installer automatically installed the necessary dependencies, libraries, and frameworks required to run the engine.   
  
If you installed or synced UE from Perforce, run the Prerequisite Installer before running any UE tools you’ve built locally. Find the installer in `[UNREAL_ENGINE_ROOT]\Engine\Extras\Redist\en-us\.`

## Adding Visual Studio Installation Options

If you are installing Visual Studio (VS) for the first time or modifying an existing installation, ensure you have the following workloads and components enabled.

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "To modify your VS installation, run the Visual Studio Installer, then click <b>Modify </b>next to the latest version. ",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26245177,
      "caption": "",
      "alt_text": "Modify button in the Visual Studio Installer",
      "image": {
        "id": 26245177,
        "file_name": "ue5_1-visual-studio-installer.png",
        "file_size": 31677,
        "content_type": "image/png",
        "created_at": "2025-11-10T21:05:56.425+00:00",
        "height": 374,
        "width": 854,
        "storage_key": "17ddf27a-e03b-4b90-95dd-9df35cba38e8",
        "context": "documentation"
      },
      "storage_key": "17ddf27a-e03b-4b90-95dd-9df35cba38e8",
      "context": "documentation",
      "width": 650,
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

### Adding Required Workloads

In the installer’s **Workloads** tab, under **Desktop & Mobile**, enable the following options:

- .NET desktop development
- Desktop development with C++
- .NET Multi-platform App UI development

Under **Gaming**, enable **Game development with C++**.

### Adding Required Components

In the installer’s **Installation Details** panel, expand **Game development with C++** and enable the following options:

- C++ profiling tools
- C++ AddressSanitizer
- Windows 10 or 11 SDK (10.0.18362 or Newer)
- Unreal Engine installer

![Visual Studio Workloads and components to include in install](https://dev.epicgames.com/community/api/documentation/image/28753bf9-2392-424e-b224-a03643d9335b)

_Click to enlarge image._

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "When you open your first Unreal Engine C++ project in VS, you might see a missing-components warning in the <b>Solution Explorer</b>. Click <b>Install </b>to allow VS to install any additional components necessary for your project.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 26245179,
      "caption": "",
      "alt_text": "Visual Studio Solution Explorer warns about missing components",
      "image": {
        "id": 26245179,
        "file_name": "ue5_3-visual-studio-missing-components.png",
        "file_size": 28011,
        "content_type": "image/png",
        "created_at": "2025-11-10T21:05:56.688+00:00",
        "height": 207,
        "width": 324,
        "storage_key": "9d7b81fe-5a93-4af4-a42e-75ac4fe4c57c",
        "context": "documentation"
      },
      "storage_key": "9d7b81fe-5a93-4af4-a42e-75ac4fe4c57c",
      "context": "documentation",
      "width": 350,
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

## Recommended Settings

These optional VS interface adjustments can make your development experience more convenient.

### Turning Off the Error List Window

Typically, the **Error List** window automatically opens when you have an error in your code. However, when working with UE, the Error List window can display additional downstream errors that make it difficult to identify the root cause. You can disable the Error List window and instead use the Output Log to see real code errors when working with UE.

To turn off the Error List window, follow these steps:

1. In VS, go to **Tools > Options**.
2. On the left side of the **Options** window, select **Projects and Solutions**.
3. Disable **Always show Error List if build finished with errors**.
4. (Optional) Change any other options and features from the table below that are relevant to your project.
5. Click **OK**.

| To: | In Options, go to: | And change this option: |
| --- | --- | --- |
| Prevent chunks of code from appearing grayed out in the text editor | **Text Editor > C/C++ > View** | Set **Show Inactive Blocks** to **False** |
| Hide unneeded folders in the Solution Explorer | **Text Editor > C/C++ > Advanced** | Set **Disable External Dependencies Folders** to **True** |
| Enable IntelliSense (code completion, suggestions, and automatic code formatting as you write) | **Text Editor > C/C++ > IntelliSense** | Turn on **Enable 64-bit IntelliSense** |

### Increasing the Width of Solution Configurations Dropdown Menu

You might find it useful to widen the Solution Configurations dropdown in the VS toolbar so you can view the full name of any custom configurations.

To widen the Solution Configurations menu, follow these steps:

1. In Visual Studio, right-click the main **toolbar** and select **Customize** at the bottom of the context menu.
2. In the **Customize** window, click the **Commands** tab, select the **Toolbar** radio button, and use the dropdown menu to change the **Toolbar** to **Standard**. ![In the Customize window, click Toolbar radio button and select Standard from the dropdown](https://dev.epicgames.com/community/api/documentation/image/0cf4ba42-ebd9-4056-8dd7-3a1184cd5b7c)
3. In the toolbar **Preview**, scroll through the options to find and select **Solution Configurations**, then click **Modify Selection**. ![Click Solution Configurations and then click Modify Selection](https://dev.epicgames.com/community/api/documentation/image/32bd8a23-1b72-48c5-a434-c896680f6622)
4. Change the **Width** to **200** and click **OK**. VS updates the toolbar with its new size.
5. Close the **Customize** window.

### Adding the Solution Platforms Dropdown Menu

When developing for multiple platforms, it’s convenient to have the Solution Platforms dropdown menu in your VS toolbar.

If you don’t see this menu on the right side of the Solution Configurations dropdown, you can add it to the toolbar by clicking the small arrow button on the right side of the Standard toolbar, go to **Add or Remove Buttons**, and select **Solution Platforms**.

![Visual Studio's main toolbar with Add More Buttons arrow highlighted](https://dev.epicgames.com/community/api/documentation/image/857bc198-4e0a-48ec-9049-fab518a57707)
