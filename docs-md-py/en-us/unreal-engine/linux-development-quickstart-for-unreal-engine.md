# Linux Development Quickstart

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/linux-development-quickstart-for-unreal-engine

> Application Version: 5.7

Unreal Engine (UE) supports development on Linux devices using either builds created from source or pre-compiled, **installed builds**. This page provides instructions on how to set up Unreal Engine on Linux, including your development environment and build pipeline. When you finish this tutorial, you will be ready to develop applications in Unreal Engine using your Linux machine.

## 1. Recommended Software and Hardware

Unreal Engine is compatible with a variety of Linux distributions and IDEs, as long as they meet these minimum requirements:

```json
{
  "type": "include",
  "excerpt_id": 81,
  "excerpt_assignment_id": 1248,
  "blocks": [
    {
      "type": "enhanced_table",
      "widths": null,
      "rows": [
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Running the Engine",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": " ",
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
              "content": "<strong>Operating System</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Rocky Linux 8 / Redhat Linux 8 or newer",
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
              "content": "<strong>Linux Kernel Version</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "kernel 4.18 or newer",
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
              "content": "<strong>Additional Dependencies</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "glibc 2.28 or newer",
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
          "content": "If either Unreal Editor or installations of UE games take a very long time on startup, check that your <code>glibc</code> is version 2.35 or newer, as earlier versions have a slow implementation of <code>dlopen</code>.",
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
  "excerpt_hash_id": "JgB",
  "settings": {
    "is_hidden": false
  }
}
```

We recommend your system meet the following standard so that **Unreal Editor** performs smoothly:

```json
{
  "type": "include",
  "excerpt_id": 968,
  "excerpt_assignment_id": 1253,
  "blocks": [
    {
      "type": "enhanced_table",
      "widths": null,
      "rows": [
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>Recommended Operating System</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Ubuntu 22.04",
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
              "content": "<strong>Processor</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Quad-core Intel or AMD, 2.5 GHz or faster",
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
              "content": "<strong>Memory</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "32 GB RAM",
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
              "content": "<strong>Graphics Card</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "GeForce 2080",
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
              "content": "<strong>Graphics RAM</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "8 GB or more",
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
              "content": "<strong>RHI Version</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Vulkan: AMD (RADV minimum 24.2.8+, recommended 25.0.0+) and NVIDIA (570+)",
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
  "excerpt_hash_id": "rL1",
  "settings": {
    "is_hidden": false
  }
}
```

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "The Vulkan rendering hardware interface (RHI) used on Linux is not friendly to low amounts of VRAM compared with other backends. We strongly recommend using a dedicated GPU with a high amount of VRAM.",
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

To set up your development environment, we recommend the following software, which we test with most frequently:

```json
{
  "type": "include",
  "excerpt_id": 83,
  "excerpt_assignment_id": 1250,
  "blocks": [
    {
      "type": "enhanced_table",
      "widths": null,
      "rows": [
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "Developing with the Engine",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": " ",
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
              "content": "<strong>Operating System</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Ubuntu 22.04, Rocky Linux 8",
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
              "content": "<strong>Compiler</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "clang 18.1.0",
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
              "content": "Optional",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          []
        ],
        [
          [
            {
              "type": "paragraph",
              "content": "<strong>IDE</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "paragraph",
              "content": "Visual Studio Code, Rider",
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
  "excerpt_hash_id": "mR4",
  "settings": {
    "is_hidden": false
  }
}
```

Refer to the documentation for your Linux distribution or IDE for further information on how to set them up. While setting up your OS and hardware is outside the scope of this documentation, setting up your IDE to work with Unreal Engine is covered below.

## 2. Install Unreal Engine

You can set up Unreal Engine on Linux either by installing a pre-compiled build, or by building the engine from source.

### 2a. Download an Installed Build

The simplest option for running Unreal Engine is to use an Installed Build. To download and install one, follow these steps:

```json
{
  "type": "include",
  "excerpt_id": 84,
  "excerpt_assignment_id": 1251,
  "blocks": [
    {
      "type": "paragraph",
      "content": "Unreal Engine on Linux supports precompiled installed builds as well as source code builds. For information about using source builds, refer to <a data-document-id=\"3228589\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine\">Building Unreal Engine from Source</a>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "To use a precompiled build, follow these steps:",
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
            "content": "Open the <a href=\"https://www.unrealengine.com/en-US/linux\">Unreal Engine for Linux</a> page. It will prompt you to to create or sign into an Epic Games account. If you already have one, sign in to access the page. If you don't have an account, click <strong>Sign Up</strong> to create one.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24430236,
            "caption": "",
            "alt_text": "Log in or sign up",
            "image": {
              "id": 24430236,
              "file_name": "linux-authentication.png",
              "file_size": 20747,
              "content_type": "image/png",
              "created_at": "2025-03-27T15:21:36.158+00:00",
              "height": 566,
              "width": 646,
              "storage_key": "3f3e7322-a09d-4bd6-a1bb-8b793e24b69d",
              "context": "documentation"
            },
            "storage_key": "3f3e7322-a09d-4bd6-a1bb-8b793e24b69d",
            "context": "documentation",
            "width": 350,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You can sign up for an Epic Games account with your email, or with a supported social media or gaming platform account.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24430237,
            "caption": "",
            "alt_text": "Choose how to sign in",
            "image": {
              "id": 24430237,
              "file_name": "linux-epic-account.png",
              "file_size": 40632,
              "content_type": "image/png",
              "created_at": "2025-03-27T15:21:36.370+00:00",
              "height": 833,
              "width": 502,
              "storage_key": "324b1ab1-4101-43b9-8a3a-94bfef7e1cee",
              "context": "documentation"
            },
            "storage_key": "324b1ab1-4101-43b9-8a3a-94bfef7e1cee",
            "context": "documentation",
            "width": 0,
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Download the <code>.zip</code> file containing the version of Unreal Engine that you need.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24430238,
            "caption": "",
            "alt_text": "Download UE",
            "image": {
              "id": 24430238,
              "file_name": "linux-download.png",
              "file_size": 88020,
              "content_type": "image/png",
              "created_at": "2025-03-27T15:21:36.445+00:00",
              "height": 622,
              "width": 1495,
              "storage_key": "eec9eed6-0919-42d2-bf35-872021e9fd5e",
              "context": "documentation"
            },
            "storage_key": "eec9eed6-0919-42d2-bf35-872021e9fd5e",
            "context": "documentation",
            "width": 700,
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Unzip the contents of the <code>.zip</code> file to your desired installation directory.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Run <code>Engine/Binaries/Linux/UnrealEditor</code> from the Terminal to launch Unreal Engine.",
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
  "excerpt_hash_id": "44g",
  "settings": {
    "is_hidden": false
  }
}
```

### 2b. Build Unreal Engine from Source

To install Unreal Engine from source, refer to [Downloading Unreal Engine Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine). Once you have compiled the engine, run `Engine/Binaries/Linux/UnrealEditor` from the Terminal to launch Unreal Editor.

## 3. Setting Up a New Project

Refer to the instructions in [Creating a New Project in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-a-new-project-in-unreal-engine) for information on how to set up a new project. You don't need a specific template or project type for the purposes of this tutorial, but you should make sure it has **C++** enabled if you are setting up your environment for C++.

## 4. Set Up Your Development Environment (C++)

If you are planning to develop C++ projects, you need to set up the clang toolchain and an IDE to work with Unreal Engine. While we don't require a specific IDE, we recommend using Visual Studio Code or Rider. This section provides instructions that are specific to Visual Studio Code, as it provides a common development environment for other operating systems as well.

1. Install the custom clang toolchain for your setup. See [Linux Development Requirements](https://dev.epicgames.com/documentation/en-us/unreal-engine/linux-development-requirements-for-unreal-engine?application_version=5.5) for more information.
2. Locate your Unreal Engine install directory and open `Build/BatchFiles/Linux`, then run `SetupToolchain.sh`.
3. Download and install VS Code as well as the official C / C++ extension pack and C# extension. These are required for reading the source code for both Unreal Engine and its Build Tools.
4. Either open Unreal Editor, open your **Editor Preferences**, and set your Source Code editor to Visual Studio Code, or modify `BaseEngine.ini` to include the following:
5. Run `GenerateProjectFiles.sh -vscode` to generate the VS Code workspace for either your engine distribution (in the case of a source code build) or your project. Add `-project=(path to your project)` to choose a specific project.

For information about configuring VS Code with IntelliSense and other helpful utilities, see [Setting Up VS Code for Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-visual-studio-code-for-unreal-engine).

## 5. Build a Project

Now that your environment is fully set up, you should run a test build of your project to ensure your workflow is fully functioning.

### 5a. Build a Project In Unreal Editor

Open your project in Unreal Editor, then click the **Platforms** dropdown and click **Linux** > **Package Project**. If your system is configured correctly, Unreal Engine will build, cook, and package your project.

### 5b. Build a Project Through the Command Line

To build a project through the Command Line, use the RunUAT script's **BuildCookRun** command detailed in the [Build Operations](https://dev.epicgames.com/documentation/en-us/unreal-engine/build-operations-cooking-packaging-deploying-and-running-projects-in-unreal-engine) guide. The following is an example of a working BuildCookRun command:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "[UE Root Directory]/RunUAT BuildCookRun -Build -Cook -Stage -Package -Run -Project=[ProjectName]",
  "lines_of_code": 1,
  "id": 46503,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NjUwMywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjQ3OjQ1KzAwOjAwIn0=--d80e06a172983e2be0c19e986088d0ad7ced5181f64d2fb6b139a4d75db01b44",
  "settings": {
    "is_hidden": false
  }
}
```

Alternatively, you can use the Turnkey command line to start the same process.

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "[UE Root Directory]/RunUAT Turnkey -command=ExecuteBuild -platform=Linux -Project=[ProjectName]",
  "lines_of_code": 1,
  "id": 46504,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0NjUwNCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE3OjQ3OjQ1KzAwOjAwIn0=--76c7d9ee519b36ab3a33a29831a6998c974ae50354127f965bfdfaec203b4a27",
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
      "content": "Normally, you need to use RunUAT from your Unreal Engine source directory. To make this command simpler to run, define a <code>$UE_ROOT</code> environment variable. This makes it possible to use RunUAT with a command such as <code>$UE_ROOT/RunUAT BuildCookRun</code> instead of providing the entire path to the RunUAT script.",
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
