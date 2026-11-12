import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    # Write code here
    pos_emd = np.zeros((seq_len, d_model), dtype=float)
    pos = np.arange(seq_len)[:, np.newaxis]
    div_trm = np.exp(np.arange(0, d_model, 2) *  - (np.log(base) / d_model))

    pos_emd[:, 0::2] = np.sin(pos * div_trm)[:, :(d_model + 1) // 2]
    pos_emd[:, 1::2] = np.cos(pos * div_trm)[:, :d_model // 2]

    return pos_emd
    pass