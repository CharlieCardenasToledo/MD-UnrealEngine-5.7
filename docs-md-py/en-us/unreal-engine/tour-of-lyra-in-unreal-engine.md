# Tour of Lyra

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/tour-of-lyra-in-unreal-engine

> Application Version: 5.7

## A Tour Of Lyra

When launching Lyra, you will be greeted with the main menu.

![main-menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f9190a7-6ab2-402a-b45e-e6f5b013ef62/mainmenu.gif)

| Main Menu Option | Description |
| --- | --- |
| **Play Game** | Launches the **Play Menu** of Lyra that contains the options to **Quickplay**, **Start a Game**, and **Browse**. |
| **Options** | For Game Languages, Video and Audio Settings, Key bindings and inputs, and Accessibility options. |
| **Credits** | Contains an example of a game Credits UI template. |
| **Quit Lyra** | Exits the game. |

## Lyra Main Play Menu

When you click Play Game from the initial main menu, the Main Play Menu is displayed.

### QuickPlay

The **QuickPlay** menu joins an existing session of any game type or starts a new online game that others can join.

### Start a Game

**Start a Game** creates a new session of any type with other players or bots. Online or local is available.
When choosing to start a game, you will have the opportunity to select your game mode from the available options.

| Game Mode | Description |
| --- | --- |
| **Control** | Secure the control points along with your teammates to increase your score and win. |
| **Elimination** | Find and eliminate enough enemies to win in this classic head-to-head team match. |
| **Exploder** | Destroy blocks, collect power-ups, and avoid getting exploded in this top-down party game. |

### Browse

The **Browse** menu searches for an active game session online and on your local network.

## Options

The options menu contains settings for Game Languages, Video and Audio Settings, Key bindings and inputs, and Accessibility options.

### Menu Options

#### Display

|  |  |  |
| --- | --- | --- |
| **Window Mode** |  | Provides a template of modes or screen settings to display the game. * **Full Screen**:Fullscreen displays the game on your entire screen and hides your operating system interface. This may prevent your interaction with other windows, however, the project will run at a better performance. * **Windowed FullScreen**: Windowed Fullscreen displays the game in a Fullscreen resolution while providing the capability to interact between other windows or applications on your operating system interface. * **Windowed**: Windowed mode provides you with the capability to drag the edges of the window to maximize or minimize the window screen, and interact between other windows and applications. |
| **Resolution** |  | Controls the number of pixels that are displayed on the dimensions of your screen size. The supported Screen Dimensions include: * **1280 x 720** * **1600 x 900** * **1920 x 1080** * **2560 x 1440** * **3840 x 2160** Depending on your current Window Mode, this will have the following results: * **Fullscreen**: Resolution determines the GPU output resolution.   Depending on your Graphics card and monitor screen size, this may result in a rendering display of black bars appearing on your screen. * **Windowed**: Resolution determines the size of the window. * **Windowed Fullscreen**: Resolution is inactive. |
| **Performance Stats** | Configures the display of performance statistics. |  |
|  | **Client FPS** | Displays the Client Frame Rate. The available display options are: * **None** * **Text Only** * **Graph Only** * **Text and Graph** |
|  | **Server FPS** | Displays the Server Frame Rate. The available display options are: * **None** * **Text Only** * **Graph Only** * **Text and Graph** |
|  | **Frame Time** | The total frame time. |
|  | **Idle Time** | The amount of time spent waiting idle for frame pacing. The available display options are: * **None** * **Text Only** * **Graph Only** * **Text and Graph** |
|  | **CPU Game Time** | The amount of time spent on the main game thread. The available display options are: * **None** * **Text Only** * **Graph Only** * **Text and Graph** |
|  | **CPU Render Time** | The amount of time spent on the rendering thread. The available display options are: * **None** * **Text Only** * **Graph Only** * **Text and Graph** |
|  | **CPU RHI Time** | The amount of time spent on the Render Hardware interface thread. The available display options are: * **None** * **Text Only** * **Graph Only** * **Text and Graph** |
|  | **GPU Render Time** | The amount of time spent on the GPU. The available display options are: * **None** * **Text Only** * **Graph Only** * **Text and Graph** |
| **Network** |  |  |
|  | **Ping** | The round trip latency of your connection to the server. The available display options are: * **None** * **Text Only** * **Graph Only** * **Text and Graph** |
|  | **Incoming Packet Loss** | The percentage of incoming packages lost. The available display options are: * **None** * **Text Only** * **Graph Only** * **Text and Graph** |
|  | **Outgoing Packet Loss** | The percentage of outgoing packages lost. The available display options are: * **None** * **Text Only** * **Graph Only** * **Text and Graph** |
|  | **Incoming Packet Rate** | Rate of Incoming packets(per second)The available display options are: * **None** * **Text Only** * **Graph Only** * **Text and Graph** |
|  | **Outgoing Packet Rate** | Rate of outgoing packets(per second)The available display options are: * **None** * **Text Only** * **Graph Only** * **Text and Graph** |
|  | **Incoming Packet Size** | The average size (in bytes) of packets received in the last second The available display options are: * **None** * **Text Only** * **Graph Only** * **Text and Graph** |
|  | **Outgoing Packet Size** | The average size (in bytes) of packets sent in the last second The available display options are: * **None** * **Text Only** * **Graph Only** * **Text and Graph** |

#### Graphics

|  |  |
| --- | --- |
| **Color Blind Mode** | Toggles the display to render in Color Blind Mode from the following options: * **Deuteranope** * **Protanope** * **Tritanope** Unreal will display the following images to assist you in finding your preferred color correction. color-blind |
| **Color Blind Strength** | Uses the provided images to test out the varying strengths of color correction within a range between 0-10. |
| **Brightness** | Adjusts the brightness between a value of 0 and 100%. |

#### Graphics Quality

|  |  |
| --- | --- |
| **Auto-Set Quality** | Auto-Set Quality automatically configures the Graphics Quality options based on the benchmark of your hardware. |
| **Quality Presets** | Quality Presets provide you with the following adjustable video quality options: * **Low** * **Medium** * **High** * **Epic** |
| **3D Resolution** | 3D Resolution determines the resolution of objects that are rendered in the game, this is controlled from a slider with a range between 0-100%. 3D Resolution will not affect the resolution of the Main Menu UI. . |
| **View Distance** | View Distance determines how far away objects are culled for performance. The following options are available: * **Near** * **Medium** * **Far** * **Epic** |
| **Shadows** | Shadows determine the resolution and view distance of dynamic shadows. Shadows improve visual quality and depth perception, however, may decrease performance. The following options are available: * **Off** * **Medium** * **High** * **Epic** |
| **Anti-Aliasing** | Anti-Aliasing reduces jagged artifacts along geometry edges. Increasing this setting will make edges look smoother, however, it may decrease performance. The following options are available: * **Off** * **Medium** * **High** * **Epic** |
| **Textures** | Textures determine the resolution quality of textures in the game. Increasing this setting will make objects more detailed, however, it may reduce performance. The following options are available: * **Low** * **Medium** * **High** * **Epic** |
| **Effects** | Effects determine the quality of visual effects and lighting in the game. Increasing this setting increases the quality of visual effects, however, it may reduce performance. The following options are available: * **Low** * **Medium** * **High** * **Epic** |
| **Global Illumination** | Global Illumination controls the quality of dynamically calculated indirect lighting bounces, Sky Shadowing, and Ambient Occlusion. Setting this to High or above will use accurate ray-tracing methods to solve lighting, however, may result in a decrease in performance. The following options are available: * **Low** * **Medium** * **High** * **Epic** |
| **Reflections** | Reflections determine the resolution and accuracy of reflections. Setting this too high or above will use accurate ray-tracing methods to solve reflections, however, may result in a decrease in performance. The following options are available: * **Low** * **Medium** * **High** * **Epic** |
| **Post Processing** | Post Processing Includes Motion Blur, Depth of Field, and Bloom. Increasing this setting will improve the quality of post-process effects, however, may result in a decrease in performance. The following Post Processing menu options are available: * **Low** * **Medium** * **High** * **Epic** |

#### Advanced Graphics

|  |  |
| --- | --- |
| **Vertical Sync** | Vertical Sync eliminates screen tearing by always rendering and presenting a full frame. Disabling vertical sync can give a higher frame rate and better input response, however, it may result in horizontal screen tearing. Vertical Sync is toggled by the following options: * **Off** * **On** |
| **Frame Rate Limit**(**On Battery**) | Sets the Frame rate limit when running on battery. Set this lower for a more consistent frame rate or higher for the best experience on faster machines. You may need to disable VSync to reach high frame rates. * **30 FPS** * **40 FPS** * **120 FPS** * **144 FPS** * **160 FPS** * **165 FPS** * **180 FPS** * **200 FPS** * **240 FPS** * **360 FPS** * **Unlimited** |
| **Frame Rate Limit** (**Menu**) | Frame rate limit when in the menu. Set this lower for a more consistent frame rate or higher for the best experience on faster machines. You may need to disable VSync to reach high frame rates. * **30 FPS** * **40 FPS** * **120 FPS** * **144 FPS** * **160 FPS** * **165 FPS** * **180 FPS** * **200 FPS** * **240 FPS** * **360 FPS** * **Unlimited** |
| **Frame Rate Limit** (**Background**) | Frame rate limit when in the background. Set this lower for a more consistent frame rate or higher for the best experience on faster machines. You may need to disable Vsync to reach high frame rates. * **30 FPS** * **40 FPS** * **120 FPS** * **144 FPS** * **160 FPS** * **165 FPS** * **180 FPS** * **200 FPS** * **240 FPS** * **360 FPS** * **Unlimited** |
| **Frame Rate Limit** | Frame rate limit sets the highest frame rate that is allowed. Set this lower for a more consistent frame rate or higher for the best experience on faster machines. You may need to disable Vsync to reach high frame rates. * **30 FPS** * **40 FPS** * **120 FPS** * **144 FPS** * **160 FPS** * **165 FPS** * **180 FPS** * **200 FPS** * **240 FPS** * **360 FPS** * **Unlimited** |

#### Volume

|  |  |
| --- | --- |
| **Overall** | Adjusts the overall volume of **Music**, **Sound Effects**, **Dialogue**, and **Voice chat**. This is controlled from a slider with a range between 0-100%. |
| **Music** | Adjusts the volume of Music. This is controlled from a slider with a range between 0-100%. |
| **Sound Effects** | Adjusts the volume of Sound Effects. This is controlled from a slider with a range between 0-100%. |
| **Dialogue** | Adjusts the volume of dialogue for game characters and voice-overs. This is controlled from a slider with a range between 0-100%. |
| **Voice Chat** | Adjusts the volume of voice chat. This is controlled from a slider with a range between 0-100%. |

#### Sound

|  |  |  |
| --- | --- | --- |
| **Subtitles** | Configures the visual appearance of Subtitles.You can access a full list of sub-settings by clicking **Options**. | Toggles Subtitles **ON** or **OFF**. |
|  | **Performance Stats** | Configures the display of performance statistics. |
|  | **Text Size** | Adjusts the size of the subtitle text through the following options: * **Extra Small** * **Small** * **Medium** * **Large** * **Extra Large** |
|  | **Text Color** | Choose different colors for the subtitle text. * **White** * **Yellow** |
|  | **Text Border** | Choose different borders for the text. * **None** * **Outline** * **DropShadow** |
|  | **Background Opacity** | Choose a different background or letterboxing for subtitles Clear * **Low** * **Medium** * **High** * **Solid** |
| **Audio Output Device** | Changes the audio output device for the game audio. The options below will display the audio output devices currently available to your Operating System. \* Default Changing this setting will not affect voice chat |  |
| **Background Audio** | Turns the game audio on/off when the game is in the background. When on, the game audio will continue to play when the game is minimized, or another window is focused. Available options include: * **Off** * **All Sounds** |  |
| **3D Headphones** | Enable binaural audio. Provides 3D audio spatialization, so you can hear the location of sounds more precisely including above, below, and behind you. Recommended for use with stereo headphones only. Available options include: * **Off** * **On** |  |
| **High Dynamic Range Audio** | Enables high dynamic range audio. Changes the runtime processing chain to increase the dynamic range of the audio mixdown. Appropriate for theater or more cinematic experiences.Available options include: * **Off** * **On** |  |

#### Sensitivity

|  |  |
| --- | --- |
| **X-Axis Sensitivity** | Sets the sensitivity of the mouse's **Horizontal**(**x**) axis. With higher settings the camera will move faster when looking left and right with the mouse. |
| **Y-Axis Sensitivity** | Sets the sensitivity of the mouse's **Vertical**(**y**) axis. With higher settings the camera will move faster when looking up and down with the mouse. |
| **Targeting Sensitivity** | Sets the modifier for reducing mouse sensitivity when targeting. 100% will have no slow down when targeting.Lower settings will have more slow down when targeting. |
| **Invert Vertical Axis** | Enable the Inversion of the Vertical look axis. Options to toggle are: * **Off** * **On** |
| **Invert Horizontal Axis** | Enable the Inversion of the Horizontal look axis. Options to toggle are: * **Off** * **On** |

#### Default Keyboard & Mouse

|  |  |
| --- | --- |
| **Move Forward** | Key Bindings for Move Forward. |
| **Move Backwards** | Key Bindings for Move Backward. |
| **Move Left** | Key Bindings for Move Left. |
| **Move Right** | Key Bindings for Move Right. |
| **Fire Weapon** | Key Bindings for Fire Weapon. |
| **Jump** | Key Bindings for Jump. |
| **Crouch** | Key Bindings for Crouch. |
| **Reload Weapon** | Key Bindings for Reload Weapon. |
| **Dash** | Key Bindings for Dash. |
| **Auto-Run** | Key Bindings for Auto-Run |
| **Fire Weapon**(**Auto**) | Key Bindings for Fire Weapon(Auto) |

#### Shooter Keyboard & Mouse

|  |  |
| --- | --- |
| **Show Scoreboard** | Key Bindings for Show Scoreboard. |
| **Aim Down Sight** | Key Bindings for Aim Down Sight. |
| **Throw Grenade** | Key Bindings for Throw Grenade. |
| **Emote** | Key Bindings for Emote. |
| **Quick Slot 1** | Key Bindings for Quick Slot 1. |
| **Quick Slot 2** | Key Bindings for Quick Slot 2. |
| **Quick Slot 3** | Key Bindings for Quick Slot 3. |
| **Melee** | Key Bindings for Melee. |
| **Quickslot Cycle Backward** | Key Bindings for Quickslot Cycle Backward. |
| **Quickslot Cycle Forward** | Key Bindings for Quickslot Cycle Forward |

#### Gamepad

|  |  |
| --- | --- |
| **Controller Hardware** | Toggles the type of controller you're using. Options to choose include: * **Xbox Controller** * **Dual sense** |
| **Vibration** | Turns controller vibration on or off. * **Off** * **On** |
| **Invert Vertical Axis** | Enables the inversion of the Vertical look axis. * **Off** * **On** |
| **Invert Horizontal Axis** | Enables the inversion of the Horizontal look axis. * **Off** * **On** |

#### Sensitivity

|  |  |
| --- | --- |
| **Look Sensitivity** | How Quickly your view rotates. * **1**(**Slow**) * **2**(**Slow+**) * **3**(**Slow++**) * **4**(**Normal**) * **5**(**Normal+**) * **6**(**Normal++**) * **7**(**Fast**) * **8**(**Fast+**) * **9**(**Fast++**) * **10**(**Insane**) |
| **Aim Sensitivity**(**ADS**) | How quickly your view rotates while aiming down sight(ADS). * **1**(**Slow**) * **2**(**Slow+**) * **3**(**Slow++**) * **4**(**Normal**) * **5**(**Normal+**) * **6**(**Normal++**) * **7**(**Fast**) * **8**(**Fast+**) * **9**(**Fast++**) * **10**(**Insane**) |

#### Controller Deadzone

|  |  |
| --- | --- |
| **Left Stick DeadZone** | Increase or decrease the area surrounding the Left stick that we ignore input from. Setting this value too low may result in the character continuing to move even after removing your finger from the stick. |
| **Right Stick DeadZone** | Increase or decrease the area surrounding the Right stick that we ignore input from. Setting this value too low may result in the character continuing to move even after removing your finger from the stick. |
