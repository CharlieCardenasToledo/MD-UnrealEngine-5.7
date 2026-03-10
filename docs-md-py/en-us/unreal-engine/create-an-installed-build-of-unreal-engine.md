# Create an Installed Build

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/create-an-installed-build-of-unreal-engine

> Application Version: 5.7

When working on a source build of an **Unreal Engine (UE)** project with a team, some team members might not have the necessary software or knowledge to [build and run Unreal Engine from source](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source). In these cases, you can build Unreal Engine binaries and distribute them to your team as an **installed build**. This creates a package similar to what is deployed by the Epic Games Launcher.

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "include",
        "excerpt_id": 1674,
        "excerpt_assignment_id": 2273,
        "blocks": [
          {
            "type": "paragraph",
            "content": "For more general instructions on how to create an Installed Build, refer to the <a data-document-id=\"3234288\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/installed-build-reference-guide-for-unreal-engine\">Installed Build Reference Guide</a>. This page provides additional information and steps for developers using <strong>Windows</strong>.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "oqX",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "include",
        "excerpt_id": 1675,
        "excerpt_assignment_id": 2274,
        "blocks": [
          {
            "type": "paragraph",
            "content": "For more general instructions on how to create an Installed Build, refer to the <a data-document-id=\"3234288\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/installed-build-reference-guide-for-unreal-engine\">Installed Build Reference Guide</a>. This page provides additional information and steps for developers using <strong>macOS</strong>.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "LQb",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "linux": [
      {
        "type": "include",
        "excerpt_id": 1676,
        "excerpt_assignment_id": 2275,
        "blocks": [
          {
            "type": "paragraph",
            "content": "For more general instructions on how to create an Installed Build, refer to the <a data-document-id=\"3234288\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/installed-build-reference-guide-for-unreal-engine\">Installed Build Reference Guide</a>. This page provides additional information and steps for developers using <strong>Linux</strong>.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "X9d",
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

## Prerequisites

Before you make an installed build, make sure you have the following prerequisites:

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "include",
        "excerpt_id": 1677,
        "excerpt_assignment_id": 2276,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "unordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "A <a data-document-id=\"3228638\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source\">source code build of Unreal Engine</a>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "<a href=\"https://dotnet.microsoft.com/en-us/download/dotnet/6.0/runtime?cid=getdotnetcore&os=windows&arch=x64\">Windows DotNet 6.0 Runtime</a>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Windows Debugging Tools component for Windows 10 SDK (Windows 10 only – See below).",
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
        "excerpt_hash_id": "1lV",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "include",
        "excerpt_id": 1678,
        "excerpt_assignment_id": 2277,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "unordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "A <a data-document-id=\"3228638\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source\">source code build of Unreal Engine</a>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "A compatible installation of Xcode with all MacOS <a data-document-id=\"3236220\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/macos-development-requirements-for-unreal-engine?application_version=5.5\">development requirements</a>.",
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
        "excerpt_hash_id": "gM8",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "linux": [
      {
        "type": "include",
        "excerpt_id": 1679,
        "excerpt_assignment_id": 2278,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "unordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "A <a data-document-id=\"3228638\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source\">source code build of Unreal Engine</a>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "You must have the appropriate OS components and libraries for using UE with Linux.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Your source code must have Linux line endings to compile on Linux.",
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
        "excerpt_hash_id": "MG9",
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

### Recommended Hardware

We recommend you use a machine with a high processor core/thread count for builds. While UE builds on a single core, build times are significantly reduced with multi-core processors. See [Hardware and Software Specifications](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-and-software-specifications-for-unreal-engine?application_version=5.5) for more details on recommended hardware.

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "include",
        "excerpt_id": 1680,
        "excerpt_assignment_id": 2279,
        "blocks": [
          {
            "type": "header",
            "content": "Windows 10 SDK (Windows 10 users only)",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "On Windows 10, you need to install the <a href=\"https://developer.microsoft.com/en-us/windows/downloads/sdk-archive/\">Windows Debugging Tools component in the Windows 10 SDK</a>. This enables <code>PDBCopy.exe</code>, which is used in the build process to strip symbols and optimize the resulting package size.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "If you do not already have the Windows 10 SDK installed, follow these steps:",
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
                  "content": "<a href=\"https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/\">Download and install the Windows 10 SDK from Microsoft's site</a>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "When you reach the dialogue that says <strong>select the features you want to install</strong>, make sure <strong>Debugging Tools for Windows</strong> is checked, then proceed with the installation.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25738655,
                  "caption": "",
                  "alt_text": "Debugging Tools for Windows is selected in the feature selection dialog for the Windows 10 SDK installer.",
                  "image": {
                    "id": 25738655,
                    "file_name": "DebuggingForWindows.png",
                    "file_size": 109407,
                    "content_type": "image/png",
                    "created_at": "2025-06-16T21:22:38.346+00:00",
                    "height": 815,
                    "width": 1105,
                    "storage_key": "7e75d2cc-a889-4057-8792-4cb833565f72",
                    "context": "documentation"
                  },
                  "storage_key": "7e75d2cc-a889-4057-8792-4cb833565f72",
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
                  "content": "Proceed with the installation.",
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
            "content": "If you already have the Windows 10 SDK set up, but don’t have Debugging Tools for Windows, follow these steps:",
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
                  "content": "Open <strong>Add or Remove Programs.</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "In the list of available programs, locate your Windows Software Development Kit installation. Click <strong>Modify</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25738656,
                  "caption": "",
                  "alt_text": "Modifying the Windows SDK in Add or Remove Programs",
                  "image": {
                    "id": 25738656,
                    "file_name": "ModifyWindowsSDK.png",
                    "file_size": 6388,
                    "content_type": "image/png",
                    "created_at": "2025-06-16T21:22:38.591+00:00",
                    "height": 156,
                    "width": 476,
                    "storage_key": "d1703e06-b34d-4253-b825-7dc6aa1939e8",
                    "context": "documentation"
                  },
                  "storage_key": "d1703e06-b34d-4253-b825-7dc6aa1939e8",
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
                  "content": "In the list of options that appears, check <strong>Change</strong> and click <strong>Next.</strong>",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "When you see the dialog that says <strong>select the features you want to change</strong>, check <strong>Debugging Tools for Windows</strong>, then click <strong>Change</strong> to proceed with the installation.",
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
        "excerpt_hash_id": "a09",
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

## Make an Installed Build

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "include",
        "excerpt_id": 1681,
        "excerpt_assignment_id": 2280,
        "blocks": [
          {
            "type": "paragraph",
            "content": "To make an Installed Build on Windows, follow these steps:",
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
                  "content": "Regenerate your Unreal Engine project files.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "enhanced_list",
                  "style": "unordered",
                  "items": [
                    [
                      {
                        "type": "paragraph",
                        "content": "If you encounter error messages when attempting to regenerate project files, double check that you have the <a href=\"https://dotnet.microsoft.com/en-us/download/dotnet/6.0/runtime\">Windows DotNet 6.0 runtime</a> installed.",
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
              [
                {
                  "type": "paragraph",
                  "content": "Use <code>RunUAT.bat</code> to create an installed build. The following is an example of a BuildGraph command to create an installed build for Windows:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "Command Line",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "RunUAT.bat BuildGraph -script=Engine/Build/InstalledEngineBuild.xml -target=&quot;Make Installed Build Win64&quot; -nosign -set:GameConfigurations=Development;Shipping -set:WithWin64=true -set:WithAndroid=true -set:WithDDC=false -set:WithLinux=false -set:WithLinuxArm64=false -set:WithIOS=false -set:WithTVOS=false -set:WithMac=false -clean",
                  "lines_of_code": 1,
                  "id": 60155,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDE1NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI4OjQ1KzAwOjAwIn0=--f0625ae06bbb9433dff9838efbc64ebcb5911a4430eb1e067498b9f86e27e1bc",
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
                      "content": "Make sure you specify whether or not every platform that you have available should be added or not. If you have additional platforms not mentioned here in your source code, add <code>-Set:With[Platform]=true</code> or <code>-Set:With[Platform]=false</code> according to your project’s needs, where [Platform] is replaced with the name of the added platform.",
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
                  "content": "The details about the parameters used in the above example are as follows:",
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
                          "content": "Parameter",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "enhanced_table_header",
                          "content": "Required or Optional",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "enhanced_table_header",
                          "content": "Description",
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
                          "content": "<code>-target=\"Make Installed Build Win64”</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Required",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Instructs BuildGraph to run a specific operation. This graph of dependencies is described in the script=\"Engine/Build/InstalledEngineBuild.xml\" and there are other options available that may meet your requirements better, but for the purposes of this document our example targets a build that matches what a user would receive from the launcher version of Unreal Engine.",
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
                          "content": "<code>-set With[Platform]=true</code> or <code>-set With[Platform]=false</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Required",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Specifies whether or not support for a given platform should be added to your installed build, where [Platform] is replaced with the name of a platform you want to enable or disable. <strong>Make sure to add this parameter for every platform you have source code for. </strong>For details on which platforms to enable or disable, refer to the Required Platforms section below.",
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
                          "content": "<code>-set:GameConfigurations=Development;Shipping</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Required",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Flag for different versions of the editor. We recommend including <strong>Development </strong>and <strong>Shipping</strong>.",
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
                          "content": "<code>-set WithClient=false</code> and <code>-set WithServer=false</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Optional",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Specifies whether to create Client and Server builds for network multiplayer projects. Defaults to false.",
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
                          "content": "<code>-set WithDDC=false</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Optional",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Specifies whether to create a build that includes <a data-document-id=\"3234030\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/using-derived-data-cache-in-unreal-engine\">Derived Data Cache</a> support. Defaults to false.",
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
                          "content": "<code>-clean</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Recommended",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Performs a fresh recompile of the project. Remove this parameter if you encounter an \"Other Compilation Error” message.",
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
                  "type": "callout",
                  "callout_type": "note",
                  "blocks": [
                    {
                      "type": "paragraph",
                      "content": "If you receive an \"Other Compilation Error\" message, remove the <code>-clean</code> parameter and try again, as there are known issues with this command on Linux.",
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
                  "content": "Build the Shader Compiler Worker.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "Engine\\Build\\BatchFiles\\Build.bat ShaderCompileWorker Win64 Development",
                  "lines_of_code": 1,
                  "id": 60156,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDE1NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI4OjQ1KzAwOjAwIn0=--b8d96f2e4e03d62030b5c46ac8c6c053684f32214a6a8206b6418f6d26b7ab0f",
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
            "content": "Your build appears in the Windows directory where Feature Packs, Templates, and Engine are located for distribution.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "JRe",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "include",
        "excerpt_id": 1682,
        "excerpt_assignment_id": 2281,
        "blocks": [
          {
            "type": "paragraph",
            "content": "To make an installed build on MacOS, follow these steps:",
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
                  "content": "Open your Unreal Engine source directory and run <code>GenerateProjectFiles.command</code> in Terminal.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "image",
                  "image_id": 25738657,
                  "caption": "",
                  "alt_text": "Message upon generating project files.",
                  "image": {
                    "id": 25738657,
                    "file_name": "MacProjectFiles.png",
                    "file_size": 209894,
                    "content_type": "image/png",
                    "created_at": "2025-06-16T21:22:38.915+00:00",
                    "height": 671,
                    "width": 1014,
                    "storage_key": "84a05ede-21a6-41ef-a77b-d734deb3bf64",
                    "context": "documentation"
                  },
                  "storage_key": "84a05ede-21a6-41ef-a77b-d734deb3bf64",
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
                  "content": "Use <code class=\"inline-code\">RunUAT.sh</code> to create an installed build:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "Command Line",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "RunUAT.sh BuildGraph -script=Engine/Build/InstalledEngineBuild.xml -target=&quot;Make Installed Build Mac&quot; -nosign** **-set:WithWin64=false** -set:WithAndroid=true** -set:WithDDC=false -set:WithLinux=false -set:WithLinuxArm64=false **-set:WithTVOS=false -set:WithIOS=true -set:WithMac=true** -clean",
                  "lines_of_code": 1,
                  "id": 60157,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDE1NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI4OjQ1KzAwOjAwIn0=--bbd0e87aeab26a70e08892fe3b3bf4f06d403f3544277fd24a4c3ed2ca11eac8",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "The details about the parameters used in the above example are as follows:",
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
                          "content": "Parameter",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "enhanced_table_header",
                          "content": "Required or Optional",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "enhanced_table_header",
                          "content": "Description",
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
                          "content": "<code>-target=\"Make Installed Build Mac\"</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Required",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Instructs BuildGraph to run a specific operation. This graph of dependencies is described in the script=\"Engine/Build/InstalledEngineBuild.xml\" and there are other options available that may meet your requirements better, but for the purposes of this document our example targets a build that matches what a user would receive from the launcher version of Unreal Engine.",
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
                          "content": "<code>-set With[Platform]=true</code> or <code>-set With[Platform]=false</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Required",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Specifies whether or not support for a given platform should be added to your installed build, where [Platform] is replaced with the name of a platform you want to enable or disable. <strong>Make sure to add this parameter for every platform you have source code for. </strong>For details on which platforms to enable or disable, refer to the Required Platforms section below.",
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
                          "content": "<code>-set:GameConfigurations=Development;Shipping</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Required",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Flag for different versions of the editor. We recommend including <strong>Development </strong>and <strong>Shipping</strong>.",
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
                          "content": "<code>-set WithClient=false</code> and <code>-set WithServer=false</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Optional",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Specifies whether to create Client and Server builds for network multiplayer projects. Defaults to false.",
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
                          "content": "<code>-set WithDDC=false</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Optional",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Specifies whether to create a build that includes <a data-document-id=\"3234030\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/using-derived-data-cache-in-unreal-engine\">Derived Data Cache</a> support. Defaults to false.",
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
                          "content": "<code>-clean</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Recommended",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Performs a fresh recompile of the project. Remove this parameter if you encounter an \"Other Compilation Error” message.",
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
                  "type": "callout",
                  "callout_type": "note",
                  "blocks": [
                    {
                      "type": "paragraph",
                      "content": "Make sure you specify all platforms that should not be built. If you receive an \"Other Compilation Error\" message, remove the <code>-clean</code> parameter and try again, as there are known issues with this command on Linux.",
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
                  "content": "Build the Shader Compiler Worker.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "Command Line",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "/Engine/Build/BatchFiles/Mac/Build.sh ShaderCompileWorker MacDevelopment",
                  "lines_of_code": 1,
                  "id": 60158,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDE1OCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI4OjQ1KzAwOjAwIn0=--a63e24a3de2ef8addcc3ee93a921c2e30549921fd967acd476fe67a7ea4ac5a4",
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
            "type": "image",
            "image_id": 25738658,
            "caption": "",
            "alt_text": "Build message upon building the shader compile worker",
            "image": {
              "id": 25738658,
              "file_name": "MacBuildShaderCompileWorker.png",
              "file_size": 146364,
              "content_type": "image/png",
              "created_at": "2025-06-16T21:22:39.075+00:00",
              "height": 334,
              "width": 1309,
              "storage_key": "d4deeef1-f5c7-42c9-9c17-fc10e8222295",
              "context": "documentation"
            },
            "storage_key": "d4deeef1-f5c7-42c9-9c17-fc10e8222295",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "6rM",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "linux": [
      {
        "type": "include",
        "excerpt_id": 1683,
        "excerpt_assignment_id": 2282,
        "blocks": [
          {
            "type": "callout",
            "callout_type": "note",
            "blocks": [
              {
                "type": "paragraph",
                "content": "If you follow the steps in this section and encounter a line ending or permissions error, follow the steps in How to Fix Linux Line Endings and Permissions below to fix your line endings, then try again.",
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
            "content": "To make an installed build on Linux, follow these steps:",
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
                  "content": "Run <code>Setup.sh</code> to obtain necessary binary packages and run your toolchain configuration.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Run <code>GenerateProjectFiles.sh</code> to generate your IDE’s project files.",
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
                      "content": "If you encounter <code>permission denied</code> errors on a file, refer to the previous section to correct their line endings. You might need to run the <code>chmod</code> command on additional files. After that, run <code>GenerateProjectFiles.sh</code> again.",
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
                  "content": "Use <code>RunUAT.sh</code> to create an installed build. The following is an example of a BuildGraph command to create an installed build for Linux:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "Command Line",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "/RunUAT.sh BuildGraph -script=Engine/Build/InstalledEngineBuild.xml -target=&quot;Make Installed Build Linux&quot; -nosign **-set:GameConfigurations=Development;Shipping **-set:WithWin64=false** -set:WithAndroid=true** -set:WithDDC=false **-set:WithLinux=true** -set:WithLinuxArm64=false -set:WithTVOS=false -set:WithMac=false -clean",
                  "lines_of_code": 1,
                  "id": 60159,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDE1OSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI4OjQ1KzAwOjAwIn0=--d00b5dff91dd9e3420c430ddc7d314af88f1ebe9e3ee62805268f2d923bf7df3",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "The details about the parameters used in the above example are as follows:",
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
                          "content": "Parameter",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "enhanced_table_header",
                          "content": "Required or Optional",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "enhanced_table_header",
                          "content": "Description",
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
                          "content": "<code>-target=\"Make Installed Build Linux”</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Required",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Instructs BuildGraph to run a specific operation. This graph of dependencies is described in the script=\"Engine/Build/InstalledEngineBuild.xml\" and there are other options available that may meet your requirements better, but for the purposes of this document our example targets a build that matches what a user would receive from the launcher version of Unreal Engine.",
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
                          "content": "<code>-set With[Platform]=true</code> or <code>-set With[Platform]=false</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Required",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Specifies whether or not support for a given platform should be added to your installed build, where [Platform] is replaced with the name of a platform you want to enable or disable. <strong>Make sure to add this parameter for every platform you have source code for. </strong>For details on which platforms to enable or disable, refer to the Required Platforms section below.",
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
                          "content": "<code>-set:GameConfigurations=Development;Shipping</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Required",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Flag for different versions of the editor. We recommend including <strong>Development </strong>and <strong>Shipping</strong>.",
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
                          "content": "<code>-set WithClient=false</code> and <code>-set WithServer=false</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Optional",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Specifies whether to create Client and Server builds for network multiplayer projects. Defaults to false.",
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
                          "content": "<code>-set WithDDC=false</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Optional",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Specifies whether to create a build that includes <a data-document-id=\"3234030\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/using-derived-data-cache-in-unreal-engine\">Derived Data Cache</a> support. Defaults to false.",
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
                          "content": "<code>-clean</code>",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Recommended",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Performs a fresh recompile of the project. Remove this parameter if you encounter an \"Other Compilation Error” message.",
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
                  "type": "callout",
                  "callout_type": "note",
                  "blocks": [
                    {
                      "type": "paragraph",
                      "content": "Make sure you specify all platforms that should not be built. If you receive an \"Other Compilation Error\" message, remove the <code>-clean</code> parameter and try again, as there are known issues with this command on Linux.",
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
                  "content": "Build the <strong>Shader Compile Worker</strong> using <code>Build.sh</code>. The following is an example of a command to build the Shader Compile Worker:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "Command Line",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "/Engine/Build/BatchFiles/Linux/Build.sh ShaderCompileWorker Linux Development",
                  "lines_of_code": 1,
                  "id": 60160,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDE2MCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI4OjQ1KzAwOjAwIn0=--1500820ddd2310175c7d87e7bfbdd9702f3c77975c799b48056572c5fa7dd3a9",
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
            "content": "You now have a build of Unreal Editor in <code>LocalBuilds/Engine/Linux</code> that you can copy to other machines or docker images and run on Linux.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "mv6",
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

### Required Platforms

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "include",
        "excerpt_id": 1684,
        "excerpt_assignment_id": 2283,
        "blocks": [
          {
            "type": "paragraph",
            "content": "When creating installed builds on Windows, make sure you enable the following platforms with the <code>-With[Platform]</code> parameter:",
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
                    "content": "Platform",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "enhanced_table_header",
                    "content": "Parameter",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "enhanced_table_header",
                    "content": "Description",
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
                    "content": "Android",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<code>-set WithAndroid=true</code>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Required to support publishing on Android, which is the target platform for most HMI projects.",
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
                    "content": "Windows 64-bit",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<code>-set WithWin64=true</code>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Required to support building the editor on Windows.",
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
            "type": "paragraph",
            "content": "Disable all other platforms, as they are not necessary for either running Unreal Editor or packaging HMI projects.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "47L",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "include",
        "excerpt_id": 1685,
        "excerpt_assignment_id": 2284,
        "blocks": [
          {
            "type": "paragraph",
            "content": "When creating installed builds on macOS, make sure you enable the following platforms with the <code>-With[Platform]</code> parameter:",
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
                    "content": "Platform",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "enhanced_table_header",
                    "content": "Parameter",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "enhanced_table_header",
                    "content": "Description",
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
                    "content": "MacOS",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<code>-set WithMac=true</code>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Required to support building the editor on Windows.",
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
                    "content": "Android",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<code>-set WithAndroid=true</code>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Required to support publishing on Android, which is the target platform for most HMI projects.",
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
                    "content": "iOS",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<code>-set WithIOS=true</code>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Required to support publishing on iOS, which you may also want to support.",
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
                    "content": "tvOS",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<code>-set WithtvOS=false</code>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "tvOS is not supported for HMI projects, and should be disabled.",
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
            "type": "paragraph",
            "content": "Disable all other platforms, as they are not necessary for either running Unreal Editor or packaging HMI projects.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "xVv",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "linux": [
      {
        "type": "include",
        "excerpt_id": 1686,
        "excerpt_assignment_id": 2285,
        "blocks": [
          {
            "type": "paragraph",
            "content": "When creating installed builds on Linux, make sure you enable the following platforms with the <code>-With[Platform]</code> parameter:",
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
                    "content": "Platform",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "enhanced_table_header",
                    "content": "Parameter",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "enhanced_table_header",
                    "content": "Description",
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
                    "content": "Android",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<code>-set WithAndroid=true</code>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Required to support publishing on Android, which is the target platform for most HMI projects.",
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
                    "content": "Linux",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<code>-set WithLinux=true</code>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Required to support building the editor on Linux.",
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
                    "content": "Linux ARM64",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "<code>-set WithLinuxArm64=true</code>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Required if you intend to support ARM64 Linux devices.",
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
        "excerpt_hash_id": "Ba6",
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
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "linux": [
      {
        "type": "include",
        "excerpt_id": 1687,
        "excerpt_assignment_id": 2286,
        "blocks": [
          {
            "type": "header",
            "content": "How to Fix Linux Line Endings and Permissions",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Depending on the way you pull your source code from your source control, the <strong>line endings</strong> in your code may change. Windows uses CR LF (Carriage Return Line Feed), while Mac and Linux use LF (Line Feed).",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "callout",
            "callout_type": "tip",
            "blocks": [
              {
                "type": "paragraph",
                "content": "For more information about line endings, see <a href=\"https://learn.microsoft.com/en-us/visualstudio/ide/encodings-and-line-breaks\">Microsoft’s documentation on encoding and line break characters</a>.",
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
            "content": "Windows line endings are not compatible with Linux. Therefore, you might encounter an error when compiling on Linux. If you encounter a line ending error, follow these steps to fix them:",
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
                  "content": "To fix your line endings, open your command line and use the <code>find</code> command and search for all files in your Unreal Engine directory with a <code>.sh</code> extension, then run the <code>chmod</code> command on each one to make them executable. For example:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "Command Line",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "find C:/Epic Games/UE-5.3/Source -type f -iname &quot;*.sh&quot; -exec chmod +x {} \\;",
                  "lines_of_code": 1,
                  "id": 60161,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDE2MSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI4OjQ1KzAwOjAwIn0=--308cda14d2cd26df3f79914da6ab3378891aee074b4c56885403dc73eff25a0f",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "The parameters of this command are as follows:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "enhanced_table",
                  "widths": [
                    "44.9091%",
                    "55.0909%"
                  ],
                  "rows": [
                    [
                      [
                        {
                          "type": "enhanced_table_header",
                          "content": "Parameter",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "enhanced_table_header",
                          "content": "Description",
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
                          "content": "-type f",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Find normal files only. This skips directories, symlinks, named pipes and sockets, and special files found in /dev.",
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
                          "content": "-iname",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Ignore case in the name.",
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
                          "content": "\"*.sh\"",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Tells the <code>find</code> command to search for files with a <code>.sh</code> extension.",
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
                          "content": "-exec chmod +x {}",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Carry out a <code>chmod</code> command on each file found and make each file executable.",
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
                          "content": "\\;",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Indicates the end of the command.",
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
              [
                {
                  "type": "paragraph",
                  "content": "To catch executable files that don’t use a <code>.sh</code> extension, change your directory to your Unreal Engine install directory, then run the following chmod commands:",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "code_snippet",
                  "description": "",
                  "snippet_type": "cpp_programming",
                  "title": "",
                  "code_preview": "chmod +x Engine/Binaries/ThirdParty/Mono/Linux/bin/mono\n         chmod +x Engine/Binaries/ThirdParty/Mono/Linux/bin/csc\n         chmod +x Engine/Binaries/ThirdParty/Mono/Linux/bin/xbuild\n         chmod +x Engine/Binaries/ThirdParty/Mono/Linux/bin/mcs\n         chmod +x Engine/Binaries/Linux/dump_syms\n         chmod +x Engine/Binaries/Linux/BreakpadSymbolEncoder\n         chmod +x Engine/Binaries/Linux/UnrealCEFSubProcess\n         chmod +x Engine/Binaries/Linux/UnrealVersionSelector-Linux-Shipping\n         chmod +x Engine/Source/ThirdParty/Intel/ISPC/bin/Linux/ispc",
                  "lines_of_code": 9,
                  "id": 60162,
                  "url_signature": "eyJzbmlwcGV0X2lkIjo2MDE2MiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI4OjQ1KzAwOjAwIn0=--a3cf043daf45134ce6950cdb4d535ef4bcc6f49b68f19c226d9ba0975cb5a86c",
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
        "excerpt_hash_id": "vO2",
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

## Test the Installed Build Executable

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "include",
        "excerpt_id": 1688,
        "excerpt_assignment_id": 2287,
        "blocks": [
          {
            "type": "paragraph",
            "content": "Installed builds appear in the LocalBuilds folder under <code>LocalBuilds/Engine/Linux/Engine/Binaries/Win64</code>. On the Windows operating system, <code>UnrealEditor.exe</code> is the main executable for the Unreal Editor. Run this executable to test your build.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25738659,
            "caption": "",
            "alt_text": "The location of UEEditor.exe",
            "image": {
              "id": 25738659,
              "file_name": "UEEditorLocation.png",
              "file_size": 62113,
              "content_type": "image/png",
              "created_at": "2025-06-16T21:22:39.896+00:00",
              "height": 604,
              "width": 654,
              "storage_key": "ddd31465-43e3-42b7-8323-a5c20ffc4f79",
              "context": "documentation"
            },
            "storage_key": "ddd31465-43e3-42b7-8323-a5c20ffc4f79",
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
                "content": "When you run your installed build for the first time, a prompt appears to ask for firewall permissions. We advise that you accept these permissions for full functionality.",
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
            "content": "To archive and distribute the build, place your installed build in the top directory of your source control repository alongside the FeaturePacks, Templates, and Engine directories.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "callout",
            "callout_type": "note",
            "blocks": [
              {
                "type": "image",
                "image_id": 25738660,
                "caption": "",
                "alt_text": "An error stating \"unable to launch ShaderCompileWorker\"",
                "image": {
                  "id": 25738660,
                  "file_name": "ShaderCompilerWorkerError.png",
                  "file_size": 5700,
                  "content_type": "image/png",
                  "created_at": "2025-06-16T21:22:40.007+00:00",
                  "height": 156,
                  "width": 407,
                  "storage_key": "32b6d1a3-412b-497d-afc0-cc6e50b80eaf",
                  "context": "documentation"
                },
                "storage_key": "32b6d1a3-412b-497d-afc0-cc6e50b80eaf",
                "context": "documentation",
                "width": null,
                "settings": {
                  "is_hidden": false
                }
              },
              {
                "type": "paragraph",
                "content": "If you see a prompt stating \"Unable to launch ShaderCompileWorker\" or experience a crash  while compiling shaders, the Shader Compiler Worker has not been built yet. Revisit the last step of the workflow under Make an Installed Build above. We build Shader Compiler Worker separately so that you do not need to rebuild Shader Compiler Worker every time you build the editor.",
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
        "excerpt_hash_id": "e1Y",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "include",
        "excerpt_id": 1689,
        "excerpt_assignment_id": 2288,
        "blocks": [
          {
            "type": "paragraph",
            "content": "Installed builds appear in <code>LocalBuilds/Engine/Mac/Engine/Binaries/Mac</code>. On the MacOS operating system, the <code>UEEditor</code> application file is the main executable for the Unreal Editor. Run this executable in a terminal shell to test your build.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25738661,
            "caption": "",
            "alt_text": "The Unreal Editor executable in the Binaries/Mac directory",
            "image": {
              "id": 25738661,
              "file_name": "UEEditorMacLoc.png",
              "file_size": 93281,
              "content_type": "image/png",
              "created_at": "2025-06-16T21:22:40.191+00:00",
              "height": 446,
              "width": 539,
              "storage_key": "6a811ff3-a3a9-437b-8e2c-4fff6f15c6b0",
              "context": "documentation"
            },
            "storage_key": "6a811ff3-a3a9-437b-8e2c-4fff6f15c6b0",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "To archive and distribute the build, place your installed build in the top directory of your source control repository alongside the FeaturePacks, Templates, and Engine directories.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "boA",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "linux": [
      {
        "type": "include",
        "excerpt_id": 1690,
        "excerpt_assignment_id": 2289,
        "blocks": [
          {
            "type": "paragraph",
            "content": "Installed builds appear in the LocalBuilds folder under <code>LocalBuilds/Engine/Linux/Engine/Binaries/Linux</code>. On the Linux operating system, the <code>UnrealEditor</code> application file is the main executable for the Unreal Editor. Run this executable in a terminal shell to test your build.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25738662,
            "caption": "",
            "alt_text": "Unreal Editor executable in the Linux directory",
            "image": {
              "id": 25738662,
              "file_name": "UEEditorLoc.png",
              "file_size": 262604,
              "content_type": "image/png",
              "created_at": "2025-06-16T21:22:40.460+00:00",
              "height": 553,
              "width": 890,
              "storage_key": "372ce4e8-beaf-46cb-82e3-ad33f8f2b7b2",
              "context": "documentation"
            },
            "storage_key": "372ce4e8-beaf-46cb-82e3-ad33f8f2b7b2",
            "context": "documentation",
            "width": null,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "To archive and distribute the build, place your installed build in the top directory of your source control repository alongside the FeaturePacks, Templates, and Engine directories.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "zAQ",
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
