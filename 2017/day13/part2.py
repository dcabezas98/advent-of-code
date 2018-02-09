def position(pic, r):
    pic = pic%(2*(r-1))

    if pic < r:
        return pic+1

    else:
        return 2*r-pic-1

l = []
with open("input.txt") as f:
    
    for line in f:
        l.append(list(map(int,line.replace("\n","").split(": "))))


delay = 0
cought = True

while cought:

    cought = False
    
    for layer in l:
        if position(layer[0]+delay, layer[1]) == 1:
            cought = True
            delay += 1
            break

print(delay)
