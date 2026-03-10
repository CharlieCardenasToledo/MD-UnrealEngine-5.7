# Force Feedback

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/force-feedback-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "include",
  "excerpt_id": 2695,
  "excerpt_assignment_id": 2591,
  "blocks": [
    {
      "type": "paragraph",
      "content": "<b>Force Feedback</b> is the vibration of a device often used in games to convey a force occurring in the game to the player. This feature is known as \"rumble\" or controller vibration for gamepads or controllers. For example, you can use force feedback to simulate the shockwave when an explosion occurs in the game. This gives an additional dimension to a player's immersion.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "Pe4m",
  "settings": {
    "is_hidden": false
  }
}
```

Force Feedback is supported by many common platforms such iOS, Android, and input controllers for consoles.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Support for certain feedback features are platform dependent. See your platform development documentation for full details.",
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

## Anatomy of a Force Feedback Effect

A **Force Feedback Effect** asset contains properties used to define a specific force feedback effect. This enables designers to customize the force feedback to many different situations.

![Force Feedback Details](https://dev.epicgames.com/community/api/documentation/image/b7bf8071-cce0-4b10-856f-f20f36ed251d)

### Channel Details

Force Feedback effects can have multiple channels. Each **channel** can play a different effect. For example, one channel could play a large, long vibration on the right side of the controller, while a second channel could play small, short bursts on the left side.

Each channel has the following properties that control how the channel effect is played:

| Channel Name | Description |
| --- | --- |
| **Affects Left Large** | If true, the left large motor will be used to play the effect. |
| **Affects Left Small** | If true, the left small motor will be used to play the effect. |
| **Affects Right Large** | If true, the right large motor will be used to play the effect. |
| **Affects Right Small** | If true, the right small motor will be used to play the effect. |
| **Curve** | Controls the intensity of the effect over time. This defines the pattern of the vibration. Values above 0.0 cause vibration, while values below 0.0 do not cause vibration. |

#### Force Feedback Curve

The pattern of the effect for each channel is controlled by a Curve. You can add a key to the curve from the Internal Curve Editor by

- Using right-click and selecting add key.
- Open the internal curve editor by double-clicking on the curve's graph.

![Internal Curve Editor](https://dev.epicgames.com/community/api/documentation/image/f7d3c1b7-05a2-490c-829b-2b943777d4b6)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For information on Curves, Keys, creating external Curve Assets, and using the Curve Editor, see the <a data-document-id=\"3231544\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine\">Curve Editor</a> and <a href=\"programming-and-scripting/blueprints-visual-scripting/UserGuide/Timelines/KeysAndCurves/\"></a> pages.",
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

### Per Device Overrides

When working with Force Feedback Assets in Unreal Engine, each platform has a different implementation of how its vibration motors or feedback systems function. Force Feedback assets use **Per Device Overrides** to support multiple platforms.

Per device overrides are an abstraction layer that provides you with a method to set different feedback settings for each platform. For example, you can apply a strong vibration to an Xbox controller, but a more detailed and nuanced vibration to a PlayStation controller.

To modify these settings, click your Force Feedback Effect, then navigate to **Details** > **Per Device Overrides**.

![Per Device Overrides](https://dev.epicgames.com/community/api/documentation/image/5359ec71-c2f5-4287-9b21-6703f5b2d63e)

### Device Properties

**Device Properties** represent the different physical properties of an input device, such as its light color display or haptic trigger resistance.

| Device Property Type | Description |
| --- | --- |
| **Audio Based Vibration** | Play a sound to an input device's speaker. On platforms that support it, this sound is played in the form of a vibration where the left and right audio channels represent the left and right side of the controller. |
| **Device Color (Curve)** | Change the color of an input device's light over time with a curve. |
| **Device Color (Static)** | Set the color of an Input Device to a static color. This will NOT reset the device color when the property is done evaluating. You can think of this as a one shot effect, that once enabled the device property color is set. |
| **Trigger Feedback** | Set simple Trigger Feedback. |
| **Trigger Resistance** | Provide linear resistance to a trigger while it is pressed between a start and an end value. |
| **Trigger Vibration** | Set Trigger Vibration. |

See [Device Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/device-properties-in-unreal-engine) for additional documentation.

### Duration

The duration of the force feedback effect is calculated automatically based on the position of the last key in the curves for all channels. For example, if there are 3 channels and the last key in each set to a value of `1.25`, `1.5`, and `1.75`, then the duration for the overall effect is `1.75`

## Create a Force Feedback Effect Asset

Force Feedback Effect assets are created using the **Content Browser**:

1. In the **Content Browser**, click **Add** and choose **Input > Force Feedback Effect**. Open the asset you have just created. ![Image](https://dev.epicgames.com/community/api/documentation/image/76db1fc6-0a2b-45e4-b198-b7a010cb4271)
2. By default, the asset has one channel but you can add more. For each channel, select the combination of the four outputs that you want the channel to affect. ![Image](https://dev.epicgames.com/community/api/documentation/image/f034246b-2659-4801-ad89-8635f02dd48a)
3. Hold **Shift** and click the **Left Mouse Button** on the curve to add one or more keys. ![Image](https://dev.epicgames.com/community/api/documentation/image/2a8123bd-24fa-41ac-8b55-b4bead36f02d)
4. Manipulate the keys by entering values directly or dragging them in the curve editor.

## Playing Force Feedback

### Preview in Editor

You can preview your Force Feedback Effect in the editor by clicking the "play" button that appears in the middle of the Force Feedback Effect's icon when you mouse over it.

![Image](https://dev.epicgames.com/community/api/documentation/image/84a2830c-e23c-40d5-9190-26af982ce0f3)

### Directly to a Player

Force Feedback is implemented in the base `PlayerController` class. You will need access to the local Player Controller in order to play Force Feedback on the target device or controller.

### Playing Force Feedback in Blueprints

1. Get a reference to your Player Controller, either with a **Get Player Controller** node or a saved reference. ![Image](https://dev.epicgames.com/community/api/documentation/image/15654977-76b9-40d6-bb81-dd64b40e9223)
2. Drag off of the output pin of the reference, then type `Play Force Feedback` into the context menu and select **Client Play Force Feedback**. ![Image](https://dev.epicgames.com/community/api/documentation/image/4d2f3532-ef87-47f9-b873-f1f9916c2242)
3. Specify the Force Feedback Effect to use directly on the node or with a connected variable. ![Image](https://dev.epicgames.com/community/api/documentation/image/f9487832-0ec3-436f-9c48-1a3d6b99c0e4)
4. Check **Looping** if you want the effect to loop. ![Image](https://dev.epicgames.com/community/api/documentation/image/38e837ea-c274-4b8a-ba43-2543b968693f)
5. Optionally, set a unique name for the effect in the Tag field. This feature allows you to stop the effect; if an effect with the same name is already playing, it is stopped and the new effect plays instead. ![Image](https://dev.epicgames.com/community/api/documentation/image/52d85c63-40ad-419f-a86c-83708d41f60c)

### Playing Force Feedback in C++

You can call [ClientPlayForceFeedback](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/APlayerController/ClientPlayForceFeedback?application_version=5.5) on the local Player Controller.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "void ClientPlayForceFeedback\n\t(\n\t\tclass UForceFeedbackEffect * ForceFeedbackEffect,\n\t\tFForceFeedbackParameters Params\n\t)",
  "lines_of_code": 5,
  "id": 150771,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA3NzEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMjo0NSswMDowMCJ9--e0008590edf6ee8c401fc88f458447bba0fecf5ec1ce64915e0c30516206a933",
  "settings": {
    "is_hidden": false
  }
}
```

You can then use the Force Feedback Effect, specifying whether or not the effect should loop, and optionally choose a name for the effect. If a name is provided, and another Force Feedback Effect with the same name is played before the original effect ends, the original effect stops immediately and the new effect plays instead.

#### At a World Location

You can place a [Force Feedback Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/Components/UForceFeedbackComponent?application_version=5.5) in the world location of the intended source effect. This plays a Force Feedback Effect that changes intensity based on distance from the player observing it.

A Force Feedback component plays a Force Feedback Effect on command, but also has a physical location in the world. Like sound or light, the intensity of the force experienced by the player changes with the player's distance from the source according to a data-defined attenuation setting.

Force Feedback Components can be attached to any Actor from the source code or Blueprint and added dynamically during gameplay. You can also use the following utility functions:

- `UGameplayStatics::SpawnForceFeedbackAtLocation`: spawn at a given world location
- `UGameplayStatics::SpawnForceFeedbackAttached`: attach to a specific pre-existing component

These functions return the spawned Force Feedback Component, so you can continue to manipulate it. However, if you have no use for the component after it finishes playing the effect, use the Auto Destroy boolean option to remove the component once the effect ends.
