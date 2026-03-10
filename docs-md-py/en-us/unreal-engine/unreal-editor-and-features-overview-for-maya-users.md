# Unreal Editor and Features Overview for Maya Users

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-editor-and-features-overview-for-maya-users

> Application Version: 5.7

If you’re moving from a full or partial Maya workflow to Unreal Engine, it can be challenging to translate familiar features that you rely on from one application to another. While both have similar functionalities in some areas, the ecosystem Unreal Engine provides and the way it’s organized differs from that of Maya, and other DCCs, in many ways.

This guide provides a walkthrough of how you would get started with Unreal Engine and its features and draw connections to Maya equivalents, where possible. The sections of this guide are broken up into many things you’d want to know as a first-time or casual user of Unreal Engine.

## What does it mean to make the switch to Unreal Engine for your Project?

![Image](https://dev.epicgames.com/community/api/documentation/image/9880b97f-1b11-4410-98cb-e60062838802)

- **An Unreal Engine Pipeline versus a Traditional Pipeline** In a traditional pipeline workflow, each department has its own assignment, such as lighting, look dev, rigging, character creation, and so on. When content is finished in one, it may go to the next to work on in isolation, which can lead to wasted time as the content each department generates can take time to get the right solution. Using a fully integrated Unreal Engine pipeline helps avoid round-trip workflows and import/export issues. It also makes collaboration between departments simpler when everyone is working in the same tool and in a WYSIWYG realtime editor.
- **Realtime Scene Updates versus a Global Timeline** In Maya, you have the main timeline that represents the overall time in a scene. You can place keys and go to a specific time. In Unreal Engine, you work in real-time without a dedicated timeline. Instead, there are dedicated tools, like Sequencer, where you’ll view a timeline and set keys to animate objects in the scene.
- **Working in Real-time versus Offline Rendering** In Maya, you can potentially wait minutes to hours for Arnold or V-Ray to render a single frame. In Unreal Engine, you can see the result in real-time.
- **Unreal Engine offers seamless asset integration** FBX, Alembic, and USD import pipelines preserve your work from Maya for geometry, rigging, and animations.
- **Built-in artist-friendly tools to replace traditional pipeline workflows** Unreal Engine includes a suite of tools to develop your projects from beginning to end. This can replace entire parts of a traditional offline pipeline with one that provides feedback in real-time as you make changes. There is no waiting to see the finished results. Unreal Engine also supports full animation workflow capabilities with Skeletal Mesh editing tools, rigging with Control Rig, the Animators Kit plugin, animation deformers, and more. With the engine’s material editor, post-process effects, particles and physics, you can create nearly any style and look for your project in an iterative and collaborative workflow with your teams. High-quality lighting systems with dynamic global illumination and reflections with cinematic quality shadowing that work without any additional setup.

## Terminology Alignment between Maya and Unreal Engine

Before you dive completely into learning Unreal Engine, let’s take a moment and look at terminology you may be familiar with in Maya and how that applies to Unreal Engine.

| Autodesk Maya | Unreal Engine |
| --- | --- |
| Scene File | Project |
| Channel Box / Attribute Editor | Details Panel |
| Outliner | Outliner / Animation Outliner |
| Referencing Characters / Assets | Instancing using the Content Browser |
| Timeline / Dope Sheet / Trax Editor | Sequencer |
| Scenes / Environment Sets | Levels |
| Animation Scene Files | Level Sequences |
| Graph Editor | Curve Editor |
| Hypershade | Material Editor |

## Topics

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "To learn about and familiarize yourself with Unreal Engine and it's features, explore the topics below. Ideally, you'd follow along with these in order from top to bottom, but each area can be explored and learned independently of other topic pages.",
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

- [Related Document](en-us/unreal-engine/unreal-editor-and-features-overview-for-maya-users.md)
