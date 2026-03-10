# PCG Biome Glossary

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-glossary-in-unreal-engine

> Application Version: 5.7

The PCG Biome Core and Sample Plugins are examples of how to use the [PCG Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-overview). This page provides definitions for many of the terms used in the documentation for this project.

```json
{
  "type": "glossary",
  "tags": [
    "pcg-biome-glossary"
  ],
  "glossary_terms": [
    {
      "id": 3947577,
      "hash_id": "8JPGJB",
      "slug": "assembly-pcg",
      "title": "Assembly (PCG)",
      "seo_slug": "assembly-pcg",
      "blocks": [
        {
          "type": "paragraph",
          "content": "PCG point data created and exported from all static meshes and instanced static meshes found in a level, using the <strong>Asset Action &gt; Create PCG Assets from Level(s)</strong>.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10284,
        "name": "assembly-pcg",
        "previous_names": [
          "assembly-pcg"
        ]
      }
    },
    {
      "id": 3947563,
      "hash_id": "rbo4b4",
      "slug": "biome",
      "title": "Biome",
      "seo_slug": "biome",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A volume in space defined by a biome definition and a list of biome assets.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10270,
        "name": "biome",
        "previous_names": [
          "biome"
        ]
      }
    },
    {
      "id": 4595954,
      "hash_id": "eJQmmd",
      "slug": "biome-actors",
      "title": "Biome Actors",
      "seo_slug": "biome-actors",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Blueprint actors that are used to set up biomes in a world. These include biome volumes, biome splines, and biome textures.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 19413,
        "name": "biome-actors",
        "previous_names": [
          "biome-actors"
        ]
      }
    },
    {
      "id": 3947566,
      "hash_id": "l48Y4a",
      "slug": "biome-assets",
      "title": "Biome Assets",
      "seo_slug": "biome-assets",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Data assets that contain asset properties to be spawned by Biome Core.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10273,
        "name": "biome-assets",
        "previous_names": [
          "biome-assets"
        ]
      }
    },
    {
      "id": 3947560,
      "hash_id": "vvarv8",
      "slug": "biome-core",
      "title": "Biome Core",
      "seo_slug": "biome-core",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A data-driven biome creation tool that provides a fixed pipeline with customizable steps. The PCG Biome Core plugin contains a collection of PCG graphs and sub-graphs used to procedurally generate biomes.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10267,
        "name": "biome-core",
        "previous_names": [
          "biome-core"
        ]
      }
    },
    {
      "id": 3947575,
      "hash_id": "Bx3Xxa",
      "slug": "biome-core-runtime",
      "title": "Biome Core Runtime",
      "seo_slug": "biome-core-runtime",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A separate PCG component and graph, used for GPU runtime generation of detailed assets spawning around the camera.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10282,
        "name": "biome-core-runtime",
        "previous_names": [
          "biome-core-runtime"
        ]
      }
    },
    {
      "id": 3947561,
      "hash_id": "05PY5o",
      "slug": "biome-sample",
      "title": "Biome Sample",
      "seo_slug": "biome-sample",
      "blocks": [
        {
          "type": "paragraph",
          "content": "The PCG Biome Sample plugin contains a level, data assets and custom PCG graphs used to showcase procedural biome generation using Biome Core.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10268,
        "name": "biome-sample",
        "previous_names": [
          "biome-sample"
        ]
      }
    },
    {
      "id": 3947581,
      "hash_id": "dK4aKY",
      "slug": "child-points",
      "title": "Child Points",
      "seo_slug": "child-points",
      "blocks": [
        {
          "type": "paragraph",
          "content": "All points created from the recursive transform step to spawn child assets.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10288,
        "name": "child-points",
        "previous_names": [
          "child-points"
        ]
      }
    },
    {
      "id": 3947569,
      "hash_id": "o3KX3g",
      "slug": "filter-graph",
      "title": "Filter Graph",
      "seo_slug": "filter-graph",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A PCG Graph that processes points and writes to a defined filter attribute from its logic or texture projection.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10276,
        "name": "filter-graph",
        "previous_names": [
          "filter-graph"
        ]
      }
    },
    {
      "id": 3947568,
      "hash_id": "QPKnPe",
      "slug": "filters",
      "title": "Filters",
      "seo_slug": "filters",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A list of filter graphs.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10275,
        "name": "filters",
        "previous_names": [
          "filters"
        ]
      }
    },
    {
      "id": 3947564,
      "hash_id": "Nz6lz2",
      "slug": "generator",
      "title": "Generator",
      "seo_slug": "generator",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A data asset with <b>Type</b>, <b>Priority</b>, and <b>Generator Graph</b> properties, referred to by biome assets entries.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10271,
        "name": "generator",
        "previous_names": [
          "generator"
        ]
      }
    },
    {
      "id": 3947565,
      "hash_id": "V6dA6a",
      "slug": "generator-graph",
      "title": "Generator Graph",
      "seo_slug": "generator-graph",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A PCG Graph that produces root points used for placing assets in the world.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10272,
        "name": "generator-graph",
        "previous_names": [
          "generator-graph"
        ]
      }
    },
    {
      "id": 4595988,
      "hash_id": "E6OQxl",
      "slug": "global-biome-core-graph",
      "title": "Global Biome Core Graph",
      "seo_slug": "global-biome-core-graph",
      "blocks": [
        {
          "type": "paragraph",
          "content": "On the Biome Core BP actor, the PCG component has the Biome Core graph assigned to it. When executed, the graph gets all data produced by all local Biome Core graphs in each Biome actor. The data goes through a difference by priority step, then spawns the remaining points as static meshes, assemblies, or actors.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 19419,
        "name": "global-biome-core-graph",
        "previous_names": [
          "global-biome-core-graph"
        ]
      }
    },
    {
      "id": 4595962,
      "hash_id": "xO6aaw",
      "slug": "global-parameters",
      "title": "Global parameters",
      "seo_slug": "global-parameters",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Graph parameters on the global Biome Core that impact its global behavior. Includes filter graphs and the debug cache display.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 19414,
        "name": "global-parameters",
        "previous_names": [
          "global-parameters"
        ]
      }
    },
    {
      "id": 3947573,
      "hash_id": "jM36MY",
      "slug": "hierarchical-generation",
      "title": "Hierarchical Generation",
      "seo_slug": "hierarchical-generation",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Subdivides the volume and processing into multiple grids of different size at which parts of a PCG graph executes. Hierarchical Generation speeds up local updates by distributing computing at different grid sizes and outputs data into separate actors that can be streamed in individually. For more information, see <a href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-generation-modes-in-unreal-engine?application_version=5.5\">Using PCG Generation Modes</a>.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10280,
        "name": "hierarchical-generation",
        "previous_names": [
          "hierarchical-generation"
        ]
      }
    },
    {
      "id": 4595980,
      "hash_id": "LenBor",
      "slug": "injected-data",
      "title": "Injected Data",
      "seo_slug": "injected-data",
      "blocks": [
        {
          "type": "paragraph",
          "content": "External data injected at different stages of the Biome Core to exclude or add points. Divided in different types based on their entry point within the pipeline: exclusions and custom biome data. ",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 19418,
        "name": "injected-data",
        "previous_names": [
          "injected-data"
        ]
      }
    },
    {
      "id": 4595977,
      "hash_id": "8J84YJ",
      "slug": "local-biome-cache",
      "title": "Local Biome Cache",
      "seo_slug": "local-biome-cache",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Point data computed locally for each biome actor and used as the bounding shape for generators used in the biome. The local cache is also used to apply the biome definition onto the produced points.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 19415,
        "name": "local-biome-cache",
        "previous_names": [
          "local-biome-cache"
        ]
      }
    },
    {
      "id": 4595979,
      "hash_id": "ndbQ0o",
      "slug": "local-biome-core-graph",
      "title": "Local Biome Core Graph",
      "seo_slug": "local-biome-core-graph",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Each biome actor has its own PCG component and a local Biome Core graph assigned to it. The local Biome Core graph generates all data locally per biome actor. The output of that local generation is then used in the global Biome Core graph.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 19417,
        "name": "local-biome-core-graph",
        "previous_names": [
          "local-biome-core-graph"
        ]
      }
    },
    {
      "id": 4595978,
      "hash_id": "akQ4Jx",
      "slug": "local-parameters",
      "title": "Local parameters",
      "seo_slug": "local-parameters",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Graph parameters in the local Biome Core that impact its local behavior. Includes preview mode, debug local cache display, and biome blending controls. Partitioning Biome Core graph parameters that impact its global behavior. Includes filter graphs and the debug cache display.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 19416,
        "name": "local-parameters",
        "previous_names": [
          "local-parameters"
        ]
      }
    },
    {
      "id": 3947580,
      "hash_id": "Leqxev",
      "slug": "root-points",
      "title": "Root Points",
      "seo_slug": "root-points",
      "blocks": [
        {
          "type": "paragraph",
          "content": "All points provided by the generators and their graphs.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10287,
        "name": "root-points",
        "previous_names": [
          "root-points"
        ]
      }
    },
    {
      "id": 3947576,
      "hash_id": "D3pe3J",
      "slug": "runtime-assets",
      "title": "Runtime Assets",
      "seo_slug": "runtime-assets",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A data asset containing properties of assets to be spawned by Biome Core runtime.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10283,
        "name": "runtime-assets",
        "previous_names": [
          "runtime-assets"
        ]
      }
    },
    {
      "id": 3947574,
      "hash_id": "5l1elm",
      "slug": "runtime-hierarchical-generation",
      "title": "Runtime Hierarchical Generation",
      "seo_slug": "runtime-hierarchical-generation",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Generates grid cells at runtime based on streaming source or PCG generation source components. Uses the generation radius of each grid size configured in the PCG Graph. Uses the same multi-level grid size approach as the Hierarchical Generation. For more information, see <a href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-generation-modes-in-unreal-engine?application_version=5.5\">Using PCG Generation Modes</a>.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10281,
        "name": "runtime-hierarchical-generation",
        "previous_names": [
          "runtime-hierarchical-generation"
        ]
      }
    },
    {
      "id": 3947570,
      "hash_id": "26KP62",
      "slug": "transform-graph",
      "title": "Transform Graph",
      "seo_slug": "transform-graph",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A PCG Graph that takes points from a generator or parent transformed points to change their properties. Used for generating and placing child points.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10277,
        "name": "transform-graph",
        "previous_names": [
          "transform-graph"
        ]
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```
