# Downloading Unreal Engine with Perforce

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-unreal-engine-with-perforce

> Application Version: 5.7

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Using the content of this page requires a custom license support agreement with Epic Games that includes access to the Unreal Engine P4 Perforce depot.",
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

## Connecting to the Epic Games P4 Perforce Server

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "This section is intended for technical administrators connecting directly to the Epic Games P4 Perforce depot, to download the source code into a local depot. It should not be used by developers who need to set up a local build of Unreal Engine. Instead, developers should contact their technical administrator to get access to a local depot holding the Unreal Engine source code.",
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
  "excerpt_id": 65,
  "excerpt_assignment_id": 1355,
  "blocks": [
    {
      "type": "paragraph",
      "content": "Connecting to the Epic Games Perforce P4 server requires using the SSL feature, and you must be running a 2017.2 or later version of a Perforce client (P4V, p4, or API). You can take advantage of latency based routing to automatically connect to the closest Perforce regional proxy by using the global DNS name. Alternatively, you can connect directly to a regional proxy to ensure you always connect to the closest one.",
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
          "content": "If you are running a local proxy, you  must connect through a broker instead of using the region proxy servers. You can connect to the global broker using the address below:",
          "settings": {
            "is_hidden": false
          }
        },
        {
          "type": "paragraph",
          "content": "<code>ssl:p4-licensee.epicgames.com:1666</code>",
          "settings": {
            "is_hidden": false
          }
        },
        {
          "type": "paragraph",
          "content": "Port <code class=\"inline-code\">1667</code> is also valid, and you can use it for troubleshooting login issues.",
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
            "content": "Install the <strong>P4V Perforce client for Windows</strong>. The client can be downloaded from the <a href=\"https://www.perforce.com/downloads/helix-visual-client-p4v\">Perforce Downloads</a> page.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "In the <strong>Open Connection</strong> dialog, enter the following connection info:",
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
                  "content": "<strong>Server</strong>: ssl:p4-licensee.epicgames.com:1666",
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
                      "content": "The address above should automatically direct you to a regional proxy with the best latency based on your geographic location. If, for some reason, you need to connect to a specific regional proxy, you can connect to them using the addresses below:",
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
                            "content": "<strong>United States East (Virginia)</strong>: ssl:p4-licensee-east.us.epicgames.com:1666",
                            "settings": {
                              "is_hidden": false
                            }
                          }
                        ],
                        [
                          {
                            "type": "paragraph",
                            "content": "<strong>United States West (Oregon)</strong>: ssl:p4-licensee-west.us.epicgames.com:1666",
                            "settings": {
                              "is_hidden": false
                            }
                          }
                        ],
                        [
                          {
                            "type": "paragraph",
                            "content": "<strong>Asia Pacific Northeast (Tokyo)</strong>: ssl:p4-licensee-northeast.ap.epicgames.com:1666",
                            "settings": {
                              "is_hidden": false
                            }
                          }
                        ],
                        [
                          {
                            "type": "paragraph",
                            "content": "<strong>Europe Central (Frankfurt)</strong>: ssl:p4-licensee-central.eu.epicgames.com:1666",
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
              ],
              [
                {
                  "type": "paragraph",
                  "content": "<strong>User</strong>: Perforce username provided by Epic Games.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "<strong>Password</strong>: Set by your technical license administrator in Epic Games’ Okta.",
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
            "content": "Click <strong>OK</strong> to connect to the Perforce P4 Server.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 25733548,
            "caption": "Click the image for full size.",
            "alt_text": "",
            "image": {
              "id": 25733548,
              "file_name": "connect-to-perforce-server.png",
              "file_size": 164686,
              "content_type": "image/png",
              "created_at": "2025-06-13T18:28:27.204+00:00",
              "height": 842,
              "width": 1400,
              "storage_key": "bee56b72-197f-413f-a41d-2a3b991daab4",
              "context": "documentation"
            },
            "storage_key": "bee56b72-197f-413f-a41d-2a3b991daab4",
            "context": "documentation",
            "width": 800,
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "When connecting to an endpoint for the first time, you must explicitly trust that endpoint.",
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
                  "content": "The Epic Games SSL fingerprint is <code class=\"inline-code\">B7:8D:23:34:71:4C:04:80:FD:D2:C0:A4:F5:7F:44:5E:D0:1C:D2:86</code>.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "P4V will prompt you to trust the new endpoint.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Command line p4 uses the p4 trust command: <code>$ p4 trust -y</code>.",
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
            "content": "In P4V, choose <strong>Connection &gt; New Workspace</strong> to create a new workspace for the engine. Enter the information below and click <strong>OK</strong> to create the workspace:",
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
                  "content": "<strong>Workspace name</strong>: Give your new workspace a name.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "<strong>Stream</strong>: Click <strong>Browse</strong> and select <code>//UE5/Release-Latest</code> from the list of available streams.",
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
            "image_id": 24429579,
            "caption": "",
            "alt_text": "Create a new workspace",
            "image": {
              "id": 24429579,
              "file_name": "ue5_1-new-workspace.png",
              "file_size": 28688,
              "content_type": "image/png",
              "created_at": "2025-03-26T18:50:46.301+00:00",
              "height": 675,
              "width": 684,
              "storage_key": "765ded13-54ae-4692-a229-20c25c0c5e12",
              "context": "documentation"
            },
            "storage_key": "765ded13-54ae-4692-a229-20c25c0c5e12",
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
            "content": "In the <strong>Depot</strong> pane, expand the <strong>Filter Depot</strong> menu and select <strong>Tree Restricted to Workspace View</strong>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24429580,
            "caption": "",
            "alt_text": "The Filter Depot menu",
            "image": {
              "id": 24429580,
              "file_name": "ue5_1-restrict-tree-view.png",
              "file_size": 23214,
              "content_type": "image/png",
              "created_at": "2025-03-26T18:50:46.368+00:00",
              "height": 182,
              "width": 832,
              "storage_key": "1fdf8fdf-6c8f-4679-bae9-26a8029ebf44",
              "context": "documentation"
            },
            "storage_key": "1fdf8fdf-6c8f-4679-bae9-26a8029ebf44",
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
      "content": "Connecting to your Local Perforce Depot",
      "level": 3,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "After your technical administrator has downloaded the Unreal Engine source code to a local P4 Perforce depot, the process for developers connecting to the local depot should be mostly the same as described above, except replace steps 2-4 with your local P4 Perforce depot connection and authentication information. Your technical administrator will have the required information for you to access your local depot.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "header",
      "content": "Download Unreal Engine",
      "level": 3,
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
          "content": "Epic Games uses stream names by convention. If you rename the streams for local use, please adjust the instructions below for your local users accordingly.",
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
      "content": "Epic Games distributes Unreal Engine to licensees using the <code>//UE5/Release-Latest</code> stream in the Perforce depot. This contains the entire engine along with several additional projects in the form of example games, samples, and demos. When setting up your local build, you have the option of downloading everything or picking and choosing only the parts you want or need.",
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "To get set up as quickly as possible, we recommend you only download the bare minimum to start with and then download other parts on an as-needed basis. This can dramatically reduce idle time spent waiting for the download to finish. We also provide a <code>//UE5/Release-Latest-Minimal</code> stream to help with this.",
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
          "content": "Because there are a large number of files in the <code>//UE5/Release-Latest</code> stream and the total download size is many gigabytes, the download can take a long time when syncing the entire branch.",
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
            "content": "Right-click on the stream you want to download and choose <strong>Get Latest Revision</strong>.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "image",
            "image_id": 24429581,
            "caption": "",
            "alt_text": "Perforce - Get Latest Revision",
            "image": {
              "id": 24429581,
              "file_name": "get-latest-revision.png",
              "file_size": 14383,
              "content_type": "image/png",
              "created_at": "2025-03-26T18:50:46.448+00:00",
              "height": 204,
              "width": 481,
              "storage_key": "174a489e-104c-443e-b50e-7538c9c49582",
              "context": "documentation"
            },
            "storage_key": "174a489e-104c-443e-b50e-7538c9c49582",
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
            "content": "The latest version of all files will be downloaded.",
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
  "excerpt_hash_id": "8Wy",
  "settings": {
    "is_hidden": false
  }
}
```

### Migrating an Existing Workspace

To avoid having to force sync your entire workspace when creating a new one on the global replica, users can use `p4 flush` to populate the information based on the files in a local workspace. This procedure will be much faster than a force sync, and allow users to essentially pick up where they left off.

1. Create a new workspace on the global replica, copying the view and root settings from the original workspace.
2. Switch to the new workspace.
3. Issue `p4 flush` command or `p4 sync -k` to populate information on the server.
4. Epic Games ages out old workspaces automatically if they are unused for six months.
