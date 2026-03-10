# Cinematic Depth of Field

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-depth-of-field-in-unreal-engine

> Application Version: 5.7

The following depth of field methods provides a cinematic look that closely resembles photography and film for desktop and console platforms using the Deferred Shading renderer and Clustered Forward renderer.

## Cinematic

**Cinematic** DOF closely matches real-world cameras, similarly to Circle and Bokeh DOF, you can see circular-shaped Bokeh (out-of-focus areas) with sharp [High Dynamic Range](https://dev.epicgames.com/documentation/en-us/unreal-engine/high-dynamic-range-display-output-in-unreal-engine) (HDR) content. This method uses a procedural Bokeh simulation that provides dynamic resolution stability and alpha channel support while being faster, scalable, and optimized for projects developing on desktops and consoles.

![Depth of Field Disabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f6cf3fb-259d-4211-9fba-2fe5bda60072/dof_cine_disabled.png)

![Cinematic Depth of Field](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e74c4893-eabb-48cc-b514-3843a8f753e9/dof_cine_enabled.png)

### Focus on the Shot's Subject

The key to achieving an aesthetically pleasing depth of field effect is all in how the subject(s) of the shot is focused. There are three core factors that affect setting up Depth of Field for any given shot:

* Decide on the Lens **Focal Length** to use.
* Choose an appropriate **Aperture** (f-stop number).
* Choose a **Distance to your Subject(s)** from the camera.

Let's break down the elements that make up the camera and scene being captured to understand what's going on when we adjust these settings:

![Camera Elements Diagram](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cda5fb6f-9634-4051-a422-b60a30c71c54/ue5_1-camera-elements-diagram.png)
