def position(pic, r):
    pic = pic%(2*(r-1))

    if pic < r:
        return pic+1

    else:
        return 2*r-pic-1
    
severity = 0

with open("input.txt") as f:
    
    for line in f:
        line = list(map(int,line.replace("\n","").split(": ")))

        if position(line[0], line[1]) == 1:
            severity += line[0]*line[1]

print(severity)
