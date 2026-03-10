# nDisplay 3D Config Editor

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-3d-config-editor-in-unreal-engine

> Application Version: 5.7

You define most aspects of the nDisplay system through a single configuration asset, the **nDisplay Config Asset**, through the **nDisplay 3D Config Editor**. This asset defines the computers that make up your cluster network, the characteristics of the windows and viewports you want the Unreal Engine to render on each computer, the display device's topology and configuration, the parts of the virtual world each viewport should render, the types of input devices you want to accept, and more.

This page describes all the settings available in the **nDisplay 3D Config Editor**.

Click image to enlarge

1. **Toolbar**, located in the top left of the Editor.
2. **Components**, located on the left below the Toolbar.
3. **Preview**, located in the middle of the Editor to the right of the Components panel.
4. **Details**, located on the right of the Editor next to the Preview panel.
5. **Cluster**, located on the left of the Editor below the Components panel.
6. **Output Mapping**, located in the middle of the Editor below the Preview panel.
7. **Compiler Results**, located in the bottom right of the Editor below the Details panel.

## Toolbar

![nDsiplay Configuration Editor Toolbar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/68064794-22f1-4ac2-909b-5eef64481636/ndisplay-configuration-editor-toolbar.png)

The Toolbar in the 3D Config Editor shares most of the buttons with the Toolbar in the Blueprint Editor. The following are the two buttons unique to the nDisplay 3D Config Editor:

* **Import**: Imports an nDisplay configuration file (`.ndisplay`, `.cfg`) from the local computer.
* **Export**: Exports the nDisplay settings to a configuration file (`.ndisplay`) on the local computer.

Refer to [Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/toolbar-in-the-blueprints-visual-scripting-editor-for-unreal-engine) for more details on the other options.

## Components

![nDisplay Components panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/211508bd-0e7e-4523-b2e8-93e8ba3de79c/ndisplay-components-panel.png)

The Components panel defines the physical display, tracking, and in-camera setup for the nDisplay cluster. Adding components to the inherited Root Component is the first step in designing an nDisplay network. You can pick from a predefined list of Displays, Transforms, and default Camera Actors, or add any available UE components.

To use nDisplay with real-world tracking systems, add a Live Link Component to the Components panel. Refer to [Live Link](https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-in-unreal-engine) for more on how to configure this for your setup.

The following sections describe the nDisplay-specific components that can be added to your setup.

### Screen

nDisplay **Screen** Components are meant to conveniently define flat 2D displays of any size, shape, and resolution. With the referenced view point, the **View Origin** Component, they define a volume, called the *view frustum,* that renders a portion of your 3D scene from the camera's or the view point's perspective. The rendered pixels are stored in the Viewport structure, which binds a display, a view point, and a projection policy together. Each of these projection screens need to have the same or similar dimensions in space as the physical screen that you'll use to render it. This setup is compatible with most projection policies.

The pivot point of a screen is always in its exact midpoint.

![nDisplay Screen Component](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ca4627f-4a3c-49d4-8f55-e32282ed48ad/ndisplay-screen-component.png)

### Static Mesh

When dealing with non-flat displays such as curved LED walls or displays, you can use the Static Mesh Component instead of the Screen Component. This allows you to fully define the shape of your screen using a Static Mesh. This setup is compatible with most projection policies.

![Static Mesh Component in nDisplay Configuration Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/945e3ca3-2b03-4ee3-b267-9621318ffd17/static-mesh-component.png)

### Xform

By default, the parent of all objects is the Root Component origin: an arbitrary point in 3D world space where the X, Y, and Z axes have their zero point. You can also configure specific named transforms in 3D space, called Xforms, which can act as parents for one or more components. This can help simplify the spatial layout of your screens, cameras, and other components. Xforms include a visualization mesh and the ability to scale the component in the Details panel.

![nDisplay xform component](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c23b27de-ef41-4282-9e42-35e1c3bd7cc3/ndisplay-xform-component.png)


You can use UE's standard Scene Components instead of Xforms to act as a parent for one or more components, but they will not have the visualization mesh or the ability to control their size in the Details panel.

### View Origin

The component for the nDisplay setup that defines the origin for what's rendered in the viewports. Alongside screens or static mesh components defining your displays, they define a view frustum used for rendering 3D content properly. You can have multiple View Origins in your configuration file and bind them to different viewports and displays. The View Origin also contains the settings for [Stereo Rendering](https://dev.epicgames.com/documentation/en-us/unreal-engine/stereoscopic-rendering-with-ndisplay-in-unreal-engine) with nDisplay.

![nDisplay View Origin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1979203c-66bc-4e82-acf4-7eee028df1ca/ndisplay-configuration-editor-view-origin.gif)

### ICVFX Camera

This is a Cine Camera Component where you can reference or link to an external camera placed within your level or project. This component creates the inner frustum necessary for [in-camera VFX](https://dev.epicgames.com/documentation/en-us/unreal-engine/in-camera-vfx-in-unreal-engine) projects.

![nDisplay ICVFX Camera](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dde911a2-102d-4247-860c-b1901d25cde7/ndisplay-icvfx-camera.gif)

## Cluster

![nDisplay Cluster panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4cba956b-a347-4a76-8ae7-bb3627b3043a/ndisplay-cluster-panel.png)
