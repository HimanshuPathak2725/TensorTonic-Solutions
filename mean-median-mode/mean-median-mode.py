from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    mean = float(np.mean(x))
    
    x = np.sort(x)
    middle = len(x) // 2
    
    if len(x) % 2 == 0:
        median = float((x[middle - 1] + x[middle]) / 2)
    else: median = float(x[middle])

    l = 0
    r = 0
    maxi = 0
    mode = None
    while r < len(x):
        
        while r < len(x) and x[l] == x[r]:
            r += 1

        curr_count = r - l
        if curr_count > maxi:
            maxi = curr_count
            mode = float(x[l])

        l = r

    return {"mean": mean, "median": median, "mode": float(mode)}
    pass