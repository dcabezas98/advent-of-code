
tower = []

def findList(first): # Find a list of tower given his first element
    for s in tower:
        if s[0] == first:
            return s

def findWrong(bottom):

    l = findList(bottom)
    p = []
    wrong = ""
    weight = int(l[1])
    
    for i in range(2, len(l)):

        w, iswrong = findWrong(l[i])
        p.append(w)

        if iswrong != "":
            wrong = iswrong
            break

        weight += w

    if wrong == "" and len(p) > 1:

        equal = -1
        
        if p[0] == p[1]:
            equal = p[0]

        elif len(p) > 2 and p[0] == p[2]:
            equal = p[0]

        else:
            equal = p[1]

        if equal >= 0:
            for k in range(0, len(p)):
                if p[k] != equal:
                    wrong = l[k+2] # Find the program with wrong weight

                    variation = p[k] - equal

                    actualw = int(findList(wrong)[1])
                    correctw = actualw - variation 
                    print(correctw) # Correct weight of the program
                    break            

    return weight, wrong # The weight over the program and the name of the program that is wrong

with open("input.txt") as f:

    fl = f.read().split("\n")
    fl.pop()

    for line in fl:
        l = line.replace(",","").replace(" ->","").replace("(","").replace(")","").split(" ")
        tower.append(l)

findWrong("mkxke") # Find the program with wrong weight
