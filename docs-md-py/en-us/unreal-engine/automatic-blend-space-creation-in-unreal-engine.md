# Blend Space Analysis

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/automatic-blend-space-creation-in-unreal-engine

> Application Version: 5.7

Placing samples accurately in the [Blend Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/blend-spaces-in-unreal-engine#blendgraph) can be slow and tedious, especially if you are not sure exactly what characteristics the animations have. **Blend Space Analysis** can be used to calculate a range of relevant properties, and to then automatically place your samples in the Blend Space.

This document provides an overview of the Blend Space Analysis system in Blend Spaces.

#### Prerequisites

* You have an understanding of [Blend Spaces](https://dev.epicgames.com/documentation/en-us/unreal-engine/blend-spaces-in-unreal-engine).
* Your project has a Skeletal Mesh character with the necessary imported animations to use as samples in the Blend Space graph.

Blend Space Analysis cannot be used for Blend Space nodes created in Animation Blueprints.

## Enabling Analysis

Blend Space Analysis can be enabled for all [Blend Space types](https://dev.epicgames.com/documentation/en-us/unreal-engine/blend-spaces-in-unreal-engine#blendspacecreationandtypes) by setting the analysis axis function properties located in the **Asset Details** panel. Setting the **Axis Function** to a value other than **None** will enable Blend Space Analysis, and the value to select depends on the kind of Blend Space you are creating. For example, if you are creating an [Aim Offset](https://dev.epicgames.com/documentation/en-us/unreal-engine/aim-offset-in-unreal-engine), then typically you may want to select **Orientation**.

![blend space analysis](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a94d67cb-75d4-4d03-b1b2-471eed556f49/enableanalysis.png)

The following **Axis Functions** are available for use:

| Axis Function | Description |
| --- | --- |
| **None** | Disables analysis for this axis. |
| **Position** | Calculates the position of a Bone or Socket averaged over the duration of the sample. |
| **Velocity** | Calculates the velocity of a Bone or Socket averaged over the duration of the sample. |
| **Delta Position** | Calculates the change in position of a Bone or Socket over the duration of the sample. |
| **Orientation** | Calculates the orientation (roll, pitch and yaw) of a Bone or Socket averaged over the duration of the sample. |
| **Orientation Rate** | Calculates the rate of change of roll/pitch/yaw of a Bone or Socket averaged over the duration of the sample. |
| **Delta Orientation** | Calculates the change in roll/pitch/yaw of a Bone or Socket over the duration of the sample. |
| **Angular Velocity** | Calculates the angular velocity as a rotation vector (in degrees per second) averaged over the duration of the sample. |
| **Locomotion** | Estimates the locomotion velocity of a biped character based on the foot movements. |
| **Root Motion** | Estimates the locomotion velocity of a character based on the motion of the root (requires root motion data in the animation sequences). |

### Analysis Properties

Selecting any of the Axis Function types will reveal additional properties, which are used to configure the analysis. Most of these properties are common for all types, however there are some that are exclusive to certain types.

![analysis properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8d83d82a-750a-4f8c-b0c9-daac54bf05bf/analysisproperties.png)

| Name | Description |
| --- | --- |
| **Axis** | The axis of the Bone or Socket to analyze. Depending on the chosen Axis Function, there will be a different **Axis** to select:   * **Position**, **Velocity**, **Delta Position**, and **Angular Velocity** provides **X**, **Y**, or **Z** for the analysis axis. * **Orientation**, **Orientation Rate**, and **Delta Orientation** provides **Pitch**, **Roll**, or **Yaw** for the analysis axis. * **Locomotion** and **Root Motion** provides **Speed**, **Direction**, **Forward Speed**, **Rightward Speed**, **Upward Speed**, **Forward Slope**, and **Rightward Slope** for the analysis axis. |
| **Bone/Socket** | This specifies the Bone or Socket to analyze. If **Axis** is set to **Locomotion**, then two Bone/Socket properties are required, one for each foot. Some analysis functions will also use the orientation of the Bone for calculating Pitch, Roll, or Yaw values. In these cases, you need to ensure that the **facing** and **right** axes are set correctly, depending on how the character's skeleton is set up. |
| **Bone Facing Axis** | The forward-facing axis of the selected Bone or Socket if **Orientation**, **OrientationRate**, or **DeltaOrientation** is selected as the Axis Function. |
| **Bone Right Axis** | The right-facing axis of the selected Bone or Socket if **Orientation**, **OrientationRate**, or **DeltaOrientation** is selected as the Axis Function. |
| **Space** | The spatial coordinates in which to perform the analysis, so you can calculate the position and orientation of one Bone with respect to another. You can select the following spatial coordinates:   * **World** space represents the space the character is in at the start of each animation sequence, and can be determined from the viewport axis display. * **Fixed** space uses the space of a particular bone or socket, without updating it during the animation sequence. Using it, you can specify your own "world space" coordinate frame using the Bone or Socket from the first frame of the animation sequence. * **Changing**, which is similar to **Fixed**, but the space is updated for each frame that is analyzed in the animation sequence. * **Moving** space, which is similar to **Changing**, except that the velocities are also calculated relative to the Bone space. |
| **Analysis Space Bone/Socket** | If Space is set to either **Fixed**, **Changing**, or **Moving**, then this is where you specify the Bone or Socket to use for the spatial analysis. |
| **Character Facing Axis** | The facing direction of your character, which can be determined from the viewport axis display. Typically this should be set to **+Y**. character facing axis |
| **Character Up Axis** | The upward direction of your character, which can be discerned from the viewport axis display. Typically this should be set to **+Z**. |
| **Start Time Fraction** | The normalized start time of the animation sample to analyze. You may want to adjust this if you only want a certain section of an animation to be analyzed. |
| **End Time Fraction** | The normalized end time of the animation sample to analyze. You may want to adjust this if you only want a certain section of an animation to be analyzed. |

## Analysis Examples

The following are some examples of how you can use Blend Space Analysis to populate your Blend Space graph.

### Aim Offset

If you want to automatically place your [Aim Offset](https://dev.epicgames.com/documentation/en-us/unreal-engine/aim-offset-in-unreal-engine) samples, you can use Blend Space Analysis in the following way. This example will assume you have already created an Aim Offset Asset.

In the Aim Offset Asset Details panel, locate both the **Horizontal Axis Function** and **Vertical Axis Function** properties and set them to **Orientation**.

![aim offset analysis orientation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fc93321e-3feb-4677-b047-8a1dc1856fbe/aimoffset1.png)
