# functie voor het negatief maken van een array
def negatief(array):
    a = array * -1
    return a
# importeer benodigde packages
import numpy as np
# bepaal hoogste getal in een random x by y matrix
def hoogste_random(dim1, dim2):
    # np.random.random geeft een array terug met random float getallen tussen 0.0 en 1.0
    a = np.random.random((dim1, dim2))
    b = a[0,0]
    # om te controleren of je script correct is:
    c = np.max(a)
    for x in range(0,dim1):
        for y in range (0, dim2):
            d = a[x,y]
            if d > b:
                b = d
    return b,c