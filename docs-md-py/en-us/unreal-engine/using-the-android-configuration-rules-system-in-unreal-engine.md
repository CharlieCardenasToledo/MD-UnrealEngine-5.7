# Android Configuration Rules System

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-android-configuration-rules-system-in-unreal-engine

> Application Version: 5.7

The Android Configuration Rules system gives Android developers using Unreal Engine control over determining if a particular Android-based device has the needed hardware and software to run their project. The following information and steps will enable you to develop your UE projects for the devices and software you intend to support.

## Config Rules File

To get started, create a new text file called **configrules.txt** and place it in your projects **Build/Android** directory.

![Image](https://dev.epicgames.com/community/api/documentation/image/f8bf4fc5-e567-47ad-954b-e87e43004ab3)

_Click for full image._

Once you have the `configrules.txt` file created and placed in the Build/Android directory, open it up in your text editor of choice and add the following text, making sure that it is the first item in the file.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// version:1",
  "lines_of_code": 1,
  "id": 164798,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ3OTgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--5a4bb387ddd95969585d6020d809652f7e316704782fc5d7338aa69bbcf4c911",
  "settings": {
    "is_hidden": false
  }
}
```

The above text is the version code parsed by the ConfigRulesTool during packaging, and must be present in this form (one space between "//" and "version:", and no spaces after the colon). The number starts at one and should be incremented any time you update the file. UE will then use this number to determine if a newer version should be used than what is currently embedded in the Android Package (APK).

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Any line that starts with a <strong>//</strong> or <strong>semicolon(;)</strong> is treated as a comment and ignored.",
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

Commands are used to manipulate case-sensitive variables which either trigger an immediate action or are passed on to the engine. Any variables still defined after the Config Rules runs may be queried from C++ with the following function:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FString* FAndroidMisc::GetConfigRulesVariable(const FString&amp; Key);",
  "lines_of_code": 1,
  "id": 164799,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ3OTksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--8d1dccf7246362914c6b3c423aa2a935b8193eda6aae7bdef29c6b93fac0c006",
  "settings": {
    "is_hidden": false
  }
}
```

**Example:**

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#if PLATFORM_ANDROID\n\tIf (FAndroidMisc::GetConfigRulesVariable(TEXT(&quot;myflag&quot;) == TEXT(&quot;true&quot;))\n\t{\n\t\tUE_LOG(LogAndroid, Display, TEXT(&quot;myflag was set!&quot;));\n\t}\n\t#endif",
  "lines_of_code": 6,
  "id": 164800,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MDAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--de0fffd8556a84e0108a32bc004e5d30ba3ef41dd0ab9c539d0484ff014734d9",
  "settings": {
    "is_hidden": false
  }
}
```

It is also possible to get access to a TMap with the key/value entries if you would like to iterate over them:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "TMap&lt;FString, FString&gt; FAndroidMisc::GetConfigRulesTMap();",
  "lines_of_code": 1,
  "id": 164801,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MDEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--2bb8f7ca2d7932fbfb76dd6ea9cae57d4bb6bb7e6ee304eda049d7913b2d261f",
  "settings": {
    "is_hidden": false
  }
}
```

**Example:**

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#if PLATFORM_ANDROID\n\tTMap&lt;FString, FString&gt; ConfigRules = FAndroidMisc::GetConfigRulesTMap();\n\tfor (const TPair&lt;FString, FString&gt;&amp; Pair : ConfigRules)\n\t{\n\t\tFString VarKey = Pair.Key;\n\t\tif (VarKey.StartsWith(&quot;myvars_&quot;))\n\t{\n\t\t\tFString VarValue = Pair.Value;\n\t\t\tUE_LOG(LogAndroid, Log, TEXT(&quot;Found variable %s = %s&quot;), *VarKey, *VarValue);\n\t}\n",
  "lines_of_code": 12,
  "id": 164802,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MDIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--35a6746402a4e4ac8c501a861b8004ecf312fb98af7ba9363386cad0c94b0382",
  "settings": {
    "is_hidden": false
  }
}
```

## Config Rules Variables

Variables may be used in values with the following syntax:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "$(varname)",
  "lines_of_code": 1,
  "id": 164803,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MDMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--9d434efb1c7cd582cb0b9656f013c79f50489a0dec202f676b6b5446068523c2",
  "settings": {
    "is_hidden": false
  }
}
```

This means that the following:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "&quot;$(SRC_DeviceMake) $(SRC_DeviceModel)&quot;",
  "lines_of_code": 1,
  "id": 164804,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MDQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--bedddfe1f247690297da2eb6ef28952359fc0d576135abc03fcdc84af4d3cac7",
  "settings": {
    "is_hidden": false
  }
}
```

Would be replaced with the values of **SRC\_DeviceMake** and **SRC\_DeviceModel** separated by a space.

The following variables are defined automatically before `configrules.txt` is parsed:

| Variable Name | Description | Example Value |
| --- | --- | --- |
| memory | Total memory in megabytes. | 3550 |
| hardware | The chipset (either Hardware from /proc/cpuinfo or getprop ro.hardware). | Qualcomm Technologies, Inc SDM845 |
| ro.hardware | The result from "getprop ro.hardware". | blueline |
| processor | Processor type from /proc/cpuinfo. | AArch64 Processor rev 12 (aarch64) |
| processorCount | Processor count from /proc/cpuinfo. | 8 |
| useAffinity | Whether or not to set thread affinity to little cores for some threads. | true |
| hasNEON | Indicates processor supports NEON features (SIMD). | true |
| isARM64 | Indicates processor supports ARM64 ABI. | true |
| littleCoreMask | Bitmask indicating which cores are little. | 0x0f |
| bigCoreMask | Bitmask indicating which cores are big. | 0xf0 |
| SRC\_GpuVendor | Vendor from GLES20.glGetString(GLES20.GL\_VENDOR). | Qualcomm |
| SRC\_GpuFamily | GPU family from GLES20.glGetString(GLES20.GL\_RENDERER). | Adreno (TM) 630 |
| SRC\_GlVersion | GL version from GLES20.glGetString(GLES20.GL\_VERSION). | OpenGL ES 3.2 V@313.0 (GIT@3f88ca2, I42f6fe38fb) (Date:07/13/18) |
| SRC\_AndroidVersion | Android version from android.os.Build.VERSION.RELEASE. | 9 |
| SRC\_DeviceMake | Device manufacturer from android.os.Build.MANUFACTURER. | Google |
| SRC\_DeviceModel | Device model from android.os.Build.MODEL. | Pixel 3 |
| SRC\_DeviceBuildNumber | Device build number from android.os.Build.DISPLAY. | PD1A.180720.030 |
| SRC\_VulkanVersion | Version of Vulkan support. | 1.1.0 |
| SRC\_VulkanAvailable | Indicates if Vulkan is supported by the device. | true |
| SRC\_UsingHoudini | Indicates ARM emulated on Intel processor by Houdini. | false |
| SRC\_SDKLevel | SDK level from android.os.Build.VERSION.SDK\_INT. | 28 |
| supportsFloatingPointRenderTargets | Indicates GPU supports FP render targets. | true |
| TextureFormats | Comma-separated list of supported texture formats by GPU. | ASTC,ATC,ETC2,ETC1 |
| navigationBarHeight | Height of Android navigation bar in pixels. | 132 |
| statusBarHeight | Height of Android status bar in pixels. | 66 |
| screenWidth | Screen width in pixels. | 1080 |
| screenHeight | Screen height in pixels. | 2160 |

## Config Rules Commands

Commands can be used with valid arguments in the forum of **action:argument**. These are defined below along with use case examples.

**Set** allows you to assign one or more variables and their specified values:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "set:(myvar=true)",
  "lines_of_code": 1,
  "id": 164805,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MDUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--8eaf00132797d4abe58337726df70710d59ab5acb70142d2acfb687eb02df48e",
  "settings": {
    "is_hidden": false
  }
}
```

If you have more than one variable, you can use a **comma** (**,**) to separate them:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "set:(myvar=false,myvar2=&quot;something&quot;,myvar3=&quot;else&quot;)",
  "lines_of_code": 1,
  "id": 164806,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MDYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--3087d2592496d72ca927d257001122d416871ae1bf4f224f35097d3eae7b75a3",
  "settings": {
    "is_hidden": false
  }
}
```

**clear** allows you to clear the value assigned to variables.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "clear:(myvar)",
  "lines_of_code": 1,
  "id": 164807,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MDcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--8c8b9fed31b1ead361b21ff32b8d553f1405925741ded279c9785661a41e4c09",
  "settings": {
    "is_hidden": false
  }
}
```

You can clear more than one variable at a time using a **comma** (**,**) to separate the values you want to clear.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "clear:(myvar,myvar3)",
  "lines_of_code": 1,
  "id": 164808,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MDgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--e6e21a1cdd5cef8a4b90ef1c7a298c0536799cde708091fbe7b1c5027b062fa6",
  "settings": {
    "is_hidden": false
  }
}
```

**condition** evaluates the list of conditions and if all are true it applies optional set and clear commands.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "condition:((comparison)[,(comparison)],[(set)],[(clear)]",
  "lines_of_code": 1,
  "id": 164809,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MDksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--3f13f41d647a32fac5bd5b96c6e4ac4fe88d0218c54b4928c1a779739af97a9e",
  "settings": {
    "is_hidden": false
  }
}
```

The comparisons are made up of three parts in parentheses separated by commas. The three parts are **SourceType**, **CompareType**, and **MatchString**.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "(SourceType=isARM64,CompareType=CMP_EQUAL,MatchString=&quot;true&quot;)",
  "lines_of_code": 1,
  "id": 164810,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MTAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--278a4615f31f242a1585ee1e4498ee8e1bbecc27320bbf1d1e8c05696e337641",
  "settings": {
    "is_hidden": false
  }
}
```

**SourceType** specifies the first argument for comparison and will usually be a variable name. The following are the three special SourceType values that can be used:

| Command Name | Description |
| --- | --- |
| SRC\_PreviousRegexMatch | The group returned from the last regex expression condition. |
| SRC\_CommandLine | The command line embedded in the APK. |
| [EXIST] | Used with MatchString to see if a variable exists or not. |

**MatchString** is any string value to use for the comparison or the variable name for the **[EXIST]** case.

**CompareType** may be one of the following:

| Command Name | Description |
| --- | --- |
| CMP\_Exist | True if variable name in MatchString is set. |
| CMP\_NotExist | True if variable name in MatchString is not set. |
| CMP\_Equal | True if variable name in MatchString is not set. |
| CMP\_NotEqual | True if SourceType not equal to MatchString. |
| CMP\_EqualIgnore | True if SourceType equals MatchString, ignoring case. |
| CMP\_NotEqualIgnore | True if SourceType does not equal Matchstring, ignoring case. |
| CMP\_Less | True if value of SourceType < value of MatchString. |
| CMP\_LessEqual | True if value of SourceType <= value of MatchString. |
| CMP\_Greater | True if value of SourceType > value of MatchString. |
| CMP\_GreaterEqual | True if value of SourceType >= value of MatchString |
| CMP\_Regex | True if regex in MatchString found in SourceType (matching group is available in SRC\_PreviousRegexMatch for additional condition checks) |

The following examples show how you might setup and use the Android Config Rules Commands in your UE projects:

The following code will set **myvar** to **arm64** if **isARM64** is **true**:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "condition:((SourceType=isARM64,CompareType=CMP_EQUAL,MatchString=&quot;true&quot;)),(myvar=&quot;arm64&quot;)",
  "lines_of_code": 1,
  "id": 164811,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MTEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--c8366f4d129326c42888d46d5934d5662d1d7757f3dd93d69559483cc14b7b24",
  "settings": {
    "is_hidden": false
  }
}
```

The following code will set **myvar** to **arm64** if **isARM64** is **true** and clears **notsupported**:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "set:(notsupported=true)\n\tcondition:((SourceType=isARM64,CompareType=CMP_EQUAL,MatchString=&quot;true&quot;)),(myvar=&quot;arm64&quot;),(notsupported)",
  "lines_of_code": 2,
  "id": 164812,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MTIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--6fbe16b8be0aaa9fa3a133ade67b129d7a8b3763a10b33b190aadd9a270c829d",
  "settings": {
    "is_hidden": false
  }
}
```

The following code uses **Regex** to extract the number in **Adreno (TM) 630** and compares it to see if it is less than **510** to flag an error.:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "condition:((SourceType=SRC_GpuFamily,CompareType=CMP_Regex,MatchString=&quot;(?!Adreno \\(TM\\))([0-9][0-9]*)&quot;),(SourceType=SRC_PreviousRegexMatch,CompareType=CMP_LessEqual,MatchString=&quot;510&quot;)), (error=&quot;CR_Info_UnsupportedGPU&quot;)",
  "lines_of_code": 1,
  "id": 164813,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MTMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--e8e00e2b3eea2b33ef827886f065b8e4f2f5d097ef9f8703a8cdb2876147bbbe",
  "settings": {
    "is_hidden": false
  }
}
```

**chipset** is a shortcut to set a group of variables if the hardware string is equal to either ro.hardware or hardware. It sets useAffinity, chipset, GPU, processorCount, bigCoreMask, and littleCoreMask. useAffinity controls whether or not taskgroup threads are restricted to the little cores with the littleCoreMask.:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "chipset: hardware string, useAffinity, part name, GPU name, processor count, big core mask, little core mask",
  "lines_of_code": 1,
  "id": 164814,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MTQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--c3d8d1d284d5b2c6998af8cf2102cfc966ee495d77b40fae940bc37f14c8358c",
  "settings": {
    "is_hidden": false
  }
}
```

Here are some examples:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "chipset:&quot;Qualcomm Technologies, Inc MSM8929&quot;, true, &quot;Snapdragon 415&quot;, &quot;Adreno (TM) 405&quot;, 8, 0xf0, 0x0f\nchipset:&quot;Qualcomm Technologies, Inc MSM8937&quot;, true, &quot;Snapdragon 435&quot;, &quot;Adreno (TM) 505&quot;, 8, 0xf0, 0x0f\nchipset:&quot;Qualcomm Technologies, Inc MSM8940&quot;, true, &quot;Snapdragon 435&quot;, &quot;Adreno (TM) 505&quot;, 8, 0xf0, 0x0f\nchipset:&quot;Qualcomm Technologies, Inc MSM8952&quot;, true, &quot;Snapdragon 617&quot;, &quot;Adreno (TM) 405&quot;, 8, 0xf0, 0x0f\nchipset:&quot;Qualcomm Technologies, Inc MSM8953&quot;, true, &quot;Snapdragon 625/626&quot;, &quot;Adreno (TM) 506&quot;, 8, 0xf0, 0x0f\nchipset:&quot;Qualcomm Technologies, Inc MSM8956&quot;, true, &quot;Snapdragon 650&quot;, &quot;Adreno (TM) 510&quot;, 6, 0x03, 0x0f\nchipset:&quot;Qualcomm Technologies, Inc MSM8976&quot;, true, &quot;Snapdragon 652/653&quot;, &quot;Adreno (TM) 510&quot;, 8, 0xf0, 0x0f\nchipset:&quot;Qualcomm Technologies, Inc SDM630&quot;, true, &quot;Snapdragon 630&quot;, &quot;Adreno (TM) 508&quot;, 8, 0xf0, 0x0f\nchipset:&quot;Qualcomm Technologies, Inc SDM636&quot;, true, &quot;Snapdragon 636&quot;, &quot;Adreno (TM) 509&quot;, 8, 0xf0, 0x0f\nchipset:&quot;Qualcomm Technologies, Inc SDM660&quot;, true, &quot;Snapdragon 660&quot;, &quot;Adreno (TM) 512&quot;, 8, 0xf0, 0x0f\n",
  "lines_of_code": 25,
  "id": 164815,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MTUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--a7ae8e7c0d98e05bfc5c2258bcfc4c9893a1ad8bb719febd5726e578e8a986f1",
  "settings": {
    "is_hidden": false
  }
}
```

## Config Rules Special Variables

There are two special variables which trigger actions if set:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "set:(log=&quot;message for the logcat&quot;)",
  "lines_of_code": 1,
  "id": 164816,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MTYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--d79b18cf087e5d33274a42759c12f4355b88f4baeb2a8eba1d1255b56ce7847f",
  "settings": {
    "is_hidden": false
  }
}
```

The value of log after any command is evaluated will be written to the logcat output and cleared.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "set:(dumpvars=1)",
  "lines_of_code": 1,
  "id": 164817,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MTcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--0021f7e85162686c2bc0d1557942203df07b50cf2779ea671eb3c5bfa32b9844",
  "settings": {
    "is_hidden": false
  }
}
```

This will dump all the variables currently set and their values to logcat.

## Config Rules Profiles

You can set the **Profile** variable to override the device profile used instead of the one that would be picked by the **AndroidDeviceProfileMatchingRules** in `DefaultDeviceProfiles.ini`. If this value is not modified the normal rules will still apply. The following example would force the **Android\_Galaxy\_S9Plus\_Adreno** setting for **SM-G965** models:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "condition:((SourceType=sammodel,CompareType=CMP_Regex,MatchString=&quot;SM\\-G965&quot;)), (Profile=&quot;Android_Galaxy_S9Plus_Adreno&quot;)",
  "lines_of_code": 1,
  "id": 164818,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MTgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--4db48ca608e34426858485b7689d4d42d61ef0fd8d0f1fe6c6adcb9adb6f7b8a",
  "settings": {
    "is_hidden": false
  }
}
```

## Config Rules Dialog

You can customize the error and warning dialog messages that are displayed using the following variables:

- caption
- exitbutton
- continuebutton
- updatebutton
- helpbutton

The value placed in the caption or buttons is looked up in the string table to get the localized text for the dialog. You should make these string names unique and place them in a `ConfigurationStrings.xml` file in your project's **Build/Android/res/values** directory for each localized language your project supports. (values-fr, for example, would be for French).

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "An example of where the ConfigurationStrings.xml file should be placed is shown below.",
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

![Image](https://dev.epicgames.com/community/api/documentation/image/e2e8ea4b-812b-487f-ab94-3860dec483c3)

_Click for full image._

- **Error -** You can signal an **error** by setting the **error variable**. The dialog will show the string table entry for the value you assign to it. All processing of the configrules.txt will stop once this is set and the user will not be able to continue into your application.
- **Warning** - A **Warning** dialog is triggered by setting the **warning variable**. The dialog will provide a continue option and optionally update and/or help buttons if the corresponding variables are set. The help button will launch an external browser to the URL specified by the link variable. Evaluation of configrules.txt will continue until the end or error is set before the dialog is shown so you can change it again with different conditions if necessary.

The following example code was setup to display an error is the user tried to use an Android device that does not support ARM64.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "set:(caption=&quot;CR_Caption_DeviceNotSupported&quot;, exitbutton=&quot;CR_Button_Quit&quot;, continuebutton=&quot;CR_Button_Continue&quot;, helpbutton=&quot;CR_Button_Help&quot;)\n\tcondition:((SourceType=isARM64,CompareType=CMP_EQUAL,MatchString=&quot;false&quot;)),(error=&quot;CR_Info_RequiresARM64&quot;)",
  "lines_of_code": 2,
  "id": 164819,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MTksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--7f5ca09402431b09d50c0745edd88789ead95f4a4cac4e4fa81f516c72d8ae9c",
  "settings": {
    "is_hidden": false
  }
}
```

When the above example is encountered, the error message that is displayed will come from the following string table.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;\n&lt;resources&gt;\n\n&lt;string name=&quot;CR_Button_Quit&quot;&gt;Quit&lt;/string&gt;\n&lt;string name=&quot;CR_Button_Help&quot;&gt;More Info&lt;/string&gt;\n&lt;string name=&quot;CR_Button_Continue&quot;&gt;Continue&lt;/string&gt;\n&lt;string name=&quot;CR_Button_Update&quot;&gt;Check for Update&lt;/string&gt;\n\n&lt;string name=&quot;CR_Caption_DeviceNotSupported&quot;&gt;Device Not Supported&lt;/string&gt;\n\n",
  "lines_of_code": 12,
  "id": 164820,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MjAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--30d36d5c08d0ca62449df40e857044953ffa2220a85265083061cebc2c457173",
  "settings": {
    "is_hidden": false
  }
}
```

## Config Rules Build Files

The following additions to your project are required for the `configrules.txt` file to be included in your APK by compressing, and optionally encrypting, it. Start by registering the following **Unreal Plugin Language** (UPL) code in your project's **`Build.cs`** file:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "if (Target.Platform == UnrealTargetPlatform.Android)\n\t{\n\t// Add UPL to add configrules.txt to our APK\n\tstring PluginPath = Utils.MakePathRelativeTo(ModuleDirectory, Target.RelativeEnginePath);\n\tAdditionalPropertiesForReceipt.Add(&quot;AndroidPlugin&quot;, System.IO.Path.Combine(PluginPath, &quot;MyGame_UPL.xml&quot;));\n\t}",
  "lines_of_code": 6,
  "id": 164821,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MjEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--8a1ba8e315891d842f4414632ea11b4017630ca011c97d4cc365648ebcbdb7f4",
  "settings": {
    "is_hidden": false
  }
}
```

Next you will want to create a new file called `MyGame_UPL.xml` which is placed in the same directory with the `Build.cs` file.

![Image](https://dev.epicgames.com/community/api/documentation/image/2559483a-2e88-4e63-9d37-05346c26f795)

_Click for full image._

Open up the `MyGame_UPL.xml` file and then add the following code, saving the file when done (change the ConfigRulesKey to contain your unique encryption key):

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;\n\t&lt;root xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;&gt;\n\t\t\n\t\t&lt;init&gt;\n\t\t\t\n\t\t\t&lt;setString result=&quot;ConfigRulesKey&quot; value=&quot;This is my encryption key&quot;/&gt;\n\t\t&lt;/init&gt;\n\t\t\n\t\t&lt;gradleCopies&gt;\n\t\t\t&lt;copyFile src=&quot;$S(BuildDir)/configrules.txt&quot;\n",
  "lines_of_code": 52,
  "id": 164822,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjQ4MjIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyNDo0NyswMDowMCJ9--201af8bc87102b74a298f7f7f9e4185ba034aefd58cb311b1deed6ceedd6f3e1",
  "settings": {
    "is_hidden": false
  }
}
```
