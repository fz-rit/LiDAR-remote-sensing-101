import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.neighbors import KDTree, BallTree
from scipy.spatial import cKDTree
from typing import Callable, Dict, Tuple, List

try:
    import open3d as o3d
    has_open3d = True
except ImportError:
    has_open3d = False


def brute_force_nn(data: np.ndarray, queries: np.ndarray, k: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Perform brute-force nearest neighbor search.

    Parameters:
        data (np.ndarray): Reference point cloud of shape (N, 3).
        queries (np.ndarray): Query points of shape (M, 3).
        k (int): Number of nearest neighbors.

    Returns:
        Tuple of indices and distances arrays, both of shape (M, k).
    """
    dists = np.linalg.norm(data[None, :, :] - queries[:, None, :], axis=2)
    idxs = np.argsort(dists, axis=1)[:, :k]
    return idxs, np.take_along_axis(dists, idxs, axis=1)


def octree_nn(data: np.ndarray, queries: np.ndarray, k: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Approximate nearest neighbor using Open3D's Octree (if available).

    Note: Open3D's octree does not support efficient k-NN out-of-the-box.
    This is a placeholder for educational purposes.
    """
    if not has_open3d:
        raise ImportError("Open3D is not installed.")

    # Convert to Open3D point cloud
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(data)
    octree = o3d.geometry.Octree(max_depth=8)
    octree.convert_from_point_cloud(pcd, size_expand=0.01)

    # Naively use brute force for actual querying, just to show structure
    return brute_force_nn(data, queries, k)


def run_benchmark(methods: Dict[str, Callable], 
                  data: np.ndarray, 
                  query_sizes: List[int], 
                  k: int = 20) -> Dict[str, List[float]]:
    """
    Run benchmarking for each nearest neighbor method over various query sizes.

    Parameters:
        methods (Dict): Dictionary mapping method names to functions.
        data (np.ndarray): Point cloud data.
        query_sizes (List[int]): List of query sizes to benchmark.
        k (int): Number of neighbors.

    Returns:
        Dictionary of timing results per method.
    """
    timing_results = {m: [] for m in methods}

    for n_query in query_sizes:
        queries = np.random.rand(n_query, 3)
        for name, method in methods.items():
            start = time.time()
            _ = method(data, queries, k)
            elapsed = time.time() - start
            timing_results[name].append(elapsed)
            print(f"{name:12s} | Queries: {n_query:6d} | Time: {elapsed:.4f} s")

    return timing_results


def plot_results(timing_results: Dict[str, List[float]], query_sizes: List[int]) -> None:
    """
    Plot benchmark results.

    Parameters:
        timing_results (Dict): Runtime per method per query size.
        query_sizes (List[int]): Query sizes used.
    """
    plt.figure(figsize=(12, 6))
    for name, times in timing_results.items():
        plt.plot(query_sizes, times, label=name, marker='o')

    plt.xlabel("Number of Query Points")
    plt.ylabel("Time (seconds)")
    plt.title("Nearest Neighbor Search Time vs. Query Size")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.xscale('log')
    plt.show()


def main():
    # Setup: generate random 3D point cloud
    num_points = 100_000
    data = np.random.rand(num_points, 3)

    # Varying query sizes
    query_sizes = np.concatenate([
        np.linspace(1, 100, 20).astype(int),
        np.linspace(100, 1000, 20).astype(int)
    ])

    k = 20  # Number of neighbors to query

    # Register NN methods
    methods: Dict[str, Callable] = {
        "Brute Force": brute_force_nn,
        "KDTree": lambda d, q, k: KDTree(d).query(q, k=k),
        "Ball Tree": lambda d, q, k: BallTree(d).query(q, k=k),
        "cKDTree": lambda d, q, k: cKDTree(d).query(q, k=k)
    }

    if has_open3d:
        methods["Octree (naive)"] = octree_nn

    # Run and plot
    timing_results = run_benchmark(methods, data, query_sizes, k)
    plot_results(timing_results, query_sizes)


if __name__ == "__main__":
    main()
