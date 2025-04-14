# LiDAR-session
Materials for preparing the LiDAR session.


## Outline (V0.1)
**Advancing LiDAR in Remote Sensing: From Traditional Methods to Deep Learning**

- **1. Introduction to LiDAR and Remote Sensing (10–15 min)**
  - Basic principles of LiDAR (How it works, data acquisition)
  - Importance in Remote Sensing (Forestry, Precision Agriculture)
  - Intuitive visuals and application examples

- **2. Traditional Point Cloud Techniques (20–25 min)**
    - **1. Preprocessing and Filtering**
        - **Noise Filtering**
            - Statistical Outlier Removal (SOR)
            - Radius Outlier Removal (ROR)
        - **Ground Filtering and DTM Generation**
            - Progressive TIN densification
            - Cloth Simulation Filter (CSF) (brief mention)

    - **2. Feature Extraction & Structural Analysis**
        - **Surface Normal Estimation (PCA-based)**
            - Intuition and applications (terrain, object identification)
        - **Edge and Feature Detection**
            - Curvature-based methods (simple explanation)
        - **RANSAC-based Shape Detection**
            - Plane, sphere, and cylinder fitting
        - Practical demonstration (CloudCompare quick example)

    - **3. Classification and Segmentation (non-DL methods)**
        - **Voxelization-based Approaches**
            - Concept and brief example use-cases
        - **Region-Growing Approaches**
            - Region-growing segmentation algorithms (simple overview)
            - When and why these methods are effective

    - **4. Point Cloud Registration & Alignment**
        - **Iterative Closest Point (ICP)**
            - Intuition and basic algorithm steps (brief)
        - **Feature-based Registration**
            - Correspondence finding via geometric features (brief mention)

    - **5. Spatial Data Structures for Efficiency**
        - **KD-Trees**
            - Quick intuitive explanation of nearest-neighbor search and indexing
        - **Octrees**
            - Hierarchical spatial indexing concept (very brief mention)

- **3. Deep Learning for LiDAR (30-45 min)**
    - **1. Motivation: Why Deep Learning?** (5 min)
        - Limitations of traditional methods
        - Potential advantages of DL for complex data

    - **2. Early DL Methods on Point Clouds: Historical Context** (5–7 min)
        - **Initial attempts: Voxel-based methods**  
            *(~2015)*  
            - Conversion to regular grids (VoxNet)
            - Benefits and limitations (high memory, limited resolution)
        - **Multi-view methods**  
            *(~2016)*  
            - Projecting point clouds to multiple 2D views (MVCNN)
            - Advantages (leveraging mature CNN architectures)
            - Limitations (loss of geometric detail, computational inefficiency)
        - **Emergence of point-based methods**  
            *(~2017-present)*  
            - Motivation: directly operating on unordered points
            - PointNet (Qi et al., CVPR 2017), PointNet++ (Qi et al., NeurIPS 2017)
            - Briefly: later developments like graph-based and sparse CNN methods

    - **3. Core Architectures: PointNet & PointNet++** (15–20 min)
        - PointNet: permutation invariance, basic structure
        - PointNet++: improved local structure capture (hierarchical features)

    - **4. Practical Considerations** (5–10 min)
        - Data preparation, common evaluation metrics, computational issues

- **4. Explainability in Deep Learning (10–15 min)**
  - Why explainability matters (trust, decision-making)
  - Simple examples of explainable visualization methods
  - Relevance to remote sensing professionals

- **5. Summary & Future Directions (5–10 min)**
  - Quick recap of key ideas
  - Brief discussion of open challenges and emerging trends
  - Final thoughts and Q&A


## Outline (V0.2)
---

### 1\. Introduction to LiDAR and Remote Sensing (8–10 min)
- **Keep:**  
  - Basic LiDAR principles (concise explanation)  
  - Importance in remote sensing (brief examples)

- **Remove/Reduce:**  
  - Limit examples to just 1-2 quick, intuitive visuals.

---

### 2\. Traditional Point Cloud Techniques (18–20 min)
- **1. Preprocessing and Filtering** *(briefly combined into one slide)*  
  - Quickly mention Noise filtering (just conceptually, no algorithm details).  
  - Brief mention of Ground Filtering (remove detailed methods).

- **2. Feature Extraction & Structural Analysis** *(main focus of this section)*  
  - PCA & Surface Normals (key visuals, intuitive explanation)  
  - RANSAC Shape Detection (keep demonstration, but short and intuitive)  
  - **Remove:** detailed Edge and Curvature explanations (or reduce significantly)

- **3. Classification and Segmentation (non-DL)** *(significantly shorten or remove completely)*  
  - Quickly mention Region-growing only in passing (1 minute, or remove altogether).
  - **Remove voxelization entirely (covered briefly later in DL)**.

- **4. Point Cloud Registration** *(reduce drastically)*  
  - Just briefly mention ICP in a single slide (no details, just intuition).  
  - Remove "feature-based registration."

- **5. Spatial Data Structures** *(significantly reduce)*  
  - Only briefly mention KD-tree in 1 min or less.  
  - Completely remove Octrees.

---

### 3\. Deep Learning for LiDAR (30–35 min, main emphasis)
- **1. Motivation: Why DL?** (3–4 min) *(keep short and intuitive)*

- **2. Historical Context** *(brief, 5 min total)*  
  - Voxel methods (mention briefly, 1-2 slides max)  
  - Multi-view methods (very quick mention, 1 slide max)  
  - Emergence of PointNet-based methods (smooth transition to next point)

- **3. Core DL Architectures (PointNet & PointNet++)** (15–18 min, your main focus)  
  - PointNet: intuitive visuals/examples  
  - PointNet++: intuition and quick examples, no deep technicalities

- **4. Practical Considerations** (3–4 min, brief overview only)  
  - Quickly summarize main practical issues: data prep, metrics.

---

### 4\. Explainability in DL (5–7 min, reduced significantly)
- Just briefly introduce concept (importance, intuitive visualization examples)  
- Limit to 2-3 slides total; no in-depth methods or frameworks.

---

### 5\. Summary & Future Directions + Quick Q&A (5 min)
- Very brief summary slide highlighting the talk’s main points  
- Mention future directions in a single slide quickly  
- Short Q&A (if possible, or invite informal follow-up discussion afterward)

---

## **Timing (75 min total):**

| Section                                              | Time           |
|------------------------------------------------------|----------------|
| 1\. Introduction                                     | **8–10 min**   |
| 2\. Traditional Techniques                           | **18–20 min**  |
| 3\. Deep Learning                                    | **30–35 min**  |
| 4\. Explainability                                   | **5–7 min**    |
| 5\. Summary & Quick Q&A                              | **5 min**      |
| **Total**                                            | **75 min**     |

---
