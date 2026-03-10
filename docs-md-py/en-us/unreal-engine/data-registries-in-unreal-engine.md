# Data Registries

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/data-registries-in-unreal-engine

> Application Version: 5.7

A **Data Registry** is an efficient global storage space for `USTRUCT`-tagged data structures. Data Registries support synchronous and asynchronous data access, and user-defined caching behaviors. They are intended to work with general read-only data.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Data Registries are part of a plugin. The <a data-document-id=\"3229105\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/quick-start-guide-for-unreal-engine-data-registries\">Data Registries Quickstart</a> can guide you through the process and familiarize you with some of the basic concepts.For specific session-based data such as progress in a story, or a character's current state, use the engine's Save Game system.",
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

You can configure your Data Registry to load or generate data from a variety of different sources, and can populate it with Asset scanning and manual registration. Data Registries are similar to **Composite Data Tables**, but can store curve data in addition to standard table rows, and use an indirection layer rather than manually compositing multiple tables together.

## Data Sources

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1695,
        "excerpt_assignment_id": 1405,
        "blocks": [
          {
            "type": "paragraph",
            "content": "Data Registries gather data items from two types of sources, <strong>Data Registry Sources</strong> and <strong>Meta Data Registry Sources</strong>. These sources are not the actual data items, instead the Data Registry uses them to find or generate data items.\nThe order in which data sources appear within a Data Registry matters, if a specific data item is not found in one source, then the Data Registry will look in the sources that appear after it in the list.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "This creates the potential for override and fallback behavior, and enables context-specific sources to override generic ones.\nThe Data Registry plugin includes built-in Data Registry Sources and Meta Data Registry Sources that wrap <strong>Data Tables</strong> and <strong>Curve Tables</strong>.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "POM",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1696,
        "excerpt_assignment_id": 1406,
        "blocks": [
          {
            "type": "paragraph",
            "content": "Data Registries gather data items from two types of sources, <strong>Data Registry Sources</strong> and <strong>Meta Data Registry Sources</strong>. These sources are not the actual data items, instead the Data Registry uses them to find or generate data items.\nThe order in which data sources appear within a Data Registry matters, if a specific data item is not found in one source, then the Data Registry will look in the sources that appear after it in the list.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "This creates the potential for override and fallback behavior, and enables context-specific sources to override generic ones.\nThe Data Registry plugin includes built-in Data Registry Sources and Meta Data Registry Sources that wrap <strong>Data Tables</strong> (<code>UDataTable</code>) and <strong>Curve Tables</strong> (<code>UCurveTable</code>).",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "QYj",
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

### Data Registry Sources

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1697,
        "excerpt_assignment_id": 1407,
        "blocks": [
          {
            "type": "paragraph",
            "content": "The Data Registry directly owns a set of Data Registry Source objects that you create and configure in an array within the Data Registry Asset. These objects represent interfaces to specific data sources where the Data Registry can find information, such as an individual data table or a web database.\nC++ developers can create Data Registry Source child classes to handle other types of data or implement different indirection rules to map identifiers to data items.\nIf your project has one or more Data Registry Source child classes, they will appear in the list when adding new data sources to a Data Registry Asset.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "G5Z",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1698,
        "excerpt_assignment_id": 1408,
        "blocks": [
          {
            "type": "paragraph",
            "content": "The Data Registry directly owns a set of Data Registry Source objects that you can create and configure in an array within the Data Registry Asset.\nThese objects represent interfaces to specific data sources where the Data Registry can find information, such as an individual data table or a web database.\nYou can create child classes of <code>UDataRegistrySource</code> if you want to handle other types of data, or implement different indirection rules to map identifiers to data items.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Any child class you create will appear in the dropdown list when you add new data sources to a Data Registry Asset.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "Z7E",
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

### Meta Data Registry Sources

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1699,
        "excerpt_assignment_id": 1409,
        "blocks": [
          {
            "type": "paragraph",
            "content": "Meta Data Registry Sources create and own other data sources at runtime. Instead of explicitly list all data sources, Meta Data Registry Sources use generic rules, such as scanning a set of user-named paths, to locate Assets that contain data items.\nThey can listen for manual registration of specific Assets. Meta Data Registry Sources are dynamically generated data sources (including the data items within those sources), because of this they discover load into the Data Registry at runtime.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Similar to Data Registry Sources, C++ developers can create Meta Data Registry child classes to handle other data types, create different scanning rules.\nIf your project contains one or more Meta Data Registry Source child classes, they will appear in the dropdown list when you add new data sources to a Data Registry Asset.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "ny2",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1700,
        "excerpt_assignment_id": 1410,
        "blocks": [
          {
            "type": "paragraph",
            "content": "Meta Data Registry Sources create and own other data sources at runtime. Rather than explicitly list all data sources, Meta Data Registry Sources use generic rules, such as scanning a set of user-named paths, to locate Assets that contain data items. They can also listen for manual registration of specific Assets.\nBecause Meta Data Registry Sources are dynamically generated, data sources (and the data items within those sources) that they discover load into the Data Registry at runtime.\nSimilar to Data Registry Sources, you can create your own child classes to handle other data types, create different scanning rules, and so on. To do this, override the <code>UMetaDataRegistrySource</code> class.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Any child classes you create will appear in the dropdown list as options when you add new Data Sources to a Data Registry Asset.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "e1z",
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

## Identifiers

The Data Registry plugin uses its own identifier types to identify or look up Data Registries and the individual data items they contain. While these identifiers are [string-based names](https://dev.epicgames.com/documentation/en-us/unreal-engine/string-handling-in-unreal-engine), the `FDataRegistryType` (for Data Registry Assets) and `FDataRegistryId` (for individual items within a Data Registry) structures act as wrappers and provide useful in-editor functionality.
`FDataRegistryType` identifies a Data Registry Asset, while `FDataRegistryId` identifies a Data Registry and a specific data item within it. You can use these identifier types when you need to find Data Registry Assets or retrieve individual data items from them.

Each Data Registry Asset must have a unique name in the **Registry Type** field.
If two Data Registry Assets have the same name in this field, the system will only recognize and populate one of them. Similarly, if multiple data items share the same identifying value (name or Gameplay Tag), the registry will read all items, but retrieval operations will only access the first one that the Data Registry Asset loaded; see the section on [data sources](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-registries-in-unreal-engine#data-sources) for information about the order in which data items load.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Developers using C++ can change this behavior by creating a child Data Registry class and overriding the <code>ResolveDataRegistryId</code> function.",
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

### Data Registry Asset Identifiers

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1701,
        "excerpt_assignment_id": 1411,
        "blocks": [
          {
            "type": "paragraph",
            "content": "While setting up a Data Registry Asset, developers must set the <strong>Registry Type</strong> field to a unique name value. This is the identifier for the Data Registry. After setting this value, all Registry Type fields across the editor will immediately add the new Data Registry name to their dropdown list.<br>\nThis prevents user error resulting from spelling mistakes when referencing the Data Registry in other Assets, and makes the selection process quicker and easier.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "bom",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1702,
        "excerpt_assignment_id": 1412,
        "blocks": [
          {
            "type": "paragraph",
            "content": "While setting up a Data Registry Asset, developers must set the <strong>Registry Type</strong> field to a unique name value. This is the identifier for the Data Registry.\nAfter setting this value, <code>FDataRegistryType</code> fields across the editor will immediately add the new Data Registry name to their dropdown list.\nThis prevents user error resulting from spelling mistakes when referencing the Data Registry in other Assets, and makes the selection process quicker and easier.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "zAG",
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

![Image](https://dev.epicgames.com/community/api/documentation/image/72d1826b-c9ff-415b-a600-be26ec37e6eb)

_Above, setting the Data Registry Asset's identifier._

![Image](https://dev.epicgames.com/community/api/documentation/image/dbe6eff2-ab03-468a-9f8a-8d0a8560949a)

### Data Item Identifiers

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1703,
        "excerpt_assignment_id": 1413,
        "blocks": [
          {
            "type": "paragraph",
            "content": "Identifying an individual data item, such as a row within a Data Table, requires specifying the Data Registry Asset and the data item itself. The Data Registry ID contains both identifiers. Its <strong>Data Registry Type</strong> field will appear as a dropdown list, from which you can select any known Data Registry by its identifying name. After selecting a Data Registry's name from that dropdown list, the <strong>Data Registry ID</strong> field will change to accommodate the Data Registry.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "If the Data Registry's ID Format uses a Gameplay Tag, the user interface will display a filtered list containing that Gameplay Tag and all of its children. If the Data Registry's ID Format did not use a Gameplay Tag, the user interface will display a dropdown list of all known rows that the Data Registry Asset contains.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "5kR",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1704,
        "excerpt_assignment_id": 1414,
        "blocks": [
          {
            "type": "paragraph",
            "content": "Identifying an individual data item, such as a row within a data table, requires specifying the Data Registry Asset and the data item itself. The <code>FDataRegistryId</code> type contains both identifiers. Its <strong>Data Registry Type</strong> field will appear as a dropdown list, from which you can select any known Data Registry by its identifying name.\nAfter selecting a Data Registry's name from that dropdown list, the <strong>Data Registry ID</strong> field will change to accommodate the Data Registry.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "If the Data Registry's ID Format uses a Gameplay Tag, the user interface will display a filtered list containing that Gameplay Tag and all of its children.\nIf the Data Registry's ID Format did not use a Gameplay Tag, the user interface will display a dropdown list of all known rows that the Data Registry Asset contains.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "y3x",
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
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "If you edit a Data Registry Asset, your changes may not take effect immediately in other Assets that reference it using data item identifiers.\nIf this happens, the data item identifiers could contain obsolete rows in its dropdown lists.\nClick the <strong>Compile</strong> button in the Asset that references the Data Registry (not the Data Registry Asset itself) to update the interface with current data item information.",
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

![Image](https://dev.epicgames.com/community/api/documentation/image/43b42174-04a4-4f77-b1eb-ba7a1be2ee50)

_On the left, item selection for a Data Registry Asset with an ID Format that uses a Gameplay Tag._

```json
{
  "type": "callout",
  "callout_type": "tip",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Because <code>FDataRegistryId</code> has an <code>FDataRegistryType</code> member (called <code>RegistryType</code>), you can find the Data Registry Asset that contains the row without needing a separate <code>FDataRegistryType</code> identifier.",
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
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1705,
        "excerpt_assignment_id": 1415,
        "blocks": [
          {
            "type": "header",
            "content": "Identifier Resolution",
            "level": 4,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "The system looks up data items by searching for the <strong>Item Name</strong> of the Data Registry ID you supply. You can alter this behavior by creating a child Data Registry class in C++. Toggle to the C++ version of this page for more details.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "qPv",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1706,
        "excerpt_assignment_id": 1416,
        "blocks": [
          {
            "type": "header",
            "content": "Dynamic Identifier Resolution",
            "level": 4,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "By default, the system looks up data items by searching for the value of the <code>ItemName</code> field of the <code>FDataRegistryId</code> you supply. If this is not the ideal behavior for your project, you can create your own <code>UDataRegistry</code> subclass and override the <code>MapIdToResolvedName</code> function to include additional <code>FDataRegistryResolverScope</code> structs in the local scope. By overriding the <code>ResolveIdToName</code> function within your <code>FDataRegistryResolverScope</code> subclasses, you can remap the incoming row names, even using dynamic or player-specific information. After resolving an ID, the system produces an <code>FDataRegistryLookup</code> which is guaranteed to be unique (within the system) and is used as the caching unique ID.",
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "RVx",
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

## Quick Function Reference

The following functions are helpful for getting started with Data Registries. This is not a complete reference, but these functions are the basics you will need to access your data after having set up Data Registries in your project.

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1707,
        "excerpt_assignment_id": 1417,
        "blocks": [
          {
            "type": "enhanced_list",
            "style": "unordered",
            "items": [
              [
                {
                  "type": "paragraph",
                  "content": "<strong>Acquire Data Registry Item</strong> searches for a given item and loads it into the cache on success. This function is very important for data items coming from MetaDataRegistrySources, as the other Data Registry functions can only access cached data items. Call this function if you want to access a data item that you believe exists (or might exist) but is not currently in the cache.",
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
            "content": "When you call this function, it will resume execution immediately through the pin on the right side. The return value indicates whether or not the loading operation has started, not the result of that operation; failure means that the operation could not begin, and the callback function you have connected will not be called. Once the callback function runs, the search and load operations have finished, and you can use the other functions described in this section to attempt to retrieve your data from the cache, presuming it loaded successfully. If your data is not in the cache immediately at that point, it was not found.",
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
                "content": "If you successfully retrieve a data item once, but fail to retrieve it later on, it may have been removed from the cache. Call <strong>Acquire Data Registry Item</strong> again and retrieve it immediately upon entering the callback function.  You may also consider making your own copy of the data, or adjusting the data item's cache behavior, based on the specific needs of your project.",
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
            "image_id": 25740072,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25740072,
              "file_name": "AcquireDRItem.png",
              "file_size": 346526,
              "content_type": "image/png",
              "created_at": "2025-06-17T15:21:54.373+00:00",
              "height": 1571,
              "width": 3313,
              "storage_key": "299dcc55-c1d6-4210-bb7f-3ad1f2ee826d",
              "context": "documentation"
            },
            "storage_key": "299dcc55-c1d6-4210-bb7f-3ad1f2ee826d",
            "context": "documentation",
            "width": 600,
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
                  "content": "<strong>Find Data Registry Item</strong> checks for an item in the Data Registry's cache, and branches based on whether or not the item was found. If it was found, you can access it through the right-side <strong>Out Item</strong> pin. This function returns immediately, so data items that exist but are not in the cache will not be found.",
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
            "image_id": 25740073,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25740073,
              "file_name": "FindDRItem.png",
              "file_size": 343353,
              "content_type": "image/png",
              "created_at": "2025-06-17T15:21:54.734+00:00",
              "height": 1547,
              "width": 3316,
              "storage_key": "14c086b6-4efb-4463-acbc-220b4f47529e",
              "context": "documentation"
            },
            "storage_key": "14c086b6-4efb-4463-acbc-220b4f47529e",
            "context": "documentation",
            "width": 600,
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
                  "content": "<strong>Get Data Registry Item</strong> is similar to <strong>Find Data Registry Item</strong>, but returns a success/failure value instead of branching, and automatically populates the variable connected to the left-side <strong>Out Item</strong> pin on success. This function returns immediately, so data items that exist but are not in the cache will not be found.",
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
            "image_id": 25740074,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25740074,
              "file_name": "GetDRItem.png",
              "file_size": 311208,
              "content_type": "image/png",
              "created_at": "2025-06-17T15:21:54.966+00:00",
              "height": 1513,
              "width": 3287,
              "storage_key": "fc7275fb-0db3-4ccf-b329-5f31a9886216",
              "context": "documentation"
            },
            "storage_key": "fc7275fb-0db3-4ccf-b329-5f31a9886216",
            "context": "documentation",
            "width": 600,
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
                  "content": "<strong>Evaluate Data Registry Curve</strong> looks for a cached curve. Like <strong>Find Data Registry Item</strong>, it is synchronous, so it will return immediately, but will fail to find a curve if that curve is not in the cache at the time of the function call. This function branches execution based on whether it succeeds or fails, and returns the default value that you provide on failure. You can use this feature in cases where you need an output value regardless of whether or not the curve data is available.",
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
            "image_id": 25740075,
            "caption": "",
            "alt_text": "",
            "image": {
              "id": 25740075,
              "file_name": "EvaluateDRCurve.png",
              "file_size": 179780,
              "content_type": "image/png",
              "created_at": "2025-06-17T15:21:55.208+00:00",
              "height": 1555,
              "width": 2915,
              "storage_key": "66555385-1989-4db9-b4ab-26fdb1014f0c",
              "context": "documentation"
            },
            "storage_key": "66555385-1989-4db9-b4ab-26fdb1014f0c",
            "context": "documentation",
            "width": 600,
            "settings": {
              "is_hidden": false
            }
          }
        ],
        "excerpt_hash_id": "POJ",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1708,
        "excerpt_assignment_id": 1418,
        "blocks": [
          {
            "type": "enhanced_table",
            "widths": null,
            "rows": [
              [
                [
                  {
                    "type": "enhanced_table_header",
                    "content": "Function",
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
                    "content": "<code>UDataRegistrySubsystem::Get</code>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Returns a pointer to the <code>UDataRegistrySubsystem</code> instance. The only static function in the list, this function acts as the entry point to the subsystem.",
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
                    "content": "<code>UDataRegistrySubsystem::GetRegistryForType</code>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Takes a name or <code>FDataRegistryType</code> (either standalone or from <code>FDataRegistryId::RegistryType</code>) and returns a <code>UDataRegistry</code> pointer to the matching Data Registry, if it exists.",
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
                    "content": "<code>UDataRegistrySubsystem::RegisterSpecificAsset</code>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Searches for a Data Registry by <code>FDataRegistryType</code>, and adds a specific Asset to it. If you do not provide a valid <code>FDataRegistryType</code>, the subsystem will attempt to add the Asset to all Data Registries in the subsystem. Returns <code>true</code> if at least one Data Registry accepted the Asset.",
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
                    "content": "<code>UDataRegistry::GetCachedItem</code>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Searches the Data Registry for the data item that corresponds to the <code>FDataRegistryId</code> you provide. If the item is not in the cache at the time of the function call, the function will return null. Otherwise, the function returns a const pointer to whichever struct type the Data Registry stores.",
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
                    "content": "<code>UDataRegistry::GetAllCachedItems</code>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Populates a map with a pointer to the engine's <code>UScriptStruct</code> data (as a <code>const uint8*</code>) for each cached item in the Data Registry, using the item's <code>FDataRegistryId</code> as the key. Also provides the <code>UScriptStruct</code> itself through a separate output parameter. This is often useful for iterating over the cache as a debugging tool, such as using the <code>UScriptStruct::ExportText</code> function to log the contents of each cached item.",
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
                    "content": "<code>UDataRegistry::EvaluateCachedCurve</code>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Finds the curve that corresponds to the <code>FDataRegistryId</code> you provide, and evaluates it for a given input value. This function will fail if the requested curve is not in the cache at the time of the call. The function's return value is of type <code>FDataRegistryCacheGetResult</code>, which provides information about the cached status of the curve you requested, and most importantly whether or not the curve was found. The curve's output value, of type <code>float</code>, comes through an output parameter.",
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
                    "content": "<code>UDataRegistry::AcquireItem</code>",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Similar to <code>GetCachedItem</code>, but finds the data item even if it is not cached at the time of the call. This function is asynchronous; it will run your callback function, of type <code>FDataRegistryItemAcquiredCallback</code>, when the search is complete. The function's return value is a <code>bool</code> that indicates success at scheduling the callback; a <code>false</code> return value means that there has been an error and your callback function will not run. A return value of <code>true</code> means that your callback function will run, but does not guarantee that the data item exists.",
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
            "callout_type": "warning",
            "blocks": [
              {
                "type": "paragraph",
                "content": "Caching struct pointers that you retrieve from a Data Registry can be unsafe. While some data items are always available, others load dynamically and the Data Registry can unload them without warning.\nIf you are potentially dealing with data that can be unloaded, the recommended practice is to use the data immediately after retrieving it, or cache your own copy rather than keeping the pointer from the Data Registry.",
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
        "excerpt_hash_id": "QYL",
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

## Integration with Game Features

The Data Registry plugin can add both Data Registries and individual Data Registry Sources from Game Feature plugins. For details on how this process works, see the [Game Features and Modular Gameplay](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-features-and-modular-gameplay-in-unreal-engine) page.
