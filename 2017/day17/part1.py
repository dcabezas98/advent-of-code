steps = 363

buffer = [0]
currentValue = 1
currentPosition = 0

for i in range(1, 2018):
    currentPosition = (currentPosition+steps)%len(buffer)
    buffer.insert(currentPosition+1, currentValue)
    currentValue += 1
    currentPosition += 1

print(buffer[(currentPosition+1)%len(buffer)])
