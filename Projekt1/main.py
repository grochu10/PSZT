#funkcja realizujaca rozwiazanie zadania
import random
import math
import pandas
from points import*
from fun import*
def main(zad,mi,lambda2,loci,prawd,N,tab):

    #inicjalizacja wartosci parametrow
    n = 10 # ilosc genow na reprezentacje pojedynczego x,y lub r
    k = 0
    old_best = [0,0,0,0]

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

    data = []
    for i in range(4):
        data.append(result[i])
    data.append(k)
    raw_data = {'data':data}
    df = pandas.DataFrame(raw_data,columns=['data'])
    df.to_excel("data.xlsx",sheet_name='data')