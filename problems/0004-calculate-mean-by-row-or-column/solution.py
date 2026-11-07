import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = 0
	a = np.array(matrix)
	if mode == 'column':
		means = np.mean(a, axis = 0)
	else:
		means = np.mean(a, axis = 1)
	return means