import numpy as np
from typing import Optional

try:
    from scipy.spatial import KDTree
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False


def get_distances(points: np.ndarray, use_kdtree: bool = True) -> np.ndarray:
    """
    Compute the pairwise Euclidean distance matrix for a set of 3D points.

    If use_kdtree=True and scipy is available, uses KDTree for efficient neighbor queries.
    Otherwise, falls back to brute-force pairwise distance calculation.

    Args:
        points (np.ndarray): Array of shape (N, 3), where N is the number of points.
        use_kdtree (bool): Whether to use KDTree for efficient distance computation.

    Returns:
        np.ndarray: Distance matrix of shape (N, N), where each element [i, j] is
                    the Euclidean distance between point i and point j.
    """
    N = len(points)
    if N == 0:
        return np.array([[]])

    if use_kdtree and SCIPY_AVAILABLE:
        tree = KDTree(points)
        # Preallocate matrix
        dists = np.zeros((N, N), dtype=np.float32)
        for i in range(N):
            dists[i, :] = tree.query(points[i], k=N)[0]  # returns (dists, indices)
        return dists

    else:
        # Brute-force pairwise distances
        diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
        dists = np.linalg.norm(diff, axis=2)
        return dists
