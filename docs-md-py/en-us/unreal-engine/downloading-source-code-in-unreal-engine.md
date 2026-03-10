# Downloading Unreal Engine Source Code from GitHub

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine

> Application Version: 5.7

This page provides detailed instructions for subscribers to download the source code for **Unreal Engine (UE)** from the Unreal Engine GitHub repository, and to get started working with the code.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Before you can access the repository at <a href=\"https://github.com/EpicGames/UnrealEngine\">https://github.com/EpicGames/UnrealEngine</a>, you must:",
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
            "content": "have an Epic Games account,",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "have a GitHub account, and",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "have associated your GitHub account with your Epic Games account as described on the <a href=\"https://www.unrealengine.com/ue-on-github\">UE on GitHub</a> page.",
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
  "settings": {
    "is_hidden": false
  }
}
```

You are not required to download the source code to work with Unreal Engine. If you'd rather simply download and install the binary version of Unreal, read our [Installing Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine?application_version=5.5) documentation to learn how to [Get Unreal](https://www.unrealengine.com/). However, you may find that having access to the source code can be extremely valuable for you and your project. For example:

- You will get access to all the latest features and bug fixes that Epic engineers make every day, practically up to the minute.
- If you find a bug that we haven't fixed yet, but that is crucial to your project, you can unblock your project by making the fix in your own version of the source code and rebuilding your own binaries.
- You can improve the engine and help the whole Unreal community by submitting your fixes and features back to Epic.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you are an Unreal Engine licensee, you can access the source code through our Perforce server instead of the public GitHub repository.",
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
  "type": "include",
  "excerpt_id": 63,
  "excerpt_assignment_id": 2636,
  "blocks": [
    {
      "type": "header",
      "content": "Accessing Unreal Engine Source Code on GitHub",
      "level": 2,
      "settings": {
        "is_hidden": false,
        "anchor_id": 22363,
        "anchor": {
          "id": 22363,
          "name": "accessing-unreal-engine-source-code-on-git-hub"
        }
      }
    },
    {
      "type": "paragraph",
      "content": "Unreal Engine includes full access to the complete C++ source code, so you can study, customize, extend, and debug the entire Unreal Engine, and complete your project without obstruction.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Our source code repository on GitHub is continually updated as we develop features in our own mainline, so you don’t even have to wait for the next product release to get your hands on the very latest code.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "To access Unreal Engine source code, do the following:",
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
            "content": "Navigate to <a href=\"https://github.com/\">GitHub</a> and sign up for an account.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Sign in to <a href=\"https://www.unrealengine.com/\">UnrealEngine.com</a> with your verified Epic Games <a href=\"https://accounts.unrealengine.com/\">account</a>. To open your account dashboard, hover over your <strong>username</strong>, and select <strong>Personal</strong> from the drop-down menu.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "With your account dashboard open, select the <strong>Connections</strong> tab from the sidebar. Select the <strong>Accounts</strong> tab, and then select the <strong>Connect</strong> button below the GitHub icon.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "If you have not already signed the Unreal Engine End User License Agreement, you will need to read through its terms and select the check box, then select <strong>Link Account</strong>. If you are signed out of your GitHub account, you will be directed to GitHub to sign in after clicking the Link Account button.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "To complete the OAuth App Authorization process, click the <strong>Authorize EpicGames</strong> button. You can learn more about this process in <a href=\"https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps\">GitHub’s overview on Authorizing OAuth Apps</a>.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "GitHub will send an email inviting you to join the @EpicGames organization on GitHub. You must select the <strong>Join @EpicGames</strong> button in this email within seven days to complete the GitHub and Epic Games account linking process.",
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
      "content": "Upon completion, you will receive an email from Epic Games verifying that your GitHub and Epic Games accounts were successfully linked. If you don’t receive a confirmation email, or if your account is experiencing problems, get help from <a href=\"https://www.epicgames.com/site/customer-service\">Customer Service</a>. You are now ready to get started by going to our <a href=\"https://github.com/EpicGames/UnrealEngine\">GitHub page</a> (login required) to download the full source code.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Source Code Branches",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "You'll notice that we've published UE's source code in several branches.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "image",
      "image_id": 24429561,
      "caption": "",
      "alt_text": "github-branches",
      "image": {
        "id": 24429561,
        "file_name": "Branches.png",
        "file_size": 420123,
        "content_type": "image/png",
        "created_at": "2025-03-26T18:50:43.941+00:00",
        "height": 1610,
        "width": 3308,
        "storage_key": "92270d28-fa89-4314-87d5-d637534e1839",
        "context": "documentation"
      },
      "storage_key": "92270d28-fa89-4314-87d5-d637534e1839",
      "context": "documentation",
      "width": null,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Branches whose names contain dev, staging, and test are typically for internal Epic processes, and are rarely useful for end-users Other short-lived branches may appear from time to time as we stabilize new releases or hotfixes.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Release Branch",
      "level": 3,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The <strong>Release</strong> branch always reflects the current official release. These are extensively tested by our QA team, so they make a great starting point for learning Unreal Engine and for making your own projects. We work hard to make releases stable and reliable, and aim to publish a new release every few months.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Main Branch",
      "level": 3,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Most active development on UE happens in the <a href=\"https://github.com/EpicGames/UnrealEngine/tree/ue5-main\">ue5-main</a> branch. This branch reflects the latest release of the engine and may be buggy or it may not compile. We make it available for developers who are eager to test new features or work in lock-step development with us.",
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
          "content": "If you choose to work in this branch, be aware that it is likely to be ahead of the branches for the current official release and the next upcoming release. Therefore, content and code that you create to work with the ue5-main branch may not be compatible with public releases until we create a new branch directly from ue5-main for a future official release.",
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
  "excerpt_hash_id": "lY2",
  "settings": {
    "is_hidden": false
  }
}
```

## Downloading the Source Code

Please follow these instructions to download the Unreal Engine source code.

```json
{
  "type": "switch",
  "switch_type": "operating_system",
  "switchable_blocks": {
    "windows": [
      {
        "type": "include",
        "excerpt_id": 92,
        "excerpt_assignment_id": 2637,
        "blocks": [
          {
            "type": "callout",
            "callout_type": "note",
            "blocks": [
              {
                "type": "paragraph",
                "content": "Refer to our <a data-document-id=\"3228590\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.5\">Setting Up Visual Studio</a> to ensure that you have a version of Visual Studio that is compatible with your desired version of Unreal Engine.",
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
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Install <a href=\"https://windows.github.com/\">GitHub for Windows</a> then <a href=\"https://guides.github.com/activities/forking/\">fork and clone our repository</a>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "To use Git from the command line, see the <a href=\"https://help.github.com/articles/set-up-git/\">Setting up Git</a> and <a href=\"https://help.github.com/articles/fork-a-repo/\">Fork a Repo</a> articles.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "If you'd prefer not to use Git, you can get the source with the 'Download ZIP' button on the right. The built-in Windows zip utility will mark the contents of zip files downloaded from the Internet as unsafe to execute, so right-click the zip file and select 'Properties...' and 'Unblock' before decompressing it. Third-party zip utilities don't normally do this.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Install <strong>Visual Studio</strong>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "All desktop editions of Visual Studio can build UE, including Visual Studio Community, which is free for small teams and individual developers.\nRefer to the <a data-document-id=\"3228590\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.5\">Setting Up Visual Studio</a> page to ensure that you have downloaded all of the necessary VS components for working with UE.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Open your source folder in Explorer and run <code>Setup.bat</code>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "This will download binary content for the engine, as well as installing prerequisites and setting up Unreal file associations.\nOn Windows, a warning from SmartScreen may appear.  Click <strong>More info</strong>, then <strong>Run anyway</strong> to continue.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "A clean download of the engine binaries may take some time to complete.\nSubsequent checkouts only require incremental downloads and will be much quicker.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Run <code>GenerateProjectFiles.bat</code> to create project files for the engine. It should take less than a minute to complete.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Load the project into Visual Studio by double-clicking on the <code>UE5.sln</code> file. Set your solution configuration to <strong>Development Editor</strong> and your solution platform to <strong>Win64</strong>, then right click on the <strong>UE</strong> target and select <strong>Build</strong>. It may take anywhere between 10 and 40 minutes to finish compiling, depending on your system specs.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "After compiling finishes, you can load the editor from Visual Studio by setting your startup project to <strong>UE5</strong> and pressing <strong>F5</strong> to debug.",
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
        "excerpt_hash_id": "yN5",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "macos": [
      {
        "type": "include",
        "excerpt_id": 93,
        "excerpt_assignment_id": 2638,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Install a Git client like <a href=\"https://central.github.com/deployments/desktop/desktop/latest/darwin\">GitHub for Mac</a>, then <a href=\"https://guides.github.com/activities/forking/\">fork and clone our repository</a>.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "To use Git from the Terminal, see the <a href=\"https://docs.github.com/en/get-started/quickstart/set-up-git\">Setting up Git</a> and <a href=\"https://docs.github.com/en/get-started/quickstart/fork-a-repo\">Fork a Repo</a> articles.\nIf you'd rather not use Git, use the 'Download ZIP' button on the right to get the source directly.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Install the latest version of <a href=\"https://apps.apple.com/us/app/xcode/id497799835\">Xcode</a>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Open your source folder in Finder and double-click on <strong>Setup.command</strong> to download binary content for the engine. You can close the Terminal window afterwards.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "If you downloaded the source as a .zip file, you may see a warning about it being from an unidentified developer (because .zip files on GitHub aren't digitally signed).\nTo work around it, right-click on Setup.command, select <strong>Open</strong>, then click the <strong>Open</strong> button.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "In the same folder, double-click <strong>GenerateProjectFiles.command</strong>.  It should take less than a minute to complete.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Load the project into Xcode by double-clicking on the <strong>UE5.xcworkspace</strong> file. Select the <strong>ShaderCompileWorker</strong> for <strong>My Mac</strong> target in the title bar, then select the 'Product &gt; Build' menu item. When Xcode finishes building, do the same for the <strong>UE5</strong> for <strong>My Mac</strong> target. Compiling may take anywhere between 15 and 40 minutes, depending on your system specs.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "After compiling finishes, select the 'Product &gt; Run' menu item to load the editor.",
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
        "excerpt_hash_id": "qkZ",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "linux": [
      {
        "type": "include",
        "excerpt_id": 94,
        "excerpt_assignment_id": 2639,
        "blocks": [
          {
            "type": "callout",
            "callout_type": "warning",
            "blocks": [
              {
                "type": "paragraph",
                "content": "Our developers and support teams currently use the latest version of Ubuntu; as a result, we may not be able to provide support for other Linux distributions (including other versions of Ubuntu).",
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
            "type": "enhanced_list",
            "style": "ordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "Install a <a href=\"https://git-scm.com/download/gui/linux\">visual Git client</a> and <a href=\"https://docs.github.com/en/get-started/quickstart/contributing-to-projects\">fork our repository</a>.\nIf you'd prefer not to use Git, use the <strong>Download ZIP</strong> button on the right to get the source as a zip file.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Open your source folder and run <strong>Setup.sh</strong> to download binary content for the engine.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Both cross-compiling and native builds are supported.",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "<strong>Cross-compiling</strong> is handy when you are a Windows (Mac support planned too) developer who wants to package your game for Linux with minimal hassle, and it requires a <a href=\"http://cdn.unrealengine.com/qfe/v8_clang-3.9.0-centos7.zip\">cross-compiler toolchain</a> to be installed (refer to the <a href=\"sharing-and-releasing-projects/Linux/getting-started\">Linux cross-compiling page</a>).",
                  "settings": {
                    "is_hidden": false
                  }
                },
                {
                  "type": "paragraph",
                  "content": "<strong>Native compilation</strong> is discussed in <a href=\"https://github.com/EpicGames/UnrealEngine/blob/release/Engine/Build/BatchFiles/Linux/README.md\">a separate README</a>.",
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
        "excerpt_hash_id": "RaP",
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
  "excerpt_id": 91,
  "excerpt_assignment_id": 2640,
  "blocks": [
    {
      "type": "callout",
      "callout_type": "note",
      "blocks": [
        {
          "type": "paragraph",
          "content": "\nThis\n page shows Licensees how to download and build Unreal Engine from our \nsource code repository on GitHub. If you'd like to download the binary \nversion of Unreal Engine, read our <a data-document-id=\"3222143\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine?application_version=5.5\">Installing Unreal Engine</a> \ndocumentation to learn how to <a href=\"https://www.unrealengine.com/\">Get Unreal</a>.\n\n",
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
      "type": "header",
      "content": "Additional target platforms",
      "level": 2,
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
            "content": "<b>Android</b> support will be downloaded by the setup script if you have the Android NDK installed. See the <a data-document-id=\"3235454\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-unreal-engine-projects-for-android-development\">Android Quick Start</a> guide.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "<b>iOS</b> development requires a Mac. Instructions are in the <a data-document-id=\"3235313\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-an-unreal-engine-project-for-ios?application_version=5.5\">iOS Quick Start</a> guide.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Development\n for consoles and other platforms with restricted access, like Sony \nPlayStation, Microsoft Xbox, and Nintendo Switch, is only possible if \nyou have a registered developer account with those third-party vendors.",
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
      "content": "Depending\n on the platform, additional documentation or guidance may be available \nin the Epic Pro Support site, or as a downloadable archive in the \nsection of the <a href=\"https://forums.unrealengine.com/\">Unreal Engine Forums</a> that is dedicated to your platform.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "If\n you don't have access to these resources, first register a developer \naccount with the third party vendor. Then contact your Epic Games \naccount manager if you have one, or fill out and submit the <a href=\"https://epicgames.secure.force.com/Forms/FormConsoleAccessRequest?\">Console Development Request</a>\n form for Unreal Engine if you don't. Epic will contact you with a \nformal agreement to digitally sign. Once this is approved, you will \nreceive instructions on how to access source code, binaries, and \nadditional instructions for your platform.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Licensing and Contribution",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Your access to and use of Unreal Engine on GitHub is governed by the <a href=\"https://www.unrealengine.com/eula\">Unreal Engine End User License Agreement</a>. If you don't agree to those terms, as amended from time to time, you are not permitted to access or use Unreal Engine.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "We welcome any contributions to Unreal Engine development through <a href=\"https://github.com/EpicGames/UnrealEngine/pulls/\">pull requests</a> on GitHub. Most of our active development is in the <strong>master</strong>\n branch, so we prefer to take pull requests there (particularly for new \nfeatures). We try to make sure that all new code adheres to the <block-relative-link document-id=\"3227315\" application-id=\"3581142\">Epic Games\ncoding standards</block-relative-link>.  All contributions are governed by the terms of the \nEULA.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Next Steps",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Now that you've downloaded and set-up Unreal Engine, you're ready to <a data-document-id=\"3228638\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source\">build the engine from source</a>.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Footnotes",
      "level": 4,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The first time you start the editor from a fresh source build, you may experience long load times.\nThe engine is optimizing content for your platform to the <em>derived data cache</em>, and it should only happen once.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "Your private forks of the Unreal Engine code are associated with your GitHub account permissions.\nIf you unsubscribe or switch GitHub user names, you'll need to re-fork and upload your changes from a local copy.",
      "settings": {
        "is_hidden": false
      }
    }
  ],
  "excerpt_hash_id": "5Xx",
  "settings": {
    "is_hidden": false
  }
}
```
