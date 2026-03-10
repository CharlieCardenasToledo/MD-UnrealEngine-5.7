# Running Unreal Engine

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/running-unreal-engine

> Application Version: 5.7

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "include",
        "excerpt_id": 95,
        "excerpt_assignment_id": 235,
        "blocks": [
          {
            "type": "image",
            "image_id": 24433395,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24433395,
              "file_name": "RunningUnrealEngineHeroImage_01.png",
              "file_size": 501867,
              "content_type": "image/png",
              "created_at": "2025-03-28T21:37:53.733+00:00",
              "height": 192,
              "width": 866,
              "storage_key": "ecb60063-5331-4ba0-a7ae-f6ab4fad510f",
              "context": "documentation"
            },
            "storage_key": "ecb60063-5331-4ba0-a7ae-f6ab4fad510f",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "The instructions on this page are for running the engine with projects compiled in a <strong>Development</strong> build configuration. You can substitute the <code>UEEditor-_.exe</code> or <code>UE-_.exe</code> that you need for opening projects built in other configurations. More information on the binary naming convention can be found on the <a data-document-id=\"3228638\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source\">Building Unreal Engine</a> page.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "Pq9",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "include",
        "excerpt_id": 96,
        "excerpt_assignment_id": 236,
        "blocks": [
          {
            "type": "image",
            "image_id": 24433396,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 24433396,
              "file_name": "RunningUnrealEngineHeroImage_01.png",
              "file_size": 501867,
              "content_type": "image/png",
              "created_at": "2025-03-28T21:37:54.061+00:00",
              "height": 192,
              "width": 866,
              "storage_key": "787594b3-19a5-47b5-ab22-d585d21e9fe2",
              "context": "documentation"
            },
            "storage_key": "787594b3-19a5-47b5-ab22-d585d21e9fe2",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "The instructions on this page are for running the engine with projects compiled in a <strong>Development</strong> build configuration. You can substitute the <code>UE5Editor-_.app</code> or <code>UE5-_.app</code> that you need for opening projects built in other configurations. More information on the binary naming convention can be found on the <a data-document-id=\"3228638\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source\">Building Unreal Engine</a> page.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "QRe",
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

## Running the Editor

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "include",
        "excerpt_id": 103,
        "excerpt_assignment_id": 300,
        "blocks": [
          {
            "type": "paragraph",
            "content": "The process of running the editor requires passing the name of the project to run as an argument to the executable.",
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
                "content": "You can add the <code class=\"inline-code\">-debug</code> switch to force the executable to load the debug version of the modules for your project, which contain all of the debugging symbols. This is necessary even when debugging through Visual Studio with the configuration set to <b>Debug</b> because the main executable is always compiled using the <b>Development</b> configuration. Of course, you must first compile your modules using the Debug configuration so they exist for the executable to load.",
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
        "excerpt_hash_id": "5XV",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "include",
        "excerpt_id": 104,
        "excerpt_assignment_id": 301,
        "blocks": [
          {
            "type": "paragraph",
            "content": "The process of running the editor requires passing the name of the project to run as an argument to the executable.",
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
                "content": "You can add the <code class=\"inline-code\">-debug</code> switch to force the executable to load the debug version of the modules for your project, which contain all of the debugging symbols. This is necessary even when debugging through Xcode with the configuration set to <b>Debug</b> because the main executable is always compiled using the <b>Development</b> configuration. Of course, you must first compile your modules using the Debug configuration so they exist for the executable to load.",
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
        "excerpt_hash_id": "yNb",
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

### Running the Editor from the Command Line

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "include",
        "excerpt_id": 105,
        "excerpt_assignment_id": 302,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "From a command prompt, navigate to your <code class=\"inline-code\">[LauncherInstall][VersionNumber]\\Engine\\Binaries\\Win64</code> directory.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Run the <code class=\"inline-code\">UEEditor.exe</code>, passing it the path to your project.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "shell",
                  "title": "",
                  "code_preview": "UEEditor.exe &quot;[ProjectPath][ProjectName].uproject&quot;",
                  "lines_of_code": 1,
                  "id": 35077,
                  "url_signature": "eyJzbmlwcGV0X2lkIjozNTA3NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjQ3OjMwKzAwOjAwIn0=--b5cfe50ef95ebefa9f6414836dfdc0317934972e73dc1d7978836934dfa0c408",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ]
            ],
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "qkE",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "include",
        "excerpt_id": 106,
        "excerpt_assignment_id": 303,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "From a command prompt, navigate to your <code class=\"inline-code\">[LauncherInstall]/[VersionNumber]/Engine/Binaries/Mac</code> directory.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Run the <code class=\"inline-code\">UEEditor.app</code> passing it the path to your project:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "shell",
                  "title": "",
                  "code_preview": "open UEEditor.app --args &quot;[ProjectPath]/[ProjectName].uproject&quot;",
                  "lines_of_code": 1,
                  "id": 35078,
                  "url_signature": "eyJzbmlwcGV0X2lkIjozNTA3OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjQ3OjMwKzAwOjAwIn0=--64054d020f0870479a20f03126a1b5cffb8bd5d452f12a47974c8df09384b364",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ]
            ],
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "Ram",
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

### Running the Editor from the Executable

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "include",
        "excerpt_id": 107,
        "excerpt_assignment_id": 304,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Navigate to your <code class=\"inline-code\">[LauncherInstall][VersionNumber]\\Engine\\Binaries\\Win64</code> directory.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Right-click on the <code class=\"inline-code\">UEEditor.exe</code> executable and choose <b>Create shortcut</b>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Rename the shortcut to something like <b>MyProject - Editor.exe</b> as this reflects that this shortcut runs the MyProject game editor.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Right-click on the newly created shortcut and choose <b>Properties</b>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Add the name of the game to run as an argument at the end of the <b>Target</b> property:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "shell",
                  "title": "",
                  "code_preview": "[LauncherInstall][VersionNumber]\\Engine\\Binaries\\Win64\\UEEditor.exe &quot;[ProjectPath][ProjectName].uproject&quot;",
                  "lines_of_code": 1,
                  "id": 35079,
                  "url_signature": "eyJzbmlwcGV0X2lkIjozNTA3OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjQ3OjMwKzAwOjAwIn0=--d35f0f3d1fefabc367e5ec28419279e526eb2a356f87a7ff8c594c0d405a22a0",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Press <b>OK</b> to save the changes.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Double-click the shortcut to launch the editor.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ]
            ],
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "PqN",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "include",
        "excerpt_id": 108,
        "excerpt_assignment_id": 305,
        "blocks": [
          {
            "type": "paragraph",
            "content": "The editor must be run from the command prompt to load a specific project directly (see above) or with no arguments (see below) to access the Project Browser. <br>",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "QRy",
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

```json
{
  "type": "include",
  "excerpt_id": 66,
  "excerpt_assignment_id": 237,
  "blocks": [
    {
      "type": "header",
      "content": "Running the Editor with No Arguments (Stand-alone)",
      "level": 3,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "If the editor is not set to open the most recent project at startup, running the editor executable without any arguments will launch the Project Browser. From here, you can <a data-document-id=\"3222330\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-a-new-project-in-unreal-engine\">create a new project</a> , <a data-document-id=\"3222330\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-a-new-project-in-unreal-engine\">open your existing projects</a> , or open <a data-document-id=\"3236691\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine\">content examples and sample games</a> .",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "7jE",
  "settings": {
    "is_hidden": false
  }
}
```

## Running an Uncooked Game

Once a project is loaded in Unreal Editor, you can [test your gameplay](https://dev.epicgames.com/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine#modes) in Uncooked Game mode from the **Play In** menu. To play the uncooked game in its own window, select the [New Window At > Default Player Start mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine#modes) using the [Play In dropdown menu](https://dev.epicgames.com/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine#toolbar) in the Level Editor toolbar.

![Image](https://dev.epicgames.com/community/api/documentation/image/675380d5-2cdd-48b3-8a37-bfa47aa78206)

*Click to see full-size image:*

Running the uncooked game version of the engine executable using either of the below methods will result in the same behavior.

### Running an Uncooked Game from the Command Line

When running from the command line, you must pass the name of the project you want to run along with the `-game` switch as arguments.

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "include",
        "excerpt_id": 97,
        "excerpt_assignment_id": 238,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "From a command prompt, navigate to your <code>[LauncherInstall][VersionNumber]\\Engine\\Binaries\\Win64</code> directory.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Run the <strong>UEEditor.exe</strong> passing it the path to the project to run, along with the <code>-game</code> parameter.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": null,
                  "snippet_type": "cpp_programming",
                  "title": null,
                  "code_preview": "UEEditor.exe &quot;[ProjectPath][ProjectName].uproject&quot; -game",
                  "lines_of_code": 1,
                  "id": 35068,
                  "url_signature": "eyJzbmlwcGV0X2lkIjozNTA2OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjQ3OjMwKzAwOjAwIn0=--53fcbdc60f415c37c351123b3eb25daec1c6d0a432ad8db941492a35bac18877",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ]
            ],
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "GQW",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "include",
        "excerpt_id": 98,
        "excerpt_assignment_id": 239,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "From a command prompt, navigate to your <code>[LauncherInstall][VersionNumber]/Engine/Binaries/Mac</code> directory.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Run the <strong>UEEditor.app</strong> passing it the path to the project to run, along with the <code>-game</code> parameter",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": null,
                  "snippet_type": "cpp_programming",
                  "title": null,
                  "code_preview": "open UEEditor.app --args &quot;[ProjectPath]/[ProjectName].uproject&quot; -game",
                  "lines_of_code": 1,
                  "id": 35069,
                  "url_signature": "eyJzbmlwcGV0X2lkIjozNTA2OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjQ3OjMwKzAwOjAwIn0=--e6ea8cff5386d39f45c170581759da09e8c13de2098e469c6635c10086983939",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ]
            ],
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "Z9r",
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

### Running an Uncooked Game from the Executable

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "include",
        "excerpt_id": 99,
        "excerpt_assignment_id": 240,
        "blocks": [
          {
            "type": "paragraph",
            "content": "When running from the executable, you must specify the path to the project you want to run along with the <code>-game</code> switch as arguments to the executable via the <strong>Target</strong> property of a shortcut.",
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
                  "content": "Navigate to your <code>[LauncherInstall][VersionNumber]\\Engine\\Binaries\\Win64</code> directory.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "<strong>Right-click</strong> on the <strong>UEEditor.exe</strong> executable and choose <strong>Create shortcut</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Rename the shortcut to reflect the game it will run, i.e. <strong>MyProject.exe</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "<strong>Right-click</strong> on the newly created shortcut and choose <strong>Properties</strong> to display the properties of the shortcut.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Add the full path to the project to run as an argument at the end of the <strong>Target</strong> property, and specify the <code>-game</code> argument to run as a game:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": null,
                  "snippet_type": "cpp_programming",
                  "title": null,
                  "code_preview": "[LauncherInstall][VersionNumber]\\Engine\\Binaries\\Win64\\UEEditor.exe &quot;[ProjectPath][ProjectName].uproject&quot; -game",
                  "lines_of_code": 1,
                  "id": 35070,
                  "url_signature": "eyJzbmlwcGV0X2lkIjozNTA3MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjQ3OjMwKzAwOjAwIn0=--ceee74013fd76e08512016c9f1024252dcee8971ab8b59907b9f12782aeaa0e8",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Press <strong>OK</strong> to save the changes.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "<strong>Double-click</strong> the shortcut to run the game.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ]
            ],
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "nP6",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "paragraph",
        "content": "The editor must be run <a data-document-id=\"3223149\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/running-unreal-engine\">from the command line</a> to load a specific project directly.",
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

## Running a Cooked Game

See [Packaging Projects](https://dev.epicgames.com/documentation/en-us/unreal-engine/packaging-your-project?application_version=5.5) for information on how to package and run cooked game builds

## Useful In-Game Commands

When you are running the game, there are a multitude of **console commands** you can use in the console inside the game. The console can be summoned by pressing the **~ (tilde)** or **Tab** keys. Some of the most useful commands are listed below.

- `EXIT/QUIT`
- `DISCONNECT`
- `OPEN [MapURL]`
- `TRAVEL [MapURL]`
- `VIEWMODE [Mode]`

## Loading Maps

It is possible to specify a particular map to load when running the engine or editor or load a new map while running the engine. This can be useful for testing by quickly jumping into the map you want to test without needing to make your way through a series of menus.

```json
{
  "type": "include",
  "excerpt_id": 100,
  "excerpt_assignment_id": 241,
  "blocks": [
    {
      "type": "header",
      "content": "Loading Maps at Startup",
      "level": 3,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The engine will always attempt to load a default map when it is run. This map is specified in the <code>DefaultEngine.ini</code> config file located in the <code>Config</code> folder of your game project. The map to run by default is set using the <strong>Map</strong> property in the <code>[URL]</code> section of the .ini file. As an example, when you create a project with a map file named \"MyMap\", the following is set automatically in its <code>DefaultEngine.ini</code> file:",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "code_snippet",
      "description": null,
      "snippet_type": "cpp_programming",
      "title": null,
      "code_preview": "GameDefaultMap=/Game/Maps/MyMap",
      "lines_of_code": 1,
      "id": 35071,
      "url_signature": "eyJzbmlwcGV0X2lkIjozNTA3MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjQ3OjMwKzAwOjAwIn0=--0218c38d613f4aefb2bc497f98d626a9eb09bb3e9585a3f5a7b09c2329e36a44",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "This will cause the <code>MyMap.umap</code> (located in <code>(UE4Directory)/(YourProjectName)/Content/Maps</code>) to load at startup unless it is overridden. Generally, you will want to specify the map that loads or is used as the background for your main menu as the default map.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "elR",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "include",
        "excerpt_id": 102,
        "excerpt_assignment_id": 243,
        "blocks": [
          {
            "type": "paragraph",
            "content": "To override the default map, you can pass in a map name (without the file extension) as a command line argument. It was mentioned previously that you must specify the project name on the command line. Following these, you can also specify a map name to force the engine to load a map other than the default. For instance, the following command line could be used to load the engine running the <code>ExampleMap</code> map:",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": null,
            "snippet_type": "cpp_programming",
            "title": null,
            "code_preview": "UEEditor.exe &quot;[ProjectPath][ProjectName].uproject&quot; ExampleMap -game",
            "lines_of_code": 1,
            "id": 35073,
            "url_signature": "eyJzbmlwcGV0X2lkIjozNTA3MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjQ3OjMwKzAwOjAwIn0=--c3044f0650d4062ebd8054fc0e9264b77bda1906649cf20c3ad0ceb11c86b609",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "z3Z",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "include",
        "excerpt_id": 101,
        "excerpt_assignment_id": 242,
        "blocks": [
          {
            "type": "paragraph",
            "content": "To override the default map, you can pass in a map name (without the file extension) as a command line argument. It was mentioned previously that you must specify the project name on the command line. Following these, you can also specify a map name to force the engine to load a map other than the default. For instance, the following command line could be used to load the engine running the <code>ExampleMap</code> map:",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "code_snippet",
            "description": null,
            "snippet_type": "cpp_programming",
            "title": null,
            "code_preview": "open UEEditor.app --args &quot;[ProjectPath]/[ProjectName].uproject&quot; ExampleMap -game",
            "lines_of_code": 1,
            "id": 35072,
            "url_signature": "eyJzbmlwcGV0X2lkIjozNTA3MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjQ3OjMwKzAwOjAwIn0=--884e0d268d20ff9a832304ef3912061546760c269292b94e127f0982ee393cbd",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "bl6",
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

The same concept works when running the editor. Specifying the name of the map to load will load that map when the editor opens instead of the default or blank map. To load the editor with the `ExampleMap` map loaded, the following command line can be used:

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "paragraph",
        "content": "<code>UE4Editor.exe \"[ProjectPath][ProjectName].uproject\" ExampleMap -game</code>",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "paragraph",
        "content": "<code>open UEEditor.app --args \"[ProjectPath]/[ProjectName].uproject\" ExampleMap</code>",
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

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The map name can also be a full map URL specifying additional settings such as the GameMode. Settings are appended to the map name as key-value pairs separated by a <code>?</code>. For example:",
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
  "code_preview": "DM-Deck?Game=CaptureTheFlag",
  "lines_of_code": 1,
  "id": 35074,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTA3NCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjQ3OjI4KzAwOjAwIn0=--e2198ece132539aa50cec950131636fa5692a55dcd85a5b320f090cd209eb033",
  "settings": {
    "is_hidden": false
  }
}
```

### Loading New Maps

If you want to load a new map during play, in order to test during development or even to switch maps during gameplay, this can be done using the `OPEN` or `TRAVEL` console commands followed by the name of the map (without the file extension) to load.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The difference between the <code>OPEN</code> and <code>TRAVEL</code> commands is described above in the <a data-document-id=\"3223149\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/running-unreal-engine\">Useful In-Game Commands</a> section.",
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

The commands below load the DM-Deck map during play with the same settings or settings reset, respectively:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "open DM-Deck",
  "lines_of_code": 1,
  "id": 35075,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTA3NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjQ3OjI4KzAwOjAwIn0=--2c64eab1c67bfbd64fd88db78a219a805a9eb94ac5752db8eccf1e20c05dc52c",
  "settings": {
    "is_hidden": false
  }
}
```

Or

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "travel DM-Deck",
  "lines_of_code": 1,
  "id": 35076,
  "url_signature": "eyJzbmlwcGV0X2lkIjozNTA3NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjQ3OjI4KzAwOjAwIn0=--682c43bb16b36c5535056c86c9a1310c7a80e5d4d1604fe89c5ad55bea21ee94",
  "settings": {
    "is_hidden": false
  }
}
```
