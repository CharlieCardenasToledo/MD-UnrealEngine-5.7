# Reordering and Hiding Properties

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/reordering-and-hiding-properties-in-details-panel-customizations-in-unreal-engine

> Application Version: 5.7

Details Panel Customizations can change the order in which properties appear in the Details Panel, as well as show or hide properties that wouldn't ordinarily be visible. This page provides instructions on how to show, hide, and reorder both properties and categories.

## Prerequisites

This page uses the [Details Panel Quickstart](https://dev.epicgames.com/documentation/en-us/unreal-engine/details-panel-quickstart-guide-for-unreal-engine) tutorial as the basis for its examples and refers to the following:

- FCustomDataProperty – A custom struct consisting of the following: TSoftObjectPtr<UTexture> CustomTexture FName CustomName FString CustomString Int32 CustomInt
- ACustomActor – A simple Actor with the following added properties: TSoftObjectPtr<UStaticMesh> CustomMesh float CustomFloat bool CustomBool FCustomDataProperty CustomData
- FCustomDataPropertyCustomization – A Property Type Customization for FCustomDataProperty.
- FCustomClassDetailsCustomization – A Detail Customization for ACustomActor.

You should also review [Refreshing the Details Panel](https://dev.epicgames.com/documentation/en-us/unreal-engine/refreshing-custom-details-panels-in-unreal-engine) if you want to show or hide details based on changes made by the user.

## Properties

### Reorder Properties

You can re-order properties by changing the order in which you make **AddProperty** calls. The Class Details customization in the [Details Panel Quickstart](https://dev.epicgames.com/documentation/en-us/unreal-engine/details-panel-quickstart-guide-for-unreal-engine) includes an example of re-ordering properties. The original property declarations for `ACustomActor` are as follows:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "CustomActorClass.h",
  "code_preview": "UPROPERTY(EditAnywhere)\n\tTSoftObjectPtr&lt;UStaticMesh&gt; CustomMesh;\n\n\tUPROPERTY(EditAnywhere)\n\tfloat CustomFloat;\n\n\tUPROPERTY(EditAnywhere)\n\tbool CustomBool;\n\n\tUPROPERTY(EditAnywhere)\n",
  "lines_of_code": 11,
  "id": 150552,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1NTIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyOToxMCswMDowMCJ9--52f77131eaff55115eb40550269ff19f0e311ec745430e3835501869345bc3a7",
  "settings": {
    "is_hidden": false
  }
}
```

Normally, CustomMesh and CustomFloat would appear first in the Details Panel. However, the `FCustomClassDetailsCustomization::CustomizeDetails` function adds them to the details panel as follows:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "CustomActorClassCustomization.h",
  "code_preview": "CustomCategory.AddProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomData));\n\tCustomCategory.AddProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomBool));\n\tCustomCategory.AddProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomMesh));\n\tCustomCategory.AddProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomFloat));",
  "lines_of_code": 4,
  "id": 150553,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1NTMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyOToxMCswMDowMCJ9--a25fd5b4578e8098e86757af7b9e68203d1d74ab9d122aa5e284ce25434a1e21",
  "settings": {
    "is_hidden": false
  }
}
```

This results in CustomData and CustomBool appearing first. Similarly, any other custom **Slate** elements will appear in the order that you add them.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you do not add a property in your <strong>Details Customization</strong>, it uses the default order and the default category for your actor. See <strong>Hide Properties</strong> below for information on how to avoid displaying properties.",
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

### Hide Properties

Use `IDetailCategoryBuilder::HideProperty` to selectively hide properties that would normally appear due to their UPROPERTY specifiers.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "CustomClassDetailsCustomization.cpp",
  "code_preview": "DetailBuilder.HideProperty(FCustomDataProperty::StaticStruct()-&gt;GetFName());",
  "lines_of_code": 1,
  "id": 150554,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1NTQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyOToxMCswMDowMCJ9--44fdc341371862acdd57abfebdda7c7d2605c2e5c6fede245956d46c09c55ac3",
  "settings": {
    "is_hidden": false
  }
}
```

## Categories

### Reorder Categories

Use `IDetailCategoryBuilder::SortCategories` to set the order your custom categories render in.

`IDetailCategoryBuilder::SortCategories` takes a delegate with the signature `void FunctionName (const TMap<FName, IDetailCategoryBuilder*>&)`. Any functions you use for this delegate must be static functions. The [TMap](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMap?application_version=5.5) is a map of all the categories added by your custom class. Once you fetch a category from it, use `IDetailCategoryBuilder::SetSortOrder` to change what order the categories appear in. `IDetailCategoryBuilder::SetSortOrder` always sorts from lowest to highest.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "CustomClassDetailsCustomization.h",
  "code_preview": "static void SortCustomDetailsCategories(const TMap&lt;FName, IDetailCategoryBuilder*&gt;&amp; AllCategoryMap);",
  "lines_of_code": 1,
  "id": 150555,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1NTUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyOToxMCswMDowMCJ9--5eee5e0369006200dc028121cd5ca83d35bd765d443fe467b26a921f1e2c0f9b",
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
  "title": "CustomClassDetailsCustomization.cpp",
  "code_preview": "//Custom details with two category names.\n\n\tvoid FCustomClassDetailsCustomization::CustomizeDetails(IDetailLayoutBuilder&amp; DetailBuilder)\n\t{\n\t\tIDetailCategoryBuilder&amp; CustomCategory = DetailBuilder.EditCategory(FName(&quot;Custom Settings&quot;));\n\t\tIDetailCategoryBuilder&amp; DataCategory = DetailBuilder.EditCategory(FName(&quot;Data&quot;));\n\t\tCustomCategory.AddProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomBool));\n\t\tCustomCategory.AddProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomMesh));\n\t\tDataCategory.AddProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomData));\n\t\tDataCategory.AddProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomFloat));\n",
  "lines_of_code": 20,
  "id": 150556,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1NTYsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyOToxMCswMDowMCJ9--cb8052724446a761102b824107569d5a416d152592084803e37eaed08bb2b0e0",
  "settings": {
    "is_hidden": false
  }
}
```

### Hide Categories

Use `IDetailCategoryBuilder::HideCategory` to hide an entire category. You can use categories you defined with UPROPERTY specifiers or one you defined as part of a detail customization. Provide the `FName` of the category.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "CustomClassDetailsCustomization.cpp",
  "code_preview": "void FCustomClassDetailsCustomization::CustomizeDetails(IDetailLayoutBuilder&amp; DetailBuilder)\n\t{\n\t\tFName CustomCategoryName = FName(&quot;Custom Settings&quot;);\n\t\tIDetailCategoryBuilder&amp; CustomCategory = DetailBuilder.EditCategory(CustomCategoryName);\n\t\tDetailBuilder.HideCategory(CustomCategoryName);\n\t}",
  "lines_of_code": 6,
  "id": 150557,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1NTcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyOToxMCswMDowMCJ9--22adcb746d95937f31c94b5fcf3ddf357a3058c265a635d3bf36e185c89ee34b",
  "settings": {
    "is_hidden": false
  }
}
```

### Advanced Categories

Use `IDetailCategoryBuilder::SetShowAdvanced` to designate a category to show only when you expand the **Advanced** section of the **Details Panel**.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "CustomClassDetailsCustomization.cpp",
  "code_preview": "void FCustomClassDetailsCustomization::CustomizeDetails(IDetailLayoutBuilder&amp; DetailBuilder)\n\t{\n\t\tFName CustomCategoryName = FName(&quot;Custom Settings&quot;);\n\t\tIDetailCategoryBuilder&amp; CustomCategory = DetailBuilder.EditCategory(CustomCategoryName);\n\t\tCustomCategory.SetShowAdvanced(true);\n\t}",
  "lines_of_code": 6,
  "id": 150558,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTA1NTgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODoyOToxMCswMDowMCJ9--83c464c3fbb4af0fdad9cb23baa6293e4214ae5bba01d8198f9f580ce8950b97",
  "settings": {
    "is_hidden": false
  }
}
```
