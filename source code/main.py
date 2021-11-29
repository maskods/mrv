import os
import numpy as np
import gaussElimination as gaussEl
import interpolation as interpol

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def menu():
    print("[+]======= M E N U =======[+]")
    print("1. Sistem Persamaan Linier")
    print("2. Matriks Hilbert")
    print("3. Interpolasi")

def choiceMenu():
    clearConsole()
    print("[+]===== M E N U =====[+]")
    print("1. Input Melalui Console")
    print("2. Input Melalui File")
    
def matriksGaussEl():
    choiceMenu()
    choice = int(input("Pilih : "))
    
    if choice == 1 :
        n = int(input("Masukkan Banyaknya Variabel : "))
        m = int(input("Masukkan Banyaknya Persamaan : "))
        print("Masukkan Koefisien Persamaan : ")
        
        augmented_matrix = np.zeros((n, n), float)
        res_matrix = np.zeros(m, float)
        # Input with Console
        for i in range(m):
            temp = input()
            temp = temp.split()
            for j in range(n):
                augmented_matrix[i][j] = temp[j] 
            res_matrix[i] = temp[n]
    elif choice == 2:
        # Input with File
        file = input("Masukkan Nama File : ")
        lines = []
        with open("../test/"+file) as f:
            lines = f.readlines()
        n = len(lines[0].split())-1
        m = len(lines)
        
        augmented_matrix = np.zeros((n, n), float)
        res_matrix = np.zeros(m, float)

        for i in range(m):
            temp = lines[i].split() 
            for j in range(n):
                augmented_matrix[i][j] = temp[j]
            res_matrix[i] = temp[n]
    else: 
        print("Pilihan anda salah!")
        exit()
            
    
    gaussEl.count(n, m, augmented_matrix, res_matrix)
    

def matriksHilbert():
    clearConsole()
    n = int(input("Masukkan N : "))
    augmented_matrix = np.zeros((n, n))
    res_matrix = np.ones((n))
    
    for i in range(n):
        for j in range(n):
            augmented_matrix[i][j] = 1 / (i+j+1)
    gaussEl.count(n, n, augmented_matrix, res_matrix)

def inputInterpolasi():
    choiceMenu()
    choice = int(input("Pilih : "))
    
    if choice == 1 :
        n = int(input("Masukkan Banyaknya Data : "))
        x = np.zeros((n))
        y = np.zeros((n))
    
        print("Masukkan Data X Y : ")
        
        for i in range(n):
            temp = input()
            temp = temp.split()
            x[i] = temp[0]
            y[i] = temp[1]
            
    elif choice == 2:
        file = input("Masukkan Nama File : ")
        lines = []
        with open("../test/"+file) as f:
            lines = f.readlines()
        
        n = len(lines)
        x = np.zeros((n))
        y = np.zeros((n))
        for i in range(n):
            temp = lines[i].split()
            x[i] = temp[0]
            y[i] = temp[1]
            
    else: 
        print("Pilihan anda salah!")
        exit()
    m = int(input("Banyak data yang akan anda cari : "))
    Xp = np.empty(m)
    for i in range(m):
        Xp[i] = float(input("%d.Masukkan Data yang dicari : " % (i+1)))
        
    interpol.count(n, m, Xp, x, y)
    

# Main Program    
menu()
choice = int(input("Pilih Menu : "))

if(choice == 1):
    matriksGaussEl()
elif choice == 2:
    matriksHilbert()
elif(choice == 3):
    inputInterpolasi()
else:
    print("Menu yang anda masukkan salah!")