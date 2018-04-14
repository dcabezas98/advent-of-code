from string import ascii_lowercase
from queue import Queue

with open("input.txt") as f:
    instructions = f.read()[:-1].split("\n")

registers = [{},{}]
for c in range(ord('a'), ord('z')+1):
    registers[0][chr(c)]=0
    registers[1][chr(c)]=0 + (c == ord('p'))

q = [Queue(), Queue()]
waiting = [False, False]
sent1 = 0
index = [0, 0]

def procede(identity):
    global sent1
    
    i = instructions[index[identity]].split(" ")
    
    if len(i) > 2:
        if i[2] in ascii_lowercase:
            n = registers[identity][i[2]]
        else:
            n = int(i[2])
                    
    if i[0] == 'set':
        registers[identity][i[1]] = n
                        
    elif i[0] == 'add':
        registers[identity][i[1]] += n
            
    elif i[0] == 'mul':
        registers[identity][i[1]] *= n

    elif i[0] == 'mod':
        registers[identity][i[1]] %= n

    elif i[0] == 'snd':
        q[abs(identity-1)].put(registers[identity][i[1]])
        waiting[abs(identity-1)] = False
        sent1 += identity

    elif i[0] == 'rcv':
           
        if q[identity].empty():
            waiting[identity] = True
            index[identity] -= 1
        else:
            registers[identity][i[1]] = q[identity].get()

    else:
        if i[1] in ascii_lowercase:
            if registers[identity][i[1]] > 0:
                index[identity] += n-1
        elif int(i[1]) > 0:
            index[identity] += n-1
            
    index[identity] +=1

while not(waiting[0] and waiting[1]):
    if not waiting[0]:
        procede(0)
    else:
        procede(1)

print(sent1)
