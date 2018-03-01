steps = 363

buffer = [0]
lenght = 1
currentValue = 1
currentPosition = 0

after0 = int()
pos0 = 0

for i in range(1, 50000001):
    currentPosition = (currentPosition+steps)%lenght
    lenght += 1

    if currentPosition == pos0:
        after0 = currentValue

    elif currentPosition == (pos0-1)%lenght:
        pos0 += 1

    currentValue += 1
    currentPosition += 1

print(after0)
