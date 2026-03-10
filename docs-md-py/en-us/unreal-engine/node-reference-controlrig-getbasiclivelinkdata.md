# Get Basic LiveLink Data

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetBasicLiveLinkData

> Application Version: 5.7

### Description

Evaluate current Live Link Basic float property data associated with supplied subject

### Information

|  |  |
| --- | --- |
| Plugin | [LiveLinkControlRig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/LiveLinkControlRig) |
| Category | Live Link |
| Type | [FRigUnit\_LiveLinkEvaluateBasicValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/LiveLinkControlRig/FRigUnit_LiveLinkEvaluateBasicVa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SubjectName | The name of the subject to evaluate | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| PropertyName | The name of the property to evaluate | [FName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The resulting value of the evaluated property | [float](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
