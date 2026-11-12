import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    a_din = np.linalg.norm(a)
    b_din = np.linalg.norm(b)
    if a_din == 0 or b_din == 0:
        return 0.0
    else: return float((a @ b) / (a_din * b_din))
    pass