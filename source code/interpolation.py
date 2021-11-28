import re
import numpy as np
import random

def count(n, Xp, x, y):
    Yp = 0
    
    for i in range(n):
        p = 1
        
        for j in range(n):
            if i != j:
                p *= (Xp-x[j])/(x[i]-x[j])
        Yp += p * y[i]
    
    print("Prediksi Harga pada Tahun %d adalah %.3f" % (Xp, Yp))
    uniqueId = random.randint(00000,99999)
    f = open("../test/result/"+str(uniqueId)+".txt", "w")
    f.write("Prediksi Harga pada Tahun %d adalah %.3f" % (Xp, Yp))
    print("Jawaban sudah disimpan dalam folder test/result/%s.txt" % str(uniqueId))