import numpy as np

def count(n, m, augmented_matrix):
    # Gauss Jordan Elimination
    result = np.zeros(n)
    for i in range(n):
        if augmented_matrix[i][i] == 0.0: 
            sys.exit("Tidak ditemukan solusi")
        for j in range(n):
            if i != j:
                ratio = augmented_matrix[j][i] / augmented_matrix[i][i]

                for k in range(n+1):
                    augmented_matrix[j][k] = augmented_matrix[j][k] - ratio * augmented_matrix[i][k]


    # Obtaining
    for i in range(n):
        result[i] = augmented_matrix[i][n]/augmented_matrix[i][i]


    # Output Result
    print("Jadi, dari matriks tersebut didapatkan : ")
    for i in range(n):
        print("X%d = %.2f" % (i+1, result[i]))