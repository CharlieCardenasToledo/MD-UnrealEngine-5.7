# Alembic File Importer

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/alembic-file-importer-in-unreal-engine

> Application Version: 5.7

The Alembic file format (ABC) is an open computer graphics interchange framework that distills complex, animated scenes into a non-procedural, application-independent set of baked geometric results. **Unreal Engine 4** (UE4) enables you to import your Alembic files through the Alembic Importer, which gives you the freedom to create complex animations externally, then bring them into UE4 and render them in real-time.

Import Alembic files in a similar manner to several of the other forms of [importing content](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine) into UE4.

You can also watch the Unreal Engine Live Stream on Animation Topics which include the Alembic File Importer:

## Exporting Alembic Caches

To export an Alembic cache from Autodesk Maya:

1. From the **File Menu** under **Cache** and **Alembic Cache**, select **Export All to Alembic...** (or **Selection**) based on your needs.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df0b70be-4837-4cb0-a31f-e7811b61fc9f/maya_01.png)
2. In the **Export** window under **Advanced Options**, enable **UV Write** and **Write Face Sets** options, then click **Export**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d7b12f2d-210b-4f7a-824f-2973e6c2f45c/maya_02.png)

   You will need to enable **Write Face Sets** if you plan to create Materials during import into Unreal Engine 4 as Materials are created based on found Face Set Names.

## Importing Alembic Files

To import an Alembic File into Unreal Engine 4:

1. Inside the **Content Browser**, click the **Import** button and point to your **.abc** file.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2d86cbf4-d53c-4e5d-a12e-6e897a9bfe1d/alembicimport_00.png "AlembicImport_00.png")
2. The **Alembic Cache Import Options** window will appear where you can define the method/options for importing. This window displays the name of the file and location you are importing from. You will also see checkbox options for the assets within your file that you can choose to include or exclude from the import process (you can also use the top level checkbox to include or exclude all tracks).

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7e91e88c-1842-4a3d-bebf-9a24c65bc5e9/alembicimport_01.png "AlembicImport_01.png")

Currently, Unreal Engine only supports meshes containing three and four-sided polygons. Your Alembic data will fail to load if your geometry contains any polygons with greater than four sides, or if your geometry is made from NURBS or SubDiv surfaces.

## Import as Static Mesh

During the import process, you can define how to import your content. By default, the **Alembic Import Type** is set to **Static Mesh**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0661dfd1-a080-465a-bbbc-eb6715ebd0c1/importtype_01.png "ImportType_01.png")

Importing an Alembic cache as a Static Mesh will import a single frame, specified by **Frame Start** value in the **Sampling** section, as one or multiple Static Meshes. The Alembic animation from that frame will be imported as a Static Mesh asset and without animation. The following settings are also available:

### Static Mesh Options

| Setting | Description |
| --- | --- |
| **Merge Meshes** | Enable to merge the Static Meshes on import (this can cause problems with overlapping UV sets). |
| **Propagate Matrix Transformations** | Enable to apply matrix transformations to the meshes before merging them. (See Propagate Matrix Transformations.) |
| **Generate Lightmap UVs** | Enable to create [lightmap UVs](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-lightmapping-in-unreal-engine) on import. |

When importing an Alembic file as a Static Mesh, if your data contains several meshes within it, you can choose **Merge Meshes** to create a single Static Mesh inside Unreal Engine. If you disable this option, each mesh within your Alembic file will be imported into UE4 as an individual Static Mesh instead.

### Propagate Matrix Transformations

When enabling **Merge Meshes**, consider whether or not to **Propagate Matrix Transformations** prior to merging the meshes. This will take the transformation data contained within the Alembic file and propagate it to the meshes upon merging so they retain their transform data.

Consider the sample scene created below which we export as an Alembic cache.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e0d0dbe4-6dc9-4725-86c5-4d46c4e9f4c0/mayaobjects.png)

When we import the file into UE4 as a Static Mesh with **Merge Meshes** and **Propagate Matrix Transformations** we get the following:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f82c3338-d2ab-418c-a697-f29830f2c0bc/importmesh1.png)

If we **Merge Meshes** but uncheck the **Propagate Matrix Transformations** we get the following:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93b66f67-47ce-4a44-974c-a43f65864d97/importmesh2.png)

Each of the meshes are merged at the 0,0,0 origin.

### Sampling Options

![Alembic Sampling options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/869df70c-ea97-4e7a-93bc-b17f58cb0fe1/alembicsampling.png "Alembic Sampling options")

| Setting | Description |
| --- | --- |
| **Sampling Type** | The type of sampling performed while importing the animation.   * **Per Frame (default)**: Samples the animation according to the imported data. * **Per X Frames**: Samples the animation at given intervals determined by Frame Steps. * **Per Time Step**: Samples the animation at given intervals determined by Time Steps. |
| **Frame Start** | Starting index to start sampling the animation from. |
| **Frame End** | Ending index to stop sampling the animation at. |
| **Skip Empty Frames at Start of Alembic Sequence** | Skip empty (pre-roll) frames where there is no geometry and start importing at the frame which contains actual data. |

### Normal Calculation Options

![Alembic Normal Calculation options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/762b7918-d0c7-494a-9bea-f86c7095dd99/alembicnormalcalc.png "Alembic Normal Calculation options")

| Setting | Description |
| --- | --- |
| **Force One Smoothing Group Per Object** | Enable to force smooth normals for each individual object rather than calculating smoothing groups. |
| **Hard Edge Angle Threshold** | Threshold value that determines whether an angle between two normals should be considered hard (closer to 0 means more smooth). |
| **Recompute Normals** | Enable to force the recomputation of normals. |
| **Ignore Degenerate Triangles** | Enable to ignore degenerate triangles when calculating tangents and normals. |

##### How Normals are Calculated

The following is a high-level overview of how normals are calculated based on the **Import type** and how normals are used within the file to be imported.

* **When importing a file that contains normals for all frames:**
  + **For Static Meshes / Geometry Cache** : the engine uses existing normals.
  + **For Skeletal Meshes** : the normals from the first frame determine smoothing groups, which are used to calculate normals for the average frame and all the bases and morph-targets (we do this in all cases).
* **When importing a file that contains normals for only the first frames:**
  + **For Static Meshes** :If using frame 0, the engine uses existing normals. Otherwise it calculates smoothing groups and normals for the requested frame.
  + **For Geometry Cache** : the engine calculates smoothing groups and resulting normals for all frames.
* **When importing a file that contains no normals:**
  + The engine calculates non-smooth normals, generates smoothing groups according to the calculated normals and recalculates normals within the smoothing groups.

When enabling Recompute Normals, the path specified above is used (for no normals).

When importing as a **Skeletal Mesh**, if your animation has a large normal delta, you may run into issues getting correct-looking normals. This is a known issue caused by the way morph-targets can alter the face and vertex normals. As a workaround, you can bypass this problem by using the (experimental) skin cache feature.

You can enable this feature in your **Project Settings** using the **Support Compute Skincache** and **Force all skinned meshes to recompute tangents** options.

This should recompile shaders the next time you start the editor. When you open the Skeletal Mesh asset, you should be able to enable the **Recompute Tangent** option for each material or section.

##### How Smoothing Groups are Calculated

If you have hard edges on the meshes you import, you may want to look at the **Hard Edge Angle Threshold** and how smoothing group calculation is performed.

![1.0 Hard Edge Angle](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aab0abcd-107b-46ef-9065-7e3d172f9175/notsmooth.png)

![0.0 Hard Edge Angle](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/101912a5-a515-4cf4-86ad-a17d8e36154f/smooth.png)

To calculate Smoothing Groups, first, the vertex and face normals are calculated, which are then used to look at all the faces that connect to a particular face. By calculating the angle between the normals, we can then determine if an edge is hard or soft (similar to the Soft/Hard Edges tool in Maya). Below, the image on the left we would consider a soft edge, while the image on the right, a hard edge. This is because the angle between the two normals in the image on the left is smaller than that of the angle of the two normals in the image on the right.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b35b8529-039e-4535-b63e-b56d44227907/normalsexample.jpg)
