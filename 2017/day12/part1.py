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

connectedTo(0)

print(len(connected))
