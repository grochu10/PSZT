#plik zawierajacy funkcje wykorzystywane w projekcie
import random
import math
import pandas

#funkcja zamieniajaca wartosci liczbowe x,y,r na ciag bitow(genow)
def int_to_bin(a,n):
    b = ""
    for i in range(3):
        tmp = a[i]
        tmp = round(tmp,3)
        if i == 2:#zamiana promienia
            tmp = tmp*1024
        else:#zamiana x,y
            tmp = (tmp+pow(2,n)/2048)*1024 
        tmp = round(tmp)
        tmp = format(tmp,"b")
        for j in range(n-len(tmp)):
            tmp = "0"+tmp
        b = b + tmp
    return b

#funkcja zamieniajaca ciag bitow(genow) na tablice wartosci liczbowych x,y,r
def bin_to_int(a,n):
    b = []
    for j in range(3):
        b.append("")
        for i in range(n):
            b[j] = b[j] + a[i*(j+1)]
        b[j] = int(b[j],2)
        if j == 2:
            b[j] = float(b[j])/float(1024)
        else:
            b[j] = float(b[j])/float(1024) - pow(2,n)/2048
        b[j] = round(b[j],3)
    return b

#funkcja do generowania populcji poczatkowej P
def generate_p(mi,n):
    m = 3
    p = [[0] * m for i in range(mi)]
    for i in range(mi):
        a = round(random.uniform(-pow(2,n)/2048,pow(2,n)/2048),3)#losowanie z zadanego przedzialu
        b = round(random.uniform(-pow(2,n)/2048,pow(2,n)/2048),3)
        c = round(random.uniform(0,pow(2,n)/1024),3)
        p[i][0] = a
        p[i][1] = b
        p[i][2] = c
    return p

#funkcja do generowania populacji T
def generate_t(lambda2,p,mi):
    t = []
    for i in range(lambda2):
        t.append(p[random.randint(0,mi-1)])
    return t

#funkcja do realizujaca utworzenie genotypow osobnikow z popolacji T
def create_o(t,n,lambda2):
    o = []
    for i in range(lambda2):
        a = int_to_bin(t[i],n)
        o.append(a)
    return o

#funkcja realizujaca krzyzowanie genotypow
def cross_o(o,n,lambda2,loci):
    o1 = [[0] * 3*n for i in range(lambda2)]
    locus = random.sample(range(1,3*n,1),loci)#losowanie loci
    locus.sort()
    rand = random.sample(range(0,lambda2,1),lambda2)
    for i in range(0,lambda2,2):
        temp1 = ""
        temp2 = ""
        for k in range(loci+1):#krzyzowanie
            if k == 0:
                for j in range(0,locus[0],1):
                    temp1 = temp1 + o[rand[i]][j]
                    temp2 = temp2 + o[rand[i+1]][j]
            else:
                if k < loci:
                    if k%2 == 1:#gdy bierzemy locus o nieparzystym indeksie w tablicy 
                        for j in range(locus[k-1],locus[k],1):
                            temp1 = temp1 + o[rand[i]][j]
                            temp2 = temp2 + o[rand[i+1]][j]
                    else:#gdy bierzemy locus o parzystym indeksie w tablicy 
                        for j in range(locus[k-1],locus[k],1):
                            temp2 = temp2 + o[rand[i]][j]
                            temp1 = temp1 + o[rand[i+1]][j]
                else:#ostani locus
                    if k%2 == 1: #gdy indeks locus nieparzysty
                        for j in range(locus[k-1],3*n,1):
                            temp1 = temp1 + o[rand[i]][j]
                            temp2 = temp2 + o[rand[i+1]][j]
                    else:#gdy indeks locus parzysty
                        for j in range(locus[k-1],3*n,1):
                            temp2 = temp2 + o[rand[i]][j]
                            temp1 = temp1 + o[rand[i+1]][j]
        o1[i] = temp1
        o1[i+1] = temp2
    return o1

#funkcja realizujace mutacje genotypow
def x_men(o1,n,lambda2,prawd):
    o = ["" for i in range(lambda2)]
    for i in range(lambda2):
        for j in range(3*n):
            if mut(prawd) == 0:#liczenie prawdopodobienstwa mutacji
                o[i] = o[i]+o1[i][j]
            else:
                if o1[i][j] == '0':
                    o[i] = o[i]+'1'
                else:
                    o[i] = o[i]+'0'
    return o

#funkcja wyliczajaca czy dany gen przejdzie mutacje
def mut(prawd):
    n = 100
    a = random.randint(0,n)
    if a <= n*prawd:
        return 1
    else:
        return 0

#funkcja do generacji populacji R = P U T
def create_r(p,o2,n,mi,lambda2):
    r =  [[0]*3 for i in range(mi+lambda2)]
    for i in range(lambda2+mi):
        if i < mi:
            r[i] = p[i]#populacja P
        else:
            r[i] = bin_to_int(o2[i-mi],n)#populacja R
    return r

#obliczenie wyniku i ocena fenotypow populacji R(podpunkt a)
def res_a(r,mi,lambda2,tab,N):
    r2 = [[0]*4 for i in range(mi+lambda2)]
    for i in range(mi+lambda2):
        e = 0
        for j in range(N):#liczenie bledu dla wszystkich punktow
            e = e+ pow(math.sqrt(pow(r[i][0]-tab[j][0],2) + pow(r[i][1]-tab[j][1],2)) - r[i][2],2)
        r2[i][0] = r[i][0]
        r2[i][1] = r[i][1]
        r2[i][2] = r[i][2]
        r2[i][3] = e
    r2.sort(key=lambda x: x[3])#sortowanie po wartosci bledu
    return r2

#obliczenie wyniku i ocena fenotypow populacji R(podpunkt b)
def res_b(r,mi,lambda2,tab,N,g):
    r2 = [[0]*4 for i in range(mi+lambda2)]
    for i in range(mi+lambda2):
        e = 0
        for j in range(N):
            a = pow(tab[j][0]-r[i][0],2) + pow(tab[j][1]-r[i][1],2)
            if a > pow(r[i][2],2):#czy punkt zawiera sie w okregu
                e = e+1
        r2[i][0] = r[i][0]
        r2[i][1] = r[i][1]
        r2[i][2] = r[i][2]
        r2[i][3] = e
    r2.sort(key=lambda x: x[3])
    k = 0
    for i in range(mi+lambda2):#wybor najlepszych spelniajacych warunek o zawieraniu punktow
        if r2[i][3] == 0:
            k = k+1
    r3 = [[0]*4 for i in range(k)]
    for i in range(k):
        r3[i][0] = r2[i][0]
        r3[i][1] = r2[i][1]
        r3[i][2] = r2[i][2]
        r3[i][3] = r2[i][3]
    r3.sort(key=lambda x: x[2])
    for i in range(k):
        r2[i][0] = r3[i][0]
        r2[i][1] = r3[i][1]
        r2[i][2] = r3[i][2]
        r2[i][3] = r3[i][3]
    return r2

#generacja nowej populacji R
def new_p(res,mi):
    tab = [[0]*3 for i in range(mi)]
    for i in range(mi):
        tab[i][0] = res[i][0]
        tab[i][1] = res[i][1]
        tab[i][2] = res[i][2]
    return tab