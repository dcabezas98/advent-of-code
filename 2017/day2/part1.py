
def min_max(l):
    
    max_ = min_ = int(l[0])

    for i in l:
        if int(i) < min_:
            min_ = int(i)

        if int(i) > max_:
            max_ = int(i)

    return min_, max_

suma = 0

with open("input.txt") as f:

    for line in f:
        l = line.split("\t")

        min_, max_ = min_max(l)
        
        dif = max_ - min_

        suma += dif


print(suma)

    
    
