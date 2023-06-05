from functools import cache
import matplotlib.pyplot as plt
import numpy as np
import time
@cache
def catalanovo(n, korak=0):
    pregledani = set()
    if n in pregledani:
        return -1
    if n not in pregledani:
        pregledani.add(n)
    if n == 1:
        return korak
    if n % 2 == 0:
        return catalanovo(n/2, korak + 1)
    else:
        return catalanovo((3*n+1)/2, korak + 1)
        
tocke = {}
casi = {}
stevilo_korakov = 1000

for i in range(1, stevilo_korakov):
    start = time.time()
    vrednost = catalanovo(i)
    if vrednost == -1:
        print("nemogoce model")
    tocke[i] = vrednost
    print(i, vrednost)
    end = time.time()
    casi[i] = end - start
cas_povprecje = sum(casi.values()) / stevilo_korakov
print(cas_povprecje)

fig, ax = plt.subplots()
x = casi.keys()
y = casi.values()

ax.scatter(x, y, s=0.5)

ax.set(xlim=(0, len(x)), xticks=[i* 10 for i in range(len(x)//10)],
       ylim=(0, max(y)), yticks=np.arange(1, max(y)))
fig.autofmt_xdate()

# fig1, ax1 = plt.subplots()
# x1 = casi.keys()
# y1 = casi.values()

# ax1.lines(x1, y1, s=0.5)

# ax1.set(xlim=(0, len(x1)), xticks=[i* 10 for i in range(len(x1)//10)],
#        ylim=(0, max(y1)), yticks=np.arange(1, max(y1)))
# fig1.autofmt_xdate()

plt.show()
