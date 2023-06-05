import numpy as np
import math
from verizni_ulomki import verizni_ulomek
import matplotlib.pyplot as plt
# d = (a + sqrt(b))/c

def konvergent_k(veriga, k, stevec, M0, M1, original_veriga):
    if stevec == k:
        p, q = M0[0][0], M0[0][1]
        return p, q
    else:
        if veriga == []:
            veriga = original_veriga
        M1 = np.array([[veriga[0], 1],
                       [1,         0]], dtype=object)
        M0 = np.matmul(M1, M0)
        return konvergent_k(veriga[1:], k, stevec+1, M0, M1, original_veriga)

def pell_za_d(d):
    veriga= verizni_ulomek(0, d, 1)  # verizni_ulomek(0, 2, 1) = [1, 2]  
    # print(veriga)
    if veriga is None:
        return d, (0, 0)
    else:
        n = len(veriga) - 1
        M0 = np.array([[veriga[0], 1],
                       [1,         0]], dtype=object)
        M1 = np.eye(2, dtype=object)
        match n % 2:
            case 0:
                return d, konvergent_k(veriga[1:], n, 1, M0, M1, veriga[1:])
            case 1:
                return d, konvergent_k(veriga[1:], 2*n, 1, M0, M1, veriga[1:])

resitve = []  # (d, (x, y))
velikosti_resitev = []
def absolutna(v):
    x, y = v
    return math.sqrt(x**2 + y**2)

for i in range(6000):
    d, r = pell_za_d(i)
    print(d, r)
    velikost = absolutna(r)
    velikosti_resitev.append(velikost)

def potenciranje_resitve(resitev, k, d):
    match k:
        case 1:
            return resitev
        case _:
            u, v = resitev
            if k % 2 == 0:
                u1 = u ** 2 + d * (v ** 2)
                v1 = 2 * u * v
                return potenciranje_resitve((u1, v1), k // 2, d)
            else:
                u, v = resitev
                u1, v1 = potenciranje_resitve(resitev, k - 1, d)
                return (u * u1 + 2 * v * v1, u * v1 + v * u1)
            
print(potenciranje_resitve((3, 2), 2, 2))
print(potenciranje_resitve((3, 2), 3, 2))


plt.plot([i for i in range(len(velikosti_resitev))], velikosti_resitev)
plt.show()
    

