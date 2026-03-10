# Creating Timelines

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-timelines-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 704,
        "excerpt_assignment_id": 417,
        "blocks": [
          {
            "type": "header",
            "content": "Creating Timelines",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You can create your own <strong>Timeline Component</strong> in an <strong>Actor</strong> Blueprint by following these steps.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "From the <strong>Content Browser</strong>, select <strong>Add+</strong> &gt; <strong>Blueprint Class</strong> and create a new Actor Blueprint named <strong>BP_TimelineActor</strong>. The <strong>Pick Parent Class</strong> dialog appears.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528033,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528033,
                    "file_name": "01_AddBPActorClass.png",
                    "file_size": 62172,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:21:55.782+00:00",
                    "height": 450,
                    "width": 600,
                    "storage_key": "d38a390d-c7a9-4c00-8252-cb8e9a97869e",
                    "context": "documentation"
                  },
                  "storage_key": "d38a390d-c7a9-4c00-8252-cb8e9a97869e",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "In the <strong>Class Defaults</strong>, right-click on the <strong>Event Graph</strong>, to display the <strong>Blueprint Context Menu</strong>, search for and select <strong>Add Timeline</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528034,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528034,
                    "file_name": "02_AddTimelineNode.png",
                    "file_size": 7270,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:21:55.888+00:00",
                    "height": 130,
                    "width": 410,
                    "storage_key": "9e804101-c573-49eb-bb88-12b262fcd183",
                    "context": "documentation"
                  },
                  "storage_key": "9e804101-c573-49eb-bb88-12b262fcd183",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ]
            ],
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "A new Timeline node appears on the Event Graph.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24528035,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24528035,
              "file_name": "03_TimelineNode.png",
              "file_size": 53623,
              "content_type": "image/png",
              "created_at": "2025-04-22T18:21:56.002+00:00",
              "height": 420,
              "width": 600,
              "storage_key": "79049274-4482-4613-8cba-03db75294f21",
              "context": "documentation"
            },
            "storage_key": "79049274-4482-4613-8cba-03db75294f21",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "When a Timeline is added to your Blueprint class, you will be able to see it listed in the <strong>My Blueprint</strong> tab.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24528036,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24528036,
              "file_name": "04_TimeLineComponent.png",
              "file_size": 21844,
              "content_type": "image/png",
              "created_at": "2025-04-22T18:21:56.184+00:00",
              "height": 410,
              "width": 320,
              "storage_key": "da5d1238-a872-436e-8b86-8935c9dbd4e5",
              "context": "documentation"
            },
            "storage_key": "da5d1238-a872-436e-8b86-8935c9dbd4e5",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Timeline Variables",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Once you have created a Timeline, you will notice it becomes available as a variable in the <strong>My Blueprint</strong> tab. This is done to provide a reference to the Timeline component, and is useful when utilizing the Timeline nodes. These nodes exist to allow access to certain features of a Timeline, such as its play rate.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24528037,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24528037,
              "file_name": "05_GetTimeLineNode.png",
              "file_size": 8168,
              "content_type": "image/png",
              "created_at": "2025-04-22T18:21:56.322+00:00",
              "height": 100,
              "width": 320,
              "storage_key": "8fa84ebb-0ddf-4cb0-9394-491cc92016ed",
              "context": "documentation"
            },
            "storage_key": "8fa84ebb-0ddf-4cb0-9394-491cc92016ed",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "For example, you can use the <strong>Get Timeline 0</strong> variable to query the current Play Rate value of that Timeline.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24528038,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24528038,
              "file_name": "06_BPScript1.png",
              "file_size": 32404,
              "content_type": "image/png",
              "created_at": "2025-04-22T18:21:56.436+00:00",
              "height": 130,
              "width": 500,
              "storage_key": "123e7313-7171-4e38-9409-786ce5822043",
              "context": "documentation"
            },
            "storage_key": "123e7313-7171-4e38-9409-786ce5822043",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "A wide variety of such nodes exist, providing the capabilities to query values and control behavior of your Timeline nodes. For a complete list of the available Timeline nodes and their functionality, see the <a data-document-id=\"3227988\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine\">Timeline Nodes</a> page.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Creating a Timeline Event",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "<strong>Timeline Events</strong> provide functionality to a <strong>Timeline Component</strong> to handle your own custom events or functions. Follow the steps below for an example on how to implement your own event.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Open <strong>BP_TimelineActor</strong>, drag off the <strong>execution pin</strong> of the <strong>Begin Play</strong> node and search for and select <strong>Add Timeline</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_Event Name=&quot;K2Node_Event_0&quot;\n     EventReference=(MemberParent=Class&#39;&quot;/Script/Engine.Actor&quot;&#39;,MemberName=&quot;ReceiveBeginPlay&quot;)\n     bOverrideFunction=True\n     NodePosY=-128\n     bCommentBubblePinned=True\n     NodeGuid=5FBA33CC4CC8CB4ED0DE10802AEC6150\n     CustomProperties Pin (PinId=04DC4F854BB6BB3B469928A3D262B532,PinName=&quot;OutputDelegate&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;delegate&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(MemberParent=Class&#39;&quot;/Script/Engine.Actor&quot;&#39;,MemberName=&quot;ReceiveBeginPlay&quot;),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=493D6ECC48C47DAF19E698BF937AB787,PinName=&quot;then&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_Timeline_0 7B94569E4931CB05569B779BA7053DE2,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     End Object\n     Begin Object Class=/Script/BlueprintGraph.K2Node_Timeline Name=&quot;K2Node_Timeline_0&quot;\n",
                  "lines_of_code": 27,
                  "id": 40437,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQzNywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjM5KzAwOjAwIn0=--f8fda37d93ce96b89e37d38c562799241a5a2b38961ebb8e171de2ffa396903c",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Drag off the <strong>Finished</strong> pin of the <strong>Timeline_0</strong> node, search for and add <strong>Print String</strong> node. Input the string \"<strong>Timeline Finished</strong>\" to the <strong>text field</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_CallFunction Name=&quot;K2Node_CallFunction_3&quot;\n     FunctionReference=(MemberParent=Class&#39;&quot;/Script/Engine.KismetSystemLibrary&quot;&#39;,MemberName=&quot;PrintString&quot;)\n     NodePosX=432\n     NodePosY=-128\n     AdvancedPinDisplay=Hidden\n     EnabledState=DevelopmentOnly\n     NodeGuid=C2E617C34EF5512E11FFEF9545AC379A\n     CustomProperties Pin (PinId=1941A1CD45D63F98C92FB1AA49279290,PinName=&quot;execute&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_Timeline_0 AEAD3EDD4B931BA678F86DBDD5D365C2,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=B5FA1DB14BEC1B77DDD8D5A441E574DB,PinName=&quot;then&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=95EA3B1449CB53545C29F38249A31A77,PinName=&quot;self&quot;,PinFriendlyName=NSLOCTEXT(&quot;K2Node&quot;, &quot;Target&quot;, &quot;Target&quot;),PinType.PinCategory=&quot;object&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=Class&#39;&quot;/Script/Engine.KismetSystemLibrary&quot;&#39;,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultObject=&quot;/Script/Engine.Default__KismetSystemLibrary&quot;,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n",
                  "lines_of_code": 18,
                  "id": 40438,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQzOCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjM5KzAwOjAwIn0=--cc283ec27e27da50110fce7a3b5defee19bb7a0505733c58e782c5f54b58c976",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Your final Blueprint Script should look as following:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "blueprint",
                  "title": "context_graph",
                  "code_preview": "Begin Object Class=/Script/BlueprintGraph.K2Node_Event Name=&quot;K2Node_Event_0&quot;\n     EventReference=(MemberParent=Class&#39;&quot;/Script/Engine.Actor&quot;&#39;,MemberName=&quot;ReceiveBeginPlay&quot;)\n     bOverrideFunction=True\n     NodePosX=-16\n     NodePosY=-128\n     bCommentBubblePinned=True\n     NodeGuid=5FBA33CC4CC8CB4ED0DE10802AEC6150\n     CustomProperties Pin (PinId=04DC4F854BB6BB3B469928A3D262B532,PinName=&quot;OutputDelegate&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;delegate&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(MemberParent=Class&#39;&quot;/Script/Engine.Actor&quot;&#39;,MemberName=&quot;ReceiveBeginPlay&quot;),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     CustomProperties Pin (PinId=493D6ECC48C47DAF19E698BF937AB787,PinName=&quot;then&quot;,Direction=&quot;EGPD_Output&quot;,PinType.PinCategory=&quot;exec&quot;,PinType.PinSubCategory=&quot;&quot;,PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node_Timeline_0 7B94569E4931CB05569B779BA7053DE2,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)\n     End Object\n",
                  "lines_of_code": 46,
                  "id": 40439,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQzOSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjM5KzAwOjAwIn0=--07a01c783ccaf34e45f43090375fff218b090daf3749def591f21e851fa722a7",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Click <strong>Compile</strong> and <strong>Save</strong> buttons.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528039,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528039,
                    "file_name": "10_SaveCompileButton.png",
                    "file_size": 14936,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:21:56.527+00:00",
                    "height": 100,
                    "width": 500,
                    "storage_key": "7f0be974-5d1c-48e1-bea1-01268fe52dc0",
                    "context": "documentation"
                  },
                  "storage_key": "7f0be974-5d1c-48e1-bea1-01268fe52dc0",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Close the <strong>Blueprint Editor</strong> and navigate to the <strong>Content Browser</strong>. Find your <strong>BP_TimelineActor</strong> and drag off it into the <strong>Level</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528040,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528040,
                    "file_name": "11_DragBPTimelineActor.png",
                    "file_size": 418373,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:21:56.678+00:00",
                    "height": 675,
                    "width": 720,
                    "storage_key": "f5211b8e-8069-4149-bd23-e991318d414f",
                    "context": "documentation"
                  },
                  "storage_key": "f5211b8e-8069-4149-bd23-e991318d414f",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Click <strong>Play</strong> button for checking result.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528041,
                  "caption": "After a default Timeline length of 5 seconds, The text \"Timeline Finished\" will appear on the top left corner of the viewport.",
                  "alt_text": "",
                  "image": {
                    "id": 24528041,
                    "file_name": "12_FinalResult.png",
                    "file_size": 321841,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:21:56.847+00:00",
                    "height": 360,
                    "width": 720,
                    "storage_key": "82f57657-859f-4f88-a86d-850f0506e10c",
                    "context": "documentation"
                  },
                  "storage_key": "82f57657-859f-4f88-a86d-850f0506e10c",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ]
            ],
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Renaming Timelines",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "When using multiple Timelines in your Blueprints, it is important to name each Timeline accordingly. By default, all Timelines are named <strong>\"Timeline_n\"</strong> where <strong>n</strong> is a serialized number at the end. You can rename a Timeline by right-clicking it within the <strong>Graph</strong> tab or in the <strong>My Blueprint</strong> tab and selecting <strong>Rename</strong>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24528042,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24528042,
              "file_name": "13_Renaming.png",
              "file_size": 71227,
              "content_type": "image/png",
              "created_at": "2025-04-22T18:21:57.036+00:00",
              "height": 400,
              "width": 985,
              "storage_key": "62af4fd0-9966-4040-8116-0a58b9848f05",
              "context": "documentation"
            },
            "storage_key": "62af4fd0-9966-4040-8116-0a58b9848f05",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Opening the Timeline Editor",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Creating a timeline may not be useful unless you set it up with something to perform. For more information on editing Timelines, please see the <a href=\"programming-and-scripting/blueprints-visual-scripting/UserGuide/Timelines/Editor\">Timeline Editing page</a>.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "ybn",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 705,
        "excerpt_assignment_id": 418,
        "blocks": [
          {
            "type": "header",
            "content": "Creating Timelines",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You can create and instantiate your own <strong>Timeline Component</strong> in an <strong>Actor</strong> class by following the steps below.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to your <strong>C++ Classes folder</strong> and click the <strong>Add+</strong>. From the drop down menu select <strong>New C++ Class</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528043,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528043,
                    "file_name": "01_AddCppActorClass.png",
                    "file_size": 16563,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:21:57.585+00:00",
                    "height": 285,
                    "width": 300,
                    "storage_key": "2510967e-2b64-4745-b4ce-329fdc714423",
                    "context": "documentation"
                  },
                  "storage_key": "2510967e-2b64-4745-b4ce-329fdc714423",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Select <strong>Actor</strong> class as a <strong>Parent Class</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528044,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528044,
                    "file_name": "02_ChooseCppParentClass.png",
                    "file_size": 38071,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:21:57.683+00:00",
                    "height": 580,
                    "width": 946,
                    "storage_key": "82200c30-59fc-4ab8-86b0-f8eb9d05b056",
                    "context": "documentation"
                  },
                  "storage_key": "82200c30-59fc-4ab8-86b0-f8eb9d05b056",
                  "context": "documentation",
                  "width": 600,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Name created Actor class <strong>Timeline Actor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528045,
                  "caption": "Click image for full size.",
                  "alt_text": "",
                  "image": {
                    "id": 24528045,
                    "file_name": "03_NameCppActorClass.png",
                    "file_size": 31824,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:21:57.795+00:00",
                    "height": 580,
                    "width": 946,
                    "storage_key": "a4753060-0e69-44a5-adfd-1ba3dc55bb9c",
                    "context": "documentation"
                  },
                  "storage_key": "a4753060-0e69-44a5-adfd-1ba3dc55bb9c",
                  "context": "documentation",
                  "width": 600,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to your <code>TimelineActor.h</code> file and include following <code>TimelineComponent</code> class library.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "TimelineActor.h",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "#include &quot;Components/TimelineComponent.h&quot;",
                  "lines_of_code": 1,
                  "id": 40440,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ0MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjM5KzAwOjAwIn0=--307eb9e15788636e0515f04b956646fa8e0c904fabf4941c15ee1430aabdac77",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Implement the following class declaration inside the TimelineActor class defintion:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "TimelineActor.h",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "protected:\n\n        UPROPERTY(EditAnywhere, BlueprintReadWrite)\n        UTimelineComponent* ExampleTimelineComp;",
                  "lines_of_code": 4,
                  "id": 40441,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ0MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjM5KzAwOjAwIn0=--240a777e29020f13dd9cf23453bc13e7f01328344371c0198b6b04e4608d99b0",
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
                      "content": "In this code sample, you use the <a data-document-id=\"3227224\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-uproperties\">Property Specifier Tags</a>, <strong>EditAnywhere</strong>, and <strong>BlueprintReadWrite</strong>.",
                      "settings": {
                        "is_hidden": false
                      }
                    }
                  ],
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to the <code>TimelineActor.cpp</code> file, then add the following code to your TimelineActor constructor <code>ATimelineActor::ATimelineActor()</code>",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "TimelineActor.cpp",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "ATimelineActor::ATimelineActor()\n     {\n         // Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n         PrimaryActorTick.bCanEverTick = true;\n         ExampleTimelineComp = CreateDefaultSubobject&lt;UTimelineComponent&gt;(TEXT(&quot;TimelineComponent&quot;));\n     }",
                  "lines_of_code": 6,
                  "id": 40442,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ0MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjM5KzAwOjAwIn0=--7d5b0392d72b6f1079afec63776f5e79d8c4dff5d89cb3d858e779fb841d5a71",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "<strong>Compile</strong> your code.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to the <strong>C++ classes folder</strong>, right-click on your <strong>TimelineActor</strong> and create a Blueprint based on your TimelineActor class. Name it <strong>Bp_TimelineActor</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528046,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528046,
                    "file_name": "04_CreateBPBased.png",
                    "file_size": 56208,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:21:57.884+00:00",
                    "height": 334,
                    "width": 622,
                    "storage_key": "a169b69a-e154-4920-b71d-f124b0048acb",
                    "context": "documentation"
                  },
                  "storage_key": "a169b69a-e154-4920-b71d-f124b0048acb",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Once you have created your TimelineActor Blueprint, you can view the <strong>Class Defaults</strong>.\nFrom the <strong>Components</strong> tab, you should see your example Timeline Component.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528047,
                  "caption": "",
                  "alt_text": "",
                  "image": {
                    "id": 24528047,
                    "file_name": "05_ExampleTimelineComp.png",
                    "file_size": 24700,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:21:57.952+00:00",
                    "height": 400,
                    "width": 420,
                    "storage_key": "2a15cd95-3df9-4d65-845c-8b101a5b416e",
                    "context": "documentation"
                  },
                  "storage_key": "2a15cd95-3df9-4d65-845c-8b101a5b416e",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ]
            ],
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Work-In-Progress Code",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "TimelineActor.h",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "#pragma once\n\t#include &quot;Components/TimelineComponent.h&quot;\n\t#include &quot;CoreMinimal.h&quot;\n\t#include &quot;GameFramework/Actor.h&quot;\n\t#include &quot;TimelineActor.generated.h&quot;\n\n\tUCLASS()\n\tclass CPPTIMELINE_API ATimelineActor : public AActor\n\t{\n\t\tGENERATED_BODY()\n",
            "lines_of_code": 27,
            "id": 40443,
            "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ0MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjM5KzAwOjAwIn0=--b121cea14aaf46420d7e86bc5f09a17a6a202b4f2e8ebb8e7595247f304d2a47",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "TimelineActor.cpp",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "#include &quot;TimelineActor.h&quot;\n\n\t// Sets default values\n\tATimelineActor::ATimelineActor()\n\t{\n\t\t// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n\t\tPrimaryActorTick.bCanEverTick = true;\n\t\tExampleTimelineComp = CreateDefaultSubobject&lt;UTimelineComponent&gt;(TEXT(&quot;TimelineComponent&quot;));\n\t}\n\n",
            "lines_of_code": 21,
            "id": 40444,
            "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ0NCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjM5KzAwOjAwIn0=--fc1e6e9bb86fb48a4a61a0dce37c296ebebd8d666e95e59b0311ab32fd133e0b",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Timeline Variables",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "When you create a Timeline Component in C++ using <code>UProperty Specifiers</code>, it will become available as a variable in your <strong>Components</strong> tab. This may be useful for designers who would\nlike to continue to make iterations to your TimelineComponent via Blueprint Scripting.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24528048,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24528048,
              "file_name": "ExamplePlayRate.png",
              "file_size": 21979,
              "content_type": "image/png",
              "created_at": "2025-04-22T18:21:58.060+00:00",
              "height": 128,
              "width": 459,
              "storage_key": "443b21a7-8228-4b93-b192-be5ba5d447a2",
              "context": "documentation"
            },
            "storage_key": "443b21a7-8228-4b93-b192-be5ba5d447a2",
            "context": "documentation",
            "width": null,
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
                "content": "Image above shows using the native C++ Timeline Variable to get the Current Play Rate value of the Timeline in Blueprint.",
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
            "type": "paragraph",
            "content": "For a complete list of the available Blueprint Timeline nodes and their functionality please see the <a data-document-id=\"3227988\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine\">Timeline nodes</a> page.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Creating a FTimeLineEvent",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Timeline Events (<code>FOnTimelineEvent</code>) are <a data-document-id=\"3227458\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/dynamic-delegates-in-unreal-engine\">Dynamic Delegates</a> that provide functionality to a Timeline Component to handle an Event.\nFollow the steps below to create your own <code>FTimeLineEvent</code> to be bound to your Timeline Component's finished functionality.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to <code>TimelineActor.h</code> file and declare the following code in the <strong>Class Definition</strong>:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "TimelineActor.h",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "protected:\n\n         //Delegate signature for the function which will handle our Finished event.\n         FOnTimelineEvent TimelineFinishedEvent;\n\n         UFUNCTION()\n         void TimelineFinishedFunction();",
                  "lines_of_code": 7,
                  "id": 40445,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ0NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjM5KzAwOjAwIn0=--facb52eb919f6d25a6174f70ca9c77dcd75136d0983f9284d0a79d53bff26a9b",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to <code>TimelineActor.cpp</code> and implement the following code:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "TimelineActor.cpp",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "void ATimelineActor::TimelineFinishedFunction()\n      {\n         UE_LOG(LogTemp, Warning, TEXT(&quot;Finished Event Called.&quot;));\n      }",
                  "lines_of_code": 4,
                  "id": 40446,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ0NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjM5KzAwOjAwIn0=--5650b7cef133aa6de516dcb3439931b60da684f6f9cd811d7480f4b36f2b0ec5",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to <code>ATimelineActor::BeginPlay()</code> method, and implement the following code:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "TimelineActor.cpp",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "// Called when the game starts or when spawned\n\n     void ATimelineActor::BeginPlay()\n     {\n         Super::BeginPlay();\n\n         TimelineFinishedEvent.BindUFunction(this, FName(&quot;TimelineFinishedFunction&quot;));\n         ExampleTimelineComp-&gt;SetTimelineFinishedFunc(TimelineFinishedEvent);\n         ExampleTimelineComp-&gt;PlayFromStart();\n     }",
                  "lines_of_code": 10,
                  "id": 40447,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ0NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjM5KzAwOjAwIn0=--cb5f23daa0e38ffcbfc1122e7539541cc48393f7194286fed89cab8cc133cbbd",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "You have now successfully bound your <code>TimelineFinished</code> Event to your custom <code>TimelineFinished</code> function.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Compile your code. Open <strong>Editor</strong> and navigate to the <strong>Content Browser</strong>. Find your <strong>BP_TimelineActor</strong> and drag off it into the <strong>Level</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528049,
                  "caption": "",
                  "alt_text": "image alt text",
                  "image": {
                    "id": 24528049,
                    "file_name": "07_DragBPTimelineActor.png",
                    "file_size": 408981,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:21:58.121+00:00",
                    "height": 686,
                    "width": 720,
                    "storage_key": "28357d14-c481-408c-b8a8-0ca300d76a4f",
                    "context": "documentation"
                  },
                  "storage_key": "28357d14-c481-408c-b8a8-0ca300d76a4f",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Press <strong>Play</strong> button. You should see the following message in the <strong>Output Log</strong> window:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 24528050,
                  "caption": "",
                  "alt_text": "image alt text",
                  "image": {
                    "id": 24528050,
                    "file_name": "08_OutputMessage.png",
                    "file_size": 9983,
                    "content_type": "image/png",
                    "created_at": "2025-04-22T18:21:58.336+00:00",
                    "height": 150,
                    "width": 720,
                    "storage_key": "26badab2-7e7c-4fb6-94f0-f372f00d15af",
                    "context": "documentation"
                  },
                  "storage_key": "26badab2-7e7c-4fb6-94f0-f372f00d15af",
                  "context": "documentation",
                  "width": null,
                  "settings": {
                    "is_hidden": false
                  }
                }
              ]
            ],
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Finished Code",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "TimelineActor.h",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "#pragma once\n\t#include &quot;Components/TimelineComponent.h&quot;\n\t#include &quot;CoreMinimal.h&quot;\n\t#include &quot;GameFramework/Actor.h&quot;\n\t#include &quot;TimelineActor.generated.h&quot;\n\n\tUCLASS()\n\tclass CPPTIMELINE_API ATimelineActor : public AActor\n\t{\n\t\tGENERATED_BODY()\n",
            "lines_of_code": 35,
            "id": 40448,
            "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ0OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjM5KzAwOjAwIn0=--30515a159ccb8261165868d8e7a633a3aaf000fbb5859fc1d191e0e13d5cd400",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "TimelineActor.cpp",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "#include &quot;TimelineActor.h&quot;\n\n\t// Sets default values\n\tATimelineActor::ATimelineActor()\n\t{\n\t\t// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don&#39;t need it.\n\t\tPrimaryActorTick.bCanEverTick = true;\n\t\tExampleTimelineComp = CreateDefaultSubobject&lt;UTimelineComponent&gt;(TEXT(&quot;TimelineComponent&quot;));\n\t}\n\n",
            "lines_of_code": 31,
            "id": 40449,
            "url_signature": "eyJzbmlwcGV0X2lkIjo0MDQ0OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIxOjM5KzAwOjAwIn0=--59c695f25cbc093e23224f66105d9fc43e24b0b2eb81448e43c3156e119e8726",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "qGX",
        "settings": {
          "is_hidden": false
        }
      }
    ]
  },
  "settings": {
    "is_hidden": false
  }
}
```
