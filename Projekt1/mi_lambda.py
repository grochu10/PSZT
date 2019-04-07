import random
import math
import pandas
from fun import*
from points import*

mi = 20
lambda2 = 7*mi
loci = 4
prawd = 0.1
n = 12
N = 10

tab = rand_points(N)
pop_p = generate_p(mi)

for i in range(200):
    pop_t = generate_t(lambda2,pop_p,mi)
    pop_o = create_o(pop_t,n,lambda2)
    pop_o1 = cross_o(pop_o,n,lambda2,loci)
    pop_o2 = x_men(pop_o1,n,lambda2,prawd)
    pop_r = create_r(pop_p,pop_o2,n,mi,lambda2)
    result = res(pop_r,mi,lambda2,tab,N)
    pop_p = new_p(result,mi)

print(result[0])
save_points(N,tab)