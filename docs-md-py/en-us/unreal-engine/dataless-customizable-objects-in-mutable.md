# Dataless Customizable Objects in Mutable

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/dataless-customizable-objects-in-mutable

> Application Version: 5.7

A **Dataless Customizable Object** is a normal **Customizable Object** whose input nodes are in-game changeable **Parameter Nodes**.

You can convert any Customizable Object to dataless by replacing the following nodes:

| Constant Nodes | Parameter Nodes |
| --- | --- |
| Texture Node | Texture Parameter Node |
| Skeletal Mesh Node | Skeletal Mesh Parameter Node |
| Material Node | Material Parameter Node |
| Table Node | T / SK / M Node |

It is not a requirement to replace all nodes. You can mix and match Constant and Parameter nodes. In short, you will only take advantage of dataless on those inputs which are Parameter nodes.

### Improvements Over Customizable Objects

- **Faster compilation time**: Inputs from Parameter nodes are not compiled, instead they are converted at runtime.
- **Encryption**: Now encryption works out of the box. Since inputs are no longer compiled (they are normal **UObjects**), they can now be encrypted as usual.
- **Regular UE workflow**: With the old Constant nodes, you had to keep in mind that meshes and parameters would be embedded in the Customizable Object in a special cook process, and the original assets would be editor-only. With the new dataless system, it works just like any other UE system-like materials.
- **Possibly smaller packages**: Previously if an input was referenced outside of Mutable, it was included in the package twice: once as a compiled **Mutable Resource** and once as a UObject, which is why it wasn’t recommended. Since Parameter inputs are no longer compiled, this is no longer the case.

### Limitations

- **Less performant**: Runtime conversions and some optimizations, like generating constants, cannot be applied at compilation time.
- **No available options**: Input parameters do not have a list of available options. This means that gameplay programmers are now responsible for restricting which inputs can be passed in the parameters.

## New Parameters

As regular parameters, the new **Texture**, **Skeletal Mesh** and **Material Parameters** can be set by creating a **Customizable Object Instance** and calling the following functions (Blueprint or C++):

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UFUNCTION(BlueprintCallable, Category = CustomizableObjectInstance)\nvoid SetTextureParameterSelectedOption(\n    const FString&amp; TextureParamName,\n    UTexture* TextureValue);\n",
  "lines_of_code": 4,
  "id": 109283,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDkyODMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxNTo1NyswMDowMCJ9--ba5b5b229f159b7fa841faff430b363c94e6f54b7f03cbe5efcb224016f09c4f",
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
  "code_preview": "UFUNCTION(BlueprintCallable, Category = CustomizableObjectInstance)\nvoid SetSkeletalMeshParameterSelectedOption(\n    const FString&amp; SkeletalMeshParamName,\n    USkeletalMesh* SkeletalMeshValue);\n",
  "lines_of_code": 4,
  "id": 109284,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDkyODQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxNTo1NyswMDowMCJ9--0d40da4de269b69f77b31a105292beb260963c602d6244adad26a8c1f2e5e97b",
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
  "code_preview": "UFUNCTION(BlueprintCallable, Category = CustomizableObjectInstance)\nvoid SetMaterialParameterSelectedOption(\n    const FString&amp; MaterialParamName,\n    UMaterialInterface* MaterialValue);\n",
  "lines_of_code": 4,
  "id": 109285,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDkyODUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxNTo1NyswMDowMCJ9--80991a4214839030ff6c92465a2f71c2f6bcc8fdc5f7b0d0f6d1115435ebbacb",
  "settings": {
    "is_hidden": false
  }
}
```

In addition, in each Parameter node you can specify a **Default Value**. This Default Value is optional and if it is not specified it will be nullptr. You can get these Default Values in the Customizable Object:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UFUNCTION(BlueprintCallable, Category = CustomizableObject)\nUTexture* GetTextureParameterDefaultValue(\n    const FString&amp; InParameterName) const;\n",
  "lines_of_code": 3,
  "id": 109286,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDkyODYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxNTo1NyswMDowMCJ9--2771ed928cc234311c5f5004cfa3a04dcd7716225b7e8225196a6454895ddb40",
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
  "code_preview": "UFUNCTION(BlueprintCallable, Category = CustomizableObject)\nUSkeletalMesh* GetSkeletalMeshParameterDefaultValue(\n    const FString&amp; ParameterName) const;\n",
  "lines_of_code": 3,
  "id": 109287,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDkyODcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxNTo1NyswMDowMCJ9--f49cbec92b3dd9d48b61e6399371f54468429a88a1b8879ca6f4c5721fb36a64",
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
  "code_preview": "UFUNCTION(BlueprintCallable, Category = CustomizableObject)\nUMaterialInterface* GetMaterialParameterDefaultValue(\n    const FString&amp; ParameterName) const;\n",
  "lines_of_code": 3,
  "id": 109288,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDkyODgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxNTo1NyswMDowMCJ9--cb490c3b9d6e64318a25e1bf12cdeb0c15b1927994222536ebdeb627c140ba69",
  "settings": {
    "is_hidden": false
  }
}
```

Keep in mind that if a Default Value is set, the referenced objects will be cooked. Also the lifecycle of these objects is the same as the Customizable Object since they are strong references.

Once all parameters have been set. To see the results, you need to call:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UFUNCTION(BlueprintCallable, Category = CustomizableObjectInstance)\nvoid UpdateSkeletalMeshAsync(\n    bool bIgnoreCloseDist = false,\n    bool bForceHighPriority = false);\n",
  "lines_of_code": 4,
  "id": 109289,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxMDkyODksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoxNTo1NyswMDowMCJ9--f5d8cb5ce735828a63f5f96e3dff598996445653b0fcd9aa3d32632ff4b9670d",
  "settings": {
    "is_hidden": false
  }
}
```

## Example

**Regular Nodes**: 
Skeletal Mesh references are shown in the **Reference Viewer** due to having an Editor-Only reference.

![Normal-constant-parameter-menu](https://dev.epicgames.com/community/api/documentation/image/1a7afecc-45e3-447b-91cd-780aa86c532b)

In a packaged game, they are not included as UObjects but as Mutable Resources:

![Skeletal-mesh-as-mutable-resources-in-Blueprints.](https://dev.epicgames.com/community/api/documentation/image/29012148-f677-4a53-85a7-f41ec9823dd6)

**Dataless Nodes**: 
Notice that only the Skeletal Mesh nodes have been converted to dataless.

![Dataless-parameter-menu.](https://dev.epicgames.com/community/api/documentation/image/a00bf35f-63c7-422c-9b4b-a50ad31f48ee)

The Material is still a constant (not a parameter):

![The-material-is-still-a-constant.](https://dev.epicgames.com/community/api/documentation/image/9b86684e-28c2-4492-b7bf-e4b6a6950169)
