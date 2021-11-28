import re
import numpy as np
import random

def count(n, m, Xp, x, y):
    uniqueId = random.randint(00000,99999)
    f = open("../test/result/"+str(uniqueId)+".txt", "w")
    for k in range(m):
        Yp = 0

        for i in range(n):
            p = 1

            for j in range(n):
                if i != j:
                    p *= (Xp[k]-x[j])/(x[i]-x[j])
            Yp += p * y[i]

        print("X = %.2f adalah %.3f\n" % (Xp[k], Yp))
        f = open("../test/result/"+str(uniqueId)+".txt", "a")
        f.write("X = %d adalah %.3f\n" % (Xp[k], Yp))
    print("Jawaban sudah disimpan dalam folder test/result/%s.txt" % str(uniqueId))