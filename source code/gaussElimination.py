import numpy as np
import random

def count(n, m, augmented_matrix, res_matrix):
    # Gauss Elimination
    np.set_printoptions(suppress=True)
    result = np.zeros((m, n+1), float)
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

    for i in range(1, n):
        if augmented_matrix[i][i] == 1 and augmented_matrix[i-1][i] != 0:
            for l in range (i):
                    temp = augmented_matrix[i-l-1][i]
                    for k in range(l, n):
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
    
    for i in range(m):
        for j in range(n):
            result[i][j] = "{:.2f}".format(augmented_matrix[i][j])
        result[i][n] = "{:.2f}".format(res_matrix[i])
    print(result)
    print("Jadi, dari matriks tersebut didapatkan : ")
    for i in range(m):
        for j in range(n):
            if result[i][j] == 1.0:
                print("X%d = %.2f" % (j+1, result[i][n]), end=" ")
                for k in range(j+1, n):
                    if result[i][k] == 0: continue
                    result[i][k] *= -1
                    if result[i][k] < 0 and k != j: print("-", end=" ")
                    else: print("+", end=" ")
                    print("%.2fX%d" % (abs(result[i][k]), k+1), end=" ")
                print("")
    
    uniqueId = random.randint(00000,99999)
    f = open("../test/result/"+str(uniqueId)+".txt", "w")
    for i in range(m):
        tempPers = ""
        for j in range(n):
            if result[i][j] == 1.0:
                tempPers = "X" + str(j+1) + " = " + str(result[i][n]) + " "
                for k in range(j+1, n):
                    if result[i][k] == 0: continue
                    result[i][k] *= -1
                    if result[i][k] < 0 and k != j: tempPers += "- "
                    else: tempPers += "+ "
                    tempPers += str(abs(result[i][k])) + "X" + str(k+1)
                tempPers += "\n"
                f = open("../test/result/"+str(uniqueId)+".txt", "a")
                f.write(tempPers)
                f.close()
    print("Jawaban sudah disimpan dalam folder test/result/" + str(uniqueId) + ".txt") 
                
            



    