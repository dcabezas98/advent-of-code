
from itertools import product

def div(l):

    #print(l)

    l = list(map(int,l))
    
    for i, j in product(l,l):

        if i != j:

            if i % j == 0:
                return i / j

            elif j % i == 0:
                return j / i
                
suma = 0

with open("input.txt") as f:

    for line in f:
        
        l = line.replace("\n","").split("\t")

        suma += div(l)

print(suma)

    
    
