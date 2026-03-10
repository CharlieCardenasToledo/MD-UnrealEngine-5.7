# Horde Glossary

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-glossary-for-unreal-engine

> Application Version: 5.7

```json
{
  "type": "glossary",
  "tags": [
    "horde-glossary"
  ],
  "glossary_terms": [
    {
      "id": 3947535,
      "hash_id": "ndvPGy",
      "slug": "acl-action",
      "title": "Acl Action",
      "seo_slug": "acl-action",
      "blocks": [
        {
          "type": "paragraph",
          "content": "  The ability to perform a certain operation on an entity in Horde, such as <code>ViewJob</code> or <code>DownloadTool</code>. See <a href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-schema-for-unreal-engine?application_version=5.5#aclactions\">Config &gt; Schema &gt; AclActions</a> for a full list.  ",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10244,
        "name": "acl-action",
        "previous_names": [
          "acl-action"
        ]
      }
    },
    {
      "id": 3947537,
      "hash_id": "dK4azY",
      "slug": "acl-profile",
      "title": "Acl Profile",
      "seo_slug": "acl-profile",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A list of actions that can be given to a user, without having to list each individual action each time. Similar to a macro.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10246,
        "name": "acl-profile",
        "previous_names": [
          "acl-profile"
        ]
      }
    },
    {
      "id": 3947536,
      "hash_id": "Leqx0v",
      "slug": "acl-scope",
      "title": "Acl Scope",
      "seo_slug": "acl-scope",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Used to refer to a layer within Horde's hierarchical permissions system. Jobs are an acl scope within a stream, which are an acl scope within a project, which is an acl scope within the global permissions scope. Entitlements to perform actions are typically inherited from parent to child scopes, unless explicitly forbidden by setting the <code>inherit</code> property in an <a href=\"https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-schema-for-unreal-engine?application_version=5.5#aclconfig\">AclConfig</a> to false.  ",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10245,
        "name": "acl-scope",
        "previous_names": [
          "acl-scope"
        ]
      }
    },
    {
      "id": 3947529,
      "hash_id": "jM36bY",
      "slug": "agent",
      "title": "Agent",
      "seo_slug": "agent",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A service on a remote machine that connects to the Horde server and can be sent work to execute.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10238,
        "name": "agent",
        "previous_names": [
          "agent"
        ]
      }
    },
    {
      "id": 3947548,
      "hash_id": "JnXVng",
      "slug": "aggregate",
      "title": "Aggregate",
      "seo_slug": "aggregate",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A name given to a set of nodes within a graph as a shorthand.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10256,
        "name": "aggregate",
        "previous_names": [
          "aggregate"
        ]
      }
    },
    {
      "id": 3947531,
      "hash_id": "Bx3Xpa",
      "slug": "analytics",
      "title": "Analytics",
      "seo_slug": "analytics",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Umbrella term for data gathering and analysis.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10240,
        "name": "analytics",
        "previous_names": [
          "analytics"
        ]
      }
    },
    {
      "id": 3947542,
      "hash_id": "b8ra42",
      "slug": "backend",
      "title": "Backend",
      "seo_slug": "backend",
      "blocks": [
        {
          "type": "paragraph",
          "content": "The underlying storage provider for a particular namespace. Horde supports many types backends, from local disks to cloud object stores.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10250,
        "name": "backend",
        "previous_names": [
          "backend"
        ]
      }
    },
    {
      "id": 3947543,
      "hash_id": "q0vegd",
      "slug": "blob",
      "title": "Blob",
      "seo_slug": "blob",
      "blocks": [
        {
          "type": "paragraph",
          "content": "An opaque byte stream and set of outward references to other blobs.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10251,
        "name": "blob",
        "previous_names": [
          "blob"
        ]
      }
    },
    {
      "id": 3947546,
      "hash_id": "WdGxJL",
      "slug": "buildgraph",
      "title": "BuildGraph",
      "seo_slug": "buildgraph",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Epic Games' scripting language for large-scale build pipelines (for example, compiling, cooking, and packaging a game to run on multiple platforms). Describes a parameterized dependency graph between nodes that produce artifacts. Epic uses BuildGraph internally to make Unreal Engine and Fortnite builds, and run all the automation around them. Horde executes BuildGraph scripts in jobs, which are created from templates.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10254,
        "name": "buildgraph",
        "previous_names": [
          "buildgraph"
        ]
      }
    },
    {
      "id": 3947545,
      "hash_id": "1X5KWJ",
      "slug": "bundle",
      "title": "Bundle",
      "seo_slug": "bundle",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Container for a set of blobs that is written to the underlying storage system. Bundles support compression and reduce the overhead of storing small objects.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10253,
        "name": "bundle",
        "previous_names": [
          "bundle"
        ]
      }
    },
    {
      "id": 3947538,
      "hash_id": "OnzlJo",
      "slug": "claims",
      "title": "Claims",
      "seo_slug": "claims",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Key/value string pair that makes a statement about that user. Claims are part of the OAuth2 standard, and identity providers maintain a list of unique claims for a user. To prevent collisions between different applications, keys typically use a URI with an owned domain name to ensure global uniqueness - though the URI does not identify an actual web resource. Horde's internally-issued claims all begin with <code>http://epicgames.com/ue/horde</code>.  ",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10247,
        "name": "claims",
        "previous_names": [
          "claims"
        ]
      }
    },
    {
      "id": 3947551,
      "hash_id": "PwKzwk",
      "slug": "continuous-delivery-cd",
      "title": "Continuous Delivery (CD)",
      "seo_slug": "continuous-delivery-cd",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Abbreviation for 'Continuous Delivery'; the process of continually producing new builds of a product through build automation.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10259,
        "name": "continuous-delivery-cd",
        "previous_names": [
          "continuous-delivery-cd"
        ]
      }
    },
    {
      "id": 3947550,
      "hash_id": "K3dx3d",
      "slug": "continuous-integration-ci",
      "title": "Continuous Integration (CI)",
      "seo_slug": "continuous-integration-ci",
      "blocks": [
        {
          "type": "paragraph",
          "content": "The process of continually validating a stream of changes submitted to a codebase through build automation.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10258,
        "name": "continuous-integration-ci",
        "previous_names": [
          "continuous-integration-ci"
        ]
      }
    },
    {
      "id": 3947539,
      "hash_id": "gwyEKY",
      "slug": "entitlement",
      "title": "Entitlement",
      "seo_slug": "entitlement",
      "blocks": [
        {
          "type": "paragraph",
          "content": "The ability of a user to perform a certain action.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10248,
        "name": "entitlement",
        "previous_names": [
          "entitlement"
        ]
      }
    },
    {
      "id": 3947554,
      "hash_id": "eJkaJx",
      "slug": "job",
      "title": "Job",
      "seo_slug": "job",
      "blocks": [
        {
          "type": "paragraph",
          "content": "An instance of a template run on a particular changelist with certain parameters.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10261,
        "name": "job",
        "previous_names": [
          "job"
        ]
      }
    },
    {
      "id": 3947555,
      "hash_id": "45E35W",
      "slug": "job-batch",
      "title": "Job Batch",
      "seo_slug": "job-batch",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A set of steps within a job that are run sequentially on a single machine (in a lease) using a synced workspace. Steps within the batch may or may not have dependencies on each other.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10262,
        "name": "job-batch",
        "previous_names": [
          "job-batch"
        ]
      }
    },
    {
      "id": 3947556,
      "hash_id": "Mpnxpr",
      "slug": "job-step",
      "title": "Job Step",
      "seo_slug": "job-step",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A unit of work that can pass or fail, tracking the execution of a node.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10263,
        "name": "job-step",
        "previous_names": [
          "job-step"
        ]
      }
    },
    {
      "id": 3947557,
      "hash_id": "GVOqVL",
      "slug": "label",
      "title": "Label",
      "seo_slug": "label",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Annotates a set of nodes whose outcomes can be monitored as a single unit. Labels are displayed prominently on the Horde dashboard, showing information on which parts of a build have succeeded or failed.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10264,
        "name": "label",
        "previous_names": [
          "label"
        ]
      }
    },
    {
      "id": 3947530,
      "hash_id": "5l1eKm",
      "slug": "lease",
      "title": "Lease",
      "seo_slug": "lease",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A unit of work that an agent is given to execute.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10239,
        "name": "lease",
        "previous_names": [
          "lease"
        ]
      }
    },
    {
      "id": 3947532,
      "hash_id": "D3pe4J",
      "slug": "metrics",
      "title": "Metrics",
      "seo_slug": "metrics",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Aggregated data computed from telemetry events matching a set of configured criteria for a particular time interval.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10241,
        "name": "metrics",
        "previous_names": [
          "metrics"
        ]
      }
    },
    {
      "id": 3947541,
      "hash_id": "kd8JYE",
      "slug": "namespace",
      "title": "Namespace",
      "seo_slug": "namespace",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A logical partition of the storage system that can have custom permissions, behaviors, and garbage collection policies.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10249,
        "name": "namespace",
        "previous_names": [
          "namespace"
        ]
      }
    },
    {
      "id": 3947547,
      "hash_id": "6WG4el",
      "slug": "node",
      "title": "Node",
      "seo_slug": "node",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A unit of work within a BuildGraph script. Each node may have dependencies on any other nodes or build outputs and executes a sequence of operations to produce its outputs. A node is executed as a job step.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10255,
        "name": "node",
        "previous_names": [
          "node"
        ]
      }
    },
    {
      "id": 3947558,
      "hash_id": "wYorYw",
      "slug": "preflight",
      "title": "Preflight",
      "seo_slug": "preflight",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A build run to test the contents of changes before submitting via a Perforce shelf.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10265,
        "name": "preflight",
        "previous_names": [
          "preflight"
        ]
      }
    },
    {
      "id": 3947559,
      "hash_id": "mJPKJ3",
      "slug": "presubmit",
      "title": "Presubmit",
      "seo_slug": "presubmit",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A suite of tests designed to run before users submit changes.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10266,
        "name": "presubmit",
        "previous_names": [
          "presubmit"
        ]
      }
    },
    {
      "id": 3947544,
      "hash_id": "E6M4p1",
      "slug": "ref",
      "title": "Ref",
      "seo_slug": "ref",
      "blocks": [
        {
          "type": "paragraph",
          "content": "A named reference to a blob. Refs are typically the entry point into the storage system for client applications. Blobs that are not directly or indirectly referenced through a ref are garbage collected.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10252,
        "name": "ref",
        "previous_names": [
          "ref"
        ]
      }
    },
    {
      "id": 3947549,
      "hash_id": "YLeaLL",
      "slug": "target",
      "title": "Target",
      "seo_slug": "target",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Specifies the nodes and aggregates within a BuildGraph script a user wishes to execute.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10257,
        "name": "target",
        "previous_names": [
          "target"
        ]
      }
    },
    {
      "id": 3947533,
      "hash_id": "8JPGOB",
      "slug": "telemetry",
      "title": "Telemetry",
      "seo_slug": "telemetry",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Individual events sent by an application to the Horde server. Horde processes telemetry events as schema-less JSON objects.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10242,
        "name": "telemetry",
        "previous_names": [
          "telemetry"
        ]
      }
    },
    {
      "id": 3947553,
      "hash_id": "3epXeW",
      "slug": "template",
      "title": "Template",
      "seo_slug": "template",
      "blocks": [
        {
          "type": "paragraph",
          "content": "Describes the options for running a particular BuildGraph script and specifies parameters for how to execute it.",
          "settings": {
            "is_hidden": false
          }
        }
      ],
      "anchor": {
        "id": 10260,
        "name": "template",
        "previous_names": [
          "template"
        ]
      }
    }
  ],
  "settings": {
    "is_hidden": false
  }
}
```
