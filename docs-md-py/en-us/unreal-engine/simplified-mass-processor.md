# Simplified Mass Processor/Query API (Query Executor)

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/simplified-mass-processor

> Application Version: 5.7

## Overview

The simplified **Mass Processor/Query API** aims to reduce boilerplate for creating Mass processor logic, and to increase code readability and type safety. This is an optional API and the current style will continue to be supported.

### Creating a Mass Processor with the QueryExecutor

Create a struct in your .cpp inheriting UE::Mass::FQueryExecutor following this example:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "struct FExampleExecutor : public UE::Mass::FQueryExecutor\n{\n  UE::Mass::FQueryDefinition&lt;\n    UE::Mass::FMutableFragmentAccess&lt;FExampleFragmentA&gt;,\n    UE::Mass::FConstSubsystemAccess&lt;UExampleSubsystem&gt;,\n    UE::Mass::FMassTagRequired&lt;FExampleTag&gt;\n  &gt; Accessors{ *this };\n\n\n  virtual void Execute(FMassExecutionContext&amp; Context)\n",
  "lines_of_code": 17,
  "id": 55953,
  "url_signature": "eyJzbmlwcGV0X2lkIjo1NTk1MywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIyOjIxKzAwOjAwIn0=--6162e35f35f88d15508c7e066c4d62a214af6b0f6a596419f33f2e89bb3274a1",
  "settings": {
    "is_hidden": false
  }
}
```

Currently QueryExecutors need to be owned by a regular UMassProcessor. This requirement will be removed in a future update.

To create a wrapper UMassProcessor:

1. Create a class that inherits from UMassProcessor.
2. Do not override the ConfigureQuery or Execute functions.
3. Create the QueryExecutor in the constructor for that processor as follows:

## Limitations

Currently a UMassProcessor is still needed to interface with the Mass Phase Executor. This will be remedied in a future update.

The declaration of the FQueryDefinition template requires full definitions of the query types and as such, doing so in a header file should be limited to predefined query definitions (not part of larger interface headers). General best practice is to declare them privately in the .cpp file where they are used.
