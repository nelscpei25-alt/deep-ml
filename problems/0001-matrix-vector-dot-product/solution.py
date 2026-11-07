import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	try:
		return np.array(a) @ np.array(b)
	except ValueError : 
		return -1