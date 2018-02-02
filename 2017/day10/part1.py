with open("input.txt") as f:
    lenghts = f.read().replace("\n","").split(",")

lenghts = list(map(int, lenghts))
l = list(range(256))
size = 256

skip = 0
position = 0

for k in lenghts:

    if (position+k)%size > position:
        l[position:position+k] = reversed(l[position:position+k])

    elif (position+k)%size < position: 
        aux = list(reversed(l[position:] + l[:(position+k)%size]))
        l[position:] = aux[:size-position]
        l[:(position+k)%size] = aux[size-position:] 
        
    position = (position+skip+k)%size
    skip += 1

print(l[0]*l[1])
