# Datasmith Exporter Plugin Release Notes

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-exporter-plugin-release-notes-for-unreal-engine

> Application Version: 5.7

## Datasmith exporter Plugin: SketchUp 5.7.300

**New:**

- Windows: Mac: The Datasmith Exporter Plugin is now signed in Sketchupʼs Extension Manager. The Datasmith Exporter Plugin is now signed in Sketchupʼs Extension Manager.

## Datasmith Exporter Plugin: SketchUp

**New:**

- Provides a way to export the current viewport camera transform information in Datasmith and through Direct Link.

**Bug Fix:**

- You can now install the Datasmith Exporter plugin if a previous install is not found.

## Datasmith Exporter Plugin: Rhino 3D

**New:**

- Provides a way to export the current viewport camera transform information in Datasmith and through Direct Link.
- Provides a way to export Named views camera transform information in Datasmith and through Direct Link.

**Bug Fix:**

- Direct Link for Unreal Engine 5.7 updates lights on settings change in Rhino.
- Fixed UV repetition on objects for Datasmith (.udatasmith files)
- Allow Install of Datasmith Exporter plugin if previous install is not found.
- Material Handling: Custom Materials Exported as expected. Double Sided Materials Currently exports only the front face.
- Emission: Only intensity = 1 is supported.
- Gem and Glass: Partially supported. Generates a material with some opacity, which is not equivalent to true clarity. Refraction values cannot be exported due to a limitation in the Datasmith material, where refraction mode is not exposed or changeable.
- Metal: Exported as expected.
- Paint: No special behavior. Physically-based. Exported as expected.
- Picture Partially supported. Only basic properties are exported. Masking and other advanced attributes are ignored.
- Plaster Exported as expected.
- Plastic Exported as expected.
- Fixed the issue where Rhino Mac force shutdowns when clicking Sync for Direct Link Resolved

## Datasmith Exporter Plugin: ArchiCAD

**New:**

- Now supports ArchiCAD 29.

**Bug Fix:**

- You can now install the Datasmith Exporter plugin if a previous install is not found.

## Datasmith Exporter Plugin: NavisWorks

**Bug Fix:**

- You can now install the Datasmith Exporter plugin if a previous install is not found.

## Datasmith Exporter Plugin: SolidWorks

**Bug Fix:**

- You can now install the Datasmith Exporter plugin if a previous install is not found.
