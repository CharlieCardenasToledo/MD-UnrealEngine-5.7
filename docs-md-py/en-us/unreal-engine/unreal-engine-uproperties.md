# Properties

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-uproperties

> Application Version: 5.7

## Property Declaration

Properties are declared using standard C++ variable syntax, preceded by the UPROPERTY macro which defines property metadata and variable specifiers.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UPROPERTY([specifier, specifier, ...], [meta(key=value, key=value, ...)])\n\tType VariableName;",
  "lines_of_code": 2,
  "id": 162537,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjI1MzcsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzozNzo1MSswMDowMCJ9--c244b05d346eed659b93e73c8a66b0ab9b2da57c51edf863642e9d570bf34a03",
  "settings": {
    "is_hidden": false
  }
}
```

## Core Data Types

### Integers

The convention for integral data types is "int" or "uint" followed by the size in bits.

| Variable Type | Description |
| --- | --- |
| **uint8** | 8-bit unsigned |
| **uint16** | 16-bit unsigned |
| **uint32** | 32-bit unsigned |
| **uint64** | 64-bit unsigned |
| **int8** | 8-bit signed |
| **int16** | 16-bit signed |
| **int32** | 32-bit signed |
| **int64** | 64-bit signed |

#### As Bitmasks

Integer properties can now be exposed to the Editor as bitmasks. To mark an integer property as a bitmask, just add "bitmask" to the meta section, as follows:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "/*~ BasicBits appears as a list of generic flags in the editor, instead of an integer field. */\n\tUPROPERTY(EditAnywhere, Meta = (Bitmask))\n\tint32 BasicBits;",
  "lines_of_code": 3,
  "id": 162538,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjI1MzgsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzozNzo1MSswMDowMCJ9--1c5eae1f67c44ddaf45e4a5ef40390bb669a92dc8699ca75ee01d0320f049e0a",
  "settings": {
    "is_hidden": false
  }
}
```

Adding this meta tag will cause the integer to be editable as a drop-down list of generically-named flags ("Flag 1", "Flag 2", "Flag 3", etc.) that can be
turned on or off individually.

![Image](https://dev.epicgames.com/community/api/documentation/image/2b1e1468-04f9-41fa-88ac-89282c9fa233)

You can also make integer parameters to Blueprint-callable functions behave as bitmasks, by adding the `Bitmask` meta tag (no value necessary) to a `UPARAM` Specifier for the parameter.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "/*~ You can set MyFunction using a generic list of flags instead of typing in an integer value. */\n\tUFUNCTION(BlueprintCallable)\n\tvoid MyFunction(UPARAM(meta=(Bitmask)) int32 BasicBitsParam)",
  "lines_of_code": 3,
  "id": 162539,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjI1MzksInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzozNzo1MSswMDowMCJ9--ab497d7767ae1c0842036b3b21f226f4576c27dadb0ea11ba5cc81d118028ce3",
  "settings": {
    "is_hidden": false
  }
}
```

In order to customize the bitflags' names, we must first create a UENUM with the "bitflags" meta tag:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UENUM(Meta = (Bitflags))\n\tenum class EColorBits\n\t{\n\t\tECB_Red,\n\t\tECB_Green,\n\t\tECB_Blue\n\t};",
  "lines_of_code": 7,
  "id": 162540,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjI1NDAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzozNzo1MSswMDowMCJ9--a50ae3e2ba84c7b11e9f2eab17805f01e12df0f6feae06119c92d831ed9858bf",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The supported value range for a bitmask enumerated type is 0 to 31, inclusive. This corresponds to the bits (starting at bit 0) of a 32-bit integer variable. In the example above, bit 0 is <code>ECB_Red</code>, bit 1 is <code>ECB_Green</code>, and bit 2 is <code>ECB_Blue</code>.",
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

As an alternate declaration style, you can use the `ENUM_CLASS_FLAGS` to turn your enumerated type into a bitmask after defining it. In order to use the flag selector in the editor, we must also add the meta field `UseEnumValuesAsMaskValuesInEditor` and set it to `true`. The key difference is that this method uses the mask values directly, instead of the bit numbers. The equivalent enumerated type, made using this method, would look like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UENUM(Meta = (Bitflags, UseEnumValuesAsMaskValuesInEditor = &quot;true&quot;))\n\tenum class EColorBits\n\t{\n\t\tECB_Red = 0x01,\n\t\tECB_Green = 0x02,\n\t\tECB_Blue = 0x04\n\t};\n\n\tENUM_CLASS_FLAGS(EColorBits);",
  "lines_of_code": 9,
  "id": 162541,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjI1NDEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzozNzo1MSswMDowMCJ9--cb4d17a11c3cc3087badf52f3cc198a2f3aed6cf2019f459218c6912eaff0ddc",
  "settings": {
    "is_hidden": false
  }
}
```

After creating this UENUM, we can reference it with the "BitmaskEnum" meta tag, like this:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "/*~ This property lists flags matching the names of values from EColorBits. */\n\tUPROPERTY(EditAnywhere, Meta = (Bitmask, BitmaskEnum = &quot;EColorBits&quot;))\n\tint32 ColorFlags;",
  "lines_of_code": 3,
  "id": 162542,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjI1NDIsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzozNzo1MSswMDowMCJ9--bc3e7ed231a6a26abc7fd79afed8bcf388bb00b04ade32817acba2d20c12952c",
  "settings": {
    "is_hidden": false
  }
}
```

Following this change, the bitflags listed in the drop-down box will take on the names and values of the enumerated class entries. In the example above, ECB\_Red
is value 0, meaning it will activate bit 0 (adding 1 to ColorFlags) when checked. ECB\_Green corresponds to bit 1 (adding 2 to ColorFlags), and ECB\_Blue
corresponds to bit 2 (adding 4 to ColorFlags).

![Image](https://dev.epicgames.com/community/api/documentation/image/e30b24de-da30-4d1d-8188-67b193b03c3d)

Similarly, you can add `BitmaskEnum` and the appropriate enumerated type name to the meta section of your `UPARAM` tag to customize it.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "/*~ MyOtherFunction shows flags named after the values from EColorBits. */\n\tUFUNCTION(BlueprintCallable)\n\tvoid MyOtherFunction(UPARAM(meta=(Bitmask, BitmaskEnum = &quot;EColorBits&quot;)) int32 ColorFlagsParam)",
  "lines_of_code": 3,
  "id": 162543,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjI1NDMsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzozNzo1MSswMDowMCJ9--8eb1e7392f2d91aa9f20c605d7390aadabd6993876351e78577eb4b335d8b3b8",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "While enumerated types can contain more than 32 entries, only the first 32 values will be visible in a bitmask association in the Property Editor UI. Similarly, while explicit-value entries are accepted, entries with explicit values not between 0 and 31 will not be included in the drop-down.",
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

### Floating Point Types

Unreal uses the standard C++ floating point types, float, and double.

### Boolean Types

Boolean types can be represented either with the C++ bool keyword or as a bitfield.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "uint32 bIsHungry : 1;\n\tbool bIsThirsty;",
  "lines_of_code": 2,
  "id": 162544,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjI1NDQsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzozNzo1MSswMDowMCJ9--7129285839d9917edc6e078381b726aa7a11a9a7dc5ffb0054e1f0a19fa966d2",
  "settings": {
    "is_hidden": false
  }
}
```

### Strings

Unreal Engine supports three core types of strings.

- FString is a classic "dynamic array of chars" string type.
- FName is a reference to an immutable case-insensitive string in a global string table. It is smaller and more efficient to pass around than an FString, but more difficult to manipulate.
- FText is a more robust string representation designed to handle localization.

For most uses, Unreal relies on the TCHAR type for characters. The TEXT() macro is available to denote TCHAR literals.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "MyDogPtr-&gt;DogName = FName(TEXT(&quot;Samson Aloysius&quot;));",
  "lines_of_code": 1,
  "id": 162545,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNjI1NDUsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxNzozNzo1MSswMDowMCJ9--517b1ac4b3a641e7a3b354e00d50a55d858baf2fbf97df16c6153b47882faa3c",
  "settings": {
    "is_hidden": false
  }
}
```

For more on the three string types, when to use each one, and how to work with them, see the [String Handling documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/string-handling-in-unreal-engine).

## Property Specifiers

```json
{
  "type": "include",
  "excerpt_id": 2728,
  "excerpt_assignment_id": 2685,
  "blocks": [
    {
      "type": "paragraph",
      "content": "When declaring properties, <strong>Property Specifiers</strong> can be added to the declaration to control how the property behaves with various aspects of the Engine and Editor.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "enhanced_table",
      "widths": [
        "38.4863%",
        "61.5137%"
      ],
      "rows": [
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Property Tag",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "Effect",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>AdvancedDisplay</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The property will be placed in the advanced (dropdown) section of any panel where it appears.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>AssetRegistrySearchable</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The <code>AssetRegistrySearchable</code> Specifier indicates that this property and its value will be automatically added to the Asset Registry for any Asset class instances containing this as a member variable.  It is not legal to use struct properties or parameters.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>BlueprintAssignable</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Usable with Multicast Delegates only. Exposes the property for assigning in Blueprints.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>BlueprintAuthorityOnly</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This property must be a Multicast Delegate. In Blueprints, it will only accept events tagged with <code>BlueprintAuthorityOnly</code>.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>BlueprintCallable</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Multicast Delegates only. Property should be exposed for calling in Blueprint code.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>BlueprintGetter=GetterFunctionName</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This property specifies a custom accessor function. If this property isn't also tagged with <code>BlueprintSetter</code> or <code>BlueprintReadWrite</code>, then it is implicitly <code>BlueprintReadOnly</code>.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>BlueprintReadOnly</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This property can be read by Blueprints, but not modified. This Specifier is incompatible with the <code>BlueprintReadWrite</code> Specifier.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>BlueprintReadWrite</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This property can be read or written from a Blueprint. This Specifier is incompatible with the <code>BlueprintReadOnly</code> Specifier.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>BlueprintSetter=SetterFunctionName</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This property has a custom mutator function, and is implicitly tagged with <code>BlueprintReadWrite</code>. Note that the mutator function must be named and part of the same class.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>Category=\"TopCategory\\|SubCategory\\|...\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the category of the property when displayed in Blueprint editing tools. Define nested categories using the | operator.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>Config</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This property will be made configurable. The current value can be saved to the <code>.ini</code> file associated with the class and will be loaded when created. Cannot be given a value in default properties. Implies <code>BlueprintReadOnly</code>.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>DuplicateTransient</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Indicates that the property's value should be reset to the class default value during any type of duplication (copy/paste, binary duplication, etc.).",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>EditAnywhere</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Indicates that this property can be edited by property windows, on archetypes and instances. This Specifier is incompatible with any of the \"Visible\" Specifiers.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>EditDefaultsOnly</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Indicates that this property can be edited by property windows, but only on archetypes. This Specifier is incompatible with any of the \"Visible\" Specifiers.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>EditFixedSize</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Only useful for dynamic arrays. This will prevent the user from changing the length of an array via the Unreal Editor property window.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>EditInstanceOnly</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Indicates that this property can be edited by property windows, but only on instances, not on archetypes. This Specifier is incompatible with any of the \"Visible\" Specifiers.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>Export</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Only useful for Object properties (or arrays of Objects). Indicates that the Object assigned to this property should be exported in its entirety as a subobject block when the Object is copied (such as for copy/paste operations), as opposed to just outputting the Object reference itself.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>GlobalConfig</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Works just like <code>Config</code> except that you cannot override it in a subclass. Cannot be given a value in default properties. Implies <code>BlueprintReadOnly</code>.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>Instanced</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Object (<code>UCLASS</code>) properties only. When an instance of this class is created, it will be given a unique copy of the Object assigned to this property in defaults. Used for instancing subobjects defined in class default properties. Implies <code>EditInline</code> and <code>Export</code>.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>Interp</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Indicates that the value can be driven over time by a Track in Sequencer.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>Localized</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The value of this property will have a localized value defined. Mostly used for strings. Implies <code>ReadOnly</code>.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>Native</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Property is native: C++ code is responsible for serializing it and exposing it to <a data-document-id=\"3227219\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-object-handling-in-unreal-engine\">Garbage Collection</a>.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>NoClear</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Prevents this Object reference from being set to none from the editor. Hides the clear (and browse) button in the editor.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>NoExport</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Only useful for native classes. This property should not be included in the auto-generated class declaration.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>NonPIEDuplicateTransient</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The property will be reset to the default value during duplication, except if it's being duplicated for a Play In Editor (PIE) session.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>NonTransactional</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Indicates that changes to this property's value will not be included in the editor's undo/redo history.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>NotReplicated</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Skip replication. This only applies to struct members and parameters in service request functions.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>Replicated</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The property should be replicated over the network.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>ReplicatedUsing=FunctionName</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The <code>ReplicatedUsing</code> Specifier specifies a callback function which is executed when the property is updated over the network.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>RepRetry</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Only useful for struct properties. Retry replication of this property if it fails to be fully sent (for example, Object references not yet available to serialize over the network). For simple references, this is the default, but for structs, this is often undesirable due to the bandwidth cost, so it is disabled unless this flag is specified.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>SaveGame</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This Specifier is a simple way to include fields explicitly for a checkpoint/save system at the property level. The flag should be set on all fields that are intended to be part of a saved game, and then a proxy archiver can be used to read/write it.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>SerializeText</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Native property should be serialized as text (<code>ImportText</code>, <code>ExportText</code>).",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>SkipSerialization</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This property will not be serialized, but can still be exported to a text format (such as for copy/paste operations).",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>SimpleDisplay</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Visible or editable properties appear in the <strong>Details</strong> panel and are visible without opening the \"Advanced\" section.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>TextExportTransient</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This property will not be exported to a text format (so it cannot, for example, be used in copy/paste operations).",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>Transient</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Property is transient, meaning it will not be saved or loaded. Properties tagged this way will be zero-filled at load time.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>VisibleAnywhere</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Indicates that this property is visible in all property windows, but cannot be edited. This Specifier is incompatible with the \"Edit\" Specifiers.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>VisibleDefaultsOnly</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Indicates that this property is only visible in property windows for archetypes, and cannot be edited. This Specifier is incompatible with any of the \"Edit\" Specifiers.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>VisibleInstanceOnly</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Indicates that this property is only visible in property windows for instances, not for archetypes, and cannot be edited. This Specifier is incompatible with any of the \"Edit\" Specifiers.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ]
      ],
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Metadata Specifiers",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "When declaring classes, interfaces, structs, enums, enum values, functions, or properties, you can add <strong>Metadata Specifiers</strong> to control how they interact with various aspects of the engine and editor. Each type of data structure or member has its own list of Metadata Specifiers.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "callout",
      "callout_type": "warning",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Metadata only exists in the editor; do not write game logic that accesses metadata.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "enhanced_table",
      "widths": [
        "40.4187%",
        "59.5813%"
      ],
      "rows": [
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Property Meta Tag",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "Effect",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>AllowAbstract=\"true/false\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used for <code>Subclass</code> and <code>SoftClass</code> properties. Indicates whether abstract Class types should be shown in the Class picker.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>AllowedClasses=\"Class1, Class2, ..\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used for <code>FSoftObjectPath</code> properties. Comma delimited list that indicates the Class type(s) of assets to be displayed in the Asset picker.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>AllowPreserveRatio</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used for <code>FVector</code> properties. It causes a ratio lock to be added when displaying this property in details panels.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>ArrayClamp=\"ArrayProperty\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used for integer properties. Clamps the valid values that can be entered in the UI to be between 0 and the length of the array property named.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>AssetBundles</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used for <code>SoftObjectPtr</code> or <code>SoftObjectPath</code> properties. List of Bundle names used inside Primary Data Assets to specify which Bundles this reference is part of.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>BlueprintBaseOnly</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used for <code>Subclass</code> and <code>SoftClass</code> properties. Indicates whether only Blueprint Classes should be shown in the Class picker.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>BlueprintCompilerGeneratedDefaults</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Property defaults are generated by the Blueprint compiler and will not be copied when the <code>CopyPropertiesForUnrelatedObjects</code> function is called post-compile.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>ClampMin=\"N\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used for float and integer properties.  Specifies the minimum value <code>N</code> that may be entered for the property.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>ClampMax=\"N\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used for float and integer properties.  Specifies the maximum value <code>N</code> that may be entered for the property.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>ConfigHierarchyEditable</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This property is serialized to a config (<code>.ini</code>) file, and can be set anywhere in the config hierarchy.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>ContentDir</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used by <code>FDirectoryPath</code> properties. Indicates that the path will be picked using the Slate-style directory picker inside the <code>Content</code> folder.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>DisplayAfter=\"PropertyName\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This property will show up in the Blueprint Editor immediately after the property named <code>PropertyName</code>, regardless of its order in source code, as long as both properties are in the same category. If multiple properties have the same <code>DisplayAfter</code> value and the same <code>DisplayPriority</code> value, they will appear after the named property in the order in which they are declared in the header file.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>DisplayName=\"Property Name\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The name to display for this property, instead of the code-generated name.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>DisplayPriority=\"N\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "If two properties feature the same <code>DisplayAfter</code> value, or are in the same category and do not have the <code>DisplayAfter</code> Meta Tag, this property will determine their sorting order. The highest-priority value is 1, meaning that a property with a <code>DisplayPriority</code> value of 1 will appear above a property with a <code>DisplayPriority</code> value of 2. If multiple properties have the same <code>DisplayAfter</code> value, they will appear in the order in which they are declared in the header file.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>DisplayThumbnail=\"true\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Indicates that the property is an Asset type and it should display the thumbnail of the selected Asset.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>EditCondition=\"BooleanPropertyName\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Names a boolean property that is used to indicate whether editing of this property is disabled. Putting \"!\" before the property name inverts the test.",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "callout",
              "callout_type": "note",
              "blocks": [
                {
                  "type": "paragraph",
                  "content": "The EditCondition meta tag is no longer limited to a single boolean property. It is now evaluated using a full-fledged expression parser, meaning you can include a full C++ expression.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>EditFixedOrder</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Keeps the elements of an array from being reordered by dragging.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>ExactClass=\"true\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used for <code>FSoftObjectPath</code> properties in conjunction with <code>AllowedClasses</code>. Indicates whether only the exact Classes specified in <code>AllowedClasses</code> can be used, or if subclasses are also valid.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>ExposeFunctionCategories=\"Category1, Category2, ..\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies a list of categories whose functions should be exposed when building a function list in the Blueprint Editor.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>ExposeOnSpawn=\"true\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies whether the property should be exposed on a Spawn Actor node for this Class type.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>FilePathFilter=\"FileType\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used by <code>FFilePath</code> properties. Indicates the path filter to display in the file picker. Common values include \"uasset\" and \"umap\", but these are not the only possible values.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>GetByRef</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Makes the \"Get\" Blueprint Node for this property return a const reference to the property instead of a copy of its value. Only usable with Sparse Class Data, and only when <code>NoGetter</code> is not present.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>HideAlphaChannel</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used for <code>FColor</code> and <code>FLinearColor</code> properties. Indicates that the <code>Alpha</code> property should be hidden when displaying the property widget in the details.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>HideViewOptions</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used for <code>Subclass</code> and <code>SoftClass</code> properties. Hides the ability to change view options in the Class picker.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>InlineEditConditionToggle</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Signifies that the boolean property is only displayed inline as an edit condition toggle in other properties, and should not be shown on its own row.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>LongPackageName</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used by <code>FDirectoryPath</code> properties. Converts the path to a long package name.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>MakeEditWidget</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used for Transform or Rotator properties, or Arrays of Transforms or Rotators. Indicates that the property should be exposed in the viewport as a movable widget.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>NoGetter</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Causes Blueprint generation not to generate a \"get\" Node for this property. Only usable with Sparse Class Data.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<code>ScriptName=\"DisplayName\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The name to use for this clas, property, or function when exporting it to a scripting language. You may include deprecated names as additional semi-colon-separated entries.",
              "settings": {
                "is_hidden": false
              }
            }
          ]
        ]
      ],
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "Egv6",
  "settings": {
    "is_hidden": false
  }
}
```
