#funkcja realizujaca rozwiazanie zadania
import random
import math
import pandas
from points import*
from fun import*


#inicjalizacja zmiennych algorytmu
zad = 1 #1 - podpunkt a, 0 -podpunkt b
mi = 20 #wielkosc popoluacji P
lambda2 = 7*mi  #wielkosc populacji T
loci = 28 #liczba loci
prawd = 0.1 #pradopodobienkstwo mutacji genu
n = 10 # ilosc genow na reprezentacje pojedynczego x,y lub r
N = 30 #ilosc punktow
k = 0
old_best = [0,0,0,0]

#generacja punktow
tab = rand_points(N)
#generacja poczatkowej populacji P
pop_p = generate_p(mi,n)

#glowna petla programu
for i in range(200):
    if k == 25:
        break
    pop_t = generate_t(lambda2,pop_p,mi)#generacja populacji T
    pop_o = create_o(pop_t,n,lambda2)#zmiana populacji T na genotypy
    pop_o1 = cross_o(pop_o,n,lambda2,loci)#krzyzowanie populacji
    pop_o2 = x_men(pop_o1,n,lambda2,prawd)#mutowanie populacji
    pop_r = create_r(pop_p,pop_o2,n,mi,lambda2)#generacja populacji R = P U T
    if zad == 1:#podpunkt a
        result = res_a(pop_r,mi,lambda2,tab,N)#wybor najlepszych fenotypow
    else:#podpunkt b
        result = res_b(pop_r,mi,lambda2,tab,N,i)#wybor najlepszych fenotypow
    new_best = result[0]
    if new_best == old_best:
        k = k+1
    else:
        k = 0
    pop_p = new_p(result,mi)#generacja nowej populacji P
    old_best = new_best

#for i in range(mi):
print(result[0])#wyswietl najlepszy wynik
print(i)
save_data(N,tab,result[0],i-k)#zapisz punkty do pliku