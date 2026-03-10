# Python Scripting

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/python-scripting

> Application Version: 5.7

The download and ingest of takes using **Capture Manager** can be automated as part of a performance capture workflow with the Python API. The Capture Manager plugin includes a number of example scripts that can be used as a reference and modified to suit your specific requirements. Python scripts should be executed using the **LiveLinkHub** executable.

```json
{
  "type": "callout",
  "callout_type": "warning",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Use forward slashes <code class=\"inline-code\">/</code>(instead of <code class=\"inline-code\">\\</code>) for paths that appear in a command to avoid problems with character parsing.",
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

## Download Takes

An example script for downloading data from a **Live Link Face** device is provided in the plugin. This can be used as a reference, and modified to suit your specific requirements. It can be found in the following location:

`\Engine\Plugins\VirtualProduction\CaptureManager\CaptureManagerApp\Content\Python\examples\live_link_face_download_only.py`

The script can be run from a Windows terminal (such as PowerShell) using the following command, with the `ip-address` parameter updated for your environment:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "command_line",
  "title": "",
  "code_preview": "LiveLinkHub.exe -ExecutePythonScript=&quot;&lt;path-to-ue-installation&gt;/Engine/Plugins/VirtualProduction/CaptureManager/CaptureManagerApp/Content/Python/examples/live_link_face_download_only.py --ip-address &lt;ip-address&gt;&quot;",
  "lines_of_code": 1,
  "id": 48637,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0ODYzNywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI1OjM2KzAwOjAwIn0=--87b39f8573e76268a398fdba72ec87251d65fc3879125f2a886277ef7b6cd22b",
  "settings": {
    "is_hidden": false
  }
}
```

## Ingest Takes

Several example scripts are provided to demonstrate ingesting data from [Mono Video](https://dev.epicgames.com/documentation/en-us/unreal-engine/mono-video-device), [Live Link Face](https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-face-device), and [Take Archive](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-archive-device) devices. These can be used as a reference and modified to suit your specific requirements. They can be found in the following folder:

`\Engine\Plugins\VirtualProduction\CaptureManager\CaptureManagerApp\Content\Python\examples\`

These scripts can be run from a Windows terminal (such as PowerShell) using the following command as a template. You will need to update the `path-to-takes` parameter for your environment:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "command_line",
  "title": "",
  "code_preview": "LiveLinkHub.exe -ExecutePythonScript=&quot;&lt;path-to-ue-installation&gt;/Engine/Plugins/VirtualProduction/CaptureManager/CaptureManagerApp/Content/Python/examples/take_archive_ingest.py --archive-path &lt;path-to-takes&gt;&quot;",
  "lines_of_code": 1,
  "id": 48638,
  "url_signature": "eyJzbmlwcGV0X2lkIjo0ODYzOCwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjI1OjM2KzAwOjAwIn0=--6a666b5ef61f4799f353f148f853df7fe2af8003caf3168066fb6edff7ee92b5",
  "settings": {
    "is_hidden": false
  }
}
```
