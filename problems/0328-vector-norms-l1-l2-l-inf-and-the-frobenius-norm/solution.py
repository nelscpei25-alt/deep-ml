import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    if norm_type == 'l1':
        ans = np.linalg.norm(arr.ravel(), ord = 1)
        return ans
    elif norm_type == 'l2':
        ans = np.linalg.norm(arr.ravel(), ord = 2)
        return ans
    elif norm_type == 'linf':
        ans = np.linalg.norm(arr.ravel(), ord = np.inf)
        return ans
    elif norm_type == 'frobenius':
        ans = np.linalg.norm(arr, 'fro')
        return ans
    else:
        return ValueError