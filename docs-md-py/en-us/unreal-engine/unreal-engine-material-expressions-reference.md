# Material Expressions Reference

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-expressions-reference

> Application Version: 5.7

This page is a reference index for all **Material expression** nodes available in the [Material Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-editor-user-guide). Material Expressions are the building blocks for creating fully functional Materials in Unreal Engine.

Each Material expression is a self-contained black box that either outputs a set of one or more specific values, or performs a single operation on one or more inputs and then outputs the results of that operation.

## Parameters

Certain Material expressions are parameters, meaning you can modify their values (dynamically during runtime in some cases) in a [Material Instance](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine) of the base material containing the parameter.

You should assign all parameters a unique name using the **Parameter Name** details property. This name is used to identify each specific parameter when you edit an instance in the [Material Instance Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui).

If two parameters of the same type have the same name within a Material, they are treated as the same parameter. Changing the value of one parameter in the Material Instance would change the value of both parameter expressions in the Material. You can set a default value for your parameters in the Details Panel. This default value is used in the Material Instance unless it is overridden and modified there.

## Material Expression Properties

All Material Expression nodes contain the same properties that provide different kinds of information. Below, we use a Texture Sample node to highlight these
on properties.

![Material Expression breakdown](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3074e534-51cc-4eff-ab1b-bcecee78b539/multiply-node.png)

| Number | Property Name | Description |
| --- | --- | --- |
| 1 | Description | All materials expressions have a common **Desc** (Description) property, which is accessible from the Details Panel. Any text entered into this in this property displays in the Material Editor just above the expression in the workspace. It can be used for any purpose, but usually serves as a good way to leave short notes about the purpose or function of the expression. |
| 2 | Title bar | Displays the name and/or pertinent information about the the Material Expression. |
| 3 | Inputs | Links to any values used by the Material Expression. |
| 4 | Outputs | Links that output the results of the Material Expression operation. |
| 5 | Preview | Displays a preview of the values that are output by the Material Expression. This updates automatically when realtime update is enabled and can be manually updated using the Spacebar. |

### Material Expression Types

These reference pages are organized according to the categories in the Material Editor palette.

















## Expression Index

This is a reference list of many, but not all, Material Expressions. All links shown here can also be accessed through the Expression Types pages listed above.
Additionally, you can use **Ctrl+F** to find the expression node you need and follow the link to its description.

[**Atmosphere**](https://dev.epicgames.com/documentation/en-us/unreal-engine/atmosphere-material-expressions-in-unreal-engine)

* [AtmosphericFogColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/atmosphere-material-expressions-in-unreal-engine#atmosphericfogcolor)

[**Color**](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine)

* [Desaturation](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#desaturation)

[**Constants**](https://dev.epicgames.com/documentation/en-us/unreal-engine/constant-material-expressions-in-unreal-engine)

* [Constant](https://dev.epicgames.com/documentation/en-us/unreal-engine/constant-material-expressions-in-unreal-engine#constant)
* [Constant2Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/constant-material-expressions-in-unreal-engine#constant2vector)
* [Constant3Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/constant-material-expressions-in-unreal-engine#constant3vector)
* [Constant4Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/constant-material-expressions-in-unreal-engine#constant4vector)
* [DistanceCullFade](https://dev.epicgames.com/documentation/en-us/unreal-engine/constant-material-expressions-in-unreal-engine#distancecullfade)
* [PerInstanceFadeAmount](https://dev.epicgames.com/documentation/en-us/unreal-engine/constant-material-expressions-in-unreal-engine#perinstancefadeamount)
* [PerInstanceRandom](https://dev.epicgames.com/documentation/en-us/unreal-engine/constant-material-expressions-in-unreal-engine#perinstancerandom)
* [Time](https://dev.epicgames.com/documentation/en-us/unreal-engine/constant-material-expressions-in-unreal-engine#time)
* [TwoSidedSign](https://dev.epicgames.com/documentation/en-us/unreal-engine/constant-material-expressions-in-unreal-engine#twosidedsign)
* [VertexColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/constant-material-expressions-in-unreal-engine#vertexcolor)

[**Coordinates**](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine)

* [ActorPositionWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine#actorpositionws)
* [CameraPositionWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine#camerapositionws)
* [LightmapUVs](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine#lightmapuvs)
* [ObjectOrientation](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine#objectorientation)
* [ObjectPositionWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine#objectpositionws)
* [ObjectRadius](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine#objectradius)
* [Panner](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine#panner)
* [ParticlePositionWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine#particlepositionws)
* [PixelNormalWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine#pixelnormalws)
* [Rotator](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine#rotator)
* [SceneTexelSize](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine#scenetexelsize)
* [ScreenPosition](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine#screenposition)
* [TextureCoordinate](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine#texturecoordinate)
* [VertexNormalWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine#vertexnormalws)
* [ViewSize](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine#viewsize)
* [WorldPosition](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinates-material-expressions-in-unreal-engine#worldposition)

[**Custom**](https://dev.epicgames.com/documentation/en-us/unreal-engine/custom-material-expressions-in-unreal-engine)

* [Custom](https://dev.epicgames.com/documentation/en-us/unreal-engine/custom-material-expressions-in-unreal-engine)

[**Depth**](https://dev.epicgames.com/documentation/en-us/unreal-engine/depth-material-expressions-in-unreal-engine)

* [DepthFade](https://dev.epicgames.com/documentation/en-us/unreal-engine/depth-material-expressions-in-unreal-engine#depthfade)
* [PixelDepth](https://dev.epicgames.com/documentation/en-us/unreal-engine/depth-material-expressions-in-unreal-engine#pixeldepth)
* [SceneDepth](https://dev.epicgames.com/documentation/en-us/unreal-engine/depth-material-expressions-in-unreal-engine#scenedepth)

[**Font**](https://dev.epicgames.com/documentation/en-us/unreal-engine/font-material-expressions-in-unreal-engine)

* [FontSample](https://dev.epicgames.com/documentation/en-us/unreal-engine/font-material-expressions-in-unreal-engine#fontsample)
* [FontSampleParameter](https://dev.epicgames.com/documentation/en-us/unreal-engine/font-material-expressions-in-unreal-engine#fontsampleparameter)

[**Functions**](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-function-expressions-in-unreal-engine)

* [FunctionInput](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-function-expressions-in-unreal-engine#functioninput)
* [FunctionOutput](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-function-expressions-in-unreal-engine#functionoutput)
* [MaterialFunctionCall](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-function-expressions-in-unreal-engine#materialfunctioncall)
* [StaticBool](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-function-expressions-in-unreal-engine#staticbool)
* [StaticSwitch](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-function-expressions-in-unreal-engine#staticswitch)
* [TextureObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-function-expressions-in-unreal-engine#textureobject)

[**MaterialAttributes**](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-attributes-expressions-in-unreal-engine)

* [BreakMaterialAttributes](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-attributes-expressions-in-unreal-engine#breakmaterialattributes)
* [MakeMaterialAttributes](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-attributes-expressions-in-unreal-engine#makematerialattributes)

[**Math**](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine)

* [Abs](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#abs)
* [Add](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#add)
* [AppendVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#appendvector)
* [Ceil](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#ceil)
* [Clamp](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#clamp)
* [ComponentMask](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#componentmask)
* [Cosine](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#cosine)
* [CrossProduct](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#crossproduct)
* [Divide](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#divide)
* [DotProduct](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#dotproduct)
* [Floor](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#floor)
* [Fmod](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#fmod)
* [Frac](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#frac)
* [If](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#if)
* [LinearInterpolate](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#linearinterpolate)
* [Multiply](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#multiply)
* [Normalize](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#normalize)
* [OneMinus](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#oneminus)
* [Power](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#power)
* [Sine](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#sine)
* [SquareRoot](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#squareroot)
* [Subtract](https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-expressions-in-unreal-engine#subtract)

[**Parameters**](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine)

* [CollectionParameters](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine#collectionparameters)
* [DynamicParameter](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine#dynamicparameter)
* [FontSampleParameter](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine#fontsampleparameter)
* [ScalarParameter](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine#scalarparameter)
* [StaticBoolParameter](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine#staticboolparameter)
* [StaticSwitchParameter](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine#staticswitchparameter)
* [StaticComponentMaskParameter](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine#staticcomponentmaskparameter)
* [VectorParameter](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine#vectorparameter)
* [TextureObjectParameter](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine#textureobjectparameter)
* [TextureSampleParameter2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine#texturesampleparameter2d)
* [TextureSampleParameterSubUV](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine#texturesampleparametersubuv)
* [TextureSampleParameterCube](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine#texturesampleparametercube)
* [TextureSampleParameterMovie](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine#texturesampleparametermovie)

[**Particles**](https://dev.epicgames.com/documentation/en-us/unreal-engine/particle-material-expressions-in-unreal-engine)

* [DynamicParameter](https://dev.epicgames.com/documentation/en-us/unreal-engine/particle-material-expressions-in-unreal-engine#dynamicparameter)
* [ParticleColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/particle-material-expressions-in-unreal-engine#particlecolor)
* [ParticleDirection](https://dev.epicgames.com/documentation/en-us/unreal-engine/particle-material-expressions-in-unreal-engine#particledirection)
* [ParticleMacroUV](https://dev.epicgames.com/documentation/en-us/unreal-engine/particle-material-expressions-in-unreal-engine#particlemacrouv)
* [ParticleMotionBlurFade](https://dev.epicgames.com/documentation/en-us/unreal-engine/particle-material-expressions-in-unreal-engine#particlemotionblurfade)
* [ParticlePositionWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/particle-material-expressions-in-unreal-engine#particlepositionws)
* [ParticleRadius](https://dev.epicgames.com/documentation/en-us/unreal-engine/particle-material-expressions-in-unreal-engine#particleradius)
* [ParticleRelativeTime](https://dev.epicgames.com/documentation/en-us/unreal-engine/particle-material-expressions-in-unreal-engine#particlerelativetime)
* [ParticleSize](https://dev.epicgames.com/documentation/en-us/unreal-engine/particle-material-expressions-in-unreal-engine#particlesize)
* [ParticleSpeed](https://dev.epicgames.com/documentation/en-us/unreal-engine/particle-material-expressions-in-unreal-engine#particlespeed)
* [SphericalParticleOpacity](https://dev.epicgames.com/documentation/en-us/unreal-engine/particle-material-expressions-in-unreal-engine#sphericalparticleopacity)
* [ParticleSubUV](https://dev.epicgames.com/documentation/en-us/unreal-engine/particle-material-expressions-in-unreal-engine#particlesubuv)
* [TextureSampleParameterSubUV](https://dev.epicgames.com/documentation/en-us/unreal-engine/particle-material-expressions-in-unreal-engine#texturesampleparametersubuv)

[**Terrain**](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-material-expressions-in-unreal-engine)

* [LandscapeLayerBlend](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-material-expressions-in-unreal-engine#landscapelayerblend)
* [LandscapeLayerCoords](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-material-expressions-in-unreal-engine#landscapelayercoords)
* [LandscapeLayerSwitch](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-material-expressions-in-unreal-engine#landscapelayerswitch)

[**Texture**](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-material-expressions-in-unreal-engine)

* [FontSample](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-material-expressions-in-unreal-engine#fontsample)
* [FontSampleParameter](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-material-expressions-in-unreal-engine#fontsampleparameter)
* [SceneColor](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-material-expressions-in-unreal-engine#scenecolor)
* [TextureObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-material-expressions-in-unreal-engine#textureobject)
* [TextureSample](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-material-expressions-in-unreal-engine#texturesample)

[**Utility**](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine)

* [BlackBody](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#blackbody)
* [BumpOffset](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#bumpoffset)
* [ConstantBiasScale](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#constantbiasscale)
* [DDX](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#ddx)
* [DDY](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#ddy)
* [DepthFade](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#depthfade)
* [DepthOfFieldFunction](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#depthoffieldfunction)
* [Desaturation](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#desaturation)
* [Distance](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#distance)
* [Fresnel](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#fresnel)
* [LightmassReplace](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#lightmassreplace)
* [LinearInterpolate](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#linearinterpolate)
* [Noise](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#noise)
* [QualitySwitch](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#qualityswitch)
* [RotateAboutAxis](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#rotateaboutaxis)
* [SphereMask](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#spheremask)
  \*[Thin Translucent](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#thintranslucent)
* [AntialiasedTextureMask](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#antialiasedtexturemask)

[**VectorOps**](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-operation-material-expressions-in-unreal-engine)

* [AppendVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-operation-material-expressions-in-unreal-engine#appendvector)
* [ComponentMask](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-operation-material-expressions-in-unreal-engine#componentmask)
* [CrossProduct](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-operation-material-expressions-in-unreal-engine#crossproduct)
* [DeriveNormalZ](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-operation-material-expressions-in-unreal-engine#derivenormalz)
* [DotProduct](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-operation-material-expressions-in-unreal-engine#dotproduct)
* [Normalize](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-operation-material-expressions-in-unreal-engine#normalize)
* [Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-operation-material-expressions-in-unreal-engine#transform)
* [TransformPosition](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-operation-material-expressions-in-unreal-engine#transformposition)

[**Vectors**](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine)

* [ActorPositionWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine#actorpositionws)
* [CameraPositionWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine#camerapositionws)
* [CameraVectorWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine#cameravectorws)
* [Constant2Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine#constant2vector)
* [Constant3Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine#constant3vector)
* [Constant4Vector](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine#constant4vector)
* [LightVector](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine#lightvector)
* [ObjectBounds](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine#objectbounds)
* [ObjectOrientation](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine#objectorientation)
* [ObjectPositionWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine#objectpositionws)
* [ParticlePositionWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine#particlepositionws)
* [PixelNormalWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine#pixelnormalws)
* [ReflectionVectorWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine#reflectionvectorws)
* [VertexNormalWS](https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-material-expressions-in-unreal-engine#vertexnormalws)
