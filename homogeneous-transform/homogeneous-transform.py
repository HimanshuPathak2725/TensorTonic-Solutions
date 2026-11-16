import numpy as np

def apply_homogeneous_transform(T: list, points: list) -> np.ndarray:
    """
    Returns transformed points with shape (3,) or (N, 3).
    """
    # Write code here
    points = np.asarray(points, dtype=float)
    T = np.asarray(T, dtype=float)
    if points.ndim == 1:
        points_h = np.append(points.reshape(1, 3), 1)
        
    if points.ndim == 2:
        points_h = np.hstack([points, np.ones((points.shape[0], 1))])
    result = points_h@T.T

    return result[..., :3]
    pass