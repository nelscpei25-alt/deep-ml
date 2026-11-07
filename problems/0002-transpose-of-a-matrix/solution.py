import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    ans = np.array(a)
    return np.transpose(ans)