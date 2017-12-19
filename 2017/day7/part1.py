
programs = set()
nobottom = set()

with open("input.txt") as f:

    fl = f.read().split("\n")

    fl.pop()

    for line in fl:
        
        l = line.replace(",","").replace(" ->","").split(" ")

        programs.add(l[0])
        nobottom.update(set(l[2:]))

    bottom = programs - nobottom

    print(bottom)        
