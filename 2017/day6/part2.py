
configurations = []

cycles = 0

repeat = False

with open("input.txt") as f:

    l = f.read().replace('\n',"").split('\t')

    l = list(map(int,l))

    configurations.append(l[:])

    while not repeat:

        value = max(l)
        i = l.index(value)

        l[i] = 0

        while value:

            i += 1

            l[i%len(l)] += 1

            value -= 1

        if configurations.count(l):
            repeat = True
            cycle_first_appearance = configurations.index(l)

        else:
            configurations.append(l[:])

        cycles += 1

    print(cycles - cycle_first_appearance)
