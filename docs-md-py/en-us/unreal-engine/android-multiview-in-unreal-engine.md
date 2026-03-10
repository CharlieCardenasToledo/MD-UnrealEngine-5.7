# Android Multi-View

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/android-multiview-in-unreal-engine

> Application Version: 5.7

## Setup Android for Unreal Engine

To successfully package ASIS (Android Single Instance Service), you will need to setup Android SDK and NDK. Unreal Engine (UE) uses Android Studio and the Android SDK Command-Line Tools to download and install the Android SDK components required to develop Android projects. Follow the following documentation:

- Related Document

If you are using Unreal Engine 5.5.x, enable the following SDK Platforms and Tools:

![enable sdk platform and tools options](https://dev.epicgames.com/community/api/documentation/image/2f39b8c7-5588-4c5c-9017-afb013123893)

![enable settings](https://dev.epicgames.com/community/api/documentation/image/b981e3a3-6f3c-4eb0-bbc1-33b8146209b7)

![enable settings](https://dev.epicgames.com/community/api/documentation/image/7ccc6db8-936f-4777-93ab-4bd8a5712b5b)

## Create project from template

With Android SDK/NDK installed, we can now setup the ASIS template plugin. The plugin is delivered as a separate archive, so manual steps need to be done to prepare UE source code.

## Get UE5.\* source code

Pull the latest source code from UE5 Main (Perforce or Github)

Perforce:

- [Accessing Unreal Engine with Perforce](https://dev.epicgames.com/documentation/en-us/unreal-engine/accessing-unreal-engine-with-perforce)

Github:

- [Downloading Unreal Engine Source Code from GitHub](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine)

## Setup ASIS Plugin

### If using Perforce:

1. Navigate to ASIS plugin folder: `UE5_Main\Engine\Restricted\NotForLicensees\Plugins\AndroidSingleInstanceService`
2. Inside the `AndroidSingleInstanceService` folder, open the `Templates` folder: `UE5_Main/Engine\Restricted\NotForLicensees\Plugins\AndroidSingleInstanceService\Templates\`

### If using Github:

Unzip Archive provided by Epic and copy ASIS plugin contents to: `Engine\Restricted\NotForLicensees\Plugins\AndroidSingleInstanceService`

### Copy the Template

![Image](https://dev.epicgames.com/community/api/documentation/image/42c4d3d5-490b-47b3-b9dc-d6ce62cadae0)

Copy the **TP\_HMI\_ASIS** folder to the **UE5/Templates/**

![Image](https://dev.epicgames.com/community/api/documentation/image/785abef4-bc99-44d5-b8e8-6500cf5ddac5)

Next copy the following code to the **UE5\_Main/Templates/TemplateCategories.ini**

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "Categories=(Key=&quot;HMI&quot;, LocalizedDisplayNames=((Language=&quot;en&quot;,Text=&quot;Automotive\\nHMI &amp;\\nVehicle Cockpit using Android Single Instance Service&quot;)), LocalizedDescriptions=((Language=&quot;en&quot;,Text=&quot;Find templates for automotive vehicle cockpit using Android Single Instance Service&quot;), Icon=&quot;TP_HMI_ASIS/Media/AutomotiveHMI_2x.png&quot;, IsMajorCategory=true)",
  "lines_of_code": 1,
  "id": 44612,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYxMiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--4e64a39c4da27983605be9e3feca5cd972c9ac868fe870c18fb219d31c48fc8b",
  "settings": {
    "is_hidden": false
  }
}
```

Run UnrealEditor. Now we should see the new HMI template when we open the Unreal Engine Project browser:

## Create Project from HMI template

![Image](https://dev.epicgames.com/community/api/documentation/image/7f007f67-dee2-4b17-9744-a94447a6665d)

The project should look like this:

![Image](https://dev.epicgames.com/community/api/documentation/image/956f735b-a004-4f8b-bb4f-b43ec911d4af)

![Image](https://dev.epicgames.com/community/api/documentation/image/3105d159-ae51-4af1-86e8-99262f27309c)

## Add ASIS plugin to existing Project

If you have an existing project you need to add ASIS to, do the following:

1. Enable ASIS in the Plugin Settings ![Image](https://dev.epicgames.com/community/api/documentation/image/efb11471-2d9e-4bf8-8774-3aa626240a88)
2. Add remap plugin directory. Add next code to the {ProjectName}/Config/DefaultGame.ini
3. Open your project and enable the following ASIS plugin settings ![Image](https://dev.epicgames.com/community/api/documentation/image/f1faaf57-7249-4d3b-95bf-c512b4acf4e4)

### Package and run ASIS example

With Android SDK/NDK and the Template setup in Unreal engine, we can now package the project as Android application:

![Image](https://dev.epicgames.com/community/api/documentation/image/b8417101-24a3-4a3f-8b44-1c02ce38e5b4)

![Image](https://dev.epicgames.com/community/api/documentation/image/197a38bd-42c9-4ecc-ad41-57b6c90189b0)

## App Communication

With the app packaged from Unreal Engine, we will use an example client app to communicate with the Unreal Engine APK

The Unreal Engine Package will have 3 artifacts.

1. APK with Android Service. It is located in the folder that was chosen while project package dialog.
2. ASIS helper libraries that are used in the client applications.
3. Example of client application that communicates with Service. This is NOT located in the packaged unreal project instead in the Binaries folder of your Unreal Engine Project. The location is **\Unreal Projects\\*Project\_Name\*\Binaries\Android** ![Image](https://dev.epicgames.com/community/api/documentation/image/fdd46573-36d0-444c-8648-057563f5d357)

You can use Android Studio to open the Android project. It will automatically go through the android build process once you open it.

![Image](https://dev.epicgames.com/community/api/documentation/image/e3a989fd-8603-4985-9c94-25c6e1f2bbc3)

Or you could use command line.

cmd could be using to generate client apk

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "cd {Project_Name}\\Binaries\\Android\\ExampleUseCase_{Project_Name}\\\ngradlew assembleDebug",
  "lines_of_code": 2,
  "id": 44615,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYxNSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--c16e92b0a364b080b03aebc04058658fe8494835fa7b040a41260a7970d78c7a",
  "settings": {
    "is_hidden": false
  }
}
```

The apk will be generated in: 
`{Project_Name}\Binaries\Android\ExampleUseCase_{Project_Name}\app\build\outputs\apk\debug\app-debug.apk`

Back in Android Studio and with an Android device selected, you can run the app with **Shift**+**F10** or select the green Play button at the top menu

![Image](https://dev.epicgames.com/community/api/documentation/image/79545ae6-3b23-4513-bc32-6737775e2b0e)

### After installation Service

Now run install the Unreal Engine apk run applications to your device. You can use cmd line in the Unreal Engine package folder and run adb

![Image](https://dev.epicgames.com/community/api/documentation/image/f913e998-294d-4d87-80f6-c7f999e09e45)

In the Android App, select Activate View1, View2, and View3 to view the Android Service communicating with the Unreal Engine application

![Image](https://dev.epicgames.com/community/api/documentation/image/33d32a01-c7a8-4153-976c-6d34398870f7)

### Enable Multiview

Multiview works from version UE 5.6. Enabling Multiview requires AndroidSingleInstanceService Plugin. Go through the previous steps to enable ASIS then you can start here.

**Enable** the **Multiview** plugin in the plugin settings.

![Image](https://dev.epicgames.com/community/api/documentation/image/1ca55dc5-01ad-489a-95dd-ba1819964c20)

Create two cameras in the level to test Multiview. The TP\_HMI\_Automotive will be used for this example.

![Image](https://dev.epicgames.com/community/api/documentation/image/407226f9-1ad9-41ea-a5f0-d4ef811f73eb)

Next, open the Level Blueprint. Add the Camera Actors to the Blueprints. Drag off the Camera Actor node and Select ‘Get Camera View’. Then Delete the Get Camera Node, we just need the Camera Component Object Reference.

![Image](https://dev.epicgames.com/community/api/documentation/image/ed0d96f2-f07a-408e-aad7-5c5a974f9d0f)

Then create `Register Camera for Asis`. Connect the camera object node to the respective nodes. Make sure to set the Camera Id to 1 and 2 for each camera. Connect the execution pins to **Event Begin Play.**

![Image](https://dev.epicgames.com/community/api/documentation/image/abf33a0d-920a-475c-9729-0d2696d05ec3)

Package the project for Android.

![Image](https://dev.epicgames.com/community/api/documentation/image/de1a802d-8e85-42d1-a7d2-824c9ec9ead1)

Now we will open the client app in Android Studio. Open the example client Android application project. This is NOT located in the packaged unreal project instead in the Binaries folder of your Unreal Engine Project. The location for the course code for client app is: 
`{Project_Name}\Binaries\Android\ExampleUseCase_{Project_Name}\`

Next, switch from standard ASIS to MultiviewEdit.

Edit `Binaries\Android\ExampleUseCase_{Project_Name}\app\src\main\AndroidManifest.xml`Change game activity to **ActivityForMultiView** line 22.

![Image](https://dev.epicgames.com/community/api/documentation/image/4c21eeaa-f57a-4966-9c5e-b983be3f97cc)

In Android Studio and with an Android device connected, you can run the app with Shift+F10 or select the green Play button at the top menu.

After installation Service

Now run install the Unreal Engine apk run applications to your device. You can use cmd line in the Unreal Engine package folder and run adb.

![Image](https://dev.epicgames.com/community/api/documentation/image/bee98ed0-0314-4c82-9a67-92833c7c32ff)

Select the Attach/Detach View1 and Attach/Detach View2 to view the cameras. You now have ASIS with multiview working on Android.

### Architecture Overview

![Image](https://dev.epicgames.com/community/api/documentation/image/9bdb2ffd-42b9-4d35-8b3c-7cc4328c07e5)

Supported approaches

![Image](https://dev.epicgames.com/community/api/documentation/image/1b968204-79ae-49ae-bbfd-b44f64f5b463)

![Image](https://dev.epicgames.com/community/api/documentation/image/a8c27224-b1c2-45a6-946e-2c1244e647fe)

![Image](https://dev.epicgames.com/community/api/documentation/image/dfa55647-ba45-484f-97a0-2a02d0ba014c)

### Interface Description

Class `ASISConnection`

This class allows establishing a connection and communicating with an ASIS service. It encapsulates the complexities of this communication and provides an easy to use interface for sending and receiving data and commands.

`ASISConnection.ASISConnectionCallBacks` interface defines callbacks for ASISConnection events. Implement this interface when you want to handle connection success events.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public interface ASISConnectionCallBacks\n{\nvoid onConnectionSuccess();\nvoid onServiceDisconnected();\n}\n",
  "lines_of_code": 5,
  "id": 44616,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYxNiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--35256ecdfb5fa393fcc1168348974ea7a9c9abc9b6b3bce78203b3893feb01db",
  "settings": {
    "is_hidden": false
  }
}
```

`onConnectionSuccess()` - is called when connection to the service was successfully established.

`onServiceDisconnected()` -  is  called when a connection to the Service has been lost

`ASISConnection.EngineMessagesListener` interface defines a listener for engine messages.  Implement this interface when you want to handle messages from the engine.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public interface EngineMessagesListener\n{\nvoid onEngineMessage(Message message);\n}\n",
  "lines_of_code": 4,
  "id": 44617,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYxNywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--be70b2026f488bc47312dff89ce8e6f71e780ccb96f18db7332fa46188cdef65",
  "settings": {
    "is_hidden": false
  }
}
```

`onEngineMessage(Message message)` - called when a message is received from the engine.

`Message` - values of the incoming message

Class `ASISConnection.ConnectionBuilder`

This class implements the builder design pattern to create instances of `ASISConnection`. It follows a fluent style where methods can be chained, allowing for more readability when multiple parameters are required.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "ConnectionBuilder(Context ctx)",
  "lines_of_code": 1,
  "id": 44618,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYxOCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--bed02548325799d51e5ee306f317191f561af0373dfcc726e6036250104aa038",
  "settings": {
    "is_hidden": false
  }
}
```

Initializes a new instance of the `ConnectionBuilder` class using the given Context.

Parameters

- `ctx` - The Context in which to create the ConnectionBuilder.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public ConnectionBuilder withConnectionListener(ASISConnectionCallBacks connectionListener)",
  "lines_of_code": 1,
  "id": 44619,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYxOSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--ea658c467ff7112c859d4a5c156642f9a20def48270caee58a2c2c9b05af5363",
  "settings": {
    "is_hidden": false
  }
}
```

Sets the ASISConnectionCallBacks listener for the ASISConnection.

Parameters

- `connectionListener` - The ASISConnectionCallBacks listener to set.

Returns

- The ConnectionBuilder instance, allowing for method chaining.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public ConnectionBuilder withEngineMessageListener(EngineMessagesListener engineMessageListener)",
  "lines_of_code": 1,
  "id": 44620,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYyMCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--fa73fdf0c5d6ee27406a2a22d472d0e1e6c30255b9fbac8729b82bdfd0171c44",
  "settings": {
    "is_hidden": false
  }
}
```

Sets the EngineMessagesListener for the ASISConnection.

Parameters

- `engineMessageListener` - The EngineMessagesListener listener to set.

Returns

- The ConnectionBuilder instance, allowing for method chaining.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public ConnectionBuilder withConnectionId(String connectionID)",
  "lines_of_code": 1,
  "id": 44621,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYyMSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--9e3dfe0cf7629f17cff852f0689ab2890f3ceadac2ba08f2635f6f2c78e24410",
  "settings": {
    "is_hidden": false
  }
}
```

Sets the connectionID for the ASISConnection.

Parameters

- `connectionID` - string with connectioID

Returns

- The ConnectionBuilder instance, allowing for method chaining.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public ConnectionBuilder withServicePackageName(String packageName)",
  "lines_of_code": 1,
  "id": 44622,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYyMiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--28aeb3e45bc477a010ba9719e568fb5ddf57229149a367ef41eede7c755bdb19",
  "settings": {
    "is_hidden": false
  }
}
```

Override default service package name

Parameters

- `packageName` - service package name (com.epicgames.PROJECTNAME)

Returns

- The ConnectionBuilder instance, allowing for method chaining.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public ConnectionBuilder withServiceClassName(String className)",
  "lines_of_code": 1,
  "id": 44623,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYyMywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--53f42842ecf440d88078913a24250d5119a65c8cd9ef1917c4c277275c1d99e8",
  "settings": {
    "is_hidden": false
  }
}
```

Override default service class name

Parameters

1. `className` - service class name (com.epicgames.makeaar.UnrealSharedInstanceService)

Returns

- The ConnectionBuilder instance, allowing for method chaining.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public ConnectionBuilder withObbModuleName(String obbModuleName)",
  "lines_of_code": 1,
  "id": 44624,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYyNCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--2d536f5a6857e28a026f984226807acfc72ce4daa808c60753ad8461c2440932",
  "settings": {
    "is_hidden": false
  }
}
```

Override default obbModuleName

Parameters

- obbModuleName - content obb name (UE project name)

Returns

- The ConnectionBuilder instance, allowing for method chaining.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "public ConnectionBuilder withInsightsTracing()",
  "lines_of_code": 1,
  "id": 44625,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYyNSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--1a0bb1911b9a46982eb3c50783831584e36f98d544f539f43f9a237a7281d245",
  "settings": {
    "is_hidden": false
  }
}
```

Enable InsightsTracing

Returns

- The ConnectionBuilder instance, allowing for method chaining.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public ConnectionBuilder withCommandLineArgs(String cmdArgs)",
  "lines_of_code": 1,
  "id": 44626,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYyNiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--ae5068d331d5489fca0b25572dbe5f08cc8beb49f12dc5bf2735bcc0adfce3c0",
  "settings": {
    "is_hidden": false
  }
}
```

Override default command line args

Parameters

1. cmdArgs - command line arguments to start UE

Returns

- The ConnectionBuilder instance, allowing for method chaining.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public ConnectionBuilder withOverridePropagateAlpha(boolean value)",
  "lines_of_code": 1,
  "id": 44627,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYyNywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--6568e7b5ba4806a8f41a6260129832f7fdbad343765798217ac05a1797d5ac7c",
  "settings": {
    "is_hidden": false
  }
}
```

Override default mobile propagate alpha value

Parameters

- `value` - override mobile propagate alpha value

Returns

- The ConnectionBuilder instance, allowing for method chaining.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public ASISConnection build()",
  "lines_of_code": 1,
  "id": 44628,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYyOCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--4123d70e9442f75ec1d1a444c93a6b9b6e158821646c447563d4670e04c16454",
  "settings": {
    "is_hidden": false
  }
}
```

Builds an ASISConnection instance using the parameters that have been set.

Returns

- A new ASISConnection instance.

Example:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public class UseServiceActivity extends Activity\n     implements ASISConnection.ASISConnectionCallBacks,\n   ASISConnection.EngineMessagesListener\n....\nASISConnection mServiceConnection ;\n...\n\nmServiceConnection = new ASISConnection.ConnectionBuilder(this)\t\t\t\t\t.withServicePackageName(&quot;com.epicgames.UE_PROJECT&quot;)\n\t\t.withObbModuleName(&quot;UE_PROJECT&quot;)\n\t\t.withConnectionListener(this)\n",
  "lines_of_code": 14,
  "id": 44629,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYyOSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--de720228ee72a12db54ff58a10342dd6854d9e74e8980ac9599ee9653ce67472",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "ASISConnection(ConnectionBuilder builder)",
  "lines_of_code": 1,
  "id": 44630,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYzMCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--92c86514a32e6b0b1bd14fe1b3896ccb1771e7847faa9719fb2691d81c442d02",
  "settings": {
    "is_hidden": false
  }
}
```

Constructor that takes a `ConnectionBuilder` as an argument.ConnectionBuilder

This constructor is typically used through the `ConnectionBuilder`'s `build()` method.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public boolean bindToUnrealInstanceService()",
  "lines_of_code": 1,
  "id": 44631,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYzMSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--27afc0fed34bc616a7e7287bb00c464b7038d535e814fdd4e9dcde1d8acaaa43",
  "settings": {
    "is_hidden": false
  }
}
```

Binds  to an unreal android single instance service by the given caller.

Returns

- `true` if binding was successful, false otherwise.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public void unbindToUnrealInstanceService()",
  "lines_of_code": 1,
  "id": 44632,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYzMiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--b96a2f8494e72dbef44590ab038328ab262f4c1e8685d82d9f1b5bb7497bcdae",
  "settings": {
    "is_hidden": false
  }
}
```

Unbinds from the Unreal instance service.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public boolean isBoundToService()",
  "lines_of_code": 1,
  "id": 44633,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYzMywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--afa6bb3d4d92515b0232a77884b73eb7a6bf071c79054153f90d2baa239bfae2",
  "settings": {
    "is_hidden": false
  }
}
```

Checks whether the application is currently bound to the service.

Returns

- This method returns true if the application is bound to the service.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public int attachSurfaceToService(int displayIndex, Surface externalSurface)",
  "lines_of_code": 1,
  "id": 44634,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYzNCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--82bbd80144ff43b746e18e1b0881ea4c00e9b8e939867f11ce3a357b51b79438",
  "settings": {
    "is_hidden": false
  }
}
```

Attach an external surface to the service for rendering.

Parameters:

- displayIndex: the index of the display, 0 for single display.
- externalSurface: the Surface to attach.

Returns:

- the ID of the attached Surface.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public boolean detachSurfaceFromService(int attachId, Handler.Callback callback)",
  "lines_of_code": 1,
  "id": 44635,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYzNSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--cc45c20ece9144c80691c30f07299772e0ee898fb64447fb8acb3388ec4d55b1",
  "settings": {
    "is_hidden": false
  }
}
```

Detaches a Surface from the service by attaching ID.

Parameters:

- attachId: the ID of the attachment to detach the Surface.
- callback: a callback that will be called when detachment is complete.

Returns

- true if detachment was initiated successfully, false otherwise.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public boolean sendData(String key, Object value)",
  "lines_of_code": 1,
  "id": 44636,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYzNiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--94ef6df714df48c195c5af74ed4540c58408116acd24c3cb6fd6598cdb140b6d",
  "settings": {
    "is_hidden": false
  }
}
```

This method allows you to send key-value data to the ASIS Service.

Parameters

- key: A String that represents the key for the data being sent.
- value: The piece of data to be sent.

Returns

- This method returns a boolean that indicates whether the data was sent successfully.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public boolean consoleCommand(String consoleCommand)",
  "lines_of_code": 1,
  "id": 44637,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYzNywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--8faa197f693eac231e0db24b39ebdc77cdae6d6986077cceea27d43441b84dc7",
  "settings": {
    "is_hidden": false
  }
}
```

Sends a console command to the connected service.

Parameters

- consoleCommand: A String with a console command.

Returns

- Returns true if the message was sent successfully.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "public boolean sendTouchEvent(MotionEvent event, int attachId)",
  "lines_of_code": 1,
  "id": 44638,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYzOCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--bd5540cdcb105b363b9058c09169a8f19d560e62a331fceb632a158a2557bb30",
  "settings": {
    "is_hidden": false
  }
}
```

Forward touch event to the service from attached surfaces.

Parameters

- event: Android MotionEvent representing the touch event.
- attachId the ID associated with the surface.

Returns

- Returns true if the touch event was sent successfully, false otherwise.

### Android application integration

Import ASIS java libraries to your project.

- Copy generated libraries from {Project\_Name}\Binaries\Android\aars to your app space (e.g libs)

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "{Android_app}/libs\n├── asisclientlib-1.0.1-debug.aar\n├── asisclientlib-1.0.1-debug.jar\n├── asiscommon-1.0.1-debug.aar\n└── asiscommon-1.0.1-debug.jar\n",
  "lines_of_code": 5,
  "id": 44639,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDYzOSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--cd22cbd3a68f197634a4c2b81d1e4e5c8b9d60c0860d2ba088f86a38c8532131",
  "settings": {
    "is_hidden": false
  }
}
```

- Add import to the lig via build.gradle

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "java",
  "title": "",
  "code_preview": "android {\n \t...\n\trepositories {\n\t\tflatDir { dirs &#39;libs&#39; }\n\t}\n...\n}\n\ndef asiscommonVersion = &quot;1.0.1&quot;\ndef asisclientlibVersion = &quot;1.0.1&quot;\n",
  "lines_of_code": 16,
  "id": 44640,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NDY0MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI0OjU4KzAwOjAwIn0=--8c7b95da5fb13c6edbf79c6ab9269a257dbf59d17180461376b9cef6387a1f3e",
  "settings": {
    "is_hidden": false
  }
}
```

The application activity lifecycle sequence diagram:

![Image](https://dev.epicgames.com/community/api/documentation/image/4282295d-465c-4a4b-a1b8-9cd49bf866ad)
