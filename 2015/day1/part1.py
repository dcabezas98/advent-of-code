with open("input.txt") as f:
    direction = list(f.read().replace("\n",""))

floor = 0

for i in direction:
    if i == "(":
        floor += 1

    elif i == ")":
        floor -= 1

print(floor)
