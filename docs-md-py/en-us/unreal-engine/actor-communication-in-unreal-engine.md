# Actor Communication

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/actor-communication-in-unreal-engine

> Application Version: 5.7

```json
{
  "type": "switch",
  "switch_type": "programming_language",
  "switchable_blocks": {
    "blueprint": [
      {
        "type": "include",
        "excerpt_id": 1691,
        "excerpt_assignment_id": 1401,
        "blocks": [
          {
            "type": "paragraph",
            "content": "Blueprint scripting and C++ provide several ways to communicate and share information between Actors. This page gives you an overview of the different Actor communication methods available, as well as requirements and common use cases for each.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You will also find links to more detailed Quick Start guides for each Actor communication type.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Direct Communication",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Direct Actor communication is the most common method of sharing information between Actors in your Level.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "This method requires a reference to the target Actor so you can access its information from your working Actor. This communication type uses a one-to-one relationship between your working Actor and your target Actor.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "When to Use It",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Use this communication method if you have a reference to the specific Actor in your Level and you need to share information or trigger functionality within that specific Actor.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Examples",
            "level": 3,
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
                  "content": "Triggering an event on an Actor.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Getting information from an Actor in your Level.",
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
            "content": "Casting",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Casting is a common communication method where you take a reference to an Actor and try to convert it to a different class. If this conversion is successful, then you can use Direct communication to access its information and functionality.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "This method requires a reference to the Actor in your Level as you can use the <strong>Cast </strong>node to try to convert it to a specific class. This communication method uses a one-to-one relationship between your working Actor and your target Actor.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "When to Use It",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Use this communication method if you have a reference to an Actor and want to check if the Actor is of a certain class to access its information.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Examples",
            "level": 3,
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
                  "content": "Using a volume to overlap all Pawns and cast the Pawn reference to a particular subclass, such as a Character, to access its information.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Using an Actor's reference to cast to a common parent class and access its information.",
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
            "content": "Interfaces",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Interfaces define a set of common behaviors or capabilities that can be implemented by different Actor classes. This communication method simplifies the process of implementing the same type of functionality on different Actor classes.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "This method requires each Actor to implement the interface in order to access its common functions. You also need a reference to the Actor so you can call the interface function using that reference. This communication method uses a  one-to-one relationship between your working Actor and your target Actor.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "When to Use It",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Use this method when you want to create common functionality that applies to different types of Actors.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Examples",
            "level": 3,
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
                  "content": "Creating an interaction system where each Actor does something different when the player interacts. For example, a door Actor will open when the player interacts with it, while a light Actor will activate when the player performs the same interaction.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Applying damage to different Actors in your Level. Each Actor can react differently to the damage taken. For example, a wall Actor could break when taking damage, while a door Actor could open after taking damage.",
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
            "content": "Event Dispatchers",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Event Dispatchers are a communication method where one Actor triggers an event and other Actors that are listening to that event get notified.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "This method requires you to create Event Dispatchers on the working Actor and have your target Actors bind to them. This communication method uses a one-to-many relationship, where a single working Actor triggers the Event Dispatcher for many listening Actors.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "When to Use It",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Use this communication method when you want a single event to influence several different Actors.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Examples",
            "level": 3,
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
                  "content": "Creating a BossDied event in your game. Once a boss enemy dies, the event will trigger, causing a door Actor to open, the HUD Actor to display a message, and a chest Actor to open.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Creating a day / night cycle where the DayStarted event tells your NPCs that they must start their daily routines.",
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
            "content": "Actor Communication Reference Table",
            "level": 2,
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
                    "content": "Communication Type",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "enhanced_table_header",
                    "content": "When to Use It",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "enhanced_table_header",
                    "content": "Requirements",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "enhanced_table_header",
                    "content": "Example",
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
                    "content": "Direct Communication",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "When communicating with a specific instance of an Actor in your Level.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Need a reference to the Actor in your Level.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Triggering an event on a specific Actor in your Level.",
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
                    "content": "Casting",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "When you want to verify an Actor is of a certain class to access its properties.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Need a reference to an Actor in your Level to cast to the desired Actor class.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Accessing specific functionality of child Actors that share the same parent class.",
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
                    "content": "Interfaces",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "When adding the same functionality to different Actor classes.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Need a reference to the Actor in your Level and the Actor needs to implement the interface.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Adding an interaction behavior to different types of Actors.",
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
                    "content": "Event Dispatchers",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "When triggering an event from one Actor to many Actors.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Actors need to subscribe to the event to react to it.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Notifying many different types of Actors that an event has triggered.",
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
        "excerpt_hash_id": "5k6",
        "settings": {
          "is_hidden": false
        }
      }
    ],
    "cpp": [
      {
        "type": "include",
        "excerpt_id": 1692,
        "excerpt_assignment_id": 1402,
        "blocks": [
          {
            "type": "paragraph",
            "content": "Blueprint scripting and C++ provide several ways to communicate and share information between Actors. This page gives you an overview of the different Actor communication methods available, as well as requirements and common use cases for each.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "You will also find links to more detailed Quick Start guides for each Actor communication type.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Direct Communication",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Direct Actor communication is the most common method of sharing information between Blueprint Actors in your Level.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "This method requires a reference to the target Actor class Blueprint so you can access its information from your working Actor. This communication type uses a one-to-one relationship between your working Actor and your target Actor.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "When to Use It",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Use this communication method if you have a reference to the specific Actor class Blueprint in your Level and you need to share information or trigger functionality within that specific Actor class Blueprint.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Examples",
            "level": 3,
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
                  "content": "Triggering an event on an Actor.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Getting information from an Actor in your Level.",
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
            "content": "Casting With Blueprint Classes",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Casting is a common communication method where you take a reference to an Actor class Blueprint and try to convert it to a different class. If this conversion is successful, then you can use Direct communication to access its information and functionality.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "This method requires a reference to the Actor class Blueprint in your Level as you can use <strong>casting </strong>to try to convert it to a specific class. This communication method uses a one-to-one relationship between your working Actor and your target Actor.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "When to Use It",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Use this communication method if you have a reference to an Actor class Blueprint and want to check if the Actor class Blueprint is of a certain class to access its information.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Examples",
            "level": 3,
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
                  "content": "Using an AVolume to overlap all APawns and cast the Pawn reference to a particular subclass, such as an ACharacter, to access its information.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Using an Actor class Blueprint's reference to cast to a common parent class and access its information.",
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
            "content": "Interfaces",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Interfaces (UInterface) define a set of common method behaviors that can be implemented by different classes. This communication type simplifies the process of implementing the same type of functionality on different Actor class Blueprints.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "This method requires each Actor to implement the interface in order to access its common methods. You will require a reference to the Actor class Blueprint so you can call the interface function using that reference. This communication method uses a  one-to-one relationship between your working Actor and your target Actor.",
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
                "content": "Note: See <a data-document-id=\"3227268\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/interfaces-in-unreal-engine?application_version=5.5\">Interfaces</a> for additional documentation.",
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
            "content": "When to Use It",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Use this method when you want to create common functionality that applies to different types of Blueprint Actors.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "header",
            "content": "Examples",
            "level": 3,
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
                  "content": "Creating an interaction system where each Actor class Blueprint does something different when the player interacts. For example, a door Actor will open when the player interacts with it, while a light Actor will activate when the player performs the same interaction.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Applying damage to different Actors in your Level. Each Actor class Blueprint can react differently to the damage taken. For example, a wall Actor could break when taking damage, while a door Actor could open after taking damage.",
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
            "content": "Delegates",
            "level": 2,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Delegates can call methods in Actor class Blueprints in a type-safe way. A delegate can be bound dynamically to form a relationship where one Actor triggers an event on another Actor \"listening\" to be notified for that event.",
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
                "content": "Note: See <a data-document-id=\"3227461\" href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/delegates-and-lambda-functions-in-unreal-engine\">Delegates</a> for additional documentation.",
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
            "content": "When to Use It",
            "level": 3,
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "Use this communication type when you want a single event to influence several different Actor class Blueprints.",
            "settings": {
              "is_hidden": false
            }
          },
          {
            "type": "paragraph",
            "content": "<strong>Examples</strong>",
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
                  "content": "Creating a BossDied event in your game. Once a boss enemy dies, the event will trigger, causing a door Actor to open, the UMG Blueprint to display a message, and a chest Actor to open.",
                  "settings": {
                    "is_hidden": false
                  }
                }
              ],
              [
                {
                  "type": "paragraph",
                  "content": "Creating a day / night cycle where the DayStarted event tells your NPCs that they must start their daily routines.",
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
            "content": "Communicating with Blueprint Classes Reference Table",
            "level": 2,
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
                    "content": "Communication Type",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "enhanced_table_header",
                    "content": "When to Use It",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "enhanced_table_header",
                    "content": "Requirements",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "enhanced_table_header",
                    "content": "Example",
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
                    "content": "Direct Communication",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "When communicating with a specific instance of an Actor in your Level.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Need a reference to the Actor in your Level.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Triggering an event on a specific Actor in your Level.",
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
                    "content": "Casting",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "When you want to verify an Actor is of a certain class to access its properties.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Need a reference to an Actor in your Level to cast to the desired Actor class.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Accessing specific functionality of child Actors that share the same parent class.",
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
                    "content": "Interfaces",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "When adding the same functionality to different Actor classes.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Need a reference to the Actor in your Level and the Actor needs to implement the interface.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Adding an interaction behavior to different types of Actors.",
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
                    "content": "Event Dispatchers",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "When triggering an event from one Actor to many Actors.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Actors need to subscribe to the event to react to it.",
                    "settings": {
                      "is_hidden": false
                    }
                  }
                ],
                [
                  {
                    "type": "paragraph",
                    "content": "Notifying many different types of Actors that an event has triggered.",
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
        "excerpt_hash_id": "y3y",
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

## Quick Start Guides

- [Related Document](en-us/unreal-engine/actor-communication-in-unreal-engine.md)
