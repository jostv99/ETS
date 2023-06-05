import math
from statistics import mean
import time
import matplotlib.pyplot as plt
from functools import cache
# vhod: a,b,c,   b > 0 nekv.
# izhod: alfa = (a + sqrt(b))/c
# perioda? oznaci jo
#za katera d >0 izracuna program u zglednem casu rezultat?
@cache
def verizni_ulomek(a, b, c):
    start = time.time_ns()
    preveri = math.sqrt(b)
    if preveri.is_integer():
        return [0], 0
    alfa0 = (a + preveri) / c
    a0 = math.floor(alfa0)
    izracunani_aji = [a0]
    alfai = alfa0
    ai = a0
    D = b * (c ** 2) # koren D
    korenD = math.sqrt(D)
    P0 = a * abs(c)
    Q0 = c * abs(c)
    pari = [(P0, Q0)]
    Pi, Qi = P0, Q0
    while True:
        Pi = int(-Pi + ai * Qi)
        Qi = int((D - Pi**2) / Qi)
        alfai = (Pi + korenD) / Qi   # hitrejs?
        ai = math.floor(alfai)
        if (Pi, Qi) in pari:
            break
        pari.append((Pi, Qi))
        izracunani_aji.append(ai)

    konec = time.time_ns()
    cas = konec - start
    # print(konec - start)
    # print(f"sqrt({b})")
    # print(izracunani_aji)
    return (izracunani_aji, cas)


x = []
rez = []
casi = []
for i in range(1, 10000):
    (sez, cas) = verizni_ulomek(0,i,1)
    x.append(i)
    dolzina = len(sez)
    rez.append(dolzina)
    casi.append(cas) #nano

# print(verizni_ulomek(0,7 + 10**10,1))

print(mean(casi))
# print(x, rez)
plt.scatter(x, rez, s=0.5)
plt.plot(x,[2 * math.sqrt(t) for t in x],"-r", markersize=0.5)
plt.show()