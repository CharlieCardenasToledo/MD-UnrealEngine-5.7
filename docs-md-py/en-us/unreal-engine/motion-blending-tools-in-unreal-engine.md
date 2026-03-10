# Motion Blending

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-blending-tools-in-unreal-engine

> Application Version: 5.7

When transitioning between character animation clips in the **Sequencer** [Animation Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-animation-track-in-unreal-engine), you can use the **Motion Blending** tools to further increase the blend quality. Using Motion Blending tools, you can dynamically transition an animation clip's motion and world position between clips. This is especially useful when working with animations that contain world displacement data.

Here, a character transitions from a walk animation to a run animation. Without any blending, the transition is a hard cut. Using a simple blend, but without motion blending, the animation still resets the character's position to the animation's origin point, but the character's mesh is transitioned smoothly. By blending the animations with motion blending, the world position is preserved and the animation transitions smoothly.

| Description | Example |
| --- | --- |
| **No Blending** | no blending demo |
| **Motion Blending with No Matching** | motion blending with no matching |
| **Motion Blending with Matching** | motion blending with matching(convert:false) |

Clip Matching references a bone from the character's skeleton and matches that bone's position and motion to the adjacent clip's bone that contains displacement data, such as a root or pelvis bone. By matching the selected bone with the adjacent clip's displacement, it automatically calculates and sets an offset to transition to the next animation while retaining the position of the character. The offset data will then be stored within the animation section in the Sequencer Asset.

## Using Motion Blending

This section contains information about how to blend animations using Motion Blending in Sequencer.

#### Prerequisites

* Your project contains at least two Animation Sequences that contain a bone, such as a root or non-root bone, with world displacement data.

### Motion Blending Set Up

To blend animations using Motion Blending in Sequencer, first add your animations to an animation track in the Sequencer Editor, ensuring they are playing sequentially or overlapping.

![blending clips in sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f8be9e0a-c60c-4e79-80d9-eb14ec8cabe6/addsequences.png)

Navigate your playhead to the beginning of the second animation section to set the time for the animation offset to be calculated. Then, to blend the second animation from the final position of the first animation, right-click the second animation clip, navigate to **Match With This Bone In Previous Clip** and select a bone from the character's skeleton relevant to the animations you are transitioning. In this workflow example, the `l_foot` bone is used to blend the walk and run animations.

![set up motion bleeding demo](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f6125e42-f56a-4937-af6b-34da19ba5d31/setmbdemo.gif)

When played back, your Animation Clips will now blend the animation motion and the world displacement position.

![motion blending demo](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f258715c-0b3b-4d74-abde-409df488d055/motionblendingdemo.gif)

## Motion Blending Properties

Motion Blending has the following properties:

| Property | Description |
| --- | --- |
| **Match With This Bone In Previous Clip** | Select a bone to match the selected animation clip's motion and position with the **previous** clip, at the playhead's location in time.  Using this property results in the animation's motion continuing from the previous clip's position. motion blending demo |
| **Match With This Bone In Next Clip** | Select a bone to match the selected animation clip's motion and position with the **following** clip, at the playhead's location in time.  Using this property results in the animation's motion playing centered around the origin point. match next clip demo |
| **Match X and Y Translation** | When enabled, the selected bone will match **X** and **Y** axes translations. This is useful for ground motion in order to retain the character's movement direction. motion blending x and y translation demo |
| **Match Z Height** | When enabled, the selected bone will match the **Z** axis height of the animation. This is useful for animations that influence a character's height in world space. motion blending height translation demo |
| **Match Yaw Rotation** | When enabled, the selected bone will match the **yaw** (**Z**) rotation. motion blending yaw rotation demo |
| **Match Pitch Rotation** | When enabled, the selected bone will match the **pitch** (**Y**) rotation. motion blending pitch rotation demo |
| **Match Roll Rotation** | When enabled, the selected bone will match the **roll** (**X**) rotation. motion blending roll rotation demo |
| **Show Root Motion Trail** | To view a debug render of the entire animation track's root motion trail, right-click your animation track and enable the **Show Root Motion Trail** property. The root motion trail will be rendered as a black-and-white, striped line that traces every animation clip's root bone translation. show root motion trail property |

### Root Motion Offset Settings

You can manually assign root motion offsets, such as translation and rotation, on each animation clip in your Level Sequence to influence the blending result. Adding root motion offsets only affects the clip, rather than the animation itself, and is applied in addition to any motion blending on a clip. Location and Rotation offsets also respect the start time of the animation clip and can be added to trimmed clips without issue.

To set a root motion offset for an animation clip, right-click the clip in the Sequencer Editor and navigate to **Properties** > **Root Motions**.

![root motion offset properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/336b2587-8130-497b-8e3d-b5804b076634/rootmotionoffset.png)
