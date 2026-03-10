# Saving and Loading Your Game

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine

> Application Version: 5.7

The meaning of "saving the game" can vary considerably from one game to the next, but the general idea of enabling players to quit the game and then resume where they left off at a later time is a part of most modern games. Depending on what type of game you're making, you may only need a few basic pieces of information, such as the last checkpoint the player reached and maybe which items the player has found. Or you may need much more detailed information, possibly involving things like a long list of the player's social interactions with other in-game characters, or the current status of a variety of quests, mission objectives, or subplots.

Unreal Engine (UE) features a saving and loading system that revolves around one or more custom **SaveGame** classes that you create to meet your game's specific needs, including all of the information that you need to preserve across multiple play sessions. The system supports the ability to have multiple saved game files, and to save different SaveGame classes to those files. This is useful for separating globally-unlocked features from playthrough-specific game data.

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1775,
        "excerpt_assignment_id": 1442,
        "blocks": [
          {
            "type": "header",
            "content": "Creating a SaveGame Object",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "To create a new SaveGame object, <a data-document-id=\"3228682\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-cplusplus-class-wizard-in-unreal-engine\">create a new Blueprint Class</a>. When the <strong>Pick Parent Class</strong> dialog pops up, expand the <strong>Custom Classes</strong>\ndropdown, then select <strong>SaveGame</strong>. You can use the search box to jump directly to SaveGame. Name your new Blueprint MySaveGame.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25753229,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25753229,
              "file_name": "savegame.png",
              "file_size": 52949,
              "content_type": "image/png",
              "created_at": "2025-06-20T19:14:30.105+00:00",
              "height": 439,
              "width": 514,
              "storage_key": "1e0019a8-ab04-4151-a4d9-ac69156a2f1a",
              "context": "documentation"
            },
            "storage_key": "1e0019a8-ab04-4151-a4d9-ac69156a2f1a",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In your new SaveGame object Blueprint, create variables for any information you would like to save.",
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
                "content": "In this example, there are also variables declared that will be used to store default values for the SaveSlotName and the UserIndex, so that each class that saves to this\nSaveGame object will not have to independently set those variables. This step is optional, and will cause there to be one save slot that gets overwritten if the default values are not changed.",
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
            "type": "image",
            "image_id": 25753230,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25753230,
              "file_name": "SaveGameVariables.png",
              "file_size": 111696,
              "content_type": "image/png",
              "created_at": "2025-06-20T19:14:30.294+00:00",
              "height": 414,
              "width": 1061,
              "storage_key": "c13903d0-6e1b-475a-8651-78f1e1f5a168",
              "context": "documentation"
            },
            "storage_key": "c13903d0-6e1b-475a-8651-78f1e1f5a168",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You can set default values for the variables after the Blueprint is compiled.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "L2L",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1776,
        "excerpt_assignment_id": 1443,
        "blocks": [
          {
            "type": "header",
            "content": "Creating a SaveGame Object",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "The <code>USaveGame</code> class sets up an object that can be used as a target for the saving and loading functions declared in <code>Kismet/GameplayStatics.h</code>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You can create a new class based on <code>USaveGame</code> using the <a data-document-id=\"3228682\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-cplusplus-class-wizard-in-unreal-engine\">C++ Class Wizard</a>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25753231,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25753231,
              "file_name": "SaveGameCode.png",
              "file_size": 55495,
              "content_type": "image/png",
              "created_at": "2025-06-20T19:14:30.573+00:00",
              "height": 574,
              "width": 950,
              "storage_key": "266ea198-39aa-40a5-b099-9e37109e465f",
              "context": "documentation"
            },
            "storage_key": "266ea198-39aa-40a5-b099-9e37109e465f",
            "context": "documentation",
            "width": 800,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In this example, the new <code>USaveGame</code> class is called <code>UMySaveGame</code>. In order to use it, add the following lines to your game module's header file, after any other <code>#include</code> directives:",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "<br>",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "MyProject.h",
            "code_preview": "#include &quot;MySaveGame.h&quot;\n\t#include &quot;Kismet/GameplayStatics.h&quot;",
            "lines_of_code": 2,
            "id": 64963,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2NDk2MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjU0OjE3KzAwOjAwIn0=--6101fe05b8d7390e4f45ed6f2c861602377585015c3430e714f512b85c915c8e",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Header",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "In the header file for your <code>SaveGame</code> object, you can declare any variables you want your <code>SaveGame</code> to store.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "UPROPERTY(VisibleAnywhere, Category = Basic)\n\tFString PlayerName;",
            "lines_of_code": 2,
            "id": 64964,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2NDk2NCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjU0OjE3KzAwOjAwIn0=--0281324072a5dc8a3313626a52fc7219d4a00ae5e3980484512b0b417298cd2f",
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
                "content": "In this example, there are also variables declared that will be used to store default values for the <code>SaveSlotName</code> and the <code>UserIndex</code>, so that each class that saves to this\n<code>SaveGame</code> object will not have to independently set those variables. This step is optional, and will cause there to be one save slot that gets overwritten if the default values are not changed.",
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
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "MySaveGame.h",
            "code_preview": "#pragma once\n\n\t#include &quot;GameFramework/SaveGame.h&quot;\n\t#include &quot;MySaveGame.generated.h&quot;\n\n\t/**\n\t *\n\t */\n\tUCLASS()\n\tclass [PROJECTNAME]_API UMySaveGame : public USaveGame\n",
            "lines_of_code": 26,
            "id": 64965,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2NDk2NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjU0OjE3KzAwOjAwIn0=--4d22c6e96d2429201eda21506936e94acda1cd46fb656c80548e3eaba97e13b5",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Source",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Generally, the <code>SaveGame</code> object's source file does not need any particular code to function, unless your particular save system has additional functionality you would like to set up\nhere.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "This example does define the values of <code>SaveSlotName</code> and <code>UserIndex</code> in the class constructor, so they can be read out and used by other gameplay classes.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "MySaveGame.cpp",
            "code_preview": "// Copyright 1998-2018 Epic Games, Inc. All Rights Reserved.\n\n\t#include &quot;[ProjectName].h&quot;\n\t#include &quot;MySaveGame.h&quot;\n\n\tUMySaveGame::UMySaveGame()\n\t{\n\t\tSaveSlotName = TEXT(&quot;TestSaveSlot&quot;);\n\t\tUserIndex = 0;\n\t}",
            "lines_of_code": 10,
            "id": 64966,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2NDk2NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjU0OjE3KzAwOjAwIn0=--de4c359e0d23db2b9f7d4deec788cad42257079dbdc6ad2e2b58ce1f01beb9b2",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "Xoe",
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

## Saving A Game

Once you have created a SaveGame class, you can populate it with variables to store your game's data. For example, you might create an integer variable to store the player's score, or a string variable for the player's name. When you save the game, you will transfer that information from the current game world into a SaveGame object, and when loading a game, you will copy it from the SaveGame object to game object like Characters, the Player Controller, or the Game Mode.

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1777,
        "excerpt_assignment_id": 1444,
        "blocks": [
          {
            "type": "paragraph",
            "content": "First, use the <strong>Create Save Game Object</strong> node to create an object based on your SaveGame class. Make sure you set the <strong>Save Game Class</strong> input pin's dropdown to the class you've created, which is <strong>MySaveGame</strong> in this example. The <strong>Create Save Game Object</strong> node will automatically change its output pin type to match the type you specify with the <strong>Save Game Class</strong> input pin. This enables you to use it directly, without a <strong>Cast To</strong> node. You may want to save the resulting object to a variable by using <strong>Promote to Variable</strong> so that you can easily reuse the object you just created later on.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25753232,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25753232,
              "file_name": "SaveGameBP_1.png",
              "file_size": 29069,
              "content_type": "image/png",
              "created_at": "2025-06-20T19:14:30.867+00:00",
              "height": 136,
              "width": 596,
              "storage_key": "cb08b644-ca91-4ed6-96a5-e1f1ab92d4c2",
              "context": "documentation"
            },
            "storage_key": "cb08b644-ca91-4ed6-96a5-e1f1ab92d4c2",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Now that the <strong>Save Game Instance</strong> holds your custom SaveGame object, you can send information to it. For example, you can set the <strong>Player Name</strong> field to \"PlayerOne\". Continue to set fields in your SaveGame object until it contains all of the data you want to store in the saved game file.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25753233,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25753233,
              "file_name": "SaveGameBP_2.png",
              "file_size": 28410,
              "content_type": "image/png",
              "created_at": "2025-06-20T19:14:30.943+00:00",
              "height": 128,
              "width": 535,
              "storage_key": "7af15c78-f75d-468a-8507-5c186e0b86de",
              "context": "documentation"
            },
            "storage_key": "7af15c78-f75d-468a-8507-5c186e0b86de",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "When the SaveGame object is fully populated, use the <strong>ASync Save Game To Slot</strong> node to finish saving the game. You will also need to provide a file name and a user ID. The file name and user ID in this example will be the default values created earlier. Execution will continue from the top pin immediately, and from the second pin once the savegame operation is complete. The output pins will not be valid until the second pin has executed.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25753234,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25753234,
              "file_name": "SaveGameBP_3.png",
              "file_size": 81562,
              "content_type": "image/png",
              "created_at": "2025-06-20T19:14:31.019+00:00",
              "height": 308,
              "width": 881,
              "storage_key": "174d3d5f-73b4-4218-897c-af1b525a50e6",
              "context": "documentation"
            },
            "storage_key": "174d3d5f-73b4-4218-897c-af1b525a50e6",
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
                "content": "<strong>Async Save Game To Slot</strong> is the recommended way to save your game, due to its ability to avoid hitches even when saving larger amounts of data. However, if your savegame data is small, or if you are saving from a menu or pause screen, you can save the game with the <strong>Save Game To Slot</strong> node, shown below, instead.",
                "settings": {
                  "is_hidden": false
                }
              },
              {
                "type": "image",
                "image_id": 25753235,
                "caption": "",
                "alt_text": "",
                "image": {
                  "id": 25753235,
                  "file_name": "SaveGameBP_4.png",
                  "file_size": 36556,
                  "content_type": "image/png",
                  "created_at": "2025-06-20T19:14:31.135+00:00",
                  "height": 166,
                  "width": 602,
                  "storage_key": "d75a61f7-887f-42c5-96d4-5ab964aa024b",
                  "context": "documentation"
                },
                "storage_key": "d75a61f7-887f-42c5-96d4-5ab964aa024b",
                "context": "documentation",
                "width": null,
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
            "content": "The following screenshot shows the entire Blueprint process for saving a game with the MySaveGame class:",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25753236,
            "caption": "Click the image above to enlarge.",
            "alt_text": "",
            "image": {
              "id": 25753236,
              "file_name": "SaveGameBP.png",
              "file_size": 98701,
              "content_type": "image/png",
              "created_at": "2025-06-20T19:14:31.237+00:00",
              "height": 309,
              "width": 1220,
              "storage_key": "3b214e97-269d-4840-836b-149380d790f0",
              "context": "documentation"
            },
            "storage_key": "3b214e97-269d-4840-836b-149380d790f0",
            "context": "documentation",
            "width": 880,
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "1Lb",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1778,
        "excerpt_assignment_id": 1445,
        "blocks": [
          {
            "type": "paragraph",
            "content": "First, call <code>CreateSaveGameObject</code> (from the <code>UGameplayStatics</code> library) to get a new <code>UMySaveGame</code> object. Once you have the object, you can populate it with the data you want to save. Finally, call <code>SaveGameToSlot</code> or <code>AsyncSaveGameToSlot</code> to write the data out to your device.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Asynchronous Saving",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "<code>AsyncSaveGameToSlot</code> is the recommended method for saving the game. Running asynchronously prevents a sudden framerate hitch, making it less noticeable to players and avoiding a possible certification issue on some platforms. When the save process is complete, the delegate (of type <code>FAsyncSaveGameToSlotDelegate</code>) will be called with the slot name, the user index, and a <code>bool</code> indicating success or failure.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "if (UMySaveGame* SaveGameInstance = Cast&lt;UMySaveGame&gt;(UGameplayStatics::CreateSaveGameObject(UMySaveGame::StaticClass())))\n\t{\n\t\t// Set up the (optional) delegate.\n\t\tFAsyncSaveGameToSlotDelegate SavedDelegate;\n\t\t// USomeUObjectClass::SaveGameDelegateFunction is a void function that takes the following parameters: const FString&amp; SlotName, const int32 UserIndex, bool bSuccess\n\t\tSavedDelegate.BindUObject(SomeUObjectPointer, &amp;USomeUObjectClass::SaveGameDelegateFunction);\n\n\t\t// Set data on the savegame object.\n\t\tSaveGameInstance-&gt;PlayerName = TEXT(&quot;PlayerOne&quot;);\n\n",
            "lines_of_code": 13,
            "id": 64967,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2NDk2NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjU0OjE3KzAwOjAwIn0=--80112f935f46e7f695ae06990c13688ad6f01cfef681c611fd58640beda34dc6",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Synchronous Saving",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "<code>SaveGameToSlot</code> is sufficient for small SaveGame formats, and for saving the game while paused or in a menu. It's also easy to use, as it simply saves the game immediately and returns a <code>bool</code> indicating success or failure. For larger amounts of data, or for auto-saving game while the player is still actively interacting with your game world, <code>AsyncSaveGameToSlot</code> is a better choice.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "if (UMySaveGame* SaveGameInstance = Cast&lt;UMySaveGame&gt;(UGameplayStatics::CreateSaveGameObject(UMySaveGame::StaticClass())))\n\t{\n\t\t// Set data on the savegame object.\n\t\tSaveGameInstance-&gt;PlayerName = TEXT(&quot;PlayerOne&quot;);\n\n\t\t// Save the data immediately.\n\t\tif (UGameplayStatics::SaveGameToSlot(SaveGameInstance, SlotNameString, UserIndexInt32))\n\t\t{\n\t\t\t// Save succeeded.\n\t\t}\n",
            "lines_of_code": 11,
            "id": 64968,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2NDk2OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjU0OjE3KzAwOjAwIn0=--b8da045129b23397b16d07554b09d753be9e3199d0c3d83fc9bdc1c7528a2598",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Binary Saving",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You can transfer a SaveGame object to memory with the <code>SaveGameToMemory</code> function. This function only offers synchronous operation, but is faster than saving to a drive. The caller provides a reference to a buffer (a <code>TArray&lt;uint8&gt;&</code>) where the data will be stored. On success, the function returns true.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "TArray&lt;uint8&gt; OutSaveData;\n\tif (UGameplayStatics::SaveGameToMemory(SaveGameObject, OutSaveData))\n\t{\n\t\t// The operation succeeded, and OutSaveData now contains a binary represenation of the SaveGame object.\n\t}",
            "lines_of_code": 5,
            "id": 64969,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2NDk2OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjU0OjE3KzAwOjAwIn0=--ac019934a3f1fd6f891b9d3dfb2f6583c8ae3bb5f8e76cab72f53b4a36e70c10",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You can also save binary data directly to a file, similar to the <code>SaveGameToSlot</code> function, by calling <code>SaveDataToSlot</code> with the buffer (a <code>const TArray&lt;uint8&gt;&</code>) and the slot name and user ID information. As with <code>SaveGameToMemory</code>, this function only offers synchronous operation, and returns a <code>bool</code> to indicate success or failure.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "if (UGameplayStatics::SaveDataToSlot(InSaveData, SlotNameString, UserIndexInt32))\n\t{\n\t\t// The operation succeeded, and InSaveData has been written to the save file defined by the slot name and user ID we provided.\n\t}",
            "lines_of_code": 4,
            "id": 64970,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2NDk3MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjU0OjE3KzAwOjAwIn0=--58bd959a81c5e1a18b81628790a348e8f7a3fe825c05d2056c6098a0050a7a72",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "gqP",
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

On development platforms, saved game files use the `.sav` extension and appear in the project's `Saved\SaveGames` folder. On other platforms, particularly consoles, this varies to accommodate the specific file system.

## Loading A Game

To load a saved game, you must provide the save slot name and user ID that you used when you saved it. If the SaveGame you specified exists, the Engine will populate your SaveGame object with the data it contains and return it as a base SaveGame (class `USaveGame`) object. You can then cast that object back to your custom SaveGame class and access the data. Depending on what kind of data your SaveGame type contains, you may want to keep a copy of it, or simply use the data and discard the object.

As with saving, you can load synchronously or asynchronously. If you have a large amount of data, or wish to use a loading screen or animation during load time, we recommend the asychronous method. For small amounts of data that load quickly, a synchronous method exists.

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1779,
        "excerpt_assignment_id": 1446,
        "blocks": [
          {
            "type": "paragraph",
            "content": "To load syncronously, use <strong>Load Game From Slot</strong>. This node is straightforward and will return a valid SaveGame object if the slot name and user ID you provide identifies a valid SaveGame file. The game will stop while the load operation is in progress.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25753237,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25753237,
              "file_name": "LoadGameBP.png",
              "file_size": 53653,
              "content_type": "image/png",
              "created_at": "2025-06-20T19:14:31.626+00:00",
              "height": 208,
              "width": 1026,
              "storage_key": "db600216-68bb-4733-ac58-39cab707a700",
              "context": "documentation"
            },
            "storage_key": "db600216-68bb-4733-ac58-39cab707a700",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "<strong>Async Load Game From Slot</strong> works in roughly the same way, but has two execution output pins. The first pin executes when the load operation begins, and the second executes when it completes. The variable output pins will not be valid until the second pin executes. The <strong>Success</strong> pin indicates whether or not the load operation succeeded, but you can also pass the returned object to an <strong>Is Valid</strong> node, or treat failure from the <strong>Cast To</strong> node to as a catch-all for any error in the loading process.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25753238,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25753238,
              "file_name": "LoadGameBPAsync.png",
              "file_size": 60406,
              "content_type": "image/png",
              "created_at": "2025-06-20T19:14:31.706+00:00",
              "height": 208,
              "width": 1026,
              "storage_key": "61175e1d-4593-4db4-9e6d-149f97a9d4ec",
              "context": "documentation"
            },
            "storage_key": "61175e1d-4593-4db4-9e6d-149f97a9d4ec",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "MlN",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1780,
        "excerpt_assignment_id": 1447,
        "blocks": [
          {
            "type": "header",
            "content": "Asynchronous Loading",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "When loading asynchronously with <code>AsyncLoadGameFromSlot</code>, you must provide a callback delegate in order to receive the data that the system loads.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "// Set up the delegate.\n\tFAsyncLoadGameFromSlotDelegate LoadedDelegate;\n\t// USomeUObjectClass::LoadGameDelegateFunction is a void function that takes the following parameters: const FString&amp; SlotName, const int32 UserIndex, USaveGame* LoadedGameData\n\tLoadedDelegate.BindUObject(SomeUObjectPointer, &amp;USomeUObjectClass::LoadGameDelegateFunction);\n\tUGameplayStatics::AsyncLoadGameFromSlot(SlotName, 0, LoadedDelegate);",
            "lines_of_code": 5,
            "id": 64971,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2NDk3MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjU0OjE3KzAwOjAwIn0=--7e0bd63c8382455958bfd96fa3f5714669bc2c6ec3c857a0b5e442838c2334d7",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Synchronous Loading",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "The <code>LoadGameFromSlot</code> function will create and return a <code>USaveGame</code> object if it succeeds.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "// Retrieve and cast the USaveGame object to UMySaveGame.\n\tif (UMySaveGame* LoadedGame = Cast&lt;UMySaveGame&gt;(UGameplayStatics::LoadGameFromSlot(SlotName, 0)))\n\t{\n\t\t// The operation was successful, so LoadedGame now contains the data we saved earlier.\n\t\tUE_LOG(LogTemp, Warning, TEXT(&quot;LOADED: %s&quot;), *LoadedGame-&gt;PlayerName);\n\t}",
            "lines_of_code": 6,
            "id": 64972,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2NDk3MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjU0OjE3KzAwOjAwIn0=--b9e3772b8b8528574738095bd67eaa034763a6c9421937987a5e6200be176024",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Binary Loading",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You can load SaveGame data from a file in raw, binary form with <code>LoadDataFromSlot</code>. This function is very similar to <code>LoadGameFromSlot</code>, except that it does not create a SaveGame object. Only synchronous operation is available for this type of loading.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "TArray&lt;uint8&gt; OutSaveData;\n\tif (UGameplayStatics::LoadDataFromSlot(OutSaveData, SlotNameString, UserIndexInt32))\n\t{\n\t\t// The operation succeeded, and OutSaveData now contains a binary represenation of the SaveGame object.\n\t}",
            "lines_of_code": 5,
            "id": 64973,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2NDk3MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjU0OjE3KzAwOjAwIn0=--503f4a7dcbfafb69ad42f7e451b1f5c6d7ca622b9c6e92c3d7d45ad5fd8297da",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You can also convert this binary data to a SaveGame object by calling <code>LoadGameFromMemory</code>. This is a synchronous call, and returns a new <code>USaveGame</code> object upon success, or a null pointer on failure.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": "",
            "snippet_type": "cpp_programming",
            "title": "",
            "code_preview": "if (UMySaveGame* SaveGameInstance = Cast&lt;UMySaveGame&gt;(LoadGameFromMemory(InSaveData)))\n\t{\n\t\t// The operation succeeded, and SaveGameInstance was able to cast to type we expected (UMySaveGame).\n\t}",
            "lines_of_code": 4,
            "id": 64974,
            "url_signature": "eyJzbmlwcGV0X2lkIjo2NDk3NCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjU0OjE3KzAwOjAwIn0=--cd86b50ff3ed79e6f88b076c12774d1351d57be680f214701f1269d7ed0ac49b",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "am4",
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
