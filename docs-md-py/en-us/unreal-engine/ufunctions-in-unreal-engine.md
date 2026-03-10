# UFunctions

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ufunctions-in-unreal-engine

> Application Version: 5.7

## UFunction Declaration

A **UFunction** is a C++ function that is recognized by the Unreal Engine reflection system. Any `UObject` or Blueprint function library can declare a member function as a UFunction by placing the `UFUNCTION` macro on the line above the function declaration in the header file. The macro will support **Function Specifiers** to change how Unreal Engine interprets and uses a function.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "UFUNCTION([specifier1=setting1, specifier2, ...], [meta(key1=&quot;value1&quot;, key2, ...)])\n\tReturnType FunctionName([Parameter1, Parameter2, ..., ParameterN1=DefaultValueN1, ParameterN2=DefaultValueN2]) [const];",
  "lines_of_code": 2,
  "id": 155031,
  "url_signature": "eyJzbmlwcGV0X2lkIjoxNTUwMzEsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowMTozMSswMDowMCJ9--4adf36bdb2fad4b7e9f16927c8c7f3196db2097e89c541071f2c68d2e42da96a",
  "settings": {
    "is_hidden": false
  }
}
```

With Function Specifiers, you can expose UFunctions to [Blueprint Visual Scripting](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine) graphs, which provide a way for developers to call or extend UFunctions from Blueprint Assets without having to alter C++ code.

UFunctions are able to bind to [Delegates](https://dev.epicgames.com/documentation/en-us/unreal-engine/delegates-and-lambda-functions-in-unreal-engine) in the default properties of a Class, enabling them to perform such tasks as associating actions with user inputs. They can also act as network callbacks, meaning you can use them to receive a notification and run custom code whenever a certain variable is affected by a network update.

You can even create your own *console commands* (often called *debug*, *configuration*, or *cheat code* commands) that you can call from the game console in development builds, or add buttons with custom functionality to game objects in the Level Editor.

### Function Specifiers

```json
{
  "type": "include",
  "excerpt_id": 2720,
  "excerpt_assignment_id": 2629,
  "blocks": [
    {
      "type": "paragraph",
      "content": "When declaring functions, <strong>Function Specifiers</strong> can be added to the declaration to control how the function behaves with various aspects of the engine and the editor.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "enhanced_table",
      "widths": null,
      "rows": [
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Function Specifier",
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
              "content": "<code>BlueprintAuthorityOnly</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This function will only execute from Blueprint code if running on a machine with network authority (a server, dedicated server, or single-player game).",
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
              "content": "The function can be executed in a Blueprint or Level Blueprint graph.",
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
              "content": "<code>BlueprintCosmetic</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This function is cosmetic and will not run on dedicated servers.",
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
              "content": "<code>BlueprintImplementableEvent</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The function can be implemented in a Blueprint or Level Blueprint graph.",
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
              "content": "<code>BlueprintNativeEvent</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This function is designed to be overridden by a Blueprint, but also has a default native implementation. Declares an additional function named the same as the main function, but with <code>_Implementation</code> added to the end, which is where code should be written. The autogenerated code will call the <code>_Implementation</code> method if no Blueprint override is found.",
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
              "content": "<code>BlueprintPure</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The function does not affect the owning object in any way and can be executed in a Blueprint or Level Blueprint graph. By default functions that are marked <code>const</code> will be exposed as pure functions. To make a const function not be a pure function you can declare:<code>BlueprintPure=false</code>",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "code_snippet",
              "description": "",
              "snippet_type": "cpp_programming",
              "title": "",
              "code_preview": "`UFUNCTION(BlueprintPure)\nfloat  BlueprintPureFunction;\n\nUFUNCTION(BlueprintCallable)\nfloat BlueprintCallableFunction\n\nUFUNCTION(BlueprintCallable)\nint32 BlueprintCallableConstFunction() const\n\nUFUNCTION(BlueprintPure=fasle)\n",
              "lines_of_code": 11,
              "id": 155030,
              "url_signature": "eyJzbmlwcGV0X2lkIjoxNTUwMzAsInVybF9leHBpcmVzX2F0IjoiMjAyNi0wMy0wOVQxODowMTozMSswMDowMCJ9--e2e45b5ddd391923a71e97a31bda7aff3b7dc34f76742541fd7e04241f112e68",
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "image",
              "image_id": 26376870,
              "caption": "",
              "alt_text": "",
              "image": {
                "id": 26376870,
                "file_name": "BPCallable.png",
                "file_size": 178988,
                "content_type": "image/png",
                "created_at": "2026-01-12T15:46:11.980+00:00",
                "height": 742,
                "width": 1531,
                "storage_key": "1d225382-28eb-482c-bdad-7939f8e53061",
                "context": "documentation"
              },
              "storage_key": "1d225382-28eb-482c-bdad-7939f8e53061",
              "context": "documentation",
              "width": null,
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "paragraph",
              "content": "Pure functions do not cache their results, therefore you should be cautious when doing any non-trivial amount of work with a blueprint function. It is good practice to avoid outputting array properties in Blueprint pure functions.",
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
              "content": "<code>CallInEditor</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This function can be called in the editor on selected instances via a button in the Details panel.",
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
              "content": "<code>Category = \"TopCategory\\|SubCategory\\|Etc\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies the category of the function when displayed in Blueprint editing tools. Define nested categories using the | operator.",
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
              "content": "<code>Client</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The function is only executed on the client that owns the Object on which the function is called. Declares an additional function named the same as the main function, but with <code>_Implementation</code> added to the end. The autogenerated code will call the <code>_Implementation</code> method when necessary.",
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
              "content": "<code>CustomThunk</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The <code>UnrealHeaderTool</code> code generator will not produce a thunk for this function; it is up to the user to provide one with the <code>DECLARE_FUNCTION</code> or <code>DEFINE_FUNCTION</code> macros.",
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
              "content": "<code>Exec</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The function can be executed from the in-game console. Exec commands only function when declared within certain Classes.",
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
              "content": "<code>NetMulticast</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The function is executed both locally on the server, and replicated to all clients, regardless of the Actor's <code>NetOwner</code>.",
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
              "content": "<code>Reliable</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The function is replicated over the network, and is guaranteed to arrive regardless of bandwidth or network errors. Only valid when used in conjunction with <code>Client</code> or <code>Server</code>.",
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
              "content": "<code>SealedEvent</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This function cannot be overridden in subclasses. The <code>SealedEvent</code> keyword can only be used for events. For non-event functions, declare them as <code>static</code> or <code>final</code> to seal them.",
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
              "content": "<code>ServiceRequest</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This function is an RPC (Remote Procedure Call) service request. This implies <code>NetMulticast</code> and <code>Reliable</code>.",
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
              "content": "<code>ServiceResponse</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This function is an RPC service response. This implies <code>NetMulticast</code> and <code>Reliable</code>.",
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
              "content": "<code>Server</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The function is only executed on the server. Declares an additional function named the same as the main function, but with <code>_Implementation</code> added to the end, which is where code should be written. The autogenerated code will call the <code>_Implementation</code> method when necessary.",
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
              "content": "<code>Unreliable</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The function is replicated over the network but can fail due to bandwidth limitations or network errors. Only valid when used in conjunction with <code>Client</code> or <code>Server</code>.",
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
              "content": "<code>WithValidation</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Declares an additional function named the same as the main function, but with <code>_Validate</code> added to the end. This function takes the same parameters, and returns a <code>bool</code> to indicate whether or not the call to the main function should proceed.",
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
      "widths": null,
      "rows": [
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Function Meta Tag",
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
              "content": "<code>AdvancedDisplay=\"Parameter1, Parameter2, ..\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The comma-separated list of parameters will show up as advanced pins (requiring UI expansion).",
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
              "content": "<code>AdvancedDisplay=N</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Replace <code>N</code> with a number, and all parameters after the Nth will show up as advanced pins (requiring UI expansion). For example, 'AdvancedDisplay=2' will mark all but the first two parameters as advanced).",
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
              "content": "<code>ArrayParm=\"Parameter1, Parameter2, ..\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Indicates that a <code>BlueprintCallable</code> function should use a Call Array Function node and that the listed parameters should be treated as wild card array properties.",
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
              "content": "<code>ArrayTypeDependentParams=\"Parameter\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "When <code>ArrayParm</code> is used, this specifier indicates one parameter which will determine the types of all parameters in the <code>ArrayParm</code> list.",
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
              "content": "<code>AutoCreateRefTerm=\"Parameter1, Parameter2, ..\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The listed parameters, although passed by reference, will have an automatically created default if their pins are left disconnected. This is a convenience feature for Blueprints, often used on array pins.",
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
              "content": "<code>BlueprintAutocast</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used only by static <code>BlueprintPure</code> functions from a Blueprint function library. A cast node will be automatically added for the return type and the type of the first parameter of the function.",
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
              "content": "<code>BlueprintInternalUseOnly</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This function is an internal implementation detail, used to implement another function or node. It is never directly exposed in a Blueprint graph.",
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
              "content": "<code>BlueprintProtected</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This function can only be called on the owning Object in a Blueprint. It cannot be called on another instance.",
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
              "content": "<code>CallableWithoutWorldContext</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used for <code>BlueprintCallable</code> functions that have a <code>WorldContext</code> pin to indicate that the function can be called even if its Class does not implement the <code>GetWorld</code> function.",
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
              "content": "<code>CommutativeAssociativeBinaryOperator</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Indicates that a <code>BlueprintCallable</code> function should use the Commutative Associative Binary node. This node lacks pin names, but features an <strong>Add Pin</strong> button that creates additional input pins.",
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
              "content": "<code>CompactNodeTitle=\"Name\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Indicates that a <code>BlueprintCallable</code> function should display in the compact display mode, and provides the name to display in that mode.",
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
              "content": "<code>CustomStructureParam=\"Parameter1, Parameter2, ..\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The listed parameters are all treated as wildcards. This specifier requires the <code>UFUNCTION</code>-level specifier, <code>CustomThunk</code>, which will require the user to provide a custom <code>exec</code> function. In this function, the parameter types can be checked and the appropriate function calls can be made based on those parameter types. The base <code>UFUNCTION</code> should never be called, and should assert or log an error if it is.",
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
                  "content": "To declare a custom <code>exec</code> function, use the syntax <code>DECLARE_FUNCTION(execMyFunctionName)</code> where <code>MyFunctionName</code> is the name of the original function.",
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
              "content": "<code>DefaultToSelf</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "For <code>BlueprintCallable</code> functions, this indicates that the Object property's named default value should be the self context of the node.",
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
              "content": "<code>DeprecatedFunction</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Any Blueprint references to this function will cause compilation warnings telling the user that the function is deprecated. You can add to the deprecation warning message (for example, to provide instructions on replacing the deprecated function) using the <code>DeprecationMessage</code> metadata specifier.",
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
              "content": "<code>DeprecationMessage</code>=\"Message Text\"",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "If the function is deprecated, this message will be added to the standard deprecation warning when trying to compile a Blueprint that uses it.",
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
              "content": "<code>DeterminesOutputType=\"Parameter\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The return type of the function will dynamically change to match the input that is connected to the named parameter pin. The parameter should be a templated type like <code>TSubClassOf&lt;X&gt;</code> or <code>TSoftObjectPtr&lt;X&gt;</code>, where the function's original return type is <code>X*</code> or a container with <code>X*</code> as the value type, such as <code>TArray&lt;X*&gt;</code>.",
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
              "content": "<code>DevelopmentOnly</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Functions marked as <code>DevelopmentOnly</code> will only run in Development mode. This is useful for functionality like debug output, which is expected not to exist in shipped products.",
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
              "content": "<code>DisplayName=\"Blueprint Node Name\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "The name of this node in a Blueprint will be replaced with the value provided here, instead of the code-generated name.",
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
              "content": "<code>ExpandEnumAsExecs=\"Parameter\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "For <code>BlueprintCallable</code> functions, this indicates that one input execution pin should be created for each entry in the <code>enum</code> used by the parameter. The parameter must be of an enumerated type that has the <code>UENUM</code> tag.",
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
              "content": "<code>ForceAsFunction</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Change a <code>BlueprintImplementableEvent</code> with no return value from an event into a function.",
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
              "content": "<code>HidePin=\"Parameter\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "For <code>BlueprintCallable</code> functions, this indicates that the parameter pin should be hidden from the user's view. Only one pin per function can be hidden in this manner.",
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
              "content": "<code>HideSelfPin</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Hides the \"self\" pin, which indicates the object on which the function is being called. The \"self\" pin is automatically hidden on <code>BlueprintPure</code> functions that are compatible with the calling Blueprint's Class. Functions that use the <code>HideSelfPin</code> Meta Tag frequently also use the <code>DefaultToSelf</code> Specifier.",
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
              "content": "<code>InternalUseParam=\"Parameter\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Similar to <code>HidePin</code>, this hides the named parameter's pin from the user's view, and can only be used for one parameter per function.",
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
              "content": "<code>KeyWords=\"Set Of Keywords\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Specifies a set of keywords that can be used when searching for this function, such as when placing a node to call the function in a Blueprint Graph.",
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
              "content": "<code>Latent</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Indicates a latent action. Latent actions have one parameter of type <code>FLatentActionInfo</code>, and this parameter is named by the <code>LatentInfo</code> specifier.",
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
              "content": "<code>LatentInfo=\"Parameter\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "For Latent <code>BlueprintCallable</code> functions, indicates which parameter is the LatentInfo parameter.",
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
              "content": "<code>MaterialParameterCollectionFunction</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "For <code>BlueprintCallable</code> functions, indicates that the material override node should be used.",
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
              "content": "<code>NativeBreakFunc</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "For <code>BlueprintCallable</code> functions, indicates that the function should be displayed the same way as a standard Break Struct node.",
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
              "content": "<code>NotBlueprintThreadSafe</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Only valid in Blueprint function libraries. This function will be treated as an exception to the owning Class's general <code>BlueprintThreadSafe</code> metadata.",
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
              "content": "<code>ShortToolTip=\"Short tooltip\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "A short tooltip that is used in some contexts where the full tooltip might be overwhelming, such as the Parent Class Picker dialog.",
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
              "content": "<code>ToolTip=\"Hand-written tooltip</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Overrides the automatically generated tooltip from code comments.",
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
              "content": "<code>UnsafeDuringActorConstruction</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "This function is not safe to call during Actor construction.",
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
              "content": "<code>WorldContext=\"Parameter\"</code>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Used by <code>BlueprintCallable</code> functions to indicate which parameter determines the World in which the operation takes place.",
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
  "excerpt_hash_id": "9kGP",
  "settings": {
    "is_hidden": false
  }
}
```

### Function Parameter Specifiers

| Parameter Specifier | Description |
| --- | --- |
| Out | Declares the parameter as being passed by reference, allowing it to be modified by the function. |
| Optional | With the optional keyword, you can make certain function parameters optional, as a convenience to the caller. The values for optional parameters which the caller does not specify depend on the function. For example, the `SpawnActor` function takes an optional location and rotation, which defaults to the location and rotation of the spawning Actor's root component. The default value of optional arguments can be specified by adding `= [value]`. For example: `function myFunc(optional int x = -1)`. In most cases, the default value for the type of variable, or zero (0, false, "", none), is used when no value is passed to an optional parameter. |

## Delegates

**Delegates** can call member functions on C++ objects in a generic, type-safe way. A delegate can be bound dynamically to a member function of an arbitrary object, calling the function on the object at a future time, even if the caller does not know the object`s type.

See the [Delegates](https://dev.epicgames.com/documentation/en-us/unreal-engine/delegates-and-lambda-functions-in-unreal-engine) page for reference and usage information.

## Timers

**Timers** schedule actions to be performed after a delay, or over a period of time. For example, you may want to make the player invulnerable after obtaining a power-up item, then restore vulnerability after 10 seconds. Or you may want to apply damage once per second while the player moves through a room filled with toxic gas. Such actions can be achieved through the use of timers.

See the [Gameplay Timers](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-timers-in-unreal-engine) page for reference and usage information.
