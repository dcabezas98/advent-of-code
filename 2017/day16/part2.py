programs = list(map(chr,range(ord('a'), ord('q'))))
start = programs.copy()

with open("input.txt") as f:

    dance = f.read()[:-1].split(',')

def lestDance():
    for move in dance:
        step = move[0]

        if step == 's':
            n = int(move[1:])
            aux = programs[:]
            programs[:n] = aux[-n:]
            programs[n:] = aux[:-n]        
        
        elif step == 'x':
            p = move[1:].split('/')
            p1 = int(p[0])
            p2 = int(p[1])
            programs[p1], programs[p2] = programs[p2], programs[p1]
        
        else:
            i = programs.index(move[1])
            j = programs.index(move[3])
            programs[i], programs[j] = programs[j], programs[i]

lestDance()
cycle = 1

while programs != start:
    cycle += 1
    lestDance()

rem = 1000000000%cycle

for _ in range(rem):
    lestDance()

programs = ''.join(programs)
print(programs)
