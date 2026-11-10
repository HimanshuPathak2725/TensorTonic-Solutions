import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    N, D = X.shape
    w = np.zeros(D)
    b = 0.0
    for _ in range(steps):
        pred = _sigmoid(X @ w + b)
        pred_w = X.T @ (pred - y) / N
        pred_b = np.mean(pred - y)
        w -= lr*pred_w
        b -= lr*pred_b
    return w, b