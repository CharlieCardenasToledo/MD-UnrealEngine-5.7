# How To Use the Mixed Reality Capture Calibration Tool

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-use-the-mixed-reality-capture-calibration-tool-in-unreal-engine

> Application Version: 5.7

The goal of calibration is to have the virtual and physical cameras match up in the virtual world.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d240474c-660f-41f8-a588-c7f6b24ebff2/adjustingalignmentstep.png "AdjustingAlignmentStep.png")
At runtime, the game needs to know a few things, like:

* The type of camera and lens that you're using.
* Where your camera is in relation to your virtual scene.

And to composite your scene, the game needs to know things like:

* The color of your chroma backdrop (usually green).
* How aggressively to cut out the chroma color.
* Areas you want fully cut out from the camera frame.

The game needs to know these things so the virtual camera can emulate the physical one. This is where the calibration tool comes into play. The calibration tool lets you configure all of these settings at once, and produces a calibration settings file with that information. The settings file can then be reused across different games.

## Pre-Calibration Setup

Before you can start a Mixed Reality capture, you will need the right equipment. Here is quick overview of the equipment you will need, and some tips on how set it up. This include the basic green screen and camera setup for the capture process, as well as the equipment and software needed for calibration.

#### Green Screen and Camera

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0522ca96-6951-47ac-abd1-1312da194c69/mr_greenscreensetup.png "MR_GreenScreenSetup.png")

1. **Video Camera**
   UE4 only supports a very specific set of video capture devices; see [Supported Video Devices](https://dev.epicgames.com/documentation/en-us/unreal-engine/supported-video-devices-for-mixed-reality-capture-in-unreal-engine) for the current list of the supported devices. Using a device from the list, connect it to your PC for streaming.
2. **Chroma backdrop**
   For chroma keying, we generally use a green screen. When setting up the green screen you will want to make sure it's taut, minimizing any wrinkles, especially behind your subject. If you are setting up lighting, you will want to make sure not to cast shadows directly behind the subject. You want a smooth, flat color. The more shades of green that there are across the backdrop, the harder it is to chroma key. It helps if the subject is far away from the backdrop as possible. If you plan on filming the subject's feet, consider a green screen for the floor as well.
3. **Camera Mount**
   For initial setup (calibration), your camera needs to be static. If you are using a webcam this may be as simple as attaching it to your desk/monitor. Another option is mount the camera to a tripod.
4. **Multi-Mount + Tracker (Optional)**
   If you plan on moving the camera around while filming, you will want attach a tracking device to the camera, such as an HTC Vive Tracker. In addition, connect the camera and tracker together with a [multi mount](https://www.bhphotovideo.com/c/product/1062513-REG/desmond_d3d_1_stereo_camera_bracket.html), so that they stay firmly locked in place.

#### Calibration Specific Equipment

There are a few additional items required specifically for the calibration process (as opposed to the capture process).

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8b20a460-9419-4877-af1f-642b517c795c/mr_requiredsetupitems.jpg "MR_RequiredSetupItems.jpg")

* **HTC Vive or Oculus Rift**
  The calibration tool requires one of these two VR systems to work. The tool uses the controllers' tracking to evaluate the location of the camera. If this is the first time you've set up an HTC Vive or Oculus system, you will need to complete their setup process first for calibration to work properly.
* **Printed Checkerboard Pattern**
  Print and attach a printed checkerboard pattern to a flat rigid surface (like a piece of cardboard). You can find an example of this checkerboard pattern included with the calibration tool download.

  When taping down the checkerboard printout, make sure not to cover the checkerboard pattern itself with tape (even clear tape can cause specular reflections that make it hard for the camera to read).

## Steps

Once the equipment is set up, you can download the calibration tool from [here](http://epic.gm/mrccal). Once you've downloaded the file, unzip it and launch MRCalibration.exe.

The calibration process is divided into distinct steps. The individual steps are discussed further below.

1. Device/Camera/Tracker Selection
2. Lens Calibration
3. Alignment Calibration
4. Alignment Adjustment
5. Compositing Calibration
6. Garbage Matting

During calibration, at the end of each step your progress is saved. So you can exit and return to the tool if needed. Once the calibration process is complete, the tool generates a settings file that you will then use to start a MRC session in other projects.

Your calibration progress is recorded in the setting file. If you want to restart the calibration process, you will need to delete the settings file. The settings file is named *MrcCalibration.sav*, and can be found under the tool's */Saved/SaveGames/* directory.

#### Shared Controls

While each step has its own distinct controls, there are some controls that are used consistently through the tool:

* **Enter** : Next/Confirm/Accept/Submit
* **End** : Skip (only applicable when step requirements have been met - some steps can't be skipped)
* **P/Thumbstick** : Preview
* **M** : Mirror the video feed
* **R** : Reset altered settings
* **Esc** : Exit

The tool is rough around the edges, and usability can be improved in places. The tool is functional, but we plan on improving the usability of it in later releases. We welcome your feedback!

## Calibration Process

### 1. Device/Camera/Tracker Selection

If you have multiple video capture devices connected to your PC, you have to specify which one you want to use. Use the **Up/Down** keys to cycle through them.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a152928d-7416-4edf-9fcd-c599d465643d/mr_deviceselection.png "MR_DeviceSelection.png")

Additionally, each camera may have multiple formats and resolutions available to it. We try to auto-select the best format and resolution, but you can use **Left/Right** to change the selection.

The resolution of the camera feed does not affect the output resolution of the Mixed Reality capture. The output resolution of the capture is controlled by the game project you will be capturing from. The resolution of the camera feed only controls how clear the feed is within the scene.

#### Device Selection Controls

* **Up/Down** : Select video capture source
* **Left/Right** : Select video capture format
* **Tab** : Select camera tracker

#### Tracker Selection

If you're planning on moving your camera while filming, you will need to attach it to a tracking device.

Before continuing to the next step, you can use the **Tab** key to cycle through the available tracking attachments. For the HTC Vive, the first tracker will be named "Special\_1" in the attachments list.

After you have made the appropriate selections, press **Enter** and continue to the next step.

### 2. Lens Calibration

Different camera lenses bend and distort the picture in different ways (think of a fisheye lens). You don't want that distortion to be carried over into the captured scene, so use this lens calibration step to figure out how to undistort the image. ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b27c26cb-2ce2-4361-adf3-ad4849f7540f/mr_lenscalibration.png "MR_LensCalibration.png")

During this step, you will need a printout of the checkerboard image that you downloaded along with the calibration tool. In this step, the calibration tool continuously takes screenshots using the checkerboard pattern as a baseline.

Hold the printout at different locations in front of the camera. Use different angles and depths, especially around the edges of your frame, so that the calibration tool gets a wide collection of samples. The text at the top of the screen will change to let you know when the calibration tool has collected enough samples.

If your camera is set to auto-focus, you might find it helpful to disable auto-focus during this step.

#### Reprojection Error

After the calibration tool has collected enough samples, the tool will show you a preview of the undistorted feed. If the feed looks acceptable, press **Enter** to continue. If needed, you can add more samples, or press **R** to reset and start over.

A good way to tell if the undistortion process is working is to find elements in frame that should be straight (wall corners, doorways, etc.). Lens distortion will often warp straight edges (especially towards the edge of the frame).

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b6963566-4b20-4c4b-a20e-fbf45c5908ae/mr_reprojectionerror.png "MR_ReprojectionError.png")

The reported "reprojection error" lets you know how accurate the process thinks it is. The lower the reprojection error value, the better. You're in great shape if the value is under one!

#### Angle of View

Probably the most important use of this step is to approximate the camera's angle-of-view (or FOV, 'field-of-view').

The FOV determines how much of the world the camera can see, and it is important that the FOV of our virtual camera matches this as closely as possible.

If you already know the FOV of your camera (in degrees), you can use the *mrc.FovOverride* console variable to set it.

Most USB camera manufacturers list the diagonal-FOV (DFOV) for their devices. However, we are interested in the horizontal-FOV (in degrees). You can compute the horizontal-FOV from the diagonal-FOV with the below formula, using the height (h) & width (w) of the resolution you selected in the previous step.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e2db52f-0c47-4a68-a658-52be448cfae9/mr_fovformula.png "MR_FOVFormula.png")

There are also ways to calculate the horizontal-FOV for DSLR lenses.

If you do not know your camera's specific FOV offhand, don't worry, this step will approximate it for you.

If you have a camera with an adjustable lens, you will want to be very careful not to adjust the zoom after you've completed calibration. Adjusting the zoom will change the physical camera's field-of-view (FOV), but not the virtual one. The virtual camera will use the FOV that was used during calibration. If you adjust the camera's zoom after calibration, you will need to repeat the calibration process.

### 3. Alignment Calibration

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ada48035-cbc8-445b-9117-bbfa713a6e42/adjustingalignment2.png "AdjustingAlignment2.png")

This step requires you to rerun the Align and Adjust phases until complete.

1. Align the controller with an on-screen model.
2. Adjust the sampled alignment.
3. Repeat.

It is important to cover your headset's sensor, so that we can get accurate tracking data from your controllers.

For the HTC Vive, make sure that the controllers are on before you launch the tool. Otherwise, the calibration tool may not display models to align with (the tool needs to recognize the type of controllers that you are using).

#### Phase 1 - Align w/ Model

On screen, there will be a pink/fuschia model to align your controller with. Hold the controller up to the screen and pull the trigger when the controller and the model are lined up.

Once you've pulled the trigger, the screen will freeze frame, and switch into the next phase.

#### Phase 2 - Adjust Sample

Don't expect to be wholly accurate when you first pull the trigger (shaky hands, etc.). In this phase, you adjust the last sample so it is more exactly aligned in the frame.

#### Phase 3 - Repeat

In total, there are 11 points for you to align with. You don't have to go through all of them, if at any point you think the alignment is satisfactory.

![image alt text](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/542d5115-e3e6-4729-86bc-c7d58bbf8d31/adjustingalignment2.gif)

#### Adjustment Controls

* **Up/Down** : Move the model vertically
* **Left/Right** : Move the model horizontally
* **Num +/-** : Zoom the model in/out
* **Alt + Up/Down** : Rotate the model vertically (pitch)
* **Alt + Left/Right** : Rotate the model horizontally (yaw)
* **Alt + Num +/-** : Rotate the model left & right (roll)
* **H** : Hide the model & its outline
* **Alt + H** : Hide the model only (leaving its outline)
* **P** : Preview alignment
* **Enter** : Accept alignment

#### Preview the Result

As you take samples, the screen will show a series of color coded icons (a cross and target). How close each pair is gives you an idea how close the alignment is. You want all pairs to be as close as possible, though don't worry if one is wildly off (it may have been an inaccurate sample).

You can preview how the alignment is coming together by holding **P** (or the thumbstick). If you're happy with the results and wish to skip the rest of the alignment points, press the **End** key.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/42fb086f-915b-4cee-92e4-491060de099e/mr_previewresults.png "MR_PreviewResults.png")
