# Materials

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-materials

> Application Version: 5.7

**Materials** in Unreal Engine define the surface properties of the objects in your scene. In the broadest sense, you can think of a Material as the "paint" that is applied to a mesh to control its visual appearance.

In more technical terms, Materials tell the render engine exactly how a surface should interact with the light in your scene. Materials define every aspect of the surface including color, reflectivity, bumpiness, transparency, and so on. These calculations are done using data that is input to the Material from a variety of images (textures) and node-based **Material expressions**, as well as from various [property settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-properties) inherent to the Material itself.

## Getting Started

Material creation is a broad topic, and the node-based workflow allows you to create an almost infinite variety of surface types. Beginners are recommended to start with with the pages linked in this section. The Essential Material Concepts and Physically Based Materials pages introduce the theory and ideas that form the foundation of Material creation in Unreal. The Material Editor User Guide is a set of tool-based documentation that teaches practical aspects of using the Material Editor.

- [Related Document](en-us/unreal-engine/essential-unreal-engine-material-concepts.md)

- [Related Document](en-us/unreal-engine/designing-visuals-rendering-and-graphics-with-unreal-engine.md)

- [Related Document](en-us/unreal-engine/physically-based-materials-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/unreal-engine-material-editor-user-guide.md)

- [Related Document](en-us/unreal-engine/unreal-engine-material-properties.md)

- [Related Document](en-us/unreal-engine/material-inputs-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/material-data-types-in-unreal-engine.md)

## Substrate Material Framework

- Related Document

- Related Document

- [Related Document](en-us/unreal-engine/substrate-materials-in-unreal-engine.md)

## Material Workflow Concepts

Once you understand the basic principles behind Material creation, the documents in this section are strongly recommended as a next step. **Material Instances** and **Material Functions** are foundational topics in Material creation, and help you optimize your workflow to save time and avoid doing the same work twice. Material Instances allow you or other artists on your team to quickly and easily customize Materials to produce multiple variations (or instances) from a single parent Material. Material Functions allow you to package parts of a Material graph into a single node, and share it to a common library for reuse in other Materials.

- [Related Document](en-us/unreal-engine/instanced-materials-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/material-functions-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/layering-materials-in-unreal-engine.md)

## Tutorials Index

The pages in this section are step-by-step, project based documents that walk you through some specific aspect of Material creation in Unreal. For example: [Animating UV Coordinates](https://dev.epicgames.com/documentation/en-us/unreal-engine/animating-uv-coordinates-in-unreal-engine), or [Using Texture Masks](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-texture-masks-in-unreal-engine).

- [Related Document](en-us/unreal-engine/unreal-engine-materials-tutorials.md)

## Material Reference Pages

The [Material Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-editor-user-guide) provides dozens of **Material Expressions** and **Functions**, each meant to perform some specific task in your Material graph. If you are looking for information about how and when to use a specific node, start with the pages linked below. The Material Expression and Function reference pages are organized according to their categories in the Materials palette — for example, Blends, Gradients, Math, Coordinates, and so on.

- [Related Document](en-us/unreal-engine/unreal-engine-material-expressions-reference.md)

- [Related Document](en-us/unreal-engine/unreal-engine-material-functions-reference.md)

- [Related Document](en-us/unreal-engine/unreal-engine-material-editor-ui.md)

- [Related Document](en-us/unreal-engine/unreal-engine-material-instance-editor-ui.md)

## Additional Concepts and Tools

Materials pages that do not fit more precisely into another category are found below. Many of these are intermediate to advanced topics that allow you to progress beyond the basics of Material creation and begin to develop more sophisticated Materials for your projects.

- [Related Document](en-us/unreal-engine/bent-normal-maps-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/bump-mapping-without-tangent-space-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/curve-atlases-in-unreal-engine-materials.md)

- [Related Document](en-us/unreal-engine/customized-uvs-in-unreal-engine-materials.md)

- [Related Document](en-us/unreal-engine/unreal-engine-material-analyzer-tool.md)

- [Related Document](en-us/unreal-engine/refraction-using-pixel-normal-offset-in-unreal-engine.md)

- [Related Document](en-us/unreal-engine/storing-custom-data-in-unreal-engine-materials-per-primitive.md)

- [Related Document](en-us/unreal-engine/lit-translucency-in-unreal-engine.md)
