
import numpy as np
import pandas as pd
import open3d as o3d
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

# === Load and prepare point cloud ===
# df = pd.read_csv('your_pointcloud.csv')  # Must have x, y, z
csv_path = "/home/fzhcis/Downloads/61-low_poly_tree/low_poly_tree/Lowpoly_tree_sample_30k.csv"  
df = pd.read_csv(csv_path)  # must contain 'x', 'y', 'z'
points = df[['x', 'y', 'z']].values

# Build Open3D point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

# Estimate normals (initial direction might be random)
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamKNN(knn=30))
normals = np.asarray(pcd.normals)

# === Build k-NN graph ===
k = 10
nbrs = NearestNeighbors(n_neighbors=k + 1).fit(points)
distances, indices = nbrs.kneighbors(points)

# Build sparse adjacency matrix for MST
rows, cols, data = [], [], []
for i, (d_row, i_row) in enumerate(zip(distances, indices)):
    for d, j in zip(d_row[1:], i_row[1:]):
        rows.append(i)
        cols.append(j)
        data.append(d)
adj_matrix = csr_matrix((data, (rows, cols)), shape=(len(points), len(points)))

# === Build MST ===
mst = minimum_spanning_tree(adj_matrix).tocoo()

# === Propagate normal orientations over MST ===
visited = set()
queue = []

# Start from root node (index 0)
visited.add(0)
queue.append(0)

while queue:
    current = queue.pop(0)
    for i, j in zip(mst.row, mst.col):
        if i == current and j not in visited:
            # Check alignment
            if np.dot(normals[i], normals[j]) < 0:
                normals[j] *= -1  # Flip
            visited.add(j)
            queue.append(j)
        elif j == current and i not in visited:
            if np.dot(normals[j], normals[i]) < 0:
                normals[i] *= -1
            visited.add(i)
            queue.append(i)

# Update normals in Open3D object
pcd.normals = o3d.utility.Vector3dVector(normals)

# === Visualize ===
o3d.visualization.draw_geometries([pcd], point_show_normal=True)
