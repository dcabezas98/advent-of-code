with open("input.txt") as f:
    direction = list(f.read().replace("\n",""))

floor = 0

for i in range(len(direction)):
    if direction[i] == "(":
        floor += 1

    elif direction[i] == ")":
        floor -= 1

    if floor < 0:
        position = i+1
        break

print(position)
