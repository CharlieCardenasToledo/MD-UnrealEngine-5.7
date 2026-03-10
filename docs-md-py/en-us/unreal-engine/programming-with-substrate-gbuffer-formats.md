# Programming with Substrate GBuffer Formats

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-with-substrate-gbuffer-formats

> Application Version: 5.7

Substrate introduces changes on how material data are gathered, processed, stored, and used for lighting. This page provides a quick overview of how the system works for programmers.

From an authoring point of view, a material can continue to use the existing root node’s inputs, or use [Substrate Material Nodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine#substrate-material-nodes) (Slabs, Operators) and plug them into the root node’s **Front Material** input. Inside a material shader, this is translated by `TEMPLATE_USES_SUBSTRATE==0` in the former case, `TEMPLATE_USES_SUBSTRATE==1` in the latter case.

When using deferred lighting, the material data is stored into an intermediate storage, called **GBuffer**. Substrate comes with two GBuffer storage modes:

- **Blendable GBuffer:** This is similar to the existing GBuffer storage format.
- **Adaptive GBuffer:** This storage is changed into a bitstream of data, whose format changes from pixel to pixel.

This GBuffer format is configured in the project settings and depends on whether the intended target platform supports Adaptive GBuffer or not.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "For more information on GBuffer and its usage with Substrate, see the “GBuffer” section of the <a data-document-id=\"4596302\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine\">Substrate Materials Overview.</a>",
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

## Scene Texture Data

Scene texture data continues to be queried with `SceneTextureLookup()` for both **Blendable GBuffer** and **Adaptive GBuffer** formats. When using Adaptive GBuffer, this function will only return the first closure data.

## Global Shader

When data needs to be accessed in a global shader, in deferred rendering (for example, for lighting purposes), you need to declare and bind the Substrate global parameter like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "Declaration",
  "code_preview": "class FMyGlobasShaderCS : public FGlobalShader\n{\n  DECLARE_SHADER_TYPE(FMyGlobasShaderCS, Global)\n  SHADER_USE_PARAMETER_STRUCT(FMyGlobasShaderCS, FGlobalShader);\n  using FPermutationDomain = TShaderPermutationDomain&lt;&gt;;\n  BEGIN_SHADER_PARAMETER_STRUCT(FParameters, )\n   ...\n   SHADER_PARAMETER_RDG_UNIFORM_BUFFER(FSubstrateGlobalUniformParameters, Substrate)\n   ...\n  END_SHADER_PARAMETER_STRUCT()\n",
  "lines_of_code": 11,
  "id": 135314,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzUzMTQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMDowNyswMDowMCJ9--c88b1c37d490672bd19e62928f13c829bcdb93d18f38ec23a6e74d921c7927b1",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "Shader Parameter Binding",
  "code_preview": "FMyGlobasShaderCS::FParameters PassParameters;\nPassParameters.Substrate = Substrate::BindSubstrateGlobalUniformParameters(View);",
  "lines_of_code": 2,
  "id": 135315,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzUzMTUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMDowNyswMDowMCJ9--86bcc70edaf647bcc17242daa53b60f713e8accaae62e1e9758b949e68fe0b81",
  "settings": {
    "is_hidden": false
  }
}
```

In the shader, both Blendable and Adaptive GBuffer formats need to be handled.

```json
{
  "type": "callout",
  "callout_type": "info",
  "blocks": [
    {
      "type": "paragraph",
      "content": "A better abstraction is planned for a future release to ease maintenance.",
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

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "#if SUBSTRATE_LOAD_FROM_MATERIALCONTAINER\n// For Adaptive GBuffer\nFSubstrateAddressing Addressing = GetSubstratePixelDataByteOffset(PixelPos, uint2(View.BufferSizeAndInvSize.xy), Substrate.MaxBytesPerPixel);\nFSubstratePixelHeader Header = UnpackSubstrateHeaderIn(Substrate.MaterialTextureArray, Addressing, Substrate.TopLayerTexture);\n#else\n// For Blendable GBuffer\nFSubstrateGBufferBSDF Data = SubstrateReadGBufferBSDF(GetScreenSpaceDataUint(PixelPos));\n#endif\n\n\n",
  "lines_of_code": 22,
  "id": 135316,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzUzMTYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMDowNyswMDowMCJ9--7d7bf99e0e5148ae8ddae258df46c7b3d5d491b1ad8b9f4d8ff8b415da9bc438",
  "settings": {
    "is_hidden": false
  }
}
```

## Material Shader

In a material shader, if the material has its **Front Material** input plugged in, `TEMPLATE_USES_SUBSTRATE==1` will be defined, and the closure data can be processed and retrieved like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Initialise a Substrate header with normal in registers\nFSubstrateData SubstrateData = PixelMaterialInputs.GetFrontSubstrateData();\nFSubstratePixelHeader Header = MaterialParameters.GetFrontSubstrateHeader();\nHeader.IrradianceAO.MaterialAO = GetMaterialAmbientOcclusion(PixelMaterialInputs);\n\nif (Header.SubstrateTree.BSDFCount &gt; 0)\n{\n   FSubstrateIntegrationSettings Settings = InitSubstrateIntegrationSettings(false, true, 0, false);\n   float3 TotalTransmittancePreCoverage = 0;\n   Header.SubstrateUpdateTree(SubstrateData, V, Settings, TotalCoverage, TotalTransmittancePreCoverage);\n",
  "lines_of_code": 23,
  "id": 135317,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzUzMTcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMDowNyswMDowMCJ9--407b45ea7e4aed318cbda09f8c0c0fe5016c4040d5a026f1d52f91fbc1cbe307",
  "settings": {
    "is_hidden": false
  }
}
```

For materials not using Substrate nodes, such as the legacy root node inputs, TEMPLATE\_USES\_SUBSTRATE==0 will be defined and the data can be retrieved as usual like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "float3 BaseColor = GetMaterialBaseColor(PixelMaterialInputs);\nfloat Metallic = GetMaterialMetallic(PixelMaterialInputs);\n...",
  "lines_of_code": 3,
  "id": 135318,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzUzMTgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMDowNyswMDowMCJ9--6c6a256ce314f6c6c6627db46f6f83f719f8952a80e26bb81e12065ce7f126e9",
  "settings": {
    "is_hidden": false
  }
}
```

## Material Properties

Once a BSDFContext has been retrieved (see code above), you can access the closure data like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "SLAB_DIFFUSEALBEDO(BSDFContext.BSDF)\nSLAB_F0(BSDFContext.BSDF);\nSLAB_ROUGHNESS(BSDFContext.BSDF)",
  "lines_of_code": 3,
  "id": 135319,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzUzMTksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMDowNyswMDowMCJ9--27106342cd4f380a90adb0a0cd5b01418a77c6974b04de6b2e77678f8a117aee",
  "settings": {
    "is_hidden": false
  }
}
```

## Lighting Evaluation

For evaluating a particular light with **deferred lighting**, the following function can be used, located in `Substrate\SubstrateDeferredLighting.ush`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "FSubstrateDeferredLighting SubstrateDeferredLighting(...)",
  "lines_of_code": 1,
  "id": 135320,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzUzMjAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMDowNyswMDowMCJ9--baacf67e2a576ebc4a70fdfbd0701c691c5bee26c858947073161b483c7f08e4",
  "settings": {
    "is_hidden": false
  }
}
```

For evaluating the entire lighting in **forward rendering**, the following function can be used located in `Substrate\SubstrateForwardLighting.ush`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "float3 SubstrateForwardLighting(...)",
  "lines_of_code": 1,
  "id": 135321,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzUzMjEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMDowNyswMDowMCJ9--c1d5dd789e5894fca047675c01ef67d9f038b0936e31084da1390e1265bcc2f7",
  "settings": {
    "is_hidden": false
  }
}
```

Additionally, two useful functions for evaluation respectively analytical lights and environment lighting, located in `Substrate/SubstrateEvaluation.ush`:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "// Analytical lighting\nFSubstrateEvaluateResult SubstrateEvaluateBSDFCommon(...);\n\n// Environment lighting\nFSubstrateEnvLightResult SubstrateEvaluateForEnvLight(...);",
  "lines_of_code": 5,
  "id": 135322,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMzUzMjIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyMDowNyswMDowMCJ9--7aa0034989276237dcde06419c9423e4ccea4cd451f0a4a16e79056269ec156c",
  "settings": {
    "is_hidden": false
  }
}
```

## Shader Files

Here is a list of commonly used shader files:

```json
{
  "type": "callout",
  "callout_type": "alert",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The current shader API is subject to change in future releases. ",
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

| Shader Files | Description |
| --- | --- |
| `Substrate/Substrate.ush` | Contains Substrate’s core data structs, data accessors, as well as data reading for Adaptive GBuffer. |
| `Substrate/SubstrateRead.ush` | Contains reading / unpacking logic for Blendable GBuffer data. |
| `Substrate/SubstrateEvaluation.ush` | Contains main shading evaluation logic for analytical light and environment light. |
| `Substrate/SubstrateDeferredLighting.ush` | Contains shading evaluation for the deferred lighting path. |
| `Substrate/SubstrateForwardLighting.ush` | Contains the shading evaluation for forward lighting path. |

## Additional Resources

- Technical presentation of Substrate: [Siggraph 2023 - Unreal Engine Substrate: Authoring Materials That Matter](https://advances.realtimerendering.com/s2023/2023%20Siggraph%20-%20Substrate.pdf)
- Authoring presentation of Substrate: Unreal Fest 2025 Stockholm - Everything You Wanted to Know About Substrate
