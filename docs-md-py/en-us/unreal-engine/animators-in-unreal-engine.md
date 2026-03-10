# Animators

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animators-in-unreal-engine

> Application Version: 5.7

**Animators** provide a variety of ways to do loopable, sequencer-controllable, and one-off animations, defined by parameters rather than keyframes.

For example, animating something like a bouncing ball using standard [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine) techniques requires creating multiple keyframes and manipulating animation curves. Using animators, you can select from a list of templated presets with customizable parameters to achieve the same effect.

You can access the animators from the [Operator Stack](https://dev.epicgames.com/documentation/en-us/unreal-engine/operator-stack-in-unreal-engine) window, along with the [modifiers](https://dev.epicgames.com/documentation/en-us/unreal-engine/modifiers-in-unreal-engine).

## Adding Animators

There are two methods for adding animators. First, you can add animators by clicking **+Add Animators** in the Operator Stack window, which displays the full menu of animators you can use.

![Animators in the Operator Stack window](https://dev.epicgames.com/community/api/documentation/image/e9dc6457-7bc9-4f15-aa16-0aa762c3877b)

You can click any of these animators to add it to your currently-selected actor in the **Motion Design Outliner**. If you already know the name of the animator you want to use, you can search for it by name in the search bar near the top.

Second, you can also add an animator by right-clicking an actor in the **Motion Design Outliner** panel, selecting **Add Animators** in the context menu, then picking the property to affect. Once added, the new animator appears in the Operator Stack panel in exactly the same way as when you add an animator there directly.

Here is an example of adding an Oscillate animator to the Scale property of a sphere actor.

![Adding an Oscillate animator.](https://dev.epicgames.com/community/api/documentation/image/cca93ec2-8b47-4b17-96a2-db68659d790a)

Before:

![Before adding an animator](https://dev.epicgames.com/community/api/documentation/image/08e6e103-bbc0-4601-a3df-b73cbaf2da39)

After:

![After adding an animator](https://dev.epicgames.com/community/api/documentation/image/40a35761-11ee-4520-93d7-9a3ef83ff1e0)

## Global Properties

The basic operation of any animator is defined by two global settings: **Global Magnitude** and **Global Time Source Name**.

### Global Magnitude

This property determines how much movement the animations you create show when applied to actors in your level. The value is a float with a range from 0.0 and 1.0. If you have several animators, this global setting affects all of them. The higher the value, the more all your animations move the actors you apply them to.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Global magnitude stacks multiplicatively with the magnitude properties of animators and with the magnitude of the linked properties of those animators.",
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

### Global Time Source Name

This property is how you manage the time source that drives the animators. Several options are available in the dropdown menu, some of which enable additional properties.

The dropdown menu options are:

- **World**
- **Manual**
- **Sequencer**
- **System**

#### World

The **World** option starts the animator the moment the level loads. For example, if you have a pulsing sphere (as in the examples below), it begins to pulse immediately.

#### Manual

The **Manual** option provides you access to methods to directly control the animation timing using several properties.

![Global Time Source Name Manual option](https://dev.epicgames.com/community/api/documentation/image/c5d8d004-a913-4398-9102-322fcc328096)

##### Custom Time

The **Custom Time** property provides a way for you to drive the overall animation from Sequencer or Remote Control by keyframing your selected time value using the keyframe icon.

![Manual option Custom Time property](https://dev.epicgames.com/community/api/documentation/image/2a14379f-6038-4a37-9e57-7ece2a7fbbad)

##### Playback State

Alongside Custom Time, you gain access to the **Playback State** property. This provides you a full playhead, which you can manipulate directly or by exposing it to **Remote Control**.

![Manual option Playback State property](https://dev.epicgames.com/community/api/documentation/image/3766cfc5-8a52-4f22-b2a2-1b4bca0e7787)

![Playback State mapped to Remote Control](https://dev.epicgames.com/community/api/documentation/image/6fc26951-41fa-4df9-a06e-1af78a39fb79)

#### Sequencer

You can control the animation from Sequencer by clicking **Create Track**.

![Sequencer option and Create track button](https://dev.epicgames.com/community/api/documentation/image/25f089fe-851e-4d33-8950-595862c55e23)

When you click Create Track, a sequencer track is created, and you can now drive the animator.

![Sequencer track driving animator](https://dev.epicgames.com/community/api/documentation/image/a3a05cd3-9294-4805-b779-a03ce262f932)

#### System

The **System** option works primarily with the text animators (the Clock animator mainly but not exclusively), and offers little additional functionality for the numeric animators. You have a few options for using it, depending on your selection in the **Mode** property dropdown menu.

##### Local Time

The **Local Time** mode option shows the time according to your current device's time zone.

![System Local Time mode](https://dev.epicgames.com/community/api/documentation/image/78693215-3c23-4b8c-b694-71e1496bccdd)

##### Countdown

The **Countdown** mode option includes subproperties where you can set the countdown format (target or duration) and time.

![System Countdown mode option](https://dev.epicgames.com/community/api/documentation/image/593a9865-33f1-4bc2-9a42-88610e04b3d7)

###### Countdown Format

The **Countdown Format** subproperty provides you with two options for how to track the countdown: **Duration** and **Target**.

- **Duration**: The countdown time is tracked in absolute terms. For example, if the current time is 10:00:00, and the countdown time is 12:00:00, then your countdown will run for 12 hours, and end at 22:00:00. This is the default option.
- **Target**: The countdown time is tracked relative to the current time. For example, if the current time is 10:00:00, and the countdown time is 12:00:00, then your countdown will run for 2 hours, and end at 12:00:00.

###### Countdown Time

The **Countdown Time** subproperty is how you determine the time value used to calculate how long the countdown runs, as described above. The default value is 23:59:59, one second short of a full day.

##### Stopwatch

The **Stopwatch** mode option records how long the animation has been running since you started it.

![System Stopwatch mode option](https://dev.epicgames.com/community/api/documentation/image/2e422f91-1604-4c57-ba69-cbb4e49bcbb3)

#### Use UTC

When using the System option, you can enable the **Use****UTC** property to show the time according to Coordinated Universal Time (UTC).

![Use UTC property](https://dev.epicgames.com/community/api/documentation/image/46112513-6130-4343-8360-7ee5d757968d)

| Global Time Source Mode Options and Properties | Description |
| --- | --- |
| **World** | Animators run continuously while the level is loaded. |
| **Manual** | Direct control of animators. Provides access to the following subproperties:: **Custom Time** **Playback State** **Frame Rate** |
| **Sequencer** | Animators are controlled by Sequencer. |
| **System** | Animators are controlled by system time. Also provides access to the Mode and Use UTC properties. |
| **Mode** | Only available when the Mode property is set to System. Options are: **Local time** **Countdown** **Stopwatch** |
| **Use UTC** | Enable to use Coordinated Universal Time. Only available when the Mode property is set to System. |

### Frame Rate

You can enable the **Frame Rate** global property to control the frame rate of your animations separately from the general frame rate of your project. Adjusting the frame rate can give your animations a smoother or choppier appearance, depending on the frame rate you choose.

![Frame Rate global property](https://dev.epicgames.com/community/api/documentation/image/a1720ef8-2ab6-4d7f-9577-1cf05f57797a)

[Video: V_PFKM2h](https://dev.epicgames.com/community/api/cms/videos/V_PFKM2h/embed.html)

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The functional value of this property is limited by the maximum frame rate of your project and hardware, regardless of the numerical value you enter. You can make it slower than your project's maximum, but not faster.",
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

## Numeric Common Properties

This section describes the shared properties common to Numeric animators, including functionality and basic examples.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "A given Numeric animator does not necessarily use all of the common properties. However, those common properties an animator does use will always function in a similar way. Refer to the description for each specific animator to see which of the common properties it uses.",
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

### Magnitude

The **Magnitude** property determines how much movement your animation shows. The value is a float with a range from 0.0 to 1.0. The higher the value, the more the animation moves the actor to which you apply it. For example, here is a ball bouncing with the magnitude value at 1.0.

![Animator magnitude value at 1.0](https://dev.epicgames.com/community/api/documentation/image/9e9de0aa-5462-48d9-9f54-de4f81965443)

Here is the ball bouncing with a .5 value for magnitude.

![Animator magnitude at 0.5](https://dev.epicgames.com/community/api/documentation/image/9cb5ea7e-6008-4290-ade5-1123471f2382)

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Remember the magnitude setting for a particular animation is different from the global magnitude, and they affect your animation together multiplicatively. For example, setting both the global magnitude and the magnitude of a specific animation to 0.5 results in an animation with a magnitude of 0.25, a quarter of its normal effect.",
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

### Cycle Mode

The **Cycle Mode** property controls the number of times an animator runs its process.

#### Do Once

When you use the **Do Once** option, the animation runs a single time. In the example below, the ball bounces once.

![Animator do once cycle mode](https://dev.epicgames.com/community/api/documentation/image/9581ba43-ee88-4d77-9151-56dae863e5bb)

#### Loop

When you use the **Loop** option, the animation runs as long as it can. In the example shown below, the ball bouncing is limited only by the Sequencer timeline running.

![Animator loop cycle mode](https://dev.epicgames.com/community/api/documentation/image/96d35378-85f7-40ef-9d22-700de54c92d3)

#### Ping Pong

When you use the **Ping Pong** option, the animation runs, and then runs in reverse. In the example, the ball bouncing then "un-bouncing" is limited only by the sequencer timeline running.

![Animator ping pong cycle mode](https://dev.epicgames.com/community/api/documentation/image/7d3f11e8-5a4a-4487-9178-1029c6c88618)

### Cycle Duration

The **Cycle Duration** property is how you control how long a single complete animation loop takes to run. Below are two examples to demonstrate:

1 Second

![Animator 1 sec cycle duration](https://dev.epicgames.com/community/api/documentation/image/1f5415cd-000b-4997-8e99-71fa2015f0e7)

0.5 Seconds

![Image](https://dev.epicgames.com/community/api/documentation/image/f8094418-67fd-4fce-9ee9-47cbef86d2eb)

### Cycle Gap Duration

The **Cycle Gap** **Duration** property provides a way for you to control the duration when using the Loop or Ping Pong cycle modes. It adds a delay between each replay of the animation, whether forward or backward.

### Seed

The **Seed** property adds variation to the overall effect of the animator when the referenced actor has many parts. Using this with **Text** actors is a prime example.

Here is an example of moving Text actors with a seed value of 0:

[Video: V_sUeAa1](https://dev.epicgames.com/community/api/cms/videos/V_sUeAa1/embed.html)

Here is the same example, but with a seed value of 1. The general timing is the same, but the animation offsets different characters to rise and fall in a unique way:

[Video: V_h1TgJP](https://dev.epicgames.com/community/api/cms/videos/V_h1TgJP/embed.html)

This effect is deterministic. Provided all the other values also remain the same, a given seed value always produces the same set of animation offsets.

### Time Source Name

The **Time Source Name** property controls when your animation plays. There are multiple time source options available to determine how your animation plays.

#### World

When you use the **World** option for your time source, your animation plays without further input from the user. For example, if you have an animation like something bouncing around, it bounces around for as long as your level is open.

#### Manual

If you want to use entirely manual controls for your animation, there are two subproperties available when you select the **Manual** option that you can use to control the timing of your animation directly.

![Time Source Name Manual option](https://dev.epicgames.com/community/api/documentation/image/09188a58-9368-4aee-b44b-a504ec6798b5)

##### Custom Time

Using the **Custom Time** subproperty, you can jump to any point in your animation by defining the time in seconds during the animation runtime for your selected point.

##### Playback State

The **Playback State** subproperty gives you access to playback controls you can expose to remote control or set manually.

**Playback State Controls**

- **Play**: Play the animation forward.
- **Rewind**: Rewind the animation backward.
- **Pause**: Pause the animation playback.
- **Stop**: Stop the animation playback, and reset the playhead.

#### Sequencer

Using the **Sequencer** option provides a way to control the animation timing using a Sequencer track. Click the **Create track** button to get started, then use Sequencer to control the time in your animation, including exposing it to remote control as usual.

[Video: V_39V6wM](https://dev.epicgames.com/community/api/cms/videos/V_39V6wM/embed.html)

#### Frame Rate

When you enable the Time Source Name property, you can also choose to enable the **Frame Rate** subproperty. This provides a way for you to set the frame rate of your time source, independently of the frame rate set in the global animation settings or the frame rate of your project.

| Numeric Common Properties | Description |
| --- | --- |
| **Magnitude** | Determines how much movement the animation shows relative to the animation's default. Stacks multiplicatively with the General Magnitude global setting. |
| **Cycle Mode** | Determines how the animation plays. Options are: Do Once Loop Ping Pong |
| **Cycle Duration** | Determines the duration of a single animation playback. |
| **Cycle Gap Duration** | Determines the duration of the gap between animation playbacks for the Loop and Ping Pong cycle modes. |
| **Seed** | Determines variation in the animation playback. |
| **Time Source Name** | Determines how the timing of the animation is tracked. Options are: World Manual Sequencer |
| **Frame Rate** | Determines the frame rate of the animation, separate from the global frame rate and project frame rate. |

## Linked Properties

**Linked Properties** is a feature shared by all animators, which determines how you animate the actor you added the animator to. When you link a property or properties from the actor's **Details** panel, the animator drives those properties. If you don’t have anything linked, you get a warning message, **No properties are currently linked to this animator**, as shown in the image below.

![Animator linked properties error message](https://dev.epicgames.com/community/api/documentation/image/0e84d67f-658b-4722-a7a6-4b4cf657208a)

### Working with Linked Properties

There are two ways to assign properties:

- Click the **+** icon under the **Animators** menu and select a property. In the example, the selected property is RelativeLocation Z, that is, the location of the animated actor on the Z axis. ![Linked properties from the Animators menu](https://dev.epicgames.com/community/api/documentation/image/dd3fcf27-6e7c-48c7-9593-d840c12d1ec9)
- Right-click the actor in your **Motion Design Rundown** and select the property or properties that you want under the **Add Animators** menu. You then need to select the **Animator** again, and select which property or properties that you want to manipulate. This method has an advantage in that you can proceed immediately to linking the property. ![Linked properties from the Motion Design Rundown](https://dev.epicgames.com/community/api/documentation/image/8b6a35e4-8fb7-4305-858e-f654a636fc2d)

Once you are browsing inside the property you linked, consider the following settings:

![Example linked properties](https://dev.epicgames.com/community/api/documentation/image/72d14fd3-1acc-41bb-af35-e3feb154c35c)

By default, you won’t see much of a change. If you're duplicating the example, add a Bounce animator to a shape and link its position on the Z axis, then use the settings below:

- **Amplitude Min**: 0.0
- **Amplitude Max**: 800.0
- **Magnitude**: 1.0
- **Time Offset**: 0.0s
- **Mode**: Absolute

You should produce a result similar to the example below:

![Linked properties animator example](https://dev.epicgames.com/community/api/documentation/image/9675bc18-2a91-454e-8eb8-4addc69e86ec)

### Amplitude Min

You can use the **Amplitude Min** property to control the minimum effect of an animation. In this example, it is a bounce. A zero setting will basically have it land at the zero point and bounce. Giving this property a negative value will cause your actor to sink into the floor, as in the example below:

![Animator amplitude min negative value](https://dev.epicgames.com/community/api/documentation/image/35bba072-4b41-4cf7-abc7-f1bcc655d313)

### Amplitude Max

The **Amplitude Max** property provides you with control of the maximum effect of the animation. In the bounce animation example, this is how high the ball will reach during the bounce.

### Magnitude

The **Magnitude** property provides a way for you to regulate how much your linked property affects your animation. Each linked property can have a different magnitude value, which you can use to make fine changes to your animation.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Remember the magnitude of a linked property is affected by both the global magnitude setting and the magnitude property of the animator, multiplicatively.",
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

### Time Offset

When set for a group of animated actors, the **Time Offset** property sets the total duration required to iterate through the animation for all of those actors. Compare this with the **Cycle Duration** property, which determines the duration required for each element in a group (such as a series of text characters) to animate.

In the examples below, the animation for the bouncy text initially takes 1 second to play, which is set by the Cycle Duration property of the animator. The animation plays at a slower pace after setting the Time Offset property's value to 3 seconds.

Here is the example with the Time Offset property value set to 0.0:

![Animator time offset 0](https://dev.epicgames.com/community/api/documentation/image/810a0c4a-96d6-4b4c-b842-d8ab2cd57b8f)

Here is an example with the Time Offset property value set to 3.0:

[Video: V_JZxgbA](https://dev.epicgames.com/community/api/cms/videos/V_JZxgbA/embed.html)

### Mode

The **Mode** property gives you the choice of two options: **Additive** and **Absolute**.

#### Absolute

The **Absolute** option for an animator means it uses the exact amplitude values you input into the field. In the example below, the animated arc moves in a range from exactly 0 to 90 degrees.

![Animator absolute mode](https://dev.epicgames.com/community/api/documentation/image/96a90a6d-c92c-4277-9d6e-73f8c3b4db67)

#### Additive

The **Additive** option takes the amplitude min and max values, and adds them to the existing value on the exposed field. In this example, the animated arc moves in a range from 180 to 270 degrees, adding on to the half-circle already present.

![Animator additive mode](https://dev.epicgames.com/community/api/documentation/image/89ec0903-80e5-4c69-84a5-992e2197b93f)

### Range

The **Range** linked property provides a way for you to determine how many elements in the linked actor (for example, letters in a text actor) are animated. You can define how this is assessed using the **Unit** subproperty options.

![Animator range linked property](https://dev.epicgames.com/community/api/documentation/image/4d048ead-c277-4721-a83d-70c2d1a60b49)

#### Unit

The **Unit** subproperty determines how the range is measured. The options are:

- **Percentage**: The range is measured as a percentage of the elements in the actor.
- **Character**: The range is measured using individual characters in a text actor.

#### Percentage

The **Percentage** option assesses the entire range and, based on the values of the **Start**, **End**, and **Offset** subproperties, animates the actor elements within those bounds. In the example below, setting the value to 50% wiggles half of the string.

![Animator 50 percent range](https://dev.epicgames.com/community/api/documentation/image/c944c22a-34d4-41cc-a80d-38ed7314747e)

##### Start and End

The **Start** and **End** subproperties determine the percentage values at which your animator's effects start and stop applying to the linked actor.

##### Offset

The **Offset** subproperty shifts the range affected by your animation by a given percentage, increasing it with a positive value, decreasing it with a negative value. This stacks with the Start and End property value percentages.

#### Character

The **Character** option has various subproperties that provide you with tools to define precisely which characters you animate in a text actor.

##### Character Start and Character End

You can define the **Character Start** and **Character End** subproperties to pick which specific characters are animated. In the example below, only the R and V characters are animated because the Character Start value is 2, and the Character End value is 4.

![Animator range defined by character start and end](https://dev.epicgames.com/community/api/documentation/image/19b6cdc0-6d0c-4721-99f5-bae92860beae)

##### Character Offset

You can use the **Character Offset** subproperty to shift the range to the right or left. This stacks with the Character Start and Character End property values. For example, another way to achieve the same result shown in the previous example would be to start the range from 0, but then use a Character Offset value of 2.

#### Direction

The **Direction** subproperty determines the order in which the actor elements are evaluated. All the examples below use a Character Start property value of 0, and a Character End property value of 2, but the subproperty functions similarly when using percentages.

- **Left to Right** ![Animator range right to left](https://dev.epicgames.com/community/api/documentation/image/ed0153a6-f5d6-4640-a283-dec40fb5080c)
- **Right to Left** ![Animator range left to right](https://dev.epicgames.com/community/api/documentation/image/7581dccb-6867-4b61-80ec-feb3cdfa2429)
- **From Center** ![Animator range from center](https://dev.epicgames.com/community/api/documentation/image/ca0de2e4-526a-47cc-a0aa-6d849493c0bc)

| Numeric Linked Properties | Description |
| --- | --- |
| **Amplitude Min** | Determines the minimum movement of the animation. |
| **Amplitude Max** | Determines the maximum movement of the animation. |
| **Magnitude** | Determines the magnitude of the linked property. |
| **Time Offset** | Determines how long it takes to play a group of linked animations. |
| **Mode** | Determines how the animator interprets values in the properties affecting the animation. Options are: **Absolute** **Additive** |
| **Range** | Determines what elements of a group actor are animated. See the Range table below. |

| Range Sub-Properties | Description |
| --- | --- |
| **Unit** | Determines how to measure the range for applying the animation. Options are: **Percentage** **Character** |
| **Start** | Determines at what percentage of the actor group to start applying the animation. Only available when the Unit property is set to Percentage. |
| **End** | Determines at what percentage of the actor group to stop applying the animation. Only available when the Unit property is set to Percentage. |
| **Offset** | Determines an offset applied to the percentage of the actor group for applying the animation. Only available when the Unit property is set to Percentage. |
| **Character Start** | Determines at what character of the text actor to start applying the animation. Only available when the Unit property is set to Character. |
| **Character End** | Determines at what character of the text actor to stop applying the animation. Only available when the Unit property is set to Character. |
| **Character Offset** | Determines an offset applied to the characters of the text actor for applying the animation. Only available when the Unit property is set to Character. |
| Direction | Determines the direction used when calculating the range. Options are: **Left to Right** **Right to Left** **From Center** |

## Individual Numeric Animators

Here, you can find a description of each of the Numeric animators.

### Bounce

The **Bounce** animator has several properties you can use to control its effect. The default behavior is for the animation target to fall, then bounce.

![Bounce animator](https://dev.epicgames.com/community/api/documentation/image/3eb15847-71d8-4cc5-84eb-942155b1e7b0)

#### Invert Effect

Enabling the **Invert Effect** property changes the behavior. Rather than falling down and bouncing, the ball will bounce, then rise up.

![Bounce animator inverted](https://dev.epicgames.com/community/api/documentation/image/0da9c36c-cbe6-4543-a266-eb6dcdb6ed34)

#### Bounce Common Properties

Refer to the [Common Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/animators-in-unreal-engine#numeric-common-properties) section for details.

- Magnitude
- Cycle Mode
- Cycle Duration
- Cycle Gap Duration
- Seed
- Linked Properties
- Time Source Name

| Bounce Properties | Description |
| --- | --- |
| **Invert Effect** | Reverses the effect of the bounce animation. |

### Curve

The **Curve** animator is versatile and has many customizable options you can use to achieve various effects. In particular, you can use the Curve animator to recreate the effects of the Bounce, Oscillate, and Pulse animators, see the Presets section for more information.

#### Loop Curve

You can use the **Loop Curve** property to determine the shape of the main part of your curve.  In the example below, we used Loop Curve to create a simple curve. We linked the Loop Curve to the **RelativeRotation.Z** property of the text actor, and set the values of the **Amplitude Min** and **Amplitude Max** properties to -90 and 90, respectively. The result is that the animation follows a curve, rotating back and forth on the Z axis between the minimum and maximum amplitude values.

![Animator loop curve](https://dev.epicgames.com/community/api/documentation/image/ff434404-f4c7-4a34-8b7c-f5b0b7346a43)

##### Loop Curve Types

There are many different curves available for use with the Loop Curve property, some based on mathematical functions. See the list of curves below.

| Icon | Name | Icon | Name |
| --- | --- | --- | --- |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/71dbf084-3731-4cc9-885e-db07aed5fc31) | **Bounce** | ![Image](https://dev.epicgames.com/community/api/documentation/image/a99e52a1-108f-400c-bd85-caff6597813c) | **Noise\_High** |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/ddbef148-d9b9-4304-8cbc-beae717d15cf) | **Constant** | ![Image](https://dev.epicgames.com/community/api/documentation/image/460a43c9-502d-43ff-a4a6-f5035e8472f3) | **Pulse** |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/f79b4f22-7cea-43a3-91ba-4f2b2a5fa5a9) | **Cosine** | ![Image](https://dev.epicgames.com/community/api/documentation/image/9f4f1c1e-e2dd-4d4a-8b80-d8ad04b35c6f) | **Sawtooth** |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/3006a32d-83b5-4ba8-bf55-cbc61797eba5) | **Elastic** | ![Image](https://dev.epicgames.com/community/api/documentation/image/d6d6906b-f6e6-45ab-a33e-39c73013e26b) | **Sine** |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/44366543-2aa0-4765-88bc-fd278bd004c7) | **Linear** | ![Image](https://dev.epicgames.com/community/api/documentation/image/97cf6dd0-1699-4c0d-831e-d9166f66128f) | **Square** |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/b4acc4a0-2da6-4af2-8b9a-3e6bde2e5abc) | **Noise** | ![Image](https://dev.epicgames.com/community/api/documentation/image/3029f266-3290-40a4-89a8-91e79975a4e2) | **Triangle** |

#### In and Out

You can use the **In** and **Out** properties to define how the animator behaves as the curve begins and ends. You can enable both properties and assign a **Curve** type for each one. For this example, to simplify the curve, we set the Loop Curve to constant so that the only influence on the curve comes from the In and Out properties.

![Animator curve in and out](https://dev.epicgames.com/community/api/documentation/image/d99aac64-938d-4a1f-982f-f3df3f3ce70b)

##### Duration

The **Duration** subproperty of the In and Out properties determines how much time to give to each part of the loop. In the example above, the Duration is longer on the Out animation, which causes the text to rotate counter-clockwise at a slower pace.

![Animator In and Out Duration subproperty](https://dev.epicgames.com/community/api/documentation/image/8f718fbb-5df3-44a8-bb46-ac672e3b4157)

##### In and Out Curve Types

There are many different curves available for use with the In and Out properties, mostly based on mathematical functions. See the list of curves below.

| Icon | Name | Icon | Name |
| --- | --- | --- | --- |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/be57a53a-480c-4721-90c2-dbdf34adb187) | Bounce | ![Image](https://dev.epicgames.com/community/api/documentation/image/e1b0cef7-1357-4057-9279-50ad8c099340) | InSine |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/eff1f400-5ba3-4c2d-a1d4-63b16f212f8d) | InBack | ![Image](https://dev.epicgames.com/community/api/documentation/image/c4d5436e-0b82-40a0-9fb1-ee272778c09f) | Jiggle1 |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/9a19eb5e-2594-4e7d-9336-083eb71faa98) | InCircular | ![Image](https://dev.epicgames.com/community/api/documentation/image/5e732bd1-260a-413a-b90b-ed002bc48e00) | Jiggle2 |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/2f18826c-0b89-48df-b108-5af3d1c0c08b) | InCubic | ![Image](https://dev.epicgames.com/community/api/documentation/image/bedb262e-3205-4989-b56b-a17c5b797f26) | Jiggle3 |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/da6b1647-edd2-401e-bea0-7c25750b439e) | InExponential | ![Image](https://dev.epicgames.com/community/api/documentation/image/a2efbed1-ce9e-4e53-a75a-55fd99fb778f) | Jiggle4 |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/55582cf3-d51c-41c6-9685-652f6ce9a10f) | InOutBack | ![Image](https://dev.epicgames.com/community/api/documentation/image/7f5c155d-27c7-45e6-817b-be1094d51fef) | Jiggle5 |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/ca43e582-81d0-4bfd-bad4-7828d9a31058) | InOutCircular | ![Image](https://dev.epicgames.com/community/api/documentation/image/02323673-8cf1-46f6-9d1d-7ddd98aa7816) | Linear |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/f371202f-c96c-456b-9f30-75c0abf664e7) | InOutCubic | ![Image](https://dev.epicgames.com/community/api/documentation/image/fa8c0d4a-f1fd-4586-a243-a03d45c86233) | OutBack |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/62293133-ca92-4511-b307-826ed3da88ab) | InOutExponential | ![Image](https://dev.epicgames.com/community/api/documentation/image/aad4b547-3456-4393-af22-af45edc7db78) | OutCircular |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/83833b22-7c59-4e49-93d7-e11b53fc2fd5) | InOutOvershoot | ![Image](https://dev.epicgames.com/community/api/documentation/image/c973c899-3454-40db-a5e2-ae981c9542bf) | OutCubic |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/830e16d5-6301-4aba-99ca-c97b871290e1) | InOutQuadratic | ![Image](https://dev.epicgames.com/community/api/documentation/image/5806d1e0-78d8-4e34-9ae1-351efa45cdf5) | OutExponential |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/e821a046-aace-4c74-aca9-a850eacddd59) | InOutQuartic | ![Image](https://dev.epicgames.com/community/api/documentation/image/41cb33fd-0517-49e7-b5b5-31e9eaa1ce9a) | OutOvershoot |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/969ca057-9fff-47c7-b8e7-27c1d92a031f) | InOutQuintic | ![Image](https://dev.epicgames.com/community/api/documentation/image/8aee9dd0-be98-49c1-8597-82437c5d1966) | OutQuadratic |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/8858c6b4-64ee-4ba7-aed5-04e07e7942bc) | InOutSine | ![Image](https://dev.epicgames.com/community/api/documentation/image/eb6bae78-f0b5-4cb7-9b09-593e2f0f4078) | OutQuartic |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/49eae9e7-96de-4ed9-9c0b-05d41e1bf248) | InOvershoot | ![Image](https://dev.epicgames.com/community/api/documentation/image/4fd1d73b-5a96-4571-8212-42039b5215af) | OutQuintic |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/5480d902-ed8e-40d2-8ca5-07584db896fb) | InQuadratic | ![Image](https://dev.epicgames.com/community/api/documentation/image/84c114a6-d374-4069-bf6e-b23324c3b415) | OutSine |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/2d83d243-13ff-4254-915d-f811c7251f5c) | InQuartic | ![Image](https://dev.epicgames.com/community/api/documentation/image/3d2bcb38-7ead-4912-b901-bb232e0cccd0) | Squared |
| ![Image](https://dev.epicgames.com/community/api/documentation/image/9b8a02b8-2387-480c-9ca5-ba666c9d2fec) | InQuintic |   |   |

#### Curve Common Properties

Refer to the [Common Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/animators-in-unreal-engine#numeric-common-properties) section for details.

- Magnitude
- Cycle Mode
- Cycle Duration
- Cycle Gap Duration
- Seed
- Linked Properties
- Time Source Name
- Range

#### Working with Curve Animators

You can emphasize the motion of your curve using the Magnitude property. Setting it to 1.0 produces results similar to the example animations above, but increasing it slightly creates a swing with a larger windup. Here is an example where we set Magnitude to 1.4.

![Curve animator with modified magnitude](https://dev.epicgames.com/community/api/documentation/image/072c6a7c-a32c-4cf2-b548-2f9ac7a06d6d)

You can create interesting effects by applying a **Time Offset** on specific text characters, and then rotating individual characters with or without the Seed property enabled. Notice that without using the **Seed** property, the characters rotate in order from right to left, but with the Seed property enabled, they rotate in a random order. Changing the Seed value changes the rotation order.

Without Seed:

![Curve animator without seed](https://dev.epicgames.com/community/api/documentation/image/fb9d00d5-0a0a-4270-a354-b47c540019ed)

With Seed:

![Curve animator with seed](https://dev.epicgames.com/community/api/documentation/image/63e9004c-3d3a-464d-9424-4954528ded2f)

| Curve Properties | Description |
| --- | --- |
| **In** | Optional. Defines a curve for the start of the curve animation. Requires you to select a curve type, and a duration in seconds. |
| **Loop Curve** | Defines the curve used for the main animation. |
| **Out** | Optional. Defines a curve for the end of the curve animation. Requires you to select a curve type, and a duration in seconds. |

### Oscillate

You can use the **Oscillate** animator to have your animated actor alternate between minimum and maximum values for the property it is attached to.

#### Oscillate Function

To achieve this effect, the animator has one unique property, the **Oscillate Function**, which controls how the animation moves between the minimum and maximum across time. The examples shown below all have the Oscillate animator applied to the RelativeLocation.Z property of sphere actors.

##### Sine and Cosine

The **Sine** and **Cosine** functions produce a smooth oscillation that decelerates at the minimum  and maximum values before reversing.

[Video: V_mnHjSL](https://dev.epicgames.com/community/api/cms/videos/V_mnHjSL/embed.html)

##### Square and Inverted Square

The Square and Inverted Square functions oscillate between the minimum and maximum values, never in-between.

![oscillate animator square and inverted square](https://dev.epicgames.com/community/api/documentation/image/37342e87-102d-4a79-ba21-625867ca38da)

##### Sawtooth

The Sawtooth function moves from minimum to maximum, and then resets before the next oscillation.

![Oscillate animator sawtooth](https://dev.epicgames.com/community/api/documentation/image/87a99bf8-de5a-49ee-8322-7dafca6cd125)

##### Triangle

The Triangle function oscillates back and forth between the minimum and maximum values at a consistent speed, with an instant reversal at each transition.

![Oscillate animator triangle](https://dev.epicgames.com/community/api/documentation/image/9176e2e0-e64e-42b4-9473-9ddb847875d0)

#### Oscillate Common Properties

Refer to the [Common Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/animators-in-unreal-engine#numeric-common-properties) section for details.

- Magnitude
- Cycle Mode
- Cycle Duration
- Cycle Gap Duration
- Seed
- Linked Properties
- Time Source Name

| Oscillate Properties | Description |
| --- | --- |
| **Oscillate Function** | Determines how the Oscillate animator moves the animated actors. Options are: Sine Cosine Square Inverted Square Sawtooth Triangle |

### Pulse

The **Pulse** animator moves a curve through the actors you are animating, creating a wavelike effect using a curve of your choosing.

#### Easing Function

The **Easing Function** property is how you choose the animation curve type for your Pulse animation. The default curve option is Linear. See below for examples of the curve options.

##### Linear

![Pulse linear easing function](https://dev.epicgames.com/community/api/documentation/image/9a3b182d-03a0-4279-8daa-d406fcb4e988)

##### Sine

![Pulse sine easing function](https://dev.epicgames.com/community/api/documentation/image/9c0b36c6-2dfb-46d9-b033-7013139f19fa)

##### Quad

![Pulse quad easing function](https://dev.epicgames.com/community/api/documentation/image/3ba639d7-d982-4c0e-9b1e-45488b9fe84a)

##### Cubic

![Pulse cubic easing function](https://dev.epicgames.com/community/api/documentation/image/07d53978-6a5d-4860-84f6-578918022ac0)

##### Quart

![Pulse quart easing function](https://dev.epicgames.com/community/api/documentation/image/92afbc30-0f1e-40bd-a890-f0f0609ef80e)

##### Quint

![Pulse quint easing function](https://dev.epicgames.com/community/api/documentation/image/4bf62a99-bafa-4419-b452-d07f30aa11fd)

##### Expo

![Pulse expo easing function](https://dev.epicgames.com/community/api/documentation/image/d0efab34-89ee-4868-af50-00ddc5e85f22)

##### Circ

![Pulse circ easing function](https://dev.epicgames.com/community/api/documentation/image/3e2ec91c-0f4e-457d-b9f8-d82a858d356b)

##### Back

![Pulse back easing function](https://dev.epicgames.com/community/api/documentation/image/2ae01ccf-5794-43c7-99c6-18c071beada2)

##### Elastic

![Pulse elastic easing function](https://dev.epicgames.com/community/api/documentation/image/7b60e5f2-db6e-44be-934f-b924e68b088f)

##### Bounce

![Pulse bounce easing type](https://dev.epicgames.com/community/api/documentation/image/40933385-ae5f-4977-8a06-09bfe7158af6)

#### Easing Type

The **Easing Type** property gives you control over how the curve is applied to your actors. Your options are:

- **In**: The curve is applied more at the beginning of the animation.
- **Out**: The curve is applied more at the end of the animation.
- **In Out**: Combines the functions of the other two options.

The video below shows some comparisons between using the In and Out Easing Type options for various curves.

[Video: V_DvS5fs](https://dev.epicgames.com/community/api/cms/videos/V_DvS5fs/embed.html)

#### Pulse Common Properties

Refer to the [Common Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/animators-in-unreal-engine#numeric-common-properties) section for details.

- Magnitude
- Cycle Mode
- Cycle Duration
- Cycle Gap Duration
- Seed
- Linked Properties
- Time Source Name

| Pulse Properties | Description |
| --- | --- |
| **Easing Function** | Determines the curve used for the animation. Options are: Linear Sine Quad Cubic Quart Quint Expo Circ Back Elastic Bounce |
| **Easing Type** | Determines when during the animation the curve applies most. Options are: In Out In Out |

### Soundwave

You can use the **Soundwave** animator to drive the properties of an actor in your level using an audio source.

#### Sampled Sound Wave

The **Sampled Sound Wave** property is how you choose what sound to drive the animation.

![Soundwave animator sampled soundwave property](https://dev.epicgames.com/community/api/documentation/image/dcd1b1d8-3356-42ea-a1ab-b6f8fd78d63e)

When you expand the dropdown menu, you are presented with several options. You can create a new [MetaSound](https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-in-unreal-engine) or [Source Bus](https://dev.epicgames.com/documentation/en-us/unreal-engine/audio-bus-overview) asset, or select any of the existing sounds available in Unreal Engine, either by selecting them from the list or browsing for one using the search bar. You can adjust your search parameters using the available settings by clicking the gear icon.

![Soundwave animator sound source options](https://dev.epicgames.com/community/api/documentation/image/c40b652b-8e01-4d02-8713-98e95a49e86b)

#### Loop

You can loop your soundwave animation by enabling the **Loop** property.

#### Soundwave Common Properties

Refer to the [Common Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/animators-in-unreal-engine#numeric-common-properties) section for details.

- Magnitude
- Seed
- Linked Properties
- Time Source Name

#### Working with Soundwave Animators

To use the animator, start by adding it to one of your actors. In the example below, we used a sphere actor.

![Soundwave animator on sphere](https://dev.epicgames.com/community/api/documentation/image/60205ddb-4a49-4960-99fe-73796bfc4b94)

In the example, the sphere already has a material applied to it using the Material Designer.

![Soundwave animator sphere material](https://dev.epicgames.com/community/api/documentation/image/8ab78c23-e99c-4c45-9a0a-831251159c78)

Because we already added the modifier, right-clicking the green value shows the following menu:

![Selecting the value for the soundwave animator](https://dev.epicgames.com/community/api/documentation/image/9ae10804-d040-4616-a306-28c033fd4bec)

In the example, we selected **Value.G (Float)** from the **Existing Animators** section. This added the property to the **Linked Properties** in the **Animators** panel. Next, we set the **Sampled Sound Wave** to an audio file. When creating your own animations, you can expose other properties to amplify the effect. In the example below, we added a scale property to make the sphere expand while the sound plays. You’ll notice that it gets brighter as it expands.

Here is the effect of combining scale with the color to make it glow and expand.

![Soundwave example using scale and brightness](https://dev.epicgames.com/community/api/documentation/image/c99344b4-bce9-4af9-a811-7954e4d8557e)

If you have several actors using this animator, and you want to make sure they aren’t synchronized, you can change the **Seed** property.

### Time

When you want to animate an object property and define how long it takes to do a complete cycle through the animation, you can use the **Time** animator to control it.

In the example below, the property animated is the rotation:

![Time animator](https://dev.epicgames.com/community/api/documentation/image/567a12d6-c477-4146-8833-82066569110f)

Notice the range of values from the Amplitude Min property value of -180 to the Amplitude Max property value of 180 results in a rotation of 360 total degrees. Values of 0 and 360 respectively would accomplish the same goal.

#### Time Common Properties

Refer to the [Common Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/animators-in-unreal-engine#numeric-common-properties) section for details.

- Magnitude
- Cycle Mode
- Cycle Duration
- Cycle Gap Duration
- Seed
- Linked Properties
- Time Source Name

### Wiggle

The **Wiggle** animator randomizes the value of a property (such as a transform) between two values: the **Amplitude Min** and **Amplitude Max**.

![Wiggle animator](https://dev.epicgames.com/community/api/documentation/image/05d701b4-3169-428e-b202-f35c850125d4)

#### Frequency

The Wiggle animator has one unique property, **Frequency**, measured in Hz. The higher your frequency, the faster your actor will wiggle. If you have several actors using this animator, and you want to make sure they aren’t wiggling in an identical fashion, you can change the Seed property.

#### Wiggle Common Properties

Refer to the [Common Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/animators-in-unreal-engine#numeric-common-properties) section for details.

- Magnitude
- Seed
- Linked Properties
- Time Source Name

| Wiggle Properties | Description |
| --- | --- |
| Frequency | Determines how quickly the animated actor wiggles. |

## Presets

The Bounce, Oscillate, and Pulse animators are functionally specialized implementations of the Curve animator. It is possible to achieve the same results as those animators using only specific parameters for the Curve animator properties. The numeric animator presets provide exactly those specific parameters.

There are three presets:

- **Pulse (Curve)**
- **Oscillate (Curve)**
- **Bounce (Curve)**

All of these function in similar ways. When added to an actor, each is a Curve animator with the properties set up so that the parameters create the effects of the standard Pulse, Oscillate, and Bounce animators, respectively.

![Animator presets](https://dev.epicgames.com/community/api/documentation/image/7b543e6b-da35-426d-a417-908d85d7ddb3)

This provides you with a starting point to make more complex animations than you can with the standard animators, by modifying those parameters to produce animation effects different from what is possible with the standard animators.

## Text

Text animators are designed to change the content of Text actors, according to the effects you want to apply, rather than animating the characters themselves as with the numeric animators. Here you can find a description of the common properties for text animators, and the functionality of each text animator.

### Time Source Name

Similar to the numeric animators, you can drive your text animator from a variety of time sources using the **Time Source Name** property, but there are differences in how the property functions, compared to numeric animators.  The **World**, **Manual**, and **Sequencer** options are similar, but you also have access to the **System** option.

#### World

Setting your time source to **World** displays the total amount of time in seconds you’ve had your level open, as shown in the example image below.

![Text animator world time](https://dev.epicgames.com/community/api/documentation/image/e7afa925-e9fc-4df4-a247-75ee6cd7005b)

#### Manual

For text animators using the **Manual** option for the Time Source Name property, the Custom Time and Playback State subproperties function identically to how they behave for numeric animators.

#### Sequencer

You can drive your text animator using a **Sequencer** track, in the same way as numeric animators.  Click **Create Track** to drive your counter using the Sequencer playhead.

You can do something like this:

[Video: V_aRtzS1](https://dev.epicgames.com/community/api/cms/videos/V_aRtzS1/embed.html)

#### System

Setting your time source to **System** displays a count of the time in seconds based on the system clock. The System option also provides a **Mode** subproperty, where you can choose between three display options for the system time.

- **Local Time**
- **Countdown**
- **Stopwatch**

##### Local Time

The **Local Time** option is the default for system time. Unlike the World option, which counts how long your level has been open, the Local Time option displays how your system tracks time from zero. As this is based on the current calendar year, with the zero point being 0 AD, the default value shown is a large number, almost 64 billion seconds.

![System time default value](https://dev.epicgames.com/community/api/documentation/image/20e71de9-2112-4b7e-a71f-84aef6764a57)

##### Countdown

The **Countdown** option, as the name reveals, counts down from the time you enabled the Time Source Name property. The Countdown option provides access to two additional subproperties, **Countdown Format** and **Countdown Time**. These function identically to how they function for the [Global Time Source Name Countdown](https://dev.epicgames.com/documentation/en-us/unreal-engine/animators-in-unreal-engine#countdown) option, except limited to only their respective text animator.

![Countdown subproperties](https://dev.epicgames.com/community/api/documentation/image/eafd0db2-1fa9-4b38-af02-e2a0aa610d25)

##### Stopwatch

The **Stopwatch** option counts up from the time you enabled the Time Source Name property. By default, the count is displayed in seconds.

##### UTC

When using the System option, you can enable the **UTC time** property to show the time according to Coordinated Universal Time (UTC).

### Linked Properties

Text animators use linked properties to control the text of text actors. The first step to using any text animator is to link its properties to the text actor you added it to.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The example here uses a Clock animator, but the workflow applies to Counter animators as well.",
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

After you add a text animator to a text actor, you see the same error message as for numeric animators, **No properties are currently linked to this animator**, as shown in the image below.

![Linked Properties error message](https://dev.epicgames.com/community/api/documentation/image/79b63ccd-574f-4f0f-9ba1-281be973855b)

In this example, we placed a standard Text actor from the Motion Design palette, then added the Clock animator to it.

![Motion Design text actor](https://dev.epicgames.com/community/api/documentation/image/753bc384-5515-4be7-97af-8feed842fb2c)

After adding the animator, click the **+** button next to **Linked Properties**, then under **Presets** select **Text**, then **Text (FText)**

![Linked Properties for text animator](https://dev.epicgames.com/community/api/documentation/image/e862e022-c468-402a-9fb8-497d5ce6a598)

After you link the Text(FText) to your text animator, the text animator now controls how the text displays, depending on the value of the properties for your text animator.

#### Mode

For text animators, only the **Mode** linked property becomes available when you link your text animator to your text actor. However, compared to the numeric animators, it gives you different functionality for the Absolute and Additive options.

##### Absolute

The Absolute option for the Mode property replaces the displayed text of the text actor with the output of the text animator.

##### Additive

The Additive option appends the output of the text animator to the existing text of the actor. The effects of the Additive option create results similar to the Display Format or Display Pattern properties, but by modifying the text actor instead of the text animator.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "We don't recommend using both the Display Format or Display Pattern and Additive Mode to modify the text simultaneously, as this is likely to have inconsistent or unpredictable results.",
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

### Clock

The **Clock** animator provides a way for you to display time in a variety of configurations. This is useful when trying to use a digital clock in your designs (such as in a sports scoreboard or a countdown). Because of this focus, the Clock animator has only one unique property, the **Display Format**, and the customization options are focused on how to display the date and time.

#### Display Format

The **Display Format** property gives you a way to decide what to display, by combining text characters with variables. By default, the Display Format property of the clock is set up to display hours, minutes, and seconds (%H:%M:%S). There are a large number of variables you can use to customize how your Clock animator displays the time and date, which you can combine freely with text characters.

| Display Format Date / Time Variable | Description |
| --- | --- |
| %a | Weekday, abbreviated. For example, Sun. |
| %A | Weekday, full. For example, Sunday. |
| %w | Weekday, 0–6, Sunday is 0. |
| %y | Year, last 2 digits, YY. |
| %Y | Year, four digits, YYYY. |
| %b | Month, abbreviated. For example, Jan. |
| %B | Month, full. For example, January. |
| %m | Month, 01–12 |
| %n | Month, 1–12 |
| %d | Day, 01–31 |
| %e | Day, 1–31 |
| %] | Day of the Year, 001–366 |
| %J | Day of the Year, 1–366 |
| %I (lowercase L) | 12h Hour, 1–12 |
| %l (capital i) | 12h Hour, 01–12 |
| %H | 24h Hour, 00–23 |
| %h | 24h Hour, 0–23 |
| %M | Minute, 00–59 |
| %N | Minute, 0–59 |
| %S | Second, 00–60 |
| %s | Second, 0–60 |
| %f | Millisecond, 000–999 |
| %F | Millisecond, 0–999 |
| %p | AM or PM |
| %P | am or pm |
| %t | Ticks since midnight, January 1, 0001 |

![Clock animator properties](https://dev.epicgames.com/community/api/documentation/image/d6c5f05b-73c9-411e-a07e-0281b2cc1006)

#### Working with Clock Animators

When you first add the Clock animator to your text actor, you must set up its Linked Properties, as described above.

After linking the Clock animator to your text actor's Text(FText) property, your result should resemble the image below. The Clock animator uses the World time by default, so it reflects how long the level has been open. In this example, it’s been open for 1 minute and 10 seconds.

![Clock animator using the World time source](https://dev.epicgames.com/community/api/documentation/image/667aafc3-eaf8-4749-b117-e130ab02c306)

If your goal is to control the time value shown on the clock rather than display the time, set the Time Source Name property to Sequencer, then click Create Track.

![Clock animator Sequencer Create Track](https://dev.epicgames.com/community/api/documentation/image/bcd8b1a5-d72d-4151-89cf-c36f2fa41da6)

After creating a track, you can directly control the displayed time by scrubbing in Sequencer (as shown above in the Text Common Properties under [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/animators-in-unreal-engine#sequencer)).

| Clock Properties | Description |
| --- | --- |
| **Display Format** | Determines the date and time format of the Clock animator using variables and text characters. |

### Counter

The **Counter** animator provides a way for you to display a numerical value as it counts, similar to a stopwatch. Unlike the Clock animator, the properties of the Counter animator are broad and customizable.

When you first add a Counter animator to your text actor, you see the following interface:

![Counter animator initial state](https://dev.epicgames.com/community/api/documentation/image/320c3122-a95f-4523-9822-dbbad6f8bc68)

You must set up the Counter animator's Linked Properties, as described above.

After linking the Counter animator to your text actor's Text(FText) property, you should immediately see the text update to show your counter:

![Counter animator after setting Linked Properties](https://dev.epicgames.com/community/api/documentation/image/5a694323-a4f5-4aa8-a301-dd9f7d14b017)

You can now proceed in two ways:

- Select a preset for your counter animator using the **Preset Format Name** dropdown menu.
- Enable **Use Custom Format** to customize your counter's properties manually.

In either case, you can customize your counter's display using the **Display Pattern** property.

#### Display Pattern

You can customize your timer's format using the **Display Pattern** property by placing text before and after the count value.

![Display pattern property default](https://dev.epicgames.com/community/api/documentation/image/0442bde1-9eb6-4550-9534-78cedd6e9d6b)

The default setting, with no additional text, produces a result similar to the image below:

![Counter animator default display](https://dev.epicgames.com/community/api/documentation/image/63a935ab-8f87-4432-bce0-c1498c992069)

In the example below, we added additional text:

![Counter animator modified Display Pattern property](https://dev.epicgames.com/community/api/documentation/image/d824ae49-0c4c-43f3-acd3-8fa4465fc48d)

The added text produces a result like in the image below:

![Counter animator modified display](https://dev.epicgames.com/community/api/documentation/image/40aa8abc-4f42-4af9-9741-f70efb4bb4fd)

#### Use Custom Format

If you don't want to use a preset, enable **Use Custom Format**.

![Use Custom Format property](https://dev.epicgames.com/community/api/documentation/image/54c49b1d-127b-47f8-99aa-e01da4adc082)

When you enable Use Custom Format, the **Custom Format** property replaces the Preset Format Name property. Expand the property to see the available subproperties you can modify to customize your Counter animator.

#### Preset Format Name

The **Preset Format Name** property provides a dropdown menu you can use to select a counter preset from those you have available. When you first start working with counter animators, you only have access to the Default preset. You need to create and save additional presets to have them available to use with counter animators in your projects.

![Preset Format Name menu default list](https://dev.epicgames.com/community/api/documentation/image/8236caea-f7d5-4d1d-bf75-70545d0d670c)

#### Custom Format

The **Custom Format** property expands to show a list of subproperties you can use to customize your counter.

![Custom Format subproperty list](https://dev.epicgames.com/community/api/documentation/image/1ac45cd4-e4a3-4afd-bc72-bfcfea1a1d4d)

##### Format Name

Use the **Format Name** subproperty to give your format a name, which determines how it appears in the list of presets in the Project Settings.

##### Min Integer Count

The **Min Integer Count** subproperty determines the number of integers before the decimal. The example in the first image below shows a value of 3. The functioning of the **Padding Character** and **Truncate** subproperties also depend on the value of the Min Integer Count subproperty.

![Min Integer Count subproperty value of 3](https://dev.epicgames.com/community/api/documentation/image/4ac8aac6-0882-481a-9087-9d4d6805a3ed)

The example below shows a value of 10.

![Min Integer Count subproperty value of 3](https://dev.epicgames.com/community/api/documentation/image/379f7714-23fc-4855-adac-a8ff6272810b)

##### Max Decimal Count

The **Max Decimal Count** subproperty determines the number of decimal places, functioning in the same way as the Min Integer Count does for the integers.

##### Grouping Size

The **Grouping Size** subproperty Increases the number of digits necessary to display something as a thousand. The default value is 0, which means no grouping.

The image below shows an example with a count of 900.3, with the Grouping Size value set to 1.

![Grouping Size set to 1](https://dev.epicgames.com/community/api/documentation/image/abcd6666-bbad-40b0-a597-1a4e6f000b79)

Here is an example with a count of 1031.3, with the Grouping Size value set to 3, which creates the standard 3-digit grouping by thousands.

![Grouping Size set to 3](https://dev.epicgames.com/community/api/documentation/image/61124850-006d-4db5-b8c5-78bc3a7aef11)

For clarification, this is a further example with a count in the thousands (1075.6) with the Grouping Size value set to 1

![Grouping size set to 1 with a 4 digit number](https://dev.epicgames.com/community/api/documentation/image/cc39a42c-6971-4f85-b19a-532db7122169)

##### Decimal Character

The **Decimal Character** subproperty replaces the character representing a decimal with the character you select. The example below shows a question mark used instead.

![Decimal Character using question mark](https://dev.epicgames.com/community/api/documentation/image/3da9e555-3218-42cd-9516-49b5b742ac15)

##### Grouping Character

The **Grouping Character** subproperty functions in the same way as the Decimal Character property, except it instead replaces the comma used for grouping with the character you select.

##### Padding Character

You can use the **Padding Character** subproperty to determine how to fill the empty spaces in your counter, using the character you select. In the example shown below, the Min Integer Count value is 9, the counter is counting seconds, but several fields are empty because the seconds count isn't high enough, so the empty spots are replaced with dashes.

![Padding Character using the dash character](https://dev.epicgames.com/community/api/documentation/image/8513a751-3fd6-488d-9b46-edde1d5702c1)

If you leave the Padding Character subproperty empty, the empty spots are not shown, and you see something like the example below:

![Padding Character property with no value](https://dev.epicgames.com/community/api/documentation/image/42f29d21-edf3-4521-a312-88c18adbba31)

##### Rounding Mode

The **Rounding Mode** subproperty provides the option to round the value up or down. The options are:

- **None**: No rounding (default).
- **Round**: Round off, which means down for rounded values below 5, and up for rounded values greater than 5.
- **Floor**: Round down.
- **Ciel**: Round up.

##### Use Sign

The **Use Sign** subproperty adds a **+** or **-** character to the count, depending on whether the value of the Custom Time property is positive or negative.

![Use Sign subproperty](https://dev.epicgames.com/community/api/documentation/image/7220ba93-379c-4422-89e3-256c3efe4b94)

![Use Sign subproperty display](https://dev.epicgames.com/community/api/documentation/image/60028a31-714b-45b5-a168-19e381d908c0)

##### Truncate

The **Truncate** subproperty provides a way for you to cap the number of displayed characters to the value set in the Min Integer Count property. For example, if you have the Min Integer Count property set to 2, you will see this:

![Min Integer Count subproperty setting at 2](https://dev.epicgames.com/community/api/documentation/image/d08652b7-5fb8-456e-b263-a1d673931170)

![Image](https://dev.epicgames.com/community/api/documentation/image/15845e1f-445b-4f48-94bb-24eeb7f75a55)

If you have the Min Integer Count set to 1, you will see this:

![Min Integer Count subproperty setting at 1](https://dev.epicgames.com/community/api/documentation/image/63d35b37-7437-4bc1-bae8-4b292cb0dbe9)

![Truncate display with Min Integer Count at 1](https://dev.epicgames.com/community/api/documentation/image/4cb61a50-007a-4969-bcea-d73f19679e2e)

#### Saving Presets

If, after creating a custom format, you want to save it for reuse, click **Save Custom Format as Preset**. The values of your custom format subproperties populate the preset properties in the **Property Animator** settings. For this example, we entered 11 for the values of several subproperties, as a demonstration:

![Sample Custom Format subproperties](https://dev.epicgames.com/community/api/documentation/image/01b5e47b-ba5a-47d6-b473-08322c474ef6)

We saved the subproperty values as described above, then disabled **Use Custom Format**:

![Disabled Use Custom Format property](https://dev.epicgames.com/community/api/documentation/image/47af5294-1476-46bd-81ec-d82c3379462b)

We then click **Open Property Animator Settings**, and can now see the saved property values as a new preset, second in the list of preset options.

![Motion Design Property Animator presets](https://dev.epicgames.com/community/api/documentation/image/228f8cc6-2f83-4212-b877-63e13bcc8fa8)

#### Creating Presets

If you want to create presets directly without using the Custom Format property, you can click **Open Property Animator Settings** to create presets for your counter animators.

![Motion Design Property Animator presets default list](https://dev.epicgames.com/community/api/documentation/image/fb3b6e24-b29d-44b7-9651-37bfe7cc758d)

The properties are the same as the subproperties available under the Custom Format property in the counter animator. Click the + icon to add a new set element to the list Counter Format Presets, then enter the preset values you choose. Make sure to give your preset a unique name to identify it.

You can optionally:

- Click **Set as Default** to make your current preset your new default for your counter animators.
- **Export** or **Import** a saved preset.
- Click **Reset to Defaults** to wipe out your current preset values to start over.

| Counter Properties | Description |
| --- | --- |
| **Display** **Pattern** | Determines the text that precedes and follows the counter. |
| **Use Custom Format** | Enable to use the Custom Format property and its subproperties. |
| **Preset Format Name** | Determines the preset used for the counter animator. Only available when Use Custom Format is disabled. |
| **Custom Format** | Provides access to various subproperties for customizing the counter animator's functionality. See the table below for the list of subproperties. |

| Custom Format Subproperties | Description |
| --- | --- |
| **Format Name** | Determines the name used to identify the custom format. |
| **Min Integer Count** | Determines the minimum number of integers shown on the counter. |
| **Max Decimal Count** | Determines the maximum number of decimal places shown on the counter. |
| **Grouping Size** | Determines how many digits to group together before showing a grouping character. |
| **Decimal Character** | Determines the character used for the decimal point. |
| **Grouping Character** | Determines the character used to separate groupings. |
| **Padding Character** | Determines the character used to fill empty spaces when using a high Min Integer Value. |
| **Rounding Mode** | Determines the method used for rounding the decimal places value. Options are: None Round Floor Ciel |
| **Use Sign** | Enable to display the sign of the value (+ or -). |
| **Truncate** | Enable to cap the number of integers shown to the Min Integer Value. |
