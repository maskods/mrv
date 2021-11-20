from numpy import matrix, linalg
import numpy as np
matrix_A = np.array([[1, 7, -2, 0, 8],[1, 7, -1, 1, 0],[2, 14, -4, 1, -13], [2, 14, -4, 0, 16]])
print('matrix_A')
print(matrix_A)
matrix_B = np.array([[-3],[2],[3],[-6]])
print('matrix_B')
print(matrix_B)
print("Knowing that 'A * A_inv = I', the solution comes down to 'S = A_inv * B'")
matrix_A_inv = linalg.inv(matrix_A)
print(matrix_A_inv)
matrix_S = np.matmul(matrix_A_inv, matrix_B)
print('matrix_S')
print(matrix_S)