import re
import numpy as np

n = int(input("Masukkan Banyaknya Variabel : "))
m = int(input("Masukkan Banyaknya Persamaan : "))

augmented_matrix = np.zeros((n, n))
res_matrix = np.zeros(n)
result = np.zeros(n)

print("Masukkan Koefisien Persamaan : ")

for i in range(m):
    temp = input()
    temp = temp.split()
    for j in range(n):
        augmented_matrix[i][j] = temp[j] 
    res_matrix[i] = temp[n]

# Gauss Elimination
for k in range(n):
    if np.fabs(augmented_matrix[k,k]) < 1.0e-12:
        for i in range(k+1, n):
            if np.fabs(augmented_matrix[i,k]) > np.fabs(augmented_matrix[k,k]):
                augmented_matrix[[k,i]] = augmented_matrix[[i,k]]
                res_matrix[[k,i]] = res_matrix[[i,k]]
                break
    
    for i in range(k+1, n):
        if augmented_matrix[i,k] == 0: continue
        factor = augmented_matrix[k,k] / augmented_matrix[i,k]
        for j in range(k,n):
            augmented_matrix[i,j] = augmented_matrix[k,j] - augmented_matrix[i,j] * factor
        res_matrix[i] = res_matrix[k] - res_matrix[i] * factor
    
for i in range(n):
    if augmented_matrix[i][i] == 1: continue
    for j in range(i, n):
        if augmented_matrix[i][j] != 0:
            temp = augmented_matrix[i][j]
            for k in range(j, n):
                augmented_matrix[i][k] /= temp
            res_matrix[i] /= temp
            break
print(augmented_matrix)
for i in range(1, n):
    if augmented_matrix[i][i] == 1 and augmented_matrix[i-1][i] != 0:
        for l in range (i):
                temp = augmented_matrix[i-l-1][j]
                for k in range(j, n):
                    augmented_matrix[i-l-1][k] -= temp * augmented_matrix[i][k]
                res_matrix[i-l-1] -= temp * res_matrix[i]
    else:
        for j in range(i, n):
            if augmented_matrix[i][j] != 0:    
                for l in range (i):
                    temp = augmented_matrix[i-l-1][j]
                    for k in range(j, n):
                        augmented_matrix[i-l-1][k] -= temp * augmented_matrix[i][k]
                    res_matrix[i-l-1] -= temp * res_matrix[i]
                break
            
            
print(augmented_matrix)
print(res_matrix)
                


 