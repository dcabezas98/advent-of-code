p = []
v = []
a = []

with open("input.txt") as f:
    for line in f:
        line = line[:-1].split(", ")
        p.append(list(map(int,line[0][3:-1].split(","))))
        v.append(list(map(int,line[1][3:-1].split(","))))
        a.append(list(map(int,line[2][3:-1].split(","))))

def resolveCollisions():
    for pos in p:
        indexes = [i for i, x in enumerate(p) if x == pos]
        if len(indexes) > 1:
            #print(len(indexes), "particles collided")
            for k in indexes[::-1]:
                p.pop(k)
                v.pop(k)
                a.pop(k)

for _ in range(100): # More iterations may be needed
    
    resolveCollisions()
    for i in range(len(p)):
        for k in range(3):
            v[i][k]+=a[i][k]
            p[i][k]+=v[i][k]    

print(len(p))
