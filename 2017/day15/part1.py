# Input:
prevA = 116
prevB = 299

factorA = 16807
factorB = 48271
divisor = 2147483647

judge = 0

for _ in range(40000000):

    A = (prevA*factorA)%divisor
    B = (prevB*factorB)%divisor
    prevA = A
    prevB = B

    binA = bin(A).split("b")[-1][-16:]
    binB = bin(B).split("b")[-1][-16:]
    binA = '0'*(16-len(binA))+binA
    binB = '0'*(16-len(binB))+binB
    
    if binA == binB:
        judge += 1

print(judge)
