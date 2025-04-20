import open3d as o3d
import numpy as np
import pandas as pd
from pathlib import Path
# === Step 1: Load the mesh file ===
# Use the .obj file for simplicity (it is widely supported and likely includes materials)
file_dir = Path("/home/fzhcis/Downloads/61-low_poly_tree/low_poly_tree")
num_of_points = 3000
# Load mesh with vertex color
mesh = o3d.io.read_triangle_mesh("Lowpoly_tree_sample.ply")
mesh.compute_vertex_normals()

# Sample to point cloud
pcd = mesh.sample_points_uniformly(number_of_points=num_of_points)

# Save as CSV (x, y, z, r, g, b)
points = np.asarray(pcd.points)
colors = (np.asarray(pcd.colors) * 255).astype(np.uint8)
df = pd.DataFrame(np.hstack((points, colors)), columns=["x", "y", "z", "r", "g", "b"])

# === Step 4: Save to CSV ===
df.to_csv(file_dir / f"Lowpoly_tree_sample_{num_of_points/1000:d}k.csv", index=False)
print("Point cloud saved to pointcloud.csv")

# === Step 5: Visualize the point cloud ===
o3d.visualization.draw_geometries([pcd])


