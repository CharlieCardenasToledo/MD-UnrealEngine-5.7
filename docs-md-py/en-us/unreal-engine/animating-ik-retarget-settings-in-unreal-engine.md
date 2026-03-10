# Using Retarget Profiles

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animating-ik-retarget-settings-in-unreal-engine

> Application Version: 5.7

In addition to **IK Retargeting** your characters during runtime, you can modify **Global**, **Root**, and **Chain** settings dynamically using **Retarget Profiles**. Retarget Profiles are an additional feature of the **Retarget Pose From Mesh** Animation Blueprint Node which you can use to change or animate these settings. This can be useful in cases where you need to change or apply different retarget settings at different points throughout an animation.

This document provides instructions on how to set up Retarget Profiles and various ways to modify them.

#### Prerequisites

* You have set up characters to dynamically retarget at runtime using **Retarget Pose From Mesh**. Refer to the [Runtime IK Retargeting](https://dev.epicgames.com/documentation/en-us/unreal-engine/runtime-ik-retargeting-in-unreal-engine) page for instructions on how to do this.
* You are familiar with using [Animation Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine).
* You are familiar with creating and using [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine).

## Accessing Retarget Profiles

You can access Retarget Profiles from the **Retarget Pose From Mesh** node in the target character's Animation Blueprint you created in the [Runtime IK Retargeting](https://dev.epicgames.com/documentation/en-us/unreal-engine/runtime-ik-retargeting-in-unreal-engine) prerequisite step. Select **Retarget Pose From Mesh** and locate the **Custom Retarget Profile** properties in the **Details** panel.

![retarget profile details](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aa1f3c8a-1f11-4c3c-a0a2-ce50f0201ca9/access1.png)

## Static Override

By default, the settings you set up in the assigned IK Retargeter Asset are used by the **Retarget Pose From Mesh** node. You can statically override those settings by modifying the **Custom Retarget Profile** properties on the node:

| Name | Description |
| --- | --- |
| **Apply Target Retarget Pose** | Enabling this overrides the [Retarget Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine#retargetpose) used for the target character. |
| **Target Retarget Pose Name** | If **Apply Target Retarget Pose** is enabled, this setting specifies the new Retarget Pose name to use instead. |
| **Apply Source Retarget Pose** | Enabling this overrides the [Retarget Pose](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine#retargetpose) used for the source character. |
| **Source Retarget Pose Name** | If **Apply Source Retarget Pose** is enabled, this setting specifies the new Retarget Pose name to use instead. |
| **Apply Chain Settings** | Enabling this overrides the [Chain Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine#chainsettings) used in the IK Retargeter Asset with new ones specified below in **Chain Settings**. |
| **Chain Settings** | An array to add chains to override with new Chain Settings. Click **Add (+)** to add a new chain and set the name to match one of the retarget chains in the IK Retargeter Asset. Expand **FK**, **IK** or **Speed Planting** categories to modify the settings within. |
| **Apply Root Settings** | Enabling this overrides the [Root Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine#rootsettings) used in the IK Retargeter Asset with new ones specified below in **Root Settings**. |
| **Root Settings** | If **Apply Root Settings** is enabled, these settings override the Root Settings used in the IK Retargeter Asset. |
| **Apply Global Settings** | Enabling this overrides the [Global Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine#globalsettings) used in the IK Retargeter Asset with new ones specified below in **Global Settings**. |
| **Global Settings** | If **Apply Global Settings** is enabled, these settings override the Global Settings used in the IK Retargeter Asset. |

## Dynamic Override

If you need to control when retarget settings change, then you must create additional blueprint logic. Due to the arbitrary nature of Blueprints and Animation situations, there are many ways you can create logic to edit a variety of retarget situations.

In this example, Retarget Profiles will be used to adjust the larger character's arm to correctly reach for the ground, matching the Mannequin.

![target character incorrect](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/334cd9e9-a97d-44b6-8896-b63206b67ee9/animate0.gif)
