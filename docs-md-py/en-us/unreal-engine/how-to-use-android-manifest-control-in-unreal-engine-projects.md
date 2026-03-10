# Android Manifest Control

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-use-android-manifest-control-in-unreal-engine-projects

> Application Version: 5.7

The `AndroidManifest.xml` file is used to store various Android system permissions and settings that are set in the **Advanced APK Packaging** section of your **Projects Settings**. The following document shows how you can input commands that will be added to the `AndroidManifest.xml` file to meet the needs of your **Unreal Engine** (UE) project.

## Android Manifest Location

Before you can locate the `AndroidManifest.xml` file for your project, you will first need to either package the project or deploy the project to your Android device. Once the project has been built or deployed you will then find the `AndroidManifest.xml` file in `(YourProjectName)\\Intermediate\Android\arm64`.

Click for full image.

You should **never** edit the `AndroidManifest.xml` file under any circumstances. Any edits that need to be made to the `AndroidManifest.xml` file should be done inside the UE Editor in the Advanced APK Packing section.

## Android Manifest Layout

In a typical `AndroidManifest.xml` file you will find the following three sections.

* **Application Definition**
* **Activity**
* **Requirements**

  ```
            <manifest xmlns:android="http://schemas.android.com/apk/res/android"
                package="com.YourCompany.Project"
                android:versionCode="1"
                android:versionName="1.0.">
  		
                <-- Application Definition -->
                <application android:label="@string/app_name" android:icon="@drawable/icon" android:hasCode="true">
                 <activity android:name="com.epicgames.unreal.GameApplication"
                 </activity>
                </application>
  		
                 <-- Requirements -->
                 <uses-sdk android:minSdkVersions="9"/>
                 <uses-feature android android:glEsVersion="0x00020000" android:required="true" />
                 <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
            </manifest>
  		
  ```

Please note that the above Android Manifest file is not a working manifest file and is only shown for reference purposes.

## Extra Tags for Manifest

Navigate to **Extra Tags for <manifest> node** in the **Advanced APK Packaging** section. You can add additional tags for the Manifest by clicking on the **Plus** sign icon to add a new element to the tags array and then inputting the tag or tags you want to use into the input box. For this example the following tag was used, **android:sharedUserId="Foo"**.

Click for full image.

Tags that are input into the **Extra Tags for <manifest> node** section will be added to the **manifest** section of the `AndroidManifest.xml` file.

```
	<manifest xmlns:android="http://schemas.android.com/apk/res/android"
		package="com.YourCompany.Project"
		android:sharedUserId="Foo"
		android:versionCode="1"
		android:versionName="1.0">
```

## Extra Tags for Application

Navigate to **Extra Tags for &#60application> node** in the **Advanced APK Packaging** section. You can add additional tags for the Application by clicking on the **Plus** sign icon to add a new element to the Application array and then inputting the tag you want to use. For this example the following tag was used, **android:hardwareAccelerated="True"**.

Click for full image.

Items that are input into the **Extra Tags for &#60application> node</strong> section will be added to the <strong>Application Definition</strong> section of the <code>AndroidManifest.xml</code> file.</p>
<pre><code>
&lt;application android:label="@string/app\_name"
android:icon="@drawable/icon"
android:hardwareAccelerated="True"
android:hasCode="true"&gt;
</code></pre>
<h2>Extra Settings for Application</h2>
<p>Navigate to <strong>Extra Settings for &#60application> section (\n to separate lines)</strong> in the <strong>Advanced APK Packaging</strong> section. You can add additional settings for the Application to use by inputting the settings you want to use into the <strong>Extra Settings for <application></strong> section. If you have more than one setting you want to use, separate each setting by adding <strong>\n</strong>. For this example the the following two items were added, <strong>android:banner="Foo"</strong> and <strong>android:vmSafeMode="True"</strong>.</p>
<block-lightbox alt="" loading="lazy" src="https://d1iv7db44yhgxn.cloudfront.net/documentation/images/87bf596b-d305-4110-a722-d075873826c8/ue5\_1-04-extra-app-settings.png" width="500"></block-lightbox>
<p class="figure-caption is-separated">Click for full image.</p>
<p>Items that are input into the <strong>Extra Settings for &#60application></strong> section will be added to the <strong>Activity</strong> section of the <code>AndroidManifest.xml</code> file.</p>
<pre><code> &lt;/activity&gt;
&lt;activity android:name=".DownloaderActivity" android:screenOrientation="sensorLandscape" android:configChanges="mcc|mnc|uiMode|density|screenSize|orientation|keyboardHidden|keyboard" android:theme="@style/UnrealSplashTheme" /&gt;
&lt;meta-data android:name="com.epicgames.unreal.GameActivity.DepthBufferPreference" android:value="0" /&gt;
&lt;meta-data android:name="com.epicgames.unreal.GameActivity.bPackageDataInsideApk" android:value="false" /&gt;
&lt;meta-data android:name="com.epicgames.unreal.GameActivity.bVerifyOBBOnStartUp" android:value="false" /&gt;
&lt;meta-data android:name="com.epicgames.unreal.GameActivity.bShouldHideUI" android:value="true" /&gt;
&lt;meta-data android:name="com.epicgames.unreal.GameActivity.ProjectName" android:value="AndroidProject" /&gt;
&lt;meta-data android:name="com.epicgames.unreal.GameActivity.bHasOBBFiles" android:value="true" /&gt;
&lt;meta-data android:name="com.epicgames.unreal.GameActivity.bSupportsVulkan" android:value="true" /&gt;
&lt;meta-data android:name="com.google.android.gms.games.APP\_ID" android:value="@string/app\_id" /&gt;
&lt;meta-data android:name="com.google.android.gms.version" android:value="@integer/google\_play\_services\_version" /&gt;
&lt;activity android:name="com.google.android.gms.ads.AdActivity" android:configChanges="keyboard|keyboardHidden|orientation|screenLayout|uiMode|screenSize|smallestScreenSize" /&gt;
android:banner="Foo"
android:vmSafeMode="True"
&lt;service android:name="OBBDownloaderService" /&gt;&lt;receiver android:name="AlarmReceiver" /&gt;&lt;/application&gt;
</code></pre>
<h2>Extra Tags for com.epicgames.unreal Game Activity</h2>
<p>You can add additional tags for the <strong>Extra Tags for com.epicgames.unreal.GameActivity activity node</strong> by clicking on the <strong>Plus</strong> sign icon to add a new element to the <strong>Extra Tags for com.epicgames.unreal.GameActivity <activity> node</strong> array and then inputting the tag you want to use.</p>
<block-lightbox alt="" loading="lazy" src="https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7a21a0a4-aa56-48ca-b4f6-92cb4e236cab/ue5\_1-05-extra-ue-tags.png" width="500"></block-lightbox>
<p class="figure-caption is-separated">Click for full image.</p>**
