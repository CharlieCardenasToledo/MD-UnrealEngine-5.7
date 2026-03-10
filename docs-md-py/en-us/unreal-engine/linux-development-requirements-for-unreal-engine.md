# Linux Development Requirements

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/linux-development-requirements-for-unreal-engine

> Application Version: 5.7

This page contains the software development kit (SDK) and hardware requirements needed to develop Unreal Engine (UE) projects for Linux devices.

## Recommended Hardware

```json
{
  "type": "include",
  "excerpt_id": 968,
  "excerpt_assignment_id": 2611,
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

## Recommended Software for Developing on Linux

Minimum requirements for running the engine or editor are listed below.

```json
{
  "type": "include",
  "excerpt_id": 81,
  "excerpt_assignment_id": 2612,
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

The requirements for programmers developing with the engine are listed below.

```json
{
  "type": "include",
  "excerpt_id": 83,
  "excerpt_assignment_id": 2613,
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

## Cross-Compile Toolchain

**Cross-compiling** makes it possible for game developers to target Linux from Windows. At this time, cross-compiling is only supported for Windows, and Mac users currently have to resort to [Native Compiling](https://dev.epicgames.com/documentation/en-us/unreal-engine/linux-development-requirements-for-unreal-engine#native-toolchain). Additionally, we support, test, and provide libraries and toolchains for the Linux-x86\_64 platform.

### Why Cross-Compilation

**Cross-compilation** makes it possible for game developers, working in a Windows-centric workflow, to target Linux. At this time, cross-compilation is only supported for Windows. Mac users currently have to resort to native compilation. We support, test, and provide the libraries and toolchains for the Linux-x86\_64 platform.

### Getting the Toolchain

To download the Cross-Compilation Toolchain, refer to the download links in the table in the [Version History](https://dev.epicgames.com/documentation/en-us/unreal-engine/linux-development-requirements-for-unreal-engine#version-history) section on this page.

### After Installing Cross-Compile SDK

You can verify your installation by doing `echo %LINUX_MULTIARCH_ROOT%`.

![Verify Cross-Compile SDK Installation](https://dev.epicgames.com/community/api/documentation/image/b6a528ba-9530-4d36-89fa-80d255c9c248)

## Native Toolchain

Unreal Engine's setup shell script (`Setup.sh`) automatically downloads a native toolchain, which guarantees your compiler and linker to work with our codebase. With the native toolchain, you compile against a fixed sysroot (`glibc` at the very least), so that, for example, if you compile a game on Ubuntu 22.04, you will be able to start the binary on Rocky Linux 8.

```json
{
  "type": "include",
  "excerpt_id": 85,
  "excerpt_assignment_id": 2614,
  "blocks": [
    {
      "type": "header",
      "content": "Performance Notes",
      "level": 2,
      "settings": {
        "is_hidden": false
      }
    },
    {
      "type": "paragraph",
      "content": "The spec below represents a typical system used at Epic (a Lenovo P620 Content Creation Workstation, standard version). This provides a reasonable guideline for developing games with Unreal Engine 5:",
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
            "content": "Operating System: Ubuntu 22.04",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Power Supply: 1000W power supply unit",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "RAM: 128GB DDR4-3200",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "Processor: AMD Ryzen Threadripper Pro 3975WX Processor - 128MB Cache, 3.5 GHz base / 4.2 GHz turbo, 32 Cores / 64 Threads, 280w TDP",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "OS Drive 1 TB M.2 NVMe3 x4 PCI-e SSD",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "DATA Drive 4 TB Raid Array - 2 x 2TB NVMe3 x4 PCI-e SSD in Raid 0",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "GPU: Nvidia RTX 3080 - 10GB",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "NIC 1GBPS on-board + Intel X550-T1 10G PCI-e Ethernet adapter",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        [
          {
            "type": "paragraph",
            "content": "TPM Compliant",
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
  "excerpt_hash_id": "xNO",
  "settings": {
    "is_hidden": false
  }
}
```

## Requirements for UE5 Rendering Features

```json
{
  "type": "include",
  "excerpt_id": 969,
  "excerpt_assignment_id": 2615,
  "blocks": [
    {
      "type": "enhanced_table",
      "widths": null,
      "rows": [
        [
          [
            {
              "type": "enhanced_table_header",
              "content": "UE5 Feature",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_table_header",
              "content": "System Requirements",
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
              "content": "<b>Lumen Global Illumination, Lumen Reflections, and MegaLights</b>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_list",
              "style": "unordered",
              "items": [
                [
                  {
                    "type": "paragraph",
                    "content": "<strong>SM6</strong> must be enabled in the Project Settings.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "One of the following graphics cards:",
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
                          "content": "NVIDIA RTX-2000 series or newer.",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "AMD RX-6000 series or newer.",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "Intel® Arc™ A-Series Graphics Cards or newer.",
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
                  "content": "Lumen Hardware Ray Tracing now requires SM6 to be set in Project Settings.",
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
              "content": "To learn more see, <a data-document-id=\"3224921\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-technical-details-in-unreal-engine\">Lumen Technical Details</a>.",
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
              "content": "<strong>Path Tracing</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_list",
              "style": "unordered",
              "items": [
                [
                  {
                    "type": "paragraph",
                    "content": "<strong>SM6</strong> must be enabled in the Project Settings.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "One of the following graphics cards:",
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
                          "content": "NVIDIA RTX-2000 series or newer.",
                          "settings": {
                            "is_hidden": false
                          }
                        }
                      ],
                      [
                        {
                          "type": "paragraph",
                          "content": "AMD RX-6000 series or newer.",
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
                ]
              ],
              "settings": {
                "is_hidden": false
              }
            },
            {
              "type": "paragraph",
              "content": "To learn more, see <a data-document-id=\"3225088\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine\">Path Tracer</a>.",
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
              "content": "<strong>Nanite Virtualized Geometry and Virtual Shadow Maps</strong>",
              "settings": {
                "is_hidden": false
              }
            }
          ],
          [
            {
              "type": "enhanced_list",
              "style": "unordered",
              "items": [
                [
                  {
                    "type": "paragraph",
                    "content": "GPU which supports the VK_KHR_shader_atomic_int64 Vulkan extension.",
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
                          "content": "<strong>SM6</strong> must be enabled in the Project Settings. (On by default in new projects.)",
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
                    "content": "Latest Graphics Drivers.",
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
              "content": "To learn more see, <a data-document-id=\"3225913\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.5\">Nanite Virtualized Geometry</a> and <a data-document-id=\"3225183\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-shadow-maps-in-unreal-engine?application_version=5.5\">Virtual Shadow Maps</a>.",
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
  "excerpt_hash_id": "dYe",
  "settings": {
    "is_hidden": false
  }
}
```

## Version History

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you migrate your 5.5 project to 5.6, you must update the cross-compile toolchain to v25 to avoid dependency issues. In addition, we don't recommend v24 (clang 19) for 5.6 or 5.7 due to undefined behaviors. ",
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

| UE Version | Recommended Operating System | Recommended IDE | Compiler | Cross-Compile Toolchain | Native Toolchain |
| --- | --- | --- | --- | --- | --- |
| 5.7 | Ubuntu 22.04, Rocky Linux 8 | Visual Studio Code, Rider | clang-20.1.8 | v26 [clang-20.1.8-based](https://cdn.unrealengine.com/CrossToolchain_Linux/v26_clang-20.1.8-rockylinux8.exe) | v26 [clang-20.1.8-based](https://cdn.unrealengine.com/Toolchain_Linux/native-linux-v26_clang-20.1.8-rockylinux8.tar.gz) |
| 5.6 | Ubuntu 22.04, Rocky Linux 8 | Visual Studio Code, Rider | clang 18.1.0 | v25 [clang-18.1.0-based](https://cdn.unrealengine.com/CrossToolchain_Linux/v25_clang-18.1.0-rockylinux8.exe) | v25 [clang-18.1.0-based](https://cdn.unrealengine.com/Toolchain_Linux/native-linux-v25_clang-18.1.0-rockylinux8.tar.gz) |
| 5.5 | Ubuntu 22.04, Rocky Linux 8 | Visual Studio Code, Rider | clang 18.1.0 | **v23** [clang-18.1.0-based](https://cdn.unrealengine.com/CrossToolchain_Linux/v23_clang-18.1.0-rockylinux8.exe) | **v23** [clang-18.1.0-based](https://cdn.unrealengine.com/Toolchain_Linux/native-linux-v23_clang-18.1.0-rockylinux8.tar.gz) |
| 5.3-5.4 | Ubuntu 22.04, CentOS 7 | Visual Studio Code, Rider | clang 16.0.6 | **v22** [clang-16.0.6-based](https://cdn.unrealengine.com/CrossToolchain_Linux/v22_clang-16.0.6-centos7.exe) | **v22**[clang-16.0.6-based](https://cdn.unrealengine.com/Toolchain_Linux/native-linux-v22_clang-16.0.6-centos7.tar.gz) |
| 5.2 | Ubuntu 22.04, CentOS 7 | Visual Studio Code, Rider | clang 15.0.1 | **-v21** [clang-15.0.1-based](https://cdn.unrealengine.com/CrossToolchain_Linux/v21_clang-15.0.1-centos7.exe) | **-v21** [clang-15.0.1-based](http://cdn.unrealengine.com/Toolchain_Linux/native-linux-v21_clang-15.0.1-centos7.tar.gz) |
| 5.1 | Ubuntu 22.04, CentOS 7 | Visual Studio Code, Rider | clang 13.0.1 | **-v20** [clang-13.0.1-based](https://cdn.unrealengine.com/CrossToolchain_Linux/v20_clang-13.0.1-centos7.exe) | **-v20** [clang-13.0.1-based](https://cdn.unrealengine.com/Toolchain_Linux/native-linux-v20_clang-13.0.1-centos7.tar.gz) |
| 5.0.2+ | Ubuntu 22.04, CentOS 7 | Visual Studio Code, Rider | clang 13.0.1 | **-v20** [clang-13.0.1-based](https://cdn.unrealengine.com/CrossToolchain_Linux/v20_clang-13.0.1-centos7.exe) | **-v20** [clang-13.0.1-based](https://cdn.unrealengine.com/Toolchain_Linux/native-linux-v20_clang-13.0.1-centos7.tar.gz) |
| 5.0 | Ubuntu 20.04, CentOS 7 | Visual Studio Code, Rider | clang 11.0.1 | **-v19** [clang-11.0.1-based](https://cdn.unrealengine.com/CrossToolchain_Linux/v19_clang-11.0.1-centos7.exe) | **-v19** [clang-11.0.1-based](https://cdn.unrealengine.com/Toolchain_Linux/native-linux-v19_clang-11.0.1-centos7.tar.gz) |
