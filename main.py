import re
import numpy as np
import gaussElimination as gaussEl
import gaussJordan as gaussJor

def menu():
    print("======= M E N U =======")
    print("1. Sistem Persamaan Linier (Gauss Elimination)")
    print("2. Sistem Persamaan Linier (Gauss Jordan)")
    print("3. Interpolasi")
    
def matriksGaussEl():
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
    
    gaussEl.count(n, m, augmented_matrix, res_matrix)
    

def matriksGaussJor():
    n = int(input("Masukkan Banyaknya Variabel : "))
    m = int(input("Masukkan Banyaknya Persamaan : "))

    augmented_matrix = np.zeros((n, n+1))
    result = np.zeros(n)

    print("Masukkan Koefisien Persamaan : ")

    # Input with Console
    for i in range(m):
        temp = input()
        temp = temp.split()
        for j in range(n+1):
            augmented_matrix[i][j] = temp[j]
    gaussJor.count(n, m, augmented_matrix)
    
def inputInterpolasi():
    print("inputInterpolasi")
    
menu()
choice = int(input("Pilih Menu : "))

if(choice == 1):
    matriksGaussEl()
elif(choice == 2):
    matriksGaussJor()
elif(choice == 3):
    inputInterpolasi()
else:
    print("Menu yang anda masukkan salah!")