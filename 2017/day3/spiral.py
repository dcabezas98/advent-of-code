
n = 361527

r1 = 8
r2 = 0

k = 1
i = 0

while k < n:
    r2 += r1
    k += r2
    i += 2

c1 = k
c2 = c1 - i
c3 = c2 - i 
c4 = c3 - i

d = min(map(abs,(n - c1, n - c2, n - c3, n - c4)))

print(i - d)
