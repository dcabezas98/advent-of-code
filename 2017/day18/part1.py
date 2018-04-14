from string import ascii_lowercase

registers = {}
freqLastSoundPlayed = int()

with open("input.txt") as f:
    instructions = f.read()[:-1].split("\n")

index = 0
while True:
    i = instructions[index].split(" ")

    if not i[1] in registers:
        registers[i[1]] = 0

    if len(i) > 2:
        if i[2] in ascii_lowercase:
            n = registers[i[2]]
        else:
            n = int(i[2])

    if i[0] == 'set':
        registers[i[1]] = n

    elif i[0] == 'add':
        registers[i[1]] += n

    elif i[0] == 'mul':
        registers[i[1]] *= n

    elif i[0] == 'mod':
        registers[i[1]] %= n

    elif i[0] == 'snd':
        freqLastSoundPlayed = registers[i[1]]

    elif i[0] == 'rcv':
        if registers[i[1]]:
            break

    else:
        if registers[i[1]] > 0:
            index += n-1

    index +=1
    
print(freqLastSoundPlayed)
        
