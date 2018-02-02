programsLeft = set(range(2000))
pipes = []
connected = set()

def connectedTo(i):
    for j in pipes[i]:
        if j not in connected:
            connected.add(j)
            connectedTo(j)
            
with open("input.txt") as f:

    for line in f:
        line = line.replace("<-> ","").replace(",","").replace("\n","").split(" ")
        pipes.append(list(map(int,line[1:]))) 

groups = 0

while len(programsLeft) > 0:
    i = programsLeft.pop()
    connectedTo(i)
    programsLeft -= connected
    connected.clear()
    groups += 1

print(groups)
