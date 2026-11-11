import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A = np.asarray(A, dtype=float)
    rows, cols = A.shape
    result = np.empty((cols, rows), dtype=float)

    for i in range(rows):
        for j in range(cols):
            result[j][i] = A[i][j]

    return result
