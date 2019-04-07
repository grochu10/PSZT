import random
import pandas

def rand_points(N):
    tab = [[0] * 2 for i in range(N)]
    for i in range(N):
        a = random.random()
        a = round(a,3)
        tab[i][0] = a
        b = random.random()
        b = round(b,3)
        tab[i][1] = b
    return tab

def save_points(N,tab):
    x = []
    y = []
    for i in range(N):
        x.append(tab[i][0])
        y.append(tab[i][1])
    raw_data = {'x' :x,'y' :y}
    df = pandas.DataFrame(raw_data,columns=['x','y'])
    df.to_excel("dane.xlsx",sheet_name='dane')