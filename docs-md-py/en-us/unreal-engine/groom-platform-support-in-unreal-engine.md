# Groom Platform Support

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/groom-platform-support-in-unreal-engine

> Application Version: 5.7

This page contains information on various platforms that support different features of grooms.

## Groom Geometry Types

Groom **Cards** and Groom **Meshes** geometry are supported on all platforms. However, Groom **Strands** rendering can only run on certain platforms due to its demanding rendering cost.

Strands rendering is only supported on the following platforms:

- Microsoft Windows that uses either DirectX 11, DirectX 12, or Vulkan.
- Apple macOS, requires Shader Model 6 on the Mac M2 and above.
- Linux
- Current generation console, such as PlayStation 5 and Xbox Series S/X.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For more general information about what hardware and software Unreal Engine supports, see Unreal Engine's <a href=\"understanding-the-basics\\installing-unreal-engine\\hardware-software-specifications\">Hardware and Software Specifications</a>.",
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

## Groom Binding

A Groom can be attached to skeletal mesh geometry with Groom Bindings. There are two types of binding attachments: rigid and skinned.

These bindings attachments support the following platforms:

- **Rigid attachment** is supported on all platforms.
- **Skinned attachment** is supported on all platforms except Nintendo Switch and mobile because the performance cost is too much and there is missing implementation to support it.

Similar to Skinned attachment, **Global Interpolation** (also called RBF) is supported on all platforms except Nintendo Switch and mobile.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "To learn more about groom bindings and how they are used, see <a data-document-id=\"3223404\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-bindings-for-grooms-in-unreal-engine\">Setting up Bindings for Grooms</a>.",
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

## Simulation

Groom simulation is supported on all platforms.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "To learn more about using simulation with grooms, see <a data-document-id=\"3223408\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/enabling-physics-simulation-on-grooms-in-unreal-engine\">Enabling Physics Simulation on Grooms</a>.",
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

## Groom Cache

Using a Groom Cache allows for pre-computed simulation / animation. This is achieved at the Guide level or Strands level.

- The **Strands Cache** is available only on platforms that support Strand rendering (see ["Groom Geometry Types"](https://dev.epicgames.com/documentation/en-us/unreal-engine/groom-platform-support-in-unreal-engine) above).
- The **Guides Cache** is supported on all platforms.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "To learn more about the grooms cache and its function, see <a data-document-id=\"3223442\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/using-groom-caches-with-hair-in-unreal-engine\">Groom Caches</a>.",
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

## Known Platform Limitations

- Frame rate depends on several factors, such as the size of the groom, the resolution of the groom, and the hardware on which the groom is being run. For example, you should expect a 30Hz or higher framerate with a NVIDIA RTX-2090Ti GPU for a human-like groom rendered at 1080p. Higher quality settings will result in a significant performance drop.
- Depth of Field is supported but may produce some artifacts.
- Grooms rendered with the [Path Tracer](building-virtual-worlds\lighting-and-shadows\ray-tracing-and-path-tracing\path-tracer) have a different appearance than the rasterizer's output.
- Grooms do not yet support proper precomputed lighting (Static or Stationary).
