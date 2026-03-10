# Machine Learning Cloth Simulation Overview

> Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/machine-learning-cloth-simulation-overview

> Application Version: 5.7

## Introducing the Machine Learning Cloth Simulation System

[Video: V_u4gErl](https://dev.epicgames.com/community/api/cms/videos/V_u4gErl/embed.html)

The **Machine-Learning (ML) Cloth Simulation** system provides high-fidelity, highly performance, real-time cloth simulation in **Unreal Engine**.

The system provides higher fidelity than the traditional physics-based model by using a trained dataset that can be used in real-time to produce results that were previously only achievable with offline simulation.

### Benefits of Using Machine Learning

In traditional game development, you simulate character clothing by using a physics solver. However, this process can be computationally intensive due to the time-consuming updates for elasticity, and the complicated interactions between cloth and body.

A machine learning system can assist users in training a model using high-quality simulation data generated in advance. This system is capable of producing clothing meshes that are of similar quality to pre-simulated data, while being fast and efficient in terms of memory usage.

## Technical Implementation

[Video: V_74kS1l](https://dev.epicgames.com/community/api/cms/videos/V_74kS1l/embed.html)

For each frame, the ML Cloth Simulation system takes the character's skeletal pose as input and predicts a final cloth pose by deforming a base cloth mesh using linear blend skinning. The deformation has two major components.

The first component is a **low-frequency deformation** similar to the neural morph model.

This component is modeled with a multi-layer perceptron (MLP) network, which predicts a set of coefficients using the Skeletal Mesh pose as input. The low-frequency deltas are computed as:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "low_frequency_deltas = mean_delta + coeffs * basis",
  "lines_of_code": 1,
  "id": 55985,
  "url_signature": "eyJzbmlwcGV0X2lkIjo1NTk4NSwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIzOjA5KzAwOjAwIn0=--e2890f5085cb5e85be92f78160fcd3e8d9e0d7b5ab5c19b34d5515c283f4e7bb",
  "settings": {
    "is_hidden": false
  }
}
```

The basis can be learned at training time or pre-computed using principal component analysis (PCA).

To train this component, you should prepare a dataset of random poses and simulate clothing to settle on each pose. For this component, we recommend 5000 poses for a humanoid character.

The second component is a **high-frequency deformation** computed using the **Nearest Neighbor** search.

This component takes the coefficients from the first component and applies a nearest neighbor search in a Nearest Neighbor dataset, namely:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "high_frequency_deltas = NearestNeighborSearch(coeffs)",
  "lines_of_code": 1,
  "id": 55986,
  "url_signature": "eyJzbmlwcGV0X2lkIjo1NTk4NiwidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIzOjA5KzAwOjAwIn0=--6eb4d687fdb1a8ea81ed9f3708c00cf9f30632f583d55ee68354d8d07068824a",
  "settings": {
    "is_hidden": false
  }
}
```

For this component, one should prepare a small, but diverse set of poses and simulate clothing to settle on each of the poses. Ideally the poses should be taken from some key frames of the animations in-game. For optimal results, between 50 and 100 poses are recommended for a humanoid character.

Using this technique, the vertex delta is calculated as follows:

```json
{
  "type": "code_snippet",
  "description": "",
  "snippet_type": "cpp_programming",
  "title": "",
  "code_preview": "vertex_delta = low_frequency_deltas + high_frequency_deltas",
  "lines_of_code": 1,
  "id": 55987,
  "url_signature": "eyJzbmlwcGV0X2lkIjo1NTk4NywidXJsX2V4cGlyZXNfYXQiOiIyMDI2LTAzLTA5VDE4OjIzOjA5KzAwOjAwIn0=--4778e3180d559e08d74fd8e1bfd93da07d19807c2b02c78db399f025719fee6b",
  "settings": {
    "is_hidden": false
  }
}
```

For the trained dataset, you can generate the final cloth position for each pose by using the **Chaos Cloth Generator** tool under the **ML Deformer Editor** in Unreal Engine. This will simulate the cloth and generate a Geometry Cache that can be used in real-time.

Alternatively, you can use external cloth simulation solvers (such as Houdini Vellum). For each pose, simulate the cloth until settlement and save the settled cloth in the Geometry Cache. You can import the cache into Unreal Engine as an Alembic file.

```json
{
  "type": "callout",
  "callout_type": "note",
  "blocks": [
    {
      "type": "paragraph",
      "content": "Follow the <a href=\"https://dev.epicgames.com/community/learning/tutorials/PdRX/unreal-engine-ml-cloth-generation\">ML Cloth Generation tutorial</a> to learn how to generate the Geometry Cache inside Unreal Engine.",
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

For best results, you should manually choose the most relevant poses for the dataset. However, it is possible to do automatic pose selection with the **KMeans Pose Generator**. The generator takes an animation sequence and runs the KMeans algorithm to generate a list of entries for the Nearest Neighbor dataset.

### Current Limitations

The current system implementation has one main limitation — the clothing is assumed to be quasi-static. This means the system can predict shape details like wrinkles but cannot predict dynamic motion like swinging or draping.

This system is currently best suited for tight-fitting clothing like pants and T-shirts, but not loose garments like dresses or capes.

You can learn how to use the ML Cloth system by following the  [ML Deformer - Nearest Neighbor Model](https://dev.epicgames.com/community/learning/tutorials/pwaY/unreal-engine-nearest-neighbor-model-5-4) tutorial on the Epic Developer Community.
