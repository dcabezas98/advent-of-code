
regs = {}

with open("input.txt") as f:

    for line in f:

        l = line.replace("\n","").split(" ")

        if not l[0] in regs:
            regs[l[0]] = 0

        if l[4] in regs:

            reference = regs[l[4]]

        else:
           
            reference = 0

        s = l[5:]

        s.insert(0,str(reference))
        
        if eval(''.join(s)):

            if l[1] == 'inc':
            
                regs[l[0]] += int(l[2])

            else:
                regs[l[0]] -= int(l[2])

v = list(regs.values())

print(max(v))
