
def manhattanDistance(a):
    d = 0
    for k in a:
        d += abs(k)

    return d

p = []
v = []
a = []

with open("input.txt") as f:
    for line in f:
        line = line[:-1].split(", ")
        p.append(list(map(int,line[0][3:-1].split(","))))
        v.append(list(map(int,line[1][3:-1].split(","))))
        a.append(list(map(int,line[2][3:-1].split(","))))

print(a.index(min(a,key=manhattanDistance)))
