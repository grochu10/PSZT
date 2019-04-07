import random
import math
import pandas

def int_to_bin(a,n):
    b = ""
    for i in range(3):
        tmp = a[i]
        tmp = round(tmp,3)
        if i == 2:
            tmp = tmp*1024
        else:
            tmp = (tmp+2)*1024 
        tmp = round(tmp)
        tmp = format(tmp,"b")
        for j in range(n-len(tmp)):
            tmp = "0"+tmp
        b = b + tmp
    return b
        
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
            b[j] = float(b[j])/float(1024) - 2
        b[j] = round(b[j],3)
    return b

#funkcja do generowania populcji poczatkowej P
def generate_p(mi):
    n = 3
    p = [[0] * n for i in range(mi)]
    for i in range(mi):
        a = round(random.uniform(-2,2),3)
        b = round(random.uniform(-2,2),3)
        c = round(random.uniform(0,4),3)
        p[i][0] = a
        p[i][1] = b
        p[i][2] = c
    return p

def generate_t(lambda2,p,mi):
    t = []
    for i in range(lambda2):
        t.append(p[random.randint(0,mi-1)])
    return t

def create_o(t,n,lambda2):
    o = []
    for i in range(lambda2):
        a = int_to_bin(t[i],n)
        o.append(a)
    return o

def cross_o(o,n,lambda2,loci):
    o1 = [[0] * 3*n for i in range(lambda2)]
    locus = random.sample(range(1,3*n,1),loci)
    locus.sort()
    rand = random.sample(range(0,lambda2,1),lambda2)
    for i in range(0,lambda2,2):
        temp1 = ""
        temp2 = ""
        for k in range(loci+1):
            if k == 0:
                for j in range(0,locus[0],1):
                    temp1 = temp1 + o[rand[i]][j]
                    temp2 = temp2 + o[rand[i+1]][j]
            else:
                if k < loci:
                    if k%2 == 1: 
                        for j in range(locus[k-1],locus[k],1):
                            temp1 = temp1 + o[rand[i]][j]
                            temp2 = temp2 + o[rand[i+1]][j]
                    else:
                        for j in range(locus[k-1],locus[k],1):
                            temp2 = temp2 + o[rand[i]][j]
                            temp1 = temp1 + o[rand[i+1]][j]
                else:
                    if k%2 == 1: 
                        for j in range(locus[k-1],3*n,1):
                            temp1 = temp1 + o[rand[i]][j]
                            temp2 = temp2 + o[rand[i+1]][j]
                    else:
                        for j in range(locus[k-1],3*n,1):
                            temp2 = temp2 + o[rand[i]][j]
                            temp1 = temp1 + o[rand[i+1]][j]
        o1[i] = temp1
        o1[i+1] = temp2
    return o1

def x_men(o1,n,lambda2,prawd):
    o = ["" for i in range(lambda2)]
    for i in range(lambda2):
        for j in range(3*n):
            if rand(prawd) == 0:
                o[i] = o[i]+o1[i][j]
            else:
                if o1[i][j] == '0':
                    o[i] = o[i]+'1'
                else:
                    o[i] = o[i]+'0'
    return o

def rand(prawd):
    n = 100
    a = random.randint(0,n)
    if a <= n*prawd:
        return 1
    else:
        return 0


def create_r(p,o2,n,mi,lambda2):
    r =  [[0]*3 for i in range(mi+lambda2)]
    for i in range(lambda2+mi):
        if i < mi:
            r[i] = p[i]
        else:
            r[i] = bin_to_int(o2[i-mi],n)
    return r

def res(r,mi,lambda2,tab,N):
    r2 = [[0]*4 for i in range(mi+lambda2)]
    for i in range(mi+lambda2):
        e = 0
        for j in range(N):
            e = e+ pow(math.sqrt(pow(r[i][0]-tab[j][0],2) + pow(r[i][1]-tab[j][1],2)) - r[i][2],2)
        r2[i][0] = r[i][0]
        r2[i][1] = r[i][1]
        r2[i][2] = r[i][2]
        r2[i][3] = e
    r2.sort(key=lambda x: x[3])
    return r2

def new_p(res,mi):
    tab = [[0]*3 for i in range(mi)]
    for i in range(mi):
        tab[i][0] = res[i][0]
        tab[i][1] = res[i][1]
        tab[i][2] = res[i][2]
    return tab