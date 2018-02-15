toAdd = [17, 31, 73, 47, 23]
size = 256

used = 0

with open("input.txt") as f:
    key = f.read().replace('\n','')

for i in range(128):
    data = '-'.join([key, str(i)])

    lenghts = [ord(c) for c in data]
    lenghts += toAdd
    l = list(range(256))

    skip = 0
    position = 0

    for _ in range(64):
        for k in lenghts:
            
            if (position+k)%size > position:
                l[position:position+k] = reversed(l[position:position+k])

            elif (position+k)%size < position: 
                aux = list(reversed(l[position:] + l[:(position+k)%size]))
                l[position:] = aux[:size-position]
                l[:(position+k)%size] = aux[size-position:] 
        
            position = (position+skip+k)%size
            skip += 1

    dense = 16*[0]

    for i in range(16):
        for j in range(16):
            dense[i] ^= l[16*i+j]

    for i in range(len(dense)):
        dense[i] = hex(dense[i]).split('x')[-1]
        if len(dense[i]) == 1:
            dense[i] = ''.join(['0',dense[i]])
    
    knot = ''.join(dense)
    used += bin(int(knot, 16)).count('1')

print(used)
