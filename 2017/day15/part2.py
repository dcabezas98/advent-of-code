# Input:
prevA = 116
prevB = 299

factorA = 16807
factorB = 48271
divisor = 2147483647

judge = 0

for _ in range(5000000):

    A = (prevA*factorA)%divisor
    prevA = A

    while A%4:
        A = (prevA*factorA)%divisor
        prevA = A
        
    B = (prevB*factorB)%divisor
    prevB = B

    while B%8:
        B = (prevB*factorB)%divisor
        prevB = B

    binA = bin(A).split("b")[-1][-16:]
    binB = bin(B).split("b")[-1][-16:]
    binA = '0'*(16-len(binA))+binA
    binB = '0'*(16-len(binB))+binB
    
    if binA == binB:
        judge += 1

print(judge)
