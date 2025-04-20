import numpy as np
import open3d as o3d

def visualize_octree(depth: int = 4, num_points: int = 1000):
    """
    Visualizes a point cloud with its octree structure in Open3D.

    Parameters:
        depth (int): Maximum depth of the octree.
        num_points (int): Number of random points in the point cloud.
    """
    # Generate random 3D points
    np.random.seed(42)
    points = np.random.rand(num_points, 3)

    # Create Open3D point cloud object
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)

    # Build the octree from point cloud
    octree = o3d.geometry.Octree(max_depth=depth)
    octree.convert_from_point_cloud(pcd, size_expand=0.01)

    # Visualize both point cloud and octree together
    print(f"Visualizing {num_points} points with octree of depth {depth}")
    o3d.visualization.draw_geometries([pcd, octree])

if __name__ == "__main__":
    visualize_octree(depth=2, num_points=2000)
