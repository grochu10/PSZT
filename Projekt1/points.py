#plik zawierajacy funkcje do generacji i zapisu punktow
import random
import pandas

#funkacja do generacji punktow do podpunktu a
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

#funkcja zapisujaca punkty i wyniki do pliku formatu xlsx
def save_data(N,tab,res,k):
    x = []
    y = []
    data = []
    for i in range(N):
        x.append(tab[i][0])
        y.append(tab[i][1])
    for i in range(4):
        data.append(res[i])
    data.append(k)
    raw_data = {'x' :x,'y' :y}
    df = pandas.DataFrame(raw_data,columns=['x','y'])
    df.to_excel("dane.xlsx",sheet_name='dane')
    raw_data2 = {'data':data}
    df = pandas.DataFrame(raw_data2,columns=['data'])
    df.to_excel("data.xlsx",sheet_name='data')