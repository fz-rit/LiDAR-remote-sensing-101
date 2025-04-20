import open3d as o3d
import pandas as pd
csv_path = "/home/fzhcis/Downloads/61-low_poly_tree/low_poly_tree/Lowpoly_tree_sample_30k.csv"  

df = pd.read_csv(csv_path)

# Extract XYZ and RGB as numpy arrays
xyz = df[['x', 'y', 'z']].values
rgb = df[['r', 'g', 'b']].values / 255.0  # Normalize to [0,1] for Open3D

# Create Open3D point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(xyz)
pcd.colors = o3d.utility.Vector3dVector(rgb)
# Estimate normals
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamKNN(knn=30))

# (Optional) Orient normals consistently (toward camera or outward)
pcd.orient_normals_consistent_tangent_plane(k=30)

# Visualize
o3d.visualization.draw_geometries([pcd], point_show_normal=True)


# Write the point cloud with normals to a new .csv file using pandas
output_csv_path = "/home/fzhcis/Downloads/61-low_poly_tree/low_poly_tree/Lowpoly_tree_sample_30k_with_normals.csv"
normals = o3d.utility.Vector3dVector(pcd.normals)
normals_df = pd.DataFrame(normals, columns=['nx', 'ny', 'nz'])
# Combine with original data
output_df = pd.DataFrame(xyz, columns=['x', 'y', 'z'])
output_df['r'] = df['r']
output_df['g'] = df['g']
output_df['b'] = df['b']
output_df['nx'] = normals_df['nx']
output_df['ny'] = normals_df['ny']
output_df['nz'] = normals_df['nz']
# Save to CSV
output_df.to_csv(output_csv_path, index=False)
print(f"Point cloud with normals saved to {output_csv_path}")
# Read the saved CSV to verify
df_with_normals = pd.read_csv(output_csv_path)
print(df_with_normals.head())
