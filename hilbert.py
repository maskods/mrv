import re
import numpy as np
import sys

n = int(input("Masukkan N : "))
augmented_matrix = np.zeros((n, n+1))
result = np.ones((n, 1))

for i in range(n):
    for j in range(n):
        augmented_matrix[i][j] = 1 / (i+j+1)
    augmented_matrix[i][n] = 1
for i in range(n):
    for j in range(n+1):
        print(augmented_matrix[i][j], end=" ")
    print("")
