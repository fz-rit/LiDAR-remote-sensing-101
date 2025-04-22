import numpy as np
from get_nn_distances import get_distances

def sor_filter(points: np.ndarray,
                nb_neighbors: int = 20, 
                std_ratio: float = 2.0) -> np.ndarray:
    """
    Apply Statistical Outlier Removal (SOR) using a full distance matrix.

    Args:
        points: Input point cloud of shape (N, 3).
        dist_matrix: Precomputed (N, N) distance matrix.
        nb_neighbors: Number of nearest neighbors to average.
        std_ratio: Threshold multiplier for outlier removal.

    Returns:
        np.ndarray: Filtered inlier points of shape (M, 3), where M <= N.
    """
    dist_matrix = get_distances(points, use_kdtree=False) # shape (N, N)
    sorted_dists = np.sort(dist_matrix, axis=1)
    mean_knn_dists = np.mean(sorted_dists[:, 1:nb_neighbors+1], axis=1)
    
    mean = np.mean(mean_knn_dists)
    std = np.std(mean_knn_dists)
    threshold = mean + std_ratio * std

    mask = mean_knn_dists < threshold
    return points[mask]


def ror_filter(points: np.ndarray, 
                radius: float = 0.5,
                min_neighbors: int = 5) -> np.ndarray:
    """
    Apply Radius Outlier Removal (ROR) using a full distance matrix.

    Args:
        points: Input point cloud of shape (N, 3).
        dist_matrix: Precomputed (N, N) distance matrix.
        radius: Radius threshold to consider a neighbor.
        min_neighbors: Minimum number of neighbors required.

    Returns:
        np.ndarray: Filtered inlier points of shape (M, 3), where M <= N.
    """
    dist_matrix = get_distances(points, use_kdtree=False) # shape (N, N)
    within_radius = dist_matrix < radius
    np.fill_diagonal(within_radius, False)

    neighbor_counts = np.sum(within_radius, axis=1)
    mask = neighbor_counts >= min_neighbors
    return points[mask]


# Example usage
if __name__ == "__main__":
    # Simulate noisy point cloud
    np.random.seed(0)
    core = np.random.randn(1000, 3)
    outliers = np.random.uniform(low=-10, high=10, size=(50, 3))
    points = np.vstack((core, outliers))

    
    print("Before filtering:", points.shape)
    filtered_points = sor_filter(points, std_ratio=2.0)
    # filtered_points = ror_filter(points, radius=0.5, min_neighbors=5)
    print("After filtering:", filtered_points.shape)
