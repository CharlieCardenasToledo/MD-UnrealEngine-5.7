# ML Deformer Sample

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ml-deformer-sample-in-unreal-engine

> Application Version: 5.7

The Machine Learning (ML) Deformer Sample demonstrates how you can use Unreal Engine's Machine Learning (ML) technology to create a high-fidelity real-time game character, with realistic deformations driven by learned offline muscle, flesh and cloth simulations. The sample uses the [ML Deformer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-use-the-machine-learning-deformer-in-unreal-engine) plugin.

This main Level in the sample is an interactive demo sequence. It shows muscles bulging and sliding under the skin and folds forming on clothing. You can also compare the results with ML Deformer on and off, and animate the model with the included ControlRig Asset.

## Downloading the Sample

To create a project with the ML Deformer sample, follow these steps:

1. Access the [ML Deformer sample](https://fab.com/s/fb59a5b662f2) from **Fab** and click **Add to My Library** for the project file to show in the **Epic Games Launcher**. Alternatively, you can search for the sample project using Fab in Launcher, or the Fab plugin for UE.
2. From the **Epic Games Launcher**, go to **Unreal Engine > Library > Fab Library** to access the project.
3. Click **Create Project** and follow the on-screen instructions to download the sample and start a new project.

To learn more about accessing sample content from Fab, see [Samples and Tutorials](https://dev.epicgames.com/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine).

## Navigating the Scene

While the scene is playing in-Editor, you can use keyboard or PlayStation gamepad controls to navigate the scene. These controls are configured in the `KeyboardGamepadMapping` file, located in the `Content/Input/` folder, and you can customize them.

### ML Deformation Toggle and Layers

While the scene is playing, press and hold the **M** key, or **left D-pad** button on your gamepad, to temporarily disable ML deformation.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26055928,
  "caption_left": "ML Deformer off",
  "image_right_id": 26055929,
  "caption_right": "ML Deformer on",
  "image_left": {
    "id": 26055928,
    "file_name": "cloth-ml-deformer-off.png",
    "file_size": 1607662,
    "content_type": "image/png",
    "created_at": "2025-09-11T18:30:02.267+00:00",
    "height": 877,
    "width": 1555,
    "storage_key": "fcd160c6-242d-4bb5-9747-f43b81d92363",
    "context": "documentation"
  },
  "image_right": {
    "id": 26055929,
    "file_name": "cloth-ml-deformer-on.png",
    "file_size": 1642798,
    "content_type": "image/png",
    "created_at": "2025-09-11T18:30:02.506+00:00",
    "height": 874,
    "width": 1557,
    "storage_key": "7c32fc5d-315d-4da6-9194-d344fc8d25d4",
    "context": "documentation"
  },
  "image_left_storage_key": "fcd160c6-242d-4bb5-9747-f43b81d92363",
  "image_right_storage_key": "7c32fc5d-315d-4da6-9194-d344fc8d25d4",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

Press the **Up** and **Down** arrow keys or use the D-pad **up / down** buttons to switch between the cloth, skin, and muscle layers.

![Character layers](https://dev.epicgames.com/community/api/documentation/image/5130ddeb-685e-4dc0-8f19-4f3220fcf409)

Toggle between normal Materials and a clay shader with the **N** key or the **right D-pad** button.

```json
{
  "type": "comparison_slider",
  "image_left_id": 26055930,
  "caption_left": "Clay shader on",
  "image_right_id": 26055931,
  "caption_right": "Clay shader off",
  "image_left": {
    "id": 26055930,
    "file_name": "clay-material-on.png",
    "file_size": 1413287,
    "content_type": "image/png",
    "created_at": "2025-09-11T18:30:02.708+00:00",
    "height": 876,
    "width": 1566,
    "storage_key": "74d40979-b5ed-4214-affd-726af70710c7",
    "context": "documentation"
  },
  "image_right": {
    "id": 26055931,
    "file_name": "clay-material-off.png",
    "file_size": 1492474,
    "content_type": "image/png",
    "created_at": "2025-09-11T18:30:02.977+00:00",
    "height": 872,
    "width": 1565,
    "storage_key": "9a36d384-7188-4036-8bbe-646b0c73ba85",
    "context": "documentation"
  },
  "image_left_storage_key": "74d40979-b5ed-4214-affd-726af70710c7",
  "image_right_storage_key": "9a36d384-7188-4036-8bbe-646b0c73ba85",
  "context": "documentation",
  "settings": {
    "is_hidden": false
  }
}
```

### Playback and HUD Controls

While the scene is playing in PIE, you can use the following playback controls:

| Action | Keyboard Shortcut | Gamepad Shortcut |
| --- | --- | --- |
| Pause playback | Spacebar | X button |
| Decrease playback speed | Comma | Square button |
| Increase playback speed | Period | Circle button |

You can also enable two separate Heads-Up Display (HUD) widgets:

| Widget | Keyboard Shortcut | Gamepad Shortcut |
| --- | --- | --- |
| Stats and performance widget | H | L1 button |
| Shortcut helper widget (shows gamepad button shortcuts) | Tab | Special button (right) |

### Camera Controls

Press the **O** key, or **triangle** button on your gamepad, to enable or disable camera controls.

While camera controls are enabled, you can use the following keyboard shortcuts:

| Action | Keyboard Shortcut | Gamepad Shortcut |
| --- | --- | --- |
| Orbit camera left / right | A / D | Left thumbstick (move horizontally) |
| Dolly (zoom) in / out | W / S | Left thumbstick (move vertically) |

## Character and Rig Details

The character used for the shot is a high-fidelity digital human, with a musculoskeletal system and true-to-life face and body materials.

The musculoskeletal system was created by combining MRI scan data, a 3D skeleton scan, and hand-authored muscles. For the face and body materials, 3D face and body scans were used, along with a reference shoot.

The sample contains a Control Rig that you can use to further explore how ML deformation interacts with different character poses. The rig is located in the `Content/Characters/Emil/Rig` folder, and the Asset file is named `CR_Emil`. Unlike a MetaHuman rig, the rig used in this sample is asymmetrical (that is, joint positions are not mirrored perfectly). This achieves the most realistic deformation possible.

## Further Information

The 2023 State of Unreal GDC presentation included an in-depth segment of how the results in this technical demo were achieved. You can learn about the whole process, from scanning the character, to training the ML model, then combining different software and technologies to achieve the final result. Watch the full segment on YouTube at [this link](https://www.youtube.com/watch?v=teTroOAGZjM&t=19000s).

To learn more about the ML Deformer plugin, see the [ML Deformer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-use-the-machine-learning-deformer-in-unreal-engine) page.
