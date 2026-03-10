# Windows Metal Shader Compiler

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-windows-metal-shader-compiler-for-ios-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The Windows Metal shader compiler currently does not work in UE 5.1 through UE 5.4.",
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

**Unreal Engine** can compile shaders for Apple's **Metal** API on a Windows machine, greatly simplifying the workflow for iOS applications. To enable this functionality, you need to install Apple's **Metal Developer Tools for Windows**. Unreal Engine will automatically use this toolset once it is set up.

## Steps

To install Metal Developer Tools for Windows, follow these steps:

1. Sign in to your **Apple Developer Account** in your web browser, then navigate to the **Downloads** section.
2. In the tabs on the upper-right of the Downloads page, click the **Release** tab. ![The Beta Downloads page](https://dev.epicgames.com/community/api/documentation/image/385c3bcb-ed64-4dee-ba13-9163e8448b78)
3. In the Software Downloads page, click the **Applications** button. ![The Applications button](https://dev.epicgames.com/community/api/documentation/image/30d12aaf-0ed3-4dbf-ad67-654685b31077)
4. Scroll down the page until you find the entry for **Metal Developer Tools for Windows**, then click the **Download** button to download the installer. ![The entry for Metal Developer Tools for Windows](https://dev.epicgames.com/community/api/documentation/image/2fab47ec-dd4e-45f7-bd3d-096dc23b5124)
5. Run the installer to install the Metal Developer Tools.

## Final Result

Once you have completed setup for the Metal Developer Tools for Windows, your Windows installation of Unreal Engine will be able to compile shaders for Metal 2.0. No additional setup is required.
