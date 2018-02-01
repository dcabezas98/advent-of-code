with open("input.txt") as f:
    stream = f.read()

total = 0
deep = 0
garbage = False

i = 0
l = len(stream)

while i < l:    

    c = stream[i]
    
    if c == "!":
        i += 1

    elif garbage == True:
        if c == ">":
            garbage = False

    elif c == "{":
        deep += 1

    elif c == "}":
        total += deep
        deep -= 1

    elif c == "<":
        garbage = True

    i += 1

print(total)
