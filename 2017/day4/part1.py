
def valid(l):

    l.sort()
    
    v = True

    i = 0
    
    while i < len(l)-1 and v:
        if l[i] == l[i+1]:
            v = False
            
        i += 1

    return v

suma = 0

with open("input.txt") as f:

    for line in f:
        l = line.replace("\n","").split(" ")

        if valid(l):
            suma += 1
            
print(suma)
